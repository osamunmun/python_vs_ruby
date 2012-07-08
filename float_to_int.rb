# encoding: UTF-8

require "benchmark"

i2 = 0.to_f
puts Benchmark::CAPTION
puts Benchmark.measure{
1000000.times do
end
}
puts Benchmark.measure{
1000000.times do
  i = i2.to_i
end
}
