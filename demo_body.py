import base64
import json
import http.client
import random
import streamlit as st

class LKD2CompletionExecutor:
    def __init__(self, host, api_key, api_key_primary_val, request_id):
        self._host = host
        self._api_key = api_key
        self._api_key_primary_val = api_key_primary_val
        self._request_id = request_id

    def _send_request(self, completion_request):
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'X-NCP-CLOVASTUDIO-API-KEY': self._api_key,
            'X-NCP-APIGW-API-KEY': self._api_key_primary_val,
            'X-NCP-CLOVASTUDIO-REQUEST-ID': self._request_id
        }

        conn = http.client.HTTPSConnection(self._host)
        conn.request('POST', '/testapp/v1/completions/LK-D2', json.dumps(completion_request), headers)
        response = conn.getresponse()
        result = json.loads(response.read().decode(encoding='utf-8'))
        conn.close()
        return result

    def execute(self, completion_request):
        res = self._send_request(completion_request)
        if res['status']['code'] == '20000':
            return res['result']['text']
        else:
            return 'Error'

def make_body_copy_example():
    example_lst = [example]
    
    return example_lst

LKD2completion_executor = LKD2CompletionExecutor(
        host='clovastudio.apigw.ntruss.com',
        api_key='api_key',
        api_key_primary_val = 'api_key_primary_val',
        request_id='request_id'
    )

example = ""
example_lst = make_body_copy_example()
for tmp_example in example_lst:
    example += tmp_example
    
request_data = {
            'text': 'final_text',
            'maxTokens': 500,
            'temperature': 0.6,
            'topK': 0,
            'topP': 0.8,
            'repeatPenalty': 5.0,
            'start': '',
            'restart': '',
            'stopBefore': ["상품"],
            'includeTokens': False,
            'includeAiFilters': True,
            'includeProbs': False
        }

with st.form("body_copy"):
    st.title("AiSAC(아이작) 광고 카피 제작 서비스(N) - 바디카피")
    
    name = st.text_input(label="상품", placeholder = "ex) 썬크림")
    key = st.text_input(label="주요 키워드", placeholder = "ex) 끈적이지 않는, 1+1")
    ToneManner = st.selectbox("톤앤매너", ["기본", "리뷰", "행동촉구"])
    iter_num = st.selectbox("생성할 결과 갯수를 입력해주세요", [1, 2, 3])
    
    if st.form_submit_button(label='Submit'):
        command = f"상품, 주요 키워드가 포함된 {ToneManner} 마케팅 메시지를 생성합니다."
        final_text = command + "\n" + example + f"상품:{name}\n    주요 키워드:{key}\n    톤앤매너:{ToneManner}\n    마케팅 메시지:"
        
        request_data['text'] = final_text
        
        for i in range(iter_num):
            LKD2response_text = LKD2completion_executor.execute(request_data)

            output = LKD2response_text.replace(final_text, "").replace("상품", "")

            st.write(output)
