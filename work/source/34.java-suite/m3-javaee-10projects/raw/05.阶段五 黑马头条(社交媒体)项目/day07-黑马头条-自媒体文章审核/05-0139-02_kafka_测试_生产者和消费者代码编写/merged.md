# 02_kafka_测试_生产者和消费者代码编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\02_kafka_测试_生产者和消费者代码编写【海量资源尽在 666java.com】.mp4
- 时长 8分53秒（音频 533s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好刚才呢咱们是把这个封装啊都已经弄完了啊那下面咱们就来去写一段代码去测试一下那个测试怎么写呢咱们首先呢呃这个测试呢首先还是得有一个消息的生产者和消息的什么消费者是吧OK那这两个类咱们需要来编写一下啊那首先呢要测试的话呢咱们统一呢都是在其他的模块去测试啊因为comment下面呢是咱们并没有这个引导类啊
[00:28] 那行 那咱们下面就来去在admin端去测试一下因为admin端后面咱们要去用到所以说咱们在这儿先在这儿去测试一下那测试的话怎么测呢打开它首先你要想去测试的话再考虑几个事儿吧第一个你首先得有当前的卡普卡应用这个软件你首先在这儿在你这块
[00:55] 卡布卡的properties里边呢这个地址你要去设置上然后第二个呢就是你在这儿去编写这个测试类就可以了啊那编试类之前呢咱们首先呢在这儿还得去加上当前的配置也就是说咱们需要去加载当前的卡布卡的配置那这个怎么写是不是在这写一个卡布卡卡布卡config然后在上面去加一个东西叫什么configuration好下面是扫描啊把这个卡布卡的包扫描到啊
[01:29] 是什么com.kma common.cafka那这样就结束了下面咱们就来去写一段代码去测试一下打开当前的这个test在这再去创建一个包好吧cafka.test.cafka test然后咱们在这去集成一下测试Spring Boot test然后是
[02:05] runways,是吧sprintrunner.class好,那这样就结束了下面的话,咱们该怎么发消息呢?
[02:15] 在这儿是不是需要去注入一个什么?
[02:18] Kafka-templateprivate-Kafka-template用它就可以了咱们给一个范型,都是sprint然后它就是Kafka-template然后你直接注入进来就可以了
[02:36] 下面咱们就来去写一段测试public void test在上面去加一个方法加一个test然后在这你可以直接用前的卡不卡template.send它有一个send的方法send方里边它有三个参数第一个参数就是它的一个什么
[03:05] 就是前的消息的名称咱们可以设置一个比如说怎么叫topic.test好吧然后这个key呢其实你可以随便设随便设啊比如咱们随便写1.3key啊其实这个无所谓啊然后下面这个就是消息的内容消息的内容最终你要发送什么样的消息呢我们就写一个itcast好吧那这样这个呢就是咱们的消息的内容呃设置完之后啊
[03:33] 咱们这会儿需要去设置另外一块这是生产者是吧生产的消息那我的监听消息该怎么办我是消费者该怎么办呢这时候其实消费者他是自动监听自动监听所以说咱们在这再去创建一个类先创建一个包什么呢KafkaListenerKafkaListener0.8OK
[04:08] 然后呢然后这个是首先呢你得让他去让shrimp去管理是吧然后呢再往下的话咱们直接去让他让这个类啊去实现一个这叫什么叫Kafka利斯Kafka名字咱们来改一改啊这个要不然的话这个他继承的呢也是Kafka利斯的也是Kafka利斯的啊稍等啊名字不行啊咱们这样这样啊
[04:40] 咱们就把这个名字稍微改一改咱们在这去加一个在前面加一个test好吧然后加上之后咱们再这样咱们再去重写一下它的方法这写的有问题Kafkatest listener那这样的话就有了几个方法有了几个方法那几个方法咱们该用哪个呢
[05:21] 其实这个是接收消息的方法这个很重要这个其实就是消息的名称你要去指定消息的名称你直接去返回就可以了消息的名称是啥呢是不是写好了topical.test好,就把它给设置过来然后咱们就在这就可以去打印咱们的消息这个就是消息内容你可以在这去写一下就说
[05:52] 接收到的消息为前面吧接收到的消息为好然后下面呢把当前那个给打印一下就可以了那这样的话咱们就算是设置完了啊设置完之后啊当然这里边还有个方法是吧那这个方法咱们其实咱们用不着啊用不着咱们现在就可以不用它主要用的是当前的这个方法好吧行那这个设置完之后啊在咱们下面呢就来就来去设置一下就来去发个消息
[06:23] 那发烧机发烧机之前呢咱们还在还在这啊再去设置一部让他呢去试一会儿那的话呢保证当前这个监听类呢让Spring容器去管理明显呢能够接收到消息啊所以说咱们在这啊去加一个ThreadThread Sleep让他试一个试一会儿吧好吧无所谓啊试一会儿也行加个0这设置完之后啊咱们在这需要去Try Catch一下把这一行呢咱们也去
[06:57] 也放到这个try cache里边好然后呢咱们在这儿去打印句话在这儿去设置一下消息发送了好吧那下面呢咱们就来启动来测试一下啊稍等正在编译好来看一下啊稍等啊看看有没有报错有报错的话咱们就调一调看看有没有错误好真报错了是吧来看一下啊说呀咱们这有一个配置是他
[07:39] 那说是没有定义是吧没有定义的话咱们这样啊咱们在这啊因为咱们之前呢是说过在去讲丰庄的时候在这有一个配置要去读取咱们的配置文件在配置文件里边呢并没有所以说咱们在这啊先去给他取消了啊在当前的Kafka当前的这个东西这个里边config里边呢咱们可以把这一把这一行呢先去注掉啊先注掉啊暂时用不着啊咱们
[08:05] 任去在业务上发消息的时候咱们在这再去用啊到时候咱们再讲好吧你们测试的时候呢把这一行呢也给他住掉好吧然后这时候呢咱们再来去测试一下看看行不行好这次应该会快一些啊稍等看看有没有报错啊好像是没有问题看到了吧你看当前消息发送了然后下面的是消息啊具体消息咱们可以找一下那个itcast看这value是不是就是itcast点点点啊
[08:45] 没问题啊那这样的话咱们这个关于当前的Kafka的这种测试啊咱们就算是做完了啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 KafkaTemplate 发送消息并使用 @KafkaListener 监听消息，以及测试过程中遇到的配置问题和最终成功运行的场景。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示项目结构，当前选中的是 heima-leadnews-common 模块，目录结构包含 Kafka 包下的多个配置类。
画面 2: 切换到 heima-leadnews-admin 模块，展示其目录结构，包含 config、Controller、dao、Service 等包，以及 test 目录。
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
@ComponentScan("com.heima.common.Kafka")
public class KafkaConfig {
}
```

画面 4:
```java
package com.heima.admin.Kafka.test;

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
package com.heima.admin.Kafka;

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

