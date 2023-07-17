import requests

RapidAPI = "토큰 입력" 

def deepl_translate(text, RapidAPI=RapidAPI, sl="en", tl="ko"):
    url = "https://deepl-translator.p.rapidapi.com/translate"
    
    payload = {
        "text": text,
        "source": sl,
        "target": tl
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": RapidAPI,
        "X-RapidAPI-Host": "deepl-translator.p.rapidapi.com"
    }
    
    response = requests.request("POST", url, json=payload, headers=headers)
    return response.json()["text"]

text ="GPT-4 is more creative and collaborative than ever before. It can generate, edit, and iterate with users on creative and technical writing tasks, such as composing songs, writing screenplays, or learning a user??s writing style."

result = deepl_translate(text)
print(result)