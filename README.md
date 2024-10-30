## PoC(Proof of Concept) 구현을 통한 클라우드 보안 공격 자동화 도구 개발
### 1. 프로젝트 소개
#### 1.1 배경 및 필요성
 클라우드 환경이 증가하면서 새로운 보안 위협을 초래하기도 한다. 하지만 클라우드 환경에서는 전통적인 보안 모델이 충분하지 않기 때문에, 새로운 보안 전략과 도구가 요구된다. 특히, CVE(Common Vulnerabilities and Exposures)와 MITRE ATT&CK 프레임워크를 기반으로 한 공격 시나리오는 클라우드 보안의 주요 위협 요소로 떠오르고 있다. 이러한 공격들을 사전에 탐지하고 방어하기 위해서는 공격 기법을 이해하고, 이를 시뮬레이션 할 수 있는 PoC(Proof of Concept)를 구현하는 것이 중요하다. 이를 통해 클라우드 환경에서의 취약점을 실질적으로 확인하고, 개선 방안을 도출할 수 있다.
#### 1.2 과제 목표
 본 과제의 목표는 클라우드 보안을 강화하기 위해 MITRE ATT&CK 프레임워크를 기반으로 클라우드 보안 공격 자동화 도구를 개발하는 것이다. 클라우드 환경으로 완전한 전환이 아닌 하이브리드 클라우드 환경을 사용하는 사용자를 위해 온프레미스(On-premise) 환경의 공격도 지원하도록 설계한다.
 MITRE ATT&CK은 새로운 공격 기법이 발견될 때마다 데이터가 업데이트되어 최신 공격에 대해 신속하게 대응할 수 있는 장점이 있다. 이 과제에서는 클라우드 및 온프레미스 환경에서 발생할 수 있는 다양한 보안 취약점과 공격 기법을 분석하고, 관련 CVE를 통해 취약점을 파악한다. 이후 분석된 정보를 바탕으로 공격 시나리오를 설계한다. 이때, 공격 시나리오는 ‘공격 대상 시스템에서 특정 목표를 달성하기 위한 일련의 과정’으로 정의하며, MITRE ATT&CK에서 제공하는 Tactic의 순서를 기반으로 자동 생성되는 기능을 포함하고자 한다. 모의 해킹이 끝나면 사용자는 공격 결과와 공격 시나리오에 대한 설명 및 공격을 예방할 수 있는 방어책을 제공받을 수 있다.
### 2. 팀소개
#### 김승혁
- **Email** : senghyuk66@gmail.com
- **GUI 개발**
  - 공격 결과 표시(시나리오, 완화 방법, 사용된 명령어 등)
- **기능 구현**
  -  초기 환경 세팅
  -  Command To MITRE ATT&CK Technique 연동
  -  공격 시나리오 구상
  -  DB 설계
#### 정재영
- **Email** : jyjung010211@gmail.com
- **GUI 개발**
  - 공격 결과에 따른 CVE 리스트 표시
- **기능 구현**
  - CVE to ATT&CK Technique 연동
  - 사용자 정보 수정 구현
  - DB 설계
#### 송재홍
- **Email** : thd8219@pusan.ac.kr
- **GUI 개발**
  - UI 구현
  - 이용 방법 및 마이페이지 구현
- **기능 구현**
  - DB 설계
  - 로그인 및 회원 가입 구현
  - CVE 스캐닝 구현
### 3. 시스템 구성도

![image](https://github.com/user-attachments/assets/e9cfeba1-3c29-452a-a9ac-47fec1dc9c78)

개발한 플랫폼의 서비스 아키텍처이다. 해당 아키텍처에서 Attack Server는 본 과제의 기능적인 부분을 총괄하며, Vulnerability Scanner, Attacker, Scenario Generator 모듈로 구성되어 있다. 각 모듈에 대한 자세한 설명은 아래에 기술한다.

- **Vulnerability Scanner**
  - Nmap, ssh-audit 등의 툴을 사용하여 대상 시스템을 스캔한다. 스캔한 정보 및 Vulners.com의 API를 이용하여 대상 시스템이 가지고 있는 CVE 목록을 추출한 후 Vulnerability DB에 저장 및 Attacker 모듈에 전달한다.
- **Attacker**
  - MITRE ATT&CK의 Technique과 대응되는 명령어와 CVE exploit 코드를 CVE DB, Technique & Tactic DB에서 가져온다. Agent를 통해 대상 시스템을 공격하고, 각 단일 공격의 성공 여부를 판단한다.
- **Scenario Generator**
  - 성공한 단일 공격을 기반으로 도출된 공격 시나리오와 이에 대한 개선 방안을 대상 시스템 사용자에게 제공한다.

#### 기술스택
##### Frontend : node.js (React, MUI, tailwindcss)
##### Backend : Python (FastAPI, SQLAlchemy, Pydentic)
##### DB : PosgresDB, pgAdmin
##### 기타 : Kali OS, Vulners.com API

### 4. 소개 및 시연 영상

[![2024년 전기 졸업과제 50 417호](https://img.youtube.com/vi/hKoIGgROhms/0.jpg)](https://www.youtube.com/watch?v=hKoIGgROhms)

### 5. 설치 및 사용법

본 프로젝트는 Ubuntu 22.04 버전에서 개발되었으며 다음의 스크립트를 수행하여 
관련 패키지들의 설치와 빌드를 수행할 수 있습니다.

- Frontend
```
.../Frontend$ npm install
.../Frontend$ npm start
```

- DB & Kali OS
```
.../Backend$ docker compose up --build 
```

- Backend
```
.../Backend$ python3 -m venv .venv
.../Backend$ source .venv/bin/activate
.../Backend$ cd api
.../Backend/api$ pip install -r requirements.txt
.../Backend/api$ gunicorn --bind 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker app:app --timeout 3000

(파이썬 가상환경 해제)
$ deactivate
```
