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

def make_head_copy_example():
    example_lst = [
        """

    상품:현대자동차
    주요 키워드:안전,가족
    톤앤매너:기본
    마케팅 메시지:당신 곁엔 언제나 든든한 차가 있습니다. 매일매일 사랑하는 사람들을 지켜줄 수 있도록 더 튼튼하게 만들어졌습니다.""",

        """

    상품:멀티비타민
    주요 키워드:에너지
    톤앤매너:기본
    마케팅 메시지:멀티비타민으로 피로를 날려버리고 에너지 충전! 멀티비타민은 건강한 라이프스타일을 위한 필수 아이템입니다.""",

        """

    상품:다짐 필라테스
    주요 키워드:무료 레슨 체험
    톤앤매너:기본
    마케팅 메시지:건강한 변화를 위한 첫 걸음, 다짐 필라테스의 무료 레슨 체험은 당신의 몸을 더욱 아름답게 가꿀 수 있는 출발점입니다.""",

        """

    상품:인터파크 동남아투어 패키지
    주요 키워드:특별 혜택 3종 세트
    톤앤매너:기본
    마케팅 메시지:인터파크 동남아투어 패키지로 떠나는 설렘 가득한 여행, 특별 혜택 3종 세트로 더욱 특별해 집니다.""",
        
        """

    상품:현대자동차
    주요 키워드:안전, 가족
    톤앤매너:리뷰
    마케팅 메시지:현대자동차의 안전한 운전 환경과 가족 중심의 디자인은 정말 감명 깊어요. 가족 모두가 함께하는 여정을 안심하며 즐길 수 있어서 좋아요.""",

        """

    상품:멀티비타민
    주요 키워드:에너지
    톤앤매너:리뷰
    마케팅 메시지:원래 건강기능식품 같은 거 잘 안 챙겨 먹는데 이건 꼭 먹어요. 야근과 회식 잦은 직장인들에게 필수템! 확실히 체력적으로 힘든게 덜 하네요.""",

        """

    상품:다짐 필라테스
    주요 키워드:휴식
    톤앤매너:리뷰
    마케팅 메시지:무료 체험을 통해 다짐 필라테스의 매력을 느낄 수 있어요. 전문 강사와 함께 몸과 마음의 균형을 찾아낼 수 있어요.""",

        """

    상품:인터파크 동남아투어 패키지
    주요 키워드:특별 혜택 3종 세트
    톤앤매너:리뷰
    마케팅 메시지:특별 혜택 3종 세트로 더욱 특별한 인터파크 동남아투어 패키지! 여행을 더욱 풍성하게 만들어준 최고의 선택이에요.""",
        
        """

    상품:현대자동차
    주요 키워드:안전, 가족
    톤앤매너:행동촉구
    마케팅 메시지:현대자동차로 안전한 카 라이프를 즐기며 가족과 함께하는 특별한 시간을 만들어보세요!""",

        """

    상품:멀티비타민
    주요 키워드:에너지
    톤앤매너:행동촉구
    마케팅 메시지:마이카인드 유기농 멀티비타민을 40% 할인된 가격으로 만나보실 수 있는 절호의 기회! 지금 바로 구입하세요!""",

        """

    상품:다짐 필라테스
    주요 키워드:무료 레슨 체험
    톤앤매너:행동촉구
    마케팅 메시지:날씬한 몸매를 원한다면 지금 바로, 다짐 필라테스에서 무료 1:1 레슨 체험을 예약하세요!""",

        """

    상품:인터파크 동남아투어 패키지
    주요 키워드:특별 혜택 3종 세트
    톤앤매너:행동촉구
    마케팅 메시지:내일까지 인터파크 동남아투어 패키지를 예약하는 분에 한해서 특별 혜택 3종 세트를 드립니다. 지금 바로 예약하세요!""",
        
        """

    상품:현대자동차
    주요 키워드:안전,가족
    톤앤매너:질문
    마케팅 메시지:현대자동차는 가족의 안전과 미래를 보장합니다. 현대자동차와 함께하면 어떤 가족의 미래를 그려볼 수 있을까요?""",

        """

    상품:멀티비타민
    주요 키워드:에너지
    톤앤매너:질문
    마케팅 메시지:매일 똑같은 피로를 견디시는 건 지루한 일이겠죠? 멀티비타민으로 변화를 만들어보세요!""",

        """

    상품:다짐 필라테스
    주요 키워드:무료 레슨 체험
    톤앤매너:질문
    마케팅 메시지:무료 레슨 체험으로 다짐 필라테스의 매력을 직접 확인해 보실래요? 몸과 마음을 동시에 건강하게 가꾸는 방법을 알려드립니다.""",

        """

    상품:인터파크 동남아투어 패키지
    주요 키워드:특별 혜택 3종 세트
    톤앤매너:질문
    마케팅 메시지:특별 혜택 3종 세트가 더해진 인터파크 동남아투어 패키지, 당신은 이번 기회를 통해 어떤 특별한 순간을 기대하시나요?""",
        
        """

    상품:현대자동차
    주요 키워드:안전,가족
    톤앤매너:언어유희
    마케팅 메시지:내 이야기 안 듣고 공대리 지금 모 봐? 모 봐? 모바~일로 바로 자동차 보험 알아봤죠!""",

        """

    상품:멀티비타민
    주요 키워드:에너지
    톤앤매너:언어유희
    마케팅 메시지:비타민이 없어도 힘을 낼 수는 있지만, 멀티비타민이 있으면 에너지가 폭발해요.""",

        """

    상품:다짐 필라테스
    주요 키워드:무료 레슨 체험
    톤앤매너:언어유희
    마케팅 메시지:무료 레슨 체험하러 다짐 필라테스로 Go Go! 다짐 필라테스와 함께하니 피곤함은 어느새 어디로?""",

        """

    상품:인터파크 동남아투어 패키지
    주요 키워드:특별 혜택 3종 세트
    톤앤매너:언어유희
    마케팅 메시지:특별 혜택 3종 세트로 더욱 특별해진 인터파크 동남아투어 패키지, "집에 돌아가고 싶지 않은 휴가" 완성!

    """
    ]
    
    return example_lst

LKD2completion_executor = LKD2CompletionExecutor(
        host='clovastudio.apigw.ntruss.com',
        api_key='NTA0MjU2MWZlZTcxNDJiY39NiD4ZzukE8hYO+doV6gqaf2GOSDWivVGYCoQzm2nGm3fdq7Kx70Oj0Un/A0bZfVERSl6a8X7tPz74IE9wVcX4H67Bo3Klyzvjy/LDAk0p8dRc+gw0JC9uVIpRSXw0OjlCObEX7Ayv9R7r5FVMz7Cu3GXA5zCV5b3UohSmWkvILqrf2L9uH8VgVxkr3zp7LclyTgOAVRujZ/0WPSLqsKU=',
        api_key_primary_val = 'lbAIyG9RaW7AEEqE5Rl1ZqJPozLr3jJeXNhS5k1b',
        request_id='fa49d3a5891245b3a29e01bc8d1d9651'
    )

example = ""
example_lst = make_head_copy_example()
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
    st.title("AiSAC(아이작) 광고 카피 제작 서비스(N) - 헤드카피")
    
    name = st.text_input(label="상품", placeholder = "ex) 썬크림")
    key = st.text_input(label="주요 키워드", placeholder = "ex) 끈적이지 않는, 1+1")
    ToneManner = st.selectbox("톤앤매너", ["기본", "리뷰", "행동촉구", "질문", "언어유희"])
    iter_num = st.selectbox("생성할 결과 갯수를 입력해주세요", [1, 2, 3])
    
    if st.form_submit_button(label='Submit'):
        command = f"상품, 주요 키워드가 포함된 {ToneManner} 마케팅 메시지를 생성합니다."
        final_text = command + "\n" + example + f"상품:{name}\n    주요 키워드:{key}\n    톤앤매너:{ToneManner}\n    마케팅 메시지:"
        
        request_data['text'] = final_text
        
        for i in range(iter_num):
            LKD2response_text = LKD2completion_executor.execute(request_data)

            output = LKD2response_text.replace(final_text, "").replace("상품", "")

            st.write(output)
