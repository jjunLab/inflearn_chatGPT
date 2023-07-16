##### �⺻ ���� �ҷ����� ####
# Streamlit ��Ű�� �߰�
import streamlit as st
# OpenAI ��Ű�� �߰�
import openai
# ���� ���� ��Ű�� �߰�
from googletrans import Translator
# API��û�� ���� Requests ��Ű�� �߰� 
import requests

##### ��� ���� �Լ� #####
# ChatGPT ����
def gpt_translate(messages):
    messages_prompt = [{"role": "system", "content": f'Translate the following english text into Korean. Text to translate : {messages}'}]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages_prompt)

    system_message = response["choices"][0]["message"]

    return system_message["content"]

# ���İ� ����
def papago_translate(text,PAPAGO_ID,PAPAGO_PW):

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

def google_trans(messages):
    google = Translator()
    result = google.translate(messages, dest="ko")

    return result.text

def deepl_translate(text, RapidAPI, sl="en", tl="ko"):
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

##### ���� �Լ� #####
def main():
    # �⺻ ����
    st.set_page_config(
        page_title="���� �÷��� ����",
        layout="wide")

    # session state �ʱ�ȭ
    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""

    if "PAPAGO_ID" not in st.session_state:
        st.session_state["PAPAGO_ID"] = ""

    if "PAPAGO_PW" not in st.session_state:
        st.session_state["PAPAGO_PW"] = ""

    if "RapidAPI" not in st.session_state:
        st.session_state["RapidAPI"] = ""


    # ���̵�� �� ����
    with st.sidebar:

        # Open AI API Ű �Է¹ޱ�
        st.session_state["OPENAI_API"] = st.text_input(label='OPENAI API Ű', placeholder='Enter Your API Key', value='',type='password')

        st.markdown('---')

        # PAPAGO API ID/PW �Է¹ޱ�
        st.session_state["PAPAGO_ID"] = st.text_input(label='PAPAGO API ID', placeholder='Enter PAPAGO ID', value='')
        st.session_state["PAPAGO_PW"] = st.text_input(label='PAPAGO API PW', placeholder='Enter PAPAGO PW', value='',type='password')

        st.markdown('---')

        # PAPAGO API ID/PW �Է¹ޱ�
        st.session_state["RapidAPI"] = st.text_input(label='RapidAPI', placeholder='Enter PapidAPI API Key', value='',type='password')
    
        st.markdown('---')

    # ���� 
    st.header('���� �÷��� ���ϱ� ���α׷�?')
    # ���м�
    st.markdown('---')
    st.subheader("������ �ϰ��� �ϴ� �ؽ�Ʈ�� �Է��ϼ���")
    txt = st.text_area(label="",placeholder="input English..", height=200)
    st.markdown('---')

    st.subheader("ChatGPT ���� ���")
    st.text("https://openai.com/blog/chatgpt")
    if st.session_state["OPENAI_API"] and txt:
        openai.api_key = st.session_state["OPENAI_API"]
        result = gpt_translate(txt)
        st.info(result)
    else:
        st.info('API Ű�� ��������')
    st.markdown('---')

    st.subheader("���İ� ���� ���")
    st.text("https://papago.naver.com/")
    if st.session_state["PAPAGO_ID"] and st.session_state["PAPAGO_PW"] and txt:
        result = papago_translate(txt,st.session_state["PAPAGO_ID"],st.session_state["PAPAGO_PW"])
        st.info(result)
    else:
        st.info('���İ� API ID, PW�� ��������')
    st.markdown('---')

    st.subheader("Deepl ���� ���")
    st.text("https://www.deepl.com/translator")
    if st.session_state["RapidAPI"] and txt:
        result = deepl_translate(txt,st.session_state["RapidAPI"])
        st.info(result)
    else:
        st.info('API Ű�� ��������')

    st.subheader("���� ���� ���")
    st.text("https://translate.google.co.kr/")
    if txt:
        result = google_trans(txt)
        st.info(result)
    else:
        st.info("APIŰ�� �ʿ� �����ϴ�")
    st.markdown('---')

if __name__=="__main__":
    main()
