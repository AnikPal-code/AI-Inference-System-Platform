@echo off
echo ========================================
echo AI Inference Platform - Local Startup
echo ========================================
echo.

echo Starting all services locally...
echo.

REM Check if virtual environment exists
if not exist ".venv\" (
    echo Creating virtual environment...
    python -m venv .venv
)

echo Activating virtual environment...
call .venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt --quiet

echo.
echo ========================================
echo Starting Services (Press Ctrl+C to stop all)
echo ========================================
echo.

REM Start services in separate windows
start "Gateway Service" cmd /k "call .venv\Scripts\activate && uvicorn backend.gateway.app.main:app --host 0.0.0.0 --port 8000"
timeout /t 3 /nobreak >nul

start "Sentiment Service" cmd /k "call .venv\Scripts\activate && uvicorn backend.services.sentiment.app.main:app --host 0.0.0.0 --port 8001"
timeout /t 2 /nobreak >nul

start "Resume Service" cmd /k "call .venv\Scripts\activate && uvicorn backend.services.resume.app.main:app --host 0.0.0.0 --port 8002"
timeout /t 2 /nobreak >nul

start "Image Service" cmd /k "call .venv\Scripts\activate && uvicorn backend.services.image.app.main:app --host 0.0.0.0 --port 8003"
timeout /t 2 /nobreak >nul

echo.
echo Waiting for services to start...
timeout /t 5 /nobreak >nul

echo.
echo Starting Streamlit UI...
start "Streamlit UI" cmd /k "call .venv\Scripts\activate && streamlit run streamlit_app/app.py"

echo.
echo ========================================
echo All services started!
echo ========================================
echo.
echo Gateway API: http://localhost:8000
echo Streamlit UI: http://localhost:8501
echo API Docs: http://localhost:8000/docs
echo.
echo Close this window or press any key to continue...
pause >nul
