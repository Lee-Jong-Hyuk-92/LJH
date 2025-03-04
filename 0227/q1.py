# 구구단 x단 프로그램 만들기
# gugu 함수를 구현해보세요.
def gugu(a):
    a=int(a)
    for i in range(1,10):
        ai=a*i
        print(f'{a}*{i}={ai}')

print('구구단입니다.')
b = input('숫자를 입력하세요')
gugu(b)

'''
def gugu(n):
    for i in range(1,10):
        print(n*i)
gugu(3)
'''