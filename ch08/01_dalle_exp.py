import openai
import urllib

openai.api_key = "api-key"
response = openai.Image.create(prompt="A futuristic city at night",n=1,size="512x512")
# size : "256x256", "512x512","1024x1024" 
# price : 0.016$, 0.018$,0.02$

image_url = response['data'][0]['url']
urllib.request.urlretrieve(image_url, "test.jpg")
print(image_url)
