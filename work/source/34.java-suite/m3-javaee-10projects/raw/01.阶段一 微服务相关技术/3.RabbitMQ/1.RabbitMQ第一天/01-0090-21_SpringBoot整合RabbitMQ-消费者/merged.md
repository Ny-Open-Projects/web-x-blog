# 21_SpringBoot整合RabbitMQ-消费者

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\21_SpringBoot整合RabbitMQ-消费者_【海量资源尽在 ubkz.com】.mp4
- 时长 8分58秒（音频 538s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 介绍完Spring Boot整合RabbitMQ的生产者代码编写那么下来呢我们来介绍消费者这一段的代码编写那么这个呢步骤极其类似前面第一步还是创建一个Spring Boot的工程第二步引入依赖的坐标还是一样的坐标第三个呢编写YAML的配置文件还是那个配置文件还是那些配置的信息那么最后一步比较不一样它需要定义一个监听类
[00:28] 那么这个监听类里边我们定义很多的监听方法在方法上我们用RabbitListener来完成监听当然这个RabbitListener里边要配置你监听哪个队列将来那个队列里边消息一旦收到了之后你这个方法里边的方法体就会被自动的执行来完成消息的处理那么介绍完步骤之后我们来完成一下代码的编写那么首先呢我们来创建一个工程吧稍等加一个这么一个模块
[00:58] Mayweather的项目好Mayweather的项目呢我们在这com这样吧那么这一次呢我们就不加Mayweather的项目了我们来加一个对应的Spring Boot的这么一个项目加一个Spring Boot的项目这个SpringInniterLaser好那么当然呢它可以通过这个网址的方式来构建你可以自定义构建我们就自定义通过网址的方式来构建了你记得可以选择1.8没有问题下一步好这个地方呢就会非常方便
[01:28] 你com.it黑码然后呢artifact id呢我们就起名为consumer-对应的一个叫做sprintboot没问题吧好然后呢你是用maywen呢还是用啥我们就用maywen的方式好用maywen的方式maywen的一个项目那么这些都是没有问题的那么再下一步他说你需要选择什么依赖吗对吧
[01:58] 选择什么依赖呀我们选择AMQPQP的一个依赖有没有呢我们搜一下好像这个玩意儿呢好像还没有搜到是吧AMQQP没有搜到没有搜到没有关系我们在这里边web这是web的然后呢web的其实呢我们现在不需要不需要然后呢这个地方呢有没有一个AMQP里边的好像这里边没有提供默认的这个选项那这个呢我们也不需要了我们下一步就可以了
[02:27] 下一步之后呢这个名字也给我定义好了我们finish好稍等一下它需要去下载对应的一些东西弄完了之后呢apply ok你看我这个consumer的工程是不是就创建好了创建好了之后呢好这些文件我都没有忽略所以它都会出现我们来主要看这个地方这个地方呢你看一下它的parent这个地方是不是帮你弄好了呀复工程是不是ok了那么这个复工程的版本好像跟我们的版本好像跟consumer
[02:57] Producer这个版本不太一样2.1.4我这是它那个地方呢好像用的是2.1.7但是呢我们为了统一期间我们这个地方都弄成2.1.4好嘞这个也做完了之后呢下边的这些东西啊反正没啥用我都把它删掉好然后呢对应的Java的版本它都给你定义了好然后呢Spring Boot这个Starter这个好像我们没有用这个呢Test我们也没有用对吧
[03:25] 我们都没有用的话呢我们把对应的AMQP的那个给它复制进来是不是这个复制进来就可以了复制进来之后呢这样这个就创建好了这么一个依赖的关系那么下面这些插件我们也可以不用管它那么这样呢我们的Maven坐标就OK了然后主要看这个地方我们看一下它自己会把这个启动类帮我们写好对吧很方便的而且呢对应的YAML配置文件它用的Proportes的那么这样我们给它改个名
[03:55] 好refactor rename一下我们不用properties的我们用yaml的方式对吧yaml的方式呢里边内容呢我就不再去编写了当然这个地方想写一下也是可以的然后我们直接把这里边的内容给它复制过来没问题吧这样复制完了之后好那么我们这个配置也写完了写完了之后呢接下来我就可以来定义这么一个监听的类了对吧定义监听类呢非常简单我们在里边定义一个这样吧
[04:24] 我们定义一个就在这上面写吧我就不单独分包了我们就写一个叫做RabbitMQ的listenerlistener这个listener呢当然要称为一个complement对应的一个bin被sprint所识别那么我们在这里边写一个方法叫做public void比如说我们叫做监听叫做一个
[04:53] Listener listener queue监听一个对列监听哪个对列呢其实我们可以写出来当然这个名写不写都是可以的方法名而已那么这玩意弄完了之后弄完了之后稍等方法定义出来了之后我们在这个地方要加一个注解这个很关键Rabbit listener你里边要指定对应的一个queue的名称这个queue的名称就是刚才我们监听的定义的那个对列的名称
[05:22] 我们找这个名以防我们写错了在这个configure里边我们是定义了个boot queue好找到它找到它之后呢我们在这里边呢找到这个地方粘过来就可以了然后这里边呢将来有消息来了之后它就会把消息封装到这个方法的一个参数叫做message里边好message里边不要导错了包好再叫做这个地方叫做amqp的核心包里边一个message对象它会封装这里边
[05:52] 封装到这里边之后呢我们需要干的事呢打印一下好吧打印一下呢message打印完事了之后呢我们的消息就可以把它取出来现在呢我们队列里边其实是有一条消息的刚才我们也看到了在我们的队列里边有条消息吧有了之后呢我们接下来就可以来完成一个核心类的启动启动一下之后你会看到控制台上如果打印出来了
[06:18] 这条消息就证明我们的消费者的监听写的是没有问题的那么这个地方呢他说找不到对应的一些个测试的用例我们来看一下对对对他这里边默认的把我们这个也写好了写好了之后呢我们还把那个坐标给删了这玩意是不是太智能了一点点是吧那这样吧我们就狠一点把这个删掉
[06:45] 就是刚才我们把那个Spring Boot对应的一个JUnit Test的依赖坐标给删掉了嘛所以呢它那个人报错了对吧好然后呢接下来我们再运行现在就没有问题了对吧启动启动完事了之后呢你注意看这个地方是不是bootmq hello这个message对象打印出来了那么你想获取对应的消息呢你只需要把它转化成字幕串是不是就可以了new string然后呢message.getabody就可以了对吧OK啊我们可以尝试一下
[07:21] 尝试一下之后呢我们就sout一下new stream然后呢这里边写message.getbody这样呢就能获取到消息体了我们重新获取一下重新获取一下现在肯定是没有消息的因为我们那个对列里边消息已经被消费掉了消费掉了之后呢我们可以clear掉我们再通过这边的测试给它发送这么一条消息好我们再通过这个地方的一个junit测试来
[07:52] 发一条消息发完之后呢来看consumer这一端这一端呢就会收到这个消息看收到了吧这样呢我们对应的Spring Boot整合RabbitMQ这个代码我们就编写完了编写完了之后呢最后我们来一个小节首先呢我们说Spring Boot提供了快速整合RabbitMQ的方式快速的整合因为这些整合的坐标都是由Spring Boot来提供的然后呢基本的信息在RAML里边的配置上
[08:24] 那么对列交换机以及绑定关系我们要声明这个bin的方式来进行一个配置那么生产端呢我们将来注入一个Rabbit Template来消息发送消费端我们直接使用Rabbit Listener来完成消息的接收其实真正将来各位要写的代码其实可能就是这两块了这两块然后呢以及定义对列交换机以及绑定关系这三块可能你要去写你想这些基本的配置呀坐标的引入啊那些只是处理一遍就可以了
[08:53] 好嘞 那么这个Spring Boot整合RobinMQ我们就讲解完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spring Boot 整合 RabbitMQ，创建生产者和消费者项目并实现消息发送与接收。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了生产者项目 `producer-Spring Boot` 的结构，其中 `ProducerTest.java` 中使用 `RabbitTemplate` 发送消息到 `boot_haha` 队列，消息内容为 `"boot mq hello---"`。
画面2: 在 IDEA 中打开“Project Structure”对话框，配置模块的源码目录，`main` 和 `test` 目录被标记为源码和测试源码。
画面3: 在创建新模块时，选择 Spring Boot 2.1.7 版本，并在依赖中勾选了 `Spring Boot Web`、`Spring Boot Test`、`Spring Boot AMQP` 等依赖。
画面4: 展示了消费者项目 `consumer-Spring Boot` 的 `pom.xml` 文件，其中 `<parent>` 指向 Spring Boot 2.1.7 的父项目，`<properties>` 定义了 Java 版本为 1.8。
画面5: 在 `pom.xml` 中添加了 `spring-boot-starter-amqp` 依赖。
画面6: 在 `pom.xml` 中添加了 `spring-boot-maven-plugin` 插件。
画面7: 打开 `application.properties` 文件，准备进行配置。
画面8: 创建 `RabbitMQListener.java` 类，准备编写监听器代码。
画面9: 在 `ConsumerSpringbootApplication.java` 中，`main` 方法调用 `SpringApplication.run` 启动应用。
画面10: 在 `RabbitMQListener` 类中，使用 `@RabbitListener(queues = "boot_queue")` 注解监听 `boot_queue` 队列，并在方法中打印消息体。
画面11: 运行 `ConsumerSpringbootApplicationTests` 测试类时，控制台报错，提示 `@SpringBootTest` 注解无法识别。
画面12: 运行 `ConsumerSpringbootApplication` 启动类，控制台显示应用启动成功，并接收到消息 `Body: mq hello`。
画面13: 在项目结构中，`consumer-Spring Boot` 和 `producer-Spring Boot` 两个模块并列显示。
画面14: PPT 标题为“1. Spring Boot 整合 RabbitMQ”，下方列出消费者开发步骤：1. 创建消费者 Spring Boot 工程；2. 引入 start 依赖坐标 `<dependency><groupId>org.springframework.boot</groupId><artifactId>spring-boot-starter-amqp</artifactId></dependency>`；3. 编写 yml 配置，基本信队配置；4. 定义监听类，使用 `@RabbitListener` 注解完成队列监听。

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
    <artifactId>consumer-Spring Boot</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>consumer-Spring Boot</name>
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
标题: 1. Spring Boot 整合 RabbitMQ
内容:
消费者
1. 创建消费者 Spring Boot 工程
2. 引入 start 依赖坐标
   `<dependency><groupId>org.springframework.boot</groupId><artifactId>spring-boot-starter-amqp</artifactId></dependency>`
3. 编写 yml 配置，基本信队配置
4. 定义监听类，使用 `@RabbitListener` 注解完成队列监听

5) 无

