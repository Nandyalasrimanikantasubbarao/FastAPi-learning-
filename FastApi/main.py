from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def helloWorld():
    return "helloWorld"


@app.get("/{name}")
def readName(name):
    return {"hello": name}
