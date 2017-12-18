package day7

// full regex for reference : /(\w+) \((\d+)\)( -> )?(.+)?/

String findBottom(List<String> programs) {
  def names = programs.collect { (it =~ /(\w+).*/)[0][1] }.toSet()

  def children = programs.collect {
    def matcher = ((it =~ /.* -> (.*)/))
    (matcher.matches()) ? (matcher[0][1] as String).split(',')*.trim() : null
  }.findAll().flatten().toSet()

  return (names - children).first()
}

assert findBottom([
  'pbga (66)',
  'xhth (57)',
  'ebii (61)',
  'havc (66)',
  'ktlj (57)',
  'fwft (72) -> ktlj, cntj, xhth',
  'qoyq (66)',
  'padx (45) -> pbga, havc, qoyq',
  'tknk (41) -> ugml, padx, fwft',
  'jptl (61)',
  'ugml (68) -> gyxo, ebii, jptl',
  'gyxo (61)',
  'cntj (57)',
]) == 'tknk'

def input = new File('input.txt').readLines()
println findBottom(input)
