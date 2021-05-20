from typing import Optional, Text
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time 

st.title('うんこ')

st.write('プログレスバー')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.3)

'Done!!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右から無に文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('トイアワsっを描く')
#text = st.text_input('あなたの趣味は')
#'あなたの趣味は:',text

#condition = st.slider('あなたの今の調子は', 0, 100, 50)
#'コンディション:', condition


#'あなたの数字は', option, 'です'

#if st.checkbox('Show Image'):
 #   img = Image.open('sample.png')
 #  st.image(img, caption='kazuhiro sakurai', use_column_width=True)





