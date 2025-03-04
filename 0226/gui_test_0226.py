import turtle #라이브러리 import
import time

scr = turtle.Screen() #화면객체 생성
scr.title("터틀 테스트")

tur =turtle.Turtle()
'''
# 사각형 그리기
for _ in range(12): # _ 써도 의미가 없어서 안쓴다, 12번 반복, 사각형 3번 그리고 종료
    tur.forward(100) #100만큼 가라
    time.sleep(0.5) #가고나서 0.5초 멈춰라
    tur.left(90) #90도 왼쪽으로 꺾어라
'''
# 삼각형 그리기
for _ in range(3):
    tur.forward(100)
    time.sleep(0.5)
    tur.left(120)

scr.mainloop()