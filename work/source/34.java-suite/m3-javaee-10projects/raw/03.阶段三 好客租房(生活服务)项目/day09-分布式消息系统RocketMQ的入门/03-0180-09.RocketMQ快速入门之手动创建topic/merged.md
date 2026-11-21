# 09.RocketMQ快速入门之手动创建topic

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\09.RocketMQ快速入门之手动创建topic【海量资源尽在 ubkz.com】.mp4
- 时长 6分24秒（音频 385s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么接下来呢我们来学习一下Rog的MQ的一些API那么下面我们首先第一看的就是如何去创建一个topic那么在前面我们讲过在blog中是不是有一个一个的这个topic来把它组成的一个topic可能会有多个那么在这个topic中呢又会有一个一个的这个master queue来做一个组成
[00:24] 那么前面的我们在做测试的时候会发现我们并没有去创建一个topic它是也是可以发动消息的对不对那么为什么是这样的原因是那么我们一般情况下而言我们都是设置为什么的设置为当我们去发动消息的时候如果这个topic不存在的话会做一个自动的一个创建但是有些时候还是需要我们手动去做一个创建
[00:48] 比如说我们在生产环境的时候呢往往我们要去把这个自动创建topic功能去给它禁用掉如果你不禁用的话就会导致我们的这个topic可能会创建会比较多啊那么也因为这个里面毕竟会有一些权限这种管理啊ok所以呢接下来我们来看一下如何去手动去创建一个topic那么我们就在这个下面吧创建一个包那么我们就叫它topic这个包然后呢我们在topic这个包下面呢我们去创建一个class
[01:17] 那就叫什么呢topic然后呢demodemo啊demo然后呢我们在这个下面去写一个卖方法好那么我们来看一下topic如何创建啊那么首先呢我们需要定义一个producer就叫default啊defaultmq啊producer然后呢我们定义是一个producer等于new一个default啊producer哎ok好然后呢我们来看一下
[01:47] 那么定义完成之后呢我们需要给他设置一个构造的一个参数啊就是设置他的一个producer一个分组那么这个分组呢可以任意去设置啊我比如说我们给他设置为叫浩克浩克好然后呢下面呢我们需要给他设置设置什么呢我们的name server的地址producer.setNameServerNameServer地址是不是就172.16.
[02:17] 55.185冒号冒号98769876然后呢下面呢我们就需要去通过producer这个方法然后呢去给他就做一个创建啊那么我们先需要把我们那个producer然后呢做一个start启动启动我们那个producer那么他呢会有异常异常呢我们就直接抛出吧抛出exception抛出exception
[02:47] 好然后呢我们这个就启动我们的注意是启动我们的一个生产者启动我们的生产者然后呢我们下面就开始去创建一个topic叫producer点什么呢create topic那么要注意那么现在我们创建我们topic有三个参数一个呢是key那一个是new一个topic也是字符号类型的然后呢还有一个就是q numberok那么我们使用就使用这个第一个三个参数这个方法
[03:17] 那么第一个参数这个key它代表什么意思呢它代表的是我们的block的名字啊或者block的那个ID那么应该是它的名字啊然后呢我们来看第二个呢就是它的一个topic的名字那第三个呢就是一个q的一个数量啊ok好那么我们来做一个创建那我们来看一下第一个参数就是我们的这个block的名字那么block的名字从哪找呢还记得我们在前面所写的我们的这个配置吗我们来看一下
[03:45] 然后我们进入到我们的号客下面有一个叫RMQ下面有一个叫做RMQBroker然后在这个里面有个Config然后我们打开来看一下在这个里面我们是不是设置了一个Broker的Name是不是就是它我们把这个拷过来好那么拷贝到这然后第二个参数就是我们所创建的一个topic的名字比如说就叫my-topic
[04:14] 然后第三个参数就是我们这个topic中有多少个什么我们的这个Q一个message就是messageQ就是我们那个消息对立消息对立有几个要注意它默认的是创建4个默认创建4个那么我们可以给大家设4或者设置8都可以这个根据我们需求来那我们来看一下这个就是干嘛去创建topic创建topic然后我们可以看到
[04:45] 第一个参数第一个参数那么我们这样来写吧就是这个参数参数分别是分别是什么呢第一个参数就是我们的broken名字broken名字名称第二个呢就是我们那个topic的名称第三个参数呢就是我们那个qq的数量q这个数量默认的是4那么我们现在给它设置8
[05:15] 然后呢当我们设置完成之后呢我们需要把我们这个producer来一个setup给他关闭掉就可以了到这呢我们去打印一句话叫做什么呢这个topic创建成功创建成功ok好那么然后呢我们来启动一下看他会怎么样走
[05:37] 那么等待它的一个执行那我们就去我们的UI工具里面查看一下我们这个MyTopic是否有创建成功OK到这里是不是打印出来了Topic创建成功了并且我这个进程是不是也结束了因为我这个Producer已经set了好那么我们来看一下然后我进入到我这个控制台工具对吧然后去找到我这个有一个主题
[06:01] 来看一下有没有有一个叫my topic看到了吗是不是他是不是就已经就是我们的my topic已经是创建成功了OK这个就是我们创建topic的一个API的一个使用OK那么有些时候我们需要做一个手动创建那么如果你有需求的话那就这样做一个创建就可以了好那么关于创建topic的API的讲解我们就先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 RocketMQ Java 客户端创建一个 Topic。

2) 按时间顺序列出每张画面的要点：
画面1：展示 RocketMQ 的架构图，包含 producer、nameserver、broker 集群、consumer，以及 broker 内部的 topic 和 message queue。
画面2：IDEA 项目结构，显示项目名为 itcast-RocketMQ，包含 src、test、resources、pom.xml 等目录。
画面3：IDEA 项目结构，选中了 topic 包下的 TopicDemo.java 文件。
画面4：显示 TopicDemo.java 文件的开头部分，包含 package 声明和 main 方法。
画面5：在 main 方法中导入 org.apache.RocketMQ.client.producer.DefaultMQProducer。
画面6：在 main 方法中创建 DefaultMQProducer 实例，并设置 nameserver 地址。
画面7：在 main 方法中设置 nameserver 地址为 "172.16.55.185:9876"。
画面8：在 main 方法中调用 producer.createTopic 方法，但尚未完成。
画面9：终端中显示 RocketMQ 的安装目录和配置文件目录。
画面10：在 main 方法中添加注释说明 createTopic 方法的参数。
画面11：在 main 方法中调用 producer.createTopic 方法，参数为 broker 名称、topic 名称和 queue 数量。
画面12：在 main 方法中添加 System.out.println 语句用于打印创建成功信息。
画面13：在 main 方法中添加 producer.shutdown() 语句用于关闭生产者。
画面14：显示 RocketMQ 控制台界面，列出已创建的 topic，包括 my-topic。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
import org.apache.RocketMQ.client.producer.DefaultMQProducer;

画面6：
DefaultMQProducer producer = new DefaultMQProducer (producerGroup: "haoke");

画面7：
producer.setNamesrvAddr("172.16.55.185:9876");

画面10：
/**
 * 创建topic, 参数分别是: broker的名称, topic的名称, queue的数量
 */

画面11：
producer.createTopic (key: "broker_haoke_im", newTopic: "my-topic", queueNum: 8);

画面12：
System.out.println("topic创建成功!");

画面13：
producer.shutdown();

画面14：
package cn.itcast.RocketMQ;
import org.apache.RocketMQ.client.exception.MQClientException;
import org.apache.RocketMQ.client.producer.DefaultMQProducer;
import org.apache.RocketMQ.client.producer.MQProducer;

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：架构图，producer 指向 broker 集群，broker 集群指向 nameserver，consumer 指向 broker，broker 指向 topic，topic 指向 Message queue。
画面14：PPT 标题为“2. 快速入门”，子标题为“2.1、创建topic”，并显示了代码示例。

5) 不要评价画面美观，不要输出与课程无关的内容。

