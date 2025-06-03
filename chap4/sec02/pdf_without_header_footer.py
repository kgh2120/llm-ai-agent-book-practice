import pymupdf
import os

pdf_file_path = "chap4/data/정보처리기사실기 요약.pdf"

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