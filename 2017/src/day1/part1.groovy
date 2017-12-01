package day1

static int captcha(String input) {
  int inputLength = input.length()
  input.chars.collect()
    .indices
    .findAll { input[it] == input[(it + 1) % inputLength]}
    .sum { int it -> input[it] as int } as int
}

def input = new File('input.txt').text.trim()
println captcha(input)
