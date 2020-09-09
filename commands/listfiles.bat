@echo off

:: Recuperation du chemin vers le dossier du fichier
set this_file_path=%~dp0 
:: Suppression de l'espace de fin
set this_file_path=%this_file_path: =%

echo.
:: Appel du script python et passage de tous les parametres avec "%*"
python "%this_file_path%_listfiles.py" %*