import streamlit as st
def pyread(fnm):
    with open(fnm, "r") as q:
        pq=q.read()
    return pq
st.title('Python Problem Statements')
st.markdown('#  *Question 1*')
st.text('WAP in Python to print the following pattern taking user input for number of rows.')
st.text('''1
2 3
4 5 6
7 8 9 10
11 12 13 14 15''' )
st.code(pyread('Pattern1.py'))
st.markdown('---')
st.markdown('#  *Question 2*')
st.text('WAP in Python to print the following pattern taking user input for number of rows.')
st.text('''XOXOX
XOXO
XOX
XO
X''' )
st.code(pyread('Pattern2.py'))
st.markdown('---')
st.markdown('#  *Question 3*')
st.text('WAP in Python to print the following pattern taking user input for number of rows.')
st.text('''*
**
***
****
****
***
**
*''' )
st.code(pyread('Pattern3.py'))
st.markdown('---')
st.markdown('#  *Question 4*')
st.text('''WAP in Python to print find the most repetitive element from a user input list.
If list has more than one elements with same frequency print the largest of them.''')
st.text('''If user input is [1,2,2,3,3,3,4] the output should be '3' 
and if user input is [1,1,2,2,3] the output should be '2'.''' )
st.code(pyread('Pattern4.py'))