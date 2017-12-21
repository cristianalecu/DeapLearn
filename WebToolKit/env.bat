
IF EXIST ..\..\venv\venv_WTK\NUL GOTO NO_CREATE

cd ..\..\
md venv
cd venv

call python -m venv  venv_WTK

cd ..\DeapLearn\WebToolKit

:NO_CREATE


call ..\..\venv\venv_WTK\Scripts\activate.bat  

set https_proxy=http://192.168.1.29:8080


if [%1] == [r] call pip install -r requirements.txt
