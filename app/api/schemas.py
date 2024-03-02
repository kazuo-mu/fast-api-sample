from pydantic import BaseModel, Field

class ProgrammerListItem(BaseModel):
  name: str

  class Config:
    orm_mode = True

class ProgrammerDetail(BaseModel):
  name: str
  twitter_id: str
  languages: list[str] = Field(
    ..., min_items=1, max_items=3
  )
