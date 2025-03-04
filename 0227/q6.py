'''
하위 디렉토리 검색하기
특정 디렉터리부터 시작해서
그 하위(디렉터리 포함)의
모든 파일 중 파이썬 파일(*.py)만
출력해 주는 프로그램을 만들어보자.

필요한 기능은? 하위 디렉토리 검색하기(재귀), 파이썬 파일만 찾아서 출력하기
입력받는 값은? 검색을 시작할 디렉터리
출력하는 값은? 파이썬 파일명
'''
# 내답, 아예 틀림. 아래꺼 많이 쓴다. 아예 외우는 수준으로 하자
'''
import glob
a=input('검색 디렉터리를 입력하세요:')
num = glob.glob(f'{a}*.py')
print(len(num))
file_list=glob.glob(f'{a}*.py')
print(file_list)
print(len(file_list))
'''

'''
다시풀기
'''

# 답1
# 재귀함수, 빠르진 않다
# 피보나치, 하노이 탑, 경로탐색
# 스택이라는 개념이 선행되어야 이해가 쉽다
# 반드시 종료 조건이 있어야함
import os
def search(dirname):
    try:
        filenames=os.listdir(dirname)
        print(filenames)
        for filename in filenames:
            full_filename=os.path.join(dirname, filename) # 디렉터리와 파일 이름 이어줌줌
            if os.path.isdir(full_filename): # 디렉터리인지 파일인지 구별, 디렉터리면
                search(full_filename) # 디렉터리일때, 재귀함수 호출
            else:
                ext=os.path.splitext(full_filename)[-1] # 확장자만 추출
                if ext =='.py':
                    print(full_filename)
    except PermissionError: # 수행권한없는 디렉터리에 접근할때
        print('접근권한없음')
search("c:/LJH/")

# 답2
import os # 이게 재귀보다 빠르다, 내장 라이브러리?
for (path, dir, files) in os.walk("C:\lsc"):
    for filename in files:
        ext=os.path.splitext(filename)[-1]
        if ext=='.py':
            print("%s%s"%(path,filename))