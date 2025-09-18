from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    address:str


@app.get("/id/{studid}")
def getid(studid:int):
    return {"id: ",studid}

@app.get("/query")
def getdetails(course:str,year:int):
    return {"course":course,
            "year":year}


@app.post("/request")
def more(Userclass:User):
    return Userclass