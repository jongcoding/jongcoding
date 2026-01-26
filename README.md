# ialleejy/JONGCODING (이종윤)

Security · Web · DevOps/DevSecOps · CTF 운영/출제  
- Portfolio: https://jongcoding.github.io/
- GitHub: https://github.com/jongcoding
- Blog: https://ialleejy.tistory.com/

---

## 소개

안녕하세요, 이종윤입니다.  
웹/시스템 보안 기반으로 **취약점 분석·재현**, **CTF 플랫폼/대회 운영**, **DevOps 기반 배포/운영**을 중심으로 프로젝트를 진행합니다.

**Interest**: Web Security · Vulnerability Research · CTF Infra/Automation · AI 기반 보안 탐지/자동화

---

## 역량 기술

- **DevOps**: Docker · Docker Compose · Kubernetes · CI/CD(GitHub Actions) · Nginx Reverse Proxy · 운영 자동화  
- **Cloud**: **GCP**(Compute 중심 배포/운영, 네트워크/방화벽 설정 경험)  
- **DevSecOps(적용 경험)**: **MJSEC LMS**에서 SAST/SCA, Secrets Scan, Container Lint 및 Code Scanning(SARIF) 운영  
- **Security**: Web 취약점 분석/재현 · CTF 문제 출제/운영 · 취약점 리서치/재현 환경 구축  

---

## 대표 프로젝트

### WEAVE (WHS 3rd) — Semantic Gap 기반 웹 취약점 표준 분류/지식 플랫폼
- Site: https://semanticgap.mjsec.kr/
- Repo: https://github.com/WHS-webao/semantic_gap
- Docs: https://github.com/WHS-webao/WHS-webao.github.io
- 내가 한 역할
  - 최신 웹 취약점 정보가 산발적으로 흩어져 있어, 프로젝트 스코프를 **Semantic Gap(의미론적 차이)** 유형으로 한정하고 정리 방향을 잡음
  - 공격 “기법” 나열이 아닌 **Root Cause 중심 Taxonomy(분류 체계)**를 설계하여, 악용 흐름/방어 포인트를 함께 볼 수 있게 구조화
  - 취약점 사례를 일정 포맷으로 **정제·표준화**하여, 이후 LLM/RAG 기반 분석·탐지 자동화에 투입 가능한 데이터 형태로 정리

---

### Reagan — Chrome Extension + DRF 기반 악성 URL 탐지 파이프라인
- Repo: https://github.com/MJSEC-MJU/Reagan
- reCAPTCHA AI: https://github.com/MJSEC-MJU/breakrecapcha_v2
- Docker Hub: https://hub.docker.com/r/ialleejy/reagan-backend
- 내가 한 역할
  - 확장 프로그램과 백엔드를 연계해 URL 분석/수집 흐름을 구성하고, 백엔드를 Docker 기반으로 패키징
  - 모델/자동화 요소(reCAPTCHA 처리 등)를 파이프라인 형태로 분리해 재현 가능하게 정리

---

### MSG CTF Platform — 대회 운영용 플랫폼(Front/Back) + Discord 운영 봇
- Front: https://github.com/jongcoding/MSG_CTF_WEB
- Back: https://github.com/jongcoding/MSG_CTF_BACK
- Discord Bot: https://github.com/MJSEC-MJU/MSG_DISCORDBOT
- 출제한 문제: https://github.com/MJSEC-MJU/MSG_CTF_WARGAME/tree/main/MISC
- 회의록(Notion): https://www.notion.so/2220f19c72be80c78e83e6f56ebefa63

<details>
  <summary><b>MSG CTF 운영/출제 상세(실무형)</b></summary>

### 운영/출제 이력
- **MSG CTF 1회**: 세종대 **SSG**, 건국대 **seKUrity**, 명지대 **MJSEC** 공동 운영·출제  
- **MSG CTF 2회 (2025.11.09)**: 명지대 **MJSEC**, 상명대 **CODECURE**, 순천향대 **SecurityFirst**, 건국대 **seKUrity**, 중앙대 **securious** 공동 운영·출제  
  - 후원: **HSPACE**
  - 회의록: https://www.notion.so/2220f19c72be80c78e83e6f56ebefa63

### 규모(지표)
- 참가자: **약 100명**
- 팀 수: **약 50팀**
- 문제 수: **총 24문제**

### 맡은 경험
- **플랫폼 개발/운영**: 대회 운영에 필요한 Front/Back 및 운영 도구(Discord Bot)를 구성하고 유지보수
- **출제**: MISC 문제 제작 및 배포 아카이빙  
  - https://github.com/MJSEC-MJU/MSG_CTF_WARGAME/tree/main/MISC
- **운영 자동화**: 공지/진행 상태 공유/반복 문의 대응을 Discord 중심으로 정리하여 운영 효율을 높이는 방향으로 개선

</details>

---

### MJSEC LMS (Front) — 배포/운영 + DevSecOps(Security CI)
- Repo: https://github.com/MJSEC-MJU/MJSEC_LMS_FRONT_LMS  
- Live: https://mjsec.kr/lms  
- DevOps: React/Vite · Nginx Reverse Proxy · Docker/Compose · GitHub Actions  
- DevSecOps(적용): GitHub Actions 기반 보안 스캔 파이프라인 운영
  - SAST: Semgrep(OWASP Top 10 + JS/React) → SARIF 업로드
  - SCA/취약점: npm audit(리포트) + Trivy(fs/image) → SARIF 업로드
  - Secrets: Gitleaks → SARIF 업로드
  - Container: Hadolint(Dockerfile lint) → SARIF 업로드

<details>
  <summary><b>Security CI (GitHub Actions) 구성 보기</b></summary>

- Trigger: PR / main push  
- Concurrency: 동일 브랜치 중복 실행 취소  
- 결과 업로드: GitHub Code Scanning(SARIF)

**Scans**
- Semgrep(SAST): OWASP Top 10 + JavaScript + React
- npm audit(SCA): report-only
- Trivy(fs/image): HIGH/CRITICAL
- Hadolint(Dockerfile lint)
- Gitleaks(secrets)

</details>

---

### MJSEC BOJ CONTEST — solved.ac 기반 백준 대회 플랫폼
- Repo: https://github.com/MJSEC-MJU/MJSEC_BOJ
- 내가 한 역할
  - solved.ac API를 활용해 대회 운영에 필요한 리더보드/집계 흐름을 구성
  - 배포 환경(Nginx/Gunicorn/Docker 등)에 맞춰 운영 가능한 형태로 정리

---

## 수상/성과

| 날짜 | 성과 | 링크 |
|---|---|---|
| 2025.12.06 | 제1회 감귤 CTF 전체 1위 | https://dreamhack.io/ctf/766 |
| 2025.05.25 | SPACE WAR URANUS — WEB 개인전 1위 | https://ialleejy.tistory.com/54 |
| 2023.07.25 | 정보사령부 보안경연대회 우수상 | - |
| 2022.12 / 2023.02 | 정보사 웹사이트 취약점 보고 | - |

---

## 경험

### 육군 정보보호병 (2022.04 – 2023.10)
- 보안장비 운용/정책 관리, 웹 취약점 보고, 관제 업무

### 리서치
- DBREACH(압축 사이드채널) 재현/평가 환경 구축 (2024.12 – )  
  - Repo: https://github.com/jongcoding/compression-side  

### 커뮤니티/운영
- MJSEC 멘토링/대회 운영 다수 (2024–2025)
- 출제 예시  
  - JWT Signature Confusion: https://github.com/MJSEC-MJU/MSG_CTF_PROBLEM/tree/main/jmt  
  - Django Session Hijacking: https://github.com/MJSEC-MJU/MSG_CTF_PROBLEM/tree/main/django_session  

---

## 진행 중 / 계획

- **JongScanAI (계획)**: AI를 활용한 웹페이지 취약점 스캐너  
- **whoru (제작 중)**: 모바일 카메라 기반 3D 사용자 모델 + 의류 시뮬레이션 쇼핑 경험  

---

## 프로그래밍 언어
![Python](https://img.shields.io/badge/python-%233776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=black)
![Java](https://img.shields.io/badge/java-F89820?style=for-the-badge&logo=java&logoColor=white&labelColor=black)
![C](https://img.shields.io/badge/c-%23A8B9CC?style=for-the-badge&logo=c&logoColor=white&labelColor=black)
![C++](https://img.shields.io/badge/c%2B%2B-%2300599C?style=for-the-badge&logo=c%2B%2B&logoColor=white&labelColor=black)

## 프레임워크
![Django](https://img.shields.io/badge/django-%23092E20?style=for-the-badge&logo=django&logoColor=white&labelColor=black)

## DB
![SQLite](https://img.shields.io/badge/sqlite-%2307405e?style=for-the-badge&logo=sqlite&logoColor=white&labelColor=black)
![MySQL](https://img.shields.io/badge/mysql-%234479A1?style=for-the-badge&logo=mysql&logoColor=white&labelColor=black)

## Libraries
![Scikit Learn](https://img.shields.io/badge/scikit_learn-%23F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white&labelColor=black)
![NumPy](https://img.shields.io/badge/numpy-%23150458?style=for-the-badge&logo=numpy&logoColor=white&labelColor=black)
![SciPy](https://img.shields.io/badge/scipy-%230C55A5?style=for-the-badge&logo=scipy&logoColor=white&labelColor=black)
![Crypto](https://img.shields.io/badge/crypto-%23FFD700?style=for-the-badge&logo=security&logoColor=white&labelColor=black)

---

## BOJ PYTHON RANKING
![Boj Statistics](http://mazassumnida.wtf/api/v2/generate_badge?boj=ialleejy)
[![ialleejy profile](http://mazandi.herokuapp.com/api?handle=ialleejy)](https://solved.ac/ialleejy)

---

## GitHub 통계
![GitHub Statistics](https://github-readme-stats.vercel.app/api?username=jongcoding&show_icons=true&hide_title=true&count_private=true&hide=prs&theme=radical)

---


---
감사합니다.
