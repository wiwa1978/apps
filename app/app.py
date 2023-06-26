import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# initialize FastAPI
app = FastAPI()

templates = Jinja2Templates(directory="./app/templates")

todos = [
    { "id": 1, "name": "Todo 1", "description": "This is a description of todo 1", "status": False},
    { "id": 2, "name": "Todo 2", "description": "This is a description of todo 2", "status": True},
    { "id": 3, "name": "Todo 3", "description": "This is a description of todo 3", "status": False},
    { "id": 4, "name": "Todo 4", "description": "This is a description of todo 4", "status": True},
    { "id": 5, "name": "Todo 5", "description": "This is a description of todo 5", "status": False},
]

@app.get("/", response_class=HTMLResponse)
async def read_todos(request: Request):
    return templates.TemplateResponse("todo.html", {"request": request, "todos": todos})


@app.get("/todos")
def get_todos():
     return JSONResponse(content=jsonable_encoder(todos), status_code=200)

@app.get("/todo/{todo_id}")
async def read_item(todo_id: int = None):
    item = list(filter(lambda todos: todos['id'] == todo_id, todos))
    
    return JSONResponse(content=jsonable_encoder(item), status_code=200)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)