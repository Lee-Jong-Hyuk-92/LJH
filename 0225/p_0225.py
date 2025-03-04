'''
today = '수요일'
if today == '일요일':
    print('게임한판')
elif today == '토요일':
    print('폰 5분만')
elif today == '수요일':
    print('오늘은 수요일')
else:
    print('물 한잔')
print('공부시작')


yellow_card = 0
foul = False
if foul:
   yellow_card += 1
   if yellow_card == 2:
     print('경고누적퇴장')
   else:
     print('휴.. 조심해야지')
else:
   print('주의')


for x in range(1,13,1): #x는 임시변수, 1부터 13미만 1 단위로 증가
    print(f'팔벌려뛰기 {x}회')

for x in range(10): #x는 임시변수, 1부터 12까지 1 단위로
    print(f'팔벌려뛰기 {x+1}회')


my_list=[4,2,7]
for x in my_list:
    print(x)


person= {'이름': '나귀욤', '나이': 7,'키': 120, '몸무게': 23}
for v in person.items():
    print(v)
for k, v in person.items():
    print(v)

fruit = 'apple'
for x in fruit:
    print(x)


max = 25 # 최대 허용 무게
weight = 0 # 현재 캐리어 무게
item = 3 # 각 짐의 무게
while weight + item <= max:
    weight += item
    print(f'짐을 추가합니다, 현재 짐 무게는 {weight}입니다.')
print(f'총 무게는 {weight} 입니다')


drama = ['시즌1', '시즌2', '시즌3', '시즌4', '시즌5']
for x in drama:
    if x == '시즌3':
        print('재미 없대, 그만 보자')
        break   #반복문 탈출
    print(f'{x} 시청')

for x in drama:
    if x == '시즌3':
        print('재미 없대, 그만 보자')
        continue    #다음 반복수행
    print(f'{x} 시청')


# 많이 중요, 비슷한거 아무생각 없이 가능할 정도로 연습
products = ['JOA-2020', 'JOA-2021', 'SIRO-2021', 'SIRO-2022'] #원본 리스트는 건드리지 않는다.
recall = [ ] # 리콜 대상 제품 리스트
for p in products:
    if p.startswith('SIRO'): # 제품명이 SIRO 로 시작하는가?
        recall.append(p)
print(recall)

# 위에것도 길다!!
# new_list = [변수 활용 for 변수 in 리스트 if 조건]
my_list = [1, 2, 3, 4, 5]
new_list = [x for x in my_list if x > 3]
#(1) my_list 에서
#(2) if x > 3 : 3보다 큰 값들만
#(3) x : 그대로 사용해서
#(4) 새로운 리스트로만들어줘
print(new_list)


products = ['JOA-2020', 'JOA-2021', 'SIRO-2021', 'SIRO-2022']
recall2 = [x for x in products if x.startswith('SIRO')]
print(recall2)


# 함수
def show_price():
    print('10,000원 입니다.')
show_price()#호출


#def 함수명(전달값):    전달값은 여러개일수 있다.
#    수행할 문장
def show_price(customer):
    print(f'{customer}고객님')
    print('10,000원 입니다.')

cus1 = '나장발'
show_price(cus1) #cus1 = 인자, call 호출할때 넣어야 한다
cus2 = '나수염'
show_price(cus2)


#반환값, 일반적으로 함수는 리턴값이 있다
def get_price():
    return 15000
price = get_price() # price = 15000
print(price)


def get_price(is_vip):
    if is_vip==True:
        return 10000
    else:
        return 15000
price = get_price(True)
print(f'단골손님은 {price}원 입니다.')


def cal(a,b):
    return a+b, a-b, a*b, a/b
result=cal(1,2)
s, minus, multiple, division = result
print(s,minus,multiple,division)


def get_price(is_vip=False): # 이 함수가 호출될때 자동으로 전달값이 False, True : 단골 손님, False : 일반 손님
   if is_vip == True:
     return 10000 # 단골 손님
   else:
     return 15000 # 일반 손님
price1 = get_price(True) # 단골 손님
price2 = get_price() # 일반 손님
print(price2)
price3 = get_price(False) # 일반 손님


def order(shot=2, size='Regular', takeout=True): # 커피주문
    print(f'아메리카노 {size}사이즈 {shot}샷')
    if takeout:
        print('포장주문이 완료되었습니다.')
    else:
        print('주문이 완료되었습니다.')
#order()
#아메리카노 Regular사이즈 2샷
#포장주문이 완료되었습니다.

#order(2, takeout=True)
#아메리카노 Regular사이즈 2샷
#포장주문이 완료되었습니다.

#order(size='Regular')
#아메리카노 Regular사이즈 2샷
#포장주문이 완료되었습니다.

#order('Regular', takeout=True)
#아메리카노 Regular사이즈 Regular샷
#포장주문이 완료되었습니다.

order(10,20,False)
#아메리카노 20사이즈 10샷
#주문이 완료되었습니다. 포장 아님.


def visit(today, *customers): #가변인자, 전달값이 많을때 마지막에 한번만 * 표시
    print(today)
    for customer in customers:
        print(customer)
visit('오늘', '나')
print('-'*10)
visit('오늘', '나', '너')
print('-'*10)
visit('오늘', '나', '너', '우리')
print('-'*10)
visit('오늘', '나', '너', '우리', '그밖')


def print_kwargs(**kwargs): #딕셔너리 전용 가변인자 *를 2개 사용
    print(kwargs)
    return(kwargs)
res=print_kwargs(name='foo', age=3, height = 150)
print(res, type(res))


name = input('이름이 뭔가요?')
print(name)


num = int(input('몇분이세요?')) #int()한 이유, 인트로 안하면 숫자를 입력했을때 문자로 받아들여서 아래쪽 if문에서 숫자 비교가 되지 않음
if num>4:
    print('죄송하지만, 4명까지만 예약가능합니다.')


#파일 열기, 실무에 가까운 느낌
f = open('list.txt', 'w', encoding='utf8') #없는데 뭘여냐? 만들거다.쓰기모드로, 인코딩 확실하게 해주면 좋다, 안깨지고
f.write('김지훈\n') #\n은 엔터
f.write('정대만\n')
f.write('허난중\n')
f.close() #다썼으면 닫아줘야 한다.

f = open('list.txt', 'r', encoding='utf8')
contents = f.read()
print(contents)
f.close() # 파일 닫기

f = open('list.txt', 'a', encoding='utf8')
f.write('가나다\n')
f.write('가나다\n')
f.write('가나다\n')
f.close()

f = open('list.txt', 'r', encoding='utf8')
contents = f.read()
print(contents)
f.close() # 파일 닫기


f = open('list.txt', 'r', encoding='utf8')
for line in f:
    print(line, end='')


with open('list.txt', 'w', encoding='utf8') as f: #as = alias 애칭
    f.write('가나다\n')
    f.write('가2다\n')
    f.write('가4다\n') #알아서 close() 해준다


with open('list.txt', 'r', encoding='utf8') as f:
    contents = f.read()
    print(contents)

'''