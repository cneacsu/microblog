# microblog - initial Flask tutorial from Miguel Grinberg
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

$ mkdir microblog
$ cd microblog
(venv) $ pip install flask

microblog/
  venv/
  app/
    __init__.py
    routes.py
  microblog.py
  
(venv) $ set FLASK_APP=microblog.py
Command Prompt:
C:\path\to\app>set FLASK_APP=microblog.py
And on PowerShell:
PS C:\path\to\app> $env:FLASK_APP = "microblog.py"
  
  (venv) $ flask run
 * Serving Flask app "microblog"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 
 (venv) $ pip install python-dotenv
 
 .flaskenv: Environment variables for flask command
FLASK_APP=microblog.py

Alternatively you can use python -m flask:
$ set FLASK_APP=microblog.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/
 * Running on http://localhost:5000/
 
 # PyStudentManager - Python & Flask course from Bo Milanovich
https://app.pluralsight.com/library/courses/python-getting-started/table-of-contents

# AWS DynamoDB - AWS Fundamentals course from Stefan Roman
https://app.pluralsight.com/library/courses/aws-dynamodb-fundamentals/table-of-contents
 