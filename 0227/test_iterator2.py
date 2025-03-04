# iterator.py
class MyItertor:
    def __init__(self, data):
        self.data = data
        self.position = 0

    def __iter__(self): # 반복행위가 일어나면 자동 수행
        return self

    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result

if __name__ == "__main__": #직접 실행할때만
    i = MyItertor([1,2,3])
    for item in i:
        print(item)

# 디버그 찍어보면서 어떻게 동작하는지 확인하기!
# AI 가 모델을 학습할때 한번씩만 학습하도록 하기 위한 안전장치.
# 어떤 데이터들은 10000번 학습, 나머지는 한번씩만 학습하면 모델이 이상해진다.