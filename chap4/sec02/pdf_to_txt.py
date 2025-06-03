import pymupdf
import os

pdf_file_path = "chap4/data/정보처리기사실기 요약.pdf"

doc = pymupdf.open(pdf_file_path)

full_text = ''

for page in doc:
    text = page.get_text()
    full_text += text

pdf_file_name = os.path.basename(pdf_file_path)
pdf_file_name = os.path.splitext(pdf_file_name)[0] # 확장자 제거 코드 `os.path.splitext`는 파일 이름 + 확장자로 분리시켜줘서 [0]은 파일 이름, [1]은 확장자가 된다.

txt_file_path = f"chap4/output/{pdf_file_name}.txt" # f"" 는 f-string(formatted string literal)이라고 불리는 문법이다. 중괄호를 통해 외부 변수를 주입해 문자열을 구성한다. JS의 ``나 코틀린에도 있는 문법과 유사한 것 같다. 또 자바만 없다.

with open(txt_file_path, 'w', encoding='utf-8') as f:
    f.write(full_text)
# 이 결과에서는 중간중간 페이지 번호나 출처 등이 반복적으로 등장하고 있음.
