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

---

> 💡 각 에이전트 폴더의 `AGENT.md` 파일에서 상세 역할과 기능을 확인하세요.
