from uuid import UUID
from typing import List
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role, UserUpdateRequest

app = FastAPI()
db: List[User] = [
    User(
        id=UUID("77aea79c-3165-4c15-a6bc-15a642f09123"), 
        firstName="Jame", 
        lastName="Neo",
        gender=Gender.male,
        roles=[Role.user]
        ),
    User(
        id=UUID("a4c86da0-9d4d-448f-97d0-98c7c7bcfa7f"), 
        firstName="Nao", 
        lastName="Maki",
        gender=Gender.female,
        roles=[Role.user]
        ),
    User(
        id=UUID("81fcc14e-45f6-450e-8c8b-45fe3f18a746"), 
        firstName="Adam", 
        lastName="Smith",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
        )
]


@app.get("/")
async def root() :
    return {"Hello" : "Python"}

@app.get("/api/v1/users")
async def fetchUser() :
    return db

@app.post("/api/v1/users")
async def registerUser(user: User) :
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{userId}")
async def deleteUser(userId: UUID) :
    for user in db :
        if user.id == userId :
            db.remove(user)
            return 200
    raise HTTPException(
        status_code=404,
        detail= f"user with id: {userId} doesn't exits"
    )

@app.put("/api/v1/users/{userId}")
async def updateUser(userUpdate: UserUpdateRequest, userId: UUID) :
    for user in db :
        if user.id == userId :
            if userUpdate.firstName is not None :
                user.firstName = userUpdate.firstName
            if userUpdate.lastName is not None :
                user.lastName = userUpdate.lastName
            if userUpdate.middleName is not None :
                user.middleName = userUpdate.middleName
            if userUpdate.roles is not None :
                user.roles = userUpdate.roles
            return 200
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {userId} doesn't exits"
    )