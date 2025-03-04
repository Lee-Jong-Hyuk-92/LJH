#Q1. 다음 코드의 결괏값은? shirt 0
'''
a  = "Life is too short, you need python"
if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:  #조건 만족, 이것만 출력 후 종료
    print("shirt")
elif "need" in a:
    print("need")
else: print("none")
'''
#Q2. while문을 사용해 1부터 1000까지 자연수 중 3의 배수의 합을 구하라. 0
'''
result = 0
i = 1
while i <= 1000:
    if i%3==0:
        result += i
    i += 1
print(result)
'''
# Q3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해보자. 0
'''
i = 0
while True:
    if i>=5:
        break
    i += 1
    print('*'*i)
'''
'''
i=0
while True:
    i+=1
    if i >5:
        break
    print('*'*i)
'''
# Q4. for문을 사용해서 1부터 100까지의 숫자를 출력해라. 0
'''
for x in range(100):
   print(x+1, end='  ')
'''
# Q5. A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다. for문을 사용하여 A학급의 평균 점수를 구해보자. 0
'''
a=[ 70, 60, 55, 75, 95, 90, 80, 80, 85, 100 ]
sum=0
for x in a:
   sum=sum+x
print(sum/len(a))
'''
#Q6. 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음과 같은 코드가 있다. 아래 코드를 리스트 내포(list comprehension)을 사용하여 표현해보자.
'''
numbers = [1,2,3,4,5]
result = []
for x in numbers:
    if x%2==1:
        result.append(x*2)
print(result)
'''

numbers = [1,2,3,4,5]
result = [x*2 for x in numbers if x%2==1]
print(result)