#!/usr/bin/env python3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import string
# import random
# import uuid

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
