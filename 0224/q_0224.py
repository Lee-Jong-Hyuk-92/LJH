#Q1
kor=80
eng = 75
math = 55
print((kor+eng+math)/3)

#Q2
num = 13
if num%2==0:
    print('짝수')
else:
    print('odd')

#Q3 인덱스 이해 문제
num = '881120-1068234'
print(num[:6], num[7:])

print(num.split('-'))

#Q4
num = '881120-1068234'
print(num[7])

#Q5
str='a:b:c:d:'
str=str.replace(':','#')
print(str[0:7])


#Q6
 #[1, 3, 5, 4, 2] 리스트를
 # [5, 4, 3, 2, 1]로 만들어 보자.
 # (Hint : sort() 함수와 reverse() 함수)

l1=[1,3,5,4,2]
l1.sort()
l1.reverse()
print(l1)


#Q7
#[‘Life’, ‘is’, ‘too’, ‘short’] 리스트를
# Life is too short 문자열로
# 만들어 출력해 보자.(Hint : join()함수)

a=['Life','is','too','short']
print(l1[0], l1[1], l1[2], l1[3])
# 리스트를 문자열로 바꿀때(.txt) join()함수 사용
print(' '.join(a))


#Q8
#(1,2,3) 튜플에
# 값 4를 추가하여
# (1,2,3,4)를 만들어 출력해 보자.

t1=(1,2,3)
print(t1)
t1=list(t1)
t1.append(4)
t1=tuple(t1)
print(t1)

#답
a = (1,2,3)
b = (4, )
print(a+ b)


#Q9
'''다음과 같은 딕셔너리 a가 있다.
다음 중 오류가 발생하는 경우를 고르고,
그 이유를 설명해 보자.
'''

a = dict()
print(a,type(a))
a['name'] = 'python'
print(a)

a[('a',)] = 'python'
print(a)

# a[[1]] = 'python'
a[250] = 'python' #250번째가 아닌 이름이 250이라는 key의 values가 'python'
print(a)


#Q10 딕셔너리 a에서 ‘B’에 해당되는 값을 추출해 보자.

a = {'A':90, 'B':80, 'C':70}
print(a['B'])


#Q11 a 리스트에서 중복 숫자를 제거해 보자. a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]

# 내답
a= [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
a=dict.fromkeys(a)
a=list(a)
print(a)

#답
a= [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
set_a = set(a) #리스트 a를 세트화, 중복제거
print(set_a)
last_a = list(set_a) #세트화 했던 a를 다시 리스트화
print(last_a)

#Q12
'''파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다.
다음과 같이 a, b 변수를 선언한 후
a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까?
그리고 이런 결과가 오는 이유에 대해 설명해 보자. '''

a = b = [1, 2, 3]
print(a)
print(b)
a[1] = 4
print(a)
print(b)

a = b = [1, 2, 3] # 이렇게 정의하면 a와 b가 같은 주소
print(id(a), id(b)) #메모리 주소 출력
a[1] = 4
print(b)