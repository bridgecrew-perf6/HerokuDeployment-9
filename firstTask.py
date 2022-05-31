from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def firstTask():
    return{"hello worldddd"}


