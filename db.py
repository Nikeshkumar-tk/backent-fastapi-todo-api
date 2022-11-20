from models import Todo
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb+srv://nikeshkumar:123@cluster0.fvmoaa4.mongodb.net/todolist?retryWrites=true&w=majority",serverSelectionTimeoutMS=5000)


database = client.todolist
collection = database.todo


#fetching a todo by title

async def fetchOneTodo(title):
    document = await  collection.find_one({"title":title})
    return document

#fetching all todos

async def fetchAllTodos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

#creating new todo in the database

async def createTodo(todo):
    document = dict(todo)
    result = await collection.insert_one(document)
    print(result)
    return str(result.inserted_id)

#Updating the todo

async def updateTodo(title, description):
    await collection.update_one({"title":title},{"$set":{"desc":description}})
    document = await collection.find_one({"title":title})
    return document

#deleting a todo by title

async def deletTodo(title):
    await collection.delete_one({"title":title})
    return True