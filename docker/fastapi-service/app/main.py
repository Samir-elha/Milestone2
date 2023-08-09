# from fastapi import FastAPI
# from pymongo import MongoClient

# # Initialize the FastAPI app
# app = FastAPI()

# # MongoDB credentials
# username = "root"
# password = "Ubuntu911"  # Decoded value of 'VWJ1bnR1OTEx'
# hostname = "mongodb"  # Usually the name of the service in Kubernetes

# # Set up MongoDB client
# client = MongoClient(f"mongodb://{username}:{password}@{hostname}:27017/")
# db = client["mydatabase"]  # Replace with your actual database name
# users_collection = db["mycollection"]  # Replace with your actual collection name


# @app.get("/")
# def read_root():
#     return {"message": "Welcome to your FastAPI application!"}


# @app.get("/user")
# def read_user():
#     # Fetching user details from MongoDB. You can adapt this query as needed.
#     user = users_collection.find_one()  # Adjust query as needed
#     if user is None:
#         return {"error": "User not found"}

#     return {"name": user["name"]}  # Adjust according to your data structure

from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:8000",  # replace with the address where your front-end is served
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = AsyncIOMotorClient("mongodb://localhost:27017/")
db = client["users"]
collection = db["myCollection"]


@app.get("/users")
async def get_users():
    users = []
    async for user in collection.find():
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
        users.append(user)
    return {"users": users}
