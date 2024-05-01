Database migrations with SQLAlchemy (261)
For raw project instructions see: http://syllabus.africacode.net/projects/python-specific/sqlalchemy-migrations/
## **EXECUTING CODE**

### **_Starting up docker container for prod database_**

**Docker compose up** using one of the given command options in your terminal:
1. cd into project package
2. docker-compose -f docker-compose-prod.yaml up
                    or
   docker compose -f docker-compose-prod.yaml up
   (Command used depends on OS you use)
   
### **_Running migrations files_**
Migrations can be run using the command: alembic -n [database] upgrade [migration code]

[database] = Database you'd like to run the migrations on

[migration code] = alphanumeric found in the revision variable in each migration file

### **_Adding recruits_**

The create recruits scripts can be run on the terminal using the command: python create_[*]_recruits.py.

[*] = Represents the cohort number of the script

### **_Displaying table_**

The table produced can be found on adminer(localhost:8080) using the following credentials to log on:

System: PostgreSQL

Server: postgres

Username: postgres

Password: post

Database (optional): prod or leave blank