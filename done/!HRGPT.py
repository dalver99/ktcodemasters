import openai
from openai import OpenAI
import os
import sys

openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

#append if I say YES!
messages = [
    {"role": "system", "content": "Act as a HR manager who was reviewed over 100,000 application letters."},
    {"role":"user","content": """
I am applying for KT's IT컨설팅분야, B2B제안/수행 position.
    
Q1: 지원한 분야와 관련된 본인의 역량(지식/Skill/경험 등)과 열정, 노력(프로젝트, 공모전, 대외활동, 논문 등)에 대해 기술해 주십시오. (최대 800자 입력가능)
     
A1: KT의 B2B제안/수행 직무는 고객사에게 제안하기 위해 다양한 기술에 대한 이해와, 이를 도입해야할 근거를 제시하며 설득하는 전략적 커뮤니케이션 능력이 필요합니다. 제가 가진 강점 중 이 두가지에 관해 기술하겠습니다.

[고객 중심의 기술적 의사소통]

  스타트업에서 근무 당시 태양광 발전 업체의 DX 프로젝트를 전담한 경험이 있습니다. 빠른 수평적 확장으로 IT 도입이 늦어져 많은 업무가 종이로, 수동적으로 진행된다는 점을 파악했습니다. 인터뷰와 미팅을 거쳐 보고서 자동화 설루션, 데이터베이스 클라우드화, mini-ERP 제작을 제안하였고, 이를 모두 수주하였습니다.

  금액에 대한 부담을 완화하기 위해, 자동화를 통해 절약할 수 있는 업무 시간, 의사소통 비용의 감소를 수치화하였습니다. 또한, ERP의 경우 추가 수주를 위해 효용을 느낄 수 있는 부분의 개발부터 소규모로 수주하여, 전략적이고 창의적인 의사소통 능력을 길렀습니다.

[끊임없는 역량 향상을 위한 노력]

  내가 기존에 하던 방식은 틀렸다는 말은 누구도 수용하기 쉽지 않습니다. 하지만 기술적 전문성을 보여 존중을 받는다면 제안과 설득이 쉬워지고, 이는 기술을 연구하게 하는 큰 동기부여가 되었습니다. 

  저는 기술적 역량을 기르기 위해 스타트업을 다니면서 AWS 클라우드 자격증을 취득하였으며, NextJS를 공부하여 업무에 사용할 내부용 툴을 개발하고, 웹앱을 서비스한 경험이 있습니다. 또한, 실무 AI 역량이 부족하다고 느껴 현재는 KT AIVLE School 과정에 참여하고 있습니다.
     
Q2: KT의 핵심가치 중 자신에게 가장 부합하는 것을 선택하고 그 이유를 구체적인 사례와 함께 기술해 주십시오. (핵심가치는 KT그룹 채용 홈페이지를 참고 바랍니다.) (최대 800자 입력가능)
     
A2: 생성형 AI를 활용한 서비스를 출시하고 실패한 경험으로, 저는 실질적인 효용이 없는 기술은 지속될 수 없다는 것을 뼈저리게 경험하였습니다. 

[다양한 서비스 실패 경험]

  창업 초기에 저는 팀과 함께 5개의 서비스를 출시하였습니다. 이 중 개발자의 수요로부터 기획하여 출시한 서비스는 그 효용을 빠르게 입증하며 현재도 유지되고 있습니다. 하지만, 어설프게 재미만 있는 서비스, 새로운 기술을 그저 활용하기에 바빠 만든 서비스들은 모두 빠르게 종료하였습니다. 초기의 반응은 모두 좋았으나 유저들은 빠르게 이탈했고, 지불 용의가 있는 고객은 없었습니다. 실패 사례를 분석해보니 지속적으로 사용하고, 돈을 지불하기 위해서는 실질적인 효용이 필요하다는 결론에 도달했습니다.

  이후 더 실질적인 가치를 더 빠르게 검증할 수 있는 고객인 비즈니스를 대상으로 전환하였습니다. 금융사가 금감원에게 보고할 문서를 자동화하는 설루션, 펀드의 유지 보수 비용을 자동으로 계산해주는 웹앱등을 제작하였습니다. 구독 서비스를 수주하고 해지하는 경험과 VoC 수집을 통해 실질적인 가치를 냉정하게 따지고 활용하는 것의 중요성을 체감하였습니다. 근본적인 가치에 집중하니 더 열정적으로 업무를 진행할 수 있었으며, 고객 경험의 개선을 보면서 보람 또한 얻을 수 있었습니다.

KT는 이미 클라우드와 통신에 기반하여 많은 기업과 단체에 DX/AIX를 통해 실질적인 가치를 제공하고 있으며, 저의 역량과 경험을 통해 이 가치에 기여하고 참여하고 싶습니다.
     

"""}
,
]

while True:
    # Get user input
    user_message = input("You: ")

    # Generate response
    messages_with_user_input = messages + [{"role": "user", "content": user_message}]
    completion_response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Make sure to use a currently available model
        messages=messages_with_user_input,
        max_tokens=2500
    )
    response_message = completion_response.choices[0].message.content
    print("#"*50)
    print("Bot: ", response_message)

    # Ask if you want to add the response to the conversation history
    confirm_input = input("Add to history? (yes/no): ")

    if confirm_input.lower() == "yes":
        # Add both user's input and bot's response to the conversation history if confirmed
        messages = messages_with_user_input + [{"role": "assistant", "content": response_message}]