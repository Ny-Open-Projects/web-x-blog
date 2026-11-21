# 画面线理解：02_kafka_测试_生产者和消费者代码编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\02_kafka_测试_生产者和消费者代码编写【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:22, 01:05, 01:47, 02:26, 02:48, 04:11, 05:08, 05:32, 06:21, 07:14, 07:33, 07:50, 08:24, 08:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:15:39

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 KafkaTemplate 发送消息并使用 @KafkaListener 监听消息，以及测试过程中遇到的配置问题和最终成功运行的场景。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示项目结构，当前选中的是 heima-leadnews-common 模块，目录结构包含 kafka 包下的多个配置类。
画面 2: 切换到 heima-leadnews-admin 模块，展示其目录结构，包含 config、controller、dao、service 等包，以及 test 目录。
画面 3: 打开 KafkaConfig.java 文件，显示其包名和注解 @Configuration 与 @ComponentScan。
画面 4: 打开 KafkaTest.java 文件，显示其包名和注解 @SpringBootTest 与 @RunWith(SpringRunner.class)。
画面 5: 在 KafkaTest.java 中，定义了 private KafkaTemplate<String, String> kafkaTemplate; 字段。
画面 6: 在 KafkaTest.java 中，定义了 public void test() 方法。
画面 7: 打开 TestKafkaListener.java 文件，显示其包名和注解 @Component。
画面 8: 在 TestKafkaListener.java 中，定义了 public String topic() 方法。
画面 9: 在 TestKafkaListener.java 中，定义了 public void onMessage(ConsumerRecord data, Consumer consumer) 方法。
画面 10: 在 KafkaTest.java 中，添加了 try-catch 块，并在 catch 块中添加了 e.printStackTrace();。
画面 11: 运行测试，控制台显示测试失败，错误信息为 PropertyPlaceholderHelper.replacePlaceholders。
画面 12: 切换回 KafkaTest.java，显示测试失败的错误信息。
画面 13: 运行测试，控制台显示测试成功，日志信息显示 Spring Boot 启动成功。
画面 14: 运行测试，控制台显示测试成功，日志信息显示 KafkaTest.test() 方法执行成功。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```java
package com.heima.admin.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan("com.heima.common.kafka")
public class KafkaConfig {
}
```

画面 4:
```java
package com.heima.admin.kafka.test;

import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner.class;

@SpringBootTest
@RunWith(SpringRunner.class)
public class KafkaTest {
}
```

画面 5:
```java
private KafkaTemplate<String, String> kafkaTemplate;
```

画面 6:
```java
public void test() {
}
```

画面 7:
```java
package com.heima.admin.kafka;

import org.springframework.stereotype.Component;

@Component
public class TestKafkaListener implements KafkaListener {
}
```

画面 8:
```java
public String topic() {
    return "topic.test";
}
```

画面 9:
```java
public void onMessage(ConsumerRecord data, Consumer consumer) {
    System.out.println("接收到的消息为===" + data);
}
```

画面 10:
```java
try {
    kafkaTemplate.send("topic.test", "123KEY", "itcast...");
    System.out.println("消息发送了");
    Thread.sleep(500000);
} catch (InterruptedException e) {
    e.printStackTrace();
}
```

画面 11:
```
Tests failed: 1 of 1 tests
at org.springframework.util.PropertyPlaceholderHelper.replacePlaceholders(PropertyPlaceholderHelper.java:104)
at org.springframework.boot.context.properties.bind.PropertySourcesPlaceholderResolver.resolvePlaceholders(PropertySourcesPlaceholderResolver.java:325)
at org.springframework.boot.context.properties.bind.Binder.bind(Binder.java:285)
at org.springframework.boot.context.properties.bind.Binder.bind(Binder.java:320)
...
Process finished with exit code -1
```

画面 12:
```
Tests failed: 1 of 1 tests
at org.springframework.boot.context.properties.bind.Binder.bind(Binder.java:130)
at org.springframework.boot.context.properties.ConfigurationPropertiesBinder.bind(ConfigurationPropertiesBinder.java:80)
at org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker.postProcessAfterInitialization(PostProcessorRegistrationDelegate.java:231)
...
```

画面 13:
```
2019-10-09 10:00:24,788  INFO main [org.springframework.boot.logging.LoggingApplicationListener] Logging initialized using 'class org.apache.ibatis.logging.stdout.StdOutImpl'
2019-10-09 10:00:28,890  INFO main [org.springframework.data.repository.config.RepositoryConfigurationDelegate] registerRepositoryConfiguration
2019-10-09 10:00:30,239  INFO main [org.springframework.data.repository.config.RepositoryConfigurationDelegate] multipleStoresDetected
2019-10-09 10:00:30,239  INFO main [org.springframework.data.repository.config.RepositoryConfigurationDelegate] multipleStoresDetected
2019-10-09 10:00:30,239  INFO main [org.springframework.data.repository.config.RepositoryConfigurationDelegate] multipleStoresDetected
2019-10-09 10:00:30,239  INFO main [org.springframework.data.repository.config.RepositoryConfigurationDelegate] multipleStoresDetected
2019-10-09 10:00:30,239  INFO main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] postProcessAfterInitialization
2019-10-09 10:00:30,239  INFO main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] postProcessAfterInitialization
2019-10-09 10:00:30,239  INFO main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] postProcessAfterInitialization
2019-10-09 10:00:30,239  INFO main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] postProcessAfterInitialization
2019-10-09 10:00:30,239  INFO main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] postProcessAfterInitialization
2019-10-09 10:00:30,239  INFO main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] postProcessAfterInitialization
2019-10-09 10:00:30,239  INFO main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] postProcessAfterInitialization
2019-10-09 10:00:30,239  INFO main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] postProcessAfterInitialization
2019-10-09 10:00:30,239  INFO main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] postProcessAfterInitialization
2019-10-09 10:00:30,239  INFO main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] postProcessAfterInitialization
2019-10-09 10:00:30,239  INFO main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] postProcessAfterInitialization
2019-10-09 10:00:30,239  INFO main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] postProcessAfterInitialization
2019-10-09 10:00:30,239  INFO main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] postProcessAfterInitialization
2019-10-09 10:00:30,239  INFO main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] postProcessAfterInitialization
2019-10-09 10:00:30,239  INFO main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] postProcessAfterInitialization
2019-10-09 10:00:30,239  INFO main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] postProcessAfterInitialization
2019-10-09 10:00:30,239  INFO main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] postProcessAfterInitialization
2019-10-09 10:00:30,239  INFO
