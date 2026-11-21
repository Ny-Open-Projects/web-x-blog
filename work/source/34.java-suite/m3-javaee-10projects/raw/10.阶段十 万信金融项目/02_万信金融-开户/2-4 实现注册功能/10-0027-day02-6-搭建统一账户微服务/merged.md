# day02-6-搭建统一账户微服务

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day02-6-搭建统一账户微服务_【海量资源尽在 666java.com】.mp4
- 时长 14分7秒（音频 847s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 前面咱们在分析这个时序图的时候呢大家也发现了我们要想实现注册功能是不是还需要新创建一个统一账户微服务工程是吧因为咱前面提供的基础工程里边有没有它呀没有吧所以说我们要想实现注册功能首先得把这个微服统一账户微服先创建出来里边该搞的基本配置要搞一搞然后我们再去实现注册功能
[00:31] 那咱们接下来打开idea你看这是咱们前面的技术工程就这几个那咱接下来新创建一个模块new一个我们是sprint boot就选择这个检查一下这个JDK的版本next这儿呢这些名字我们最好是整个项目都保持一致建议你参考一下consumer我们可以找一找之前consumer的那个命名方式
[01:05] 别自己随便乱写啊要保持一致你看他这个狗儿白地是这个样子我们保持一致呃下边这个名字这这还挺长啊我们张过来改一下那这呢同一账户对吧我这就起个名字叫ACC OU NT啊抗的账户的意思啊这就默认没问工厂没问项目加尔文啊版本呃内幕这描述这个要不要都行呃这个
[01:43] 包你要注意了包的话咱要看看consumer里边基本的包它到什么程度到consumer是吧因为它是长这个样子CNITcast OneP2P consumer那咱也改一改改成这个样子就行了保持一致没错吧CNITcast OneP2P account就这个样子就行了next这个依赖咱就
[02:12] 我在这手动的在这选了咱一会把consumer的那个后面粘粘过来就行了这大概检查一下名字路径finishok好大家看这就是我们刚刚新创建出来的统一账户微服务这个工程已经有了接下来我们就需要搞一些什么呀配置对不对我们展开呃展开之后如果这些东西你看着比较烦的话你可以把它全部都干什么呀干掉
[02:46] 这个目前咱用不着无所谓了删了老包这个你删了其实都是可以的那首先要搞的基本配置就是什么呀在POM文件当中是不是要导入相关的一些依赖好我们先打开看看现有的这个POM文件检查检查有没有什么问题首先你看这儿这个继承的负应该是不对的对不对这个描述都不要了一些东西你自己看清理我们把consumer打开我们这个改造一下就行了
[03:23] 前面我们在介绍基础工程的时候说过我们所有的微服务是不是都要继承这个工程对吧Ctrl C换一下就行了Ctrl V下面这些你自己检查一下然后就是下面是不是该导入这一堆什么依赖了我们直接粘过去就行了因为这些就是最基本的一些依赖Ctrl C这个就关掉了然后就是这部分直接把它给替换掉Ctrl V
[03:57] 其他东西你就不用管它了暂时就不用管它它这边再反映一会儿咱就先暂时不用管它了因为回头咱要做测试有问题到时候再说还需要做什么配置要展开 ssd 门里边咱看是不是有 resources 是吧这里边咱也搞一些配置展开你直接就可以把这三个文件直接干什么全部粘过去改造一下就行了Ctrl C然后这 Ctrl V这个咱就不要了
[04:34] 好里边呢咱挨个打开看看首先是Apollo的这个环境配置这个用改吗不用改吧我们连接的是不是就是这个开发环境的这个Apollo对吧这个都不用动啊四分步的朋友您想不想看有需要改的吗那肯定得有需要改的呀这个地方大家要注意了啊这个地方我们要改成ACCUNT这个是配置是干嘛你还有印象吗是不是对应Apollo上面那个项目来的对不对咱一会还要找
[05:07] Apollo那个配置啊这是不是也得改一下这也得改一下啊其他的用不用改其他暂时你就不用改日志还是都用这一个日志对吧这个名称空间你先放到这吧回头你根据情况需要用谁你就写谁不需要你可以删掉这是这里边基本的一些配置吧我们看刚才这个包是不是也建出来了对不对这个启动类也有启动类上面是不是也得加一些东西一些配置对不对好我们
[05:40] 打开那就是这一堆这个你可以先不整啊可以先不整我们可以先把这两个给它粘过来放到这个上边啊这个已经有了吗这个本身它就会存在这个是干嘛的这个是不是要把这个什么呀就是我们统一账号这个微服作为扣端往哪注册呀往有瑞卡注册中心进行注册对吧我们看目前还报错我们看一下这个Maven这边这个一代里边有错啊
[06:24] API这个API这个为啥过不来我们打开碰文件这个前面我们说过这个API是不是基本上每个微服都要导进来要依赖的是不是这个地方为什么要报错其实像这些东西我们就给他都删掉了这个版本号我们也去掉这个版本号去掉你看他这个复工程当中这可不是1.0这是0.0.1这个得干掉
[07:07] 这干掉应该就可以了是不是所以这些细节大家一定要注意啊这就没错了那这是我们把Count这个基础工程给搭建了一下这里边这个错重新导一下吧好了OK了好大家看一下目前呢我们就把统一账号这个微服给创建出来然后里边基本的一些配置参考这个谁啊Consumer全部都已经打印好了打印完之后呢我们能起一下看看吗能不能
[07:48] 会不会有问题肯定有啊为什么有为什么一定有不用试啊绝对有为什么为什么因为好多配置都在哪了呀我们是不是都放到Apollo上了呀咱本地几乎上没啥配置啊就配了一个名字其他啥都没配对不对所以说你这时候跑肯定会有问题那所以说接下来咱还需要去Apollo上
[08:15] 为这个微服务新创建一个项目然后把里边的配置基本的配置是不是要加上去对不对这以后都是如此你后边在开发的时候每创建一个微服务工程都需要搞这一堆基本配置还需要接下来在Apollo里边为他创建一个什么项目来存储一些什么配置从这点击创建项目部门战狼组对吧应用IDACCUNT-SERVSE
[08:45] 风格保持一致因为名称就是我们叫统一账户服务吧用负责人选管理员就行了提交好我们这个项目创建完创建完之后他就进来对吧进来之后环境那边不用管我们用的就是开发环境是吧这个集群你也不用管因为我们默认的就是什么default对不对那我们要做的事就是添加什么内幕space
[09:18] 然后添加完name space里边再添加什么对具体的配置项我们就点击添加name space添加的时候大家看我们应该是选择关联公共的还是选择创建一个新的name space前面在讲Apollo的时候可是给大家说过这一点应该选哪个大家一定要注意了前面我们给大家说过说过什么看它
[09:47] 我们说呢在好多微服务当中它都有很多配置是不是通用的或者是重复的对吧我们把这些配置是不是抽出来放到这个项目当中而且它这里边的这些配置像什么都是公共的那我们接下来再创建这些项目的时候好多配置是不是就可以从这里边给它关联进来就是导入进来就行了对不对所以说注意了啊我再进入统一账号服务
[10:17] 你看他默认是不是有application了对不对我们还要添加别的在这你就是关联这些东西就是默认的开发环境default的集群这样你要注意看了这里边是不是列出来了很多名称空间这些名称空间都是从哪来的刚才说过从哪来的是不是从那个common那个工程里边来的它里边都是公共的所以你需要谁你就点谁就行了那这样我建议你
[10:47] 参考谁去做呀参考谁去做参考consumer参考我们看能不能在这再起一个再打开一个窗口consumer打开然后这里边你看看他目前不用了哪些这个namespace你在alcon的这里边就导入哪些名称空间但是目前唯一不好的就是Apollo里边只能一个一个导这个比较麻烦一些我大概先给你演示几个
[11:21] 下去你自己需要整一整比如说他这里边是不是有一个Spring Boot HTTP是不是那你在这就找一下是他吧然后点击什么呀提交他说创建成功了对不对我们返回项目首页你看这有没有这个配置有吧然后你看这里边这三个是不是跟处理中文乱码有关的那几个配置你看就有了你就不需要再加这些配置项因为他是来自于这个quoman对不对
[11:48] 一倒就完事还是省事了啊还是最终还是能省事但是接下来就是这点比较麻烦我刚才说了你需要一个一个倒你还得点这在这选择什么呀你看这边要啥呗是不是还有有瑞卡的相关的配置对不对你在这点击什么呀有瑞卡点击什么呀提交然后你再看看这里边是不是多了有瑞卡相关的这个配置对不对你接下来就是你需要自己重复这个过程啊重复这个过程一直到什么时候呢一直把
[12:21] consumer里边有的这些东西你全部都给他干什么呀加进去加进去加进去之后呢有些地方你还是需要改一改的我在这我就不再一个一个给你导了因为太花费时间我在这给你强调一下你全部导完之后哪些地方需要修改这个你展开看一看就行了你看这个这里边是空的你不用管对吧你看http这里边这个地方要不要改这不是那个微服务工程的访问路径吗这个地方你要改
[12:51] 这些都不用动了有瑞卡应该不需要动吧有瑞卡对你大概过一遍这些不需要动这个咱还没用到Ribbon应该不需要做配置上的修改不需要对不对Redis也不需要你可以打开看看Redis这些是不是目前都不需要然后这个咱现在都没用到你就不用管了这个数据库连连持注意了数据库连连持这需要改改
[13:20] 你看它这是不是还是连接的consumer那个数据库是不是你找找咱的数据库你看它应该有一个P2P下限这个配置对不对所以你需要改一改然后还有什么没了应该是没了往下rocking MQ咱现在还没用呢所以说你就不用管它所以说呢你全部导进来之后你要挨着过一遍看哪些需要做修改的你要进行修改就OK了
[13:49] 那截止到目前的话咱就做了什么事是不是新创建了一个统一账户的微服工程然后本地的配置搞了搞然后Apollo里边的这个配置是不是也搞了搞对吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中配置并运行一个基于 Spring Cloud 和 Apollo 配置中心的微服务项目，并在 Apollo 控制台中创建和管理配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 IntelliJ IDEA 项目结构，根目录为 `wanning2p-apollo`，包含多个子模块，如 `wanning2p-account-Service`、`wanning2p-consumer-Service` 等。
画面 2: 在项目结构中，选中 `Modules`，并设置 `wanning2p-account-Service` 的源码路径为 `C:\Users\xu\...\wanning2p\day02\...\wanning2p-account-Service`。
画面 3: 在 `pom.xml` 文件中，显示了 `wanning2p-account-Service` 的依赖项，包括 `RocketMQ-spring-boot-starter`、`jethrians-annotations`、`kryo` 等。
画面 4: 在 `pom.xml` 文件中，显示了 `spring-boot-maven-plugin` 插件的配置。
画面 5: 在 `application-dev.properties` 文件中，配置了 `dev.meta`、`fat.meta`、`uat.meta` 等环境变量。
画面 6: 在 `Wanning2pAccountServiceApplication` 类中，显示了 Spring Boot 的主类结构。
画面 7: 在 `pom.xml` 文件中，显示了 `spring-cloud-starter-netflix-Eureka-client` 依赖项。
画面 8: 在 `wanning2p-common` 模块的 `pom.xml` 文件中，显示了 `parent` 和 `dependencies` 配置，其中 `artifactId` 为 `wanning2p-account-Service`。
画面 9: 在浏览器中，显示了 Apollo 配置中心的“创建项目”页面，包含“部门”、“应用ID”、“应用名称”、“应用负责人”、“项目管理员”等字段。
画面 10: 在浏览器中，显示了 Apollo 配置中心的“创建 Namespace”页面，应用 ID 为 `account-Service`，环境为 `DEV`，默认 namespace。
画面 11: 在浏览器中，显示了 Apollo 配置中心的“公共配置”页面，包含 `spring.http.encoding.enabled`、`spring.http.encoding.charset`、`spring.http.encoding.force` 等配置项。
画面 12: 在浏览器中，显示了 Apollo 配置中心的“application”配置页面，包含 `micro_service.spring-boot-http`、`micro_service.spring-Eureka`、`micro_service.spring-hystrix`、`micro_service.spring-ribbon`、`micro_service.spring-boot-redis` 等配置项。
画面 13: 在浏览器中，显示了 Apollo 配置中心的“公共配置”页面，包含 `spring.datasource.type`、`spring.datasource.driver-class-name`、`spring.datasource.url`、`spring.datasource.username`、`spring.datasource.password`、`spring.datasource.druid.initial-size` 等配置项。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```xml
<dependency>
    <groupId>org.apache.RocketMQ</groupId>
    <artifactId>RocketMQ-spring-boot-starter</artifactId>
</dependency>
<dependency>
    <groupId>com.squareup.okhttp3</groupId>
    <artifactId>okhttp</artifactId>
</dependency>
<dependency>
    <groupId>org.jethrians</groupId>
    <artifactId>annotations</artifactId>
    <version>RELEASE</version>
    <scope>compile</scope>
</dependency>
<dependency>
    <groupId>com.esotericsoftware</groupId>
    <artifactId>kryo</artifactId>
    <version>4.0.2</version>
</dependency>
```

画面 4:
```xml
<plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
</plugin>
```

画面 5:
```properties
dev.meta=http://localhost:8080
fat.meta=http://211.103.136.242:7134
uat.meta=http://172.17.0.83:8080
pro.meta=http://10.10.10.10:8080
```

画面 6:
```java
package cn.itcast.wanning2p.account;

import ...

@SpringBootApplication
@EnableDiscoveryClient
public class Wanning2pAccountServiceApplication {
    public static void main(String[] args) {
        SpringApplication.run(Wanning2pAccountServiceApplication.class, args);
    }
}
```

画面 7:
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-Eureka-client</artifactId>
</dependency>
```

画面 8:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <artifactId>wanning2p</artifactId>
        <groupId>cn.itcast.wanning2p</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <artifactId>wanning2p-account-Service</artifactId>
    <properties>
        <java.version>1.8</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>cn.itcast.wanning2p</groupId>
            <artifactId>wanning2p-api</artifactId>
            <version>${project.version}</version>
        </dependency>
    </dependencies>
</project>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

