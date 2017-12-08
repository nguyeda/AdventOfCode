
def isValidPassword(String password) {
  List<String> words =  password.split(' ')
  return words.size() == words.toSet().size()
}

assert isValidPassword('aa bb cc dd ee')
assert !isValidPassword('aa bb cc dd aa')
assert isValidPassword('aa bb cc dd aaa')

def input = new File('input.txt').readLines()*.trim()
println input.findAll { isValidPassword(it) }.size()
