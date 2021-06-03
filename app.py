import streamlit as st
import json
import requests
import pandas as pd

URL = "https://mgmt590-api-xiicktdcsq-uc.a.run.app/models"

st.title('Information about the existing Models')

if st.button('Show Models'):

    headers = {'Content-Type': 'application/json'}
    response = requests.request('GET', URL, headers=headers)
    res_json = response.json()
    model_li = []
    name_li = []
    tokenizer_li = []

    for i in res_json:
        model_temp = i['model']
        name_temp = i['name']
        tokenizer_temp = i['tokenizer']
        model_li.append(model_temp)
        name_li.append(name_temp)
        tokenizer_li.append(tokenizer_temp)

    # using data frame
    df = pd.DataFrame({'model': model_li,
                       'name': name_li,
                       'tokenizer': tokenizer_li})

    st.write(df)

st.title('Input a Model')

model = st.text_input('Model')
name = st.text_input('Name1')
tokenizer = st.text_input('tokenizer')

if st.button('INSERT MODEL'):

    payload = json.dumps({
        'model': model,
        'name': name,
        'tokenizer': tokenizer
    })

    headers = {'Content-Type': 'application/json'}
    response = requests.request('PUT', URL, headers=headers, data=payload)
    res_json = response.json()
    model_li = []
    name_li = []
    tokenizer_li = []

    for i in res_json:
        model_temp = i['model']
        name_temp = i['name']
        tokenizer_temp = i['tokenizer']
        model_li.append(model_temp)
        name_li.append(name_temp)
        tokenizer_li.append(tokenizer_temp)

    # using data frame
    df = pd.DataFrame({'Model': model_li,
                       'name': name_li,
                       'tokenizer': tokenizer_li})

    st.write('Model added Successfully')
    st.write(df)

st.title('Delete a Model')

model2 = st.text_input('Name')
model2 = str(model2)

if st.button('DELETE MODEL'):

    response2 = requests.delete('https://mgmt590-api-xiicktdcsq-uc.a.run.app/models', params={'model': model2})
    res_json2 = response2.json()
    model_li = []
    name_li = []
    tokenizer_li = []

    for i in res_json2:
        model_temp = i['model']
        name_temp = i['name']
        tokenizer_temp = i['tokenizer']
        model_li.append(model_temp)
        name_li.append(name_temp)
        tokenizer_li.append(tokenizer_temp)

    # using data frame
    df2 = pd.DataFrame({'Model': model_li,
                        'name': name_li,
                        'tokenizer': tokenizer_li})

    st.write('Model Deleted Successfully')

    st.write(df2)

URL2 = "https://mgmt590-api-xiicktdcsq-uc.a.run.app/answer"

st.title('Upload/Question-Answering API')

question = st.text_input('Question')
context = st.text_input('Context')
model3 = st.text_input('Model3')

datafile = st.file_uploader("Upload CSV", type=['csv'])
if datafile is not None:
    file_details = {"FileName": datafile.name, "FileType": datafile.type}

    df2 = pd.read_csv(datafile)
    # st.dataframe(df)

    question_2 = df2['question'].tolist()[0]
    context_2 = df2['context'].tolist()[0]
    model_2 = df2['model'].tolist()[0]

    if st.button('Answer Question'):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(URL2, headers=headers,
                                 data=json.dumps({'question': question_2, 'context': context_2, 'model': model_2}))
        answer_final = []
        answer_final.append(response.json()['answer'])
        model_final = []
        model_final.append(response.json()['model'])
        question_final = []
        question_final.append(response.json()['question'])
        context_final = []
        context_final.append(response.json()['context'])

        df3 = pd.DataFrame()
        df3['answer'] = answer_final
        df3['model'] = model_final
        df3['question'] = question_final
        df3['context'] = context_final
        df3['sno'] = 1

        st.write(df3)


else:

    if st.button('Answer Question'):

        payload = json.dumps({
            'question': question,
            'context': context

        })
        headers = {'Content-Type': 'application/json'}
        get_models = requests.request('GET', URL, headers=headers)
        res_json = get_models.json()
        model_li = []

        for i in res_json:
            model_temp = i['name']
            model_li.append(model_temp)

        if not model3:
            model2 = 'distilled-bert'

            response = requests.post(URL2, headers=headers, params={'model': model2}, data=payload)

            answer_final = []
            answer_final.append(response.json()['answer'])
            model_final = []
            model_final.append(response.json()['model'])
            question_final = []
            question_final.append(response.json()['question'])
            context_final = []
            context_final.append(response.json()['context'])

            df = pd.DataFrame()
            df['answer'] = answer_final
            df['model'] = model_final
            df['question'] = question_final
            df['context'] = context_final
            df['sno'] = 1

            st.write(df)

        else:
            payload = json.dumps({
                'question': question,
                'context': context})

            headers = {'Content-Type': 'application/json'}
            response = requests.post(URL2, headers=headers, params={'model': model3}, data=payload)

            answer_final = []
            answer_final.append(response.json()['answer'])
            model_final = []
            model_final.append(response.json()['model'])
            question_final = []
            question_final.append(response.json()['question'])
            context_final = []
            context_final.append(response.json()['context'])

            df = pd.DataFrame()
            df['answer'] = answer_final
            df['model'] = model_final
            df['question'] = question_final
            df['context'] = context_final
            df['sno'] = 1

            st.write(df)