from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def Charitha():
    return {"message":"hello world","number":44,"is_fun":True}
