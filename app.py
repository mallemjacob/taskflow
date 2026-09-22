# users_list = {"users": [{"name": "mouse"}, {"name": "cat"}]}

# value_to_look = 'mouse'


# for i in users_list["users"]:
#     if i["name"] == value_to_look:
#         print(i)


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
# def greet(name, age):  # name, age --> parameter
#     # function body
#     return "hi" + name


# function calling
# greet('mouse', 23)  # 'mouse' --> argument


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
#     return {"status": status}


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
