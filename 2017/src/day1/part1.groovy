package day1

static int captcha(String input) {
  def sum = 0
  List<Integer> digits = input.chars.collect { Integer.parseUnsignedInt(it as String) }
  digits.eachWithIndex { current, index ->
    def next = (index == digits.size() - 1) ? digits.first() : digits.get(index + 1)
    //println "current: $current, next: $next, currentSum: $sum"
    sum += (current == next ? current : 0)
  }
  return sum
}

def input = new File('input.txt').text.trim()
println captcha(input)
