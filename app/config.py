import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://himeshsrivastava123:rk9RUCdC3aJsdqWA@cluster0.aqzjeb9.mongodb.net/Database_backend")
