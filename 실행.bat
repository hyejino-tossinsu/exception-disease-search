@echo off
chcp 65001 > nul 2>&1
title 예외질환 검색 사이트
cd /d "%~dp0"

echo.
echo  =============================================
echo   예외질환 검색 사이트
echo  =============================================
echo.

:: ── Python 찾기 ──────────────────────────────
set PYTHON=
for %%p in (python python3 py) do (
    if not defined PYTHON (
        %%p --version > nul 2>&1 && set PYTHON=%%p
    )
)

if not defined PYTHON (
    echo  [오류] Python이 설치되어 있지 않습니다.
    echo.
    echo  해결 방법:
    echo  1. https://www.python.org/downloads/ 에서 Python 설치
    echo  2. 설치 시 "Add Python to PATH" 반드시 체크!
    echo  3. 설치 후 이 파일 다시 실행
    echo.
    pause
    exit /b 1
)

echo  Python 확인 완료: %PYTHON%

:: ── Flask 설치 확인 ──────────────────────────
%PYTHON% -c "import flask" > nul 2>&1
if errorlevel 1 (
    echo  Flask 설치 중... (최초 1회만)
    %PYTHON% -m pip install flask --quiet
    if errorlevel 1 (
        echo  [오류] Flask 설치 실패. 인터넷 연결을 확인해주세요.
        pause
        exit /b 1
    )
    echo  Flask 설치 완료!
)

:: ── 서버 실행 ────────────────────────────────
echo.
echo  사이트 시작 중...
echo  브라우저에서 http://localhost:5000 으로 자동 접속됩니다.
echo  (이 창을 닫으면 사이트도 종료됩니다)
echo.

%PYTHON% app.py

if errorlevel 1 (
    echo.
    echo  [오류] 서버 실행 중 문제가 발생했습니다.
    echo  5000번 포트가 이미 사용 중일 수 있습니다.
    echo.
    pause
)
