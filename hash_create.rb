# encoding: UTF-8

require "benchmark"

hash = Hash.new
10000.times {|i|
  hash[i.to_s] = i
}
puts Benchmark::CAPTION
puts Benchmark.measure{
10000.times {|i|
  i.to_s
}
}
puts Benchmark.measure{
10000.times {|i|
  hash[i.to_s]
}
}
