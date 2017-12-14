package day6

def balance(List<Integer> banks) {
  List<Integer> current = banks.collect()
  Set<List<Integer>> combinations = [banks]

  while(true) {
    def index = current.findIndexOf { it == current.max() }
    def value = current[index]
    current[index] = 0
    (1..value).each {
      current[(index + it) % current.size()] += 1
    }

    if (combinations.contains(current)) {
      return combinations.size()
    }
    combinations.add(current.collect())
  }
}

assert balance([0, 2, 7, 0]) == 5

def input = new File('input.txt').text.split(/ +|\t/).collect { it.trim() as int }
println balance(input)
