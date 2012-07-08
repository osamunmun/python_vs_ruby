#encoding: UTF8
import time,random

n = 100000
list = []
for i in range(n):
  list.insert(0,random.randint(1,n))
before_loop = time.clock()
for i in range(n):
  pass
after_loop = time.clock()
before = time.clock()
for i in range(n):
  list.sort()
  pass
print (time.clock()- before - (after_loop - before_loop))

