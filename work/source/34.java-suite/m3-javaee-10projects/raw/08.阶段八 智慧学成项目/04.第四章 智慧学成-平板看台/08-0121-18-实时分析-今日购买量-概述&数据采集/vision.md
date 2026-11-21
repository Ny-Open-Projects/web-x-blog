# 画面线理解：18-实时分析-今日购买量-概述&数据采集

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\18-实时分析-今日购买量-概述&数据采集_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:08, 01:23, 01:44, 01:57, 02:36, 02:46, 03:12, 03:25, 03:48, 05:00, 05:26, 05:52, 06:08, 06:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:48:52

1) 这一组画面整体在讲如何使用 NiFi 实时采集 MySQL 数据并发送到 Kafka，以及如何测试该数据流。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程PPT，标题为“4 今日购买量”，子标题“4.1 数据采集”，内容说明“今日购买量的采集逻辑是：监听xc_order表的binlog，有xc_ordersort数据，获取到订单id，放入Kafka指定topic”。下方有“4.1.1 NiFi采集流程”小节。
画面2：NiFi工作区空白，准备新建或编辑数据流。
画面3：弹出“Upload Template”对话框，提示“Select Template”，鼠标悬停在“UPLOAD”按钮上。
画面4：弹出“Add Template”对话框，下拉菜单中选中“今日购买量Kafka实时”，鼠标悬停在“ADD”按钮上。
画面5：弹出“Enable Controller Service”对话框，服务为“DistributedMapCacheClientService”，作用域为“Service only”，引用组件为“CaptureChangeMySQL”。
画面6：NiFi工作区显示数据流，包含“CaptureChangeMySQL”、“Insert”、“PutKafka”、“EvaluateJsonPath”等处理器，数据流向为：CaptureChangeMySQL → Insert → PutKafka，同时Insert → EvaluateJsonPath。
画面7：展示课程PPT，标题为“4.1.4 测试”，内容包括“测试方式同：2.3.4 测试”和“模拟测试命令”，命令为“./kafka-console-consumer.sh --bootstrap-server xc-online-kafka:9092 --topic course_buy”，下方有“订单表插入数据SQL”。
画面8：NiFi工作区显示数据流，与画面6相同，但“Insert”处理器下方的“过滤器”处理器被选中。
画面9：弹出“Empty Queue”对话框，提示“7,967 FlowFiles (8.83 MB) were removed from the queue”，鼠标悬停在“OK”按钮上。
画面10：终端窗口显示“kafka-console-consumer.sh”命令执行结果，输出大量订单数据。
画面11：展示课程PPT，标题为“4.1.4 测试”，内容包括“测试方式同：2.3.4 测试”和“模拟测试命令”，命令为“./kafka-console-consumer.sh --bootstrap-server xc-online-kafka:9092 --topic course_buy”，下方有“订单表插入数据SQL”。
画面12：数据库管理工具（Navicat Premium）中显示“xc_order”表，SQL语句为“INSERT INTO `xc_order`...”，执行结果为“affected rows: 1”。
画面13：展示课程PPT，标题为“4.1.4 测试”，内容包括“测试方式同：2.3.4 测试”和“模拟测试命令”，命令为“./kafka-console-consumer.sh --bootstrap-server xc-online-kafka:9092 --topic course_buy”，下方有“订单表插入数据SQL”。
画面14：终端窗口显示“kafka-console-consumer.sh”命令执行结果，输出大量订单数据，同时显示“4.2 统计分析”和“4.2.1 统计分析逻辑”标题。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面7、11、13中的SQL：
INSERT INTO `xc_order` `xc_orders` (`order_number`, `initial_price`, `price`, `start_time`, `end_time`, `status`, `user_id`, `details`, `old_status`) VALUES ('00042b89c2e8cc1b5a9f7c40393796', NULL, 1201.00, '2019-10-08 09:22:03', '2019-10-08 09:22:03', '401002', '7f3561356b44405b62f757ae59c6af1', '{"orderNumber": "00042b89c2e8cc1b5a9f7c40393796", "itemId": "004eb7dde20842a3b143c313ab5a6a", "itemNum": 1, "itemPrice": "217"}', NULL);

画面7、11、13中的命令：
./kafka-console-consumer.sh --bootstrap-server xc-online-kafka:9092 --topic course_buy

画面12中的SQL：
INSERT INTO `xc_order` `xc_orders` (`order_number`, `initial_price`, `price`, `start_time`, `end_time`, `status`, `user_id`, `details`, `old_status`) VALUES ('00042b89c2e8cc1b5a9f7c40393796', NULL, 1201.00, '2019-10-08 09:22:03', '2019-10-08 09:22:03', '401002', '7f3561356b44405b62f757ae59c6af1', '{"orderNumber": "00042b89c2e8cc1b5a9f7c40393796", "itemId": "004eb7dde20842a3b143c313ab5a6a", "itemNum": 1, "itemPrice": "217"}', NULL);

画面10、14中的命令：
kafka-console-consumer.sh --bootstrap-server xc-online-kafka:9092 --topic course_buy

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：PPT标题“4 今日购买量”，子标题“4.1 数据采集”，内容“今日购买量的采集逻辑是：监听xc_order表的binlog，有xc_ordersort数据，获取到订单id，放入Kafka指定topic”。
画面6：NiFi数据流架构图，结构为：CaptureChangeMySQL → Insert → PutKafka，同时Insert → EvaluateJsonPath。
画面7、11、13：PPT标题“4.1.4 测试”，内容“测试方式同：2.3.4 测试”，“模拟测试命令”为“./kafka-console-consumer.sh --bootstrap-server xc-online-kafka:9092 --topic course_buy”，“订单表插入数据SQL”为“INSERT INTO `xc_order`...”。
画面12：数据库管理工具界面，显示“xc_order”表，SQL语句为“INSERT INTO `xc_order`...”，执行结果为“affected rows: 1”。
画面14：终端窗口显示“kafka-console-consumer.sh”命令执行结果，同时显示“4.2 统计分析”和“4.2.1 统计分析逻辑”标题。

5) 无。
