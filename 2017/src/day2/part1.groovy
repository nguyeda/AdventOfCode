package day2

def checksum = { List<List<Integer>> input ->
  input.sum { it.max() - it.min() }
}

assert checksum([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]) == 18

def input = new File('input.txt').readLines().collect { it.split(/ +|\t/)*.trim().collect { it as int } }
println checksum(input)
