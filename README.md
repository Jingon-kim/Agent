# 🤖 에이전트 폴더 구조

이 폴더는 **Intelligence Collection (INTCOL)**의 정보를 기반으로 동작하는 전문 에이전트들의 모음입니다.

---

## 📁 폴더 구조

```
Agent/
├── README.md                    # 이 파일 - 전체 구조 설명
├── git-expert/                  # Git 전문 에이전트 (30년+ 경력)
│   ├── AGENT.md                # 에이전트 역할 및 기능 정의
│   ├── commands/               # 자주 사용하는 명령어 모음
│   └── workflows/              # 작업 흐름 정의
├── vercel-expert/              # Vercel 전문 에이전트
│   ├── AGENT.md                # 에이전트 역할 및 기능 정의
│   ├── commands/               # 배포 명령어 모음
│   ├── workflows/              # 배포 워크플로우
│   └── guides/                 # 가이드 문서
├── openrouter-expert/          # OpenRouter 전문 에이전트 (30년+ 경력)
│   ├── AGENT.md                # 에이전트 역할 및 기능 정의
│   ├── commands/               # API 호출 명령어 모음
│   ├── workflows/              # 무료 사용 워크플로우
│   └── guides/                 # 비용 최적화 가이드
├── ad-monetization-expert/     # 광고 수익화 전문 에이전트 (30년+ 경력)
│   └── AGENT.md                # 에이전트 역할 및 기능 정의
├── prompt-engineering-expert/  # 프롬프트 엔지니어링 전문 에이전트 (30년+ 경력)
│   └── AGENT.md                # 프롬프트 최적화 전문가
├── rag-expert/                 # RAG 전문 에이전트 (30년+ 경력)
│   └── AGENT.md                # 검색 증강 생성 전문가
├── seo-expert/                 # SEO 전문 에이전트 (30년+ 경력)
│   └── AGENT.md                # 검색엔진 최적화 전문가
├── design-pattern-expert/      # 설계 패턴 전문 에이전트 (30년+ 경력)
│   └── AGENT.md                # 소프트웨어 아키텍처 전문가
└── [future-agents]/            # 추가 에이전트들
```

---

## 🎯 작동 방식

1. **정보 소스**: `Desktop/intelligence collection (INTCOL)/` 폴더의 정보 활용
2. **에이전트 역할**: 각 분야별 전문가로서 해당 정보를 기반으로 실행
3. **언어**: 한글로만 대화

---

## 📋 에이전트 목록

| 에이전트 | 상태 | 설명 |
|---------|------|------|
| [Git 전문가](./git-expert/AGENT.md) | ✅ 완료 | 30년+ Git 경력의 버전 관리 전문가 |
| [Vercel 전문가](./vercel-expert/AGENT.md) | ✅ 완료 | 클라우드 배포 및 호스팅 전문가 |
| [OpenRouter 전문가](./openrouter-expert/AGENT.md) | ✅ 완료 | 30년+ AI/API 경력의 무료 서비스 최적화 전문가 |
| [광고 수익화 전문가](./ad-monetization-expert/AGENT.md) | ✅ 완료 | 30년+ 광고 수익화 및 애드테크 전문가 |
| [프롬프트 엔지니어링 전문가](./prompt-engineering-expert/AGENT.md) | ✅ 완료 | 30년+ AI 프롬프트 최적화 전문가 |
| [RAG 전문가](./rag-expert/AGENT.md) | ✅ 완료 | 30년+ 검색 증강 생성 시스템 전문가 |
| [SEO 전문가](./seo-expert/AGENT.md) | ✅ 완료 | 30년+ 검색엔진 최적화 전문가 |
| [설계 패턴 전문가](./design-pattern-expert/AGENT.md) | ✅ 완료 | 30년+ 소프트웨어 아키텍처 전문가 |

---

> 💡 각 에이전트 폴더의 `AGENT.md` 파일에서 상세 역할과 기능을 확인하세요.
