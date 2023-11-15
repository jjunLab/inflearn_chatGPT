##### 기본 정보 입력 #####
# Streamlit 패키지 추가
import streamlit as st
# OpenAI 패키기 추가
import openai
# Bard 패키지 추가
from bardapi import Bard

##### 기능 구현 함수 정리#####
# ChatGPT
def askGpt(prompt,apikey):
    client = openai.OpenAI(api_key = apikey)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}])

    return response.choices[0].message.content, response.usage.completion_tokens,response.usage.prompt_tokens 

#Bard
def askBard(prompt):
    bard = Bard(token=st.session_state["Bard_TK"],timeout=120)
    result = bard.get_answer(prompt)
    return result["choices"][0]["content"],result["choices"][1]["content"], result["choices"][2]["content"] 


##### 메인 함수 #####
def main():

    st.set_page_config(
        page_title="ChatGPT vs Bard 비교 프로그램",
        layout="wide")

    st.title('ChatGPT vs Bard 비교 프로그램🤜🤛')
    st.markdown('---')

    if "model" not in st.session_state:
        st.session_state["model"] = ""
    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""
    if "Bard_TK" not in st.session_state:
        st.session_state["Bard_TK"] = ""

    #사이드바
    with st.sidebar:
        # OpenAI API 키 입력받기
        open_apikey = st.text_input(label='OPENAI API 키', placeholder='Enter Your API Key', value='',type='password') 
        if open_apikey:
            st.session_state["OPENAI_API"] = open_apikey 
            openai.api_key = open_apikey

        #OpenAI 모델 선정하기
        st.session_state["model"] = st.radio(label="GPT 모델",options=['gpt-4', 'gpt-3.5-turbo'])
        st.markdown('---')
        
        #bard 토큰받기
        bard_token = st.text_input(label='Bard Token 키', placeholder='Enter Your Bard Token', value='',type='password')
        if bard_token:
            st.session_state["Bard_TK"] = bard_token

    # 프롬프트 입력 받기
    st.header("프롬프트를 입력하세요")
    prompt = st.text_input(" ")
    st.markdown('---')

    #결과 출력
    col1, col2 =  st.columns(2)
    with col1:
        st.header("ChatGPT")
        if prompt:
            if st.session_state["OPENAI_API"]:
                result, completion_token,prompt_token  = askGpt(prompt,st.session_state["OPENAI_API"])
                st.markdown(result)
                if st.session_state["model"] == "gpt-3.5-turbo":
                    total_bill = (completion_token*0.02+prompt_token*0.015)*0.001
                    
                    st.info(f"총 사용 토큰 : {(completion_token+prompt_token)}")
                    st.info(f"금액 : {total_bill}$")
                else:
                    total_bill = (completion_token*0.06+prompt_token*0.03)*0.001
                    
                    st.info(f"총 사용 토큰 : {(completion_token+prompt_token)}")
                    st.info(f"금액 : {total_bill}$")
            else:
                st.info("OpenAI API 키를 입력하세요")

    with col2:
        st.header("Bard")
        if prompt:
            if st.session_state["Bard_TK"]:
                result1, result2,result3 = askBard(prompt)
                st.markdown("### 답변1")
                st.markdown(result1[0])
                st.markdown("### 답변2")
                st.markdown(result2[0])
                st.markdown("### 답변3")
                st.markdown(result3[0])
            else:
                st.info("Bard Token을 입력하세요")

if __name__=="__main__":
    main()
    