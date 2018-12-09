package day03

import java.io.File
import java.util.*
import kotlin.test.assertEquals

data class Claim2(val id: Int, val x: Int, val y: Int, val w: Int, val h: Int) {

  val rangeX = x..(x + w - 1)
  val rangeY = y..(y + h - 1)

  val points = this.rangeX.map { rx -> this.rangeY.map { ry -> rx to ry } }.flatten()

  companion object {
    val claimRegex = "#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)".toRegex()

    fun valueOf(string: String): Claim2 {
      val m = claimRegex.find(string)
      return Claim2(
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

  fun List<String>.solve(): Int? {
    val claims = this.map { Claim2.valueOf(it) }
    val uniques = claims.map { it.points }
      .flatten()
      .groupingBy { it }
      .eachCount()
      .filterValues { it == 1 }

    return claims.firstOrNull { uniques.keys.containsAll(it.points) }?.id
  }

  assertEquals(3, listOf("#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2").solve())

  val start = Date()
  val result = File("input.txt").readLines().solve()
  val time = Date().time - start.time

  println("----")
  println("result: $result")
  println("time: $time")
}
