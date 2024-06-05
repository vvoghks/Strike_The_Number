# Strike The Number (숫자야구)

### 구현 목표

* 본 프로젝트는 어렸을 때 누구나 해봤던 추억의 게임 숫자 야구를 재구현하는 것이 목적입니다.
* 제한된 횟수 안에 정확한 숫자를 맞춰 삼진을 잡는 것이 목표인 게임입니다.
* 제한된 횟수를 초과할 동안 맞추지 못하면 패배하고 맞추면 승리하는 단순한 게임입니다.

### 구현 기능

* pygame 기반 게임 환경 구현
```
https://github.com/pygame/pygame
```
* 제한된 키보드 입력 기능: 숫자, 엔터, 백스페이스
* 재시작 기능

# 지원OS 및 실행방법

## 지원OS

|OS|지원 여부|
|-----|-----|
|Linux|O|
|Windows|X|
|MacOS|X|

## 실행방법

### Linux

* 전제조건: Docker 설치
1. 프로젝트 폴더를 clone한다.
```
$ git clone https://github.com/vvoghks/Strike_The_Number.git
```
2. Dockerfile을 build한다.
```
$ docker build . -t strike:0.1
```
3. 게임을 실행한다.
$ docker run -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix strike:0.1
```

# 코드 설명

## main.py

* generate_random_number: 무작위 세자리 숫자 생성 (중복 숫자 없음, 0으로 시작 가능)
* calculate_balls_and_strikes: 볼 (숫자O, 포지션X) 그리고 스트라이크 (숫자O, 포지션O) 계산
* create_restart_button: 재시작 버튼

* 키보드 입력 가능: 0~9, Enter, Backspace, r (그 외 입력 불가능)

* 최상단에 이번 실행의 게임 회차 출력
* 우측에 18회 제한의 볼-스트라이크 테이블 저장

* 제한 초과 시 패배
* 삼진 (스트라이크 세개) 시 승리

## 실행 예시

![1](https://github.com/vvoghks/Strike_The_Number/assets/81789939/543c3a37-6ac5-4089-a530-09573d69af0b)
![2](https://github.com/vvoghks/Strike_The_Number/assets/81789939/987ddc37-52e0-484d-aa2c-18676f4603e0)
![3](https://github.com/vvoghks/Strike_The_Number/assets/81789939/d6e3bad5-5254-424d-9eb6-6b9e3e934066)

# 향후 계획

* 버튼 입력 추가
* 네자리, 다섯자리 모드 추가
* 디자인 고급화