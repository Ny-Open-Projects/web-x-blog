# 画面线理解：03_高级特性-消息可靠投递-return

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/2.RabbitMQ第二天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\2.RabbitMQ第二天\03_高级特性-消息可靠投递-return_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:17, 00:42, 02:39, 03:03, 03:39, 04:04, 04:16, 04:49, 06:02, 06:20, 07:12, 07:21, 08:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:45:52

1) 这一组画面整体在讲什么（一句话）：
讲解 RabbitMQ 消息的可靠投递机制，包括 confirm 确认模式和 return 返回模式的实现与配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：PPT 标题为“1.1 消息的可靠投递”，介绍 RabbitMQ 提供的 confirm 和 return 两种可靠投递模式，以及消息传递路径：producer → rabbitmq broker → exchange → queue → consumer。
画面 2：展示 Java 代码，定义 RabbitTemplate 的 confirmCallback，用于处理消息发送到 exchange 后的确认回调。
画面 3：展示 Java 代码，定义 testReturn 方法，用于测试 return 模式。
画面 4：展示 spring-rabbitmq-producer.xml 配置文件，定义了 ConnectionFactory、RabbitTemplate、队列和交换机的配置，其中 publisher-confirms 和 publisher-returns 属性被设置为 true。
画面 5：展示 Java 代码，注释说明 return 模式的工作原理，并开始编写 testReturn 方法。
画面 6：展示 Java 代码，设置 RabbitTemplate 的 ReturnCallback，并调用 convertAndSend 方法发送消息。
画面 7：展示 Java 代码，测试方法 testReturn 已执行，测试通过。
画面 8：展示 Java 代码，测试方法 testReturn 已执行，测试通过。
画面 9：展示 Java 代码，设置 RabbitTemplate 的 mandatory 属性为 true，以启用 return 模式。
画面 10：展示 Java 代码，设置 RabbitTemplate 的 mandatory 属性为 true，测试方法 testReturn 已执行，测试通过。
画面 11：展示 Java 代码，注释说明 ReturnCallback 的参数含义。
画面 12：展示 Java 代码，测试方法 testReturn 已执行，测试通过。
画面 13：展示 Java 代码，测试方法 testReturn 已执行，测试通过。
画面 14：PPT 标题为“1.1 消息的可靠投递小结”，总结了设置 publisher-confirms 和 publisher-returns 为 true，使用 setConfirmCallback 和 setReturnCallback 方法，以及 RabbitMQ 的事务机制（txSelect, txCommit, txRollback）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4 的 XML 配置：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/context"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:rabbit="http://www.springframework.org/schema/rabbit"
       xsi:schemaLocation="http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd
       http://www.springframework.org/schema/rabbit http://www.springframework.org/schema/rabbit/spring-rabbit.xsd">

    <context:property-placeholder location="classpath:rabbitmq.properties"/>

    <!-- 定义rabbit连接工厂 -->
    <rabbit:connection-factory id="connectionFactory" host="172.16.98.133"
                               port="5672"
                               username="guest"
                               password="guest"
                               virtual-host="/"
                               publisher-confirms="true"
                               publisher-returns="true"/>

    <!-- 定义rabbitTemplate，用于发送消息 -->
    <rabbit:template id="rabbitTemplate" connection-factory="connectionFactory"/>

    <!-- 消息可靠投递（生产者）-->
    <rabbit:queue id="test_queue_confirm" name="test_queue_confirm"/>
    <rabbit:direct-exchange name="test_exchange_confirm"/>
    <rabbit:bindings>
        <rabbit:binding queue="test_queue_confirm" key="confirm"/>
    </rabbit:bindings>
    <rabbit:direct-exchange name="test_exchange_confirm"/>
</beans>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1 的 PPT 标题：
1. RabbitMQ 高级特性
1.1 消息的可靠投递

画面 14 的 PPT 标题：
1. RabbitMQ 高级特性
1.1 消息的可靠投递小结

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
