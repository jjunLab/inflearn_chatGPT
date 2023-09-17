##### 기본 정보 입력 #####
# Streamlit 패키지 추가
import streamlit as st
# PDF reader
from PyPDF2 import PdfReader
# Langchain 패키지들
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
# 구글 번역 API 
from googletrans import Translator

##### 기능 구현 함수 #####
def google_trans(messages):
    google = Translator()
    result = google.translate(messages, dest="ko")
    return result.text

##### 메인 함수 #####
def main():
    st.set_page_config(page_title="PDF analyzer", layout="wide")

    # 사이드바
    with st.sidebar:

        # Open AI API 키 입력받기
        open_apikey = st.text_input(label='OPENAI API 키', placeholder='Enter Your API Key', value='',type='password')
        
        # 입력받은 API 키 표시
        if open_apikey:
            st.session_state["OPENAI_API"] = open_apikey 
        st.markdown('---')
        
    # 메인공간
    st.header("PDF 내용 질문 프로그램📜")
    st.markdown('---')
    st.subheader("PDF 파일을 넣으세요")
    # PDF 파일 받기
    pdf = st.file_uploader(" ", type="pdf")
    if pdf is not None:
        # PDF 파일 텍스트 추출하기
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        # 청크 단위로 분할하기
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)

        st.markdown('---')
        st.subheader("질문을 입력하세요")
        # 사용자 질문 받기
        user_question = st.text_input("Ask a question about your PDF:")
        if user_question:
            # 임베딩/ 시멘틱 인덱스
            embeddings = OpenAIEmbeddings(openai_api_key=st.session_state["OPENAI_API"])
            knowledge_base = FAISS.from_texts(chunks, embeddings)
            
            docs = knowledge_base.similarity_search(user_question)

            # 질문하기
            llm = ChatOpenAI(temperature=0,
                    openai_api_key=st.session_state["OPENAI_API"],
                    max_tokens=2000,
                    model_name='gpt-3.5-turbo',
                    request_timeout=120
                    )
            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain.run(input_documents=docs, question=user_question)
            # 답변결과
            st.info(response)
            #한국어로 번역하기
            if st.button(label="번역하기"):
                trans = google_trans(response)
                st.success(trans)

if __name__=='__main__':
    main()