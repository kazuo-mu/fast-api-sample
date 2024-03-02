from fastapi import FastAPI
from app.api.routers import programmers

app = FastAPI()

@app.get("/")
def index():
  return {"message": "Hello World"}

app.include_router(
  programmers.router,
  prefix="/api/programmers",
  tags=["programmers"],
)