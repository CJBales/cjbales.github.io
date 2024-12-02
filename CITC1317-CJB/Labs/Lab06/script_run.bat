@echo off
:loop
timeout /t 2
if exist "InputFolder\PlayerNamesRequested.txt" (
    python Main.py "InputFolder\PlayerNamesRequested.txt" "output_folder"
    del "InputFolder\PlayerNamesRequested.txt"
)
goto loop