# day13-1-可靠消息实现最终一致性-入门案例-环境搭建

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-6 可靠消息实现最终一致性
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-6 可靠消息实现最终一致性\day13-1-可靠消息实现最终一致性-入门案例-环境搭建_【海量资源尽在 666java.com】.mp4
- 时长 8分52秒（音频 532s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们一起了解了一下通过RocketMQ是如何实现或者说解决分布式事物问题的就是通过这个什么呀消息对链对吧或者通过可靠消息这里边我们重重点是不是提到两个问题吗一个是消息发送方这边涉及到的这个原子性的问题还有一个是对消息的接收方涉及到这个原子性的问题那这些呢我们刚才跟大家说过了这个呢是
[00:30] 非常重要的这个内容当然了这一块都是一些理论知识对吧所以说接下来呢我们就要通过一个快速入门案例啊拿着我们刚才说的这个解决方案去实战一下那咱这个入门案例呢还是这个两个账户这个转账啊还是这个案例只不过这次呢我们是通过RawKit MQ啊这个可靠消息来解决这个分布式事务问题了最终达到这个什么呀这个实现最终一致性
[00:59] 那大概的这个业务呢大家都比较比较熟悉了啊还是两个账户一个张三一个李四张三是在半个一李四是在半个二啊半个一和半个二是两个相互独立的微服啊那么这里边呢就涉及到分不识受的问题那我这还画了一个图啊这个图呢其实就是这个图就这个图啊只不过我呢是结合咱们转账这个案例又给了一个图吗这个看起来更加清晰一些啊我们熟悉熟悉了
[01:31] 首先就是Bank1这边啊就是张三这边先发送一个什么消息给什么MQ但是这个消息呢大家注意它是一个半消息是不是啊那就是MQ它能接收到这个消息但是这个消息不能被谁啊Bank2去消费一块去接收这个B银行其实指的就是Bank2对它是不可见的它接收不了是半消息咱们前面说过然后呢Jockey的MQ会返回给Bank1一个什么呀一个消息接收成功的一个回调
[01:58] 那Bank1接收到这个回调之后呢他就开始执行什么呀本地事务我们说的主要是完成账户的一个一个什么呀对检控的一个操作那执行完之后呢他还会向MQ发送这个券消息就是我们前面说的这个Commute或者说什么呀对Rowback那成功的话他这边就会发什么呀对Commute失败就会发什么Rowback如果是成功那这个时候呢这个Rocky的MQ呢就会把这个
[02:27] 消息的状态设置成什么可消费的那这个时候呢这个币银行就Bank2这边是不是就可以在这边给接收啊或者说消费这个转账的消息就是咱结合这个转账这个案例吧就给了一个图啊熟悉一下这个业务那这个业务大家清理了之后我们就是进行环境搭建吧咱们这个快速的过一遍啊第一个就是这个数据库我们用的是哪个版本啊GPK啊微服啊
[02:55] 啊重点你要看看我们的说kita mq啊我们用的是4.5这个版本啊包括说kita mq的扣单扣单我们直接用他跟sprintboot的一个一个一个机场一个家暴这个是大家需要注意的然后我们就需要创建数据库吗这个大家都知道你不管是半个一还是半个二都要拖数据库吗一个是扣件一个是什么呀增加余额吗我都要用到数据库那我们还是需要两个数据库一个就是半个一一个就是什么呀半个二那这两个数据库大家不用见了啊
[03:25] 大家还有印象吗我们之前在讲Hemingway的时候是不是也实现过这个转账案例吗当时呢就已经创建过半颗1号半颗2号两个数据库咱直接拿用都是转账嘛但是我们这次呢是需要在这两个数据库里边再额外创建一张表就这个表那需要增加这个表是啥原因呢对吧为什么要增加这个表呢主要是为了解决这个问题哪个问题第三个问题就这个密冷性的问题
[03:57] 我们前面说了嘛这个问题是需要咱自己去搞定的那我们需要创建这么一个表来来去去干嘛去虫啊啊就实现密等性啊具体怎么用到时候再说啊咱先把这个表先给他创建出来咱把这个脚本呢复制一下然后呢去我们这个搜狗样里边你看这是咱以前建的半个一半个二嘛对不对哎我们需要在这里边再建一个别啊因为你给这个脚本给他粘过来啊然后直接执行一下就行
[04:31] 能问题吧对不对你这边刷新一下应该是多了一个表对吧半卡二这边也需要半卡二你看这是半卡二走好大家看这边是不是也成功了对不对然后呢我们刷新一下有了吧对不对这个表里边很简单就两个字段啊用的时候再说吧这是我们新增了两个表啊主要是来来实现那个密等性的这是一个准备工作吧
[05:08] 然后接下来就是启动我们本机上的这个rocket MQ这个咋启动呢我就不再过头说了吧咱讲一边也有啊比较简单一个是是不是要先启动name server对吧然后再启动这个什么呀broke咋启动大家自己看讲义吧这个大家比较熟了啊通过这个命令就可以运行就这块那么MQ启动完之后我们就需要导入这个门工厂啊我们在这个资料文件夹里边给大家提供的有这个基础工厂啊
[05:35] 大家这个直接用ID给它导进来就行了那我这边呢就已经导好了咱去ID里边直接看看这是复工程这两个呢是它这个这个模块对不对一个Bank1一个Bank2你应该能猜出来Bank1Bank1不就是咱图里边说的这个Bank1这个微服务吗对不对这个呢对应的就是Bank2这个微服务嘛两个微服务嘛各自操作各自的数据库一个Bank1数据库一个Bank2数据库那这个复工程啊还是主要来管理这个依赖
[06:05] 这里边都需要用哪些依赖都已经导过了这里边你看看啊那么book对不对呃我们重点看看这个my circle这个什么呀my balance这个是什么W1对不对连接池啊这边是rocky的mq然后这个spring cloud呀Spring Boot这个又不再说了呃然后呢这个半个一里边咱过一过吧这个破误念不再说了大家现在自己看然后我们重点看这个配置问题
[06:38] 这些咱们之前都学习过也用过英文程序的名字啊端口号啊56081基本反复路径这个编码这是什么呀数据库连接相关的一些信息你看我们这儿连接的是什么呀半个1对不对账号密码这个Swagger那个功能开启这儿你要注意了是不是说kitmq相关的page对吧组名啊好这个地址啊端口号这些我就不再过多说了大家都清楚
[07:07] 然后半颗一里边我们看看这个加二代码这块都提供了啥在外面给的配置不再说了啊controllercontroller这块基本上是一个空实现了对不对到时候再说啊编码的时候再说啊实体内对账号吗我看了info吗账号啊这还有一个实体内这是应该是跟那个发消息有关了到时候用的时候再说就其他没了启动类真的没啥好看了对不对然后我们看这个半颗
[07:40] 半壳这边呢那一样的我们看看他的这个配置文件吧配置文件应该跟半个一差不多了在这边名字登课号是56082对吧基本访问路径半壳DN码这是不是数据库连接信息吗你注意看这连接的是哪个数据库半壳刚才那是半个一嘛对不对还有这说kitmq的配置组名啊apt的登课这不再说了
[08:06] 然后加了代码这一块应该也是那几个吧这个sweggle的配置对不对实体类还是这个实体类这个model还是那个model用的时候再说然后呢这是启动类就不再说了有些东西咱用到时候再说这是咱们把这个什么呀maven工厂啊这一块呢我们也导进来这个基本的一些代码呢我们一起熟悉了一下这是一些准备工作吧咱就做到这一会呢咱就开始干什么呀
[08:36] 实现功能啊就是通过什么呀RocketMQ可靠消息实现追踪一日性这个方案去实现什么功能啊两个账户的转账功能来解决里边的什么分布设施问题

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 RocketMQ 实现分布式事务消息的最终一致性，通过模拟银行转账场景，讲解环境搭建、数据库创建、服务配置及消息流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PPT 第 5.2 节“RocketMQ 可靠消息”，解释其原子性保证机制，图示本地事务、发送方、服务端、接收方四部分交互流程。
画面 2: 展示 PPT 第 5.3.1 节“业务说明”，图示银行转账流程：Bank1 发送转账消息 → RocketMQ 接收 → Bank2 接收并处理 → Bank1 确认 → RocketMQ 设置消息状态 → Bank2 读取消息。
画面 3: 展示 PPT 第 5.3.1 节“业务说明”，图示流程中“消息接受成功，此时消息对银行系统不可见”步骤。
画面 4: 展示 PPT 第 5.3.1 节“业务说明”，图示流程中“本地事务，完成账户减操作”步骤。
画面 5: 展示 PPT 第 5.3.2 节“环境需求”，列出数据库、JDK、微服务框架、RocketMQ 服务端和客户端的版本要求。同时展示“创建数据库”部分，包含 SQL 语句。
画面 6: 展示 SQLyog 界面，正在执行 SQL 语句，用于创建或修改数据库表。
画面 7: 展示 PPT 第 5.3.4 节“Maven 工程”，图示 IDEA 中的 Maven 项目结构，包含三个子模块：ensure-message-demo-bank1、ensure-message-demo-bank2 和父工程。
画面 8: 展示 IDEA 中父工程的 pom.xml 文件，高亮显示 Spring Boot 和 Swagger 的依赖配置。
画面 9: 展示 IDEA 中父工程的 pom.xml 文件，高亮显示 Spring Cloud 的依赖配置。
画面 10: 展示 ensure-message-demo-bank1 的 application.properties 配置文件，设置服务名、端口、数据库连接、RocketMQ 生产者组和名称服务器。
画面 11: 展示 ensure-message-demo-bank1 的 AccountChangeEvent.java 类，定义了账户变更事件的实体结构，包含 accountNo、amount、txNo 字段。
画面 12: 展示 ensure-message-demo-bank2 的 application.properties 配置文件，设置服务名、端口、数据库连接、RocketMQ 生产者组和名称服务器。
画面 13: 展示 PPT 第 5.3.2 节“环境搭建”，重复展示数据库创建 SQL 和启动 RocketMQ 的命令。
画面 14: 展示 PPT 第 5.3.2 节“环境搭建”，图示银行转账流程，与画面 2、3、4、5、6、7、8、9、10、11、12、13 中的流程图一致。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5:
```
5.3.2.1 环境需求
• 数据库：MySQL 5.7+
• JDK：64位 JDK 8+
• 微服务：spring-boot 2.1.3、spring-cloud-Greenwich.RELEASE
• RocketMQ 服务端：RocketMQ 4.5.0
• RocketMQ 客户端：RocketMQ-spring-boot-starter 2.0.2-RELEASE

5.3.2.2 创建数据库
本案例需要两个数据库，一个是bank1，一个是bank2，无需创建，直接使用Hmily快速入门案例中的数据库即可。另外，为了实现幂等性，需要分别在bank1、bank2数据库中新增de_duplication表，即交易记录表(去重表)。

DROP TABLE IF EXISTS `de_duplication`;
CREATE TABLE `de_duplication` (
  `tx_no` bigint(20) NOT NULL,
  `create_time` datetime(0) NOT NULL DEFAULT NULL,
  PRIMARY KEY (`tx_no`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;
```

画面 6:
```
DROP TABLE IF EXISTS `de_duplication`;
CREATE TABLE `de_duplication` (
  `tx_no` bigint(20) NOT NULL,
  `create_time` datetime(0) NOT NULL DEFAULT NULL,
  PRIMARY KEY (`tx_no`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;
```

画面 7:
```
set ROCKETMQ_HOME=[RocketMQ服务端解压路径]
start [RocketMQ服务端解压路径]/bin/mqnamesrv.cmd

启动broker:
set ROCKETMQ_HOME=[RocketMQ服务端解压路径]
start [RocketMQ服务端解压路径]/bin/mqbroker.cmd -n 127.0.0.1:9876
autoCreateTopic=true
```

画面 8:
```
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>io.springfox</groupId>
      <artifactId>springfox-swagger2</artifactId>
      <version>2.8.0</version>
    </dependency>
    <dependency>
      <groupId>io.springfox</groupId>
      <artifactId>springfox-Swagger-ui</artifactId>
      <version>2.8.0</version>
    </dependency>
    <dependency>
      <groupId>org.projectlombok</groupId>
      <artifactId>lombok</artifactId>
      <version>1.18.0</version>
    </dependency>
  </dependencies>
</dependencyManagement>
```

画面 9:
```
<dependency>
  <groupId>org.springframework.cloud</groupId>
  <artifactId>spring-cloud-dependencies</artifactId>
  <version>Greenwich.SR1</version>
  <type>pom</type>
  <scope>import</scope>
</dependency>
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-dependencies</artifactId>
  <version>2.1.3.RELEASE</version>
</dependency>
```

画面 10:
```
spring.application.name = ensure-message-demo-bank1
server.port=56081
server.servlet.context-path = /bank1
spring.http.encoding.enabled = true
spring.http.encoding.charset = UTF-8
spring.mvc.throw-exception-if-no-handler-found = true

spring.datasource.type = com.alibaba.druid.DruidDataSource
spring.datasource.driver-class-name = com.mysql.jdbc.Driver
spring.datasource.url = jdbc:mysql://localhost:3306/bank1?useUnicode=true
spring.datasource.username = root
spring.datasource.password = 123

Swagger.enable = true

RocketMQ.producer.group = producer_ensure_bank1
RocketMQ.name-server = 127.0.0.1:9876
```

画面 11:
```
@Data
@AllArgsConstructor
@NoArgsConstructor
public class AccountChangeEvent implements Serializable {
    private String accountNo;
    private double amount;
    private long txNo;
}
```

画面 12:
```
spring.application.name = ensure-message-demo-bank2
server.port=56082
server.servlet.context-path = /bank2
spring.http.encoding.enabled = true
spring.http.encoding.charset = UTF-8
spring.mvc.throw-exception-if-no-handler-found = true

spring.datasource.type = com.alibaba.druid.DruidDataSource
spring.datasource.driver-class-name = com.mysql.jdbc.Driver
spring.datasource.url = jdbc:mysql://localhost:3306/bank2?useUnicode=true
spring.datasource.username = root
spring.datasource.password = 123

Swagger.enable = true

RocketMQ.producer.group = producer_ensure_bank2
RocketMQ.name-server = 127.0.0.1:9876
```

画面 13:
```
5.3.2.2 创建数据库
本案例需要两个数据库，一个是bank1，一个是bank2，无需创建，直接使用Hmily快速入门案例中的数据库即可。另外，为了实现幂等性，需要分别在bank1、bank2数据库中新增de_duplication表，即交易记录表(去重表)。

DROP TABLE IF EXISTS `de_duplication`;
CREATE TABLE `de_duplication` (
  `tx_no` bigint(20) NOT NULL,
  `create_time` datetime(0) NOT NULL DEFAULT NULL,
  PRIMARY KEY (`tx_no`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;
```

画面 14:
```
5.3.2 环境搭建
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题“5.2 RocketMQ 可靠消息”，图示中“本地事务”指向“发送方”，“发送方”指向“服务端”，“服务端”指向“

