#encoding: UTF8
import time,re

str = 'abcdefghijklmn'
before_loop = time.clock()
for i in range(1000):
  pass
after_loop = time.clock()
before = time.clock()
for i in range(1000):
  re.match(r'^abc.*',str)
  pass
print (time.clock()- before - (after_loop - before_loop))

