#encoding: UTF8
import time

f = float(1.0)
f2 = float(1.0)
before_loop = time.clock()
for i in range(1000000):
  pass
after_loop = time.clock()
before = time.clock()
for i in range(1000000):
  f = f2
  pass
print (time.clock()- before - (after_loop - before_loop))

