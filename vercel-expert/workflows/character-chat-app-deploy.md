# 🚀 character-chat-app Vercel 배포 가이드

> 배포 일시: 2026-01-28 23:24 ~ 23:29 (약 5분)

---

## 📋 개요

| 항목 | 내용 |
|------|------|
| **프로젝트** | character-chat-app |
| **프레임워크** | Next.js 16.1.4 |
| **배포 플랫폼** | Vercel |
| **배포 URL** | https://character-chat-app-five.vercel.app |

---

## ⚡ 핵심 명령어 (3단계)

```bash
# 1️⃣ 빌드 테스트
npm run build

# 2️⃣ GitHub Push
git add .
git commit -m "Prepare for Vercel deployment"
git push origin main

# 3️⃣ Vercel 배포
npx -y vercel --prod --yes
```

---

## 📂 프로젝트 구조

```
character-chat-app/
├── src/                    # 소스 코드
├── public/                 # 정적 파일
├── .env.local             # 환경 변수 (로컬)
├── .env.local.example     # 환경 변수 예시
├── .gitignore             # Git 제외 파일
├── package.json           # 의존성 정의
├── next.config.ts         # Next.js 설정
└── tsconfig.json          # TypeScript 설정
```

---

## 🔐 환경 변수

```bash
# Supabase
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key

# OpenRouter
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_DEFAULT_MODEL=anthropic/claude-3.5-sonnet

# App
NEXT_PUBLIC_APP_URL=https://character-chat-app-five.vercel.app
```

---

## 📝 배포 과정 상세

### Step 1: 빌드 테스트
```bash
> npm run build

▲ Next.js 16.1.4 (Turbopack)
✓ Collecting page data in 1939.9ms
✓ Generating static pages (8/8) in 542.8ms
✓ Finalizing page optimization in 12.8ms

Route (app)
├ ○ /                    # 메인 페이지 (Static)
├ ○ /chat               # 채팅 목록 (Static)
├ ƒ /chat/[characterId] # 개별 채팅 (Dynamic)
├ ○ /chat/group         # 그룹 채팅 (Static)
└ ○ /chat/spectate      # 관전 모드 (Static)
```

### Step 2: GitHub Push
```bash
> git add .
> git commit -m "Prepare for Vercel deployment"
[main 137b11f] Prepare for Vercel deployment
 2 files changed, 14 insertions(+)

> git push origin main
Enumerating objects: 7, done.
Writing objects: 100% (4/4), 543 bytes
   b9d920a..137b11f  main -> main
```

### Step 3: Vercel 배포
```bash
> npx -y vercel --prod --yes

Vercel CLI 50.8.1
✅ Production: https://character-chat-app-five.vercel.app [41s]
```

---

## ✅ 배포 검증 결과

```
Title: Character Universe

# Character Universe
## 🏠 거실
- 민수: 야 오늘 날씨 개좋다ㅋㅋㅋ 어디 갈까?
- 하나: 카페 어때? 새로 생긴 곳 있던데~!
- 유진: 좋아. 작업하기도 좋을 것 같아.

## 캐릭터 (8명)
민수, 유진, 하나, 소라, 리나, 미카, 준, 유키
```

---

## 🔄 자동 배포 설정

배포 완료 후, GitHub에 Push하면 자동으로 재배포됩니다:

```bash
git add .
git commit -m "변경 내용"
git push origin main
# → 자동 배포! 🚀
```

---

## ⚠️ 주의사항

1. **환경 변수**: Vercel 대시보드에서 별도 설정 필요
2. **Hobby 플랜**: 상업적 이용 불가 (광고, 쇼핑몰 등)
3. **빌드 실패 시**: 로컬에서 `npm run build` 먼저 테스트

---

## 🔗 관련 링크

- **배포 URL**: https://character-chat-app-five.vercel.app
- **GitHub**: https://github.com/Jingon-kim/character-chat-app
- **Vercel 대시보드**: https://vercel.com
