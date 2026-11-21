# 画面线理解：12-课程分析-课程访问量分析-使用NiFi将课程访问量分析结果同步到MySQl

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/1.数据清洗
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\1.数据清洗\12-课程分析-课程访问量分析-使用NiFi将课程访问量分析结果同步到MySQl_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:19, 01:35, 01:57, 02:17, 03:26, 03:39, 03:50, 04:00, 04:15, 04:37, 04:50, 05:24, 05:39, 06:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:55:50

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 NiFi 将 Hive 数据同步到 MySQL，包括创建业务表、配置数据流和编写 NiFi 流程 XML 代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录结构，当前章节为“1.2 业务数据从Hive到MySQL”，右侧显示 Hive 表结构和 SQL 创建语句。
画面2：在 Navicat Premium 中展示数据库结构，选中了 `xc_learning` 数据库下的 `business` 数据库。
画面3：展示 NiFi 数据流设计，包含 `SelectHiveSQL` → `ConvertAvroToSQL` → `SplitJson` → `EvaluateJsonPath` → `PutSQL` 的流程。
画面4：展示 NiFi 流程图，包含 `SelectHiveSQL` → `ConvertAvroToSQL` → `SplitJson` → `EvaluateJsonPath` → `PutSQL` 的流程。
画面5：在 Hive 的 Table Browser 中展示 `course_visit_biz` 表的数据。
画面6：浏览器打开 NiFi 界面，页面为空白。
画面7：在 NiFi 界面中弹出“Upload Template”对话框，点击“LOAD”按钮。
画面8：弹出“Add Template”对话框，选择模板“课程访问量-Hive-To-Mysql”。
画面9：在 NiFi 的“课程访问量-Hive-To-Mysql Configuration”页面，显示“GENERAL”标签页，包含 Hive 和 MySQL 的连接池配置，状态为“Disabled”。
画面10：在 NiFi 的“课程访问量-Hive-To-Mysql Configuration”页面，显示“GENERAL”标签页，Hive 连接池状态已改为“Enabled”，MySQL 连接池状态仍为“Disabled”。
画面11：在 NiFi 流程图中，显示 `SelectHiveSQL` → `ConvertAvroToSQL` → `SplitJson` → `EvaluateJsonPath` → `PutSQL` 的流程，各组件的属性已配置。
画面12：在 NiFi 流程图中，显示 `SelectHiveSQL` → `ConvertAvroToSQL` → `SplitJson` → `EvaluateJsonPath` → `PutSQL` 的流程，各组件的属性已配置。
画面13：展示 NiFi 数据流设计，包含 `SelectHiveSQL` → `ConvertAvroToSQL` → `SplitJson` → `EvaluateJsonPath` → `PutSQL` 的流程。
画面14：展示 NiFi 流程图，包含 `SelectHiveSQL` → `ConvertAvroToSQL` → `SplitJson` → `EvaluateJsonPath` → `PutSQL` 的流程，各组件的属性已配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```sql
-- 在导入业务数据时，business数据库需导入
CREATE TABLE 'course_visit_biz' (
    'date_info' date NOT NULL COMMENT '天，某一天的访问量',
    'count' int(11) NOT NULL COMMENT '当前访问计数'
) ENGINE=InnoDB DEFAULT CHARSET=utf8
```

画面3：
```text
-- 导入业务数据时，business数据库需导入
CREATE TABLE 'course_visit_biz' (
    'date_info' date NOT NULL COMMENT '天，某一天的访问量',
    'count' int(11) NOT NULL COMMENT '当前访问计数'
) ENGINE=InnoDB DEFAULT CHARSET=utf8
```

画面4：
```text
nifi 流程xml代码路径：
    资源资料
        第3章-课程分析
            nifi/课程访问量-课程访问量-Hive-To-Mysql.xml
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：NiFi 数据流流程图，结构为：
SelectHiveSQL → ConvertAvroToSQL → SplitJson → EvaluateJsonPath → PutSQL

画面11：NiFi 数据流流程图，结构为：
SelectHiveSQL → ConvertAvroToSQL → SplitJson → EvaluateJsonPath → PutSQL

画面12：NiFi 数据流流程图，结构为：
SelectHiveSQL → ConvertAvroToSQL → SplitJson → EvaluateJsonPath → PutSQL

画面13：NiFi 数据流流程图，结构为：
SelectHiveSQL → ConvertAvroToSQL → SplitJson → EvaluateJsonPath → PutSQL

画面14：NiFi 数据流流程图，结构为：
SelectHiveSQL → ConvertAvroToSQL → SplitJson → EvaluateJsonPath → PutSQL

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
