# generator.py
def mygen():
    for i in range(1, 1000):
        result = i * i
        yield result

gen = mygen()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# generator2.py
import time

def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"

list_job = (longtime_job() for i in range(5))
print(next(list_job))
[longtime_job() for i in range(5)]
# 코드를 제너레이터 표현식 (longtime_job() for i in range(5)) 으로 바꾸었을 뿐이다.
# 그런데 실행 시 1초의 시간만 소요되고 출력되는 결과도 전혀 다르다.

# job start
# done
# 왜냐하면 제너레이터 표현식으로 인해 longtime_job() 함수가
# 5회가 아닌 1회만 호출되기 때문이다.
# 이러한 방식을 느긋한 계산법(lazy evaluation)이라고 부른다.
# 시간이 오래 걸리는 작업을
# 한꺼번에 처리하기보다는
# 필요한 경우에만 호출하여 사용할 때 제너레이터는 매우 유용하다.