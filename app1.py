import streamlit as st

st.title('こんにちわ、吉村ゼミ')

name = st.text_input('名前を入力')
st.write(name)

st.checkbox('同意します')

adress = st.selectbox('場所を選んでください',['兵庫','大阪'])
st.write(adress)

point = st.slider('この映画を10点満点で評価してください',0,10,0)
st.write(point)

st.radio('性別を選択してください',['男性','女性'])

hobby = st.multiselect('趣味を次から選択してください',['映画','散歩','音楽'])
st.write(hobby)

list = [
  {'latitude':35.05,'longitude':135.76},
  {'latitude':35.04,'longitude':135.75}
]
st.map(list)

camera = st.camera_input('写真を撮影します')
if camera:
  st.image(camera, caption='写真', use_column_width=True)

