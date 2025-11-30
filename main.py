from fastapi import FastAPI


app = FastAPI()


@app.get("/hello/{name}")
def create_graph(name: str):
    return f"Hello, {name}"
