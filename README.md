## initialize venv
$ python3 -m venv venv
$ . venv/bin/activate

## install dependencies
pip install fastapi uvicorn

## start server
$ uvicorn app.main:app --reload

## 以下の順で作成する
- スキーマ
- ルーター
- dependency
- CRUD

# create table
$python
>> from app.db.session import Engine
>> from app.db.models import Base
>> Base.metadata.create_all(bind=Engine)
>> quit()

# swagger ui on localhost
Swagger UI: http://127.0.0.1:8000/docs