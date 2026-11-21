# 画面线理解：6.RocketMQ研究-Rocket基础-快速入门-创建工程

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\6.RocketMQ研究-Rocket基础-快速入门-创建工程【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:45, 01:31, 02:07, 02:32, 03:04, 03:41, 04:10, 04:59, 05:22, 05:50, 06:16, 07:00, 07:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 03:07:14

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中创建 RocketMQ 生产者和消费者工程，并配置相关依赖和启动类。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示课程文档目录，当前章节为“2.3.3 生产者工程”，内容为“2.3.2 消息结构”，介绍消息的基础属性（topic、消息体、消息 Flag）和扩展属性（tag、keys、waitStoreMsgOK）。
画面 2：在 IntelliJ IDEA 中打开“Project Structure”对话框，准备为项目添加新模块，当前选中“shanjupay-payment-agent-service”模块。
画面 3：在“Project Structure”中，选中“test-rocketmq”模块，显示其源码路径为“F:\teach\shanjupay\model\code\shanjupay\test-rocketmq”。
画面 4：展示课程文档目录，当前章节为“2.3.4 消费者工程”，内容为“1.1 MQ的应用场景”，图示传统同步调用与异步处理的对比。
画面 5：在 IntelliJ IDEA 中，弹出“New Module”对话框，模块名为“test-rocketmq”，路径为“F:\teach\shanjupay\model\code\shanjupay\test-rocketmq”。
画面 6：展示课程文档目录，当前章节为“2.3.3.1 创建生产者工程”，内容为“2）创建rocketmq-producer生产者工程”，并显示了 Maven 依赖配置，其中包含 RocketMQ 和 Spring Boot 的 starter。
画面 7：在 IntelliJ IDEA 中，打开“test-rocketmq”项目的 pom.xml 文件，显示了 Maven 依赖配置，其中包含 RocketMQ 和 Spring Boot 的 starter。
画面 8：在 IntelliJ IDEA 中，右键点击“rocketmq-producer”模块，选择“Refactor” -> “Rename”。
画面 9：展示课程文档目录，当前章节为“2.3.3.2 发送同步消息”，内容为“3）新建rocketmq-producer工程的application.yml文件”，并显示了 application.yml 配置文件内容。
画面 10：展示课程文档目录，当前章节为“2.3.3.2 发送同步消息”，内容为“3）新建rocketmq-producer工程的application.yml文件”，并显示了 application.yml 配置文件内容，其中 server.port 为 8181，spring.application.name 为 rocketmq-producer。
画面 11：在 IntelliJ IDEA 中，打开“rocketmq-producer”模块的“src/main/java”目录，显示了“ProducerApplication.java”文件。
画面 12：在 IntelliJ IDEA 中，右键点击“ProducerApplication.java”文件，选择“Run 'ProducerApplication'”。
画面 13：展示课程文档目录，当前章节为“2.3.3.2 发送同步消息”，内容为“4）新建启动类”，并显示了 ProducerApplication.java 的代码。
画面 14：展示课程文档目录，当前章节为“2.3.4.2 消费消息”，内容为“3、配置文件application.yml”，并显示了 application.yml 配置文件内容，其中 server.port 为 8182，spring.application.name 为 rocketmq-consumer。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 6 的 YAML 配置：
```xml
<version>1.0-SNAPSHOT</version>
<parent>
    <artifactId>test-rocketmq</artifactId>
    <modelVersion>4.0.0</modelVersion>
    <packaging>pom</packaging>
</parent>
<dependencies>
    <dependency>
        <groupId>org.apache.rocketmq</groupId>
        <artifactId>rocketmq-spring-boot-starter</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>
```
画面 9 的 YAML 配置：
```yaml
server:
  port: 8181 #服务端口
  servlet:
    context-path: /rocketmq-producer

spring:
  application:
    name: rocketmq-producer #指定服务名
  rocketmq:
    nameServer: 127.0.0.1:9876
    producer:
      group: demo-producer-group
```
画面 13 的 Java 代码：
```java
@SpringBootApplication
public class ProducerApplication {
    public static void main(String[] args) {
        SpringApplication.run(ProducerApplication.class, args);
    }
}
```
画面 14 的 YAML 配置：
```yaml
server:
  port: 8182 #服务端口
  servlet:
    context-path: /rocketmq-consumer

spring:
  application:
    name: rocketmq-consumer #指定服务名
  rocketmq:
    nameServer: 127.0.0.1:9876
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 4 的架构图：
- “订单服务”指向“仓储服务”。
- “仓储服务”指向“订单服务”。
- “订单服务”指向“仓储服务”。
- “仓储服务”指向“订单服务”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
