package day02

import java.io.File
import java.util.*
import kotlin.test.assertEquals

fun main(vararg args: String) {
  fun List<String>.solve(): Int {
    return this
      .map { string -> string.groupingBy { it }.eachCount() }
      .map { map ->
        Pair(
          if (map.values.contains(2)) 1 else 0,
          if (map.values.contains(3)) 1 else 0
        )
      }
      .fold(Pair(0, 0)) { acc, pair -> acc.first + pair.first to acc.second + pair.second }
      .run { first * second }
  }

  assertEquals(12, listOf("abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab").solve())

  val start = Date()
  val result = File("input.txt").readLines().solve()
  val time = Date().time - start.time;

  println("----")
  println("result: $result")
  println("time: $time")
}
