package day05

import java.io.File
import java.util.*
import kotlin.test.assertEquals

fun main(vararg args: String) {
  fun String.solve(): Any {
    return this.fold(LinkedList<Char>()) { keep, current ->
        when {
          keep.isEmpty() -> keep.add(current)
          else -> {
            val previous = keep.pollLast()
            val diff = current.toInt() - previous.toInt()
            if (diff != 32 && diff != -32) {
              keep.add(previous)
              keep.add(current)
            }
          }
        }
        keep
      }
      .size
  }

  assertEquals(0, "aA".solve())
  assertEquals(0, "abBA".solve())
  assertEquals(4, "abAB".solve())
  assertEquals(6, "aabAAB".solve())
  assertEquals(10, "dabAcCaCBAcCcaDA".solve())

  val start = Date()
  val result = File("input.txt").readLines().first().solve()
  val time = Date().time - start.time

  println("----")
  println("result: $result")
  println("time: $time")
}
