import os

import streamlit as st
import pandas as pd
##import plotly.graph_objs as go
import streamlit.components.v1 as stc
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')
font = {'family': 'meiryo'}
matplotlib.rc('font', **font)


#st.video("https://www.youtube.com/watch?v=RCuGLRtggrI&t=6s")

#st.snow()


#st.title('My app')

#df = pd.DataFrame({
#    'first column': [1, 2, 3, 4],
#    'second column': [10, 20, 30, 40]
#})

#st.table(df)

#st.markdown('# Markdown documents')


#values = st.slider(
#    'Select a range of values',
#   0.0, 100.0, (25.0, 75.0))
#st.write('Values:', values)

file = "201801_Punctuality_Statistics_Full_Analysis.csv"

file = pd.read_csv(file)
df = pd.DataFrame(file)

st.dataframe(df)

#df1 = df[['airline_name', 'origin_destination']].groupby('airline_name').count()
#df1 = df1.sort_values('origin_destination', ascending=False).head(10)

df1 = df.filter('airline_name == "RYANAIR"')

#st.dataframe(df1)

df.columns

st.text(df.columns[0])

st.latex(
r'''
S = \pi * r^2

'''
)


### Checkbox
if st.checkbox('Check it!'):
    st.write('Check please!')


## Select list
### Define select list
select_list = ['Apple', 'Orange', 'Grape']
### Choose one of them
ret = st.selectbox('Please select fruits', select_list)
### Display
st.write(ret)

### Choose plural items
ret_plural = st.multiselect('Select as many as you want', select_list)
### Display it
st.write(ret_plural)


left_col, right_col = st.beta_columns(2)

if left_col.checkbox('Select left'):
    left_col.write('Selected LEFT')

if right_col.checkbox('Select right'):
    right_col.write('Selected RIGHT!')

ret_radio = st.radio('Select 1 fruit', select_list)

st.write('Selected fruit is ', ret_radio)


ret_input_number = st.number_input('Please input number')

st.write('Input number is', ret_input_number)



