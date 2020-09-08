@echo off
echo (where python)
FOR /f %%p in ('where python') do SET PYTHONPATH=%%p
ECHO %PYTHONPATH%

set path_to_use=%1
echo %path_to_use%