# 画面线理解：12-热门学科排名-统计分析-销售量-周-代码-获取周区间日期

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\12-热门学科排名-统计分析-销售量-周-代码-获取周区间日期_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:15, 00:20, 00:34, 01:52, 02:01, 02:09, 03:25, 03:46, 03:52, 03:55, 04:03, 04:11, 04:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:17:39

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Scala 中使用 SparkSession 初始化并执行一个计算上海周销售数据的程序，包含日期处理、数据读取和打印输出等步骤。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Scala 代码编辑器，文件 `SubjectSalesVolumeByWeekBiz.scala` 中定义了 SparkSession 和 main 函数，注释说明了程序的七个步骤，当前光标在第 7 步“保存结果”。
画面 2: 光标移动到第 2 步“获取上海周的时区信息”，高亮显示该注释行。
画面 3: 光标在第 7 步“保存结果”处，准备进行操作。
画面 4: 光标在第 2 步“获取上海周的时区信息”处，高亮显示该注释行。
画面 5: 光标移动到第 2 步注释行，下方代码中定义了 `val date_info = "2019-11-11"` 和 `val weeks = getWeeksRelativelyInterval(date_info).split(",")`。
画面 6: 光标在 `println(weeks)` 行，下方终端显示程序已成功运行。
画面 7: 终端显示程序运行日志，包括 Spark 各组件的启动和停止信息，最后显示“Process finished with exit code 0”。
画面 8: 光标在 `val current = weeks(0)` 行，下方弹出 Scala 类型推断提示，显示 `current` 的类型为 `Any`。
画面 9: 光标在 `val current = weeks(0)` 行，下方弹出 Scala 类型推断提示，显示 `current` 的类型为 `Any`。
画面 10: 右键菜单弹出，显示“Run 'SubjectSalesVolumeByWeekBiz'”等选项。
画面 11: 光标在 `val date_info = "2019-11-11"` 行，下方终端显示程序已成功运行。
画面 12: 光标在 `val date_info = "2019-11-11"` 行，下方终端显示程序已成功运行。
画面 13: 光标在 `val date_info = "2019-11-11"` 行，下方终端显示程序已成功运行。
画面 14: 光标在 `val date_info = "2019-11-11"` 行，下方终端显示程序已成功运行。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```scala
object SubjectSalesVolumeByWeekBiz {
  // Spark session
  val spark: SparkSession = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
  def main(args: Array[String]): Unit = {
    // 1. 获取上海周的时区信息，例：上海 1 个周
    // 2. 获取上海周的时区信息，例：上海 1 个周
    // 3. 获取上海周的时区信息，例：上海 1 个周
    // 4. 获取上海周的时区信息，例：上海 1 个周
    // 5. 计算涨幅
    // 6. 根据维度以及维度相关数据
    // 7. 保存结果
    spark.close()
  }
}
```

画面 5:
```scala
import cn.itcast.xc.common.ETLEnvironment
import org.apache.spark.sql.SparkSession
import cn.itcast.xc.utils.DateUtils.getWeeksRelativelyInterval

object SubjectSalesVolumeByWeekBiz {
  // Spark session
  val spark: SparkSession = ETLEnvironment.getSparkSession(this.getClass.getSimpleName)
  def main(args: Array[String]): Unit = {
    // 1. 获取上海周的时区信息，例：上海 1 个周
    // 2. 获取上海周的时区信息，例：上海 1 个周
    val date_info = "2019-11-11"
    val weeks = getWeeksRelativelyInterval(date_info).split(",")
    // 3. 获取上海周的时区信息，例：上海 1 个周
    // 4. 获取上海周的时区信息，例：上海 1 个周
    // 5. 计算涨幅
    // 6. 根据维度以及维度相关数据
    // 7. 保存结果
  }
}
```

画面 6:
```scala
val date_info = "2019-11-11"
val weeks = getWeeksRelativelyInterval(date_info).split(",")
println(weeks)
```

画面 8:
```scala
val current = weeks(0)
```

画面 11:
```scala
val date_info = "2019-11-11"
val weeks = getWeeksRelativelyInterval(date_info).split(",")
val current = weeks(0)
val last = weeks(1)
println(current)
println(last)
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
