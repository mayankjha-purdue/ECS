import streamlit as st
import json
import requests
import pandas as pd
import seaborn as sns
import sqlite3, csv

conn = sqlite3.connect('data.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS responses (eid, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, phqtotal, gadtotal);") # use your column names here

with open('Data_responses.csv','r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['Employee_ID'], i['PHQ-9-Q1'], i['PHQ-9-Q2'], i['PHQ-9-Q3'], i['PHQ-9-Q4'], i['PHQ-9-Q5'], i['PHQ-9-Q6'], i['PHQ-9-Q7'], i['PHQ-9-Q8'], i['PHQ-9-Q9'], i['GAD-7-Q1'], i['GAD-7-Q2'], i['GAD-7-Q3'], i['GAD-7-Q4'], i['GAD-7-Q5'], i['GAD-7-Q6'], i['GAD-7-Q7'], i['PHQ_TOTAL'], i['GAD_TOTAL']) for i in dr]

cur.executemany("INSERT INTO responses (eid, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, phqtotal, gadtotal) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
conn.commit()
conn.close()


st.sidebar.title("Mental Health Help")

myrad = st.sidebar.radio("", ('My Profile', 'Company statistics', 'Take Survey', 'Schedule Appointment', 'Advanced Survey', 'Self Help', 'Settings'))

if myrad == 'My Profile':
    st.title('My profile')

if myrad == 'Take Survey':
    st.title('Survey')
    q1 = st.radio("Little interest or pleasure in doing things", ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    q2 = st.radio("Feeling down, depressed, or hopeless", ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    q3 = st.radio("Trouble falling or staying asleep, or sleeping too much", ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    q4 = st.radio("Feeling tired or having little energy", ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    q5 = st.radio("Poor appetite or overeating", ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    q6 = st.radio("Feeling bad about yourself — or that you are a failure or have let yourself or your family down", ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    q7 = st.radio("Trouble concentrating on things, such as reading the newspaper or watching television", ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    q8 = st.radio("Moving or speaking so slowly that other people could have noticed? Or the opposite — being so fidgety or restless that you have been moving around a lot more than usual", ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    q9 = st.radio("Feeling nervous, anxious or on edge", ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    q10 = st.radio("Not being able to stop or control worrying", ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    q11 = st.radio("Worrying too much about different things", ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    q12 = st.radio("Trouble relaxing", ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    q13 = st.radio("Being so restless that it is hard to sit still", ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    q14 = st.radio("Becoming easily annoyed or irritable", ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    q15 = st.radio("Feeling afraid as if something awful might happen", ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    q16 = st.radio("Thoughts that you would be better off dead or of hurting yourself in some way", ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))

#
if myrad == 'Company Statistics':
    st.title('Statistics')
    df = pd.read_csv('Data_responses.csv')
    s1 = pd.Series(df['PHQ_TOTAL'])
    s2 = pd.Series(df['GAD_TOTAL'])
    t1=s1.sum()
    t2 = s2.sum()
    data = [['PHQ_TOTAL', t1], ['GAD_TOTAL', t2]]

    df1 = pd.DataFrame(data, columns=['PHQ_TOTAL', 'GAD_TOTAL'])
    df1.head()
    st.bar_chart(df1)
# if myrad== 'Answer Question' :

