from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
CONNECTION_STRING = os.getenv('CONNECTION_STRING')


client = MongoClient(CONNECTION_STRING)
