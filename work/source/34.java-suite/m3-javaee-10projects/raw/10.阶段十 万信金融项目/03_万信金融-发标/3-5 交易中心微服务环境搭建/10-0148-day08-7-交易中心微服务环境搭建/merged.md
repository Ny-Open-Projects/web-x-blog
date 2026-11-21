# day08-7-交易中心微服务环境搭建

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-5 交易中心微服务环境搭建
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-5 交易中心微服务环境搭建\day08-7-交易中心微服务环境搭建_【海量资源尽在 666java.com】.mp4
- 时长 11分4秒（音频 665s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把P2P项目当中涉及到交易的或者说跟标的有关的这个数据库的设计跟大家说了一下其实具体来说就是这个数据库具体怎么进行什么呀分库分别而且这个数据库呢我们老早是不是都已经造好了是不是都已经有那接下来呢我们就要搭建一下什么呀开发环境因为咱们这一张要实现发标功能嘛是不是现在数据库也有了也都设计好
[00:30] 那就需要搭建开发环境然后一步一步去实现发标的这个业务功能那我们计划准备这么干啊就是咱们P2P平台当中呢跟交易有关的比如说啊发标投标对不对那么跟交易有关的这些功能咱们全部单独放到一个微服务工程里边实现这个微服务工程大家看一下叫万信P2P Translation Service叫这个名字
[00:59] 这个translucation不就是交易的意思吗所有跟交易有关的这功能全部放到这个微服里面有时候我们接下来会新增一个微服工程那么这个工程呢我们在资料文件夹里边已经给大家提供了一个初始的一个工程大家直接导到我们的P2P项目里边就行了那么这个工程主要操作的就是咱上面这个什么数据库他们都是一对应的跟咱前面这个套路都是一样的
[01:26] 那咱接下来去资料文件夹里边啊我们找一下啊代码在这儿在这个地方呃你可以这样Ctrl C对吧然后找到我们的这个代码所处的位置07代码是吧那就在这个地方直接先粘过来粘到这儿对吧粘到这个目录下之后呢我们在这儿进行什么呀导入其实这个呢大家都比较熟了我们给它导进来
[02:02] 点这个加是吧然后导入导入哪呢导入就是对你这个要选对啊位置要找对啊选中他点击ok然后呢下边就是nextnextfinish对吧就不用管他了好这应该就导进来了吧我看一下反应有点慢啊这是他吧对不对万信p2p-translucation-什么呀Service对没错就是他
[02:38] 这是一个初始工程里边基本的一些代码或者配置已经有但是功能上的这个东西还需要咱自己开发那这个工程导进来之后呢我们把它里边基本的一些东西咱过一遍那这里边就是第一个就是破文件里边的一些依赖你自己从头到尾大概过一遍了这里边我就强调一下跟咱最近这个密切相关的就是那个谁啊
[03:08] Mesoco的驱动对吧德鲁伊啊等等其他的大家现在自己看一下然后我们还要看什么东西这里边的一些已经提供好的一些类啊一些配置呢我们整体要过一遍好我们先打开这个启动类吧看这个启动类没啥好瞅的了跟以前都一样不再说了然后呢我们再看这里边Coreman里边有一些这个现成的一些什么呀对一些类
[03:41] 这里边其实就是一些各种各样的状态码因为我们在做交易的时候里边难免涉及到要设置各种各样的交易状态这是全局一场补货的处理这个咱以前见过包括一些工具类用到时候再说Configure里边这MyBalance Swagger的SmartVC的不再说了然后实体类这个是发标的这是投标的用的时候再说这是Token连接器还有印象吗这里边是对
[04:12] 这是咱之前第几章前面在实现这个登录的时候涉及到的登录用户的那个封装信息嘛Service里边这个config Service咱最近刚见过就是通过它来从Apollo上取数据的而用的时候再说然后呢就是这个什么呀搞配置其实我们整个搭建这个开发环境的时候呢最主要的就是搞配置那这里边的配置咱跟之前的套也是一样的大部分配置全部都放到什么呀
[04:41] Apollo上了所以接下来大家看我们的第三步就是在Apollo上你需要创建一个项目叫transaction-Service当然大家能猜出来这个项目里边存的就是咱刚导的这个微服工程里边的什么呀配置然后呢你需要做一系列的这个配置都有哪个配置呢我挑一些重点给大家说一说这个过程你需要自己整来这里呢我们要打开我本机的Apollo然后我们登录进去
[05:12] 我这边都已经做好了啊因为这个过程比较耗时嘛所以我提前就已经做好了这样呢给大家展示一下你看这样你是不是得新创建这么一个项目叫transication-Service这我就不再过头说了好这应该全部打开了啊你创建完项目之后是不是还要跟以前一样添加这个名称空间而且你这是不是要关联那些公共的这个空间对不对都关联哪些呢你这看一下吧你这瞅一眼吧看咱们transication-Service这里边都用到谁啊application
[05:42] Spring Boot, HTTP, Eureka, Fain, Ribbon这不用说了MP对吧Rocket MQ我们这个交易中心最后还是要用到Rocket MQ这是你需要关联的然后哪些配置需要进行修改呢根据咱以往的经验我能想到的是MyBetis Plus这边你是不是需要修改这个对这个扫描的这个包的这个路径你这要改一改然后还有哪好Ribbon, Fain, Eureka这些都不用改
[06:13] 啊斯本布的udp 里边你需要配这个呃微幅的基本访问路径是不是然后最重要的就是在application 里面application 里边呢我们主要就是配什么东西啊这个你还挺熟悉的吧是不是sharding-gdbc 相关的一些配置咱们前面在那个入门案例里边是已经讲过了是不是这配置呢咱也全部都放到Apollo里边了啊就在application 里边大家看一下是不是就是那个分副分辨啊数据库连接等等这些东西
[06:45] 全部都配到这里边了那这块配置呢你就参考咱的讲义进行就行了咱可以把这个配置给大家过一遍复习一下你看这块我们是不是定义这个数据源呢DS0 DS1你还有印象吗我们当时那个入门案例里边它里边是不是定义了六个数据源为啥是六个呀因为咱当时有主同架构嘛每个每一方里边有三个库嘛所以主同加起来一共六个
[07:16] 我这里边没有搞主层架构啊所以这里边就两个库就刚才不是有这个图吗在这是不是P2PTransaction0P2PTransaction1就两个库所以我们就是DS0DS1然后呢我们是不是要先进行数据库的一个什么呀连接嘛所以你看这就是连接DS0的DS0是谁呢你看这这不是P2PTransaction0吗对应的就是这个数据库啊账号密码这个不能照抄啊我们的不一定都一样
[07:46] DS1DS1是DS1就是translucation1看这是不是然后这还有密码这数据库链接数据链接整完之后下边其实就是干什么对就是分库分表的策略要进行配置这首先配的就是分库的策略分库的策略你还有印象怎么分库我们刚才说给你发表人的ID发表人的ID发表人的ID其实就是consumer ID我们的分片的键这个字段就是consumer ID就发表人ID
[08:17] 策略就是除业二求余说判断基础还是偶说这是分库的策略下面就是这两张表的分表的策略分表的策略你看是不是给你主建来分的ID这边叫project ID这个你要看着表里边的这个字段名去来写你可以打开看看你看这边就叫ID而这个图标这边叫在这叫project的下限ID所以这个你们要注意然后是
[08:47] 分表策略完我们刚才也说了就是这个ID啊标底的ID啊除以二求余数也是判断极有数然后呢这两张表是什么呀对互为绑定表这是打印这个日志这是我们整个这一块最核心的一块配置就相对上GDPC了呃这个配完之后呢你还要再检查一下你本地的application.yml这里边配置当然这个是给大家提供好的但是你最好检查一下
[09:18] 还有没有哪有什么问题了该改改一下这都没有问题了最后我们就要配置这个什么呀启动参数我们的每个微服务都有启动参数了要从Apollo上去取这个配置而且你还要设置它的什么呀端口号我们这个交易中心这个微服务它的端口号是53060所以我们在这呢要做一个配置就这个啊我这之前都已经配过53060那配好之后呢你就可以启动一下看看这个环境方面有没有什么问题
[09:49] 当然呢我可以先把出头中心先起了然后再指指启动一下谁啊对这个交易中心我们看看这个启动过程当中有没有问题因为启动的时候他会去从阿卜罗上是不是来来来加载配置嘛读取配置如果有问题的话他控制台有可能会报一些错误咱观察一下这是咱这个交易中心啊现在正在启动你看他这正在从阿卜罗上加载配置呢咱们稍等一下
[10:24] 你看刚才这个端口号稍等啊53060呢在这在这是不是然后整个过程没有报错是不是啊没有报错当然呢你这个比较谨慎的同学你也可以像咱以前一样咱那玩的一个套路就是建卡车了卡车里边你订一个哈喽啊就这种方法然后访问一下测测也可以啊我这就不再进行了这是咱们把什么呀对咱们发飙
[10:54] 这个业务所需的这个一个微服务工程就是交易中心这个微服务工程整个给把这个开发环境全部给搭建好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 P2P 项目中搭建并配置 ShardingSphere 分库分表的交易服务模块，包括导入工程、配置 Apollo 和编写 application.yml。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 Word 文档中查看课程内容，指出需在 Apollo 中配置 transaction-Service 项目。
画面 2: 展示分库分表的架构图，说明以 ID % 2 为分片策略，将数据分到 p2p_transaction_0 和 p2p_transaction_1 两个库。
画面 3: 在 IDEA 中导入模块，设置导入 Maven 项目并自动创建模块组。
画面 4: 在 IDEA 中查看 pom.xml，高亮显示添加了 sharding-jdbc-spring-boot-starter 依赖。
画面 5: 在 IDEA 中浏览项目结构，定位到 transaction-Service 模块。
画面 6: 打开浏览器，准备访问 Apollo 配置中心。
画面 7: 在 Apollo 配置中心，查看 micro_service.spring-boot-http 等多个命名空间。
画面 8: 在 Apollo 中编辑 application 配置，设置 ShardingSphere 的分片策略和数据源。
画面 9: 在 Word 文档中再次展示需要在 Apollo 中配置的 application.yml 内容。
画面 10: 打开 SQLyog，查看数据库结构，准备执行 SQL。
画面 11: 在 IDEA 中查看 application.yml，配置 Apollo 的 namespaces 和 spring.application.name。
画面 12: 在 IDEA 控制台中，启动项目，显示 Spring Boot 启动日志。
画面 13: 控制台显示 Quartz Scheduler 初始化成功，服务启动完成。
画面 14: 回到 Word 文档，再次强调在 Apollo 中配置 transaction-Service 项目。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```
Swagger.enable = true
spring.mvc.throw-exception-if-no-handler-found = true

spring.shardingsphere.datasource.names = ds0,ds1

spring.shardingsphere.datasource.ds0.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.ds0.driver-class-name = com.mysql.cj.jdbc.Driver
spring.shardingsphere.datasource.ds0.url = jdbc:mysql://localhost:3306/p2p_transaction_0?useUnicode=true
spring.shardingsphere.datasource.ds0.username = root
spring.shardingsphere.datasource.ds0.password = 123

spring.shardingsphere.datasource.ds1.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.ds1.driver-class-name = com.mysql.cj.jdbc.Driver
spring.shardingsphere.datasource.ds1.url = jdbc:mysql://localhost:3306/p2p_transaction_1?useUnicode=true
```

画面 4:
```xml
<dependency>
    <groupId>org.apache.shardingsphere</groupId>
    <artifactId>sharding-jdbc-spring-boot-starter</artifactId>
</dependency>
```

画面 8:
```
spring.shardingsphere.datasource.ds0.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.ds0.driver-class-name = com.mysql.cj.jdbc.Driver
spring.shardingsphere.datasource.ds0.url = jdbc:mysql://localhost:3306/p2p_transaction_0?useUnicode=true
spring.shardingsphere.datasource.ds0.username = root
spring.shardingsphere.datasource.ds0.password = 123

spring.shardingsphere.datasource.ds1.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.ds1.driver-class-name = com.mysql.cj.jdbc.Driver
spring.shardingsphere.datasource.ds1.url = jdbc:mysql://localhost:3306/p2p_transaction_1?useUnicode=true
spring.shardingsphere.datasource.ds1.username = root
spring.shardingsphere.datasource.ds1.password = 123

spring.shardingsphere.sharding.default-database-strategy.inline.sharding-column = CONSUMER_ID
spring.shardingsphere.sharding.default-database-strategy.inline.algorithm-expression = ds${CONSUMER_ID % 2}
spring.shardingsphere.sharding.tables.project.actual-data-nodes = ds${0..1}.project
spring.shardingsphere.sharding.tables.project.table-strategy.inline.sharding-column = project_id
spring.shardingsphere.sharding.tables.project.table-strategy.inline.algorithm-expression = project_${project_id % 2}
```

画面 11:
```yaml
app:
  id: transaction-Service
apollo:
  bootstrap:
    enabled: true
    # superLoad:
    #   enabled: true
    namespaces: application,micro_service.spring-boot-http,micro_service.spring-Eureka,micro_service.spring-ribbon,micro_service.mybatis-plus,micro_service.spring-cloud-feign,micro_service.spring-RocketMQ
spring:
  application:
    name: transaction-Service
  main:
    allow-bean-definition-overriding: true
logging:
  config: classpath:log4j2-dev.xml
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 2:
架构图结构：
- 顶层：p2p_transaction（蓝色框）
- 两个分支指向：
  - 左侧：p2p_transaction_0（橙色框）包含“标的的信息表”和“投标信息表”
  - 右侧：p2p_transaction_1（橙色框）包含“标的的信息表”和“投标信息表”

画面 14:
PPT 标题：“3.3 开发环境搭建”
内容：
1. 把资料文件夹中的 wanning2p-transaction-Service 工程导入到当前 P2P 项目中
2. 检查 maven 依赖和工程中的基本代码
3. 在 Apollo 中创建 transaction-Service 项目，在 application 名称空间中进行如下配置：

5) 无

