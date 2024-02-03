from transformers import pipeline 
import streamlit as st
from PIL import Image 

#tab name and favicon
st.set_page_config(page_title='Text Summarizer', page_icon='📖', layout='centered')

#import pipeline
summarizer=pipeline('summarization')



#image=Image.open('image.png')
#st.image('bot.gif',use_column_width=True)

st.write("""
# Text Summarizer 📝 
Using Hugging Face Transformers 🤗
""")
cols = st.columns(2)
with cols[0].form(key='my_form'):

    input=st.text_area('Enter your Text',height=300)
    columns = st.columns(2)
    #left_column, right_column=st.beta_columns(2)

    min_words=columns[0].number_input('Minimum words',value=30)
    max_words=columns[1].number_input('Maximum words',value=130)
    submit_button = st.form_submit_button('Summarize!')


if submit_button:
    summary=summarizer(input,max_length=max_words, min_length=min_words, do_sample=False)
    cols[1].subheader('Summarized text:-')
    cols[1].info(summary[0]['summary_text'])
    cols[1].write('**Length:** '+str(len(summary[0]['summary_text'].split(' ')))+' words')



