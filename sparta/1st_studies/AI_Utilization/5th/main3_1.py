#ChatGPT와 ElevenLabs 실습

#환영 인사 프로그램 코드
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "너는 변호사야, 나에게 법적인 상담을 해줘"},
    {"role": "user", "content": "안녕하세요, 저는 이형민 입니다."}  
  ]
)

print("대답: " + completion.choices[0].message.content)


