# 画面线理解：7.RocketMQ研究-Rocket基础-快速入门-生产者

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\7.RocketMQ研究-Rocket基础-快速入门-生产者【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:56, 01:25, 01:39, 02:17, 04:10, 04:40, 04:55, 05:17, 05:43, 06:24, 06:40, 07:07, 07:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 03:07:42

1) 这一组画面整体在讲如何使用 RocketMQ 实现同步消息发送，包括创建生产者工程、编写发送代码、编写测试类并运行测试，以及通过 RocketMQ 控制台查看消息发送结果。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程目录，当前选中“2.3.3.1 创建生产者工程”。
画面2：展示“日志收集”场景的交互流程图，包含“log”、“消息队列”、“日志需求服务一”、“日志需求服务二”四个节点，其中“log”指向“消息队列”，“消息队列”指向“日志需求服务一”和“日志需求服务二”。
画面3：展示项目结构，包含“src/main/java/com/shanjiuyu/test/rocketmq/message”和“src/main/resources/application.yml”。
画面4：展示“ProducerSimple.java”文件内容，包含“@Component”注解和空的类体。
画面5：在“ProducerSimple.java”中导入“org.springframework.beans.factory.annotation.Autowired;”并使用“@Autowired”注解注入“RocketMQTemplate”。
画面6：在“ProducerSimple.java”中定义“public void sendSyncMsg(String topic, String msg)”方法，并调用“rocketMQTemplate.syncSend(...)”。
画面7：在项目结构中选中“src/main/java/com/shanjiuyu/test/rocketmq/message”包。
画面8：在“ProducerSimpleTest.java”中导入“org.springframework.boot.test.context.SpringBootTest”。
画面9：在“ProducerSimpleTest.java”中定义“@Autowired”注解注入“ProducerSimple”。
画面10：在“ProducerSimpleTest.java”中定义“@Test”注解的“public void testSendSyncMsg()”方法，并调用“producerSimple.sendSyncMsg(...)”。
画面11：在控制台中执行“mvn spring-boot:run”命令，启动应用。
画面12：在“ProducerSimpleTest.java”中执行“producerSimple.sendSyncMsg(...)”，并出现“Illegal base64 character 2e”错误。
画面13：展示 RocketMQ 控制台，包含“Broker TOP 10”和“Topic TOP 10”图表。
画面14：在“ProducerSimpleTest.java”中执行“producerSimple.sendSyncMsg(...)”，并出现“Invalid VCS root mapping”错误。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```yaml
server:
  port: 8192 #服务端口
spring:
  context-path: /rocketmq-consumer
application:
  name: rocketmq-producer #指定服务名
rocketmq:
  nameServer: 127.0.0.1:9876
```

画面5：
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.apache.rocketmq.spring.core.RocketMQTemplate;
```

画面6：
```java
public void sendSyncMsg(String topic, String msg) {
    rocketMQTemplate.syncSend(...);
}
```

画面8：
```java
import org.springframework.boot.test.context.SpringBootTest;
```

画面9：
```java
@Autowired
ProducerSimple producerSimple;
```

画面10：
```java
@Test
public void testSendSyncMsg() {
    producerSimple.sendSyncMsg(...);
}
```

画面11：
```bash
mvn spring-boot:run
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：
- 标题：2、应用程序解耦合
- 标题：3）日志收集
- 流程图：
  - “log”指向“消息队列”
  - “消息队列”指向“日志需求服务一”
  - “消息队列”指向“日志需求服务二”

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。
