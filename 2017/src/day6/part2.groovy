package day6

def balance(List<Integer> banks) {
  List<Integer> current = banks.collect()
  List<List<Integer>> combinations = [banks]

  while(true) {
    def index = current.findIndexOf { it == current.max() }
    def value = current[index]
    current[index] = 0
    (1..value).each {
      current[(index + it) % current.size()] += 1
    }

    def i = combinations.indexOf(current)
    if (i > -1) {
      return combinations.size() - i
    }
    combinations.add(current.collect())
  }
}

assert balance([0, 2, 7, 0]) == 4

def input = new File('input.txt').text.split(/ +|\t/).collect { it.trim() as int }
println balance(input)
