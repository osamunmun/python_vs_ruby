#encoding: UTF8
import time

list = []
for i in range(1000):
  list.insert(0,i)
before_loop = time.clock()
for i in range(1000):
  pass
after_loop = time.clock()
before = time.clock()
for i in range(1000):
#  list.pop(0)
  list[0]
  pass
print (time.clock()- before - (after_loop - before_loop))

