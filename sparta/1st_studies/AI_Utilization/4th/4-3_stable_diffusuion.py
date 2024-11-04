#Stable Diffusion 모델 예제
from diffusers import StableDiffusionPipeline
import torch

# Stable Diffusion 파이프라인 로드
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)
pipe = pipe.to("cuda")  # GPU 사용

# 텍스트 설명을 기반으로 이미지 생성
prompt = "A futuristic cityscape with flying cars at sunset"
image = pipe(prompt).images[0]

# 생성된 이미지 저장 및 출력
image.save("generated_image.png")
image.show()
