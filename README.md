# set up the environment on your pc
to use the environment on Linux or mac run the following in the terminal ```source env/bin/activate ```

to use the environment on windows you need to open powershell as administrator and type in the following ```set-executionpolicy RemoteSigned ``` or else the env script can't run. Then run ``` env/scripts/activate.ps1 ``` in the terminal

# set up the database
to run our database you need to open ```moviegenerator.sql``` in the database folder and change all of the absolute paths to the .csv files in the same folder. You then need to go into the code and change the credentials to your postgresql user.

# How to run the flask backend
to run the flask backend just open a terminal and go to the file location of the ```app.py``` file and run ````python app.py``` and press enter

# How to access the website
when you have started the ```app.py``` file open a webbrowser and enter ````http://127.0.0.1:5000```
