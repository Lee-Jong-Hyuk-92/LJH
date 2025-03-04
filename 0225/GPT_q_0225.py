#Q1. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자. 0
'''
def is_odd(x):
    if x>=1:
        if x%2==0:
            print(f'{x}는 짝수입니다.')
        else:
           print(f'{x}는 홀수입니다.')
    else:
        print('자연수가 아닙니다.')
is_odd(int(input('숫자를 입력하세요')))
'''

'''
def is_odd(number):
  if number % 2==1:
    return True
  else:
    return False
a=is_odd(a)
'''
# Q2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해보자. (단, 입력으로 들어오는 수의 개수는 정해져 있지 않다. ?
'''
def total_sum(a,*b):
    i=1
    while i<a+1:
        sum=0
        sum= sum+int(input('숫자를 입력하세요'))
        i+=1
    return sum
name = input('몇개를 입력하실까요?')
print(total_sum(int(name), ))
'''
'''
def avg_num(*args):
  result=0
  for i in args:
    result += i
  result = result/len(args)
  return result
print(avg_num(1,2))
print(avg_num(1,2,4,8,16,32,64))
'''
# Q3. 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다. 0
'''
input1 = int(input("첫 번째 숫자를 입력하세요:"))
input2 = int(input("두 번째 숫자를 입력하세요:"))

total = input1 + input2
print(f"두 수의 합은 {total}입니다.")
'''
'''
위 식에 대한 출력값이다.
첫 번째 숫자를 입력하세요: 3 두 번째 숫자를 입력하세요: 6 두 수의 합은 36입니다.
3과 6을 입력했을 때, 9가 아닌 36을 반환했다.
이 프로그램의 오류를 수정해보자.
'''

#Q4. 다음 중 출력 결과가 다른 것 한 개를 골라보자. 4번X 3번, 3번은 떨어져서 나오고 나머지는 붙어서 나온다
'''
print('you' 'need' 'python')
print('you'+'need'+'python')
print('you', 'need', 'python') #쉼표가 있으면 한칸 떨어져서 나온다다
print(''.join(['you', 'need', 'python']))
'''


#Q5. 다음은 “text.txt”라는 파일에 “Life is too short” 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다. 0
'''
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close() #닫으면 된다

f2 = open("test.txt", 'r')
print(f2.read())
'''
'''
이 프로그램은 우리가 예상한 “Life is too short”라는 문장을 출력하지 않는다.

우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해보자.
'''

#Q6. 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해보자.(단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야한다.) ?
'''
user_input = input("저장할 내용을 입력하세요 : ")
f = open('test.txt', 'w')
f.write(user_input)
f.close()
'''
'''
user_input = input("저장할 내용을 입력하세요 : ")
f = open('test.txt', 'a')
f.write(user_input)
f.write('\n')
f.close()
'''
#Q7. 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 ‘java’라는 문자열을 ‘python’으로 바꾸어서 저장해 보자. ?

'''
Life is too short

you need java

'''

'''
f = open('test.txt', 'w')
f.write("Life is too short\n")
f.write("you need java")
f.close()

f=open('test.txt', 'w')
contents = f.read()
contents.replace('java','python')
f.close()
'''
'''
f = open('test.txt', 'w')
f.write("Life is too short\n")
f.write("you need java")
f.close()

f=open('test.txt', 'w')
contents = f.read()
contents.replace('java','python')
f.close()

f=open('test.txt', 'r')
body=f.read()
f.close()

body=body.replace('java','python')
f=open('test.txt','r')
f.close()
'''

#GPT 문제
'''
1.문자열을 반대로 뒤집는 함수 작성하기
주어진 문자열을 반대로 뒤집는 함수 reverse_string을 작성하세요. 예를 들어, 입력 문자열이 “Python”이면 출력은 “nohtyP”이어야 합니다.
'''
'''
def reverse_string(str):
    return str[::-1] #처음부터 -1단위로, 뒤집는게 된다

str = 'Python'
print(reverse_string(str))
'''
'''
소수를 판별하는 함수 작성하기
주어진 숫자가 소수인지 아닌지를 판별하는 함수 is_prime을 작성하세요. 소수는 1과 자기 자신만을 약수로 갖는 1보다 큰 양의 정수입니다. 함수는 소수일 경우 True를 반환하고, 아닐 경우 False를 반환해야 합니다.
def f(a):
    if a<1:
        print('소수가 아닙니다.')
        break
    if 
'''
'''
def is_prime(num):
    #소수인 조건이 뭐야? 1보다 크고, 1과 자기자신 말고는 나눠지지 않는수
    if 소수:
        return True
    else:
        return False

    #숫자를 입력받고, 숫자를 is_prime() 함수를 호출해서 소수인지 아닌지를 판별, 판별해서 소수이면 True, 아니면 Flase 반환

print('소수입니다.')
print('소수가 아닙니다.')
'''
'''
사용자로부터 숫자를 입력받아 제곱한 값을 출력하기
사용자로부터 숫자를 입력받아 그 숫자의 제곱 값을 출력하는 프로그램을 작성하세요.

사용자로부터 이름과 나이를 입력받아 10년 후의 나이 출력하기
사용자로부터 이름과 나이를 입력받아, 10년 후의 나이를 출력하는 프로그램을 작성하세요.

사용자로부터 입력받은 내용을 파일에 작성하기
사용자로부터 입력받은 내용을 파일에 작성하는 프로그램을 작성하세요. 파일 이름은 “input.txt”로 합니다.

명령 줄 인수를 사용하여 두 숫자의 사칙연산 결과 출력하기
명령 줄 인수로 두 숫자와 사칙연산 기호(+, -, *, /)를 입력받아 계산 결과를 출력하는 프로그램을 작성하세요.

'''
#갑자기 중요하다고 하면서 알려주심
'''
import sys
args = sys.argv[1:]
for i in args:
  print(i)
'''