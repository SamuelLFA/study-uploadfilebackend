from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.projectDB

users = db["Users"]
files = db["Files"]