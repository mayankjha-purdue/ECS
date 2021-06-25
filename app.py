import webbrowser

import streamlit as st
import pandas as pd
from PIL import Image
import streamlit.components.v1 as components
import time



def get_category(score):
    if score < 6:
        return "None to Minimal"
    elif score >= 6 and score < 11:
        return "Mild : Watchful waiting; repeat PHQ-9 at follow-up"
    elif score >= 11 and score < 16:
        return "Moderate : Treatment plan, consider counseling, follow-up and/or pharmacotherapy"
    elif score >= 16 and score < 21:
        return "Moderately severe : Active treatment with pharmacotherapy and/or psychotherapy"
    elif score >= 21:
        return "Severe : Immediate initiation of pharmacotherapy and, if severe impairment or poor response to therapy, expedited referral to a mental health specialist for psychotherapy and/or collaborative management"


def calculate_score(q1):
    if (q1 == 'Not at all'):
        return 0
    elif (q1 == 'Several days'):
        return 1
    elif (q1 == 'More than half the days'):
        return 2
    elif (q1 == 'Nearly every day'):
        return 3


st.sidebar.title("Mental Health Help")

myrad = st.sidebar.radio("", (
'My Profile', 'Company statistics', 'Take Survey', 'Find a Provider', 'Advanced Survey', 'Self Help'))

if myrad == 'My Profile':
    st.title('My profile')
    col1, col2, col3 = st.beta_columns([6, 10, 1])
    image = Image.open('profilepic.png')
    with col1:
        st.write("")
    with col2:
        st.image(image, width=200, use_column_width=False)
    with col3:
        st.write("")
    st.markdown(""" <style> .big-font { font-size:30px !important; } </style> """, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: black;'>Hello Merry Foi</h1>", unsafe_allow_html=True)
    st.markdown(""" <style> .medium-font { font-size:20px !important; } </style> """, unsafe_allow_html=True)
    st.markdown('<p class="medium-font">Employee ID: E1</p>', unsafe_allow_html=True)
    st.markdown('<p class="medium-font">Gender: Female</p>', unsafe_allow_html=True)
    st.markdown('<p class="medium-font">Date of Birth: 05/24/1982</p>', unsafe_allow_html=True)
    st.markdown('<p class="medium-font">Designation: Level 1</p>', unsafe_allow_html=True)
    st.markdown('<p class="medium-font">Manager ID: E7</p>', unsafe_allow_html=True)
    st.markdown('<p class="medium-font">Zip Code: 83433</p>', unsafe_allow_html=True)

if myrad == 'Take Survey':
    st.title('Survey')
    depression_score = 0
    q1 = st.radio("Little interest or pleasure in doing things",
                  ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    depression_score = depression_score + calculate_score(q1)
    q2 = st.radio("Feeling down, depressed, or hopeless",
                  ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    depression_score = depression_score + calculate_score(q2)
    q3 = st.radio("Trouble falling or staying asleep, or sleeping too much",
                  ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    depression_score = depression_score + calculate_score(q3)
    q4 = st.radio("Feeling tired or having little energy",
                  ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    depression_score = depression_score + calculate_score(q4)
    q5 = st.radio("Poor appetite or overeating",
                  ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    depression_score = depression_score + calculate_score(q5)
    q6 = st.radio("Feeling bad about yourself — or that you are a failure or have let yourself or your family down",
                  ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    depression_score = depression_score + calculate_score(q6)
    q7 = st.radio("Trouble concentrating on things, such as reading the newspaper or watching television",
                  ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    depression_score = depression_score + calculate_score(q7)
    q8 = st.radio(
        "Moving or speaking so slowly that other people could have noticed? Or the opposite — being so fidgety or restless that you have been moving around a lot more than usual",
        ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    depression_score = depression_score + calculate_score(q8)
    q9 = st.radio("Feeling nervous, anxious or on edge",
                  ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    depression_score = depression_score + calculate_score(q9)
    anxiety_score = 0
    q10 = st.radio("Not being able to stop or control worrying",
                   ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    anxiety_score = anxiety_score + calculate_score(q10)
    q11 = st.radio("Worrying too much about different things",
                   ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    anxiety_score = anxiety_score + calculate_score(q11)
    q12 = st.radio("Trouble relaxing",
                   ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    anxiety_score = anxiety_score + calculate_score(q12)
    q13 = st.radio("Being so restless that it is hard to sit still",
                   ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    anxiety_score = anxiety_score + calculate_score(q13)
    q14 = st.radio("Becoming easily annoyed or irritable",
                   ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    anxiety_score = anxiety_score + calculate_score(q14)
    q15 = st.radio("Feeling afraid as if something awful might happen",
                   ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    anxiety_score = anxiety_score + calculate_score(q15)
    q16 = st.radio("Thoughts that you would be better off dead or of hurting yourself in some way",
                   ('Not at all', 'Several days', 'More than half the days', 'Nearly every day'))
    anxiety_score = anxiety_score + calculate_score(q16)

    if st.button('Submit'):
        st.slider('Your depression level is: ', 0, 27, depression_score)
        st.markdown(get_category(depression_score) + " depression")
        st.slider('Your anxiety level is: ', 0, 27, anxiety_score)
        st.markdown(get_category(anxiety_score) + " anxiety")

if myrad == 'Company statistics':
    st.title('Employee Insights')
    html_temp = """<div class='tableauPlaceholder' id='viz1624574613819' style='position: relative'><noscript><a href='#'><img alt='Depression Status ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;De&#47;DepressionStatus&#47;Sheet5&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='DepressionStatus&#47;Sheet5' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;De&#47;DepressionStatus&#47;Sheet5&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1624574613819');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp, width=1000, height=1000)
    html_temp = """<div class='tableauPlaceholder' id='viz1624574734338' style='position: relative'><noscript><a href='#'><img alt='Anxiety Status ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;An&#47;AnxietyStatus&#47;Sheet52&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='AnxietyStatus&#47;Sheet52' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;An&#47;AnxietyStatus&#47;Sheet52&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1624574734338');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp, width=1000, height=1000)

if myrad == 'Self Help':
    image1 = Image.open('/Users/saksheeagarwal/Desktop/try.png')
    st.image(image1, width=400)
    # html = f"<a href='https://screening.mhanational.org/diy/'><img src='data:image/png;base64,{'/Users/saksheeagarwal/Desktop/try.png'}></a>"
    # st.markdown(html, unsafe_allow_html=True)
    # st.markdown('[![](/Users/saksheeagarwal/Desktop/try on your own.png)](https://screening.mhanational.org/diy/)')
    st.write("[Things to try on your own](https://screening.mhanational.org/diy/)")
    st.write("[Connect with others](https://screening.mhanational.org/connect/)")
    st.write("[Find a provider](https://screening.mhanational.org/get-help/)")
    st.write("[Learn about treatments](https://screening.mhanational.org/treatment/)")

if myrad == 'Find a Provider':
    pin = st.text_input('Enter your pincode')
    if (pin == '47906'):
        st.text('Finding providers near you...')
        time.sleep(2)
        image = Image.open('/Users/saksheeagarwal/Downloads/googlemap.png')
        st.image(image, use_column_width=True)

if myrad == 'Advanced Survey':
    text = """You can make use of our Chatbot MAX to feel better , click on chat button to start right away. You can chat with M.A.X. when you feel the need to share your feelings - the good and the bad. Your mental health is at least as important as your physical health. Therefore, you should take good care of it. Sadly, mental health disorders are not uncommon. If the threshold to talk to a human therapist is too high, you can always talk to M.A.X. The first step is always the hardest, M.A.X. focuses on making this step easier. The goal of M.A.X. is to make mental health care more accessible."""

    st.markdown(text)

    if st.button("Talk To MAX"):
        url = 'http://www.corticare.online/'
        webbrowser.open_new_tab(url)
