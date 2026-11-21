# 画面线理解：day13-9-可靠消息实现最终一致性-入门案例-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-6 可靠消息实现最终一致性
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-6 可靠消息实现最终一致性\day13-9-可靠消息实现最终一致性-入门案例-功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:24, 02:22, 04:10, 04:54, 05:52, 07:55, 09:19, 10:17, 11:00, 12:08, 13:01, 13:53, 14:19, 15:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:06:13

1) 这一组画面整体在讲什么（一句话）：
演示基于消息的最终一致性事务解决方案，通过 Broker 中间件协调两个银行服务（bank1 和 bank2）的本地事务，实现跨服务的事务一致性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 展示了 bank1 服务的 Controller 层代码，用于处理转账请求。
- 代码逻辑：解析 JSON 消息体，创建 AccountChangeEvent 事件，调用 accountInfoService.updateAccountBalance 方法。
- 画面右侧是课程 PPT，标题为“5.4 解决标审核业务中的事务问题”，子标题“5.3.4 功能测试”。
- PPT 内容：bank1 和 bank2 都成功时，bank2 接收不到转账消息；bank1 执行本地事务失败，bank2 接收不到转账消息；bank1 执行完本地事务后，不返回任何信息，则 Broker 会进行事务回查；bank2 执行本地事务失败，会进行重试消费。
- PPT 说明：可选消息最终一致性事务适合执行周期长且实时性要求不高的场景。引入机制后，同步事务操作变为基于消息执行的异步操作，避免了分布式事务中的同步阻塞操作，实现了两个服务的解耦。

画面 2:
- 展示了 bank1 服务的 application.properties 配置文件。
- 配置内容：
  spring.application.name=ensure-message-demo-bank1
  server.port=50001
  server.servlet.context-path=/bank1
  spring.http.encoding.enabled=true
  spring.http.encoding.charset=UTF-8
  spring.mvc.throw-exception-if-no-handler-found=true
  spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
  spring.datasource.driver-class-name=com.mysql.jdbc.Driver
  spring.datasource.url=jdbc:mysql://localhost:3306/bank1?useUnicode=true

画面 3:
- 展示了 bank1 服务的 AccountInfoController.java 代码。
- 代码逻辑：接收转账请求，调用 accountInfoService.updateAccountBalance 方法。
- 控制台输出：转账成功。

画面 4:
- 展示了 bank1 服务的 AccountInfoServiceImpl.java 代码。
- 代码逻辑：更新账户余额，调用 bankMessageProducer.sendAccountChangeEvent 方法发送消息。
- 代码中包含注解 @Transactional(isolation = Isolation.SERIALIZABLE)。

画面 5:
- 展示了事务处理流程图。
- 流程图结构：
  - “本地事务 A服务数据库” → “发送方 A服务”（步骤 3：执行本地事务）
  - “发送方 A服务” → “服务端 Broker”（步骤 1：发送半消息）
  - “服务端 Broker” → “接收方 B服务”（步骤 2：半消息发送成功）
  - “服务端 Broker” → “发送方 A服务”（步骤 4：Commit 或者 Rollback）
  - “发送方 A服务” → “本地事务 A服务数据库”（步骤 6：检查本地事务的状态）
  - “服务端 Broker” → “发送方 A服务”（步骤 5：未收到 4 的确认时，回查事务状态）
  - “服务端 Broker” → “接收方 B服务”（步骤 7：根据事务的状态 Commit/Rollback）

画面 6:
- 与画面 5 完全相同，为流程图的延续展示。

画面 7:
- 展示了 TransferTransactionListener.java 文件中的 executeLocalTransaction 方法。
- 代码逻辑：解析消息体，创建 AccountChangeEvent 事件，执行本地事务。
- 代码中包含注释“//执行本地事务”。

画面 8:
- 展示了 TransferTransactionListener.java 文件中的 checkLocalTransaction 方法。
- 代码逻辑：打印“事务回查”，解析消息体，创建 AccountChangeEvent 事件。
- 控制台输出：事务回查。

画面 9:
- 展示了 bank1 数据库的 account_info 表，其中 account_no 为 1，account_balance 为 900。

画面 10:
- 展示了 TransferTransactionListener.java 文件中的 executeLocalTransaction 方法。
- 代码逻辑：执行本地事务后，根据结果返回 COMMIT 或 ROLLBACK。
- 代码中包含注释“//返回执行结果”。

画面 11:
- 展示了 bank2 服务的 AccountInfoServiceImpl.java 代码。
- 代码逻辑：更新账户余额，调用 accountInfoDao.updateAccountBalance 方法。
- 代码中包含注解 @Transactional(isolation = Isolation.SERIALIZABLE)。

画面 12:
- 展示了 bank2 服务的 AccountInfoServiceImpl.java 代码。
- 代码逻辑：更新账户余额，调用 accountInfoDao.updateAccountBalance 方法。
- 控制台输出：bank2 执行本地事务。

画面 13:
- 展示了 bank2 数据库的 account_info 表，其中 account_no 为 2，account_balance 为 200。

画面 14:
- 展示了课程 PPT，标题为“5.4 解决标审核业务中的事务问题”，子标题“5.3.4 功能测试”和“5.4.1 问题分析”。
- PPT 内容：存储账户人的最初始的有余额，P2P 运营管理模块该标的，触发放款，并共同还款流程。
