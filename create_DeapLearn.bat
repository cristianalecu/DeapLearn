
IF EXIST DeapLearn\NUL GOTO NO_OVERWRITE

IF EXIST ..\DeapLearn\NUL GOTO GO_OUTSIDE

rem    Put your name here  to sign your updates
call git config --global user.name "Cristian Alecu"

rem    Put your git email here  that will be used to access git repo (password will be requested for it)
call git config --global user.email cristian.alecu@pss.ro

rem  use proxy if you are behind proxy
rem call git config --global http.proxy 192.168.1.29:8080

git clone https://github.com/cristianalecu/DeapLearn.git

cd DeapLearn

start setup_DeapLearn.bat

GOTO EOF

:NO_OVERWRITE 

ECHO Cannot run here, DeapLearn\ folder will be overwritten

GOTO EOF

:GO_OUTSIDE

ECHO Move and execute this batch file outside folder DeapLearn\

:EOF
