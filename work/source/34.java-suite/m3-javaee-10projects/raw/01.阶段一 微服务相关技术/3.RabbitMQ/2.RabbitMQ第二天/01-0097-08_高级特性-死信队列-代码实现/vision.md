# 画面线理解：08_高级特性-死信队列-代码实现

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/2.RabbitMQ第二天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\2.RabbitMQ第二天\08_高级特性-死信队列-代码实现_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:14, 02:32, 03:47, 04:41, 05:10, 06:57, 08:39, 09:59, 11:30, 12:01, 14:36, 15:54, 17:22, 18:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:48:45

1) 这一组画面整体在讲什么（一句话）：
讲解 RabbitMQ 死信队列的配置方法，包括如何通过 XML 配置文件设置队列的死信交换机和路由键。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PPT 标题“1.5 死信队列”，并说明“队列绑定死信交换机：给队列设置参数：x-dead-letter-exchange 和 x-dead-letter-routing-key”。
画面 2: 展示 RabbitMQ 管理界面，列出队列 test_queue_confirm 和 test_queue_ttl，并在下方显示“Add a new queue”表单。
画面 3: 展示 IDE 中的 XML 配置文件 spring-rabbitmq-producer.xml，其中包含用于创建正常队列和死信队列的配置片段。
画面 4: 展示 IDE 中的 XML 配置文件，光标位于创建死信队列的配置部分。
画面 5: 展示 IDE 中的 XML 配置文件，光标位于配置死信队列的 arguments 部分。
画面 6: 展示 IDE 中的 XML 配置文件，高亮显示死信队列的 arguments 配置，其中包含 x-dead-letter-exchange 和 x-dead-letter-routing-key。
画面 7: 展示 RabbitMQ 管理界面，显示“Arguments”配置项，包括 x-dead-letter-exchange 和 x-dead-letter-routing-key。
画面 8: 展示 IDE 中的 XML 配置文件，光标位于配置死信队列的 arguments 部分。
画面 9: 展示 RabbitMQ 管理界面，显示队列 queue_dlx、test_queue_confirm、test_queue_dlx 和 test_queue_ttl。
画面 10: 展示 IDE 中的测试类 ProducerTest，显示测试通过，终端输出“Tests passed: 1 of 1 test”。
画面 11: 展示 IDE 中的消费者监听器类 DlxListener，其中包含注释说明其功能。
画面 12: 展示 RabbitMQ 管理界面，显示队列 queue_dlx、test_queue_confirm、test_queue_dlx 和 test_queue_ttl。
画面 13: 展示 RabbitMQ 管理界面，显示队列 queue_dlx、test_queue_confirm、test_queue_dlx 和 test_queue_ttl。
画面 14: 展示 PPT 结束页，显示“黑马程序员”和“www.itheima.com”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```xml
<rabbit:topic-exchange name="test_exchange_ttl">
    <rabbit:bindings>
        <rabbit:binding pattern="ttl.*" queue="test_queue_ttl"/>
    </rabbit:bindings>
</rabbit:topic-exchange>

<!-- 正常队列 -->
<rabbit:queue name="test_queue_ttl" id="test_queue_ttl">
    <rabbit:queue-arguments>
        <entry key="x-dead-letter-exchange" value="exchange_dlx" />
        <entry key="x-dead-letter-routing-key" value="dlx.hehe" />
    </rabbit:queue-arguments>
</rabbit:queue>
```

画面 4:
```xml
<rabbit:queue name="test_queue_dlx" id="test_queue_dlx">
    <rabbit:queue-arguments>
        <entry key="x-dead-letter-exchange" value="exchange_dlx" />
        <entry key="x-dead-letter-routing-key" value="dlx.hehe" />
    </rabbit:queue-arguments>
</rabbit:queue>
```

画面 5:
```xml
<rabbit:queue name="test_queue_dlx" id="test_queue_dlx">
    <rabbit:queue-arguments>
        <entry key="x-dead-letter-exchange" value="exchange_dlx" />
        <entry key="x-dead-letter-routing-key" value="dlx.hehe" />
    </rabbit:queue-arguments>
</rabbit:queue>
```

画面 6:
```xml
<rabbit:queue name="test_queue_dlx" id="test_queue_dlx">
    <rabbit:queue-arguments>
        <entry key="x-dead-letter-exchange" value="exchange_dlx" />
        <entry key="x-dead-letter-routing-key" value="dlx.hehe" />
    </rabbit:queue-arguments>
</rabbit:queue>
```

画面 8:
```xml
<rabbit:queue name="test_queue_dlx" id="test_queue_dlx">
    <rabbit:queue-arguments>
        <entry key="x-dead-letter-exchange" value="exchange_dlx" />
        <entry key="x-dead-letter-routing-key" value="dlx.hehe" />
    </rabbit:queue-arguments>
</rabbit:queue>
```

画面 11:
```java
@Component
public class DlxListener implements ChannelAwareMessageListener {
    @Override
    public void onMessage(Message message, Channel channel) throws Exception {
        // 消费者处理消息
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题“1.5 死信队列”，下方文字“队列绑定死信交换机：给队列设置参数：x-dead-letter-exchange 和 x-dead-letter-routing-key”。
画面 3: 架构图显示 Producer → Exchange → Queue → Consumer1 和 Consumer2，其中 Queue 指向红色的 Dead Letter Exchange，标注“消息成为死信”。
画面 7: 表格数据包括队列名称、状态、Ready、Unacked、Total 等列。
画面 9: 表格数据包括队列名称、状态、Ready、Unacked、Total 等列。
画面 12: 表格数据包括队列名称、状态、Ready、Unacked、Total 等列。
画面 13: 表格数据包括队列名称、状态、Ready、Unacked、Total 等列。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
