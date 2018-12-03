package day01

import java.io.File
import java.util.*
import kotlin.test.assertEquals

fun main(vararg args: String) {
  // Alternate solution using a sequence (from: https://todd.ginsberg.com/post/advent-of-code/2018/day1/)
  // more functional but seems a little bit slower than my previous implementation (45-50ms vs 55-65ms)
  fun <T> List<T>.toInfiniteSequence(): Sequence<T> = sequence {
    if (this@toInfiniteSequence.isEmpty()) {
      return@sequence
    }
    while (true) {
      yieldAll(this@toInfiniteSequence)
    }
  }

  fun List<Int>.solve(): Int {
    val frequencies = mutableSetOf(0)
    var current = 0

    return this.toInfiniteSequence()
      .map {
        current += it
        current
      }
      .first { !frequencies.add(it) }
  }

  assertEquals(2, listOf(+1, -2, +3, +1).solve())
  assertEquals(0, listOf(+1, -1).solve())
  assertEquals(10, listOf(+3, +3, +4, -2, -4).solve())
  assertEquals(5, listOf(-6, +3, +8, +5, -6).solve())
  assertEquals(14, listOf(+7, +7, -2, -7, -4).solve())

  val start = Date()
  val result = File("input.txt")
    .readLines()
    .map(String::toInt)
    .solve()

  val end = Date()
  println("----")
  println("result: $result")
  println("time: ${end.time - start.time}")
}
