from openai import OpenAI
from dotenv import load_dotenv
import os
import pymupdf

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


def pdf_to_text(pdf_file_path:str):
    # pdf_file_path = "chap4/data/정보처리기사실기 요약.pdf"

    doc = pymupdf.open(pdf_file_path)

    footer_height = 60 # 책은 80으로 나왔지만, 해당 PDF의 경우 60으로 해야 내용 손실이 없다.

    full_text = ''

    for page in doc:
        rect = page.rect

        footer = page.get_text(clip=(0, rect.height - footer_height, rect.width, rect.height)) # 왜 한거지?
        text = page.get_text(clip=(0, 0, rect.width, rect.height - footer_height))
        full_text += text + '\n-------------------------------------------\n'

    pdf_file_name = os.path.basename(pdf_file_path)
    pdf_file_name = os.path.splitext(pdf_file_name)[0] 

    txt_file_path = f"chap4/output/{pdf_file_name}_with_preprocessing.txt" 

    with open(txt_file_path, 'w', encoding='utf-8') as f:
        f.write(full_text)
    return txt_file_path


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

def summarize_pdf(pdf_file_path:str, output_file_path:str):
    txt_file_path = pdf_to_text(pdf_file_path)
    summary = summarize_txt(txt_file_path)

    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(summary)

if __name__ == '__main__':
    pdf_file_path = 'chap4/data/정보처리기사실기 요약.pdf'
    summarize_pdf(pdf_file_path, './chap4/output/crop_model_summary2.txt')