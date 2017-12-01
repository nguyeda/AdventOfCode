package day1

static int captcha(String input) {
  int delta = input.length() / 2
  int inputLength = input.length()

  input.chars.collect()
    .indices
    .findAll { input[it] == input[(it + delta) % inputLength]}
    .sum { int it -> Integer.valueOf(input[it]) } as int
}

def input = new File('input.txt').text.trim()
println captcha(input)

