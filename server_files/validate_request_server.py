from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'It Works!'}

"""
Pydantic is a battle tested library which will validate the request body efficiently
More here: https://docs.pydantic.dev/latest/#why-use-pydantic
"""
class Student(BaseModel):
    name: str = Field(min_length=2)
    gpa: float = Field(gt=0)
    fees: int = Field(gt=0)
    dob: datetime

@app.post('/student/')
def new_student(student: Student):
    return {'message': 'Student is valid', 'student': student}
