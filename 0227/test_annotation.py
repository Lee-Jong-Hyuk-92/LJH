def add(a: int, b: int) -> int: # annotation, 어노테이션, 힌트
    return a+b

result = add(3, 3.4)
print(result)  # 6.4 출력
# int라고 되어있는데 결과값이 출력되는 이유는
# 어노테이션은 체크가 아닌 힌트이다.