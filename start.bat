@echo off
setlocal

:: --- Configuration ---
set "PYTHON_EXEC=python"
set "LAUNCHER_SCRIPT=launcher.py"

:: Liste des dépendances Python requises (ajoutez-en d'autres si nécessaire)
set "DEPENDENCIES=Pillow"

echo =======================================================
echo Lancement de l'ADB Control Center
echo =======================================================
echo.

:: --- Vérification et installation des dépendances Python ---
echo Verification des dependances Python...
for %%d in (%DEPENDENCIES%) do (
    echo.
    echo Verification de %%d...
    %PYTHON_EXEC% -c "import %%d" >nul 2>&1
    if errorlevel 1 (
        echo %%d non trouve. Installation en cours...
        %PYTHON_EXEC% -m pip install %%d
        if errorlevel 1 (
            echo Erreur: Echec de l'installation de %%d.
            echo Verifiez votre connexion internet ou les permissions.
            pause
            exit /b 1
        ) else (
            echo %%d installe avec succes.
        )
    ) else (
        echo %%d est deja installe.
    )
)
echo Toutes les dependances sont installees.
echo.

:: --- Vérification de l'existence du script launcher.py ---
if not exist "%LAUNCHER_SCRIPT%" (
    echo Erreur: Le script lanceur "%LAUNCHER_SCRIPT%" est introuvable.
    echo Assurez-vous que "launcher.py" est dans le meme dossier que ce script batch.
    pause
    exit /b 1
)

:: --- Lancement de launcher.py ---
echo Lancement de l'application via %LAUNCHER_SCRIPT%...
echo.

:: Lance launcher.py dans une nouvelle fenêtre de console.
:: 'start ""' est utilisé pour démarrer un nouveau processus en arrière-plan.
start "" %PYTHON_EXEC% "%LAUNCHER_SCRIPT%"

endlocal
exit /b 0