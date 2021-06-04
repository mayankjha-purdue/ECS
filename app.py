import streamlit as st
import json
import requests
import pandas as pd
import os

URL = os.environ.get("URL")

URL1=URL+"/models"
URL2=URL+"/answer"
st.sidebar.title("Functionalities")

myrad = st.sidebar.radio("Select Action", ('Add Model','Delete Model', 'Answer Question', 'View Models'))

if myrad == 'View Models':
    st.title('Existing Models')
    headers = {'Content-Type': 'application/json'}
    response = requests.request('GET', URL1, headers=headers)
    res_json = response.json()
    model= []
    name= []
    tokenizer= []

    for resp in res_json:
        model.append(resp['model'])
        tokenizer.append(resp['tokenizer'])
        name.append(resp['name'])

    # using data frame
    df = pd.DataFrame({'model': model,
                       'name': name,
                       'tokenizer': tokenizer})
    st.write(df)

if myrad == 'Add Model':
    st.title('Input a Model')
    model = st.text_input('Model')
    name = st.text_input('Name')
    tokenizer = st.text_input('Tokenizer')

    if st.button('Insert'):

        payload = json.dumps({
            'model': model,
            'name': name,
            'tokenizer': tokenizer
        })

        headers = {'Content-Type': 'application/json'}
        response = requests.request('PUT', URL1, headers=headers, data=payload)
        res_json = response.json()

        model = []
        name = []
        tokenizer = []

        for resp in res_json:
            model.append(resp['model'])
            tokenizer.append(resp['tokenizer'])
            name.append(resp['name'])

        # using data frame
        df = pd.DataFrame({'model': model,
                           'name': name,
                           'tokenizer': tokenizer})

        st.write('Model added Successfully')
        st.write(df)

if myrad == 'Delete Model':
    st.title('Delete a Model')

    model = st.text_input('Name')
    model2 = str(model)

    if st.button('Delete'):

        response = requests.delete(URL1, params={'model': model})
        res_json = response.json()
        model = []
        name = []
        tokenizer = []

        for resp in res_json:
            model.append(resp['model'])
            tokenizer.append(resp['tokenizer'])
            name.append(resp['name'])

        # using data frame
        df = pd.DataFrame({'model': model,
                           'name': name,
                           'tokenizer': tokenizer})

        st.write('Model Deleted Successfully')

        st.write(df)

if myrad== 'Answer Question' :

    st.title('Upload/Question-Answering API')

    question = st.text_input('Question')
    context = st.text_input('Context')
    model3 = st.text_input('Model')

    datafile = st.file_uploader("Upload CSV", type=['csv'])
    if datafile is not None:
        file_details = {"FileName": datafile.name, "FileType": datafile.type}

        df2 = pd.read_csv(datafile)
        # st.dataframe(df)

        question_2 = df2['question'].tolist()[0]
        context_2 = df2['context'].tolist()[0]
        payload = json.dumps({'question':question_2, 'context':context_2})
        if st.button('Answer Question'):
            headers = {'Content-Type': 'application/json'}
            response = requests.post(URL2, headers=headers,params ={'model':'distilled-bert'}, data= payload)
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
            get_models = requests.request('GET', URL1, headers=headers)
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
                response = requests.post(URL+'/answer', headers=headers, params={'model': model3}, data=payload)

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
