@echo off

set this_file_path=%~dp0 
set this_file_path=%this_file_path: =%
echo.
python "%this_file_path%_listfiles.py" %*