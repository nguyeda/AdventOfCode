package day03

import java.io.File
import java.util.*
import kotlin.test.assertEquals

data class Claim(val id: Int, val x: Int, val y: Int, val w: Int, val h: Int) {

  val rangeX = x..(x + w - 1)
  val rangeY = y..(y + h - 1)

  companion object {
    val claimRegex = "#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)".toRegex()

    fun valueOf(string: String): Claim {
      val m = claimRegex.find(string)
      return Claim(
        m!!.groups[1]!!.value.toInt(),
        m.groups[2]!!.value.toInt(),
        m.groups[3]!!.value.toInt(),
        m.groups[4]!!.value.toInt(),
        m.groups[5]!!.value.toInt()
      )
    }
  }
}

fun main(vararg args: String) {

  fun List<String>.solve(): Any {
    return this
      .map { Claim.valueOf(it) }
      .map { claim -> claim.rangeX.map { rx -> claim.rangeY.map { ry -> rx to ry }}.flatten() }
      .flatten()
      .groupingBy { it }
      .eachCount()
      .count { it.value > 1 }
  }

  assertEquals(4, listOf("#1 @ 1,3: 4x4","#2 @ 3,1: 4x4","#3 @ 5,5: 2x2").solve())
  assertEquals(7, listOf("#1 @ 2,1: 4x3", "#2 @ 1,2: 3x3", "#3 @ 3,3: 4x3", "#4 @ 8,8: 4x3").solve())

  val start = Date()
  val result = File("input.txt").readLines().solve()
  val time = Date().time - start.time

  println("----")
  println("result: $result")
  println("time: $time")
}
