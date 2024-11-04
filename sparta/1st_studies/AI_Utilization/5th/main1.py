#5-1
#API 심화 및 간단한 실습 (FastAPI 활용)

#"Hello_world" API 작성
from fastapi import FastAPI

#FastAPI 인스턴스 생성
app = FastAPI()

#루트 경로에 GET 요청이 들어왔을 때, "Hello World!"를 반환하는 엔드포인트 정의
@app.get("/") # /test -> 이런 식으로 검색하면 localhost:8000/test 경로에서 처리
def read_root():
    return{"message": "Hello World!"}

@app.get("/test") # /test -> 이런 식으로 검색하면 localhost:8000/test 경로에서 처리
def read_root():
    return{"message": "Hello test!"}

@app.get("/test2") # /test -> 이런 식으로 검색하면 localhost:8000/test 경로에서 처리
def read_root():
    return{"message": "Hello test2!"}

#터미널에 위 코드 작성 시, FastAPI 서버 시작
#"/docs"로 접속 시, 기능들이 서술되어 있음.