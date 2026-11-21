# 18-实时分析-今日购买量-概述&数据采集

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\18-实时分析-今日购买量-概述&数据采集_【海量资源尽在 666java.com】.mp4
- 时长 6分41秒（音频 401s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 咱们接下来呢学习今日购买量这个指标前边呢已经完成了今日访问量以及新增用户量最后一个指标呢就是咱们的今日购买量它呢和前两个指标也是非常相似的咱们呢通过这个指标的学习需要掌握采集今日购买量的原始数据这里呢是实时采集保存到卡普卡中然后呢编写实时分析程序
[00:29] 通过读取Kafka中的数据然后实时的进行统计分析最终呢将结果保存到resist中供咱们的报表系统进行一个展示咱们首先来看数据采集这里呢今日购买量采集的是订单数据咱们前边呢其实在做购买量的时候已经采集过订单数据之前呢采集的数据是放到Hive中的这里呢咱们采集数据
[00:57] 因为是时时分析是需要放到Kafka中是基于咱们原来的采集进行的一个修改这里呢咱们直接把这个采集调度给上传上来即可咱们呢调度在咱们的资料中这里呢咱们切到NiFi把咱们这个NiFi采集这个调度给上传上来进行一个配置咱们呢切到时时分析这个处理器组在这里呢咱们新建一个处理器组是
[01:30] 今日购买量在这个处理器组内呢咱们上传咱们的数据采集的任务调度选择上传模板咱们呢现在选择的是今日购买量这个托卡普卡这个配置然后点击打开然后进行上传上传之后呢咱们使用添加模板的方式把它给添加进来好添加进来之后呢点入进入这个点击进入这个处理器组
[02:05] 这个处理器组也是包含了数据生产和数据采集咱们现在是数据采集阶段这个和咱们前边的新增用户量是非常类似的都是监控MySQL的binlog进行数据的采集采集完成之后放到卡布卡中这里咱们之前MapKit的Cyber就是缓存服务已经配置好这里需要将咱们当前
[02:34] 使用缓存服的客户端把它给启用启用完成之后咱们处理器组还需要一个配置就是MySQL的配置因为咱们现在是监控MySQL的Binlog它的相关配置是在当前处理器内然后咱们要把密码给配置上密码是123456其他的选项都是咱们配置好了直接使用即可好这里配置已经完成
[03:06] 接下来呢咱们就是对这个数据采集进行一个测试这里呢中间还有过滤的配置以及卡普卡的配置感兴趣的话可以去了解一下这里呢咱们都是配置好的直接使用即可咱们来进行测试这里呢测试的话就是首先启用咱们这个处理器组启用完处理器组呢咱们在卡普卡上进行一个数据的一个查看首先来启用这个处理器组这里呢
[03:36] 还是和之前一样咱们这个处理器呢它会监控所有的BINLOG之前的BINLOG呢是有大量的这个垃圾数据的咱们先启动一下启动完成之后呢把这个BINLOG让它堵一遍堵完之后呢它就不会再堵这个历史的BINLOG了这个时候呢咱们把这个数据给清了咱们就可以进行测试了这个地方还有一个在运行说明呢它还没有堵起完成堵起完成咱们已经停过了
[04:09] 这是所有的都是暂停状态就是说明它已经执行完成了这个呢还在运行中300已经读了300多张的数据还在读取中好已经运行完成运行完成呢咱们把对列的数据给清了再次启动集合这样做的一个主要原因是对列里边有大量的一个数据但是呢咱们现在采集的数据呢是不能直接放到卡普卡中它需要将对列的所有数据都给读完读取完成才行
[04:45] 咱们呢就使用先启动然后让它读数据读完数据呢把对链里给清了再次启动呢它这个对链里边就是空的咱们呢来监听binlog的时候就可以直接使用咱们呢切了卡卡把这个暂停了这个呢还是之前的一个跑的一个数据咱们呢使用新的这个监听命令这里呢执行它这个地方它说还没有
[05:16] 一个数据进来咱们呢这个地方先不用管它它是阻塞状态只要有数据了就行接下来呢咱们使用买色户的插入数据的命令来咱们呢就是业务买色户这个业务买色户呢就是咱们学生在线的业务买色户咱们来插入一条数据新建一个查询这个地方已经显示查入成功咱们来看Netflix采集到没这个地方可以看到Netflix已经采集到咱们来看卡普卡中
[05:47] 这里呢卡普卡中也可以看到有一条数据了咱们来对一下ID是00042然后尾号是3796这个数据呢肯定是对的咱们来切回问答这里呢咱们使用NiFi调度实时的采集MySQL的数据呢这里已经采集完成采集完成之后呢咱们也进行了咱们也进行测试测试这个流程上是没有问题的
[06:21] 好咱们本节呢就是概述了今日购买量需要掌握的内容以及呢进行了这个使用nife进行了数据的采集将咱们需要的订单数据呢实时的采集到Kafka中好视频呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 NiFi 实时采集 MySQL 数据并发送到 Kafka，以及如何测试该数据流。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程PPT，标题为“4 今日购买量”，子标题“4.1 数据采集”，内容说明“今日购买量的采集逻辑是：监听xc_order表的binlog，有xc_ordersort数据，获取到订单id，放入Kafka指定topic”。下方有“4.1.1 NiFi采集流程”小节。
画面2：NiFi工作区空白，准备新建或编辑数据流。
画面3：弹出“Upload Template”对话框，提示“Select Template”，鼠标悬停在“UPLOAD”按钮上。
画面4：弹出“Add Template”对话框，下拉菜单中选中“今日购买量Kafka实时”，鼠标悬停在“ADD”按钮上。
画面5：弹出“Enable Controller Service”对话框，服务为“DistributedMapCacheClientService”，作用域为“Service only”，引用组件为“CaptureChangeMySQL”。
画面6：NiFi工作区显示数据流，包含“CaptureChangeMySQL”、“Insert”、“PutKafka”、“EvaluateJsonPath”等处理器，数据流向为：CaptureChangeMySQL → Insert → PutKafka，同时Insert → EvaluateJsonPath。
画面7：展示课程PPT，标题为“4.1.4 测试”，内容包括“测试方式同：2.3.4 测试”和“模拟测试命令”，命令为“./Kafka-console-consumer.sh --bootstrap-server xc-online-Kafka:9092 --topic course_buy”，下方有“订单表插入数据SQL”。
画面8：NiFi工作区显示数据流，与画面6相同，但“Insert”处理器下方的“过滤器”处理器被选中。
画面9：弹出“Empty Queue”对话框，提示“7,967 FlowFiles (8.83 MB) were removed from the queue”，鼠标悬停在“OK”按钮上。
画面10：终端窗口显示“Kafka-console-consumer.sh”命令执行结果，输出大量订单数据。
画面11：展示课程PPT，标题为“4.1.4 测试”，内容包括“测试方式同：2.3.4 测试”和“模拟测试命令”，命令为“./Kafka-console-consumer.sh --bootstrap-server xc-online-Kafka:9092 --topic course_buy”，下方有“订单表插入数据SQL”。
画面12：数据库管理工具（Navicat Premium）中显示“xc_order”表，SQL语句为“INSERT INTO `xc_order`...”，执行结果为“affected rows: 1”。
画面13：展示课程PPT，标题为“4.1.4 测试”，内容包括“测试方式同：2.3.4 测试”和“模拟测试命令”，命令为“./Kafka-console-consumer.sh --bootstrap-server xc-online-Kafka:9092 --topic course_buy”，下方有“订单表插入数据SQL”。
画面14：终端窗口显示“Kafka-console-consumer.sh”命令执行结果，输出大量订单数据，同时显示“4.2 统计分析”和“4.2.1 统计分析逻辑”标题。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面7、11、13中的SQL：
INSERT INTO `xc_order` `xc_orders` (`order_number`, `initial_price`, `price`, `start_time`, `end_time`, `status`, `user_id`, `details`, `old_status`) VALUES ('00042b89c2e8cc1b5a9f7c40393796', NULL, 1201.00, '2019-10-08 09:22:03', '2019-10-08 09:22:03', '401002', '7f3561356b44405b62f757ae59c6af1', '{"orderNumber": "00042b89c2e8cc1b5a9f7c40393796", "itemId": "004eb7dde20842a3b143c313ab5a6a", "itemNum": 1, "itemPrice": "217"}', NULL);

画面7、11、13中的命令：
./Kafka-console-consumer.sh --bootstrap-server xc-online-Kafka:9092 --topic course_buy

画面12中的SQL：
INSERT INTO `xc_order` `xc_orders` (`order_number`, `initial_price`, `price`, `start_time`, `end_time`, `status`, `user_id`, `details`, `old_status`) VALUES ('00042b89c2e8cc1b5a9f7c40393796', NULL, 1201.00, '2019-10-08 09:22:03', '2019-10-08 09:22:03', '401002', '7f3561356b44405b62f757ae59c6af1', '{"orderNumber": "00042b89c2e8cc1b5a9f7c40393796", "itemId": "004eb7dde20842a3b143c313ab5a6a", "itemNum": 1, "itemPrice": "217"}', NULL);

画面10、14中的命令：
Kafka-console-consumer.sh --bootstrap-server xc-online-Kafka:9092 --topic course_buy

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：PPT标题“4 今日购买量”，子标题“4.1 数据采集”，内容“今日购买量的采集逻辑是：监听xc_order表的binlog，有xc_ordersort数据，获取到订单id，放入Kafka指定topic”。
画面6：NiFi数据流架构图，结构为：CaptureChangeMySQL → Insert → PutKafka，同时Insert → EvaluateJsonPath。
画面7、11、13：PPT标题“4.1.4 测试”，内容“测试方式同：2.3.4 测试”，“模拟测试命令”为“./Kafka-console-consumer.sh --bootstrap-server xc-online-Kafka:9092 --topic course_buy”，“订单表插入数据SQL”为“INSERT INTO `xc_order`...”。
画面12：数据库管理工具界面，显示“xc_order”表，SQL语句为“INSERT INTO `xc_order`...”，执行结果为“affected rows: 1”。
画面14：终端窗口显示“Kafka-console-consumer.sh”命令执行结果，同时显示“4.2 统计分析”和“4.2.1 统计分析逻辑”标题。

5) 无。

