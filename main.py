from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from db import fetchOneTodo,createTodo,fetchAllTodos,updateTodo,deletTodo
from models import Todo



app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
@app.get("/")
async def getData():
  
    return {"stable":"true"}


@app.get("/api/v1/todo")

async def getTodos():
    res = await fetchAllTodos()
    return res


@app.post("/api/v1/todo")

async def addTodos(todo:Todo):
    res = await createTodo(todo)
    return res

@app.get("/api/v1/todo/{title}", response_model=Todo)

async def getTodoByTitle(title):
    res = await fetchOneTodo(title)
    return res

@app.put("/api/v1/todo/{title}", response_model=Todo)
async def update_todo(title:str,data:str):
    res = await updateTodo(title,data)
    return res

@app.delete("/api/v1/todo/{title}")
async def delete_todo(title:str):
    res = await deletTodo(title)
    return res