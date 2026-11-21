# 画面线理解：18即时查询-统计分析-NiFi生产数据-配置

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\18即时查询-统计分析-NiFi生产数据-配置_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:16, 01:38, 01:47, 01:56, 02:01, 02:16, 02:22, 02:25, 02:30, 02:42, 02:53, 03:04, 03:11, 03:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 00:05:34

1) 这一组画面整体在讲如何使用 Python 脚本生成用户学习数据，并通过 NiFi 流程调度将数据写入 HDFS。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 Python 脚本的开头部分，导入了 random、uuid、time、datetime、java.io、org.apache.commons.io、org.apache.nifi.processor.io 等模块，并定义了 BROWSER 列表和 datetamp() 函数。
画面2: 展示了 Python 脚本的 datetamp() 函数实现，用于生成随机的时间戳。
画面3: 展示了 NiFi 流程图，包含多个处理器（如 ReadFile、SplitJson、EvaluateJsonPath、PutHive、ConvertAvroToJSON、JsonToHiveProcessor）及其连接关系。
画面4: 展示了 NiFi 流程图的详细视图，包括处理器和连接的配置。
画面5: 展示了 NiFi 流程图中 ConvertAvroToJSON 和 JsonToHiveProcessor 的详细信息。
画面6: 展示了 NiFi 流程图的空白状态。
画面7: 展示了文件上传对话框，选择文件“数据生产_用户学习(在线学习)-ToHDFS.xml”。
画面8: 展示了 NiFi 流程图的空白状态。
画面9: 展示了 NiFi 流程图中“数据生产_用户学习(在线学习)-ToHDFS”处理器的详细信息。
画面10: 展示了 NiFi 控制器服务配置界面，配置了数据库连接 URL、驱动类名、用户名、密码等。
画面11: 展示了启用控制器服务的界面，服务名为“Mysql连接”，作用域为“Service only”。
画面12: 展示了 NiFi 流程图的空白状态。
画面13: 展示了 NiFi 流程图的详细视图，包括处理器和连接的配置。
画面14: 展示了 NiFi 流程图中“数据生产_用户学习(在线学习)-ToHDFS”处理器的详细信息。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1:
```python
import random
import uuid
import time, datetime
import java.io
from org.apache.commons.io import TOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
from org.apache.nifi.processors.script import ExecuteScript

BROWSER = ['Firefox', 'Chrome', '360', 'Fz', 'sougou', 'Reboot', 'IE', 'Spark', 'QQ', 'UC', 'Dnuc1', 'Liebao', 'AY']
```

画面2:
```python
def datetamp():
    now_info = datetime.datetime.now()
    delta = datetime.timedelta(random.randint(1, 30))
    time_info = now_info - delta
    for_time = time.time.strftime('%Y-%m-%d %H:%M:%S')
    times = int(time.mktime(time.strptime(for_time, '%Y-%m-%d %H:%M:%S')))
    return times
```

画面3:
```xml
资料中介代码路径：
    - 投资资料
        - 第3章-即时营销
            - nifi
                - 用户学习(在线学习).py
```

画面7:
```xml
<filename>数据生产_用户学习(在线学习)-ToHDFS.xml</filename>
```

画面10:
```properties
Database Connection URL: jdbc:mysql://xc-online:3306/xc_cours...
Database Driver Class Name: com.mysql.cj.jdbc.Driver
Database Driver Location: /root/mysql-connector-java-8.0.16.jar
Database User: root
Password: (No value set)
Max Wait Time: 500 mills
Max Total Connections: 8
Validation query: (No value set)
Minimum Idle Connections: 0
Max Idle Connections: 8
Max Connection Lifetime: -1
Time Between Eviction Runs: -1
Minimum Evictable Idle Time: 10 mins
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面3:
- 标题: 3.3.2 NiFi调度
- 流程图结构:
  - ReadFile → SplitJson → EvaluateJsonPath → PutHive
  - ReadFile → SplitJson → EvaluateJsonPath → ConvertAvroToJSON → JsonToHiveProcessor
  - ReadFile → SplitJson → EvaluateJsonPath → PutHive
  - ReadFile → SplitJson → EvaluateJsonPath → ConvertAvroToJSON → JsonToHiveProcessor
  - ReadFile → SplitJson → EvaluateJsonPath → PutHive
  - ReadFile → SplitJson → EvaluateJsonPath → ConvertAvroToJSON → JsonToHiveProcessor

画面5:
- 表格数据:
  - ConvertAvroToJSON: Read/Write 194.35 KB / 575.31 KB, Tasks/Time 00:00:00.031
  - JsonToHiveProcessor: Read/Write 110 bytes / 116 bytes, Tasks/Time 00:00:02.495

画面10:
- 表格数据:
  - Database Connection URL: jdbc:mysql://xc-online:3306/xc_cours...
  - Database Driver Class Name: com.mysql.cj.jdbc.Driver
  - Database Driver Location: /root/mysql-connector-java-8.0.16.jar
  - Database User: root
  - Password: (No value set)
  - Max Wait Time: 500 mills
  - Max Total Connections: 8
  - Validation query: (No value set)
  - Minimum Idle Connections: 0
  - Max Idle Connections: 8
  - Max Connection Lifetime: -1
  - Time Between Eviction Runs: -1
  - Minimum Evictable Idle Time: 10 mins

5) 无。
