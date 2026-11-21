# 6.RocketMQ研究-Rocket基础-快速入门-创建工程

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\6.RocketMQ研究-Rocket基础-快速入门-创建工程【海量资源尽在 666java.com】.mp4
- 时长 7分51秒（音频 471s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来我们继续来实现Rocket MQ的快速入门程序那么这个快速入门程序我们虽然是快速入门但是呢该有的还是要有的比如说生产者的工程我们要搭建一个消费者的工程我们也要创建一个然后呢生产者向MQ发送消息消费者呢去拿到消息整个过程我们是需要测试通过好首先我们来准备创建生产者的工程
[00:25] 我们这里边创建一个Test Rocket MQ的工程打开我们的工程列表那么在这里边我们是需要去一步一步的创建的因为这个工程创建起来也不是非常复杂那么你要知道这个Rocket MQ的工程虽然不复杂但是它至少得包括两一个是生产者一个是消费者对吧好这里边我们选择还是在这个散具的整个工程下面我们去创建
[00:54] 我们先看一下这个副工程我们准备选择还是闪聚的副工程然后这个就是我们说的测试rocketMQ的这个工程好下边往下走好这个就搞定接下来先不要关窗口接下来我们要做什么事就是你要创建生产者工程生产者工程刚才你创建了一个工程我们可以认为是我们整个rocketMQ测试的一个副工程
[01:21] 我们在下边再创建两个一个是生产者一个是消费者是吧好那接下来我还是要继续继续新增至于这时候新增大家知道我要干嘛吗它的复工程我要选择谁呀你不要选择散剧了你要选择哪个就是刚才咱们添的这个TES的RockedMQ懂吧然后这个就是生产者对怎么做这一点要
[01:50] 注意了这点注意了这点呢我们要选择好你现在一个目录结构啊你要选择对键到test的下面这么弄好完成这是生产者工程是不是就搞定然后还有一个消费者工程名字不要写错了来复制然后呢把它拿到这儿再来新建好新建那新建的时候呢复工程仍然是选择testrocket mq对吧好
[02:23] 然后同样的道理这儿选择路径选择路径选择test RocketMQ选它好然后呢输它好这样的话我们生产者和消费者这两个工程咱们是不是就创建好了好如果创建好了之后呢大家来看一下效果看好你看这个是test RocketMQ嘛打开是不是两个工程一个是生产者一个消费者
[02:50] 好那下面呢我们在复工程当中啊准备把复工程的POM文件呢给它完善一下因为现在我们是基于Spring Boot进行开发对不对所以说现在呢我们还要整合Rocket MQ那我们就需要加入一些依赖这个依赖是什么呢这个依赖大家看一下应该也能看得懂啊那也就是首先是你看Rocket MQ哎集成Spring Boot的一个STAR包对吧还有测试单元测试的
[03:19] 这个呢是一个web的包Spring MVC的啊好这就搞定了这是我们说的这个复工程那这样复工程我把依赖都加进去了它这两个子工程是不是都自动依赖好了当然复工程这里边有个问题你要注意就是你是复工程所以我们这个packing要写成POM这些呢都是我们当初学习Maven的知识这里边我就不再过多的去强调好注意
[03:45] 这个时候呢这个工程就基本上搞定那么下面我们就开始一个工程一个工程的来做啊首先是生产者这个生产者工程呢虽然是不太复杂但是呢它是麻雀虽小五脏俱全那你仍然还是要创建Spring Boot的这个配置文件的对吧好那下面呢我们来看一下首先我们创建一个配置文件叫Application YML好然后呢新建各位我创建这个配置文件那你说这里头要放啥呀你告诉我
[04:15] 你首先是不是要连上这个RocketMQ对吧你连接RocketMQ的话你是不是要指定谁啊name server对不对所以大家看一看上面这一些配置前面我们都用过无数次了不再说了后边你看就是RocketMQ的配置呢都以RocketMQ开头下边是一个name server那这个就是name server的地址那么生产者呢我们是需要指定一个生产者组
[04:43] 对后面我会说生产者组的作用现在呢暂时先不说啊先记着这个事然后接下来我们再来继续配置那当然还有一个启动类啊好启动类如果是启动类的话这里边呢我们是需要来创建一个怎么样创建一个包吧那你创建一个包的话这里边呢我们就创建一个在Java下边创建一个包那这个包呢你看这个包它是有一定规律的啊
[05:12] 我们这个工程它是靠目散就配Test的Rocket MQ对吧所以我们刚才说的那个启动类我准备呢准备把它创建到这个包的这个最根下面对吧然后也就是这个Rocket MQ下面是吧好这个整个的这个Spring的启动类这一块呢我就不再去写了因为这个太简单了啊我们就节省时间好这样这个生产者工程是不搞定好同样的道理呢
[05:42] 消费者的这个工程也搞定消费者工程我就我来一个简单的直接复制call对吧然后呢把它拷贝到consumer来一个简单的然后呢那这个名字改一下吧叫consumer是吧consumer这样的话这是弄到哪了不对吧我们应该是复制它吧粘进去吧对吧好
[06:13] 那这个是消费者工程消费者工程我们把producer给它干掉啊嗯然后呢大家注意看啊眼睛不要眨啊在这消费者工程是吧然后呢生产者生产者那这个consumer肯定干掉了好这两个工程你看是不是都有一个Spring Boot的这个启动类啊嗯好那么当然消费者这也有一个配置文件这是不能少的考过去就行了好这样的话那你要注意有一点啊有一点这一点你看
[06:42] 这个是原来是8181嘛这是8182吧它俩端口你要起来就不能一样那这个呢它的这个工程路径应该是consumer对吧好那是不是就可以了呀OK了这就好了所以我们通过刚才我们快速的把生产者工程和消费者工程创建其实主要是这个配置文件主要这个配置文件这个配置文件要连接内部server那生产者呢
[07:10] 要指定这个group后边我会说这个生产者组然后消费者工程呢这里边你也是要连接NameServer只不过消费者这一块呢如果它确切因为我们是测试工程它只是一个消费者的话那么其实这里边这个生产者组就可以不要了对因为它不是生产者因为我们现在是测试但是实际生产当中你要注意实际生产当中这个工程它很有可能既是消费者也是什么生产者你明白我说的意思吧
[07:39] 好了那么这个工程我们就创建好了这就相当于我们快速入门程序的两个工程我们准备工作做好一会呢我们就开始携带嘛好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中创建 RocketMQ 生产者和消费者工程，并配置相关依赖和启动类。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示课程文档目录，当前章节为“2.3.3 生产者工程”，内容为“2.3.2 消息结构”，介绍消息的基础属性（topic、消息体、消息 Flag）和扩展属性（tag、keys、waitStoreMsgOK）。
画面 2：在 IntelliJ IDEA 中打开“Project Structure”对话框，准备为项目添加新模块，当前选中“shanjupay-payment-agent-Service”模块。
画面 3：在“Project Structure”中，选中“test-RocketMQ”模块，显示其源码路径为“F:\teach\shanjupay\model\code\shanjupay\test-RocketMQ”。
画面 4：展示课程文档目录，当前章节为“2.3.4 消费者工程”，内容为“1.1 MQ的应用场景”，图示传统同步调用与异步处理的对比。
画面 5：在 IntelliJ IDEA 中，弹出“New Module”对话框，模块名为“test-RocketMQ”，路径为“F:\teach\shanjupay\model\code\shanjupay\test-RocketMQ”。
画面 6：展示课程文档目录，当前章节为“2.3.3.1 创建生产者工程”，内容为“2）创建RocketMQ-producer生产者工程”，并显示了 Maven 依赖配置，其中包含 RocketMQ 和 Spring Boot 的 starter。
画面 7：在 IntelliJ IDEA 中，打开“test-RocketMQ”项目的 pom.xml 文件，显示了 Maven 依赖配置，其中包含 RocketMQ 和 Spring Boot 的 starter。
画面 8：在 IntelliJ IDEA 中，右键点击“RocketMQ-producer”模块，选择“Refactor” -> “Rename”。
画面 9：展示课程文档目录，当前章节为“2.3.3.2 发送同步消息”，内容为“3）新建RocketMQ-producer工程的application.yml文件”，并显示了 application.yml 配置文件内容。
画面 10：展示课程文档目录，当前章节为“2.3.3.2 发送同步消息”，内容为“3）新建RocketMQ-producer工程的application.yml文件”，并显示了 application.yml 配置文件内容，其中 server.port 为 8181，spring.application.name 为 RocketMQ-producer。
画面 11：在 IntelliJ IDEA 中，打开“RocketMQ-producer”模块的“src/main/java”目录，显示了“ProducerApplication.java”文件。
画面 12：在 IntelliJ IDEA 中，右键点击“ProducerApplication.java”文件，选择“Run 'ProducerApplication'”。
画面 13：展示课程文档目录，当前章节为“2.3.3.2 发送同步消息”，内容为“4）新建启动类”，并显示了 ProducerApplication.java 的代码。
画面 14：展示课程文档目录，当前章节为“2.3.4.2 消费消息”，内容为“3、配置文件application.yml”，并显示了 application.yml 配置文件内容，其中 server.port 为 8182，spring.application.name 为 RocketMQ-consumer。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 6 的 YAML 配置：
```xml
<version>1.0-SNAPSHOT</version>
<parent>
    <artifactId>test-RocketMQ</artifactId>
    <modelVersion>4.0.0</modelVersion>
    <packaging>pom</packaging>
</parent>
<dependencies>
    <dependency>
        <groupId>org.apache.RocketMQ</groupId>
        <artifactId>RocketMQ-spring-boot-starter</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>
```
画面 9 的 YAML 配置：
```yaml
server:
  port: 8181 #服务端口
  servlet:
    context-path: /RocketMQ-producer

spring:
  application:
    name: RocketMQ-producer #指定服务名
  RocketMQ:
    nameServer: 127.0.0.1:9876
    producer:
      group: demo-producer-group
```
画面 13 的 Java 代码：
```java
@SpringBootApplication
public class ProducerApplication {
    public static void main(String[] args) {
        SpringApplication.run(ProducerApplication.class, args);
    }
}
```
画面 14 的 YAML 配置：
```yaml
server:
  port: 8182 #服务端口
  servlet:
    context-path: /RocketMQ-consumer

spring:
  application:
    name: RocketMQ-consumer #指定服务名
  RocketMQ:
    nameServer: 127.0.0.1:9876
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 4 的架构图：
- “订单服务”指向“仓储服务”。
- “仓储服务”指向“订单服务”。
- “订单服务”指向“仓储服务”。
- “仓储服务”指向“订单服务”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

