# day06-18-开户第三阶段-搭建MQ环境

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day06-18-开户第三阶段-搭建MQ环境_【海量资源尽在 666java.com】.mp4
- 时长 10分26秒（音频 627s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那咱接下来就开始编码实现开户业务的第三阶段那由于第三阶段咱们前面分析的时候说过他要用到Rocket MQ对吧所以咱首先呢要把Rocket MQ的这个环境先给他准备一下咱参考讲一来就行了首先第一步呢就是大家自行安装和配置Rocket MQ因为这块咱之前讲过了我这就不再过多给大家说了
[00:31] 那这里边提醒大家注意你要配置加了home环境变量还要配置这个RocketMQ这个home这个环境变量这都是需要配的那配好之后呢你就去安装目录里边找到这个bb啊找到他之后呢在这个目录下边你要执行这几个命令啊然后就可以把RocketMQ给启动下来呃第一个命令这个是用来启动他那个什么呀
[01:01] Name server 嘛对不对然后第二个呢就是启动这个MQ那么在启动的时候呢我们设置了一些参数比如说我们指定他的这个IP地址端口号9876这个autocrate topic这个配置是用来这个让他自动创建这个topic就为了测试方便我们为了测试方便加这么一个配置下面这个命令呢纯粹是为了启动一个控制台就是
[01:33] 图形化的一个一个界面嘛一个控制台我们可以在这里边观察这个MQ的一些运行情况这里边的话有一个运行一个价文件就行了这个价文件我们在资料文件夹里边给大家提供的有就是他你直接用加网杠机压命就可以运行运行的时候指定他这样的端口号因为他是一个web应用程序啊指定一个端口号然后呢指定了他这个名称空间嘛就是还是那个name
[02:03] 还是这个9876当然你为了这个执行方面你也可以像我一样我是这么干的我这写了一个批处理BAT其实很简单这个BAT里边就是刚才我们说的这这三个命令你沾过来就行了沾过来之后呢你就双击他就可以把这三个命令都已经执行了你看开了几个窗口三个窗口这不是那个谁吗Nameserver他是不是已经启动成功了对不对Nameserver这个是那个那个broker是不是9876端口号吗
[02:36] 也启动成功而这个第三个创造这个就我们说的那个council说那个可视化的带囤文界面的那个那个程序啊council控制台他也启动成功啊呃他启动成功之后怎么访问呢通过一个固定的一个一个访问地址我这都收藏过了就这个地址6万嘛咱刚才在命令里边大家也看到我们的这个命令是不是就是占用的那个什么呀6万嘛是不是后边上写呃敲上这个rocky的mq
[03:05] 这是他这个固定的一个访问路径啊在这里边呢你能观察一些数据能看到这个MQ的一些运行情况这样呢我们可以换成这个简体中文你看这里边你能看到各种各样的信息集群呀主题啊消费者生产阵来还有各种各种消息啊啊等等等等我们把这几个给关掉啊这是什么呀这是呃RocketMQ啊他怎么去启动呢我们在这给大家先说一下
[03:41] 然后接下来我们要去我们的p2p里来检查一下这个碰一来我们加了没有那都需要检查哪些微服那么在开会里边我们涉及到mq的是不是一个用户中心一个存款代理服务对吧那我们就去这两个位置里边检查一下说kita mq的这个依赖有没有加进来一个是卡苏莫碰文件对不对这个哎在这已经加过了对不对然后还有谁啊
[04:15] 还有这个存款代理服务有吗这个你也可以搜一下如果太多你可以搜一下看着家F吗对不对啊哦CKET这个应该是没有的啊这个应该是没家那这个没家的话我们就给他粘过来就行就这个位置反正你要自己检查一下啊我们给他粘到下边啊这样哪都行在这吧好我们就
[04:55] 这个依赖就加进来了啊加进来之后呢我们可以稍等片刻你可以观察一下这边有没有报错啊这会有点卡你你自己观察就行了啊如果有错你还得解决这个环境的问题呃这是什么呀这是依赖啊依赖搞完之后呢还需要进行相关的一些什么样配置那由于呢咱呢这个大部分配置都是在什么呀Apollo上放着说咱得去Apollo里边检查用户中心啊存款代理服务相关的这个Apollo的配置
[05:28] 有没有哪些地方需要修改或者需要增加的对不对Apollo这边我已经打开了啊就这儿我们先去用户中心吧consumer这边consumer这边呢我们看看在这儿你看这个名称空间他已经关联进来关联进来之后我们看看他的通用配置这是那个name server地址那刚才是不是就是9876吗对不对然后这是那个生产者的组这个组
[06:01] 这个咱就不需要改了吧这俩配置咱不需要改那咱需要增加配置吗需要咱需要增加配置增加什么配置呢因为咱这个consumer这边刚才我们说了在咱们开户第三阶段这个consumer就是用户中心这边它是不是属于消息的接受方是吧也就是说它属于消费者那消费者这边的话我们要给他配置一个东西配什么东西呢就增加一个配置增加这个组名消费者这个组的组名
[06:32] 我们把这个配置呢给他增加到Apollo上就OK了将来我们在代码里边用一会写代码的时候大家就发现我在这应该是怎么着啊我在这应该是要干什么要新增是不是那点这呗你给他扔进去一条粘过来啊然后提交然后干什么发布发布哎若这个谁啊卡村们这边加这么一个配置就行了
[07:02] 那然后那个谁那个那个还有一个微服叫存管代理服这边需要进行配置吗看看啊存管代理服这边咱检查检查哎他这边好像还没有关联MQ这个空间了名称空间对不对我们添加一下反正这些就是你自己自己要检查的啊MQ就是他提交这个搞定了呗是不是然后咱回来再看看Rookie的MQ展开
[07:34] 看这俩配置咱需要改不需要这两个不需要改生产者的这个组这个名字也行还需要增加点什么配置吗也不需要也不需要那等于说吧就是阿卜罗上这个配置我们只做了一件事就是在consumer这边是不是加了这么一个配置就是消费者这边设了一个组组名这是阿卜罗配置就这个样子这个样子之后呢我们竟然还要检查检查检查啥检查这个配偶链里边有没有引这个名称空间
[08:05] 咱之前就忘我这个事儿吃我这个亏咱先看consumerconsumer的这个配置这个你看啊这个地方有印象这是干嘛的吧是不是你看我们这儿啊这个这个地方已经mq这个名称空间了啊然后咱再去这个谁啊存管代理服务这边我们再检查检查这个你要是没有配置的话那那那也不行啊这边我们瞅一瞅这边估计应该没有吧哎有啊这边还还有呢
[08:44] 有的话我们就不用管反正你自己需要检查检查需要检查一下这是什么RawKidsMQ相关的环境我们就给它搭建完了大家晚上之后我们启动一下看看这改动的这两个微服务能不能正常启动现在我们顺手做一个测试都是谁consumer重启一下还有谁存管代理服务存管代理服务稍等一下这咋办
[09:25] 这我们办了我们看一下这边开始启动了对不对那我们再去存款代理服务这边把它也重启一下这时候他就会从阿布罗上重新嗯这个加载读取配置是不是consumer这边我们看看这边启动完了是启动了是吧应该没有报错吧啊没有报错应该也不会有啥错啊存款代理服务这边我们看看现在还在启动啊还在启动你看这边是不是在从阿布罗上加载这个配置呢
[10:11] 读取配置了启动完了也没有问题那到此的话咱们就把这个rocky的mq这个环境给他准备好了那咱一会就开始动手这个编写代码

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在本地环境安装并启动 RocketMQ，并配置用户中心和存管代理服务以接入 RocketMQ 消息队列。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档，讲解 RocketMQ 环境搭建步骤，列出启动命令。
画面2：展示 RocketMQ 安装目录下的 bin 文件夹，列出启动脚本。
画面3：在命令行中执行启动命令，成功启动 Broker。
画面4：在命令行中执行启动命令，成功启动 NameServer。
画面5：在 IDEA 中查看 pom.xml 文件，展示依赖项。
画面6：展示 PPT 页面，列出 RocketMQ 启动步骤和配置检查项。
画面7：展示课程文档，内容模糊，无法识别具体信息。
画面8：展示课程文档，讲解存管代理服务的配置。
画面9：在浏览器中打开 Apollo 配置中心，显示空页面。
画面10：在 Apollo 配置中心，显示 application 的配置项列表。
画面11：展示课程文档，重复讲解 RocketMQ 启动命令。
画面12：在 IDEA 中查看 application.yml 文件，显示配置内容。
画面13：在 IDEA 控制台中显示配置加载失败的错误日志。
画面14：展示课程文档，讲解存管代理服务的配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
start mqnamesrv.cmd
start mqbroker.cmd -n 127.0.0.1:9876 autoCreateTopicEnable=true
java -jar RocketMQ-console-ng-1.0.1.jar --server.port=60000 --RocketMQ.config.namesrvAddr=127.0.0.1:9876

画面2：
（无代码或配置）

画面3：
start mqbroker.cmd -n 127.0.0.1:9876 autoCreateTopicEnable=true
The broker[00000000000000000000000000000000] boot success. serializetype=JSON and name server is 127.0.0.1:9876

画面4：
start mqnamesrv.cmd
start mqbroker.cmd -n 127.0.0.1:9876 autoCreateTopicEnable=true
The broker[00000000000000000000000000000000] boot success. serializetype=JSON and name server is 127.0.0.1:9876

画面5：
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-consul-discovery</artifactId>
</dependency>

画面6：
（无代码或配置）

画面7：
（无代码或配置）

画面8：
<dependency>
    <groupId>org.apache.RocketMQ</groupId>
    <artifactId>RocketMQ-spring-boot-starter</artifactId>
</dependency>

RocketMQ.consumer.group = CTD_P2P_GATEWAY_NOTIFY

画面9：
（无代码或配置）

画面10：
（无代码或配置）

画面11：
start mqnamesrv.cmd
start mqbroker.cmd -n 127.0.0.1:9876 autoCreateTopicEnable=true
java -jar RocketMQ-console-ng-1.0.1.jar --server.port=60000 --RocketMQ.config.namesrvAddr=127.0.0.1:9876

画面12：
spring:
  application:
    name: warningzp-depository-agent-Service
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3306/warningzp?useUnicode=true&characterEncoding=utf8&useSSL=false&serverTimezone=Asia/Shanghai
    username: root
    password: 123456
  jpa:
    hibernate:
      ddl-auto: update
    properties:
      hibernate:
        dialect: org.hibernate.dialect.MySQL8Dialect
  redis:
    host: 127.0.0.1
    port: 6379
  RocketMQ:
    namesrv-addr: 127.0.0.1:9876
    producer:
      group: CTD_P2P_GATEWAY_NOTIFY
    consumer:
      group: CTD_P2P_GATEWAY_NOTIFY

画面13：
（无代码或配置）

画面14：
<dependency>
    <groupId>org.apache.RocketMQ</groupId>
    <artifactId>RocketMQ-spring-boot-starter</artifactId>
</dependency>

RocketMQ.consumer.group = CTD_P2P_GATEWAY_NOTIFY

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面6：
标题：1. 自行安装和配置 RocketMQ，然后去安装目录的 bin 文件中执行下面命令启动 RocketMQ
标题：4. 检查用户中心和存管代理服务 application.yml 中是否引入 mq 的名称空间
内容：（无具体架构图或流程图）

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

