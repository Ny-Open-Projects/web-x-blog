# 画面线理解：14.RocketMQ快速入门之消息过滤器（用户自定义属性）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\14.RocketMQ快速入门之消息过滤器（用户自定义属性）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:29, 01:14, 01:35, 02:12, 03:03, 03:43, 04:20, 05:07, 05:26, 06:03, 06:43, 07:32, 07:52, 08:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:02:54

1) 这一组画面整体在讲什么（一句话）：
演示 RocketMQ 消息过滤器的使用，包括设置支持过滤的配置、发送带属性的消息、以及消费者根据 SQL 表达式过滤消息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- PDF 文档内容：章节“2.5. 消息过滤器”，说明 RocketMQ 支持用户自定义属性进行过滤，过滤表达式类似 SQL 的 WHERE。
- 代码片段：展示消费者订阅的两种方式，包括完整匹配和或匹配。

画面 2：
- IDE 界面：显示 `SyncProducer.java` 文件，代码中创建了 `DefaultMQProducer`，设置 NameServer 地址，并启动生产者。
- 代码片段：`producer.setNamesrvAddr("172.16.55.185:9876"); producer.start();`

画面 3：
- IDE 界面：展示发送消息的代码，设置 topic 为 "my-topic"，tag 为 "delete"，并设置用户属性 "sex" 为 "女"。
- 代码片段：`message.putUserProperty("sex", "女");`

画面 4：
- IDE 界面：代码中设置用户属性 "age" 为 "18"。
- 代码片段：`message.putUserProperty("age", "18");`

画面 5：
- IDE 界面：代码中 topic 设置为 "my-topic-filter"。
- 代码片段：`Message message = new Message(topic: "my-topic-filter", tags: "delete", ...);`

画面 6：
- IDE 界面：展示消费者代码，订阅主题 "my-topic-filter"，使用 SQL 表达式 "sex='女' AND age=18" 进行过滤。
- 代码片段：`consumer.subscribe(topic: "my-topic-filter", MessageSelector.bySql("sex='女' AND age=18"));`

画面 7：
- IDE 界面：展示发送消息的代码，设置 topic 为 "my-topic-filter"，tag 为 "delete"，属性 "sex" 为 "女"，"age" 为 "18"。
- 控制台输出：显示消息发送成功，包含消息 ID、消息队列、消息偏移量等信息。

画面 8：
- IDE 界面：展示发送消息的代码，设置 topic 为 "my-topic-filter"，tag 为 "delete"，属性 "sex" 为 "女"，"age" 为 "18"。
- 控制台输出：显示异常信息，提示 Broker 不支持 SQL92 过滤。

画面 9：
- PDF 文档内容：说明原因是默认配置下不支持自定义属性过滤，需要设置配置项。
- 代码片段：`enablePropertyFilters=true`

画面 10：
- 终端界面：显示在 Docker 中重启 RocketMQ 服务的命令 `docker restart rmqbroker`。

画面 11：
- IDE 界面：展示发送消息的代码，设置 topic 为 "my-topic-filter"，tag 为 "delete"，属性 "sex" 为 "女"，"age" 为 "15"。
- 控制台输出：显示消费者接收到消息，但未打印出消息体，因为过滤条件不匹配。

画面 12：
- IDE 界面：展示发送消息的代码，设置 topic 为 "my-topic-filter"，tag 为 "delete"，属性 "sex" 为 "女"，"age" 为 "20"。
- 控制台输出：显示消费者接收到消息，但未打印出消息体，因为过滤条件不匹配。

画面 13：
- IDE 界面：展示消费者代码，订阅主题 "my-topic-filter"，使用 SQL 表达式 "sex='女' AND age=18" 进行过滤。
- 代码片段：`consumer.subscribe(topic: "my-topic-filter", MessageSelector.bySql("sex='女' AND age=18"));`

画面 14：
- PDF 文档内容：展示异常信息，提示 Broker 不支持 SQL92 过滤。
- 代码片段：`Exception in thread "main" org.apache.rocketmq.client.exception.MQClientException: CODE: 1 DESC: The broker does not support consumer to filter message by SQL92`

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
//完整匹配
consumer.subscribe("haoke_im_topic", "SEND_MSG");
//或匹配
consumer.subscribe("haoke_im_topic", ["SEND_MSG" || SEND_MSG1]);
```

画面 9：
```properties
#加入broker配置项过滤
enablePropertyFilters=true
```

画面 10：
```bash
docker restart rmqbroker
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1：
- PPT 标题：2.5. 消息过滤器
- 内容：RocketMQ 支持根据用户自定义属性进行过滤，过滤表达式类似 SQL 的 WHERE，如：a > 5 AND b = 'abc'

画面 6：
- 代码片段：`consumer.subscribe(topic: "my-topic-filter", MessageSelector.bySql("sex='女' AND age=18"));`

画面 13：
- 代码片段：`consumer.subscribe(topic: "my-topic-filter", MessageSelector.bySql("sex='女' AND age=18"));`

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
