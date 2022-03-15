@echo off

call %~dp0env\Scripts\activate

@REM cd %~dp0telegram_bot

set TOKEN=5007766649:AAHLWZcJfXsfaogzwhTMZsbXMYg-lD175Ns

python telegram_bot.py

pause
