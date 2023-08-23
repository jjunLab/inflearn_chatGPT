import requests

PAPAGO_ID = "ID 입력" 
PAPAGO_PW = "Password 입력" 

def papago_translate(text):
     
    data = {'text' : text,
            'source' : 'en',
            'target': 'ko'}

    url = "https://openapi.naver.com/v1/papago/n2mt"
    header = {"X-Naver-Client-Id":PAPAGO_ID,
              "X-Naver-Client-Secret":PAPAGO_PW}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if(rescode==200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data
    else:
        print("Error Code:" , rescode)



text ="GPT-4 is more creative and collaborative than ever before. It can generate, edit, and iterate with users on creative and technical writing tasks, such as composing songs, writing screenplays, or learning a user??s writing style."

result = papago_translate(text)
print(result)