#openai 예제 코드

#openai 환경변수 설정
import os
os.environ["OPENAI_API_KEY"] = "<your OpenAI API key>"

from openai import OpenAI #해당 클래스를 통해 다양한 기능에 접속 가능

#클라이언트 생성
client = OpenAI()

#결과를 저장할 completion 만들기
completion = client.chat.completions.create(
    model = 'gpt-4o',
    messages = [
        {"role": "system", "content": "너는 환영 인사를 하는 인공지능이야, 농담을 넣어 재미있게 해줘"},
        {"role": "user", "content": "안녕?"}
    ]
)

print("답변: " + completion.choices[0].message.content)