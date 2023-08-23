##### 기본 정보 입력 #####
import streamlit as st
# OpenAI 패키기 추가
import openai
# 인스타그램 패키기 추가
from instagrapi import Client
#이미지 처리
from PIL import Image
import urllib
#구글 번역
from googletrans import Translator

##### 기능 구현 함수 #####
# 영어로 번역
def google_trans(messages):
    google = Translator()
    result = google.translate(messages, dest="en")

    return result.text

# 인스타 업로드
def uploadinstagram(description):
    cl = Client()
    cl.login(st.session_state["instagram_ID"], st.session_state["instagram_Password"])
    cl.photo_upload("instaimg_resize.jpg" , description)

# ChatGPT에게 질문/답변받기
def getdescriptionFromGPT(topic, mood):
    prompt = f'''
Write me the Instagram post description or caption in just a few sentences for the post 
-topic : {topic}
-Mood : {mood}
Format every new sentence with new lines so the text is more readable.
Include emojis and the best Instagram hashtags for that post.
The first caption sentence should hook the readers.
write all output in korean.'''
    messages_prompt = [{"role": "system", "content": prompt}]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages_prompt)

    system_message = response["choices"][0]["message"]
    return system_message["content"]

# DALLE.2에게 질문/그림 URL 받기
def getImageURLFromDALLE(topic,mood):
    t_topic = google_trans(topic)
    t_mood = google_trans(mood)
    prompt_ = f'Draw picture about {t_topic}. picture Mood is {t_mood}'
    print(prompt_)
    response = openai.Image.create(prompt=prompt_,n=1,size="512x512")

    image_url = response['data'][0]['url']
    urllib.request.urlretrieve(image_url, "instaimg.jpg")

##### 메인 함수 #####
def main():

    # 기본 설정
    st.set_page_config(page_title="Instabot", page_icon="?")
    
    # session state 초기화
    if "description" not in st.session_state:
        st.session_state["description"] = ""

    if "flag" not in st.session_state:
        st.session_state["flag"] = False

    if "instagram_ID" not in st.session_state:
        st.session_state["instagram_ID"] = ""

    if "instagram_Password" not in st.session_state:
        st.session_state["instagram_Password"] = ""

    # 제목 
    st.header('인스타그램 포스팅 생성기')
    # 구분선
    st.markdown('---')

    # 기본 설명
    with st.expander("인스타그램 포스팅 생성기", expanded=True):
        st.write(
        """     
        - 인스타그램 포스팅 생성는 UI는 스트림릿을 활용하여 만들었습니다.
        - 이미지는 OpenAI의 Dall.e 2 를 활용하여 생성합니다. 
        - 포스팅 글은 OpenAI의 GPT 모델을 활용하여 생성합니다. 
        - 자동 포스팅은 instagram API를 활용합니다.
        """
        )

        st.markdown("")

    # 사이드바 바 생성
    with st.sidebar:

        # Open AI API 키 입력받기
        open_apikey = st.text_input(label='OPENAI API 키', placeholder='Enter Your API Key', value='',type="password")

        # 입력받은 API 키 표시
        if open_apikey:
            openai.api_key = open_apikey    
        

        st.markdown('---')

    topic = st.text_input(label="주제", placeholder="축구, 인공지능...")
    mood = st.text_input(label="분위기 (e.g. 재미있는, 진지한, 우울한)",placeholder="재미있는")

    if st.button(label="생성",type="secondary") and not st.session_state["flag"]:

        with st.spinner('생성 중'):
            st.session_state["description"] = getdescriptionFromGPT(topic,mood)
            getImageURLFromDALLE(topic,mood)
            st.session_state["flag"] = True

    if st.session_state["flag"]:
        image = Image.open('instaimg.jpg')  
        st.image(image)
        # st.markdown(st.session_state["description"])
        txt = st.text_area(label = "Edit Description",value  = st.session_state["description"],height=50)
        st.session_state["description"] = txt

        st.markdown('인스타그램 ID/PW')
        # 인스타그램 ID 입력받기
        st.session_state["instagram_ID"] = st.text_input(label='ID', placeholder='Enter Your ID', value='')
        # 인스타그램 비밀번호
        st.session_state["instagram_Password"] = st.text_input(label='Password',type='password', placeholder='Enter Your Password', value='')

        if st.button(label='업로드'):
            image = Image.open("instaimg.jpg")
            image = image.convert("RGB")
            new_image = image.resize((1080, 1080))
            new_image.save("instaimg_resize.jpg")
            uploadinstagram(st.session_state["description"])
            st.session_state["flag"] = False

if __name__=="__main__":
    main()