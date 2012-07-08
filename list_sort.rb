# encoding: UTF-8

require "benchmark"
n = 100000
i = 0
list = Array.new
1.upto(n) {|i|
  list.insert(0,rand(i))
}
puts Benchmark::CAPTION
puts Benchmark.measure{
1.upto(n) {|i|
}
}
puts Benchmark.measure{
1.upto(n) {|i|
  list.sort!
}
}
