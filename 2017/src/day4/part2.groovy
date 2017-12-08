package day4

def isValidPassword(String password) {
  def words = password.split(' ').collect { it.chars.toList().sort() }
  return words.size() == words.toSet().size()
}

assert isValidPassword('abcde fghij')
assert !isValidPassword('abcde xyz ecdab')
assert isValidPassword('a ab abc abd abf abj')
assert isValidPassword('iiii oiii ooii oooi oooo')
assert !isValidPassword('oiii ioii iioi iiio')

assert isValidPassword('abc abca')

def input = new File('input.txt').readLines()*.trim()
println input.findAll { isValidPassword(it) }.size()
