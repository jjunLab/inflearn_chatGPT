from fastapi import Request, FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "TelegramChatbot"}

@app.post("/chat")
async def chat(request: Request):
    telegramrequest = await request.json()
    print(telegramrequest)
    return  0 
