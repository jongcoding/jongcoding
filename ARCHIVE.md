# 프로젝트와 활동 기록

[프로필로 돌아가기](README.md) · [포트폴리오](https://jongcoding.github.io/)

## 경력

### ENKI WhiteHat

Security Researcher / Content Team / 2026년 3월부터

웹 애플리케이션의 인증 흐름과 취약점 발생 조건을 분석하고, 클라우드·AI 에이전트의 권한 경계를 연구
Docker·Compose·Nginx 기반 연구 환경 구성, 재현 조건과 서비스 동작 검증, 연구 결과 문서화

2026년 CODEGATE·HACKTHEON Sejong 예선 웹 문제 출제, CCE 예선·본선 웹 문제 출제

[공개 발표자 소개](https://info.defcon.org/defcon34/people/67239) · [CODEGATE 기록](https://ctftime.org/event/3131) · [HACKTHEON 기록](https://ctftime.org/event/3199/)

## 프로젝트

### MSGCTF Cloud Platform

여러 클라우드의 자원을 묶어 팀별로 격리된 CTF 실행 환경을 제공하는 플랫폼을 개발 중
아키텍처 설계, 서비스 간 API 계약 검토, PR 리뷰와 연동 검증 담당

[프로젝트 저장소](https://github.com/MSG-CTF)

### GnawLab

실제 AWS 침해 사례를 Terraform으로 재현하는 오픈소스 보안 실습 프로젝트
AWS Bedrock Agent 시나리오에 기여하고 DEF CON 34 Demo Labs에서 공동 발표

[저장소](https://github.com/Beaver-Dam-Community/GnawLab) · [발표 정보](https://info.defcon.org/defcon34/content/66504)

### WEAVE

웹 구성 요소가 같은 입력을 다르게 해석할 때 발생하는 취약점 연구
원인별 분류 체계 설계와 사례 정리 담당

[연구 저장소](https://github.com/WHS-webao/semantic_gap) · [사이트](https://semanticgap.mjsec.kr/) · [웹 저장소](https://github.com/WHS-webao/WHS-webao.github.io)

### DBREACH

압축 사이드채널 연구의 재현·평가 환경 구성
Docker·MariaDB 기반 실험 환경에서 측정 잡음과 재현 조건 검토

[저장소](https://github.com/jongcoding/compression-side)

### Reagan

악성 URL 탐지를 위한 브라우저 확장 프로그램과 Django REST 백엔드
백엔드 Docker 패키징과 배포 환경 구성, 관련 연구 환경 정리

[저장소](https://github.com/MJSEC-MJU/Reagan) · [관련 연구](https://github.com/MJSEC-MJU/breakrecapcha_v2) · [Docker Hub](https://hub.docker.com/r/ialleejy/reagan-backend)

### MSG CTF / 2025

대회 플랫폼의 프론트·백엔드 연동과 Discord 운영 도구 개발, 대회 공동 운영과 Web·MISC 문제 출제
현재 개발 중인 MSGCTF Cloud Platform과 구분되는 2025년 대회 운영 기록

- 1회차 / SSG·seKUrity·MJSEC 공동 운영
- 2회차 / 2025년 11월 9일 / MJSEC·CODECURE·SecurityFirst·seKUrity·securious 공동 운영, HSPACE 후원
- 2회차 규모 / 약 100명·50팀, 총 24문제

[Frontend](https://github.com/jongcoding/MSG_CTF_WEB) · [Backend](https://github.com/jongcoding/MSG_CTF_BACK) · [Discord Bot](https://github.com/MJSEC-MJU/MSG_DISCORDBOT) · [2회차 운영 기록](https://www.notion.so/2220f19c72be80c78e83e6f56ebefa63)

출제 기록 / [jmt](https://github.com/MJSEC-MJU/MSG_CTF_PROBLEM/tree/main/jmt) · [django_session](https://github.com/MJSEC-MJU/MSG_CTF_PROBLEM/tree/main/django_session) · [2회차 MISC](https://github.com/MJSEC-MJU/MSG_CTF_WARGAME/tree/main/MISC)

### MJSEC Homepage & LMS

동아리 홈페이지와 학습 관리 서비스의 배포 환경 및 보안 검사 파이프라인 구성
React·Vite, Nginx, Docker·Compose, GitHub Actions 사용

| 검사 | 도구 |
| --- | --- |
| 정적 분석 | Semgrep |
| 의존성과 이미지 취약점 | npm audit, Trivy |
| 비밀정보 노출 | Gitleaks |
| Dockerfile 검사 | Hadolint |

PR과 main push에서 검사를 실행하고 GitHub Code Scanning에 SARIF 결과 업로드

[홈페이지 저장소](https://github.com/MJSEC-MJU/MJSEC_LMS_FRONT) · [LMS 저장소](https://github.com/MJSEC-MJU/MJSEC_LMS_FRONT_LMS) · [LMS](https://mjsec.kr/lms)

### MJSEC BOJ Contest

백준 풀이 기록을 반영하는 프로그래밍 대회 리더보드와 운영 도구
제출 검증·점수 집계, Django 기반 서비스와 GCP 배포 환경 구성

[저장소](https://github.com/MJSEC-MJU/MJSEC_BOJ)

### 기타 개발

- **[TokenCat](https://github.com/jongcoding/TokenCat)** / Claude와 Codex 사용량을 확인하는 Windows 데스크톱 위젯
- **[Watchdog](https://github.com/WATCHDOG-INCOGNITO/watchdog)** / 보안 연구 실행 기록과 발견 사항을 관리하는 워크플로 프로젝트
- **[DELDEVTOOL](https://github.com/jongcoding/DELDEVTOOL)** / Windows 브라우저 개발자 도구 사용 정책을 관리하는 유틸리티

## 활동

### INC0GNITO CTF / 2026

예선 108팀·315명, 본선 8팀·30명이 참여한 대회의 운영 총괄과 팀 간 조율
예선 Web 3문제, 본선 Jeopardy 2문제와 Live Fire Web 제작

[저장소](https://github.com/Incognito-CTF/incognito-ctf.github.io) · [예선](https://dreamhack.io/ctf/792) · [본선](https://dreamhack.io/ctf/814) · [운영 계획](https://github.com/Incognito-CTF/incognito-ctf.github.io/blob/main/docs/final-plan.md) · [본선 출제 기록](https://github.com/Incognito-CTF/incognito-ctf.github.io/blob/main/docs/finals-challenges.md)

### MJSEC

2024년 명지대학교 보안동아리 창단과 초기 운영
2024년 9월부터 2025년 8월까지 네 기수의 웹 보안·포렌식·Android·DevOps 멘토링과 Pwnable·리버싱 스터디 진행
교내 CTF·프로그래밍 대회 기획, 대회 플랫폼 개발과 MSG CTF 공동 운영

[동아리](https://mjsec.kr) · [CTF 2025](https://github.com/MJSEC-MJU/MJSEC_CTF_2025) · [문제 아카이브](https://github.com/MJSEC-MJU/MJSEC_CTF_CHALLENGE)

## 수상과 대회

| 연도 | 기록 | 자료 |
| --- | --- | --- |
| 2026 | DEF CON 34 CTF 결승 참가 / The Seoul Sauna Shogunate | [예선 결과](https://ctftime.org/event/3205/) |
| 2026 | DEF CON 34 Demo Labs / GnawLab 공동 발표 | [발표 정보](https://info.defcon.org/defcon34/content/66504) |
| 2026 | RubiyaLab / UofTCTF 팀 8위, 0xL4ugh CTF v5 팀 4위 | [팀 대회 기록](https://ctftime.org/team/303159/) |
| 2025 | 제1회 감귤 CTF 개인전 1위 | [대회 기록](https://dreamhack.io/ctf/766) |
| 2025 | SPACE WAR URANUS Web 개인전 1위 | [풀이 기록](https://ialleejy.tistory.com/54) |
| 2023 | 정보사령부 보안경연대회 우수상 | [수상 기록](https://github.com/jongcoding/jongcoding.github.io/blob/main/assets/award.png) |

[알고리즘 풀이 기록](https://solved.ac/ialleejy)

## 학력

- 명지대학교 정보통신공학 졸업
- 화이트햇 스쿨 3기 / KITRI / 2025년 3월 ~ 9월

## 병역

육군 정보보호병 / 2022년 4월 ~ 2023년 10월

보안장비 운용, 보안 정책 관리와 관제 업무
2022년 12월·2023년 2월 내부 웹 취약점 보고, 브라우저 정책 관리 도구 개발
