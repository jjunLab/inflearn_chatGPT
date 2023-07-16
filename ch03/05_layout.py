import streamlit as st

# 기본 설정
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
)


# # 세로로 나누기
# col1, col2, col3 = st.columns(3)

# with col1:
#    st.header("A cat")
#    st.image("https://static.streamlit.io/examples/cat.jpg")

# with col2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg")

# with col3:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg")


# st.video("https://www.youtube.com/watch?v=pSUydWEqKwE")

# 간격 비율 조정 
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
   st.video("https://www.youtube.com/watch?v=pSUydWEqKwE")

# 사이드바
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )


#탭 생성
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)