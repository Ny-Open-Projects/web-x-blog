# 画面线理解：06-课程分析-课程购买量-NiFi生产订单数据保存到MySQL&并进行实时采集

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\06-课程分析-课程购买量-NiFi生产订单数据保存到MySQL&并进行实时采集_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:35, 01:05, 01:28, 01:50, 02:04, 02:27, 03:30, 04:07, 04:20, 04:52, 05:06, 05:17, 05:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:02:02

1) 这一组画面整体在讲如何使用 Nifi 实时采集 MySQL 订单数据并写入 Hive，涉及数据源配置、流程设计、Python 脚本处理及测试验证。

2) 按时间顺序列出每张画面的要点：
画面1：在 Navicat Premium 中执行 SQL 插入语句，向 xc_orders 表插入一条订单记录，显示受影响行数为1。
画面2：在 Navicat Premium 中查看 xc_orders 表的数据，显示了多条订单记录，包括 order_number、initial_price、start_time 等字段。
画面3：在 Typora 编辑器中展示 Nifi 数据流设计文档，包含 Nifi 流程图和 Python 代码片段。
画面4：在 Nifi 界面中弹出“Upload Template”对话框，用于上传模板。
画面5：在 Nifi 界面中弹出“Add Template”对话框，选择“课程购买量-到MySQL”模板。
画面6：在 Nifi 界面中显示“0. 数据生产：课程购买量-ToMySQL Configuration”配置页面，包含 DistributedMapCacheServer 和 MySQL 连接池服务。
画面7：在 Nifi 界面中展示数据流图，包含 QueryDatabaseTable、ConvertAvroToJSON、SplitJson、EvaluateJsonPath、ReplaceText、ExecuteScript、PutSQL 等处理器。
画面8：在 Nifi 界面中展示数据流图，包含 QueryDatabaseTable、ConvertAvroToJSON、SplitJson、EvaluateJsonPath、ReplaceText、ExecuteScript、PutSQL 等处理器，并显示右键菜单选项。
画面9：在 Hue 界面中展示 course_orders_source 表的数据，显示了多条订单记录。
画面10：在 Hue 界面中展示 course_orders_source 表的数据，显示了多条订单记录。
画面11：在 Hue 界面中执行 SQL 查询，显示查询结果为 18642。
画面12：在 Typora 编辑器中展示 Nifi 数据流设计文档，包含 Nifi 流程图和 Python 代码片段。
画面13：在 Typora 编辑器中展示 Python 代码，用于生成模拟订单数据并写入流文件。
画面14：在 Typora 编辑器中展示测试步骤，包括启动服务、验证数据写入 Hive 等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```sql
INSERT INTO `xc_order`.`xc_orders` (`order_number`, `initial_price`, `start_time`, `end_time`, `status`, `user_id`, `details`, `old_status`)
VALUES ('2901226', 0.81, '2018-04-05 10:32:33', '2018-04-05 21:32:33', 401002, '68769ff7579411a9a3464d438d4e88', '[{"itemId":"2901226","itemNum":1,"itemPrice":"0.81","orderNumber":"2901226"}]', 401002);
```

画面3：
```text
QueryDatabaseTable → ConvertAvroToJSON → SplitJson → EvaluateJsonPath → ReplaceText → ExecuteScript → SplitJson → EvaluateJsonPath → PutSQL
```

画面7：
```text
QueryDatabaseTable
ConvertAvroToJSON
SplitJson
EvaluateJsonPath
ReplaceText
ExecuteScript
PutSQL
```

画面13：
```python
dist['status'] = str(pay_status)
dist['order_time'] = str(datetamp())
dist['user_id'] = str(user_id)
dist['details'] = json.dumps(data)
arr.append(dist)

outputStream.write(bytearray(json.dumps(arr), encoding="utf-8"))
```

画面14：
```text
所有的配置量完成之后，按下运行程序进行了测试，启动之前需要确认的服务已启动，这里依赖了MySQL、Hadoop、Hive，请确认已启动，最终在MySQL订单表中产生订单，Nifi把数据实时采集到Hive中，测试成功，测试步骤如下：
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：
标题：2.3.3.2.2 流程代码
流程图结构：
QueryDatabaseTable → ConvertAvroToJSON → SplitJson → EvaluateJsonPath → ReplaceText → ExecuteScript → SplitJson → EvaluateJsonPath → PutSQL

画面7：
流程图结构：
QueryDatabaseTable → ConvertAvroToJSON → SplitJson → EvaluateJsonPath → ReplaceText → ExecuteScript → PutSQL

画面12：
标题：2.3.3.2.2 流程代码
流程图结构：
QueryDatabaseTable → ConvertAvroToJSON → SplitJson → EvaluateJsonPath → ReplaceText → ExecuteScript → SplitJson → EvaluateJsonPath → PutSQL

5) 不要评价画面美观，不要输出与课程无关的内容。
