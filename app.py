import requests
import json
import streamlit as st

def main():
    url = ' http://127.0.0.1:8000/'

    st.title('商品情報検索')
    select = st.selectbox('入力値',['商品コード','JANコード'])
    code = st.text_input(f'{select}を入力してください。(商品コードは８桁で)')

    if select == '商品コード':
        res = requests.get(url+'code/'+code)
        if res.status_code ==200:
            res_j = res.json()
    else:
        res = requests.get(url+'jan/'+code)
        if res.status_code == 200:
            res_j = res.json()

    if code:
        if res.status_code == 200:
            st.success('データを取得しました')
            st.json(res_j)
        else:
            st.error('データ取得に失敗しました。正しいコードを入力してください。')

if __name__ == '__main__':
    main()