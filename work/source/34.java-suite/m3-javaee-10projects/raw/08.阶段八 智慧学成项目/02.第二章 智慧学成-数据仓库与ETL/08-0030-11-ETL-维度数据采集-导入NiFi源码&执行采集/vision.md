# 画面线理解：11-ETL-维度数据采集-导入NiFi源码&执行采集

- 阶段：08.阶段八 智慧学成项目
- 章节：02.第二章 智慧学成-数据仓库与ETL
- 源文件：08.阶段八 智慧学成项目\02.第二章 智慧学成-数据仓库与ETL\11-ETL-维度数据采集-导入NiFi源码&执行采集_【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:32, 00:58, 01:19, 01:47, 02:17, 02:52, 04:14, 05:23, 06:24, 07:05, 07:47, 08:27, 09:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:45:09

1) 这一组画面整体在讲如何在 NiFi 中导入模板、配置 Hive 和 MySQL 连接器，并通过 ExecuteScript 处理器生成时间维度数据并写入 Hive。

2) 按时间顺序列出每张画面的要点：
画面1：在 Typora 中查看 NiFi 调度源码目录结构，提示需要配置 MySQL、HDFS、Hive。
画面2：在 NiFi 界面中右键空白区域，弹出“Upload Template”对话框。
画面3：点击“Upload Template”后弹出“Add Process Group”对话框，用于创建新的处理组。
画面4：NiFi 流程图界面，显示了“Query/database”、“ConvertAvroToJSON”、“JsonToHiveProcessor”等处理器，以及“时间-维度”处理组。
画面5：配置“Controller Service”中的“Hive Connection Pool”，显示其类型为 HiveConnectionPool 1.9.2。
画面6：配置“Controller Service”中的“Database Connection URL”和“Database Driver Class Name”，分别为 jdbc:mysql://xc-online:3306/... 和 com.mysql.cj.jdbc.Driver。
画面7：在 Typora 中查看 Python 脚本，用于计算闰年和生成时间维度数据。
画面8：配置“ExecuteScript”处理器，设置其“Scheduling”为“Enabled”，并设置“Penalty Duration”为“30 sec”。
画面9：在 Hue 中查看“time_dim”表的数据，显示了时间维度信息。
画面10：NiFi 流程图界面，显示了“Query/database”、“ConvertAvroToJSON”、“JsonToHiveProcessor”等处理器，以及“时间-维度”处理组。
画面11：在 Hue 中查看“course_dim”表的数据，显示了课程维度信息。
画面12：在 Typora 中查看“3.2.6.1 注意事项”，提示如果维度数据出现乱码，需按步骤解决。
画面13：在 Navicat Premium 中查看“xc_course”数据库中的“course_base”表数据，显示了课程信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面7 代码：
```python
import java.io
from org.apache.commons.io import Tutils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.script import Import ExecutScript

def isLeapYear(years):
    if (years % 4 == 0 and years % 100 != 0) or (years % 400 == 0):
        days_sum = 366
    else:
        days_sum = 365
    return days_sum

class PyStreamCallback(StreamCallback):
    def __init__(self):
        pass
    def process(self, inputStream, outputStream):
        years = int('2018')
        data = []
        start_date = 'Ms-1' % years
        a = 0
        days_sum = isLeapYear(int(years))
        while a < days_sum:
            for num in range(0, 24):
                time_dim_id = arrow.get(start_date).shift(days=a).format("YYYY-MM-DD")
                obj = []
                obj['line_dim_id'] = line.dim.id
                a += 1
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4、10：NiFi 流程图，显示“Query/database”处理器指向“ConvertAvroToJSON”处理器，后者指向“JsonToHiveProcessor”处理器。
画面9、11：Hue 中的表格数据，显示了“time_dim”和“course_dim”表的字段和数据。
画面12：Typora 中的“3.2.6.1 注意事项”，提示如果维度数据出现乱码，需按步骤解决。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。
