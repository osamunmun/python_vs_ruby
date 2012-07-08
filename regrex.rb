# encoding: UTF-8

require "benchmark"

str="abcdefghijklmn"
match=/^abc.*/
puts Benchmark.measure{
1000.times do
end
}
puts Benchmark.measure{
1000.times do
  match =~ str
end
}
