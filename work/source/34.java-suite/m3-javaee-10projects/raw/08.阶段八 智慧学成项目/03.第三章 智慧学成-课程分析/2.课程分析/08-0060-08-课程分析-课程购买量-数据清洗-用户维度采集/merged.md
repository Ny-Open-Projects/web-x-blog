# 08-课程分析-课程购买量-数据清洗-用户维度采集

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\08-课程分析-课程购买量-数据清洗-用户维度采集_【海量资源尽在 666java.com】.mp4
- 时长 2分45秒（音频 165s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前边呢,咱们分析了DW层的数据结构,以及咱们需要清晰哪些字段来补全数据。
[00:07] 接下来呢,就是进行一个代码编写阶段。
[00:11] 但是在代码编写开始之前呢,咱们还有一个工作要做,就是用户相关的数据需要获取。
[00:20] 这里用户相关的数据呢,就指的是用户维度,因为咱们这个地方呢,需要通过用户ID来关联。
[00:29] 到用户维度,然后获取用户的IP,最终获取到区域ID。
[00:36] 咱们来看维度的一个采集。
[00:39] 这里呢,维度的采集,咱们在资料中已经准备好了相关的代码。
[00:46] 咱们之前在维度采集的时候呢,已经做了时间维度和那个课程维度的一个采集。
[00:56] 配置呢还是一样的咱们呢这里直接把源码给导入进行一个相关的配置接着呢配置完成之后就进行相当的一个采集咱们来切换Netfine这里呢咱们来进入维度这个处理器组咱们来导入用户维度的一个采集导入之后呢进行上传上传之后咱们以添加模板的方式将它给添加进来添加进来之后呢
[01:25] 咱们进行相应的配置配置方式还是一样的这里呢要把hi5给启用了hi5启用完成之后呢把买sok的密码给配置上买sok的密码呢是123456配置完成之后呢也是把这个给启用启用完成之后咱们的配置就完成了这里来进入这个工作组处理器组你就可以看到这些呢已经没有感叹了呢咱们直接执行即可
[02:01] 这里呢数据已经可以看到已经进行一个采集采集操作只要这个地方有读取数据就说明咱们这个地方已经采集完成采集完成之后呢把它给停下来咱们来HOE来确认一下咱们呢来切到维度这个库咱们刚才采集的是用户维度来查看一下数据这里呢查看一下数据这个地方呢用户维度的数据呢已经采集过来大概是这么多
[02:31] 数据呢就已经有了数据数据有了之后呢咱们再切了温档这个时候呢咱们维度采集就已经完成了好这视频呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面8：在“用户 - 维度 Configuration”窗口的“CONTROLLER SERVICES”标签页中，显示了三个服务：DistributedMapCacheServer、Hive连接池、DBCP连接池。
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
Spark.close()
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
画面8：在“CONTROLLER SERVICES”标签页中，显示了三个服务：DistributedMapCacheServer、Hive连接池、DBCP连接池。
画面9：在“CONTROLLER SERVICES”标签页中，DBCP连接池的状态从“Disabled”变为“Enabled”。
画面10：在“CONTROLLER SERVICES”标签页中，DBCP连接池的状态从“Enabled”变为“Disabled”。
画面11：在Hue的Query界面中，显示了执行的SQL语句和结果，结果为“1 18642”。
画面12：在Hue的Table Browser界面中，显示了“data_dimen > user_dim”表的结构和部分数据。
画面13：在Hue的Table Browser界面中，显示了“data_dimen > user_dim”表的更多数据，包括用户ID、用户名、用户类型等字段。
画面14：在Hue的Table Browser界面中，显示了“data_dimen > user_dim”表的更多数据，包括用户ID、用户名、用户类型等字段。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

