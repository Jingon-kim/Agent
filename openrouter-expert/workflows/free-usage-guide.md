# 🆓 OpenRouter 무료 사용 완벽 워크플로우

> 비용 $0으로 AI 서비스 이용하기

---

## 📋 전체 프로세스

```
┌─────────────────────────────────────────────────┐
│  1. 계정 생성     →  openrouter.ai 회원가입      │
├─────────────────────────────────────────────────┤
│  2. API 키 생성   →  Credit Limit $0 설정 필수!  │
├─────────────────────────────────────────────────┤
│  3. 환경 설정     →  환경 변수에 API 키 저장     │
├─────────────────────────────────────────────────┤
│  4. 무료 모델 사용 →  :free 접미사 모델만 사용    │
├─────────────────────────────────────────────────┤
│  5. 사용량 관리   →  일 50회, 분 20회 준수       │
└─────────────────────────────────────────────────┘
```

---

## 1️⃣ 계정 생성

### 단계별 가이드
```
1. https://openrouter.ai 접속
2. 우측 상단 "Sign Up" 클릭
3. 가입 방법 선택:
   - 이메일 가입 (권장)
   - Google 계정 연동
   - MetaMask 지갑 연동
4. 이메일 인증 완료
```

### 체크리스트
- [ ] 웹사이트 접속
- [ ] 회원가입 완료
- [ ] 이메일 인증 완료

---

## 2️⃣ API 키 생성 (핵심!)

### 단계별 가이드
```
1. 로그인 후 프로필 아이콘 클릭
2. "Keys" 또는 "API Keys" 메뉴 선택
3. "Create Key" 버튼 클릭
4. 설정:
   - Name: my-free-key (자유롭게)
   - Credit Limit: $0 ← 필수! 과금 차단!
5. "Create" 클릭
6. 키 복사 후 안전하게 저장
```

### ⚠️ 중요 주의사항
```
┌──────────────────────────────────────────────┐
│  API 키는 한 번만 표시됩니다!                  │
│  반드시 복사해서 안전한 곳에 저장하세요!        │
│                                              │
│  형식: sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxx      │
└──────────────────────────────────────────────┘
```

### Credit Limit 설정 (과금 방지 핵심)
```
⭐ Credit Limit을 $0으로 설정하면:
   - 무료 모델: 정상 작동
   - 유료 모델: 자동 차단 (에러 발생)
   - 실수로 유료 모델 호출해도 과금 없음!
```

### 체크리스트
- [ ] API 키 생성
- [ ] Credit Limit $0 설정
- [ ] 키 안전하게 저장

---

## 3️⃣ 환경 설정

### Windows (PowerShell)
```powershell
# 임시 설정 (현재 세션만)
$env:OPENROUTER_API_KEY="sk-or-v1-your-key-here"

# 영구 설정 (사용자 환경 변수)
[Environment]::SetEnvironmentVariable("OPENROUTER_API_KEY", "sk-or-v1-your-key-here", "User")
```

### Windows (CMD)
```cmd
# 임시 설정
set OPENROUTER_API_KEY=sk-or-v1-your-key-here

# 영구 설정 (시스템 환경 변수로 추가)
setx OPENROUTER_API_KEY "sk-or-v1-your-key-here"
```

### Linux / Mac
```bash
# 임시 설정
export OPENROUTER_API_KEY="sk-or-v1-your-key-here"

# 영구 설정 (~/.bashrc 또는 ~/.zshrc에 추가)
echo 'export OPENROUTER_API_KEY="sk-or-v1-your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### 체크리스트
- [ ] 환경 변수 설정 완료
- [ ] 터미널 재시작 후 확인

---

## 4️⃣ 무료 모델 사용

### 추천 무료 모델
| 모델 | 용도 | 특징 |
|------|------|------|
| `meta-llama/llama-3.1-8b-instruct:free` | 범용 | 가장 추천, 높은 성능 |
| `google/gemma-2-9b-it:free` | 경량 작업 | 빠른 응답 |

### 기본 코드 템플릿
```python
import os
from openai import OpenAI

# 클라이언트 설정
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# 무료 모델로 요청
response = client.chat.completions.create(
    model="meta-llama/llama-3.1-8b-instruct:free",  # :free 필수!
    messages=[
        {"role": "system", "content": "한국어로 답변해주세요."},
        {"role": "user", "content": "안녕하세요!"}
    ]
)

print(response.choices[0].message.content)
```

### 체크리스트
- [ ] 무료 모델 (:free) 선택
- [ ] 테스트 API 호출 성공

---

## 5️⃣ 사용량 관리

### 무료 플랜 한도
```
┌────────────────────────────────┐
│  일일 요청: 50회              │
│  분당 요청: 20회              │
│  모델 수: 25개 이상           │
│  비용: $0                     │
└────────────────────────────────┘
```

### 효율적 사용 전략
```
📊 일일 50회 배분 예시:

시간대       │ 배분  │ 용도
───────────┼──────┼─────────────
09:00~12:00│ 15회 │ 중요 작업
12:00~14:00│  5회 │ 가벼운 질문
14:00~18:00│ 20회 │ 메인 작업
18:00~22:00│ 10회 │ 마무리/학습
```

### 요청 횟수 절약 팁
```
✅ 프롬프트를 충분히 다듬어서 한 번에 원하는 결과 얻기
✅ 시스템 프롬프트로 답변 방향 명확히 지정
✅ 불필요한 테스트 요청 최소화
✅ 결과를 로컬에 저장해서 재사용
```

### 체크리스트
- [ ] 일일 사용량 모니터링
- [ ] 사용 패턴 최적화

---

## ✅ 최종 체크리스트

```
[ ] 1. OpenRouter 계정 생성 완료
[ ] 2. 이메일 인증 완료
[ ] 3. API 키 생성 완료
[ ] 4. Credit Limit $0 설정 완료
[ ] 5. 환경 변수 설정 완료
[ ] 6. 테스트 API 호출 성공
[ ] 7. 무료 모델 (:free) 사용 확인
```

---

## 🚨 문제 해결

### 에러: 401 Unauthorized
```
원인: API 키가 잘못됨
해결:
1. 환경 변수 확인
2. API 키 유효성 확인
3. 키 재생성
```

### 에러: 429 Too Many Requests
```
원인: Rate Limit 초과
해결:
1. 잠시 대기 (1-2분)
2. 요청 간격 늘리기
3. 일일 한도 확인
```

### 에러: Model not found
```
원인: 모델명 오류
해결:
1. :free 접미사 확인
2. 모델명 정확히 입력
3. openrouter.ai/models 에서 확인
```

---

> 💡 **핵심**: Credit Limit $0 + 무료 모델(:free) = 완전 무료 AI 서비스!
