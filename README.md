# ft_transcendence-test
Testing 

venv is used and a small part of allauth is edited to allow custom provider to work
Currently using allauth package for account creation but username is required and have to be unique.
Current implementation
- [x] 42oauth
- [x] Normal account creation
- [x] Password reset/verification
- [ ] DB for user game data and relational mapping(use username)
- [ ] Check signup for duplicate unique username
- [ ] migrate to postgres

Installing using Windows
1. Download python 3.11.8 from Microsoft store
2. Install python intellisense
3. Install Virtual environment, pip install virtualenv
4. Install vscode extension python environment manager
5. Activate environment, \venv\script\activate  (I dont quite remember the path)
6. Run development server, python migrate.py runserver

A few useful things to note
1. Clear all tables and data in db by using django extension, run, python migrate.py reset_db --noinput
2. To check database via admin dashboard, create superuser by running, python migrate.py createsuperuser, then login via browser through, 127.0.0.1/admin
3. To login through allauth, use homepage or 127.0.0.1/accounts/login
4. To singup through allauth, use hompage or 127.0.0.1/accounts/signup
