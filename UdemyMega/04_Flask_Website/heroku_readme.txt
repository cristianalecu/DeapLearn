www.heroku.com

install PostgreSQL www.postgresql.org

install heroku CLI from https://devcenter.heroku.com/articles/heroku-cli#windows 

>heroku login
>heroku create financiar
 (https://financiar.herokuapp.com/ | https://git.heroku.com/financiar.git)
 >heroku apps
 >pip freeze > requirements.txt
 >echo "web: gunicorn script1:app" > Procfile
  (app in the variable inside script1 that contains the Flask instance: app=Flask(__name__))
  >echo "python-3.6.3" > runtime.txt
   (check supported runtimes https://devcenter.heroku.com/articles/python-runtimes#supported-python-runtimes)
  
 >git init
 >git add .
 >git commit -m "First commit"
 >heroku git:remote --app financiar
 >git push heroku master
 >heroku open
 >heroku info
 