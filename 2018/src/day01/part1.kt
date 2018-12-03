package day01

import java.io.File
import kotlin.test.assertEquals

fun main(vararg args: String) {
  fun List<Int>.solve() = this.sum()

  assertEquals(3, listOf(+1, -2, +3, +1).solve())
  assertEquals(3, listOf(+1, +1, +1).solve())
  assertEquals(0, listOf(+1, +1, -2).solve())
  assertEquals(-6, listOf(-1, -2, -3).solve())

  val result = File("input.txt")
    .readLines()
    .map(String::toInt)
    .solve()

  println("----")
  println("result: $result")
}
