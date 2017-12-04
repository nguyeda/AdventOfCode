package day2

def checksum = { List<List<Integer>> input ->
  input.sum { List<Integer> row ->
    row.subsequences()
      .findAll { it.size() == 2 }
      *.sort()
      .find { it.last() % it.first() == 0 }
      .inject { first, last -> last/first }
  }
}

assert checksum([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]) == 9

def input = new File('input.txt').readLines().collect { it.split(/ +|\t/)*.trim().collect { it as int } }
println checksum(input)
