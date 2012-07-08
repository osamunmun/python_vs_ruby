# encoding: UTF-8

require "benchmark"
f = 0.to_f
f2 = 1.to_f
f3 = 2.to_f
puts Benchmark::CAPTION
puts Benchmark.measure{
1000000.times do
end
}
puts Benchmark.measure{
1000000.times do
  f = f2/f3
end
}
