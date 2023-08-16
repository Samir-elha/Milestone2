# from motor.motor_asyncio import AsyncIOMotorClient
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# origins = [
#     "http://192.168.2.160",  # replace with the address where your front-end is served
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# MONGO_HOST = "my_mongodb_container"  # Use the name of your MongoDB container
# MONGO_PORT = 27017

# client = AsyncIOMotorClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")
# db = client["users"]
# collection = db["myCollection"]

# @app.get("/users")
# async def get_users():
#     users = []
#     async for user in collection.find():
#         user["_id"] = str(user["_id"])  # Convert ObjectId to string
#         users.append(user)
#     return {"users": users}

from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = [
    "http://192.168.2.160",  # replace with the address where your front-end is served
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MONGO_HOST = "my_mongodb_container"  # Use the name of your MongoDB container
MONGO_PORT = 27017

client = AsyncIOMotorClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")
db = client["users"]
collection = db["myCollection"]

@app.get("/users")
async def get_users():
    users = []
    async for user in collection.find():
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
        users.append(user)
    return {"users": users}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
