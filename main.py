from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello_index():
    return {
        "message": "Hello, World!"
    }

@app.get("/index/")
def list_items():
    return {
        "item1",
        "item2",
        "item3",
        "fjnsf"
    }
