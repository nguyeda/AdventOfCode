package day1

static int captcha(String input, int compareToIndex) {
  def sum = 0
  List<Integer> digits = input.chars.collect { Integer.parseUnsignedInt(it as String) }
  digits.eachWithIndex { current, index ->
    def leftOvers = digits.size() - index
    def nextIndex = leftOvers > compareToIndex ? index + compareToIndex : compareToIndex - leftOvers
    // println "index: $index, nextIndex: $nextIndex, currentSum: $sum"
    sum += (current == digits.get(nextIndex) ? current : 0)
  }
  return sum
}

def input = new File('input.txt').text.trim()
println captcha(input, (input.length() / 2) as int)
