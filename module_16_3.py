import uvicorn
from fastapi import FastAPI, Path
from typing import Annotated

app=FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_user() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def user_register(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                        age: Annotated[int, Path(ge=18, le=120, description='Enter username', example='24')]) -> str:
    user_id= str(int(max(users, key=int))+1)
    users[user_id]=f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[str, Path()],
                      username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age")]):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[str, Path()]):
    del users[user_id]
    return f"User {user_id} has been deleted"

if __name__ == '__main__':
    uvicorn.run('module_16_3:app', host='127.0.0.1', port=8000, reload=True)