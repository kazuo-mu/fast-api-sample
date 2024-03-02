from fastapi import APIRouter
from app.api.schemas import (
  ProgrammerListItem, ProgrammerDetail
)

router = APIRouter()

@router.get(
  "/",
  response_model=list[ProgrammerListItem]
)
def list_programmers():
  return [
    ProgrammerListItem(name="susumuis"),
    ProgrammerListItem(name="altnight")
  ]

@router.get(
  "/{name}",
  response_model=ProgrammerDetail,
)
def detail_programmer(name: str):
  return ProgrammerDetail(
    name="susumuis",
    languages=["Python", "Java", "JavaScript"],
    twitter_id="susumuis"
  )

@router.post("/")
def add_programmer(programmer: ProgrammerDetail):
  return {"result": "OK"}

@router.put("/{name}")
def update_programmer(
  name: str, programmer: ProgrammerDetail,
):
  return {"result": "OK"}

@router.delete("/{name}")
def delete_programmer(name: str):
  return {"result": "OK"}
