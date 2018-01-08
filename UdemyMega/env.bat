
IF EXIST ..\..\venv\venv_dml2\NUL GOTO NO_CREATE

cd ..\..\
md venv
cd venv

call python -m venv  venv_dml2

cd ..\DeapLearn\UdemyMega\



:NO_CREATE


call ..\..\venv\venv_dml2\Scripts\activate.bat  

rem set https_proxy=http://192.168.1.29:8080


if [%1] == [r] call pip install -r requirements.txt

