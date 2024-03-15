# app.py

# FastAPI
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# FastAPI 애플리케이션 생성
app = FastAPI()

# CORS 설정 허용할 주소
origins = [
    "http://localhost:3000",  # Next.js 애플리케이션의 주소
    "http://127.0.0.1:3000",  # Next.js 애플리케이션의 주소
]

# CORS 미들웨어 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Greet": "Hello, FastAPI!" }

database = []
@app.post("/create")
def create_data(data: dict):
    database.append(data)
    save_to_json(database)  # 데이터를 JSON 파일에 저장
    return {"message": "Data created successfully"}

def save_to_json(data):
    with open("data.json", "w") as json_file:
        json.dump(data, json_file)

@app.get("/read")
def get_all_data():
    return database

def save_to_json(data):
    with open("data.json", "w") as json_file:
        json.dump(data, json_file)



# FastAPI 서버 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)