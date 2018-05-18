
IF EXIST ..\..\venv\venv_dml\NUL GOTO NO_CREATE

cd ..\..\
md venv
cd venv

call python -m venv  venv_dml

cd ..\DeapLearn\MachineLearn\

:NO_CREATE

call ..\..\venv\venv_dml\Scripts\activate.bat  

echo "Use env r   to install requirements"
echo "Use env r p  if you have also pss proxy "

if %computername%==L560-CNA if [%2]==[p] set https_proxy=http://192.168.1.29:8080

if [%1] == [r] call pip install -r requirements.txt