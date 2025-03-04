# iterator.py
# iterator  반복자

a=[1,2,3] #리스트
ia=iter(a) #ia는 이터레이터 객체 변수

for i in ia:
    print(i)

for i in ia: #한번쓰면 또 쓸수 없다
    print(i)