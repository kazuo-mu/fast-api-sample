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