package day5


def jump(List<Integer> input) {
  def maze = input.collect()
  def currentIndice = 0
  def steps = 0
  while (currentIndice >= 0 && currentIndice < maze.size()) {
    def currentValue = maze[currentIndice]
    def nextIndice = currentIndice + currentValue
    maze[currentIndice] = ++currentValue
    currentIndice = nextIndice
    steps++
  }
  steps
}

assert jump([0, 3, 0, 1, -3]) == 5

def input = new File('input.txt').readLines().collect { it.trim() as int }
println jump(input)
