import streamlit as st

st.title('こんにちわ、吉村ゼミ')

name = st.text_input('名前を入力')
st.write(name)

camera = st.camera_photo('写真を撮影します')
if camera:
  st.image(camera, caption='写真', use_column_width=True)
