from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
app.counter = 0


class HelloResp(BaseModel):
    msg: str


@app.get("/")
def hello_world():
    return {"message": "Hello world"}


@app.get("/counter")
def counter():
    app.counter += 1
    return str(app.counter)


@app.get("/hello/{name}", response_model=HelloResp)
def hello_name(name: str):
    return HelloResp(message=f"Hello {name}")
