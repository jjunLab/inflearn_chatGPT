##### 기본 정보 입력 #####
# Streamlit 패키지 추가
import streamlit as st
# OpenAI 패키기 추가
import openai

##### 기능 구현 함수 #####
def askGpt(prompt):
    messages_prompt = [{"role": "system", "content": prompt}]
    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages_prompt)
    gptResponse = response["choices"][0]["message"]["content"]
    return gptResponse

##### 메인 함수 #####
def main():
    st.set_page_config(page_title="광고 문구 생성 프로그램")
    # 사이드바
    with st.sidebar:
        # Open AI API 키 입력받기
        open_apikey = st.text_input(label='OPENAI API 키', placeholder='Enter Your API Key', value='',type='password')
        # 입력받은 API 키 표시
        if open_apikey:
            openai.api_key  = open_apikey 
        st.markdown('---')

    #메인공간
    st.header("🎸광고 문구 생성 프로그램")
    st.markdown('---')

    col1, col2 =  st.columns(2)
    with col1:
        name = st.text_input("제품명",placeholder=" ")
        strenghth = st.text_input("제품 특징",placeholder=" ")
        keyword = st.text_input("필수 포함 키워드",placeholder=" ")
    with col2:  
        com_name = st.text_input("브랜드 명",placeholder="Apple, 올리브영..")
        tone_manner = st.text_input("톤엔 메너",placeholder="발랄하게, 유머러스하게, 감성적으로..")
        value = st.text_input("브랜드 핵심 가치",placeholder="필요 시 입력")

    if st.button("광고 문구 생성"):
        prompt = f'''
        아래 내용을 참고해서 1~2줄짜리 광구문구 5개 작성해줘
        - 제품명: {name}
        - 브렌드 명: {com_name}
        - 브렌드 핵심 가치: {value}
        - 제품 특징: {strenghth}
        - 톤엔 매너: {tone_manner}
        - 필수 포함 키워드: {keyword}
        '''
        st.info(askGpt(prompt))

if __name__=='__main__':
    main()