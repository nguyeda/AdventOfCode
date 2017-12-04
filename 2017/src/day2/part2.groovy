package day2

def pair = { List<Integer> row ->
  def r = row.collect()
  List<List<Integer>> p = []
  while (!r.empty) {
    p.addAll([r.pop(), r].combinations())
  }
  p*.sort(true)
}

def checksum = { List<List<Integer>> input ->
  input.sum { List<Integer> row ->
    pair(row)
      .find { it.last() % it.first() == 0 }
      .inject { first, last -> last / first }
  }
}

assert checksum([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]) == 9

def input = new File('input.txt').readLines().collect { it.split(/ +|\t/)*.trim().collect { it as int } }
println checksum(input)
