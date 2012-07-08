#encoding: UTF8
import time

i2 = 1
i3 = 2
before_loop = time.clock()
for i in range(1000000):
  pass
after_loop = time.clock()
before = time.clock()
for i in range(1000000):
  i = i2 + i3
  pass
print (time.clock()- before - (after_loop - before_loop))

