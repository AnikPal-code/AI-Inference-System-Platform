@echo off
echo ========================================
echo AI Inference Platform - Docker Startup
echo ========================================
echo.

echo Building and starting Docker containers...
docker-compose up --build -d

echo.
echo Waiting for services to be ready...
timeout /t 10 /nobreak >nul

echo.
echo Checking service health...
docker-compose ps

echo.
echo ========================================
echo Docker Services Started!
echo ========================================
echo.
echo Gateway API: http://localhost:8000
echo API Docs: http://localhost:8000/docs
echo.
echo To view logs: docker-compose logs -f
echo To stop services: docker-compose down
echo.

REM Start Streamlit in separate window
echo Starting Streamlit UI...
if not exist ".venv\" (
    echo Creating virtual environment for Streamlit...
    python -m venv .venv
    call .venv\Scripts\activate
    pip install streamlit requests --quiet
) else (
    call .venv\Scripts\activate
)

start "Streamlit UI" cmd /k "call .venv\Scripts\activate && streamlit run streamlit_app/app.py"

echo.
echo Streamlit UI: http://localhost:8501
echo.
echo Press any key to continue...
pause >nul
