# 画面线理解：19即时查询-统计分析-NiFi生产数据-测试&代码测试

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\19即时查询-统计分析-NiFi生产数据-测试&代码测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:46, 01:39, 02:26, 03:11, 03:53, 04:18, 04:41, 05:00, 05:31, 05:48, 06:06, 06:53, 07:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 00:06:14

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
from org.apache.hadoop.io import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
from org.apache.nifi.nifi.processor.script import Executescript

BROWSER = ['firefox', 'chrome', '360', 'rz', 'sogou', 'Reboot', 'it', 'spark', 'QQ', 'UC', 'Dnurl', 'Liebao', 'AR']

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
val learnDS = spark.sql("select * from ${hiveToLzName} where date_info = '${data_info}'").asLearningCourseOnlineDwm
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
val learnDS = spark.sql("select * from ${hiveToLzName} where date_info = '${data_info}'").asLearningCourseOnlineDwm
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
hive(main):001: List
TABLE
-> "learningonlinedetail"  "demo"
0 rows) in 2.9490 seconds

hive(main):003: drop "learningonlinedetail"
0 rows) in 1.2608 seconds

hive(main):004: List
TABLE
-> "demo"
0 rows) in 0.0050 seconds

hive(main):005: List
TABLE
-> "learningonlinedetail"  "demo"
0 rows) in 0.0060 seconds
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：PPT 标题为“3.3 NiFi生产数据”，子标题“3.3.1 生产数据脚本”。
画面13：PPT 标题为“3.3.3 测试”，子标题“采集步骤如下图所示”，图中显示 NiFi 流程图，包含“读取”、“处理”、“写入”等步骤。
画面14：HDFS 的 Browse Directory 页面，表格包含列：Permission、Owner、Group、Last Modified、Replication、Block Size、Name。

5) 无。
