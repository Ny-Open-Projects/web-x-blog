@echo off
chcp 65001 >nul
title Java P10 刷题面板服务
rem 若 8907 端口已被占用（服务已在跑）则直接打开浏览器
netstat -ano | findstr :8907 | findstr LISTENING >nul
if %errorlevel%==0 (
    echo 服务已在运行，直接打开面板...
) else (
    echo 启动本地服务...
    cd /d "%~dp0notes\quiz\exams"
    start /b python -m http.server 8907 --bind 127.0.0.1
    timeout /t 1 >nul
)
start http://127.0.0.1:8907/interactive-quiz.html
echo 面板已在浏览器打开（可最小化本窗口，关闭窗口不影响已启动的服务）
pause
