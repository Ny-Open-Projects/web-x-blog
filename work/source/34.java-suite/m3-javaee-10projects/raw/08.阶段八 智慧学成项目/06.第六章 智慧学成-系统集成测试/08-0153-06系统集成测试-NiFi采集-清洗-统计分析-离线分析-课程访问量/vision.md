# 画面线理解：06系统集成测试-NiFi采集-清洗-统计分析-离线分析-课程访问量

- 阶段：08.阶段八 智慧学成项目
- 章节：06.第六章 智慧学成-系统集成测试
- 源文件：08.阶段八 智慧学成项目\06.第六章 智慧学成-系统集成测试\06系统集成测试-NiFi采集-清洗-统计分析-离线分析-课程访问量_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:39, 00:56, 01:59, 02:32, 02:46, 03:07, 03:27, 03:49, 04:07, 04:19, 04:29, 04:39, 04:46, 05:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 00:12:05

1) 这一组画面整体在讲什么（一句话）：
演示如何在 NiFi 中配置数据流，从 Hive 表读取数据，经过处理后写入 MySQL 数据库。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 NiFi 主界面，包含多个处理器的运行状态面板，如“demo”、“离线分析”、“实时分析”等，显示数据处理的吞吐量和任务时间。
画面 2: 展示 NiFi 流程图，包含三个处理器：1. 数据源-维度表流量统计；2. 数据维度统计-维度表流量；3. 同步到业务库维度表-Hive-To-Mysql。其中，处理器 2 的“From Out”连接到处理器 3 的“To Input”。
画面 3: 展示处理器详情窗口，选中“PROPERTIES”标签页，显示“Script Engine”为 python，“Script Body”包含 Python 代码，用于生成时间戳。
画面 4: 展示处理器详情窗口，选中“PROPERTIES”标签页，显示“Command Arguments”为“$Bin(ToNumber($minval))$format(yyyy-MM-dd HH:mm:ss)”，“Command Path”为“/opt/run/script/course_visit.sh”，“Working Directory”为“/opt/run/script”，“Max Attribute Length”为“256”。
画面 5: 展示 NiFi 流程图，包含“input”、“SelectHiveQL”、“EvaluateJsonPath”和“PutSQL”处理器。其中，“SelectHiveQL”连接到“EvaluateJsonPath”，“EvaluateJsonPath”连接到“PutSQL”。
画面 6: 展示 NiFi 流程图，与画面 5 类似，但“SelectHiveQL”和“EvaluateJsonPath”处理器的属性面板显示“Tasks/Time”为“0/00:00:00.000”。
画面 7: 展示 MySQL 数据库管理工具界面，显示“course_visit”表的结构，包含字段“date_info”和“count”。
画面 8: 展示 NiFi 流程图，与画面 2 类似，但处理器 2 的“Read/Write”显示“22.29 MB / 422.85 MB”，“Out”显示“1 → 0 (0 bytes)”。
画面 9: 展示 NiFi 流程图，包含“input”、“SelectHiveQL”、“EvaluateJsonPath”和“PutSQL”处理器。其中，“SelectHiveQL”连接到“EvaluateJsonPath”，“EvaluateJsonPath”连接到“PutSQL”。处理器“SelectHiveQL”的“Tasks/Time”为“1/00:00:00.945”，“EvaluateJsonPath”的“Tasks/Time”为“0/00:00:00.000”，“PutSQL”的“Tasks/Time”为“0/00:00:00.114”。
画面 10: 展示 Hue 文件浏览器界面，显示“/user/hive/external/data_course”目录下的文件列表，包括“course_buy_biz”、“course_buy_dim”、“course_hot_month_biz”等。
画面 11: 展示 Hue 文件浏览器界面，显示“/user/hive/external/data_course/course_visit_source”目录下的文件列表，包括“2019-12-10”、“2019-12-11”等日期文件夹。
画面 12: 展示 Hue 文件浏览器界面，显示“/user/hive/external/data_course/course_visit_source/2019-12-16”目录下的文件列表，包含一个文件“909226c-8c3a-42a3-81a2-8ac25f6c0381”，大小为 22.0 MB。
画面 13: 展示 Hue 文件浏览器界面，显示“/user/hive/external/data_course/course_visit_source/2019-12-16”目录下的文件列表，但页面加载中，显示加载图标。
画面 14: 展示 NiFi 主界面，显示空白的流程图，无任何处理器。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3 中的 Script Body 代码：
```python
import random
import uuid
import time, datetime
from org.apache.commons import IOUtils
from java.io.ByteArrayInputStream import ByteArrayInputStream
from org.apache.nifi.processor import StandardCharsets
from org.apache.nifi.processor.script import StreamCallback
from org.apache.nifi.processors.script import ExecuteScript

BROWSER = ['Firefox', 'Chrome', '360', '23', 'sougou', 'Robot', 'IE', 'spark', 'QQ', 'UC', 'Druc']

def datetimestamp():
    now_info = datetime.datetime.now()
    date = datetime.datetime.fromtimestamp(int(time.time()))
    time_info = now_info - delta
    for time_info.strftime("%Y-%m-%d %H:%M:%S")
    times = int(time.mktime(time.strptime(for_time, "%Y-%m-%d %H:%M:%S")))
    return times
```

画面 4 中的 Command Arguments：
```
$Bin(ToNumber($minval))$format(yyyy-MM-dd HH:mm:ss)
```

画面 4 中的 Command Path：
```
/opt/run/script/course_visit.sh
```

画面 4 中的 Working Directory：
```
/opt/run/script
```

画面 4 中的 Max Attribute Length：
```
256
```

画面 7 中的 SQL：
```
SELECT * FROM `business`.`course_visit` LIMIT 0, 1000
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2 中的流程图结构：
- 处理器 1（数据源-维度表流量统计）的“Out”连接到处理器 2（数据维度统计-维度表流量）的“To Input”。
- 处理器 2（数据维度统计-维度表流量）的“Out”连接到处理器 3（同步到业务库维度表-Hive-To-Mysql）的“To Input”。

画面 9 中的流程图结构：
- 处理器“SelectHiveQL”连接到“EvaluateJsonPath”。
- “EvaluateJsonPath”连接到“PutSQL”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
