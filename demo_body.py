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
    example_lst = [
        """

    상품:썬크림
    주요 키워드:촉촉
    톤앤매너:기본
    마케팅 메시지:새로운 피부 관리 습관을 만들어보세요! 피부 톤을 밝게 만들어주고 동시에 촉촉함을 더해주는 톤업 썬크림으로 자신만의 매력을 뽐내보세요. 썬크림의 톤업 효과는 자연스럽게 피부를 교정하고, 촉촉함은 지친 피부를 화사하게 빛나는 피부로 되살아 나게 하여 주변의 시선을 사로잡는 답니다.""",

        """

    상품:현대자동차
    주요 키워드:안전,가족
    톤앤매너:기본
    마케팅 메시지:안전한 드라이빙으로 가족을 지켜주세요. 현대자동차는 가족의 소중함을 알고 있습니다. 현대자동차의 선진적인 안전 기술과 첨단 시스템은 길 위에서의 모든 여정을 더욱 안전하고 신뢰성 있게 만들어줍니다. 우리는 운전자와 승객의 안전을 위해 끊임없이 연구하며 혁신하고 있습니다. 가족과 함께하는 모든 순간을 더욱 특별하게 만들어줄 현대자동차와 함께하세요.""",

        """

    상품:MZ청바지
    주요 키워드:트렌디함
    톤앤매너:기본
    마케팅 메시지:지금 MZ청바지로 트렌디함을 업그레이드하세요! 젊고 모던한 스타일을 완성하는 비결은 바로 MZ청바지입니다. 더 이상 보통의 청바지로 만족하지 마세요. MZ청바지는 특별한 디자인과 섬세한 디테일로 트렌디한 분위기를 한층 업그레이드시켜줍니다. 모든 룩에 완벽하게 어울리며 스타일을 더욱 돋보이게 해줄 MZ청바지로 자신만의 유니크한 패션을 표현해보세요.""",

        """

    상품:멀티비타민
    주요 키워드:에너지
    톤앤매너:기본
    마케팅 메시지:에너지부터 건강까지, 멀티비타민이 모두 챙겨줍니다! 멀티비타민은 비타민과 미네랄의 조합으로 하루의 에너지를 보충하고, 영양소 공급을 도와줄 뿐만 아니라, 여러분의 체력과 면역을 강화시켜 활기찬 일상을 만들어줍니다. 지친 일상에서 멀티비타민이 함께하면, 피로와 스트레스에 대항하는 더 건강한 나를 발견할 수 있습니다.""",
        
        """

    상품:톤업 썬크림
    주요 키워드:촉촉
    톤앤매너:리뷰
    마케팅 메시지:톤업 썬크림을 사용하고서 피부 상태가 매일 좋아졌어요. 피부 톤이 밝아지면서 피부가 더욱 생기 있는 느낌이 들고, 촉촉함은 하루 종일 지속돼요. 뭔가 부드럽게 발리면서도 피부에 묻지 않고 자연스럽게 흡수되는 느낌이 좋아요. 햇빛을 가려주는 기능까지 갖춰져 있어서 외출 시에도 편하게 사용할 수 있어서 더 좋아요!""",

        """

    상품:현대자동차
    주요 키워드:안전, 가족
    톤앤매너:리뷰
    마케팅 메시지:현대자동차의 안전성은 진정한 보물입니다. 가족을 위해 운전하는데 있어서 어떤 것보다 중요한 것은 바로 안전입니다. 그래서 현대자동차를 선택한 것이었죠. 가장 최신 기술로 보호되는 이 자동차는 운전자와 승객의 안전을 위한 완벽한 선택이었습니다. 특히 길 위에서의 안정성과 신뢰성은 절대 어딘가에 뒤떨어지지 않는 것 같아요. 가족과 함께하는 모든 여정이 더욱 평안하고 안전한 이유는 바로 현대자동차 때문입니다.""",

        """

    상품:MZ청바지
    주요 키워드:트렌디함
    톤앤매너:리뷰
    마케팅 메시지:MZ청바지는 정말 트렌디함을 살린 최고의 선택이에요. 여기서 트렌디함은 단순한 스타일을 넘어서 독특한 매력을 지칭하는데요. 이 청바지는 유행을 주도하는 패션 트렌드를 완벽하게 반영하면서도 개성적인 느낌을 줘요. 고급스러운 디자인과 편안한 착용감이 조화를 이루어 여러분의 스타일에 환상적인 변화를 불러옵니다. MZ청바지로 당신만의 독특한 패션 센스를 표현하며, 어디서든 눈에 띄는 멋을 자랑해보세요.""",

        """

    상품:멀티비타민
    주요 키워드:에너지
    톤앤매너:리뷰
    마케팅 메시지:멀티비타민은 제가 찾던 답이었습니다. 에너지 부족과 피로로 고민하던 와중에 이 제품을 만났는데, 그 효과가 믿을 수 없을 만큼 크네요. 비타민과 미네랄의 조화가 몸에 깊숙히 스며들어서, 하루 중 힘들고 지친 순간을 훨씬 더 쉽게 이겨낼 수 있게 해줍니다. 멀티비타민 덕분에 내 면모를 더욱 빛나게 발견할 수 있었고, 일상 속에 새로운 활력을 불어넣을 수 있었습니다.""",
        
        """

    상품:톤업 썬크림
    주요 키워드:촉촉
    톤앤매너:행동촉구
    마케팅 메시지:촉촉한 피부로 더 자신감 있게 빛나보세요! 톤업 썬크림으로 피부에 활력을 불어넣어보세요. 매일 아침, 이 작은 썬크림 한 번 발라보는 건 어떨까요? 햇빛으로부터 피부를 지키고 동시에 촉촉한 상태를 유지하며, 자연스럽게 피부 톤을 높여보세요. 아무런 노력 없이도 더욱 환하고 건강한 피부를 만날 수 있을 거예요. 지금 바로 시작해보세요!""",

        """

    상품:현대자동차
    주요 키워드:안전, 가족
    톤앤매너:행동촉구
    마케팅 메시지:가족을 지키는 선택, 현대자동차와 함께하세요. 도로 위에서의 안전은 우리의 최우선 과제입니다. 현대의 최신 안전 기술과 품질로 가득한 차량들은 당신의 소중한 가족을 위한 완벽한 파트너가 될 것입니다. 가족과 함께하는 모든 순간을 더욱 안전하게 만들어보세요.""",

        """

    상품:MZ청바지
    주요 키워드:트렌디함
    톤앤매너:행동촉구
    마케팅 메시지:트렌디함을 입다, MZ청바지로 스타일을 새롭게 시작해보세요! 내게 딱 맞는 핏과 편안한 착용감으로, 자신감 넘치는 일상을 만들어보세요. MZ청바지와 함께라면 어디든 자유롭게 떠날 수 있는 기분이 들어, 새로운 경험을 위한 떠남을 도와줄 거예요. 지금 당장 MZ청바지로 트렌디한 모습을 완성하고, 세상에 자신만의 스타일을 펼쳐보세요!""",

        """

    상품:멀티비타민
    주요 키워드:에너지,40% 할인
    톤앤매너:행동촉구
    마케팅 메시지:바쁜 일상 속 건강 챙기기 힘드시죠? 건강을 위해 이것저것 챙겨먹자니 귀찮고...이것 하나면 충분해요! 필요한 8가지 비타민을 1알에 담았다! 현대사회 직장인들에게 딱 맞는 멀티비타민이 무려 40%나 할인한다고? 지금 구매하고 추가 증정품 받아가세요!
    
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
