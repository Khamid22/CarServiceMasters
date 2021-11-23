
Make sure the following programs are already installed on your PC
- Python version 3.9
- Pycharm (Community/Professional)
- There might be problems in vscode or other programs


In order to use the code please, perform the following steps:
1. Download the code and save in storage(better paste on desktop)
2. Download the CarService code also in the repository and save it on desktop (next to the CarServiceMasters)
3. Download the xampp(runs database from the server) via this link: https://www.apachefriends.org/download.html

# CarService
Installing necessary libraries and interpreters:
- open the CarService folder in your Pycharm and choose python interpreter 3.9 version
- create .env file and copy and paste the followings:
           ADMINS=12345678(Give user_id to make the user admin, telegrambot:@userinfobot)
           BOT_TOKEN=Paste the token of the bot(you can get it from BotFather on telegram)
           IP=localhost
       
- if pycharm is not installing required libraries automatically, write this on the terminal(alt +F12):
  pip install -r requirements.txt
- after installing all required libraries run app.py (you can also run through the terminal: python app.py)
  There is gonna be error telling the MySQL is not connected, we will solve it later but make sure the all required libraries are installed!!!

# CarServiceMaster:
Installing necessary libraries and interpreters:
- open the CarServiceMaster folder in your Pycharm but in the new window!
- create .env file and copy and paste the followings:
          ADMINS=12345678(Give user_id to make the user admin, telegrambot:@userinfobot)
          BOT_TOKEN=Paste the token of the bot(you can get it from BotFather on telegram)
          BOT2_TOKEN=the same token you have used in CarService
          IP=localhost
- if pycharm is not installing required libraries automatically, write this on the terminal: pip install -r requirements.txt)
- after installing all required libraries run app.py (you can also run through the terminal: python app.py)
  Again, the same error depicting the disconnection of MySQL from the server, make sure there is no error depicting the absence of required libraries

# Xampp 
Solving the MySQL error.
- Open xampp control panel and push the start buttons on Apache and MySQL
- Push the admin button of MySQL and click the "Создать БД" to create new table then name it as "car_service" if different name is given you must also change it in loader.py
- after creating table, import sql file from CarServiceMasters\car_service.sql
- after importing the database, click the button on the top right "Привилегия" then, "Добавть новый"
- name must be "turin" password must be "qwerty12" and choose all the options.

After completing all of the steps above, run the bots and enjoy!)



