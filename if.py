#encoding: UTF8
import time

i = 0
i2 = 0
before_loop = time.clock()
for i in range(1000000):
  pass
after_loop = time.clock()
before = time.clock()
for i in range(1000000):
  (i == i2)
  pass
print (time.clock()- before - (after_loop - before_loop))

i = 'abc'
i2 = 'abc'
before_loop = time.clock()
for i in range(1000000):
  pass
after_loop = time.clock()
before = time.clock()
for i in range(1000000):
  (i == i2)
  pass
print (time.clock()- before - (after_loop - before_loop))
