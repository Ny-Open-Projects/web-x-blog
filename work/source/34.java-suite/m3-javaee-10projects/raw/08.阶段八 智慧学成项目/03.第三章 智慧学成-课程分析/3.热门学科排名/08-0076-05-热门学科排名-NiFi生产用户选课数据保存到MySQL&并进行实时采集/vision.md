# 画面线理解：05-热门学科排名-NiFi生产用户选课数据保存到MySQL&并进行实时采集

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\05-热门学科排名-NiFi生产用户选课数据保存到MySQL&并进行实时采集_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:17, 00:58, 01:18, 02:42, 03:06, 03:20, 03:46, 04:22, 04:53, 05:25, 05:42, 06:05, 06:22, 07:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:13:02

1) 这一组画面整体在讲如何使用 NiFi 结合 Python 脚本生成模拟用户数据并写入 MySQL 数据库。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程目录，当前位于“3.3.4 NiFi生产数据”章节，同时显示 Navicat Premium 中的数据库表结构，SQL 查询语句为：SELECT * FROM `xc_learning`.`xc_learning_course` LIMIT 1,000。
画面2：展示 PPT 内容，标题为“3.3.4 NiFi生产数据”，子标题“3.3.4.1 NiFi 调用流程”，内容说明 NiFi 调用流程：QueryDatabaseTable → ConvertAvroToJSON → SplitJson → EvaluateJsonPath → ReplaceText → ExecuteScript → SplitJson → EvaluateJsonPath → PutSQL。
画面3：与画面2内容相同，为 PPT 页面的延续。
画面4：展示课程目录，鼠标悬停在“3.3.4.3 生产数据python脚本”上，下方显示“nifi 流程.vm代码路径”。
画面5：展示 NiFi 流程界面，显示“数据生产：用户选课-ToMySQL”流程的运行状态，包含“QueryDatabaseTable”组件。
画面6：在 NiFi 界面中弹出“Upload Template”对话框，包含“Select Template”搜索框和“CANCEL”、“UPLOAD”按钮。
画面7：在 NiFi 界面中显示“0, 数据生产：用户选课-ToMySQL Configuration”配置页面，包含“GENERAL”和“CONTROLLER SERVICES”标签页，表格中显示“DistributedMapCacheServer”和“MySql连接”两个服务，状态为“Enabled”。
画面8：在 NiFi 界面中显示“0, 数据生产：用户选课-ToMySQL Configuration”配置页面，表格中“MySql连接”服务的状态被改为“Disabled”。
画面9：在 NiFi 界面中显示“数据生产：用户选课-ToMySQL”流程的运行状态，包含“QueryDatabaseTable”组件。
画面10：展示 Navicat Premium 中的数据库表结构，SQL 查询语句为：SELECT * FROM `xc_learning`.`xc_learning_course` LIMIT 1,000。
画面11：展示 NiFi 流程界面，显示“数据生产：用户选课-ToMySQL”流程的完整组件连接，包括 QueryDatabaseTable、ConvertAvroToJSON、SplitJson、EvaluateJsonPath、ReplaceText、ExecuteScript、SplitJson、EvaluateJsonPath、PutSQL 等组件。
画面12：展示 Hue 的 Table Browser 页面，页面正在加载中，显示“Table Browser”标题。
画面13：展示课程目录，鼠标悬停在“3.3.4.4 测试”上，下方显示“nifi 流程.vm代码路径”。
画面14：与画面2内容相同，为 PPT 页面的延续。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面13代码：
```python
import random
import time, datetime
import uuid
import json
import io
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processors.script import Import ExecuteScript

def datestamp():
    now.info = datetime.datetime.now()
    delta = datetime.timedelta(random.randint(1, 60))
    time.info = now.info + delta
    for_time = time.info.strftime('%Y-%m-%d %H:%M:%S')
    times = int(time.mktime(time.strptime(for_time, '%Y-%m-%d %H:%M:%S')))
    return times

class PutStreamCallback(StreamCallback):
    def __init__(self):
        pass

    def process(self, inputStream, outputStream):
        uc = str(IOUtils.toString(inputStream, StandardCharsets.UTF_8)).split(",")
        arr = []
        obj = {}
        obj['learning_course_id'] = str(uuid.uuid4()).replace("-", "")
        obj['course_id'] = uc[0]
        obj['user_id'] = uc[1]
        obj['valid'] = uc[2]
        obj['start'] = uc[3]
        obj['end'] = uc[4]
        obj['create_time'] = times
        obj['update_time'] = times
        obj['delete_flag'] = 0
        obj['create_user'] = "admin"
        obj['update_user'] = "admin"
        obj['create_dept'] = 0
        obj['update_dept'] = 0
        obj['create_ip'] = "127.0.0.1"
        obj['update_ip'] = "127.0.0.1"
        obj['create_source'] = "1"
        obj['update_source'] = "1"
        obj['create_type'] = "1"
        obj['update_type'] = "1"
        obj['create_reason'] = "1"
        obj['update_reason'] = "1"
        obj['create_note'] = "1"
        obj['update_note'] = "1"
        obj['create_time'] = times
        obj['update_time'] = times
        obj['delete_flag'] = 0
        obj['create_user'] = "admin"
        obj['update_user'] = "admin"
        obj['create_dept'] = 0
        obj['update_dept'] = 0
        obj['create_ip'] = "127.0.0.1"
        obj['update_ip'] = "127.0.0.1"
        obj['create_source'] = "1"
        obj['update_source'] = "1"
        obj['create_type'] = "1"
        obj['update_type'] = "1"
        obj['create_reason'] = "1"
        obj['update_reason'] = "1"
        obj['create_note'] = "1"
        obj['update_note'] = "1"
        obj['create_time'] = times
        obj['update_time'] = times
        obj['delete_flag'] = 0
        obj['create_user'] = "admin"
        obj['update_user'] = "admin"
        obj['create_dept'] = 0
        obj['update_dept'] = 0
        obj['create_ip'] = "127.0.0.1"
        obj['update_ip'] = "127.0.0.1"
        obj['create_source'] = "1"
        obj['update_source'] = "1"
        obj['create_type'] = "1"
        obj['update_type'] = "1"
        obj['create_reason'] = "1"
        obj['update_reason'] = "1"
        obj['create_note'] = "1"
        obj['update_note'] = "1"
        obj['create_time'] = times
        obj['update_time'] = times
        obj['delete_flag'] = 0
        obj['create_user'] = "admin"
        obj['update_user'] = "admin"
        obj['create_dept'] = 0
        obj['update_dept'] = 0
        obj['create_ip'] = "127.0.0.1"
        obj['update_ip'] = "127.0.0.1"
        obj['create_source'] = "1"
        obj['update_source'] = "1"
        obj['create_type'] = "1"
        obj['update_type'] = "1"
        obj['create_reason'] = "1"
        obj['update_reason'] = "1"
        obj['create_note'] = "1"
        obj['update_note'] = "1"
        obj['create_time'] = times
        obj['update_time'] = times
        obj['delete_flag'] = 0
        obj['create_user'] = "admin"
        obj['update_user'] = "admin"
        obj['create_dept'] = 0
        obj['update_dept'] = 0
        obj['create_ip'] = "127.0.0.1"
        obj['update_ip'] = "127.0.0.1"
        obj['create_source'] = "1"
        obj['update_source'] = "1"
        obj['create_type'] = "1"
        obj['update_type'] = "1"
        obj['create_reason'] = "1"
        obj['update_reason'] = "1"
        obj['create_note'] = "1"
        obj['update_note'] = "1"
        obj['create_time'] = times
        obj['update_time'] = times
        obj['delete_flag'] = 0
        obj['create_user'] = "admin"
        obj['update_user'] = "admin"
        obj['create_dept'] = 0
        obj['update_dept'] = 0
        obj['create_ip'] = "127.0.0.1"
        obj['update_ip'] = "127.0.0.1"
        obj['create_source'] = "1"
        obj['update_source'] = "1"
        obj['create_type'] = "1"
        obj['update_type'] = "1"
        obj['create_reason'] = "1"
        obj['update_reason'] = "1"
        obj['create_note'] = "1"
        obj['update_note'] = "1"
        obj['create
