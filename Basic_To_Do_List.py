import streamlit as st
from datetime import date

st.title('To-Do List')

cdt = date.today()
st.subheader('{ ' + str(cdt) + ' }')

st.markdown("## *Welcome! Plan your day ahead*.🔥")
st.image("sunrise.jpg")

st.markdown('## *Motivate yourself 💪*')
a=st.text_input('Enter a quote:')
if a!='':
    st.text('That\'s a great start!')
else:
    st.text('Give it a Try!')

st.markdown('## ***Tasks***🎯')
n = st.text_input('Enter the number of tasks:', '0')
n = int(n)

l = []
for i in range(n):
    tsk = st.text_input('Enter the task:',placeholder='Enter a task!',key=i)
    l.append(tsk)

st.markdown('## *List*')

chk=''
for j,i in enumerate(l):
    if i!='':
        chk=st.checkbox(i)
    if chk:
        st.text(f'Great! 👏\nTask {j+1} : "{i}" : IS DONE')
