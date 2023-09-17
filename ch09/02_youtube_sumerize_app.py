##### 기본 정보 입력 #####
import streamlit as st
# URL 분석을 위해 추가
import re
# Langchain 패키지 추가
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
#번역을 위해 추가
from googletrans import Translator

##### 기능 구현 함수 #####
# 영어 번역
def google_trans(messages):
    google = Translator()
    result = google.translate(messages, dest="ko")

    return result.text

# Youtube URL 체크
def youtube_url_check(url):
    pattern = r'^https:\/\/www\.youtube\.com\/watch\?v=([a-zA-Z0-9_-]+)(\&ab_channel=[\w\d]+)?$'
    match = re.match(pattern, url)
    return match is not None

##### 메인 함수 #####
def main():

    #기본 설정
    st.set_page_config(page_title="YouTube Summerize", layout="wide")

    # session state 초기화
    if "flag" not in st.session_state:
        st.session_state["flag"] = True
    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""
    if "summerize" not in st.session_state:
        st.session_state["summerize"] = ""

    #제목
    st.header(" 📹영어 YouTube 내용 요약/대본 번역기")
    st.markdown('---')
    #URL 입력받기
    st.subheader("YouTube URL을 입력하세요")
    youtube_video_url = st.text_input("  ",placeholder="https://www.youtube.com/watch?v=**********")

    #사이드바 생성
    with st.sidebar:
        # Open AI API 키 입력받기
        open_apikey = st.text_input(label='OPENAI API 키', placeholder='Enter Your API Key', value='',type='password')
        
        # 입력받은 API 키 표시
        if open_apikey:
            st.session_state["OPENAI_API"] = open_apikey 
        st.markdown('---')

    

    if len(youtube_video_url)>2:
        if not youtube_url_check(youtube_video_url):
            st.error("YouTube URL을 확인하세요.")
        else:

            width = 50
            side = width/2
            _, container, _ = st.columns([side, width, side])
            # 입력받은 유튜브 영상 보여주기
            container.video(data=youtube_video_url)
            
            # 대본 추출하기
            loader = YoutubeLoader.from_youtube_url(youtube_video_url)
            transcript = loader.load()
        
            
            st.subheader("요약 결과")
            if st.session_state["flag"]:
                # LLM 모델 설정
                llm = ChatOpenAI(temperature=0,
                        openai_api_key=st.session_state["OPENAI_API"],
                        max_tokens=3000,
                        model_name="gpt-3.5-turbo",
                        request_timeout=120
                    )
                
                # 요약 프롬프트 설정
                prompt = PromptTemplate(
                    template="""Summarize the youtube video whose transcript is provided within backticks \
                    ```{text}```
                    """, input_variables=["text"]
                )
                combine_prompt = PromptTemplate(
                    template="""Combine all the youtube video transcripts  provided within backticks \
                    ```{text}```
                    Provide a concise summary between 8 to 10 sentences.
                    """, input_variables=["text"]
                )

                # 대본 쪼개기
                text_splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=0)
                text = text_splitter.split_documents(transcript)

                #요약 실행
                chain = load_summarize_chain(llm, chain_type="map_reduce", verbose=False,
                                                map_prompt=prompt, combine_prompt=combine_prompt)
                st.session_state["summerize"] = chain.run(text)
                st.session_state["flag"]=False
            st.success(st.session_state["summerize"])
            #번역하기   
            transe = google_trans(st.session_state["summerize"])
            st.subheader("요약 번역 결과")
            st.info(transe)
            
            #대본 번역
            st.subheader("대본 번역하기")  
            if st.button("대본 번역실행"):
                transe = google_trans(transcript[0])
                st.markdown(transe)

if __name__=="__main__":
    main() 
