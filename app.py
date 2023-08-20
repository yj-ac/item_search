import requests
import json
import streamlit as st

def main():
    
    # FastAPIアプリケーションのホスト名とポート番号
    fastapi_host = "http://localhost"  # FastAPIのホスト名 (例えばIPアドレスでも可)
    fastapi_port = 8000  # FastAPIのポート番号

    # APIエンドポイントのURL
    api_url = f"{fastapi_host}:{fastapi_port}/https://search_item-1-q2774845.deta.app/"
    #url = 'https://search_item-1-q2774845.deta.app/'

    st.title('商品情報検索')
    select = st.selectbox('入力値',['商品コード','JANコード'])
    code = st.text_input(f'{select}を入力してください。(商品コードは7桁で)')

    if select == '商品コード':
        res = requests.get(api_url +'code/'+code)
        if res.status_code ==200:
            res_j = res.json()
    else:
        res = requests.get(api_url +'jan/'+code)
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

