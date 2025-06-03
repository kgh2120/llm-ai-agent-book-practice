from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def summarize_txt(file_path: str):
    client = OpenAI(api_key=api_key)

    with open(file_path, 'r', encoding='utf-8') as f:
        txt = f.read()
    
    system_prompt = f'''
    너는 다음 글을 요약하는 봇이다. 아래 글을 읽고, 각 내용을 요약해라.

    작성해야 하는 포맷은 다음과 같아.

    # 현재 파트의 제목

    ## 해당 파트에서 주요한 키워드 요약

    {txt}

    ===========================================

    '''

    print(system_prompt)
    print('=====================================')

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        temperature=0.1,
        messages=[
            {"role" : "system", "content" : system_prompt}
        ]
    )

    return response.choices[0].message.content

if __name__ == '__main__':
    file_path = './chap4/output/정보처리기사실기 요약_with_preprocessing.txt'

    summary = summarize_txt(file_path)
    print(summary)

    with open('./chap4/output/crop_model_summary.txt', 'w', encoding='utf-8') as f:
        f.write(summary)
