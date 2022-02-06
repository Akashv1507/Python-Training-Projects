@REM On Windows 10, a batch file typically has a ".bat" extension, 
@REM and it is a special text file that includes one or multiple commands 
@REM that run in sequence to perform various actions with Command Prompt
call python -m venv project_env
call project_env\Scripts\activate.bat
call pip install -r requirements.txt

