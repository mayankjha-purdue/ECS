import requests
import json
import streamlit as st

url = "https://finalssignment2-xiicktdcsq-uc.a.run.app"
st.sidebar.title("Functionalities")
a = st.sidebar.button('Answer Question')
st.sidebar.button('Edit Models')
st.sidebar.button('Upload a file')


# radio = st.sidebar.radio(label="", options=["Set A", "Set B", "Add them"])


if a:
    st.title('Question Answering Model')
    # Inputs
    question = st.text_input('Question')
    context = st.text_area('Context')

    # Execute question answering on button press
    if st.button('Display Answer'):

        payload = json.dumps({
            "question": question,
            "context": context
            })
        headers = {'Content-Type': 'application/json'}
        answerurl = url + "/answer"
        response = requests.request("POST", answerurl, headers=headers, data=payload)
        answer = response.json()['answer']

        st.success(answer)
