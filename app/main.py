#!/usr/bin/env python3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import string
import pymongo
import bson
import requests
import os
# import random
# import uuid

MONGO_URI = os.getenv("RC_MONGO_URI")

app = FastAPI()
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET"]
)

@app.get("/")
def zone_apex():
    return {"project": "Placeholder for UVA Data Science unified building API.","docs":"docs/"}

@app.get("/floors")
def return_floors():
    return {"floors":[1, 2, 3, 4]}

@app.post("/temperature")
def temperature(request: dict):
    client = pymongo.MongoClient(MONGO_URI)
    db = client["building_data"]
    collection = db["temperature"]
    collection.insert_one(request)
    return {"message": "Temperature data received", "data": request}