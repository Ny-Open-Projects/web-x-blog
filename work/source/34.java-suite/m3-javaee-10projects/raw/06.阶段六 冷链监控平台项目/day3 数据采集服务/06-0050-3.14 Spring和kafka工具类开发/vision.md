# 画面线理解：3.14 Spring和kafka工具类开发

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day3 数据采集服务
- 源文件：06.阶段六 冷链监控平台项目\day3 数据采集服务\3.14 Spring和kafka工具类开发_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:14, 00:23, 00:46, 01:01, 01:34, 01:44, 02:02, 02:39, 02:53, 03:08, 03:26, 03:46, 04:04, 04:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:10:12

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 KafkaTemplate 发送消息，并通过 SpringContextUtils 工具类获取 Spring 容器中的 Bean。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构，选中 Client.java，代码中包含创建客户端连接和生成模拟数据的逻辑。
画面2：右键点击 Client.java，弹出菜单，准备进行操作。
画面3：打开 KafkaSender.java 文件，开始编写 Kafka 生产者代码。
画面4：在 KafkaSender 类中，使用 @Component 注解，并引入 KafkaTemplate。
画面5：在 KafkaSender 类中，使用 @Autowired 注解注入 KafkaTemplate。
画面6：在 KafkaSender 类中，定义私有成员变量 kafkaTemplate。
画面7：在 KafkaSender 类中，调用 kafkaTemplate.send() 方法发送消息。
画面8：打开 SpringContextUtils.java 文件，准备编写工具类。
画面9：在 SpringContextUtils 类中，实现 ApplicationContexAware 接口。
画面10：在 SpringContextUtils 类中，声明静态变量 applicationContext。
画面11：在 SpringContextUtils 类中，编写 setApplicationContext 方法。
画面12：在 SpringContextUtils 类中，编写 getBean 方法。
画面13：在 SpringContextUtils 类中，完成 getBean 方法的实现。
画面14：在 SpringContextUtils 类中，完成代码编写，类上添加 @Component 注解。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public static void main(String[] args) {
    // 建立客户端
    new Client("127.0.0.1", "port 10010").connect();
    // 产生模拟的请求数据
    private String getMsg(String meterCode) {
        MessageEntity me = new MessageEntity();
        me.setMetercode(meterCode);
        // 设置随机值
        me.setTemperature(Random(-100, 100));
        // 设置随机湿度
    }
```

画面3：
```java
package com.ithima.netty.demo.common;

import org.springframework.stereotype.Component;

@Component
public class KafkaSender {
```

画面4：
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Component;

@Component
public class KafkaSender {
    @Autowired
    private KafkaTemplate<String, String> kafkaTemplate;
```

画面5：
```java
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.support.SendResult;
import org.springframework.util.concurrent.ListenableFuture;
import org.springframework.util.concurrent.ListenableFutureCallback;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework.util.concurrent.ListenableFutureTask;
import org.springframework
