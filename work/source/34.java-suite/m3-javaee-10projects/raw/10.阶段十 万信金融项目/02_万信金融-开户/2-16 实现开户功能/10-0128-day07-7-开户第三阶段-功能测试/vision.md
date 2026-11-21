# 画面线理解：day07-7-开户第三阶段-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day07-7-开户第三阶段-功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:46, 03:49, 04:46, 05:51, 07:06, 09:34, 10:02, 11:22, 12:21, 13:23, 14:34, 15:34, 16:40, 17:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:32:24

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 RocketMQ 消息队列实现用户开户流程中的异步通知，并通过 Apollo 配置中心管理相关配置，同时展示测试数据的插入和消息消费的全过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了测试前的准备工作说明，包括需要启动的系统组件（RocketMQ、Apollo、银行存储系统、微服务工程、P2P前端工程）。
- 提供了用于测试的 SQL 脚本，用于插入测试用户数据。
  USE `p2p_consumer`;
  INSERT INTO `consumer` (`ID`, `USERNAME`, `MOBILE`, `IS_BIND_CARD`) VALUES
  (C001, '15378791981', '15378791981', 0),
  (C002, '15378791982', '15378791982', 0),
  (C003, '15378791983', '15378791983', 0),
  (C004, '15378791984', '15378791984', 0),
  (C005, '15378791985', '15378791985', 0);
  USE `p2p_account`;
  INSERT INTO `account` (`ID`, `USERNAME`, `MOBILE`, `PASSWORD`, `DOMAIN`) VALUES
  (C001, '15378791981', '15378791981', 'a79c7ae8be23f8ad4e6604c6166b846b515e8b7e25414e', 'c'),
  (C002, '15378791982', '15378791982', 'a79c7ae8be23f8ad4e6604c6166b846b515e8b7e25414e', 'c'),
  (C003, '15378791983', '15378791983', 'a79c7ae8be23f8ad4e6604c6166b846b515e8b7e25414e', 'c'),
  (C004, '15378791984', '15378791984', 'a79c7ae8be23f8ad4e6604c6166b846b515e8b7e25414e', 'c'),
  (C005, '15378791985', '15378791985', 'a79c7ae8be23f8ad4e6604c6166b846b515e8b7e25414e', 'c');

画面 2：
- 展示了 Apollo 配置中心的登录页面，用于管理服务配置。
- 右侧是浏览器开发者工具的 Network 标签页，用于监控网络请求。

画面 3：
- 展示了 IDE 中的 Java 代码，是 `GatewayNotifyConsumer` 类的一部分。
- 代码中包含一个异常信息：`Caused by org.apache.rocketmq.client.exception.MQClientException: the specified group is blank`，提示消费者组配置为空。
- 代码逻辑：当 tag 为 "PERSONAL_REGISTER" 时，调用 `consumerService.modifyResult(response)`。

画面 4：
- 展示了 `GatewayNotifyConsumer` 类的代码，其中定义了 `@Value("${rocketmq.consumer.group}")` 和 `@Value("${rocketmq.name-server}")` 注解，用于注入 RocketMQ 的消费者组和 NameServer 配置。
- 代码中 `defaultMQPushConsumer` 的构造函数被调用，传入了 `consumerGroup`。

画面 5：
- 展示了 Apollo 配置中心的界面，其中显示了多个服务的配置文件，包括 `wanningzp.account-service` 和 `wanningzp.consumer-service`。
- 界面中显示了 `micro_service.spring-eureka` 的配置信息。

画面 6：
- 展示了 IDE 中的 Java 代码，是 `GatewayNotifyConsumer` 类的构造函数部分。
- 代码中 `defaultMQPushConsumer` 被实例化，并设置了 NameServer 和 ConsumerGroup。

画面 7：
- 展示了 IDE 中的 Java 代码，是 `GatewayNotifyConsumer` 类的构造函数部分。
- 代码中 `defaultMQPushConsumer` 被实例化，并设置了 NameServer 和 ConsumerGroup。
- 代码中 `subscribe` 方法被调用，订阅了主题 `TP_GATEWAY_NOTIFY_AGENT`。

画面 8：
- 展示了 Apollo 配置中心的页面，显示了用户登录后的首页，包含产品推荐和用户信息。
- 右侧是浏览器开发者工具的 Network 标签页，用于监控网络请求。

画面 9：
- 展示了 SQL Server Management Studio 中的 `p2p_depository` 数据库，显示了 `user` 表的数据。
- 表中包含用户 ID、用户名、手机号等字段。

画面 10：
- 展示了 Apollo 配置中心的页面，显示了开户存管的页面，包含身份证信息、客户姓名、银行账号、手机号等字段。
- 右侧是浏览器开发者工具的 Network 标签页，用于监控网络请求。

画面 11：
- 展示了 IDE 中的 Java 代码，是 `GatewayNotifyConsumer` 类的构造函数部分。
- 代码中 `defaultMQPushConsumer` 被实例化，并设置了 NameServer 和 ConsumerGroup。
- 代码中 `subscribe` 方法被调用，订阅了主题 `TP_GATEWAY_NOTIFY_AGENT`。

画面 12：
- 展示了 RocketMQ 控制台的消费者页面，显示了主题 `TP_GATEWAY_NOTIFY_AGENT`。
- 页面中包含“状态”、“重置”、“CONSUMER 管理”、“TOPIC 配置”、“发送消息”、“删除”等操作按钮。

画面 13：
- 展示了 RocketMQ 控制台的消息详情页面，显示了一条消息的详细信息。
- 消息 ID：COA802992DB010B4AAC25072F5770006
- Topic：TP_GATEWAY_NOTIFY_AGENT
- Tag：PERSONAL_REGISTER
- Storetime：2019-08-16

画面 14：
- 展示了测试 SQL 脚本，与画面 1 中的内容相同。
  USE `p2p_consumer`;
  INSERT INTO `consumer` (`ID`, `USERNAME`, `MOBILE`, `IS_BIND_CARD`) VALUES
  (C001, '15378791981', '15378791981', 0),
  (C002, '15378791982', '15378791982', 0),
  (C003, '15378791983', '15378791983', 0),
  (C004, '15378791984', '15378791984', 0),
  (C005, '15378791985', '15378791985', 0);
  USE `p2p_account`;
  INSERT INTO `account` (`ID`, `USERNAME`, `MOBILE`, `PASSWORD`, `DOMAIN`) VALUES
  (C001, '15378791981', '15378791981', 'a79c7ae8be23f8ad4e6604c6166b846b515e8b7e25414e', 'c'),
  (C002, '15378791982', '15378791982', 'a79c7ae8be23f8ad4e6604c6166b846b515e8b7e25414e', 'c'),
  (C003, '15378791983', '15378791983', 'a7
