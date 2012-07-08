#encoding: UTF8
import time

f = float(0)
before_loop = time.clock()
for i in range(1000000):
  pass
after_loop = time.clock()
before = time.clock()
for i in range(1000000):
  i = int(f)
  pass
print (time.clock()- before - (after_loop - before_loop))

