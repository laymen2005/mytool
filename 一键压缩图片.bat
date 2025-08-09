@echo off
chcp 65001 > nul

:: 设置标题
title 图片压缩处理器

:: 获取Python脚本的完整路径（假设它和本bat文件在同一个目录下）
set PYTHON_SCRIPT_PATH=%~dp0compress_image.py

:: 检查是否有文件被拖入
if "%~1"=="" (
    echo.
    echo  没有文件被拖入！
    echo.
    echo  请将一个或多个图片文件拖动到此脚本图标上。
    echo.
    goto end
)

:: 循环处理所有拖入的文件
:loop
if "%~1"=="" goto done
echo.
echo ----------------------------------------------------
echo 正在处理文件: %~nx1
echo ----------------------------------------------------
python "%PYTHON_SCRIPT_PATH%" "%~1"
shift
goto loop

:done
echo.
echo ==================== 所有任务处理完毕 ====================
echo.

:end
pause