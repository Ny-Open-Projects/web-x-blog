# 画面线理解：21_SpringBoot整合RabbitMQ-消费者

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\21_SpringBoot整合RabbitMQ-消费者_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:51, 01:10, 02:07, 02:48, 03:19, 03:38, 03:57, 04:36, 05:30, 05:56, 06:26, 07:11, 07:43, 08:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:43:23

1) 这一组画面整体在讲如何使用 Spring Boot 整合 RabbitMQ，创建生产者和消费者项目并实现消息发送与接收。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了生产者项目 `producer-springboot` 的结构，其中 `ProducerTest.java` 中使用 `RabbitTemplate` 发送消息到 `boot_haha` 队列，消息内容为 `"boot mq hello---"`。
画面2: 在 IDEA 中打开“Project Structure”对话框，配置模块的源码目录，`main` 和 `test` 目录被标记为源码和测试源码。
画面3: 在创建新模块时，选择 Spring Boot 2.1.7 版本，并在依赖中勾选了 `Spring Boot Web`、`Spring Boot Test`、`Spring Boot AMQP` 等依赖。
画面4: 展示了消费者项目 `consumer-springboot` 的 `pom.xml` 文件，其中 `<parent>` 指向 Spring Boot 2.1.7 的父项目，`<properties>` 定义了 Java 版本为 1.8。
画面5: 在 `pom.xml` 中添加了 `spring-boot-starter-amqp` 依赖。
画面6: 在 `pom.xml` 中添加了 `spring-boot-maven-plugin` 插件。
画面7: 打开 `application.properties` 文件，准备进行配置。
画面8: 创建 `RabbitMQListener.java` 类，准备编写监听器代码。
画面9: 在 `ConsumerSpringbootApplication.java` 中，`main` 方法调用 `SpringApplication.run` 启动应用。
画面10: 在 `RabbitMQListener` 类中，使用 `@RabbitListener(queues = "boot_queue")` 注解监听 `boot_queue` 队列，并在方法中打印消息体。
画面11: 运行 `ConsumerSpringbootApplicationTests` 测试类时，控制台报错，提示 `@SpringBootTest` 注解无法识别。
画面12: 运行 `ConsumerSpringbootApplication` 启动类，控制台显示应用启动成功，并接收到消息 `Body: mq hello`。
画面13: 在项目结构中，`consumer-springboot` 和 `producer-springboot` 两个模块并列显示。
画面14: PPT 标题为“1. SpringBoot 整合 RabbitMQ”，下方列出消费者开发步骤：1. 创建消费者 SpringBoot 工程；2. 引入 start 依赖坐标 `<dependency><groupId>org.springframework.boot</groupId><artifactId>spring-boot-starter-amqp</artifactId></dependency>`；3. 编写 yml 配置，基本信队配置；4. 定义监听类，使用 `@RabbitListener` 注解完成队列监听。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1:
```java
@SpringBootTest
@RunWith(SpringRunner.class)
public class ProducerTest {
    @Autowired
    private RabbitTemplate rabbitTemplate;

    @Test
    public void testSend() {
        rabbitTemplate.convertAndSend(RabbitMQConfig.EXCHANGE_NAME, routingKey: "boot_haha", object: "boot mq hello---");
    }
}
```

画面4:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.7.RELEASE</version>
        <relativePath/>
    </parent>
    <groupId>com.ithema</groupId>
    <artifactId>consumer-springboot</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>consumer-springboot</name>
    <description>Spring Boot project for Spring Boot</description>
    <properties>
        <java.version>1.8</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter</artifactId>
        </dependency>
    </dependencies>
</project>
```

画面5:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-amqp</artifactId>
</dependency>
```

画面6:
```xml
<plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
</plugin>
```

画面10:
```java
@Component
@RabbitListener(queues = "boot_queue")
public void listenerQueue(Message message) {
    System.out.println(message);
}
```

画面14:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-amqp</artifactId>
</dependency>
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面14:
标题: 1. SpringBoot 整合 RabbitMQ
内容:
消费者
1. 创建消费者 SpringBoot 工程
2. 引入 start 依赖坐标
   `<dependency><groupId>org.springframework.boot</groupId><artifactId>spring-boot-starter-amqp</artifactId></dependency>`
3. 编写 yml 配置，基本信队配置
4. 定义监听类，使用 `@RabbitListener` 注解完成队列监听

5) 无
