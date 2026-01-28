# ⚙️ Git 기본 설정 명령어

> INTCOL 정보 기반 핵심 명령어 모음

---

## 🚀 필수 초기 설정 (3단계)

```bash
# 1. 사용자 이름 설정
git config --global user.name "여러분의 이름"

# 2. 이메일 설정
git config --global user.email "여러분의이메일@example.com"

# 3. 기본 브랜치 이름 설정
git config --global init.defaultBranch main
```

---

## 🖊️ 편집기 설정

### Windows
```bash
# VS Code
git config --global core.editor "code --wait"

# Notepad++ (64비트)
git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"
```

### Mac/Linux
```bash
# VS Code
git config --global core.editor "code --wait"
```

---

## ✅ 설정 확인 명령어

```bash
# 모든 설정 보기
git config --list

# 설정 출처 포함해서 보기
git config --list --show-origin

# 특정 설정값만 확인
git config user.name
git config user.email
```

---

## 🔧 설정 수정/삭제

```bash
# 설정 변경 (같은 명령어 재실행)
git config --global user.name "새이름"

# 설정 삭제
git config --global --unset user.name

# 설정 파일 직접 편집
git config --global --edit
```

---

## 📊 설정 레벨별 명령어

| 레벨 | 옵션 | 적용 범위 |
|------|------|----------|
| 시스템 | `--system` | 모든 사용자 |
| 사용자 | `--global` | 현재 사용자 전체 |
| 프로젝트 | `--local` 또는 생략 | 현재 프로젝트만 |

```bash
# 프로젝트별 다른 설정 적용
git config user.email "work@company.com"
```

---

> 📍 **출처**: INTCOL/AI/Git/git_initial_setup.md, git_config_files.md
