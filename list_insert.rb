# encoding: UTF-8

require "benchmark"
i = 0
list = Array.new
1.upto(100000) {|i|
  list.insert(0,i)
}
puts Benchmark::CAPTION
puts Benchmark.measure{
1.upto(100000) {|i|
}
}
puts Benchmark.measure{
1.upto(100000) {|i|
  list.shift
}
}
