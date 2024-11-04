#ElevenLabs를 사용한 음성 합성 프로그램

import os
import requests
from pydub import AudioSegment
from pydub.playback import play
import io
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# .env 파일에서 API 키와 URL 가져오기
api_key = os.getenv("ELEVEN_API_KEY")
url = os.getenv("ELEVEN_API_URL")

#설정 가능한 변수
output_filename = "output_audio.mp3"

headers = {
    "xi-api-key": api_key,
    "Content-Type": "application/json"
}

# 문장을 입력받습니다.
text = input("생성할 텍스트를 입력하세요: ")

# 음성 생성 요청을 보냅니다.
data = {
    "text": text,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.3,
        "similarity_boost": 1,
        "style": 1,
        "use_speaker_boost": True
    }
}

response = requests.post(url, json=data, headers=headers, stream=True)

if response.status_code == 200:
    audio_content = b""
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            audio_content += chunk

    segment = AudioSegment.from_mp3(io.BytesIO(audio_content))
    segment.export(output_filename, format="mp3")
    print(f"Success! Wrote audio to {output_filename}")

    # 오디오를 재생합니다.
    play(segment)
else:
    print(f"Failed to save file: {response.status_code}")
