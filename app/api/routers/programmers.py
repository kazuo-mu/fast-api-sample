from fastapi import APIRouter, Depends
from app.api.schemas import (
  ProgrammerListItem, ProgrammerDetail
)
from app.api.dependencies import get_db
from app.api import cruds

router = APIRouter()

@router.get(
  "/",
  response_model=list[ProgrammerListItem]
)
def list_programmers(
  db=Depends(get_db)
):
  return cruds.get_programmers(db)

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
def add_programmer(
  programmer: ProgrammerDetail,
  db=Depends(get_db),
):
  cruds.add_programmer(db, programmer)
  return {"result": "OK"}

@router.put("/{name}")
def update_programmer(
  name: str, programmer: ProgrammerDetail,
):
  return {"result": "OK"}

@router.delete("/{name}")
def delete_programmer(name: str):
  return {"result": "OK"}
