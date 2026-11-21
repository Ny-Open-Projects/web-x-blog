# day05-15-Hmily实现转账-bank1

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-13 Hmily框架
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-13 Hmily框架\day05-15-Hmily实现转账-bank1_【海量资源尽在 666java.com】.mp4
- 时长 16分13秒（音频 973s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把转账这个案例的基本环境给搭建起来了接下来呢我们就具体实现功能实现的就是转账这个功能其实这个要功能很简单对吧而且呢我们这个案例当中其实重点不是让你去去去实现这个转账这个功能而是重点是让大家去使用谁啊Harmony来解决转账业务当中的分布式事物问题
[00:29] 这是咱的重点啊您一定要注意了呃功能实现这一块的话是这样咱讲一当中呢只是展示了一些最核心的代码最核心的代码啊那完全的代码的话你应该直接去哪去咱这个项目当中去去找一下就行了啊这里边是这样啊这个微服呢我们就不再展开看了这个呢就是有瑞卡实现的一个呃什么呀注册中心对吧咱就不再管咱重点看的就是半颗一和什么呀对
[01:00] 半个二这两个呢是具体来实现转账业务这里边涉及到Heming那咱接下来先看谁呀Bank1因为Bank1在咱们转账这个案例当中应该是属于事务的发起方对吧是不是张三这边要转账吗张三要给谁转给李四转是不是所以说Bank1这边是发起方Bank2就是李四这边应该属于是参与方这一些大概的一些名词大家需要
[01:30] 提前需要了解半个一里边咱大概首先要看到无非就是先看配置就这个配置文件吧咱打开这个里边的配置很多啊但是这里边大部分配置大家都比较熟咱快速过一遍你看这些东西我就不再过头说了反正路径啊端口号56081啊这个你一会儿防那时候要注意这块是什么呀对有瑞卡相关的这块是什么呀这块不就是那个数据库连接相关的吗你看我们这儿连接的就是什么呀
[02:02] 对Bank1啊账号密码啥的这个我就不再过头说了你看都能看明白这块是Harmony相关的留到最后这块是什么呀对Ribbon因为我们这里边涉及到我们前面说过了Bank1要通过非远程电话是谁呀Bank2是吧所以这里边会有Ribbon相关的一些配置那我们重点要看的配置是这块这块这个呢就是Harmony啊这个框架相关的一些配置咱们重点要看一看啊这里边
[02:31] 你看这个配置呢是用来设置一个序列化工具那它呢是目前吧市面上相对来说应该是性能最好的一个序列化工具咱们前面在学加热的时候是不是也学过加热的序列化序列化反序列化有印象吗但是呢这个工具呢它的性能比加热的甚至比市面上其他的一些同产品性能都要高因为Harmony呢它在底层工作的时候它是需要使用这个序列化工具的
[03:02] 这个地方就是用来设置那个什么最大的虫式次数这个虫式次数大家还有印象吗前面我们在介绍TCC介绍Hemily的时候是不是提过这个词在什么地方提过你还有印象吗来咱说说在这我们说了这个TCC是不是分成三块然后进行执行然后先执行trytry有问题就走cancel没问题就走什么confirm
[03:33] 我们当然说了如果他在执行confirm和cancel的时候出问题怎么办当然你还有印象吗你看这那就需要干什么呀重试或者交给人工处理那么重试这一块呢我们就需要在这配置一下重试的什么呀次数你不能老是让人家一直在设计着那事那谁受得了是不是所以我们这设置了一个什么呀30次但这个具体设计多少次这个没有规定
[03:59] 没有规定你能结合自己的应用场景我这儿是设置了30次另外这儿是设置持久化方式DB就是通过数据库这个其实指的就是它是不是有一些日志需要存储那么日志存储的时候咱前面介绍它可以通过文件进行存储可以通过Redis进行存储对吧等等我们这采用的是数据库我们存到MySQL里面Started这个大家看注射就知道我们Bank1这边它是不是属于咱这个业务当中的事务的一个什么
[04:30] 对发起方这个事物是由张三这边发起的李斯那边是是什么呀是我的参与方所以说出表是发起方False表是什么呀对参与方这个事你得告诉HarmonyHarmony他可没那么智能他可不知道谁是事物的发起方谁是事物的参与方我们得通过这个配置告诉他下面这些我不用过多说了吧这是不是那个Harmony连接数据库的相关的一些错误对不对连接驱动啊
[05:00] 连接哪个数据库啊这一块呢因为我们说了他是不是要操作日志吗是不是你其实你你在一会你在运行的时候你会发现呢刚才也给大家说他是不是在这里边咱的库里面是不是会自动键表而且将来他会往这里边存什么样日志信息所以说他是需要连接数据库的他会有这些相关的一些配置这是二排kation.yml这里边的一些配置这个说完之后呢跟配置相关的还有还有这个
[05:30] 一个配置类Harmony相关的一个配置类大家打开看一下这个配置类呢可能大家不是很常见吗我觉得不是很常见因为咱基本上平时看还不会有这种写法这里边呢它其实最终是要产生一个对象就是Harmony事物的一个引导类一个引导对象一个BotstrapHarmony事物就是引导器这个其实至关重要的作用这个对象对于Harmony框架来说非常非常重要
[06:01] 但是这个对象呢在创建的时候呢他需要知道很多配置信息然后呢大家看一下你仔细看看这里边这些配置信息都是从哪来的从哪来对说完就从这里边来啊从这就这一堆你看这是咱刚才虚的化这个retrymax你看这里边有没有有没有对这些不就是配置键里边的这些键吗他其实得到不就是这个值吗这里边对不对你看他得到就是这些值环境环境配置相关一些信息
[06:34] 得到这些值之后呢全部存到这个对象里面最终呢把这个对象作为这个反应值返回了就是我们说了这个对象是事物的一个引导对象啊它非常关键而且呢在这个类上面你要注意加这个注解这个注解咱以前不经常用我们前面其实提到过一次就是Harmony呢它内部使用到了AOP啊这其实是用来设置代理AOP代理的一种实现方式这种实现方式应该是
[07:05] 咱以前学过代理吗包括死不受那一块是不是也学过代理代理是不是有两种就是动态代理有两种嘛一种是基于接口的一种是基于内的嘛对这种就是基于内基于内产生的一种代理这个大家大概了解一下这是这块配置这个相关的配置说完之后呢我们接下来在实现功能的时候还要做一个准备工作就这个这个你一看你应该能猜出来这是啥对我们前面说过我们的Bank1是比较远程调用Bank2通过飞影
[07:38] 是不是我们在实现转账这个功能的时候啊所以这其实就是一个黑印监考这个代码大家应该很熟了我们远程调呢是不是Bank2那边这是Bank2的那个微幅的名字这是你访问的Bank2那边具体的那个路径它应该是那个什么呀Control那里边某个方法配的那个路径这边是传过去的那个转账的金额你看这是不是都加的有什么呀还没因为你你你这个远程调是属于什么呀整个事物当中的其中一个操作嘛
[08:08] 说他也是需要进行事务管理的你看这这是跟以前不一样的地方啊咱以前在写分解解考的时候加这种注解码不加但是这是需要加的要交给Harmony进行控制我这是需要大家注意的就不一样的地方啊需要大家注意的呃然后这些准备工作做完之后呢具体接下来我们是不是就要实现转账这个功能我们看一下具体实现这个转账功能的时候呢
[08:36] 这个业务功能呢它这个代码其实我们说了主要就是一个是不是这个数据库操作就是增删改查当中的什么呀增删改查当中改就是修改嘛对不对张三这边应该是余额减少李四那边应该是余额增加嘛所以这边其实主要就是一个数据库的一个操作然后再加上一个非硬的一个远程什么呀了用但是呢这个功能实现起来很简单代码也没多少行但是这里边你要重点
[09:05] 一会你要重点观察啥观察这个东西我们重点要观察的是tryconfirmcancel这三块代码是怎么编写它跟这个图里边的这些内容是一一对应的那咱接下来就找一找这个具体实现业务的这个代码这个代码无非就是什么呀Controller还有什么呀对Service还有就是什么呀do,do这块就不再说了太简单了我们使用mybase实现一个数据库的
[09:35] 一个修改吗我们就不再看了啊包括实体内就不再看了我们重点就看Controller和Service就够了那咱先看controllercontroller这个比较简单bank1controller对不对调用这个什么业务层业务层的一个一个修改余额对不对你看updateaccount balance对吧修改余额然后呢这个是请求地址transfer交易的意思那要求你传进来一个这个单应该能猜到这是什么呀对转账金额转多少钱你说了算
[10:04] 你测试的时候呢你可以给他传值传一个数字就行了小说对不对然后我们就调右层的一个方法来具体实现这个转账的这个功能那这里边你看右层这个方法有几个参数对两个参数一个是什么一第二个是谁啊第二个就是那个转账的金额这个一是谁啊这个一是咱写死了这个一是谁你看看你觉得一是谁一不就是指的张三吗
[10:33] 因为咱这就是一个模拟的一个案例啊所以说这个用户的这个ID我们在这直接写扫啊永远转的都是涨涨三的钱啊比较悲催是不是和这需要大家注意然后接下来咱继续跟踪代码我们是不是该去这个account info Service里面是不是要找这个方法这个update的这个方法进来进来之后你看这里边代码很简单吧就这个方法嘛传过来一个ID就是number一个什么呀对转账的金额很简单
[11:03] 然后这是一个打印啊日志打印这个我们将来便于观察困难然后你看这行代表其实至关重要重要吧是不是这个是不是开始操作数据库了对让张三开始什么呀减钱了哎这是啥意思什么乘以负一啥意思啊这个大家应该能看懂吧比如我要给李斯转100块钱100乘以负一不就是负100负100不就是减了100块钱吗对不对就这意思啊呃这个这些代表都比较简单啊
[11:37] 核心的代码在这里核心代码在这这边大家注意跟TCC相关相关的就是那个tryconform还有那个cancel那些代码我们单独给他抽出来放到另外一个Service里边就这里叫account info tcc没有直接就扔到这个方案里边单独抽了一下抽到这个右层的prepare预处理try里边预处理放到这里边我们接下来重点是要看这个类当中的prepare这个方案就在这
[12:08] 他也是一个右层的一块代码就这个方法哎这里边注意了具体就要体现tryconform还有什么呀cancel这三段代码啊三块代码那具体怎么体现了主要是靠一些注解大家一定要重点看了啊重点看了就是这三块这三块啊大家注意看一下来这块其实就是try里边代码这块就是try里边代码啊
[12:39] 刘同学老说我看不到哪哪踹了对不对你的确看不到踹这个什么单词但是呢这一块的确是踹为啥呢因为他上面加了一个注解叫HemilyHemily这个注解这个发明可以随便完全自定义包括参数也是完全自定义的我们以前在介绍Hemily的时候说过嘛他只关心你要给他注册是不是三块代码那代码里边或者说这三块里边这个代码具体这个实现啥功能啥业务跟人家没关系人家也不管
[13:08] 所以这个方法可以自定义里边功能也是完全自己说了算但是呢这个方法通过这个注解进行注册这块就属于Try里边这个代码因为Try里边代码我们主要干什么事是不是要发起远程调用你看这这刚才介绍过这住的是不是就是那个那个代理嘛那个非那个远程代理他是不是就调用那个Bank2那边进行减钱了嘛进行加钱啊进行加钱那边是加钱这边代码我们一会再说啊一会再说所以这是Try
[13:38] 另外呢这我们要提醒大家注意我们这并没有实现什么冻结解冻这种药工啊只是实现纯粹一个转向啊这是需要大家注意那然后呢下面这两个方法一个是对应的是什么呀哪块代码一块对应的是confirm一块对应的是cancel这对应的是cancel那有的学员说老师你说他对应的是confirm他对应的是cancel凭什么呀哎大家看这儿看这儿啊还是看这儿这个你应该能看懂是什么意思吧
[14:12] confirm methodcommute这个值跟这是对应的啊然后你看cancel method这写的这个值跟这是什么呀对对应的如果我这个方案叫abc你这就要改成什么呀abc如果是个方案叫hello你这就要改成什么呀hello明白什么意思吗也就是说呢家有还没力注解的这块代码就是try然后他在后边同时指定了跟他相配套的什么呀
[14:41] confirm的代码是在这儿的而cancel的代码是在这儿的明白什么意思吗你只需要把这三块代码告诉Hemily剩下的事儿你就不用管将来运行的时候由Hemily去推进两边的微服务先执行什么呀这块代码明白什么意思吗如果这块代码里边出现异常那他就推进代码往哪走对走这儿他怎么知道往这儿走因为这儿进行配置
[15:08] 如果这块代码没问题他就推进走什么呀对走这儿因为这儿也配置过了现在明白什么意思吧对这个代码大概就是这个样子这是功能代码咱基本上就实验完了就是这个样子然后最后别忘了我们启动内上还有一些配置需要大家强调这个启动内上的话主要就是这个地方这个包扫描大家应该知道组件扫描componets看这个大家都很熟悉关键是呢我们跟以往不同的是有这么一个配置
[15:41] 这个地方这个配置的话很明显是不是扫描还没框架内部的一些东西对不对就是它里边有些类啊或者说有些对象也是需要交给此朋友去管理的啊说这个包呢是开门框架API的一个包所以你需要把这个也加到这个这个扫描的这个路径里边就行了其他的跟咱之前的写法没有啥区别啊该怎么着怎么着就行这是半可疑吧这边的这个代码咱整体过了一遍

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在分布式事务场景中，通过 Hmily 框架实现银行转账业务的事务管理，包括配置文件、服务类和主启动类的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 的目录结构，当前章节为“3.3.4 功能实现”，子章节“3.3.4.1 hmily-demo-bank1工程”和“(1) application.yml配置（只显示hmily部分）”。
画面 2: 在 IntelliJ IDEA 中打开 `application.yml` 文件，展示 Hmily 相关配置，包括 `registry-fetch-interval-seconds`、`serviceUrl`、`spring.application.name`、`datasource` 和 `hmily` 配置块。
画面 3: 在 `application.yml` 中高亮显示 `hmily` 配置块，包括 `serializer`、`retryMax`、`repositorySupport`、`started` 和 `hmilyDbConfig`。
画面 4: 在 `application.yml` 中高亮显示 `hmilyDbConfig` 的 `driverClassName`、`url`、`username` 和 `password`。
画面 5: 在 IntelliJ IDEA 中打开 `DatabaseConfiguration.java` 文件，展示 `@Configuration` 注解和 `HmilyTransactionBootstrap` 的初始化代码。
画面 6: 在 `application.yml` 中高亮显示 `hmily` 配置块，包括 `serializer`、`retryMax`、`repositorySupport`、`started` 和 `hmilyDbConfig`。
画面 7: 在 `DatabaseConfiguration.java` 中高亮显示 `HmilyTransactionBootstrap` 的 `setSerializer`、`setRetryMax`、`setRepositorySupport`、`setHmilyDbConfig` 方法调用。
画面 8: 展示课程 PPT 的“(3) feign代理”和“(4) 转账业务”部分，包含 `@FeignClient` 注解的接口定义和 `AccountInfoTcImpl` 类的结构。
画面 9: 在 IntelliJ IDEA 中打开 `Bank1Controller.java`，展示 `@RestController` 注解和 `transfer` 方法。
画面 10: 在 `AccountInfoTcImpl.java` 中高亮显示 `@Hmily(confirmMethod = "commit", cancelMethod = "rollback")` 注解和 `prepare` 方法。
画面 11: 在 `AccountInfoTcImpl.java` 中高亮显示 `if(!bank2Client.transfer(amount)) { throw new RuntimeException("bank2 exception"); }` 代码。
画面 12: 在 `AccountInfoTcImpl.java` 中高亮显示 `public void commit(String accountNo, double amount) { System.out.println("******* Bank1 Service commit..."); }` 代码。
画面 13: 在 `AccountInfoTcImpl.java` 中高亮显示 `public void rollback(String accountNo, double amount) { accountInfoDao.updateAccountBalance(accountNo, amount); System.out.println("******* Bank1 Service rollback..."); }` 代码。
画面 14: 在 IntelliJ IDEA 中打开 `BankHmilyServer.java`，展示 `@SpringBootApplication`、`@EnableDiscoveryClient`、`@EnableFeignClients` 注解和 `main` 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```yaml
registry-fetch-interval-seconds: 5 # 获取服务列表
serviceUrl:
defaultZone: http://localhost:50080/Eureka/
spring:
application:
name: hmily-demo-bank1
datasource:
url: jdbc:mysql://localhost:3306/hack?useUnicode=true
username: root
password: 123
type: com.alibaba.druid.pool.DruidDataSource
driver-class-name: com.mysql.cj.jdbc.Driver
```

画面 3:
```yaml
org:
dromara:
hmily:
serializer: kryo # 序列化工具
retryMax: 30 # 最大重试次数
repositorySupport: db # 持久化方式
started: true # 事务发起方
hmilyDbConfig:
driverClassName: com.mysql.cj.jdbc.Driver
url: jdbc:mysql://localhost:3306/hack?useUnicode=true
username: root
password: 123
```

画面 4:
```yaml
hmilyDbConfig:
driverClassName: com.mysql.cj.jdbc.Driver
url: jdbc:mysql://localhost:3306/hack?useUnicode=true
username: root
password: 123
```

画面 5:
```java
package cn.itcast.wanxint.hmily.demo.bank1.config;

import org.dromara.hmily.common.config.HmilyDbConfig;
import org.dromara.hmily.core.bootstrap.HmilyTransactionBootstrap;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.EnableAspectJAutoProxy(proxyTargetClass=true);

@Configuration
@EnableAspectJAutoProxy(proxyTargetClass=true)
public class DatabaseConfiguration {

    @Autowired
    private Environment env;

    @Bean
    public HmilyTransactionBootstrap hmilyTransactionBootstrap(HmilyService hmilyService) {
        HmilyTransactionBootstrap hmilyTransactionBootstrap = new HmilyTransactionBootstrap(hmilyService);
        hmilyTransactionBootstrap.setSerializer(env.getProperty("org.dromara.hmily.serializer"));
        hmilyTransactionBootstrap.setRetryMax(Integer.parseInt(env.getProperty("org.dromara.hmily.retryMax")));
        hmilyTransactionBootstrap.setRepositorySupport(env.getProperty("org.dromara.hmily.repositorySupport"));
        HmilyDbConfig hmilyDbConfig = new HmilyDbConfig();
        hmilyDbConfig.setDriverClassName(env.getProperty("org.dromara.hmily.hmilyDbConfig.driverClassName"));
        hmilyDbConfig.setUrl(env.getProperty("org.dromara.hmily.hmilyDbConfig.url"));
        hmilyDbConfig.setUsername(env.getProperty("org.dromara.hmily.hmilyDbConfig.username"));
        hmilyDbConfig.setPassword(env.getProperty("org.dromara.hmily.hmilyDbConfig.password"));
        hmilyTransactionBootstrap.setHmilyDbConfig(hmilyDbConfig);
        return hmilyTransactionBootstrap;
    }
}
```

画面 6:
```yaml
org:
dromara:
hmily:
serializer: kryo # 序列化工具
retryMax: 30 # 最大重试次数
repositorySupport: db # 持久化方式
started: true # 事务发起方
hmilyDbConfig:
driverClassName: com.mysql.cj.jdbc.Driver
url: jdbc:mysql://localhost:3306/hack?useUnicode=true
username: root
password: 123
```

画面 7:
```java
@Configuration
@EnableAspectJAutoProxy(proxyTargetClass=true)
public class DatabaseConfiguration {

    @Autowired
    private Environment env;

    @Bean
    public HmilyTransactionBootstrap hmilyTransactionBootstrap(HmilyService hmilyService) {
        HmilyTransactionBootstrap hmilyTransactionBootstrap = new HmilyTransactionBootstrap(hmilyService);
        hmilyTransactionBootstrap.setSerializer(env.getProperty("org.dromara.hmily.serializer"));
        hmilyTransactionBootstrap.setRetryMax(Integer.parseInt(env.getProperty("org.dromara.hmily.retryMax")));
        hmilyTransactionBootstrap.setRepositorySupport(env.getProperty("org.dromara.hmily.repositorySupport"));
        HmilyDbConfig hmilyDbConfig = new HmilyDbConfig();
        hmilyDbConfig.setDriverClassName(env.getProperty("org.dromara.hmily.hmilyDbConfig.driverClassName"));
        hmilyDbConfig.setUrl(env.getProperty("org.dromara.hmily.hmilyDbConfig.url"));
        hmilyDbConfig.setUsername(env.getProperty("org.dromara.hmily.hmilyDbConfig.username"));
        hmilyDbConfig.setPassword(env.getProperty("org.dromara.hmily.hmilyDbConfig.password"));
        hmilyTransactionBootstrap.setHmilyDbConfig(hmilyDbConfig);
        return hmilyTransactionBootstrap;
    }
}
```

画面 8:
```java
@FeignClient(value = "hmily-demo-bank2")
public interface Bank2Client {
    @RequestMapping("/bank2/transfer")
    @Hmily
    Boolean transfer(@RequestParam("amount") Double amount);
}
```

画面 9:
```java
@RestController
public class Bank1Controller {

    @Autowired
    AccountInfoService accountInfoService;

    @RequestMapping("/transfer")
    public String test(@RequestParam("amount") Double amount) {
        this.accountInfoService.updateAccountBalance("accountNo.1", amount);
        return "bank1向bank2转账" + amount;
    }
}
```

画面 10:
```java
@Hmily(confirmMethod = "commit", cancelMethod = "rollback")
public class AccountInfoTcImpl implements AccountInfoTc {

    @Autowired
    private AccountInfoDao accountInfoDao;

    @Autowired
    private Bank2Client bank2Client;

    @Override
    public void prepare(String accountNo, double amount) {
        System.out.println("******* Bank1 Service prepare...");
        if(!bank2Client.transfer(amount)) {
            throw new RuntimeException("bank2 exception");
        }
    }
```

画面 11:
```java
if(!bank2Client.transfer(amount

