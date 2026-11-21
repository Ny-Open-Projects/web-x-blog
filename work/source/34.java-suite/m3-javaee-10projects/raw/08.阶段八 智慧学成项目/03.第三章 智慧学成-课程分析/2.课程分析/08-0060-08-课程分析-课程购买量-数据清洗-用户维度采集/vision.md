# 画面线理解：08-课程分析-课程购买量-数据清洗-用户维度采集

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\08-课程分析-课程购买量-数据清洗-用户维度采集_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:39, 00:43, 01:13, 01:17, 01:23, 01:26, 01:29, 01:37, 01:45, 01:50, 02:14, 02:24, 02:29, 02:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:02:58

1) 这一组画面整体在讲什么（一句话）：
演示如何在Nifi中配置并运行一个从Hive读取数据、清洗并写入维度表的ETL流程，并展示清洗后数据在Hue中的结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示IDE中“2.4.1.3 清洗代码”章节，代码从Hive读取MySQL采集的数据，导入包包括cn.itcast.xc.analysys.buy、cn.itcast.xc.entity等。
画面2：展示IDE中“2.4.1.4 测试”章节，显示了在IDE中运行程序后的控制台输出结果，包含多行数据记录。
画面3：在Nifi界面中，弹出“Upload Template”对话框，提示选择模板。
画面4：在“Upload Template”对话框中，用户从本地文件夹选择名为“用户维度表.xml”的文件并点击“打开”。
画面5：在Nifi界面中，弹出“Add Template”对话框，用户选择“用户维度表”模板并点击“ADD”。
画面6：在Nifi界面中，显示了三个处理组的监控面板，分别显示“用户-维度”、“课程-维度”和“用户-维度”的状态。
画面7：在Nifi界面中，弹出“用户 - 维度 Configuration”窗口，显示“Process Group Name”为“用户-维度”。
画面8：在“用户 - 维度 Configuration”窗口的“CONTROLLER SERVICES”标签页中，显示了三个服务：DistributedMapCacheServer、hive连接池、DBCP连接池。
画面9：在“CONTROLLER SERVICES”标签页中，DBCP连接池的状态从“Disabled”变为“Enabled”。
画面10：在“CONTROLLER SERVICES”标签页中，DBCP连接池的状态从“Enabled”变为“Disabled”。
画面11：在Hue的Query界面中，显示了执行的SQL语句和结果，结果为“1 18642”。
画面12：在Hue的Table Browser界面中，显示了“data_dimen > user_dim”表的结构和部分数据。
画面13：在Hue的Table Browser界面中，显示了“data_dimen > user_dim”表的更多数据，包括用户ID、用户名、用户类型等字段。
画面14：在Hue的Table Browser界面中，显示了“data_dimen > user_dim”表的更多数据，包括用户ID、用户名、用户类型等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
package cn.itcast.xc.analysys.buy
import cn.itcast.xc.common.EtlEnvironment
import cn.itcast.xc.entity.{AreaDimen, CourseBuyDimen, CourseOrdersSource, UserDimen}
import cn.itcast.xc.utils.IpUtils
```
画面2：
```java
spark.close()
}
```
画面4：
```xml
用户维度表.xml
```
画面11：
```sql
INFO : Completed executing command(query2s-root...): Time taken: 14.295 seconds
```
画面12：
```sql
user_dim.user_dim_id user_dim_username user_dim_name user_dim_userpic user_dim_utype user_dim
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“2.4.1.3 清洗代码”，内容为“从Hive读取MySQL采集的数据，根据清洗分析编写代码如下”。
画面2：PPT标题为“2.4.1.4 测试”，内容为“IDEA中直接运行程序，控制台运行结果”。
画面6：Nifi界面中，三个处理组的监控面板分别显示“用户-维度”、“课程-维度”和“用户-维度”的状态。
画面7：Nifi界面中，弹出“用户 - 维度 Configuration”窗口，显示“Process Group Name”为“用户-维度”。
画面8：在“CONTROLLER SERVICES”标签页中，显示了三个服务：DistributedMapCacheServer、hive连接池、DBCP连接池。
画面9：在“CONTROLLER SERVICES”标签页中，DBCP连接池的状态从“Disabled”变为“Enabled”。
画面10：在“CONTROLLER SERVICES”标签页中，DBCP连接池的状态从“Enabled”变为“Disabled”。
画面11：在Hue的Query界面中，显示了执行的SQL语句和结果，结果为“1 18642”。
画面12：在Hue的Table Browser界面中，显示了“data_dimen > user_dim”表的结构和部分数据。
画面13：在Hue的Table Browser界面中，显示了“data_dimen > user_dim”表的更多数据，包括用户ID、用户名、用户类型等字段。
画面14：在Hue的Table Browser界面中，显示了“data_dimen > user_dim”表的更多数据，包括用户ID、用户名、用户类型等字段。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
