from pydantic import BaseModel

class ProgrammerListItem(BaseModel):
  name: str

  class Config:
    orm_mode = True

class ProgrammerDetail(BaseModel):
  name: str
  twitter_id: str
  languages: list[str]
