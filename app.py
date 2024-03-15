# app.py

import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# CORS 설정 허용할 주소
origins = [
    "http://localhost:8000",  # 추가된 주소
    "http://127.0.0.1:8000",  # 추가된 주소
    # "http://localhost:3000",  
    # "http://127.0.0.1:3000",  
]

# CORS 미들웨어 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 정적 파일 제공을 위한 경로 설정
app.mount("/", StaticFiles(directory=".", html=True), name="www")

database = []

def save_to_json(data):
    with open("data.json", "w") as json_file:
        json.dump(data, json_file)
        
@app.post("/create")
def create_data(data: dict):
    database.append(data)
    save_to_json(database)
    return {"message": "Data created successfully"}


# 추가된 코드: 메인 페이지를 띄우기 위한 핸들러
@app.get("/")
async def read_main():
    return {"message": "Welcome to the main page!"}

# FastAPI 서버 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)





# @app.get("/read")
# def get_all_data():
#     return database

# def save_to_json(data):
#     with open("data.json", "w") as json_file:
#         json.dump(data, json_file)