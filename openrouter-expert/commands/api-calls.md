# 🔧 OpenRouter API 호출 명령어 모음

> 무료 모델 중심의 API 호출 예제

---

## 🆓 무료 모델 기본 호출

### Python - requests 사용
```python
import os
import requests

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    },
    json={
        "model": "meta-llama/llama-3.1-8b-instruct:free",
        "messages": [
            {"role": "user", "content": "안녕하세요!"}
        ]
    }
)

print(response.json()['choices'][0]['message']['content'])
```

### Python - OpenAI SDK 사용 (권장)
```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

response = client.chat.completions.create(
    model="meta-llama/llama-3.1-8b-instruct:free",
    messages=[
        {"role": "user", "content": "안녕하세요!"}
    ]
)

print(response.choices[0].message.content)
```

---

## 📝 시스템 프롬프트 포함 호출

```python
response = client.chat.completions.create(
    model="meta-llama/llama-3.1-8b-instruct:free",
    messages=[
        {"role": "system", "content": "당신은 친절한 한국어 AI 어시스턴트입니다."},
        {"role": "user", "content": "오늘 날씨가 어떨까요?"}
    ]
)
```

---

## 🔄 스트리밍 응답

### 실시간 출력
```python
response = client.chat.completions.create(
    model="meta-llama/llama-3.1-8b-instruct:free",
    messages=[
        {"role": "user", "content": "긴 이야기를 해주세요."}
    ],
    stream=True
)

for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## 🛡️ 에러 처리 포함 호출

### Rate Limit 대응
```python
import time

def call_with_retry(messages, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="meta-llama/llama-3.1-8b-instruct:free",
                messages=messages
            )
            return response.choices[0].message.content
        except Exception as e:
            if "429" in str(e):  # Rate Limit 에러
                wait_time = 2 ** attempt  # 1초, 2초, 4초
                print(f"Rate Limit! {wait_time}초 대기 중...")
                time.sleep(wait_time)
            else:
                raise e
    return None

# 사용
result = call_with_retry([{"role": "user", "content": "안녕!"}])
print(result)
```

---

## 📊 사용량 확인

### 응답에서 토큰 사용량 확인
```python
response = client.chat.completions.create(
    model="meta-llama/llama-3.1-8b-instruct:free",
    messages=[{"role": "user", "content": "간단한 질문입니다."}]
)

# 토큰 사용량 출력
usage = response.usage
print(f"입력 토큰: {usage.prompt_tokens}")
print(f"출력 토큰: {usage.completion_tokens}")
print(f"총 토큰: {usage.total_tokens}")
```

---

## 🎯 무료 모델 목록 확인

```python
# 무료 모델 예시 (모델명 뒤에 :free)
FREE_MODELS = [
    "meta-llama/llama-3.1-8b-instruct:free",
    "google/gemma-2-9b-it:free",
    # 최신 목록은 openrouter.ai/models 에서 확인
]
```

---

## ⚙️ 파라미터 조절

### Temperature (창의성)
```python
response = client.chat.completions.create(
    model="meta-llama/llama-3.1-8b-instruct:free",
    messages=[{"role": "user", "content": "창의적인 이야기 해주세요."}],
    temperature=0.8  # 0.0 (결정적) ~ 1.0 (창의적)
)
```

### Max Tokens (최대 출력 길이)
```python
response = client.chat.completions.create(
    model="meta-llama/llama-3.1-8b-instruct:free",
    messages=[{"role": "user", "content": "간단히 답해주세요."}],
    max_tokens=100  # 출력 토큰 제한
)
```

---

## 💡 팁

```
✅ 무료 모델은 반드시 :free 접미사 확인
✅ 환경 변수로 API 키 관리
✅ 에러 처리로 Rate Limit 대응
✅ 스트리밍으로 사용자 경험 향상
```
