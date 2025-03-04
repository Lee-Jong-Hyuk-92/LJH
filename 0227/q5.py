# 탭 문자를 공백 문자 4개로 바꾸기
# 다음과 같은 형식으로 프로그램이
# 수행되도록 만들 것이다.

# python tabto4.py src dst

# tabto4.py는 우리가 작성해야 할
# 파이썬 프로그램 이름,
# src는 탭을 포함하고 있는 원본 파일 이름,
# dst는 파일 안의 탭을
# 공백 4개로 변환한 결과를 저장할 파일 이름이다.

# 예를 들어 a.txt에 있는 탭을
# 4개의 공백으로 바꾸어 b.txt에
# 저장하고 싶다면 다음과 같이 수행해야 한다.

# python tabto4.py a.txt b.txt

'''
text = "Hello\tWorld"
print(text)
new_text = text.replace("\t", "    ")#문자 바꿀때
print(new_text)\
'''
#다시풀기
'''
import sys # 파일 어쩌구 할거니까

def tab_to_spaces(src, dst): # 탭을 4개 공백4개로, src source, dst destination
    with open(src, 'r') as infile: # 불러들일 파일을 r 모드 열기
        content = infile.read() # 파일 내용 읽기
    with open(dst, 'w') as outfile: # 저장할 파일을 w 모드로 열기
        outfile.write(content)

if __name__ == "__main__": # 현재 실행되는 파일에서 직접 터미널 실행중인게 맞냐?
    if len(sys.argv) !=3:
        print("다음과 같이 입력하세요: python tabto4.py <원본파일이름> <변경파일이름>")
    else:
        src = sys.argv[1] # 원본 파일 이름
        dst = sys.argv[2] # 결과 파일 이름
        tab_to_spaces(src,dst) # 변환 함수 실행
'''

import sys
src=sys.argv[1]
dst=sys.argv[2]

f=open(src)
tab_content=f.read()
f.close()

space_content=tab_content.replace("\t"," "*4)

fw=open(dst,'w')
fw.write(space_content)
fw.close()
