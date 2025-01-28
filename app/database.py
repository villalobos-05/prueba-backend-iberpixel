import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

# Load .env variables
load_dotenv()


def get_database():
    # Create a connection
    client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))

    # Return database
    return client[os.getenv("MONGODB_DATABASE")]


if __name__ == "__main__":
    database = get_database()
    print("Database connected: ", database)
