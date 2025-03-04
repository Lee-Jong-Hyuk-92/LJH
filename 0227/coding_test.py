# q1
# a:b:c:d 라는 문자열이 있을때
# split과 join 을 이용하여 다음과 같이 고쳐라
# a#b#c#d
'''
a='a:b:c:d'
split_a=a.split(':')
print(split_a)

join_a='#'.join(split_a)
print(join_a)
'''



#q2
# 딕셔너리 값 추출하기
# 다음은 딕셔너리의 a에서
# 'C'라는 key에 해당하는 value를 출력하는 프로그램이다.
# a = {'A':90, 'B':80} a['C']
# a딕셔너리에는 'C'라는 key가 없으므로
# 오류가 발생한다.
# 'C'에 해당하는 key값이 없을 경우
# 오류대신 70을 얻을 수 있도록 수정하시오.
'''
def innotin(x):
    a = {'A':90, 'B':80}
    if a.get(x) == True:
        print(a[x])
    else:
        return 70

print(innotin('C'))
'''
'''
a = {'A':90, 'B':80}

if a.get('C') == None:
    a['C']=70

print(a['C'])
'''



# q3
# 리스트 a에 [4, 5]를 + 기호를 사용하여 더한 결과는 다음과 같다.
# 리스트 a에 [4, 5]를 extend를 사용하여 더한 결과는 다음과 같다.
# + 기호를 사용하여 더한 것과
# extend한 것의 차이점이 있을까? 없다
# 있다면 그 차이점을 설명하시오. 둘다 리스트
'''
a = [1, 2, 3]
a = [1, 2, 3]
a = a + [4, 5]
print(a) 
print(type(a))
a = [1, 2, 3]
a.extend([4, 5])
print(a) 
print(type(a))
'''
'''
a = [1, 2, 3]
print(id(a))
a = a + [4, 5]
print(a)
print(id(a))

new_a = [1, 2, 3]
print(id(a))
new_a = new_a.extend([4,5])
print(a)
print(id(a))
'''



# q4
# 다음은 A학급 학생의 점수를 나타내는 리스트이다.
# 다음 리스트에서 50점 이상 점수의 총합을 구하시오.
'''
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
print(sum(filter(lambda x: x>50, A)))
'''
'''
sum=0
for a in A:
    if a>=50:
        sum+=a
print(sum)
'''



# q5, 대표적인 알고리즘 문제, 재귀를 쓰라는 얘기가 없다
# 첫 번째 항의 값이 0이고
# 두 번째 항의 값이 1일 때,
# 이후에 이어지는 항은
# 이전의 두항을 더한 값으로 이루어지는 수열을
# 피보나치 수열이라고 한다.
# 0, 1, 1, 2, 3, 5, 8, 13 ...
# 입력을 정수 n으로 받았을 때,
# n이하까지의 피보나치 수열을
# 출력하는 함수를 작성해 보자.
'''
def fibo(n):
    a = [0,1]
    if n < 2:
        print('더 큰 숫자를 입력해라')
    else:
        for i in range(2,n):
            a.append(a[i-2]+a[i-1])
    return a
print(fibo(15))
'''
'''
def fib(n): # 쉬운 버전, 재귀함수 없이
    result=[]
    a,b=0,1
    while a<=n:
        result.append(a)
        a,b=b,a+b
        return result
n = int(input('입력'))
print(fib(n))
'''
'''
input=int(input('입력')) # 재귀 버전으로 설명, 스택, 호출 횟수가 많다

def fib(n):
    if n== 0:
        return 0
    if n==1:
        return 1
    return fib(n-2) + fib(n-1)

for i in range(input):
    print(fib(i))
'''


# q6 , 다시 해보기, 다시 풀기
# 사용자로부터 다음과 같은 숫자를 입력받아
# 입력받은 숫자의 총합을 구하는 프로그램을
# 작성하시오. (단 숫자는 콤마로 구분하여 입력한다.)
# 65, 45, 2, 3, 45, 8
'''
a=input('숫자 6개 입력해라 숫자와 숫자 사이는 ,를 눌러라')
print(a, type(a)) # a 타입은 스트링
split_a=a.split(',') # ,로 끊었음
print(split_a, type(split_a)) # split_a는 문자열 리스트
split_a = [int(x) for x in split_a] # int로 형변환
print(sum(split_a))
'''
'''
val=input("입력해라")
a=map(int, val.split(',')) # 이부분 뭔지 공부 필요, 리스트 컴프리헨션?
print(a, type(a))

result=0
for i in a:
    result += i
print(result)
'''



# q7
# 사용자로부터 2~9까지의 숫자 중 하나를 입력받아
# 해당 숫자의 구구단을 한 줄로 출력하는
# 프로그램을 작성하시오.
# 실행 예)
# 구구단을 출력할 숫자를
# 입력하세요(2~9): 2 2 4 6 8 10 12 14 16 18
'''
gugu=int(input("구구단을 출력할 숫자를 입력해라(2~9): "))
for i in range(1,10):
    print(gugu*i, end=' ')
'''



# q8
'''
역순 저장

다음과 같은 내용의 파일 abc.txt가 있다.

AAA

BBB

CCC

DDD

EEE

이 파일의 내용을 다음과 같이 역순으로 바꾸어 저장하시오.

EEE

DDD

CCC

BBB

AAA
'''
'''
import os
with open('abc.txt', 'r') as f:
    a=[]
    for line in f:
        a.append(line.strip())
with open('cba.txt','w') as f:
    for line in a[::-1]:
        f.write(line + '\n')
'''
'''
f=open('abc.txt','r')
lines=f.readlines()
print(lines, type(lines)) # 디버그 찍어보면 좋다
f.close()

lines.reverse()

f=open('result_abc.txt','w')
for line in lines:
    line =line.strip() # 문자 앞뒤에 지저분한 것들 잘라주는것
    f.write(line)
    f.write('\n')
f.close()
'''

# q9
# 평균값 구하기
# 총 10줄로 이루어진 q9_sample.txt 파일이 있다.
# q9_sample.txt 파일의 숫자 값을 모두 읽어
# 총합과 평균 값을 구한 후 평균 값을
# q9_result.txt 파일에 쓰는 프로그램을 작성하시오.
'''
70

60

55

75

95

90

80

80

85

100
'''
'''
import os
with open('q9_sample.txt', 'r') as f:
    a=[]
    for line in f:
        try:
            a.append(int(line.strip()))
        except ValueError:
            pass
with open('q9_result.txt','w') as f:
    total_sum=sum(a)
    avg=total_sum/len(a)
    f.write(f'{avg}')
'''
'''
f=open('q9_sample.txt','r')
lines =f.readlines()
f.close()

total=0
for line in lines:
    score=int(line)
    total+=score
    avg=total/len(lines)

f=open('q9_result.txt','w')
f.write(str(avg))
f.close()
'''



# q10
'''
다음과 같이 동작하는 클래스 Calculator를 작성하시오.

>>> cal1 = Calculator([1,2,3,4,5])
>>> cal1.sum() # 합계
15
>>> cal1.avg() # 평균
3.0
>>> cal2 = Calculator([6,7,8,9,10])
>>> cal2.sum() # 합계
40
>>> cal2.avg() # 평균
8.0
'''
'''
class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum(self):
        return sum(self.numbers)

    def avg(self):
        return self.sum() / len(self.numbers)

cal1 = Calculator([1,2,3,4,5])
cal2 = Calculator([6,7,8,9,10])
print("cal1 total sum:", cal1.sum())
print("cal1 average:", cal1.avg())
print("cal2 total sum:", cal2.sum())
print("cal2 average:", cal2.avg())
'''
'''
class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum(self):
        result=0
        for num in self.numbers:
            result +=num
        return sum(self.numbers)

    def avg(self):
        return self.sum() / len(self.numbers)

cal1 = Calculator([1,2,3,4,5])
cal2 = Calculator([6,7,8,9,10])
print("cal1 total sum:", cal1.sum())
print("cal1 average:", cal1.avg())
print("cal2 total sum:", cal2.sum())
print("cal2 average:", cal2.avg())
'''
# q11
# C:\doit 디렉터리에 mymod.py 파이썬 모듈이 있다고 가정해 보자.
# 명령 프롬프트 창에서 파이썬 셸을 열어
# 이 모듈을 import 해서 사용할 수 있는 방법을 모두 기술하시오.
# ? 파일쪽 공부

# 12. 오류와 예외 처리
# 다음 코드의 실행 결과를 예측하고 그 이유에 대해 설명하시오.
'''
result = 0
try:
    [1,2,3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)
'''

# q13   # 이런문제유형 많다...
# DashInsert 함수는
# 숫자로 구성된 문자열을 입력받은 뒤
# 문자열 안에서 홀수가 연속되면
# 두 수 사이에 - 를 추가하고,
# 짝수가 연속되면 * 를 추가하는
# 기능을 갖고 있다. DashInsert 함수를 완성하시오.
# 입력 예시 : 4546793 출력 예시 : 454*67-9-3
'''
def DashInsert(str):
    a=str 을 슬라이싱하고 저장
    while 요소 in a:
        dash_inset_a[요소]=a[요소]
        if 1번 요소랑 0번 요소랑 짝수 연속이면:
            1번 요소랑 0번 요소 사이에 * 삽입
        elif 1번 요소랑 0번 요소가 홀수 연속이면:
            1번 요소랑 0번 요소 사이에 - 삽입
        else:
            그냥 지나감
        요소+=1
    return dash_insert_a
print()
'''
'''
def DashInsert(str):
    a = list(str)
    dash_insert_a = []
    
    for i in range(len(a) - 1):
        dash_insert_a.append(a[i])
        if int(a[i]) % 2 == 0 and int(a[i + 1]) % 2 == 0:
            dash_insert_a.append('*')
        elif int(a[i]) % 2 != 0 and int(a[i + 1]) % 2 != 0:
            dash_insert_a.append('-')
    dash_insert_a.append(a[-1])
    return ''.join(dash_insert_a)
print(DashInsert("4546793"))
'''
'''
in_data=input('입력')
#data="4546793"
numbers=list(map(int,in_data)) # ?
print(numbers)
result=[]
for i, num in enumerate(numbers): # ?
    result.append(str(num)) # ?
    if i<len(numbers)-1:
        is_odd=num%2==1
        is_next_odd=numbers[i+1]%2==1
        if is_odd and is_next_odd:
            result.append("-") 
        elif not is_odd and not is_next_odd:
            result.append("*")
print("".join(result))
'''           

# q14, 어려운 문제
# 문자열을 입력받아
# 같은 문자가 연속적으로
# 반복되는 경우에 그 반복 횟수를
# 표시해 문자열을 압축하여 표시하시오.
# 입력 예시 : aaabbcccccca 출력 예시 : a3b2c6a1

def compress_string(s):
    if not s:
        return ""
    
    compressed=[]
    count=1
    current_char=s[0] # 첫번째 문자 저장

    for i in range(1,len(s)):
        if s[i]==current_char: # 현재 문자와 이전 문자가 같을때
            count+=1 # 반복 횟수 증가
        else:
            compressed.append(current_char + str(count))
            current_char = s[i] # 현재 문자를 새로운 문자로 변경
            count=1 # 카운트를 1로 다시 초기화

    # 마지막 문자와 그 카운트를 추가
    compressed.append(current_char + str(count))

    return ''.join(compressed) #공백없이 결합해서 리턴

# 밑에 더 있는거 같은데??



# q15
# Duplicate Numbers 09의 문자로 된 숫자를 입력받았을 때,
# 이 입력값이 09의 모든 숫자를
# 각각 한 번씩만 사용한 것인지
# 확인하는 함수를 작성하시오.
# 입력 예시 : 0123456789 01234 01234567890 6789012345 012322456789
# 출력 예시 : true false false true false
# 입출력 예시 보기 좋게 변경
'''
# 0123456789 True
# 01234 False 0~9가 다 들어가지 않음
# 01234567890 False 0이 두번 입력
# 6789012345 True
# 012322456789 False 2가 다중 입력
'''
'''
문자로 처리할건지, 숫자로 변환해서 처리할건지?
문자로 처리해야하지 않을까?
input으로 숫자를 입력받음(문자), 여러개 숫자 동시에 입력 가능
리스트 a에 저장(a는 문자)

1. a[i]의 길이가 10보다 길다 또는 짧다 바로 False
2. a[i]의 길이가 10인것만 True인지 검증
2.1 a[i]를 슬라이싱 해서 리스트 b로
2.2 리스트 b를 슬라이싱해서 10개로 만든후 각 슬라이싱한것들이 중복인지 확인
2.3 b[i]부터 시작, 중복이면? 동작을 멈추고 return False
    중복이 아니면 b[i+1]로  변경 후 중복검사
    끝까지 중복이 아니면 return True, 아니면 return False -> a[i]
'''
'''
def check_unique_numbers(s):
    # 각 숫자의 등장 횟수를 세기 위한 리스트
    number_count = [0] * 10
    print([number_count])
    # 문자열의 각 문자를 확인하여 숫자만 카운트
    for char in s:
        number_count[int(char)] += 1
    # 모든 숫자가 정확히 1번만 등장하는지 확인
    return all(count == 1 for count in number_count if count > 0)
# 예시 입력 리스트
inputs = ["0123456789", "01234", "01234567890", "6789012345", "012322456789"]
# 각각의 입력에 대해 함수 실행 후 결과 출력
for inp in inputs:
    print(check_unique_numbers(inp))
'''
'''
def chkDupNum(s):
    result=[]
    for num in s:
        if num not in result: # 이부분이 중요
            result.append(num)
        else:
            return False
    return len(result)==10

print(chkDupNum("0123456789"))
print(chkDupNum("01234"))
print(chkDupNum("01234567890"))
print(chkDupNum("6789012345"))
print(chkDupNum("012322456789"))
'''

# q16 모스부호 문제

dic = { '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G',
       '....':'H','..':'I','.---':'J','-.-':'K','.-..':'L', '--':'M','-.':'N',
       '---':'O','.--.':'P','--.-':'Q','.-.':'R', '...':'S','-':'T','..-':'U',
       '...-':'V','.--':'W','-..-':'X', '-.--':'Y','--..':'Z' 
}

def morse(src):
    result=[]
    for word in src.split("  "):
        for char in word.split(" "):
            result.append(dic[char])
        result.append(" ")
    return "".join(result)

print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))