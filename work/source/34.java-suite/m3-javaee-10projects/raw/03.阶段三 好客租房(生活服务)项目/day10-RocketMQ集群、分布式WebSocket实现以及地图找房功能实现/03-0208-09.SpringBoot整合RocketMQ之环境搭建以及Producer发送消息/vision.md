# 画面线理解：09.SpringBoot整合RocketMQ之环境搭建以及Producer发送消息

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\09.SpringBoot整合RocketMQ之环境搭建以及Producer发送消息【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:56, 02:13, 03:01, 04:00, 04:46, 05:43, 07:05, 07:41, 08:25, 09:17, 10:02, 10:41, 11:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:16:30

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中集成 RocketMQ，包括添加依赖、配置属性、编写生产者代码并进行单元测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 页面“3.1、导入依赖”，并显示了 Maven 的父项目配置，其中 `<version>2.1.0.RELEASE</version>`。
画面2：展示 PPT 页面“3.1、导入依赖”，并显示了添加的 RocketMQ 依赖，包括 `itcast-rocketmq` 和 `spring-boot-starter`。
画面3：展示 PPT 页面“3.1、导入依赖”，并显示了 Maven 的 `<build>` 部分，其中 `<plugin>` 为 `maven-compiler-plugin`，配置 `<source>1.8</source>` 和 `<target>1.8</target>`。
画面4：展示 IntelliJ IDEA 中的 `application.properties` 文件，配置了 Spring Boot 应用名和 RocketMQ 的 NameServer 地址。
画面5：展示 IntelliJ IDEA 中的 `application.properties` 文件，配置了 Spring Boot 应用名和 RocketMQ 的 NameServer 地址。
画面6：展示 IntelliJ IDEA 中的 `SpringProducer.java` 文件，定义了 `@Component` 注解的类，并声明了 `@Autowired` 的 `RocketMQTemplate` 成员变量。
画面7：展示 IntelliJ IDEA 中的 `SpringProducer.java` 文件，为 `sendMsg` 方法添加了 `this.rocketMQTemplate.convertAndSend(payload: "spring-my-topic");` 语句。
画面8：展示 IntelliJ IDEA 中的 `SpringProducer.java` 文件，为 `sendMsg` 方法添加了 `@param topic` 和 `@param msg` 注释。
画面9：展示 IntelliJ IDEA 中的 `TestSpringRocketMQ.java` 文件，开始编写测试类，使用 `@RunWith(SpringRunner.class)` 和 `@SpringBootTest` 注解。
画面10：展示 IntelliJ IDEA 中的 `TestSpringRocketMQ.java` 文件，声明了 `private SpringProducer springProducer;` 成员变量。
画面11：展示 IntelliJ IDEA 中的 `TestSpringRocketMQ.java` 文件，完成 `@Test` 方法的声明。
画面12：展示 IntelliJ IDEA 中的 `TestSpringRocketMQ.java` 文件，编写了 `testSendMsg` 方法，调用 `springProducer.sendMsg` 发送消息，并在控制台输出“发送成功”。
画面13：展示 IntelliJ IDEA 中的 `SpringProducer.java` 文件，为 `sendMsg` 方法添加了 `this.rocketMQTemplate.sy` 语句（未完成）。
画面14：展示 IntelliJ IDEA 中的 `SpringProducer.java` 文件，为 `sendMsg` 方法添加了 `this.rocketMQTemplate.sy` 语句（未完成）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
        http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.0.RELEASE</version>
    </parent>
```

画面2：
```xml
<dependency>
    <groupId>cn.itcast.rocketmq</groupId>
    <artifactId>itcast-rocketmq</artifactId>
    <version>1.0-SNAPSHOT</version>
</dependency>
```

画面3：
```xml
<build>
    <plugins>
        <!-- java编译插件 -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.2</version>
            <configuration>
                <source>1.8</source>
                <target>1.8</target>
                <encoding>UTF-8</encoding>
            </configuration>
        </plugin>
    </plugins>
</build>
```

画面4：
```properties
# Spring boot application
spring.application.name = itcast-rocketmq
spring.rocketmq.nameServer=172.16.55.185:9876
spring.rocketmq.producer.group=my-group
```

画面6：
```java
package cn.itcast.rocketmq.spring;

import org.apache.rocketmq.spring.core.RocketMQTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class SpringProducer {
    // 注入RocketMQ的模板
    @Autowired
    private RocketMQTemplate rocketMQTemplate;
}
```

画面7：
```java
public void sendMsg() {
    this.rocketMQTemplate.convertAndSend(payload: "spring-my-topic");
}
```

画面8：
```java
/**
 * 发送消息
 * @param topic
 * @param msg
 */
public void sendMsg(String topic, String msg) {
    this.rocketMQTemplate.convertAndSend(topic, msg);
}
```

画面9：
```java
package cn.itcast.rocketmq.spring;

import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class TestSpringRocketMQ {
```

画面10：
```java
private SpringProducer springProducer;
```

画面12：
```java
@Test
public void testSendMsg() {
    String msg = "我的第一个SpringRocketMQ消息！";
    this.springProducer.sendMsg(topic: "spring-my-topic", msg);
    System.out.println("发送成功");
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“3.1、导入依赖”。
画面2：PPT 标题为“3.1、导入依赖”。
画面3：PPT 标题为“3.1、导入依赖”。
画面4：无 PPT 标题。
画面5：无 PPT 标题。
画面6：无 PPT 标题。
画面7：无 PPT 标题。
画面8：无 PPT 标题。
画面9：无 PPT 标题。
画面10：无 PPT 标题。
画面11：无 PPT 标题。
画面12：无 PPT 标题。
画面13：无 PPT 标题。
画面14：无 PPT 标题。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
