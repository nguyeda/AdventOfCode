package day05

import java.io.File
import java.util.*
import kotlin.test.assertEquals

fun main(vararg args: String) {
  fun String.solve(ignore: Char): Int {
    return this.fold(LinkedList<Char>()) { keep, current ->
      when {
        current.toLowerCase() == ignore -> {
        }

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
    }.size
  }

  assertEquals(6, "dabAcCaCBAcCcaDA".solve('a'))
  assertEquals(8, "dabAcCaCBAcCcaDA".solve('b'))
  assertEquals(4, "dabAcCaCBAcCcaDA".solve('c'))
  assertEquals(6, "dabAcCaCBAcCcaDA".solve('d'))

  val start = Date()
  val text = File("input.txt").readLines().first()
  val result = ('a'..'z').map { text.solve(it) }.min()
  val time = Date().time - start.time

  println("----")
  println("result: $result")
  println("time: $time")
}
