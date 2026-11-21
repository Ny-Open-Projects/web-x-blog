# 19即时查询-统计分析-NiFi生产数据-测试&代码测试

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\19即时查询-统计分析-NiFi生产数据-测试&代码测试_【海量资源尽在 666java.com】.mp4
- 时长 7分36秒（音频 456s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,前边呢,咱们已经在NiFi上配置了咱们生产数据的这个NiFi调度,接下来呢,就是使用这个生产数据的一个处理器组进行数据的生成,数据生成完成之后呢,咱们在代码中进行这个测试,因为咱们不周一和不周二的代码已经编写完成,但是呢,数据之前是不完整的,这两个代码的都需要重新
[00:29] 测试这里呢在开始之前呢怎么还要做一件事就是把原来这个垃圾数据给删除掉首先呢是ES上的这里呢点击动作然后点击删除它会让你输入这个删除进行一个确认然后你输入就行这个时候呢已经把ES上的数据给删了接下来呢是HBaseHBase呢这个地方我已经连接到了HBase的sale在这个地方接下来呢
[00:59] 首先是把这个表给禁用禁用完成之后呢再删除好禁用成功接下来呢是删除咱们来查看一下是否删除成功这个时候呢你就可以看到只有一个demo了这是咱们存储这一块的一个数据清理接下来呢还有咱们原始数据的一个清理首先呢是咱们原来采集的这个数据咱们切到hdfs上的文件路径
[01:36] 这里呢咱们原来数据的采集是在课程这个目录下是这个online source还有呢咱们生成的这个数据不是生成啊咱们那个中间表这个数据是在这个dwm这两个呢直接删除即可这两个目录直接删除即可因为咱们采集还有咱们数据清洗这个目录还会重新创建接下来呢就是咱们对dwm的这个上面的这个数据的一个清理现在你可以查看
[02:05] 这个数据已经是没有了但是他这个分区还在咱们呢把这个分区给删了这个分区呢其实你不删也是行的但是呢为了这个数据的一个干净咱们就把它给删了他这个删除的时候你可以看他的日志他这里呢只删除成功了一个这个分区来说还比较多咱们呢是我之前测试的时候留下了一个分区咱们呢就先不管他
[02:36] 这个分区其实不删也行咱们来把它给NiFi调度这个生产数据给跑起来这里呢可以看到数据已经堵到这了好到这了现在还没有放到HDFS上再次刷新OK已经可以看到放到HDFS上了咱们大概生产一兆左右的数据就可以进行测试了好已经超过一兆了把处理器组给停下来了这个时候呢咱们先来跑步周一
[03:10] 但是步骤一开始之前呢咱们需要一个注意事项这个地方呢关于时间处理的时候咱们原来是用的是啥呀GS买点采集的时候他用的是毫秒值但是现在的话咱们使用脚本生产数据的时候他这个地方呢是时间戳他得到的是时间戳所以说呢咱们是有需要把它给这个时间戳这个除以
[03:39] 以前这个可以去掉因为它本身已经是实验出来就不需要再处理了咱们来运行那个测试这个测试完成之后呢咱们再来跑第二步的一个测试这个呢咱们来HUE来刷新这个数据就行了哎呀这个刚才是点了之后它可能还是不对咱们来到这重新刷新还没有数据说明程序呢还没有跑完咱们来等待这个程序运行完成好程序呢已经运行完成咱们来刷新
[04:23] 走好已经有数据这个数据呢是完整的咱们来运行步骤的代码走起这里呢等待程序运行完成这个地方呢代码中我已经做了一个处理也是有一个注意事项因为呢咱们前期测试的时候是根据时间进行测试的但是呢这个地方我为什么把它给注视掉呢主要的一个原因是咱们这个地方生产数据生产数据这个脚本呢它是生产了
[05:04] 1到30天的数据1到30天的数据呢都放到了咱们这个HDFS上的这个目录内放到这个目录内咱们数据处理的时候就代码上没有对它进行一个逻辑过滤所以说呢这个里边是有30天的数据这个地方呢我就把这个时间过滤给去掉让它有更多的数据咱们后边展示的时候这个效果才会更好所以说就把这个时间过滤给去掉了
[05:34] 这里呢就是处理所有的数据也就是说在这个里边在这个DWM里边现在是30天的数据这里呢就对中年表这30天的数据都做了一个处理咱们来看这里运行完成没已经运行完成已经运行完成的情况下呢咱们来ES header里边查看ES上的数据来浏览这里面你可以看到是完整的而且呢咱们工具没有报错说明
[06:03] 这里也是完整的来查看一下它已经有了咱们呢scan一下就是查看这个表的数据这个多了一个逗号它没有正常的运行好scan没有错这里呢很多数据你可以看到已经在刷新了因为咱们现在字段的字段是完整的你可以看到cosname各种的name都有了但是呢
[06:38] 中文的情况下它是转译的英文这里是采用了拼音它是可以展示的好咱们切回问答这里呢使用NiFi生产数据呢咱们已经测试完成生成之后呢代码这个测试呢也已经测试OK咱们呢也通过这个测试来验证咱们这个代码的一个完整性这里呢测试的过程中有两个注意事项代码一呢
[07:05] 这里边就是这个时间圈的问题咱们这个地方已经不需要再除以1000了步骤二呢的注意事项咱们就是把这个日期过滤给去调调了就是处理了所有的数据通过本节的学习呢你需要能够掌握使用NiFi生产数据然后呢将生产后的数据进行两步这个统计分析步骤一呢就是关联维度统计分析步骤二呢就是保存到HBase所有呢Lassoc Search好 视频呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 NiFi 生产模拟用户学习数据并将其写入 HDFS，同时展示数据在 Hive 和 Spark 中的处理与查询过程。

2) 按时间顺序列出每张画面的要点：
画面1：展示 NiFi 文档中“3.3.1 生产数据脚本”部分，其中包含 Python 代码用于生成模拟数据。
画面2：展示 Elasticsearch 界面，显示索引“demo”包含 3 条文档，状态为黄色（5 of 10）。
画面3：展示 Hue 的文件浏览器，路径为 /user/hue/external/data_course，列出多个课程相关的表。
画面4：展示 Hue 的 Table Browser，查看表 learning_course_online_dwm 的列和分区信息。
画面5：展示 IntelliJ IDEA 中的 Scala 代码，包含 Spark SQL 查询语句和配置。
画面6：展示 IntelliJ IDEA 的终端，显示 Spark 应用提交成功。
画面7：展示 IntelliJ IDEA 的终端，显示 Spark 应用运行日志和结果。
画面8：展示 IntelliJ IDEA 的终端，显示 Spark 应用提交成功。
画面9：展示 Typora 中的 Python 代码，用于 NiFi 流程中生成模拟用户学习数据。
画面10：展示 IntelliJ IDEA 的终端，显示 Spark SQL 查询执行日志。
画面11：展示 IntelliJ IDEA 的终端，显示 Spark SQL 查询执行日志。
画面12：展示终端中执行 Hive 命令，创建、删除和查看表。
画面13：展示 NiFi 界面，显示数据采集流程的“测试”步骤。
画面14：展示 HDFS 的 Browse Directory 页面，显示学习数据目录。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1：
```python
import random
import time, datetime
import java.io
from org.apache.commons import TOOLSFile
from org.apache.Hadoop.io import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
from org.apache.nifi.nifi.processor.script import Executescript

BROWSER = ['firefox', 'chrome', '360', 'rz', 'sogou', 'Reboot', 'it', 'Spark', 'QQ', 'UC', 'Dnurl', 'Liebao', 'AR']

def datetamp():
    now_info = datetime.datetime.now()
    delta = datetime.timedelta(random.randint(1, 30))
    time_info = now_info - delta
    time_info = time_info.strftime("%Y-%m-%d %H:%M:%S")
    return time_info
```

画面5：
```scala
val hiveToLzName = "data_course.learning_course_online_dwm"
val data_info = "2019-12-12"
val learnDS = Spark.sql("select * from ${hiveToLzName} where date_info = '${data_info}'").asLearningCourseOnlineDwm
val learnDS = learnDS.map(x => {
  learningCourseOnlineIndex(
    obj.learning_course_online_id,
    obj.video_name,
    obj.user_name,
    obj.course_name,
    obj.video_id,
    obj.user_id
  )
})
```

画面9：
```python
class PyStreamCallback(StreamCallback):
    def __init__(self):
        pass

    def process(self, inputStream, outputStream):
        uc = str(IOUtils.toString(inputStream, StandardCharsets.UTF_8).split(","))
        sessions = str(''.join(str(random.randint(0, 1000000)) for i in range(4)))
        user_id = uc[0]
        course_id = uc[2]
        session_id = str(random.randint(0, 1000000))
        user_agent = str(BROWSER[random.randint(0, len(BROWSER) - 1)])
        visit_time = str(datetamp())
        outputstream.write(bytearray(user_id + '\t' + course_id + '\t' + session_id + '\t' + user_agent + '\t' + visit_time + '\n', encoding='utf-8'))
```

画面10：
```scala
val learnDS = Spark.sql("select * from ${hiveToLzName} where date_info = '${data_info}'").asLearningCourseOnlineDwm
val learnDS = learnDS.map(x => {
  learningCourseOnlineIndex(
    obj.learning_course_online_id,
    obj.video_name,
    obj.user_name,
    obj.course_name,
    obj.video_id,
    obj.user_id
  )
})
```

画面12：
```bash
Hive(main):001: List
TABLE
-> "learningonlinedetail"  "demo"
0 rows) in 2.9490 seconds

Hive(main):003: drop "learningonlinedetail"
0 rows) in 1.2608 seconds

Hive(main):004: List
TABLE
-> "demo"
0 rows) in 0.0050 seconds

Hive(main):005: List
TABLE
-> "learningonlinedetail"  "demo"
0 rows) in 0.0060 seconds
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：PPT 标题为“3.3 NiFi生产数据”，子标题“3.3.1 生产数据脚本”。
画面13：PPT 标题为“3.3.3 测试”，子标题“采集步骤如下图所示”，图中显示 NiFi 流程图，包含“读取”、“处理”、“写入”等步骤。
画面14：HDFS 的 Browse Directory 页面，表格包含列：Permission、Owner、Group、Last Modified、Replication、Block Size、Name。

5) 无。

