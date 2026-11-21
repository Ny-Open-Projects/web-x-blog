# 画面线理解：21-实时分析-今日购买量-NiFi生产数据&测试

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\21-实时分析-今日购买量-NiFi生产数据&测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:27, 00:46, 01:03, 01:30, 01:51, 02:09, 02:29, 02:59, 03:10, 03:30, 03:50, 04:09, 04:40, 04:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:51:21

1) 这一组画面整体在讲如何使用 NiFi 工具生成模拟订单数据并写入 MySQL 数据库，同时展示相关的 Python 脚本和 Spark 实时分析代码。

2) 按时间顺序列出每张画面的要点：
画面1: 显示 Typora 文档，标题为“4.3 NiFi生产数据”，子标题“4.3.1 生产数据脚本”，展示 Python 代码片段，导入模块包括 random、uuid、time、datetime、json、java.io，以及 org.apache.nifi.processors.script 的 ExecuteScript。
画面2: 显示 Navicat Premium 中的 MySQL 数据库表 xc_order，包含 order_number、initial_price、start_time、end_time、status、user_id、details 字段，数据行数为 21647。
画面3: 显示 IntelliJ IDEA 中的 Scala 项目，运行日志显示 Spark 作业执行过程，包括 DStreamGraph、SparkContext、DAGScheduler 等信息，最终结果为 ResultStage 42。
画面4: 显示 Typora 文档，标题为“4.3 NiFi生产数据”，子标题“4.3.1 生产数据脚本”，展示 Python 代码片段，定义了 datestamp 函数，用于生成随机时间戳。
画面5: 显示 NiFi 流编辑器界面，空白画布，准备创建数据流。
画面6: 显示 NiFi 流编辑器界面，弹出“Enable Controller Service”对话框，服务名称为“Mysql连接”，作用域为“Service only”，引用组件包括“PutSQL”和“QueryDatabaseTable”。
画面7: 显示 NiFi 流编辑器界面，已构建的数据流，包含 In、ExecuteScript、SplitJson、ReplaceText、PutSQL 等处理器，数据流向清晰。
画面8: 显示 NiFi 流编辑器界面，弹出“RodView Community v1.7.0”窗口，显示数据库表结构，字段为“course buy d...”。
画面9: 显示 NiFi 流编辑器界面，数据流已构建完成，处理器包括 In、ExecuteScript、SplitJson、ReplaceText、PutSQL，数据流向清晰。
画面10: 显示 Navicat Premium 中的 MySQL 数据库表 xc_order，执行 SQL 语句，INSERT INTO 语句插入数据，影响行数为 1。
画面11: 显示 Typora 文档，标题为“4.3 NiFi生产数据”，子标题“4.3.1 生产数据脚本”，展示 NiFi 流架构图，包含 In、ExecuteScript、SplitJson、ReplaceText、PutSQL 等处理器，以及资料中调度代码路径。
画面12: 显示 IntelliJ IDEA 中的 Scala 项目，运行日志显示 Spark 作业执行过程，包括 DStreamGraph、SparkContext、DAGScheduler 等信息，最终结果为 ResultStage 42。
画面13: 显示 Navicat Premium 中的 MySQL 数据库表 xc_order，执行 SQL 语句，INSERT INTO 语句插入数据，影响行数为 1。
画面14: 显示 Typora 文档，标题为“4.3 NiFi生产数据”，子标题“4.3.1 生产数据脚本”，展示 Python 代码片段，定义了 datestamp 函数，用于生成随机时间戳。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1:
```python
import random
import uuid
import time, datetime
import json
import java.io
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
from org.apache.nifi.processors.script import ExecuteScript
```

画面4:
```python
import random
import uuid
import time, datetime
import json
import java.io
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
from org.apache.nifi.processors.script import ExecuteScript

def datestamp():
    now_info = datetime.datetime.now()
    delta = datetime.timedelta(random.randint(1, 60))
    time_info = now_info - delta
    for_time = time_info.strftime('%Y-%m-%d %H:%M:%S')
    times = int(time.mktime(time.strptime(for_time, '%Y-%m-%d %H:%M:%S')))
    return times
```

画面10:
```sql
INSERT INTO `xc_order` (`order_number`, `initial_price`, `price`, `start_time`, `end_time`, `status`, `user_id`, `details`, `old_status`) VALUES ('00042860926e4c1', 1201.00, 1201.00, '2019-10-08 09:22:03', '2019-10-08 09:22:03', 401002, '73501356444405b74', NULL, 401002);
```

画面13:
```sql
INSERT INTO `xc_order` (`order_number`, `initial_price`, `price`, `start_time`, `end_time`, `status`, `user_id`, `details`, `old_status`) VALUES ('00042860926e4c1', 1201.00, 1201.00, '2019-10-08 09:22:03', '2019-10-08 09:22:03', 401002, '73501356444405b74', NULL, 401002);
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面11:
- PPT 标题：4.3 NiFi生产数据
- 子标题：4.3.1 生产数据脚本
- 架构图：In → ExecuteScript → SplitJson → ReplaceText → PutSQL
- 资料中调度代码路径：
  - 资源资料
    - 第1章 实时分析
      - nifi
        - 代码
          - 如此实现 - tokafta-实时.xml
- PS: 数据生产的 NiFi 流程实时采集的流程放在了一个 XML 中，只导入一次即可！

5) 无
