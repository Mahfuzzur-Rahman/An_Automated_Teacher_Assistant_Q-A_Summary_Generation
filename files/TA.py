import termcolor
from termcolor import colored

import streamlit as st
import pandas as pd
import summary_generate
import keyword_generate
import question_generate

## Title of the site
st.title("An Automated Teacher Assistant")

## Header
st.header("AI-powered Q&A Generation and Analysis")


## Take passage input
st.subheader("Passage:")
input_msg= st.text_input(label="Input Passage", placeholder='Submit your passage here...', label_visibility='collapsed')
st.write(input_msg) # Show passage

## Next Step
proceed = st.radio(
        label= "Proceed",
        options= ('Stay in this step','Proceed to the next step'),
        horizontal=True,
        label_visibility='collapsed',)




if proceed=='Proceed to the next step':
    
    ## Generating passage summary and Ques table
    ques_summary= summary_generate.summary_main(input_msg)
    ques_keyword = keyword_generate.keyword_main(ques_summary)
   

    teacher_questions, teacher_answers = question_generate.question_main(ques_summary, ques_keyword)
    teacher_questions_cut = teacher_questions[:10]
    teacher_answers_cut = teacher_answers[:10]
    ques_table = pd.DataFrame({ 'Question Number': list(range(1,11)),'Questions': teacher_questions_cut, 'Answers' : teacher_answers_cut})

    ques_keyword_df = pd.DataFrame({'Keywords' : ques_keyword})
    ques_keyword_df = ques_keyword_df.T

    ## Show passage summary
    st.markdown("""### Passage Summary: """)
    st.write(ques_summary) 

  
    # CSS to inject contained in a string
    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """

    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    ## Show summary's keyword
    st.markdown("""### Question Summary's Keywords: """)
    st.write(ques_keyword_df) 




    ## Show Question Table
    st.markdown("""### Question Answer Table: """)
    st.table(ques_table)

    ## Show options for question
    s_q = st.radio(label= "Which qeustion do you want to check ? ", options= ('1', '2', '3','4', '5', '6', '7', '8', '9', '10','None'), index=10, help= 'Select a question no.')
    #selected_q = st.radio(label="Which qeustion do you want to check ? ", options=data, index=10, help= 'Select one question.')
    
    
    
    

    if s_q == 'None':
        st.write("You've selected: ", s_q)
    else:
        selected_q = int(s_q)
        ## Show selected question and answer
        c_ques = ques_table['Questions'][selected_q-1]
        c_ans = ques_table['Answers'][selected_q-1]
        
        st.markdown("""### Selected Question : """)
        st.write(c_ques)
        st.markdown("""### Correct Answer : """)
        st.write(c_ans)

        ## Take answer input
        input_ans= st.text_input(label="Input Answer", placeholder='Submit the answer here...')
        st.write(input_ans) # Show answer

        
        
        if st.button('Summarize'):

            ## Generating answer summary and check
            ans_summary= summary_generate.summary_main(input_ans)

            answer_keyword= keyword_generate.keyword_main(ans_summary)

            

            ## Show answer summary
            st.markdown("""### Answer Summary: """)
            st.write(ans_summary)

            answer_keyword_df = pd.DataFrame({'Keywords' : answer_keyword})
            answer_keyword_df = answer_keyword_df.T

            ## Show summary's keyword
            st.markdown("""### Answer Summary's Keywords: """)
            st.write(answer_keyword_df) 
            
