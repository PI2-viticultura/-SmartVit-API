from flask_pymongo import MongoClient
import os

password = os.environ["mongoPassword"]
dbname = os.environ["dbname"]
env = os.environ["env"]

client = MongoClient(
    "mongodb+srv://smartAdmin:"
    + password + "@feedback.6s6r9.mongodb.net/"
    + dbname + "?retryWrites=true&w=majority"
)
