import re
pattern = re.compile('[a-z]+') # 소문자 a~z중 어떤거든 + 하나 있어야한다
result=pattern.match('3 python')
print('match',result,'\n')

result=pattern.search('3 python')
print('search',result,'\n')

result = pattern.findall("life is too short")
print('findall',result,'\n')

result = pattern.finditer("life is too short")
print('finditer',result,'\n')
'''
r=pattern.match('python')
print(r.group())
print(r.start())
print(r.end())
print(r.span())
'''