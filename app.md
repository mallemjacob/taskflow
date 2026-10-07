# users_list = {"users": [{"name": "mouse"}, {"name": "cat"}]}

# value_to_look = 'mouse'

# for i in users_list["users"]:

# if i["name"] == value_to_look:

# print(i)

tasks = [
{
"id": 1,
"title": "Your title is React",
"description": "The description is V19",
"completed": False
},
{
"id": 2,
"title": "Your title is Python",
"description": "The description is v3",
"completed": False
},
{
"id": 3,
"title": "Your title is FastAPI",
"description": "The description is backend library for python",
"completed": False
}
]

for task in tasks:
if task["id"] == 2:
print(task["title"])

# function definiton

# def greet(name, age): # name, age --> parameter

# # function body

# return "hi" + name

# function calling

# greet('mouse', 23) # 'mouse' --> argument

# Path parameters

# Query parameters

# task_name = 'learn react'

# duration = '1 month'

# Query parameters starts with ? and multiple queries are seperated by &

# http://127.0.0.1:8000/login?username=mouse&password=hello@123&location=guntur

# /tasks?task_name=learn%20react&duration=1%20month

# POST

# /tasks?status=done

# @app.get('/tasks')

# def get_tasks(status: str | None = None):

# return {"status": status}

# posting some data ----> /tasks ---> tasks = [task1, task2]

# /tasks?title=react&description=learnreact&completed=False

# @app.post('/login')

# @app.post('/singup')

# @app.get('/users')

# @app.get('/tasks')

# @app.get('/users/mouse')

# @app.get('/tasks/{id}')

# @app.patch('/tasks/{id}')

# @app.delete('/tasks/{id}')

# POST a task

# Get all tasks

# Get single task

# Update task

# GET

# POST

# PATCH

person = {
'name': 'mouse',
'age': 5
}

person['age'] = 6
print(person['age'])

# animal = 'cat'

# if the animal is not monkey, then do this

##########################################################

frontend client(swagger) - -- -> GET / tasks - --- -> backend server(FastAPI) - - -> Database(Postgresql)
GET / tasks/1 / tasks
POST / tasks / users
PATCH / tasks/1 / signup
DELETE / tasks/1 / login
/projects

                                GET / users
                                GET / users/3
                                POST / users

lots of books - - -> secience, philosphy, biology, law

Database

Science Tables
book_name, author, pages, published_date
evoltuion, dawkins 100 2001
biology hawkins 250 2010
zoology hawkins 150 2015
surgery hawkins 550 2020
mecidice scdscdsc 950 1995

Law Tables
book_name, author, pages, published_date
evoltuion, dawkins 100 2001
biology hawkins 250 2010
zoology hawkins 150 2015
surgery hawkins 550 2020
mecidice scdscdsc 1000 1995

4 columns
2 rows

i want book_name called evoltuion
i want authir called hawkins
i want books that have pages more than 200
i want books published after 2010

Taskflow Database

users tables
id, name, email

tasks tables
id, title, description
1 | fastAPI | backend python library
2 | react | frontend javascript library

project table
id, project_name, project_type, duration``
1 ECE science 1 month

print()
def greet():

\l ---> to view databases
\dt ---> view tables

# create table

CREATE TABLE tasks (id SERIAL PRIMARY KEY, title VARCHAR(100), description VARCHAR(200));

# insert data into table

INSERT INTO tasks (title, description) VALUES ('fastAPI', 'backend python library');

# View data from the table.

SELECT \* FROM tasks;

###################################################

superuser = postgres
password = 12345

user = taskflow_user
password = 12345

pgAdmin (GUI) ---> postgresql database server
psql (TUI) ---> postgresql database server
fastAPI -----> SQL Alchemy ----> postgresql database server

human (terminal) ----> postgresql database

clinet (POST /tasks {title:react, description:v19}) ----> server (fastAPI) (.env) ----> postgresql database

tasks DB ---> tasks Table ---> title:react, description:v19

Room --> science book database ---> Table (s.no, author, pubished data, pages)

german <-- french -> enlgish

## database server

owner1 --> tasks db --> tables --> rows
owner2 --> users db --> tables --> rows

facebook.com (167.80.4.1)

charitha computer (brodpter 4th line)

lakshimi grand apartments (postcolont 4th line)

charotha cpmputer (97384438734)

## Laptop - local host

fastapi server ---> http://127.0.0.1:8000/
postgres server ---> http://127.0.0.1:5433/

ports = 8000, 5433
local host

brodipter 4th line, LG towers --> 401
brodipter 4th line, LG towers --> 402
brodipter 4th line, LG towers --> 403

my ph number ---> your ph number

react (http://127.0.0.1:3000/) ---> fastapi (http://127.0.0.1:8000/) --> postgres (http://127.0.0.1:5433/)

## Files and folders:

main.py ---> fastapi (backend)

.env ---> credentials to connect to database
database.py ---> sqlalcehmy, psycopg connection to postgresql
models.py ---> Mapping tables in postgresql

FastAPI --> SQLAlchemy --> psycopg --> Postgresql

swagger (http://127.0.0.1:8000/docs) ---> FastAPI ---> sqlalcehmy, psycopg --> postresql

commands ---> linux ---> windows (vscode)

1. Install WSL in windows
   Create username and password

2. Install postgresql in WSL
   Create a database called taskflow and password for the database

third party modules - - -> pypi.org - - -> pip install requests - - -> import requests
built-in modules - - -> import random, import sys
user-defined modules - -> filename.py - -> import filename

swagger (http://127.0.0.1:8000/docs) ---> FastAPI ---> sqlalcehmy, psycopg --> postresql (windows)

rules - models
routes - pages
store in db
return resources

## <!-- users

name, username, email, password -->

fastAPI (local computer) ---> Postgresql (online database server) NeonDB

## 07-Oct-2026

FastAPI
↓
SQLAlchemy
↓
psycopg
↓
localhost:5432
↓
PostgreSQL

FastAPI
↓
SQLAlchemy
↓
psycopg
↓
Internet / SSL
↓
Neon PostgreSQL

fastapi ----> neondb
