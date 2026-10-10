from fastapi import FastAPI

from routers import projects, tasks


app = FastAPI(title="TaskFlow API")


@app.get("/")
def home():
    return {"message": "TaskFlow API is running"}


app.include_router(projects.router)

app.include_router(tasks.router)
