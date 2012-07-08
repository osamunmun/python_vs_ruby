# encoding: UTF-8

require "benchmark"

i = 0
i2 = 0
puts Benchmark::CAPTION
puts Benchmark.measure{
1000000.times do
end
}
puts Benchmark.measure{
1000000.times do
  (i == i2)
end
}
i = 'abc'
i2 = 'abc'
puts Benchmark.measure{
1000000.times do
  (i == i2)
end
}
