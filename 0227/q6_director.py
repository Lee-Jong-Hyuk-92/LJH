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
import os
def search(dirname):
    try:
        filenames=os.listdir(dirname)
        #지정된 경로 x에 있는 파일과 디렉터리의 목록을 반환하는 함수, 파일과 디렉터리(경로) 구분X
        # filenames에는 경로들이 리스트 형식으로 저장
        
        print(f'지금 전달받은 경로 안에 있는 디렉터리들은 다음과 같다',filenames)
        #['0224', '0225', '0226', '0227', 'simple_memo.txt']
        
        for filename in filenames:
            # filename은 변수, filenames안에있는 디렉터리 경로들을 시행
            
            full_filename=os.path.join(dirname, filename)
            # full_filename에다가 경로를 저장해라
            
            # print(f'for문 돌리는중, 이제부터', full_filename, '여기를 검색할거다')
            # 원래 답
            print(f'for문 돌리는중, 이제부터', filename, '여기를 검색할거다')
            # 지금 보려는거거
            
            if os.path.isdir(full_filename):
                # 주어진 경로가 디렉터리인지 확인하는 함수, 디렉터리라면 참, 디렉터리랑 파일은 다르다
                search(full_filename)
                print(f'지금 타고 들어온 경로 안에 또 경로가 있으면 경로 이름 출력',full_filename)

            else:
                # 해당경로 검색이 끝났으니 한번 위로 나와라
                ext=os.path.splitext(full_filename)[-1]
                if ext=='.py':
                    # print(f'해당경로에서 더이상 경로는 없음, .py로 끝나는 파일을 출력',full_filename)
                    # 원래 코드

                    print(f'해당경로에서 더이상 경로는 없음, .py로 끝나는 파일을 출력',full_filename)
                    # 지금 보려는거

    except PermissionError: #접근권한없으면 아래를 출력해라
        print('접근권한없음')
search("C:\LJH") # 경로 하위의 경로 검색, 재귀함수 호출


import os
def search(dirname):
    try:
        filenames=os.listdir(dirname)
        print(filenames)
        for filename in filenames:
            full_filename=os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext=os.path.splitext(full_filename)[-1]
                if ext =='.py':
                    print(full_filename)
    except PermissionError:
        print('접근권한없음')
search("c:/LJH/")