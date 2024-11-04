from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from openai import OpenAI

app = FastAPI()

# OpenAI API 클라이언트 설정
client = OpenAI()

# Jinja2 템플릿 설정
templates = Jinja2Templates(directory="templates")

# 정적 파일 서빙
app.mount("/static", StaticFiles(directory="static"), name="static")

# 초기 시스템 메시지 설정
system_message = {
    "role": "system",
    "content": "너는 환영 인사를 하는 인공지능이야, 농담을 넣어 재미있게해줘"
}

# 대화 내역을 저장할 리스트 초기화
messages = [system_message]

@app.get("/", response_class=HTMLResponse)
async def get_chat_page(request: Request):
    """채팅 페이지 렌더링"""
    conversation_history = [msg for msg in messages if msg["role"] != "system"]
    return templates.TemplateResponse("index.html", {"request": request, "conversation_history": conversation_history})

@app.post("/chat", response_class=HTMLResponse)
async def chat(request: Request, user_input: str = Form(...)):
    """사용자 메시지를 받아 OpenAI API 호출 및 응답 반환"""
    global messages

    # 사용자의 메시지를 대화 내역에 추가
    messages.append({"role": "user", "content": user_input})

    # OpenAI API 호출
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    # AI의 응답 가져오기
    assistant_reply = completion.choices[0].message.content

    # AI의 응답을 대화 내역에 추가
    messages.append({"role": "assistant", "content": assistant_reply})

    # 화면에 표시할 대화 내역에서 system 메시지를 제외하고 전달
    conversation_history = [msg for msg in messages if msg["role"] != "system"]

    # 결과를 HTML로 반환 (대화 내역과 함께)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "conversation_history": conversation_history
    })