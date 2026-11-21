# 3.14 Spring和kafka工具类开发

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day3 数据采集服务
- 源文件：06.阶段六 冷链监控平台项目\day3 数据采集服务\3.14 Spring和kafka工具类开发_【海量资源尽在 666java.com】.mp4
- 时长 5分3秒（音频 303s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们来开发冷链设备监控平台NetE服务器端的工具类而这工具类呢主要是为了发送Kafka队列我把我们的消息发送到Kafka队列里边去那么我们现在来开发首先我们添加一个我们的包叫comment那么我们紧接着创建一个component或者说创建一个我们的java类这个java类呢是一个component是一个组件
[00:32] 我们叫做Kafka三的或者是Kafkamanager都可以那么首先它是一个common的也就是说它是一个组件这个组件里边我们用到了我们用到了Kafka的一个template叫per定一个Kafkatemplate它的类型是stringstring类型的那么名字叫Kafkatemplate这样的一个变量
[01:07] 然后紧接着我们创建方法这个方法呢会返回我们出或者否则就是发送成功或者不成功那么我们如果像我们的卡普卡里边发送我们的数据的时候我们希望传入的参数是什么呢我们可以传入一个卡普卡的一个topic那么还要传入我们发送的数据那此时我们使用try cacheexception我们把
[01:41] 如果出现异常的时候我们把异常站给它打印出来然后同时返回一个false就是发送失败了那么正常情况下它应该是返回true那此时我们在try里边直接就用Kavaka template的send方法而send里边有一个是topic有一个是messageOK这是我们创建了一个组件而这个组件呢叫Kavaka send那么我们这个组件的话
[02:14] 在我们整个QAM启动的时候在spring的一个容器里边进行启动我们在应用程序里边调用的时候我们需要先找到这个组件我们需要创建一个java类这个类呢是属于我们spring的上下文的一个工具类叫springcontext-util而这个类呢我们需要实现一个接口这个接口就是applicationapply
[02:46] 可以选context的这个接口而这个接口里边我们需要先定义一个我们的一个static对象这个对象是applicationcontext上下文那我们在我们这个类里边我们需要实现或者复写一个方法这个方法叫setapplicationcontact那么我们设置设置一下
[03:29] Utile.applicationContext等于传入进来的ApplicationContext那紧接着它需要创建一个从我们的上下文中获取bin的方法叫static静态的一个方法object.getbin我们根据名字来得到binreturnApplicationContext.getbin
[04:04] 然后我们就把Name传进了去此时我们就可以通过我们Spring的容器根据bin的名字拿到我们的具体的bin当然这个类的话其实是一个component就是是一个组件那么它的基本原理就是说我们Spring在启动之后本身是个容器而容器里边我们需要把其他的一个bin给拿过来也就是说我们的Kafka3的它是一个
[04:34] 实体bin在启动的时候已经在我们的Spring容器中注册了那么我们通过这个SpringContext它的一个工具类就是Spring上下文的工具类能够拿到我们的bin那么我们在服务器端开发的时候我们就可以使用这个这个工具类了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import org.springframework.Kafka.core.KafkaTemplate;
import org.springframework.stereotype.Component;

@Component
public class KafkaSender {
    @Autowired
    private KafkaTemplate<String, String> kafkaTemplate;
```

画面5：
```java
import org.springframework.Kafka.core.KafkaTemplate;
import org.springframework.Kafka.support.SendResult;
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

