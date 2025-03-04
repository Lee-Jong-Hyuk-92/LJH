'''
import goodjob_0226
goodjob_0226.goodjob()

from goodjob_0226 import goodjob
goodjob()


import random
my_list = ['가위', '바위', '보']
print(random.choice(my_list))
'''
from pack_test import goodjob   #pack_test폴더에 있는 goodjob.py파일에 접근
goodjob.goodjob()

import pack_test.module_test as mo
mo.test()

import ano.where_test as wh
wh.where()