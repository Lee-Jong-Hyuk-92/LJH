'''
print('1')#정수
print('3.14')#실수

#중요한건 문자자료

print('hello')
print("안녕하세요") # 작은따옴표, 큰따옴표 모두 문자자료, 강사님은 작은따옴표를 사용

print('5') #이건 문자 5, 더하기 빼기 되지 않음

evel = 10000
evel2 = 20000
evel3 = '안녕하세요'

print(evel)
print(evel2)
print(evel3)


name2 = '1'
print('name2')


print(int(float('3.99')))

print(5+2)
print(5-2)
print(5*2)
print(5/2)

print(5%2) # 5나누기 2의 나머지
print(5//2) #5나누기 2의 몫
print(5**2) #5^2

#비교연산
print(5>2) #5가 2보다 크냐?
print(5>=2) # 5가 2보다 크거나 같냐
print(5<2) # 5가 2보다 작냐
print(5<=2) # 5가 2보다 작거나 같냐

print(5==2) #5랑 2가 같냐
print(5!=2) # 5랑 2가 다르냐냐

#논리연산
print(3<5 and 7<5) #3이 5보다 작고, 7이 5보다 작냐
print(3<5 or 7<5) #3이 5보다 작고 또는 7이 5보다 작냐
print(not 7<5) #7이 5보다 작냐의 결과 반대

#멤버 연산
print('c' in 'cat') # cat안에 c가 있냐
print('c' not in 'cat') # cat안에 c가 있냐에서 있냐 반대

print(3 > 5)
print(bool(None))
print(bool('False'))

#작은 따옴표 3개는 여러 문장 주석처리

#인덱싱은 잘라서 한부분만
lang = 'PYTHON'
# P     Y       T       H       O       N
# 0     1       2       3       4       5
#-6     -5      -4      -3      -2      -1
print(lang[-1]) #-1은 마지막!!

#슬라이싱 어디부터 어디까지
print(lang[1:])#1번부터 끝까지
print(lang[:5])#처음부터 5미만까지(인덱싱 4번까지)
print(lang[2:6])#인덱싱2번부터 인덱싱 6번 미만까지(5번까지)
print(lang[:])#전체
print(lang[:-1])#마지막 한글자 빼고 다

snack='꿀꽈배기'
two ='2개'
num =4
print(snack + '' +two)
juseyo = snack+two
juseyo = juseyo +'주세요'
print(juseyo)

print(len(snack)) #len은 길이


snack=#꿀꽈배기
#2개
#있네요
#이부분 작은따옴표 3개 나중에 지워야함
#print(snack)


print('-'*10)
print('안녕하세요')
print('-'*10)


letter = 'how are YOU? how how how' #모든 내용을 소문자로?
print(letter.lower()) #모두 소문자
print(letter.upper()) #모두 대문자
print(letter.capitalize()) #문장의 첫번째만 대문자
print(letter.title()) # 각 어절의 첫글자만 대문자
print(letter.swapcase())#소문자는 대문자로, 대문자는 소문자로


print(letter.split()) # 엄청많이 쓰일거다, 외워라!!
print(letter.count('how')) #'how' 가 몇번 쓰였는지지

#필수는 split(), 무조건 외워라
# .찍고 Ctrl + Space 하면 예문 영어로 보여줌



s = '나도고등학교'
print(s.startswith('나도'))
print(s.endswith('고등학교')) #.jpg .mp3 .txt 확장자 검색용, 고급적인 코딩, 효율적인코딩


s = '   ...나도고등학교...   ' # 띄어쓰기 3번, . 3번이 좌우에 있다
print(s.strip('.'))
print(s.lstrip('.'))
print(s.rstrip('.'))
print(s.strip(' '))
print(s.lstrip(' '))
print(s.rstrip(' '))


s = '나도고등학교'
print(s.replace('고등학교', '초교'))#“고등학교” 를 “초교” 로 변경



s = '나도고등학교'
print(s.find('학교'))#학교는 어디서 시작?


startswith()
endswith()
strip()     이 4가지 중요
replace()



python = '파이썬'
java = '자바'
c = 'C언어'
print(python + java) #둘 다 출력하려면?
print(python, java, c)
print('개발 언어에는' + ' ' + python, java, c + '가 있어요.') # 지저분하다, 구분도 어렵고
print('개발 언어에는 {}, {}, {}가 있어요'.format(python, java, c))
print('개발 언어에는 {2}, {1}, {0}가 있어요'.format(python, java, c)) # python이 0, java가 1, c가 2
print(f'개발 언어에는 {python}, {java}, {c}가 있어요')

# 예) printf(f'현재값은 {심박수}, {혈압}, {산소포화도}') 중요하다!!


print('하지만 \'나만 당할 순 없지\'라는 생각에 \"엄청 쉽지\" 라고 했다.') 역슬래쉬 뒷부분은 작은따옴표, 큰따옴표 무시, 탈출문자

#print('C:\\a\\test.py')
#print(r'C:\a\test.py') #raw string, 이게 더 효과적!!

snack = '꿀꽈배기는\n너무\n맛있어요'
print(snack)



my_list = ['오예스', '몽쉘', '초코파이']
my_list = ['오예스', '몽쉘', '초코파이', '초코파이'] # 중복허용
your_list = [1, 2, 3.14, True, False, '아무거나'] #다른 타입의 변수 입력 가능, python에서는 가능

print(my_list[0])

my_list = ['오예스', '몽쉘', '초코파이']
my_list[1] = '몽쉘카카오' # 값 수정
my_list.append('빅파이') # 값 추가, 리스트를 수정하려면?
#print(my_list)

my_list.remove(('오예스')) # 값 삭제
# print(my_list)

your_list = ['빅파이', '오뜨']
my_list.extend(your_list) # 리스트 확장
print(my_list)



my_list = ['오예스', '몽쉘', '초코파이', '카카오오']
#my_list.insert(1,'여기 맞나')
#print(my_list)

#my_list.pop(1)
#print(my_list)


#my_list.clear()
#print(my_list)


#my_list.sort()
#print(my_list)

#my_list.reverse()
#print(my_list)

#copy_list = my_list.copy()
#print(copy_list)

print(my_list.count('오예스'))
print(my_list.index('카카오오'))


# 튜플 =(값1, 값2, ...) 수정불가, 읽기전용, 인덱싱은 된다(읽기니까), 인덱싱이 되니까 슬라이싱도 된다, 패킹(묶는다)
my_tuple=('오예스', '몽쉘', '초코파이', '카카오')

print(my_tuple[1]) #인덱싱은 []

print(my_tuple[0:2])


pie1, pie2, pie3, pie4 = my_tuple # 언패킹, 정말 많이 쓰이는 문법

print(pie1, pie2, pie3, pie4)

#예
# height, width, channel = img.shape  사진 파일 정보, 가로, 세로, 채널 정보

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#one, two, *others = numbers # *매개변수, pointer랑 비스무리?? 인데 포인터라고 안한다
#print(one, two, others) # others는 리스트형태라는것 주의
#print(others, type(others)) # 타입 확인하고싶을때

*others, nine, ten = numbers
print(others, nine, ten)


#세트 순서랑, 중복 허용X, 중괄호, 어떤 단어가 몇번 쓰였을까??, 인덱싱이 안되서 수정이 불가, 근데 특이하게 추가는 가능, 제거는 된다.
#세트 ={값1, 값2, ...}

A={'돈까스','보쌈','제육덮밥'}
B={'짬뽕','초밥','제육덮밥'}

print(A.intersection(B)) #교집합
print(A.union(B)) #합집합
print(A.difference(B)) #차집합



#딕셔너리, 마지막 자료형
#튜플모양(key, value) key는 중복불가
'''

person = {'이름': '나귀욤', '나이': 7,'키': 120, '몸무게': 23}
'''
print(person)
print(person['이름'])
print(person['나이'])
print(person.get('별명'))
person['최종학력'] = '유치원'
print(person)
person['키'] = 130
print(person)

#여러가지 한번에 바꿀때
person.update({'키': 160 , '몸무게':46})
print(person)

#삭제는 pop
person.pop('몸무게')
print(person)

print(person.keys())  #이거 3개는 외우자
print(person.values())
print(person.items())

print(person.fromkeys('이'))
print(person.popitem())
print(person)


# 리스트=[], 튜플=(), 세트={}, 딕셔너리={key:val}  다 중요하다, 완벽하게 알아야 한다, 구조, 특징

my_tuple = ('오예스', '몽쉘')
print(type(my_tuple)) # 튜플에 추가가 안되니까 튜플을 리스트로 자료변환후, 추가, 다시 튜플로 자료변환
my_list = list(my_tuple)
print(my_list, type(my_list))
my_list.append('초코파이')
my_tuple = tuple(my_list)
print(my_tuple)



#중복 자료 제거할때는 세트 자료형

my_list = ['오예스', '몽쉘', '초코파이', '초코파이', '초코파이']
my_set=set(my_list)
my_list=list(my_set)
print(my_list) #중복 제거는 되지만, 순서는 보장하지 않는다

#순서, 중복 두가지 다 중요한 자료라면?? -> 딕셔너리!


my_list = ['오예스', '몽쉘', '초코파이', '초코파이', '초코파이']
my_dict=dict.fromkeys((my_list)) #key를 가져다가 dictionary 딕셔너리를 만든다
print(my_dict)
my_list = list(my_dict)
print(my_list) #중복제거, 순서도 유지

'''