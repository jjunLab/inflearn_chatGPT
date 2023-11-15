import openai
import urllib

API_KEY = "api key"
client = openai.OpenAI(api_key = API_KEY)

response = client.images.generate(
  model="dall-e-2",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)
# size : "256x256", "512x512","1024x1024" 
# price : 0.016$, 0.018$,0.02$

image_url = response.data[0].url
urllib.request.urlretrieve(image_url, "test.jpg")
print(image_url)
