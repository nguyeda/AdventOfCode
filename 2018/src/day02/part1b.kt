package day02

import java.io.File
import java.util.*
import kotlin.test.assertEquals

// from https://todd.ginsberg.com/post/advent-of-code/2018/day2/
fun main(vararg args: String) {
  fun List<String>.solve(): Int {
    val r = this
      .map { string -> string.groupingBy { it }.eachCount() }
      .map { counts: Map<Char, Int> -> Pair(counts.any { it.value == 2 }, counts.any { it.value == 3 }) }

    return r.count { it.first } * r.count { it.second }
  }

  assertEquals(12, listOf("abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab").solve())

  val start = Date()
  val result = File("input.txt").readLines().solve()
  val time = Date().time - start.time;

  println("----")
  println("result: $result")
  println("time: $time")
}
