"""
Google Drive 운영 백업 정보 다운로드 스크립트
===========================================
이 스크립트를 로컬 PC에서 실행하세요.

사용법:
  python download_gdrive_backup.py

필요 패키지:
  pip install google-api-python-client google-auth google-auth-oauthlib

token.json 파일이 같은 디렉토리에 있어야 합니다.
"""

import os
import json
import io
import sys
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

TOKEN_PATH = r"C:\Users\Administrator\Desktop\나스미디어_김진곤\nap 논리워드\클러드코드\트래픽최적화(클러드코드용)\credentials\token.json"
FOLDER_ID = "1K2xOXezyz_mmma2O9TMRowcqzQKSs1bM"
OUTPUT_DIR = "gdrive_backup_output"

SCOPES = ["https://www.googleapis.com/auth/drive"]


def get_credentials():
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_PATH, "w") as f:
            f.write(creds.to_json())
    return creds


def list_files_recursive(drive, folder_id, path=""):
    """폴더 내 모든 파일을 재귀적으로 조회"""
    all_files = []
    query = f"'{folder_id}' in parents and trashed=false"
    results = drive.files().list(
        q=query,
        fields="files(id, name, mimeType, size, modifiedTime)",
        pageSize=1000,
    ).execute()

    for f in results.get("files", []):
        full_path = os.path.join(path, f["name"]) if path else f["name"]
        if f["mimeType"] == "application/vnd.google-apps.folder":
            print(f"  [DIR] {full_path}/")
            all_files.append({"type": "folder", "path": full_path, **f})
            all_files.extend(list_files_recursive(drive, f["id"], full_path))
        else:
            size = f.get("size", "N/A")
            print(f"  [FILE] {full_path}  ({size} bytes)")
            all_files.append({"type": "file", "path": full_path, **f})

    return all_files


def download_file(drive, file_info, output_dir):
    """파일 다운로드 (Google Docs는 export)"""
    file_id = file_info["id"]
    mime = file_info["mimeType"]
    name = file_info["name"]

    # Google Docs 형식 → export
    export_map = {
        "application/vnd.google-apps.spreadsheet": (
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            ".xlsx",
        ),
        "application/vnd.google-apps.document": (
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            ".docx",
        ),
        "application/vnd.google-apps.presentation": (
            "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            ".pptx",
        ),
    }

    rel_path = file_info["path"]
    out_path = os.path.join(output_dir, rel_path)
    os.makedirs(os.path.dirname(out_path) if os.path.dirname(out_path) else output_dir, exist_ok=True)

    try:
        if mime in export_map:
            export_mime, ext = export_map[mime]
            if not out_path.endswith(ext):
                out_path += ext
            request = drive.files().export_media(fileId=file_id, mimeType=export_mime)
        else:
            request = drive.files().get_media(fileId=file_id)

        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()

        with open(out_path, "wb") as f:
            f.write(fh.getvalue())

        print(f"  ✓ {out_path} ({len(fh.getvalue())} bytes)")
        return out_path

    except Exception as e:
        print(f"  ✗ {name}: {e}")
        return None


def read_text_content(filepath):
    """텍스트 파일 내용 읽기"""
    text_exts = {".txt", ".json", ".csv", ".md", ".yaml", ".yml", ".xml", ".html", ".py", ".js", ".ts", ".sql", ".log", ".conf", ".cfg", ".ini", ".env", ".sh"}
    ext = os.path.splitext(filepath)[1].lower()

    if ext in text_exts:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return f.read()
        except Exception:
            try:
                with open(filepath, "r", encoding="cp949") as f:
                    return f.read()
            except Exception:
                return None
    return None


def main():
    print("=" * 60)
    print("Google Drive 운영 백업 정보 다운로드")
    print("=" * 60)

    creds = get_credentials()
    drive = build("drive", "v3", credentials=creds)

    about = drive.about().get(fields="user").execute()
    print(f"\n연결 성공: {about['user']['emailAddress']}")

    print(f"\n폴더 ID: {FOLDER_ID}")
    print("파일 목록 조회 중...\n")

    files = list_files_recursive(drive, FOLDER_ID)

    print(f"\n총 {len(files)}개 항목 발견")
    print(f"\n{'=' * 60}")
    print("파일 다운로드 중...\n")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    downloaded = []
    for f in files:
        if f["type"] == "file":
            result = download_file(drive, f, OUTPUT_DIR)
            if result:
                downloaded.append(result)

    # 텍스트 파일 내용을 JSON으로 출력
    print(f"\n{'=' * 60}")
    print("텍스트 파일 내용 추출 중...\n")

    content_output = {}
    for filepath in downloaded:
        content = read_text_content(filepath)
        if content:
            rel = os.path.relpath(filepath, OUTPUT_DIR)
            content_output[rel] = content
            print(f"  텍스트 추출: {rel} ({len(content)} chars)")

    # 결과를 JSON 파일로 저장
    output_json = os.path.join(OUTPUT_DIR, "_backup_contents.json")
    summary = {
        "folder_id": FOLDER_ID,
        "total_files": len(files),
        "downloaded": len(downloaded),
        "file_list": [
            {
                "path": f["path"],
                "type": f["type"],
                "mimeType": f.get("mimeType", ""),
                "size": f.get("size", "N/A"),
                "modifiedTime": f.get("modifiedTime", ""),
            }
            for f in files
        ],
        "text_contents": content_output,
    }

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f"\n{'=' * 60}")
    print(f"다운로드 완료!")
    print(f"  다운로드 폴더: {os.path.abspath(OUTPUT_DIR)}")
    print(f"  요약 JSON: {os.path.abspath(output_json)}")
    print(f"\n아래 파일의 내용을 Claude Code 채팅에 붙여넣어 주세요:")
    print(f"  → {os.path.abspath(output_json)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
