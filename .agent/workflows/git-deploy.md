---
description: Git 커밋 및 GitHub Push 자동 실행 (보안 검토 포함)
---

# Git 배포 워크플로우

// turbo-all

## 변경사항 커밋 및 Push
1. 변경사항 스테이징: `git add .`
2. 커밋 생성: `git commit -m "커밋메시지"`
3. GitHub Push: `git push`
4. 🔐 **보안 검토**: `@security-expert` 에이전트가 배포 전 보안 체크리스트 확인

## 새 저장소 초기화
1. Git 초기화: `git init`
2. 파일 추가: `git add .`
3. 첫 커밋: `git commit -m "Initial commit"`
4. 원격 저장소 연결: `git remote add origin [URL]`
5. Push: `git push -u origin main`
6. 🔐 **보안 검토**: `@security-expert` 에이전트가 배포 전 보안 체크리스트 확인

---

## 🔐 보안 체크리스트 (배포 전 필수)

`security-expert` 에이전트가 다음 항목을 검토합니다:

### 코드 보안
- [ ] 민감 정보(API 키, 비밀번호) 노출 여부
- [ ] .env 파일 커밋 제외 확인
- [ ] 하드코딩된 시크릿 없음

### 의존성 보안
- [ ] 취약한 패키지 확인 (`npm audit` / `pip audit`)
- [ ] 라이센스 충돌 없음

### 설정 보안
- [ ] HTTPS 강제 적용
- [ ] 보안 헤더 설정
- [ ] CORS 정책 확인
