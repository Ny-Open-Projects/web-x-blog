# 20_SpringBoot整合RabbitMQ-生产者

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\20_SpringBoot整合RabbitMQ-生产者_【海量资源尽在 ubkz.com】.mp4
- 时长 17分49秒（音频 1069s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来介绍Spring Boot整合RabbitMQ那么我们的RabbitMQ被Spring Boot整合之后它的一个编码就会变得非常的简单那么在这一章节中我们将分两部分来完成讲解第一部分我们来讲解Spring整合RabbitMQ的一个生产端的开发第二部分我们来讲解消费者这一端的一个代码的编写那么首先我们先来说第一个生产者
[00:28] 代码的编写的一个步骤那么步骤呢分为这么五步啊我们一个一个来看一下首先我们来说第一步当然是创建一个Spring Boot的工程这个非常的简单那么第二件事呢就是要引入Spring Boot的一个整合RabbitMQ的一个E-Line那么这个E-Line是由Spring Boot提供的一个Stutter整合AMQP的这么一个E-Line啊那么这个E-Line添加好了之后
[00:55] 第三步我们就要编写YAML的配置文件那么这个配置文件其实只需要配置一些基本的信息就可以了那么这些基本的信息将来给对应的一个Connection Factory来使用比如说host、主机、username、password用户名密码以及端口号这些基本的信息那么基本信息有了之后其实我们还是需要来定义对列交换机以及绑定的关系的
[01:23] 那么这些关系我们将使用配置类来编码的方式来完成那么当然通过了一个bin注解的方式把它注入到对应的Spring的bin的容器里边就可以了那么这些准备的工作其实都可以做好了之后我们就可以在我们的需要发送消息的那个类里边来完成注入注入一个叫做Rabbit Template这么一个模板类调用它的方法来完成消息的发送就可以了
[01:52] 讲解完这个流程之后接下来我们来写代码那么首先呢我们先在这地方创建一个工程好在这创建一个工程加一个new一个模块那么我们创建一个mayweb的项目这个地方起名为com.it稍等卡住了it黑马然后呢我们起名为producerducer-sprefoot好
[02:20] 写好了之后接下来我们下一步然后呢把这个名呢复制一下finish这样呢这个工程就创建好了创建好了之后呢接下来我们就一步一步来做这个事情就行了第一步呢引入依赖引入依赖这个地方呢你要引两个第一个呢就是我们的副工程副工程的一个依赖那么因为是Spring Boot项目所以要引个副工程那么我们在这个地方呢
[02:46] 今天的一个资料里边资料里边我们找到今天的资料资料呢RabbitMQ然后呢第一天第一天里边的我们的一个资料里边对应的配置文件Spring Boot好这里边呢就有POP文件那么这里边呢复工程就是这么一个然后呢下边这两个我们也简单的说一下下边呢这个就是我们需要的Spring Boot整合RabbitMQ的一个依赖咱们还有下边这个依赖呢是完成这一游戏的单元测试的依赖
[03:16] 所以我们把这三个全部给它复制过来放这个地方就可以了放这个地方了之后我们在这个地方也写一个注释第二个就是我们的SprutRabbitMQ的一个依赖好依赖写完了之后引完了之后接下来我们来写对应的一个配置那么配置也是比较简单的我们在这个地方就来创建一个appliapplication.yml这么一个文件
[03:44] 那么在这个文件里面我们要配置配置RabbitMQ的基本信息比如说它的IP端口对吧端口UserNamePassword等等这些基本信息这些信息是用来创建连接工厂的那么这些信息你也不用去背因为这里面都有一些提示我们直接写Rabbit好
[04:13] MQ你看下面就有提示啊好那么这个地方呢我们来一个个配啊第一个host如果你不配的话默认值是localhost当然这个地方呢我们肯定不是用localhost了我们在这里边呢用这个133的这么一个路径好把http的方式给它删掉这是ipip主机名第二个呢端口其实后边这些信息啊都可以用默认值哈因为port啊
[04:43] 端口呢我们还是默认就是5672对吧然后呢用户名我们也写一下叫做guestG-O-E-S-T密码也是G-O-E-S-T然后呢虚拟机默认就是杠好那么这些东西呢都配好了之后那么接下来我们就可以来写一个启动类了那么启动类这个地方呢我们直接写个类啊com.it黑马.比如说producer
[05:12] producer这个地方的applicationapplication这样就写好了这个启动类了那么producer启动类那边加一个supreme boot application这么一个注解然后主方法supreme application.run方法把当前这个类的字节码文件给它传进去就可以了好嘞
[05:39] 那么如果你用快速创建的方式这个类呢它是帮你创建好的那么这个启动类也写好了之后接下来我们就可以来完成第三步就是比较麻烦的一步我们来写一个配置的类那么这个配置类呢我们写一个RabbitMQ的包然后叫做Configure的包然后我们起名为RabbitMQConfigure这么一个类好这个类要想作为配置类你需要加一个注解叫做Configuration
[06:08] 这么一个诸解那么这个弄完了之后呢接下来这个配置类里边配什么东西我们要知道刚才我们也介绍了说配三个第一个交换机第二个呢第二个配啥呀第二个我们要去完成一个叫做对列的配置对列Q好对列第三个呢我们要去做一个对列和交换机的一个绑定关系其实呢这个地方关系呢关系是一个bonding的对象
[06:39] 邦定的对象好这么三个东西那么我们一个一个来啊先说第一个交换机那么我们交换机呢叫做exchange我们需要返回一个exchange这么一个类然后呢这个方法呢随便起个名儿比如说我们叫bootbootexchange这么一个方法那么这个方法写完了之后呢你要做两件事第一件事呢就是给它加一个注解啊叫做bin相当于我们定义了一个bin
[07:09] 这个并的名称呢我们就叫做boot exchange叫这个名啊好弄完了之后呢接下来我们再来去写写啊那么这个exchange要去作为方法的返回值那我相当于是比较return一个呀对吧那return一个return怎么去创建出来这个exchange呢它提供了一个叫做exchange的一个builder这个类来完成构建一个交换机对象
[07:37] 那么构建交换机你一点你会看到四种不同类型的交换机就罗列出来了那么今天我们只讲topic类型的那么其他的三种呢下去自己演示一下那么topic类型的交换机呢比如说我们就可以用一个通配服的方式那么当然这个地方指定的是一个name就是交换机的名称那这个名称呢一般情况下我们在配置类里边提供一个常量public
[08:04] 叫做 StaticFanel类型的叫做exchangeName起这个名我们起名为boot-topic类型的好起名为这个名那么将来我们就把这个exchange的Name放这个地方
[08:32] 那么交换机的名字就声明好了那么声明交换机除了名字之外呢你是不是还可以指定一些参数啊比如说19化不对吧你看下边drawable就是处好19化然后呢其他的参数呢你可以声明啊是否自动删除啊等等那么这些其他的我们都不声明了那么不声明了之后呢最后你都要用个build构建一下那么这样我们的交换机就声明好了交换机声明好了之后呢对列的方式呢都类似了那么下来我们来说对列
[09:00] 对列呢那就返回一个q好返回一个q那么返回一个q呢我们叫做bootq好p u u e u e啊好这个弄完了之后接下来我们还是一样啊加一个并注解哈并注解这个地方呢我们起名为起名为就叫这个名吧bootq好这是这个对象的一个并的一个名字
[09:27] 名字弄完了之后呢我们也同样return一个q的一个builder.这里边有两种第一种是joyable就是持久化的一个对立还有nojoyable就是不持久化的一个对立那么当然我们选择持久化那么持久化这块呢又有两个方法一个呢是空餐的默认名字的一个是指定名称的我们要指定名称的那么指定名称我们在这个地方呢复制一个名字这个名字呢我们叫做qnameqyou
[09:57] E由E因为是Final修饰的所以我们所有的单词都用大写而且我们在这个地方用下滑线来分隔对应的一个单词Q由E由E这是这个名对列的名称我们把对列的名称放这个地方来bootQ放里边来了之后我们也可以设置参数对吧当然我们不再去设置了我们直接build就可以了那么这样对列的声明也就完成了
[10:27] 那么第三个事就是对列和交换机的一个绑定关系那么你要绑定交换机和对列我们简单说一下那这个地方你肯定是不是需要知道这么几个东西你首先知道谁啊是不是知道对列是谁啊要知道哪个对列啊哪个对列啊那么你除了知道哪个对列之外呢你还知道这个对列和哪个交换机绑定啊你还要知道知道哪个哪个交换机对吧
[10:57] 除了知道交换机和对列之后呢你还需要去设置一个routing k吧out, ing, routing k你是不是需要设置一下那么这三个东西有了之后呢你就可以来完成这个绑定了那么下来呢我们就来写代码同样呢写一个方法public返回一个bonding的对象返回bonding对象不要写错了只有很多的bonding的对象那么这个bonding呢我们当然用的是amqp.call里边这个bonding那么我们就写名为bondq
[11:27] Xchange好绑定一下那么绑定一下之后呢我们这个地方呢先弄一个bin注解因为将来这个玩意呢是不需要被注入的所以呢你不用给它写名字了哈那么这个地方弄完了之后呢接下来我们接着来弄接着来说接着来说这个绑定这一块呢你需要知道前面两个哪个对列哪个交换机那么肯定需要在这方法里边去用的那么到底哪个对列哪个交换机呢我们是不是可以在这里边去注入啊
[11:56] 所以我们在这里边Q一下好Q一下好Exchange一下Exchange一下把它注入进来然后将来我们肯定在这个类里边有很多的对类和交换机所以我们为了区分我们用call it file用名字来去注入名字我们就写我们的Q的名称叫bootQ好交换机的名称我们call it file一下然后我们这个地方就做bootExchange
[12:27] 好这个也写完了之后呢我们直接来return就行了那么bonding呢它也有一个bonding builder它有一个第一个方法叫bond你通过对列去绑定交换机那么就把对列传进来然后呢绑定哪个交换机呢to方法绑定你看不同的交换机都可以交换机呢我们这块呢是一个topic类型的交换机然后呢对列和交换机绑定的时候是不是要指定routing k啊
[12:56] 所以ways这个方法就传的是routing k那么我们就boot.json当然这是仅号后面零个和多个单词都是可以的弄完了之后这地方你需要指定参数吗如果需要就按的指定参数不需要就用noax那么我就不需要noax就可以了好 代码就写完了写完了之后我们的交换机对列和绑定关系都声明好了
[13:24] 生命好了之后我们的配置也就完成了那么这个配置完成了之后我们就可以写代码来测试了测试呢我们在这个测试包里边来创建一个类叫做com.it黑码.比如说叫做producer test好我们再加个包test包test test包
[13:50] 弄完了之后,我们Spring Boot要写测试类呢我们首先写一个Spring Boot Test然后呢,at runwaysrunways是Spring Runner,第二class弄完了之后呢,第一件事我们要去注入对应的刚才说了有一个叫做Rabbit Template这么一个类注入完了之后,其实待会儿我们就可以调用它的方法来发对应的消息了Rabbit Template
[14:20] 然后呢rabbit template好注入完了然后呢写个测试类测试方法test sendsend完成了之后呢我们at符号我们去给它进行一个测试的注解加上加上之后呢我们直接来发送消息发消息convert and send里边传三个参数那么第一个参数呢我们传的是一个交换机的名称那么交换机的名称呢其实就是这个名字哈
[14:49] boot topic exchange当然这个地方也用长量定义了所以呢我们直接可以用这个类的长量来表示交换机的名称exchange name第二个呢我们传一个routing k刚才我们也定义了定义了之后呢绑定的时候是boot.警号那么这个警号随便写就可以哈那么我们写个哈哈够随便吧那么弄完了之后再来第三个就是消息了消息就是boot比如说mq
[15:18] 然后呢hello好这是随便的随便写了一个消息那么这个消息也就弄完了弄完了之后呢我们来测试一下运行音启动一下启动一下如果程序没有任何的异常那么我们这个消息将发送到对应的这个对列里边去并且消息长这个样子好发完了之后呢我们待会来管控台上来看一下哎报错了看到了吧报错了他说nonpointexception
[15:48] nonpointexception这个地方注意看nonpoint的意思表示了这个玩意调用这个方法是不是point那么我们猜一定是这个玩意就是rabbit template一定为空要不是它肯定不会报nonpointexception那么为什么为空呢是因为我们忘记了加autoware注解非常简单的一个错误解决一下再来发送稍等好这个时候我们启动成功了是吧
[16:22] 成功了之后呢我们来看是否变成绿条哎绿条了没问题的话呢我们打开管理控制台你看一下哎这个地方我们就有一个对列了叫做boot-q这么一个对列对吧这是刚才我们起的对列的名称然后里边有条消息ok吧消息有了之后呢我们可以看一下这个对列啊这个对列里边呢我们来看一下对应的message信息啊message get message我们启动一下ok来看一下这里边呢就有对应的这么一个哎稍等哈取消一下
[16:52] 取消一下这里边呢就有刚才我们发送的这条消息那么个消息有了之后呢我们就证明我们的消息的生产者这一端没有任何的问题哈那么接下来回过头来最后呢我们来看一下这个消息的生产者这些代码哈其实最麻烦的就是我们对应的一个配置这一块那么配置这一块呢我们定义了一些交换机呀对列呀以及绑定的关系其实这个代码呢也都还好
[17:20] 那么将来在这个配置类里边你可能就需要定义很多很多的交换机和对列以及它们的对应关系的绑定关系的这么一些bin就可以了那么真正你编码的时候呢想在哪个地方发消息那你就在哪个类里边注入这个template调用它的convert and send这个方法来发送就可以了整体呢我们感觉这个编码量还是不大的那么生产者这一段我们就将接完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中整合 RabbitMQ，包括添加依赖、配置连接信息、定义交换机和队列、绑定关系，以及使用 RabbitTemplate 发送消息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程标题页，列出生产者实现的五个步骤：创建工程、引入依赖、编写 yml 配置、定义交换机/队列/绑定、注入 RabbitTemplate 并发送消息。
画面 2: 在 IDEA 中打开 pom.xml 文件，准备添加 Spring Boot AMQP 依赖。
画面 3: 在 application.yml 文件中配置 RabbitMQ 的连接参数，包括 host、port、username、password、virtual-host。
画面 4: 在 src/main/java/com/itheima/RabbitMQ/config 包下创建 RabbitMQConfig.java 文件。
画面 5: 在 RabbitMQConfig.java 中导入必要的包，并定义一个 @Configuration 类。
画面 6: 在 RabbitMQConfig.java 中定义交换机，使用 ExchangeBuilder 创建一个 topic 类型的交换机。
画面 7: 在 RabbitMQConfig.java 中定义队列，使用 QueueBuilder 创建一个队列。
画面 8: 在 RabbitMQConfig.java 中定义绑定关系，使用 BindingBuilder 将队列绑定到交换机。
画面 9: 在 RabbitMQConfig.java 中完成绑定关系的代码，指定队列名、交换机名和路由键。
画面 10: 在 test 包下创建 ProducerTest.java 文件，并导入 SpringBootTest 和相关注解。
画面 11: 在 RabbitMQConfig.java 中完成交换机和队列的定义。
画面 12: 在 ProducerTest.java 中编写测试方法 testSend()，使用 rabbitTemplate.convertAndSend() 发送消息。
画面 13: 运行测试，终端显示测试通过，日志显示 Spring Boot 应用启动成功。
画面 14: 在 ProducerTest.java 中完成测试方法的编写，并在测试结果中显示测试通过。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-amqp</artifactId>
</dependency>
```

画面 3:
```yaml
RabbitMQ:
  host: 127.0.0.1 # ip
  port: 5672
  username: guest
  password: guest
  virtual-host: /
```

画面 5:
```java
package com.itheima.RabbitMQ.config;

import org.springframework.amqp.core.Exchange;
import org.springframework.amqp.core.Queue;
import org.springframework.amqp.core.Binding;
import org.springframework.amqp.core.BindingBuilder;
import org.springframework.amqp.support.converter.Jackson2JsonMessageConverter;
import org.springframework.amqp.support.converter.MessageConverter;
import org.springframework.amqp.rabbit.connection.CachingConnectionFactory;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.amqp.rabbit.listener.SimpleMessageListenerContainer;
import org.springframework.amqp.rabbit.listener.adapter.MessageListenerAdapter;
import org.springframework.amqp.rabbit.support.RabbitResourceHolder;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;

