import streamlit as st

total = 0

num = st.text_input(" ")
if num:
    total = total+int(num)

st.title(total)

# if "total" not in st.session_state:
#     st.session_state["total"] = 0

# num = st.text_input(" ")
# if num:
#     st.session_state["total"] = st.session_state["total"]+int(num)

# st.title(st.session_state["total"])


