#점프투 파이썬 5장
#Q1. 다음은 Calculator 클래스이다.
'''
class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val
#위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해보자.
#즉 다음과 같이 동작하는 클래스를 만들어야 한다.
'''
#1 풀이
'''
class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value) #10에서 7을 뺀  3을 출력
'''



#@Q2. 객체변수 value가 100이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어보자
#단, 반드시 다음과 같은 Calculator클래스를 상속해서 만들어야한다.
'''
class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val
class MaxLimitCalculator(Calculator):
    def add(self, val):
        if self.value+val>100:
            print('100 over')
        else:
            self.value+=val

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)
'''



#Q3. 다음 결과를 예측해보자
'''
print(all([1,2,abs(-3)-3])) #False 예상
print(chr(ord('a'))=='a') #ㅁ=ㅁ? True 예상
'''


#Q4. filter와 lambda를 사용해서 리스트 [1,-2,3,-5,8,-3]에서 음수를 제거해보자.
# 람다, lambda 함수 사용법 다시 공부부
#print(list(filter(lambda x: x>=0, [1,-2,3,-5,8,-3]))) #lambda 조건, 원본
#x를쓴다: x>=인것만, 여기서



#Q5. 234라는 10진수의 16진수는 다음과 같이 구할 수 있다. 이번에는 반대로 16진수의 문자열 0xea를 10진수로 변경해보자.
#hex(234) ‘0xea’
#print(int('0xea', 16))



#Q6. map과 lambda를 사용해서 [1,2,3,4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3,6,9,12]를 만들어보자.
#print(list(map(lambda x: x*3, [1,2,3,4])))



#Q7. 다음 리스트의 최댓값가 최솟값의 합을 구해보자.
#[-8, 2, 7, 5, -3, 5, 0, 1]
#a=[-8, 2, 7, 5, -3, 5, 0, 1]
#print(f'최댓값은 {max(a)}, 최솟값은 {min(a)}')



#Q8. 17/3의 결과는 다음과 같다. 소숫점 4자리까지만 반올림해서 표시해보자.
#print(round(17/3, 4))



#Q9. 다음과 같이 실행할 때
# 입력값을 모두 더해서 출력하는
# 스크립트(C:\doit\myargv.py)를 작성해보자.
#모름, 다시풀기
#C:\cd doit
#C:\doit> python myargv.py 1 2 3 4 5 6 7 8 9 10
#55
'''
import sys
num=sys.argv[1:]

result=0
for i in num:
    result +=int(i)
print(result)
'''



#Q10. os모듈을 사용해서 다음과 같이 동작하도록 코드를 작성해라.
#모름, 다시풀기
#C:\doit 디렉터리로 이동한다.
#dir 명령을 실행하고 그 결과를 변수에 담는다.
#dir 명령의 결과를 출력한다
'''
import os
os.chdir('c:/LJH/')
f=os.popen('dir')
print(f.read())
f.close()
'''



#Q11. glob모듈을 사용해서
# C:\doit 디렉터리의 파일 중
# 확장자가 .py인 파일만 출력하는 프로그램을 만들어보자.
#모름, 다시풀기
'''
import glob
num = glob.glob(r'c:\LJH\0226\q_0226.py')
print(len(num))

file_list=glob.glob(r'c:\LJH\0226*.py')
print(file_list)
print(len(file_list))
'''



#Q12. time모듈을 사용해서 현재 날짜와 시간을 다음과 같은 형식으로 출력해보자.
#2018/04/03 17:20:32
#import time
#print(time.strftime('%Y/%m/%d %X', time.localtime(time.time())))



#Q13. random 모듈을 이용해서 로또번호(1~45사이의 숫자 6개)를 생성해보자. (중복 숫자 안 됨) 중복 제거 못함, 왜?
# 정확히 모름, 다시 풀기
'''
import random

def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

a = list()
for i in range (0,45):
    a.append(i+1) #a=1~45
print(a)

b=list()
for i in range(6):
    pop=random_pop(a)
    if pop in b:
        break
    b.append(pop)
    print(list(b))
'''
#선생님 답
'''
import random
result =[]
while len(result) < 6: #result라는 리스트 길이가 6이 될때까지
    num = random.randint(1,45)
    if num not in result:
        result.append(num)
print(result)
'''
'''
#GPT 답
import random
a = list(range(1, 46))  # a = 1~45
print("Original list:", a)

# 중복 없이 6개의 값을 랜덤으로 뽑기
b = random.sample(a, 6)

print("Randomly selected 6 values:", b)
'''

#GPT 1
#아래와 같은 클래스 Person을 생성하세요:

# 클래스 속성: name, age
# 생성자: __init__(self, name, age): name과 age를 인자로 받아 객체를 초기화합니다.
# 메소드: greet(self): "{name}님이 {age}살입니다" 형식의 문자열을 반환합니다.
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f'{self.name}님이 {self.age}살입니다')
p1 = Person('OPQWE', 15)
p1.greet()
'''



#GPT 2
#아래와 같은 클래스 BankAccount을 생성하세요:
#클래스 속성: account_number, balance
# 생성자: __init__(self, account_number, balance=0): account_number와 초기 잔액 balance(기본값 0)을 인자로 받아 객체를 초기화합니다.
# 메소드: deposit(self, amount): 계좌에 amount만큼 입금합니다.
# 메소드: withdraw(self, amount): 계좌에서 amount만큼 출금합니다. 잔액이 출금액보다 작을 경우 “잔액이 부족합니다”라고 출력합니다.
# 예시 코드를 작성하고 테스트해보세요.

#2풀이
'''
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number=account_number
        self.balance=balance
        print(f'계좌 초기잔액은 {self.balance}원 입니다.')
    def deposit(self, amount):
        self.balance += amount
        print(f'입금후 계좌잔액은 {self.balance}원 입니다.')
    def withdraw(self, amount):
        if self.balance-amount < 0:
            print(f'잔액이 부족합니다. 현재 계좌잔액은 {self.balance}원 입니다.')
        else:
            self.balance-=amount
            print(f'출금후 계좌잔액은 {self.balance}원 입니다.')
    def transfer(self, amount, target_account):
        if self.balance < amount:
            print('잔액이 부족합니다.')
        else:
            self.withdraw(amount)
            target_account.deposit(amount)

account1 = BankAccount(12345, 1000)
account2 = BankAccount(56795, 600000)
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000)  # 출력: 잔액이 부족합니다

account1.transfer(500,account2)#account2의 계좌번호 56795를 적는게 아니라 account2를 전달값으로 적기만 하면됨
'''



#GPT Q3 했음, 다시 하기
'''
아래와 같은 간단한 모듈 calculator.py를 작성하고, 다른 파이썬 스크립트에서 이 모듈을 사용해보세요.
함수: add(a, b): 두 숫자의 합을 반환합니다.
함수: subtract(a, b): 두 숫자의 차를 반환합니다.
함수: multiply(a, b): 두 숫자의 곱을 반환합니다.
함수: divide(a, b): 두 숫자의 나눗셈 결과를 반환합니다. 0으로 나누는 경우, “0으로 나눌 수 없습니다”라고 출력합니다.
예시 코드를 작성하고 테스트해보세요.

# calculator.py 파일
# 여기에 코드를 작성하세요
'''
#파일명 calculator.py
#3풀이
'''
def add(a,b):
        sum(a,b)
def subtract(a,b):
        a-b
def multiply(a,b):
        a*b
def divide(a,b):
    if b==0:
        print('0으로 나눌수 없습니다.')
    else:
        a/b
'''
'''
# main.py 파일
import calculator

print(calculator.add(3, 4))      # 출력: 7
print(calculator.subtract(3, 4)) # 출력: -1
'''
'''
def add(a,b):
        return sum(a,b)
def subtract(a,b):
        return a-b
def multiply(a,b):
        return a*b
def divide(a,b):
    if b==0:
        return print('0으로 나눌수 없습니다.')
    else:
        return a/b
'''



#GPT Q4 오름차순 정렬을 어떻게? 다시풀기
'''
파이썬 표준 라이브러리 random 모듈을 사용하여 1부터 100 사이의 무작위 정수를 10개 생성하고, 이를 오름차순으로 정렬하는 코드를 작성하세요.
예시 코드를 작성하고 테스트해보세요.

# 여기에 코드를 작성하세요
'''
#4풀이
'''
import random
a=[]
for i in range(10):
    b=random.randint(1,100)
    a.append(b)
print(a)
sorted(a) #오름차순 정렬???
print(a)
'''
'''
import random
random_number = [random.randint(1,100) for _ in range(10)]
# 중복예외처리 안되어있어서 중복 될수 있다
# 1에서 100사이의 정수생성, 10번
sorted_number = sorted(random_number)
'''



#GPT Q5 패키지가 뭐지? 다시 하기
'''
아래와 같은 간단한 패키지 my_math를 생성하세요.

패키지: my_math
모듈: operations.py
함수: add(a, b): 두 숫자의 합을 반환합니다.
함수: subtract(a, b): 두 숫자의 차를 반환합니다.
패키지를 생성한 후, 다른 파이썬 스크립트에서 이 패키지를 사용해보세요.

예시 코드를 작성하고 테스트해보세요.

# my_math/operations.py 파일
# 여기에 코드를 작성하세요

# main.py 파일
from my_math.operations import add, subtract
print(add(3, 4))      # 출력: 7
print(subtract(3, 4)) # 출력: -1
'''



#GPT Q6 했음
'''
위의 my_math 패키지에 다음과 같이 새로운 모듈 geometry.py를 추가하세요.

모듈: geometry.py
함수: circle_area(radius): 원의 반지름을 입력받아 넓이를 반환합니다. (넓이 = 반지름 x 반지름 x π)
함수: rectangle_area(width, height): 사각형의 가로와 세로를 입력받아 넓이를 반환합니다. (넓이 = 가로 x 세로)
패키지를 수정한 후, 다른 파이썬 스크립트에서 이 패키지를 사용해보세요.

예시 코드를 작성하고 테스트해보세요.

# my_math/geometry.py 파일
# 여기에 코드를 작성하세요

# main.py 파일
from my_math.geometry import circle_area, rectangle_area

print(circle_area(5))       # 출력: 78.53981633974483 (값은 π에 따라 약간 다를 수 있음)
print(rectangle_area(4, 5)) # 출력: 20
'''
#6 문제 풀이
'''
#파일명 geometry.py
import math
def circle_area(radius):
    area = radius**2*math.pi
    return area
def rectangle_area(width, height):
    area = width * height
    return area
'''
'''
import math
def circle_area(radius):
    return radius**2*math.pi
def rectangle_area(width, height):
    return width * height
'''



#GPT Q7 했음, 다시풀기
'''
아래 코드는 사용자로부터 숫자를 입력받아 제곱을 출력하는 코드입니다.
사용자가 숫자가 아닌 문자를 입력할 경우,
ValueError 예외가 발생할 수 있습니다.
이 예외를 처리하고, 사용자에게 숫자를 입력하도록 안내하는 코드를 작성하세요.

number = input("숫자를 입력하세요: ")
squared_number = int(number) ** 2
print("입력한 숫자의 제곱:", squared_number)
'''
#7 풀이
'''
number = input("숫자를 입력하세요: ")
try:
    squared_number = int(number) ** 2
except:
    print('숫자를 입력하세요')
else:
    print("입력한 숫자의 제곱:", squared_number)
finally:
    print('수행종료')
'''
'''
try:
    number = input('숫자를 입력하세요')
    squared_number = int(number)**2
    print('입력의 제곱은', squared_number)
except ValueError:
    print('숫자를 입력해야 합니다')
'''



#GPT Q8 했음, 다시 하기
'''
아래 코드는 두 숫자를 나누는 코드입니다. 분모가 0인 경우, ZeroDivisionError 예외가 발생할 수 있습니다. 이 예외를 처리하고, 사용자에게 0으로 나눌 수 없다는 메시지를 출력하는 코드를 작성하세요.

numerator = 10
denominator = 0
result = numerator / denominator
print("결과:", result)
'''
#8풀이
'''
numerator = 10
denominator = 0
try:
    result = numerator / denominator
except:
    print('0으로 나눌수 없습니다.')
else:
    print("결과:", result)
finally:
    print('수행종료')
'''
'''
numerator = 10
denominator = 0
try:
    result = numerator / denominator
    print('결과', result)
except ZeroDivisionError:
    print('0으로 나눌수 없습니다.')
'''



#GPT Q9
'''
다음과 같은 리스트가 주어졌을 때, max()와 min() 내장 함수를 사용하여 최댓값과 최솟값을 찾고 출력하는 코드를 작성하세요.

numbers = [3, 7, 2, 1, 6, 4, 9, 8]
# 여기에 코드를 작성하세요
'''
#9풀이
'''
numbers = [3, 7, 2, 1, 6, 4, 9, 8]
print(max(numbers))
print(min(numbers))
'''



#GPT Q10 함수 사용법을 정확히 모름, 많이 쓰임
#다시풀기
'''
주어진 문자열에서 공백을 기준으로 단어를 분리하고,
각 단어의 첫 글자를 대문자로 변경한 후,
다시 공백을 기준으로 합쳐서 출력하는 코드를 작성하세요.
이 문제를 해결하기 위해 str.split(), str.capitalize(), str.join() 내장 함수를 사용하세요.

text = "hello world, this is a python example."
# 여기에 코드를 작성하세요
'''
#10 풀이
'''
text = "hello world, this is a python example." #text 는 str
text=text.split() #text는 list로 바뀜
capitalized_text = [item.capitalize() for item in text]  # 리스트에서 각 요소에 대해 capitalize() 적용
result = " ".join(capitalized_text)  # 리스트의 요소들을 한칸씩 띄어서 문자열로 연결
print(result)
'''
'''
text = "hello world, this is a python example." #text 는 str
text=text.split() #text는 list로 바뀜
capitalized_text = [i.capitalize() for i in text]  # 리스트에서 각 요소에 대해 capitalize() 적용
result = " ".join(capitalized_text)  # 리스트의 요소들을 한칸씩 띄어서 문자열로 연결
print(result)
'''



#GPT Q11 했음
'''
파이썬 datetime 모듈을 사용하여 현재 시간을 출력하는 코드를 작성하세요.
# 여기에 코드를 작성하세요
'''
#11풀이
'''
import time
print(time.strftime('%X', time.localtime(time.time())))
'''
#샘 답
'''
from datetime import datetime
current_time = datetime.now()
print('현재시간:', current_time)
print(current_time.strftime(%Yblahblah...))
'''



#GPT Q12 했음
'''
파이썬 random 모듈을 사용하여 1에서 100 사이의 무작위 정수 10개를 생성하고 출력하는 코드를 작성하세요.
# 여기에 코드를 작성하세요
'''
#12풀이
'''
import random
for i in range(10):
    print(random.randint(1,100))
'''
'''
import random
r_n=[random.randint(1,100) for _ in range(10)]
print('무작위 정수 10개:', r_n)
'''