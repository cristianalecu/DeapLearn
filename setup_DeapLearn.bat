cd ..
md venv
cd venv

call python -m venv  venv_dml
call venv_dml\Scripts\activate.bat  

cd ..\DeapLearn\

call pip install -r requirements.txt
