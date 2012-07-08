#encoding: UTF8
import time

dict = {}
i2 = 0
before_loop = time.clock()
for i in range(10000):
  str(i)
  pass
after_loop = time.clock()
before = time.clock()
for i in range(10000):
  dict[str(i)] = i
  pass
print (time.clock()- before - (after_loop - before_loop))

