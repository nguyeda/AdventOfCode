package day04

import java.io.File
import java.util.*
import kotlin.test.assertEquals


fun main(vararg args: String) {
  val dateRegex = "\\[\\d{4}\\-\\d{2}\\-\\d{2} \\d{2}:(\\d{2})\\]"
  val shiftStartRegex: Regex = ".* Guard #(\\d+) begins shift".toRegex()
  val startSleepRegex = "$dateRegex falls asleep".toRegex()
  val wakeUpRegex = "$dateRegex wakes up".toRegex()

  fun List<String>.solve(): Any? {
    return this
      .sorted()
      .run {
        val sleeps = mutableMapOf<Int, List<Int>>()
        var currentSleepStartMinute = 0
        var currentGuard = 0

        fun Regex.findOne(string: String): Int? {
          return this.find(string)?.destructured?.component1()?.toInt()
        }

        this.forEach {
          when {
            it.matches(shiftStartRegex) -> currentGuard = shiftStartRegex.findOne(it)!!
            it.matches(startSleepRegex) -> currentSleepStartMinute = startSleepRegex.findOne(it)!!
            else  -> {
              if (it.matches(wakeUpRegex)) {
                val wakeUpMinute = wakeUpRegex.findOne(it)!! - 1
                sleeps.merge(currentGuard, (currentSleepStartMinute..wakeUpMinute).toList()) { a, b -> a + b }
              }
            }
          }
        }

        sleeps
      }
      .maxBy { it.value.size }!!
      .run {
        val guardId = this.key
        val minute = this.value.groupBy { it }.maxBy { it.value.size }!!.key
        guardId * minute
      }
  }

  val testData = """
  | [1518-11-01 00:00] Guard #10 begins shift
  | [1518-11-01 00:05] falls asleep
  | [1518-11-01 00:25] wakes up
  | [1518-11-01 00:30] falls asleep
  | [1518-11-01 00:55] wakes up
  | [1518-11-01 23:58] Guard #99 begins shift
  | [1518-11-02 00:40] falls asleep
  | [1518-11-02 00:50] wakes up
  | [1518-11-03 00:05] Guard #10 begins shift
  | [1518-11-03 00:24] falls asleep
  | [1518-11-03 00:29] wakes up
  | [1518-11-04 00:02] Guard #99 begins shift
  | [1518-11-04 00:36] falls asleep
  | [1518-11-04 00:46] wakes up
  | [1518-11-05 00:03] Guard #99 begins shift
  | [1518-11-05 00:45] falls asleep
  | [1518-11-05 00:55] wakes up
  """.trimMargin("| ")

  assertEquals(240, testData.lines().solve())

  val start = Date()
  val result = File("input.txt").readLines().solve()
  val time = Date().time - start.time

  println("----")
  println("result: $result")
  println("time: $time")
}
