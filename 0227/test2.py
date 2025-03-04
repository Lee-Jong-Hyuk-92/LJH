a='한글'
b=a.encode('euckr')
print(b, type(b))

#c=b.decode('utf-8')
#print(c)

d=b.decode('euckr')
print(d)