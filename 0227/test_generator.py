def mygen():
    yield 'a'
    yield 'b'
    yield 'c'

g = mygen()
print(next(g))
print(next(g))
print(next(g))