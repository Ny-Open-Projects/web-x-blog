# 03_高级特性-消息可靠投递-return

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/2.RabbitMQ第二天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\2.RabbitMQ第二天\03_高级特性-消息可靠投递-return_【海量资源尽在 ubkz.com】.mp4
- 时长 9分10秒（音频 551s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 介绍完确认模式之后接下来我们来说第二种模式第二种模式呢刚才我们也介绍了说它叫退回或者回退模式都可以啊那么第二种模式呢跟第一种模式类似啊我们来写一个代码验证一下我们把这个代码呢给它复制一份啊复制一份然后呢放这个地方来放这个地方来改一个方法名这个名叫做test returnr-e-t-u-r-n同样呢我们把这里边回调这个删掉
[00:30] 但是消息的发送呢我们还是把它留着但是呢我们把这个交换机给它改为正确的发送消息那么同理呢我们先来分析一下这个回退的模式它的一个实现的步骤刚才我们也说了这个回退模式这个模式呢是当这个消息发送给excaexchange后然后呢exchange它好caxangeexchange它
[01:01] 去路由到Q失败时才会执行一个叫做return callback这么一个回调OK吧那么它的一个步骤呢我们来说一下第一步呢也同样是要去开启这个回退模式好那么开启回退模式呢跟刚才类似哈我们待会再来写这个代码那么第二步呢要去设置
[01:29] 对应的一个return callbackOK那么设置完了之后第三步很关键很多同学将来会忽略了这一步这一步呢是我们来做的是要去去设置一个exchange来处理这个消息的模式它有两种模式第一种是如果呀消息没有路由到Q
[01:59] 丢弃这个消息这是第一种那也是一种默认的处理方式他消息就不要了丢弃了那么第二种是我们今天所需要的那么如果这个消息呢没有录入到K我们返回给对应的一个消息的发送方也就是我们的这个return的callback那么这个要设置一下其实呢我们用reddit的template可以来设置他这个模式就可以了好嘞
[02:28] 有这门三步那么接下来我们就来完成代码的编写那么第一步呢我们还是要设置开启开启刚才呢publish confirms它第二种叫publisher returns也设为true默认也是关闭的好我们把这个呢给它粘过来粘过来之后呢我们放到这个地方开启一下第二步呢我们要设置好设置一下这个return callback
[02:55] 也同样用rabbit template的set return callback然后new一个return callback当然这个地方呢你也可以通过Lambda表达式来完成简化这个匿名内部类的编写我们在这块就不再使用了那么我们可以在这呢打印一句话打印个什么话呢说这个return呢好执行了好执行了点点那么现在呢注意啊我并没有去设置这个处理消息的模式默认是不是丢弃了
[03:26] 丢弃了他就不会把消息发送给这个地方了那么也就是话也就是说这句话就不会被执行了我们可以来尝试一下在这个地方呢我们正常的方式肯定是不会执行的我们可以来运行一下正常的方式这句话肯定不会执行稍等看没有执行吧那么我们想让他说到交换机了但是呢没有到Q也非常简单啊当然除了系统的内部的一些问题比如说我在这个地方呢
[03:54] 我这个路由可以就写错了吗写错了他肯定就到不了了对不对那么这个时候呢我也没有去设置这个处理消息的模式他默认就丢弃了他也不会去执行这么一个毁掉可以稍等一下看一下那么这个时候呢交换机把消息呢丢弃了那么我们要想让他把消息再返回给对应的一个生产者我们需要去设置一下模式我们设置一下模式好
[04:24] 设置交换机处理处理失败消息的模式非常简单一句代码rabbit template.set这个地方叫做meditary好设为处设为处之后呢消息交换机就会把消息呢再返回给我们对应的生产者生产者通过这个监听就可以把这个消息拿到你看这个方法里边return的
[04:53] message这里边是不是有个message对象拿到了当前这条消息啊我们可以再来运行一下稍等一下我们看一下这个return是否执行啊哎这个地方呢我们就看到return执行了对吧那么这要进行三步的这么一个处理啊第一个开启第二个呢设置回调第三个呢要设置它的一个处理的模式啊那么这个弄完了之后呢接下来我们最后呢来聊一聊
[05:22] 这个return的message里边这些参数代表什么意思啊也非常好理解啊我们来写个注释好第一个参数呢message就不说了这个玩意儿呢就是消息对象啊好我们发送的那个消息对象好第二个呢叫做replaycode其实就是返回的这个code啊就是失败的码失败的错误码好错误码第三个呢text叫做错误信息
[05:53] 好失败的信息第四个exchange叫做交换机是哪个然后呢routing key就是路由件好那么我们也可以把这些消息呢都分别的给他打印一下参数message好复制几份然后呢第二个recode然后呢text好第三个呢叫做exchange最后一个叫做routing key好打印完事之后呢我们重新的再来执行一下
[06:25] 看一下这些个数据参数到底长什么样子稍等我们看这前边是一条日志信息return执行了然后下边这个就是我们的消息数据Body就是我们的message confirm刚才我们发的消息数据后边有一些消息的properties配置的参数信息OK然后312就是我们的codecode代表的含义叫做no root对吧
[06:53] 然后呢就是这个意思就是没有一个路由路由嘛没有路由成功然后呢对应的交换机呢是这么一个名字对应的写的路由K呢是confirm加了三个一是我们自己写错的这么一个交换机路由K的一个值那么在这种return的模式里边我们可以拿到一些成功被exchange接收但是呢没有被Q处理的这么一些消息当然
[07:21] 在这些消息里边我们也可以做一些特殊的处理当然不仅仅是打印将来我们要在这做一些处理处理然后可能会再次的去让它去路由到另外一个Q还是怎么怎么着这个处理的方式是我们第二部分要讲解的内容那么这一块我们也讲完了这个return的这种模式那么下来我们对这两种模式做一个简单的小结第一个我们说了conform的模式首先我们要去开启
[07:51] 设置它的publisher confirms为true第二种呢我们给它绑定一个confirm的callback那么confirm callback里边要注意啊我们方法里边要判断这个ACK如果为true则发送成功如果为false则发送失败需要我们处理啊然后第二种呢我们介绍了一下return的回退模式那么也同样需要开启设置publisher returns为true然后同样呢去给它绑定一个return的callback
[08:17] return callback里边要注意啊它只有是消息失败了才会调用它那么消息失败还不一定会调用它还需要设置一个meditary这么一个参数为true的话才会去执行对应的return callback里边的回调函数那么其实呢在我们的RapidMQ里边也提供了一种事务机制来保证它消息发送成功也就是说你开启事务
[08:42] 如果发送成功提交事务发送失败回滚事务但是事务的方式性能比较差所以这一点就不做讲解了下面也给你提供了三个方法说ts select来开事务ts commit来提交事务ts rollback来回滚事务它们都是channel的方法这块有兴趣的同学可以去了解一下好嘞那么对于第一个消息可靠性投递的一些API操作我们就讲解完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 RabbitMQ 消息的可靠投递机制，包括 confirm 确认模式和 return 返回模式的实现与配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：PPT 标题为“1.1 消息的可靠投递”，介绍 RabbitMQ 提供的 confirm 和 return 两种可靠投递模式，以及消息传递路径：producer → RabbitMQ broker → exchange → queue → consumer。
画面 2：展示 Java 代码，定义 RabbitTemplate 的 confirmCallback，用于处理消息发送到 exchange 后的确认回调。
画面 3：展示 Java 代码，定义 testReturn 方法，用于测试 return 模式。
画面 4：展示 spring-RabbitMQ-producer.xml 配置文件，定义了 ConnectionFactory、RabbitTemplate、队列和交换机的配置，其中 publisher-confirms 和 publisher-returns 属性被设置为 true。
画面 5：展示 Java 代码，注释说明 return 模式的工作原理，并开始编写 testReturn 方法。
画面 6：展示 Java 代码，设置 RabbitTemplate 的 ReturnCallback，并调用 convertAndSend 方法发送消息。
画面 7：展示 Java 代码，测试方法 testReturn 已执行，测试通过。
画面 8：展示 Java 代码，测试方法 testReturn 已执行，测试通过。
画面 9：展示 Java 代码，设置 RabbitTemplate 的 mandatory 属性为 true，以启用 return 模式。
画面 10：展示 Java 代码，设置 RabbitTemplate 的 mandatory 属性为 true，测试方法 testReturn 已执行，测试通过。
画面 11：展示 Java 代码，注释说明 ReturnCallback 的参数含义。
画面 12：展示 Java 代码，测试方法 testReturn 已执行，测试通过。
画面 13：展示 Java 代码，测试方法 testReturn 已执行，测试通过。
画面 14：PPT 标题为“1.1 消息的可靠投递小结”，总结了设置 publisher-confirms 和 publisher-returns 为 true，使用 setConfirmCallback 和 setReturnCallback 方法，以及 RabbitMQ 的事务机制（txSelect, txCommit, txRollback）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4 的 XML 配置：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/context"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:rabbit="http://www.springframework.org/schema/rabbit"
       xsi:schemaLocation="http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd
       http://www.springframework.org/schema/rabbit http://www.springframework.org/schema/rabbit/spring-rabbit.xsd">

    <context:property-placeholder location="classpath:RabbitMQ.properties"/>

    <!-- 定义rabbit连接工厂 -->
    <rabbit:connection-factory id="connectionFactory" host="172.16.98.133"
                               port="5672"
                               username="guest"
                               password="guest"
                               virtual-host="/"
                               publisher-confirms="true"
                               publisher-returns="true"/>

    <!-- 定义rabbitTemplate，用于发送消息 -->
    <rabbit:template id="rabbitTemplate" connection-factory="connectionFactory"/>

    <!-- 消息可靠投递（生产者）-->
    <rabbit:queue id="test_queue_confirm" name="test_queue_confirm"/>
    <rabbit:direct-exchange name="test_exchange_confirm"/>
    <rabbit:bindings>
        <rabbit:binding queue="test_queue_confirm" key="confirm"/>
    </rabbit:bindings>
    <rabbit:direct-exchange name="test_exchange_confirm"/>
</beans>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1 的 PPT 标题：
1. RabbitMQ 高级特性
1.1 消息的可靠投递

画面 14 的 PPT 标题：
1. RabbitMQ 高级特性
1.1 消息的可靠投递小结

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

