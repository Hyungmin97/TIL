#Chat GPT를 사용한 간단한 질의응답 프로그램

from openai import OpenAI

client = OpenAI()

system_message = {
    "role": "system", "content": "너는 AI 및 프로그래밍 취업 전문가야, 나에게 커리어적인 상담을 해줘. 단, 컴퓨터 비전공자에게 조언한다고 생각하고, 어떤 프로젝트를 해서 포트폴리오를 남기는 게 좋은 지 포트폴리오 조언을 기준으로 해"
}

#대화 내역을 저장할 공간
messages = [system_message, 
            {"role":"assistant", "content":"대화 상대의 이름은 이형민"},
            {"role":"assistant", "content":"학위: 자동차정비 전문학사"},
            {"role":"assistant", "content":"학위: 경영학사"},
            {"role":"assistant", "content":"학위: 한국외국어대학교 경영대학원 경영학과 경영정보전공(MIS) 석사"},
            {"role":"assistant", "content":"AI/데이터분석 분야 취업 희망"}
            ]

#반복문을 통해 대화 구현
while True:
    user_input = input("사용자 전달: ")
    #대화 종료 코드: 사용자가 exit 입력 시, 대화 종료
    if user_input == "exit":
        print("즐거운 대화였습니다! 감사합니다.")
        break

    #사용자가 전달한 입력을 대화 형태로 gpt에게 전달
    messages.append({"role":"user", "content":user_input})
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages = messages
    )

    reply = completion.choices[0].message.content
    print("대답: " + reply)
    messages.append({"role":"assistant", "content":reply})