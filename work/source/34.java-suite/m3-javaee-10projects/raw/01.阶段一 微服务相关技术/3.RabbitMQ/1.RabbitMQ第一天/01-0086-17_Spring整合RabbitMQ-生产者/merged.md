# 17_Spring整合RabbitMQ-生产者

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\17_Spring整合RabbitMQ-生产者_【海量资源尽在 ubkz.com】.mp4
- 时长 14分30秒（音频 871s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来介绍Spring整合RapidMQ因为之前我们写代码都是以AMQP Client的这种方式来写代码相对来说编码还是非常的麻烦的那么我们使用了Spring整合之后我们的代码就会变得非常的简练而且Spring给我们提供了一些模板对象方便我们去收发这些消息那么这个章节我们分两块来讲解第一个小节我们来讲Spring整合RapidMQ的生产者
[00:30] 在第二小节我们来讲它的消费者的一个代码好嘞那么简单的说一下这个整合就是使用Spring整合一下RapidMQ就可以了那么它的步骤呢生产者我们创建工程添加依赖然后写个配置编写代码发送消息其实基本上就是这么一个思路那么接下来呢我们来直接开始写代码那么在这个地方呢我们创建两个工程重新创建两个工程我们创建第一个生产者的一个工程没问
[01:01] com.it黑马点下边写spring-rabbitrabbitmq-producer我丢这死吧然后我们弄完了之后把这个复制一下生产者的工程有了有了之后接下来我们再创建一个创建一个消费者的工程
[01:28] 还是一样com.it黑码然后呢模块的名称我们写成consumers好区分一下下一步上一步上一步我们把这个复制一下好复制一下之后呢两个工程就创建好了applyokok完事了之后呢两个工程有了之后呢接下来第二件事就是来导入对应的坐标那么这个坐标呢肯定是要导Spring相关的坐标的
[01:58] 在我们今天的资料里边也给大家提供好了对应的一个坐标资料里边配置文件里边Spring相关的在这个PoM文件里边我们把它打开打开这个PoM文件之后呢我们来看有这么一些坐标我们把它复制一下包括这个编译的插件我们都复制一下复制一下之后呢分别粘到这两个项目里边来就可以了简单的来解释一下这些坐标都不是很难来看一下第一个呢就是Spring的上下文用的5.1.7这个版本
[02:29] 然后呢这是一个Spring整合AMQP的这么一个插件包然后呢单元测试的包OK吧然后呢最后有一个编译插件1.8的这么一个编译插件的这么一个插件包好嘞这个弄完了之后呢接下来我们再把它复制到consumer里边去就可以了一样的坐标复制过来好嘞那么这两个文件呢就可以把它关掉了关掉之后呢接下来我们先来写这个producer
[02:56] 在producer里边呢首先第一件事我们来写配置配置呢我们也准备好了准备好了之后呢我们简单的来看一下对应的一个配置首先呢是这个wrapmq的properties以及呢对应的一个xml的配置文件我们先把这个配置文件给它粘过来先把这个properties粘过来粘过来之后呢可以来看一下
[03:23] 这就是我们的一些参数信息嘛IP地址啊短口号用户名密码以及虚拟机信息把它抽取到了配置文件里边这样方便我们去修改将来第一个有了之后呢接下来还有一个就是Producer的一个配置文件这是Sprint的核心配置文件也粘进来粘进来之后呢粘进来这个地方乱码了乱码了之后呢我们这样我们把它打开打开之后乱码了我们把它编码一下用这个
[03:50] Ansi就是本地默认的一个GBK的一个编码Ctrl C复制一下然后呢再把它粘进来这样它就不会再乱码了Ctrl V好保存一下然后呢接下来我们来看这个地方呢Properties有个目录我们把这个目录给它删掉这样呢就能找着这个配置文件了其实呢我们这个配置文件我们简单的来读一下非常简单首先呢我们加载了一个配置文件然后呢去声明了一个连接的工厂
[04:18] 因为之前我们的工厂是不是自己创建的然后设置这些参数现在呢通过一个标签rabbit的configureconnection factory这个标签就可以把工厂定义出来然后呢这有一个管理交换机对列的这么一个封装之后的admin的工厂那么这个弄完了之后呢下来这些就是来声明对列你注意看哦我这块是不是声明了第一个spring q的一个对列这个对列声明好了然后呢又声明了一个对列这个对列呢是
[04:48] Found这么一个对列那么这个对列它有个参数就是Auto DeclaredAuto Declared叫做自动的去创建就是说如果没有的话就自己去创建了我们声明了两个Found相关的一个对列然后呢声明好了之后对列之后这是RabbitQ这么一个名称空间的标签然后呢还有就是声明一个交换机注意看这个交换机的类型就是Found类型的这个交换机
[05:18] 那这个交换机呢它有一个名字并且呢绑定了这么两个对列注意看是这样的吧绑定好了之后呢将来我们给这个交换机是不是发送信息就可以给这两个对列分别可以收到对应的信息了除了这个之外还有还有一个呢我们下面声明了三个对列topic类型的三个对列那么这三个对列我们也声明了一个topic类型的交换机并且呢指定了交换机的名字
[05:45] 然后呢以及它的匹配的路由的规则有信号有警号的规则并且呢绑定了这三个队列那么将来我们给这个交换机加上路由的一个名称就可以指定发送到某一个队列里边去了然后呢前边第一个SpringQ这个就相当于是Hello World的方式好嘞那么基本的这个配置呢我们就简单的读了一下其实还是比较简单的很容易就可以看懂了如果刚才我们的基础的工作模式掌握的还OK的话
[06:14] 那么最后有一个非常关键的就是rabbit然后有一个template将来呢我们就用这个对象来进行发送消息rabbit template将来呢我们就把rabbit template这个对象给它注入到我们的类里边就可以来完成消息的发送了那么这个配置文件我们看完了之后呢接下来我们来写一点代码我们在测试类里边来写吧我们直接来写类吧叫做com.it
[06:43] 黑码点比如说就写producer test好这个类写一下之后呢我们要加载对应的sprint的配置文件首先呢是runways然后呢sprintsprint.unit4classrunner.class对吧然后呢第二是compact configuration然后呢要加载一个配置文件的路径locations然后呢等于classpass下的这一个文件
[07:14] 把这个文件复制一下给它粘过来OK粘过来之后呢现在我们要做的第一件事就是要注入对应的一个叫做RabbitR-A-B-B-I-T当然这个是大写的Rabbit Template这么一个类呢是Spring给我们提供的T-E-M-P-L-A-T-E这么一个类然后呢我们用AutoVir注解来注入一下Private好叫做Rabbit Template好Template
[07:43] 这个类呢给它注入进来注入进来将来我们通过它的一些方法就可以来完成消息的发送了我们写第一个test我们写hello world最简单的一种消息格式那么在这个地方呢为了让方法能独立运行我们加一个test的注解OK吧导一个对应的一个包这个地方少写个括号好弄完了之后呢我们来发送消息第二步来发送发送消息
[08:13] 这个编码量就非常的少了消息将来这些配置如果我们提前约定好的话将来在代码里边你就需要注入个这玩意然后发就行了这里边提供了叫做Converter and Send的方法注意看Converter and Send我们可以指定像Routing Key还有指定一个消息的数据不再看对象当然这个Routing Key这种参数是比较简单的就是适用于第一和第二种
[08:42] 就是我们的Hello World以及我们的Work Queues的这种格式工作模式的一种消息要发复杂的也是可以的后边有一大堆的重载形式我们先发一个简单的指定Routing Key第一种Hello World的Routing Key是不是跟对立的名称要一致那么我们看第一个对立的名称叫做Spring Queue是吧我们把它张过来然后接下来我们给一个消息数据比如就叫Hello World
[09:12] 好发完了我们写个SpringSpring好发完了之后呢我们来运行一下运行一下现在我们先来看这个地方是没有对应的这些个对列的没有一个叫做SpringQ的这么一个对列对吧其实呢将来你把这个东西呢以运行一加载将来这里边所有定义的交换机和对列都会自动的创建出来因为我们都定义了Auto Declare这么一个属性我们可以来尝试运行一下走
[09:46] 稍等一下它会加载配置文件并且来创建队列来发送消息稍等这个条只要绿了就说明成功了绿了是吧那么我们运行成功了之后呢我们回过头来看你看它是不是创建了很多Spring开头的一个队列这都是我们刚才在我们配置文件里边定义的队列对吧我们现在来看Spring Q这是我们自己的队列这里边是不是一条消息OK然后同样也有两个交换机Spring开头两个交换机然后呢这个
[10:16] 这个交换机是否绑定Q1和Q2这两个队列然后呢这个topic这个队列这个交换机是否绑定这三个队列对吧好嘞第一个消息我们就发成功了那么接下来我们再来测试发第二种消息我们把它复制一下复制一下之后呢我们来发送发送一个叫做Foundout这个每一个消息
[10:45] 那么这个消息该用哪个方法呢我们来看一下test我们就改个名F-A-N-O-U-T这么一个消息那么这个消息呢就不能直接用routing k了我们这个地方呢就需要采用三个参数这个方法了刚才我们说了如果你是pubsub这种模式的交换机那么它呢必须把消息发到exchange上然后呢它的
[11:15] 路由K指定为None或者说指定为空字不串不是None然后呢再给具体的参数信息所以呢它是这么三个参数那么第一个Exchange就是我们交换机的名称刚才我们看了这个交换机叫做这个名字对吧交换机的名称然后呢给了之后呢路由K是不是给空字不串就可以了将来会把消息分别发送到这两个Q上然后呢给个消息消息我们就随便写一个了
[11:42] 就写个sprayf-a-n-o-u-t点点好随便写一下那么我们把这个方法运行一下那么这个Q1和Q2是不是都可以得到消息稍等一下我们看一下这个是否成功啊稍等哎也绿了是吧绿了之后呢我们回过头来看这个地方你看这两个有消息了吧消息刚过来啊这样这两个Q绑定的Q是不是也收到两个消息了没有问题啊然后还有最后一个
[12:14] 最后一个呢我们弄了一个topic的方式那么我们那个topic的方式呢我们来测一下routing的方式我们并没有在这边体现有兴趣的同学可以自己下去试验一下topics那么我们发送的是topic的一个方式topic的方式那么topic的呢我们来看一下这个地方的一个对列的交换机的名称叫做Spring Topic Exchange那么我们把这个名字一改
[12:44] 就可以了然后呢他就需要指定routing k了而这个地方呢routing k你看啊注意是黑马点新发到第一个star对列黑马点仅发到第二个仅号这么一个对列然后呢itcast仅号发到这个对列那么我们这样我们为了验证它我们这样我们写一个黑马点呵呵点哈哈你注意看我在后边写的是不是两个单词
[13:14] 那么两个单词是不是只能匹配到这个井号而新号只能匹配一个单词是不是就匹配不到了所以呢将来这条消息发出去是不是应该到这个q-v这么一个对类里边啊OK那么我们把这个消息呢也可以简单的改一下topic好我们来尝试运行一下稍等运行完事了之后呢看到也变绿了那么接下来我们来看是不是到那个v里边了你看
[13:49] 稍等消息过来了是吧在VL里边是不是有条消息而这两个对列是不是都没有对应的消息因为它们跟那个通配符并不匹配那么这样呢我们的生产者的代码就写完了其实非常简单用了Spring之后呢你会发现我们的代码量大大的减少了那么简单来说一下Spring使用其实就这么两步第一步呢就是写配置约定好你的交换机和对列的绑定方式
[14:18] 那第二步呢就是在你对应的代码里边去注入Rabbit Template然后呢用它的Converter and Send的方法去发送消息就可以了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring 项目中整合 RabbitMQ，包括配置文件编写、交换机与队列的声明、以及生产者发送消息的测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 标题页“5. Spring 整合RabbitMQ”和子标题“5.1 Spring 整合 RabbitMQ”。
画面 2: 展示文件资源管理器，路径为“资料 (F:) > RabbitMQ 一天”，其中包含“代码”、“讲义”、“视频”、“资料”四个文件夹。
画面 3: 在 IntelliJ IDEA 中打开项目“spring-RabbitMQ-producers”，展示 `pom.xml` 文件内容，包含 Spring Framework、Spring AMQP、JUnit 等依赖。
画面 4: 在 IDEA 中，将“RabbitMQ 一天”文件夹下的 `RabbitMQ.properties` 文件复制到项目 `src/main/resources` 目录。
画面 5: 在 IDEA 中打开 `spring-RabbitMQ-producer.xml` 文件，展示 RabbitMQ 连接工厂和队列的配置片段。
画面 6: 在 IDEA 中，继续编辑 `spring-RabbitMQ-producer.xml`，添加了用于定义广播交换机和绑定队列的配置。
画面 7: 在 IDEA 中，继续编辑 `spring-RabbitMQ-producer.xml`，添加了用于定义主题交换机和绑定队列的配置。
画面 8: 在 IDEA 中，打开 `ProducerTest.java` 文件，展示测试类的包名和导入的依赖。
画面 9: 在 IDEA 中，编辑 `ProducerTest.java`，添加了 `RabbitTemplate` 的注入和测试方法的框架。
画面 10: 在 IDEA 中，切换到桌面，展示多个打开的窗口，包括 RabbitMQ 管理界面、IDEA、讲义等。
画面 11: 在浏览器中打开 RabbitMQ 管理界面，显示主题交换机 `spring_topic_exchange` 及其绑定的队列。
画面 12: 在浏览器中打开 RabbitMQ 管理界面，显示所有队列列表，包括 `spring_queue`、`spring_fanout_queue_1` 等。
画面 13: 在 IDEA 中，运行测试，显示测试通过，日志中包含 RabbitMQ 的连接信息。
画面 14: 在 IDEA 中，编辑 `ProducerTest.java`，添加了测试方法 `testSendTopic`，用于发送主题消息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>5.1.7.RELEASE</version>
</dependency>

<dependency>
    <groupId>org.springframework.amqp</groupId>
    <artifactId>spring-rabbit</artifactId>
    <version>2.1.8.RELEASE</version>
</dependency>

<dependency>
    <groupId>org.junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.12</version>
</dependency>

<dependency>
    <groupId>org.springframework.test</groupId>
    <artifactId>spring-test</artifactId>
    <version>5.1.7.RELEASE</version>
</dependency>

<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.8.0</version>
</plugin>
```

画面 5:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:rabbit="http://www.springframework.org/schema/rabbit"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        http://www.springframework.org/schema/context/spring-context.xsd
        http://www.springframework.org/schema/rabbit
        http://www.springframework.org/schema/rabbit/spring-rabbit.xsd">
    <context:property-placeholder location="classpath:properties/RabbitMQ.properties"/>
    <rabbit:connection-factory id="connectionFactory"
                               host="${RabbitMQ.host}"
                               port="${RabbitMQ.port}"
                               username="${RabbitMQ.username}"
                               password="${RabbitMQ.password}"
                               virtual-host="${RabbitMQ.virtual-host}"/>
    <rabbit:admin connection-factory="connectionFactory"/>
    <rabbit:queue id="spring_queue" name="spring_queue" auto-declare="true"/>
```

画面 6:
```xml
    <rabbit:fanout-exchange id="spring_fanout_exchange" name="spring_fanout_exchange" auto-declare="true">
        <rabbit:bindings>
            <rabbit:binding queue="spring_fanout_queue_1" />
            <rabbit:binding queue="spring_fanout_queue_2" />
        </rabbit:bindings>
    </rabbit:fanout-exchange>
```

画面 7:
```xml
    <rabbit:topic-exchange id="spring_topic_exchange" name="spring_topic_exchange" auto-declare="true">
        <rabbit:bindings>
            <rabbit:binding queue="spring_topic_queue_star" pattern="heima.*" />
            <rabbit:binding queue="spring_topic_queue_well" pattern="itcast.#" />
        </rabbit:bindings>
    </rabbit:topic-exchange>
```

画面 8:
```java
package com.ithema;
import org.junit.runner.RunWith;
import org.springframework.context.annotation.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
```

画面 9:
```java
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ContextConfiguration;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired

