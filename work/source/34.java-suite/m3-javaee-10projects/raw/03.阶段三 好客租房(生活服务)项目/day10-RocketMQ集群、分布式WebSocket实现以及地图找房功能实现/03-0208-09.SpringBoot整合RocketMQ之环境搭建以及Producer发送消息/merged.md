# 09.SpringBoot整合RocketMQ之环境搭建以及Producer发送消息

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\09.SpringBoot整合RocketMQ之环境搭建以及Producer发送消息【海量资源尽在 ubkz.com】.mp4
- 时长 11分26秒（音频 686s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下我们去整合Spring Boot来使用Rock.mq那么其实呢就是通过Spring去做一个这样的一个整合好那么下面呢我们来看一下那么我们这么玩的目的呢其实就是要去简化我们的Rock.mq的一个使用那么我们来看一下怎么去用啊那么首先呢我们去导入依赖那么我们需要给我们这个工程呢先给它添加一个这个parent好那么我们给它
[00:29] 加一个这个parent把这个我们就先关掉了好然后呢我们打开pub文件那么在pub文件中啊那么我们先给它添加一个parent那么这个parent添加好之后呢我们紧接着要去加入一些sprint boot的一些依赖那么这个是sprint boot以及它的一个测试的这样的一个依赖OK那么把它呢导入进来
[00:54] 那么导入进来之后呢其实我们需要紧接着要导入它是这个RogatMQSpringBootStar这样的一个配置把这个导进来把这个依赖的我们也导入进来那么要注意的是在这个地方特别要说的一点就是这个依赖这个依赖那么是RogatMQ官方所开发的这样的一个Spring Boot这样的一个扩展包
[01:22] 但是呢要注意的是这个依赖他并没有把这个包呢上传到我们的Manman的中央仓库那么怎么办呢那就需要我们自己去做一个手动的一个安装那么怎么样安装呢我们就需要去下载他的一个源码然后呢做一个Manman的一个install然后把它安装到我们的本地仓库
[01:46] 去做一个使用那么你可以通过这个GitHub一个地址去做一个源码的下载那么也可以呢使用我们在资料中给大家所提供那个源码那么你只需要执行一个Main Install当然有个CleanClean就是清理做一个Install把它安装到本地仓库就可以了那么OK好那么接着我们继续往下面看那么这个呢是RockMQ它的依赖已经是有所以这个就不需要再导入了
[02:15] 那么下面呢我们把这个编译的这个插件导入进来指定我们的编译的一个版本哎放到这好嘞那么到这里呢我们所需要的依赖就导入进来了那么其实最关键的一个依赖呢就是他啊但是呢他呢在我们的manu的中央仓库呢并没有需要大家呢做一个手动的一个安装好那么接下来呢我们来看一下那他代码的一个编写那么首先呢我们需要编写一个application properties这样的一个文件
[02:44] 那么我们把这个名字来拷贝一下然后呢在我们的这个项目中的工程里面呢我们找到我们的resource找到它然后呢去创建这样一个文件那么创建好之后呢我们把这个配置的内容拷贝过来哎OK把它拷贝过来那么拷贝过来之后呢那么我们现在呢这个是不是就搞定了对吧其实我们这个位置你可以配两个因为我们现在是不是已经搭建了一个RockedMQ的一个集群啊
[03:14] OK好那么这个是我们的一个producer的一个group一个分组叫mygroup这个分组你可以自定义OK那么到这里呢我们基本所需要的配置那么就搞定了那么接下来呢我们就可以编写我们的生产者和我们的消费者一个去发消息一个去接收消息那么我们首先先来看我们的生产者那么生产者怎么写呢那我们先来在我们这个下面的创建一个包
[03:43] 我们去做一个代码的一个编写那么创建一个Spring的包那我们会把我们的所有的一些Spring相关的一些这个API的使用都放到这个包下面我们首先来写的呢就是我们的生产者所以呢我们在这个位置创建一个类这个类呢就叫SpringProducer然后呢我们首先需要给它去添加一个component的注解把它标记为这是一个Spring的一个组件
[04:13] 那么接下来呢我们需要在这个位置去注入注入什么呢注入一个RocketMQ的一个模板mq的一个模板哎ok那么通过什么呢通过我们的这个通过sprint去注入然后呢我们导入一个RocketMQ然后呢template模板这个呢是他所提供的这样一个模板那么由于呢我们在
[04:41] application配置文件中是不是添加了这样的一个配置那么它就会自动去给我们去实力化这样的一个模板然后呢我们通过这个模板就可以做一个测试了那么下面呢我们在这个位置写一个方法然后呢就叫send messageOK那么这个呢就是我们发动消息那么发动消息怎么发的我们通过this.rockedmqtemplate.有一个叫做什么呢conword
[05:10] convert and send去做一个发送那么要注意在这个位置我们调用这个方法它有两个参数第一个参数是它的这个叫什么目标地址对吧发到哪里去然后第二个这个叫做什么就是我们的一个发送的一个数据OK那么我们来看一下那么我们调用它第一个这个方法那么我们的目标就是我们的一个topic那么发送到哪里我们可以来写一个比方说来一个spring
[05:38] 呃,这个my,什么呢,topic,就是我们Spring所发送的这个文件啊,这个消息的一个主题,然后呢,我们给它定义一个message,等于写一句话,就是叫我的,我的第一个Spring的rocket,rocketMQ消息,OK,好,那么这个呢,就是我们的消息的内容,那我们把这个message传递给它,传到它,
[06:08] 是不是就搞定了其实我们会发现我们会发现我们的使用使用我们模板是不是就变得非常简单当然了我们这个是写的一个发送对吧我们不能把这俩写死对不对所以我们应该这么来玩那么我们应该在这个位置写一个stream topic然后再写一个
[06:31] 叫做message吧应该这样去写才对啊那么咱们把这个拿走因为一会儿呢我们要去写一个测试用力对吧OK那么那就这样吧把这个topic放到这吧message哎OK那就这样来写吧那么这个就是我们的一个发送消息啊发送消息哎OK好那么接下来我们是不是就可以去编写一个测试用力了那么下面呢我们在在我们的这个
[06:59] 测试这个包下面的去创建这样的一个包然后呢我们去编写我们的测试用力ok把它拷过来然后呢在这个下面呢我们来写一个测试用力那就叫test test springrocketmqok然后呢我们给它添加两个注解一个注解呢叫做runways然后呢写一个springsprinterunner.class
[07:29] 还有一个注解叫做什么呢Spring boot test写这样两个注解然后接下来我们就需要去注入我们刚刚所写的这个类对吧就叫什么呢Spring producer然后把它注进来那么现在它能注入进来吗能注进来吗显然肯定是不行的对不对
[07:57] 因为我们现在缺少一个我们这个启动类所以呢我们需要来一个启动类那么这样我们来找一下咱们这个启动类啊启动类呢是在下面这个位置把它靠过来就是非常简单的一个启动类那么把它也丢到这个Spring这个包下面来OK那么现在我们是不是就已经啊有了这个启动类了好那么我们有了启动类之后呢那么我们是不是就可以去在这个里面给来给我们注入这个对象
[08:24] 那么下面我们是不是就可以去编写我们的测试用例对吧然后呢来一个test然后呢send message然后呢我们去加一个注解叫test然后呢我们就要用this.producer.send message那么两个对吧第一个就是我们topic刚刚我们所写的那个topic叫什么呢spring-my-topic
[08:50] 然后第二个就是消息的内容那么我们来定义一个消息那么在这个位置定义一个message等于叫我的第一个Spring RocketMQ消息OK那么这样的话是不是就可以去做一个发送了那么当它发送完成之后我们打印一句话叫什么呢发送成功OK
[09:22] 好这样的话是不是我们就发送成功了走等待他的一个执行好那么我们来看一下发送的一个结果那么可以看到这个消息他是不是已经发送成功了对吧那我们来检查一下这个消息他究竟有没有发送成功呢我们来看一下我们的这个主题那么我们来搜一下找到一个叫做Spring My Topic来看一下搜索那么是不是已经有一个消息了来看一下消息的
[09:50] 详情是不是我的第一个SpringSpring RocketMQ的消息OK那么到这里我们是不是就已经发送成功了反而可能会有同学会有点疑惑就说我们在这个位置能不能拿到它的一个发出响应的一个结果对吧返回值那么我们其实可以看到这个方法它的返回值其实返回是空那么也就是说它并没有任何的一些返回对不对那么我们如果想要去拿到
[10:19] 跟我们之前一样这样的发送的一个返回值那么应该怎么去拿就是这个send result对象怎么拿呢其实也是比较简单的啊他也提供了这样的一个API就是我们来看一下啊类似点log.mqtemplate点什么呢有一个叫做什么SYNC就是我们的一个同步发送你可以看到他返回的是不是就是一个这个result如果想异步发送那就是什么呢点AS ASYNC那么是不是去做这样的一个发送
[10:48] 那么也可以有一个callback在callback中是不是也可以拿到它的一个结果那么跟我们前面的这种写法那么就一样了就一样了你看跟异步这种写法那就一样了来看一下异步的写法发送的时候有一callback在这个里面是不是就可以拿到一个send readout的对象那OK好那么如果有些时候我们没有必要去拿它的一个
[11:12] 这个返回值的话那么直接做这样的发送也是OK的啊也是OK的好那么关于我们的这个Spring的RocketMQ的一个生产者的一个消息发送那我们就先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中集成 RocketMQ，包括添加依赖、配置属性、编写生产者代码并进行单元测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 页面“3.1、导入依赖”，并显示了 Maven 的父项目配置，其中 `<version>2.1.0.RELEASE</version>`。
画面2：展示 PPT 页面“3.1、导入依赖”，并显示了添加的 RocketMQ 依赖，包括 `itcast-RocketMQ` 和 `spring-boot-starter`。
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
    <groupId>cn.itcast.RocketMQ</groupId>
    <artifactId>itcast-RocketMQ</artifactId>
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
spring.application.name = itcast-RocketMQ
spring.RocketMQ.nameServer=172.16.55.185:9876
spring.RocketMQ.producer.group=my-group
```

画面6：
```java
package cn.itcast.RocketMQ.spring;

import org.apache.RocketMQ.spring.core.RocketMQTemplate;
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
package cn.itcast.RocketMQ.spring;

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

