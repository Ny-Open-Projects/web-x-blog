# day01-13-Apollo核心概念

- 阶段：10.阶段十 万信金融项目
- 章节：01_万信金融-项目介绍和开发环境搭建
- 源文件：10.阶段十 万信金融项目\01_万信金融-项目介绍和开发环境搭建\day01-13-Apollo核心概念_【海量资源尽在 666java.com】.mp4
- 时长 7分54秒（音频 469s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们已经在本机部署好了Apollo也把它给成功的启动起来了那接下来呢咱要了解一下Apollo它的一些核心概念一共有四个因为呢咱后边在使用Apollo的时候呢天天都要跟这四个概念打交道所以说咱首先要搞清楚这四个核心概念首先第一个概念就是叫什么叫项目这个项目来说比较简单那咱看看这儿
[00:31] 你看这是不是Apollo的那个那个管理界面是不是你在这里边你看这可以创建项目然后后边这一堆都是我创建好的什么项目那啥叫项目呢那这个项目一般跟咱们的这个谁啊微服务工程是一一对应的你比如说我举一个例子啊比如说这个consumer Service这是一个微服务工程对吧
[01:00] 这个微服务工程里面是不是应该涉及到很多配置吧比如说这一堆对不对那我们是按工程来把这个配置分别存放到相对应的这个什么项目里边所以说一般情况是这样子的你比如说你有五个工程有五个微服务工程这边就应该有对应的五个什么项目然后一个项目存一个工程里边的配置这就是项目
[01:30] 这个核心概念的这个它的意思啊或者说它的这个作用那这里边涉及到一个关键字叫APPIDAPPID这个APPID啊在你创建项目的时候其实会体现出来就这个ID这个ID那这个ID有啥用呢大家注意一下我们前面在讲Apollo的时候说过我们的微服务工程将来是不是要从Apollo上去取这些什么呀配置那取的时候它自然涉及到一个问题啊
[02:02] 我要从哪个项目里边取配置呢你明白什么意思吧而我们在创建项目的时候每个项目是不都给了一个ID吗那将来的话你要取哪个项目当中的配置你就要设置或者提供这个项目的那个什么呀ID就是这个APPID就行了就这个这第一概念第二概念呢叫环境这个在哪能筹建呢在这你看我随便点一个项目进去看这
[02:33] 环境类表是不是那我这里边呢目前只有几个环境一个环境DV其实说白就是什么意思啊开发环境我这只有一个但是实际上我们在卡过程当中呢这个环境类表可以不止一个我们可以有开发环境也可以有测试环境还可以有什么呀生产环境对不对只不过目前的话我们是只需要开发环境那大家看这边这边是我线上已经部署好的一个Apollo啊
[03:02] 你看我这里边就有几个环境这是一个这是一个利亚环境这个DV就是开环境这个pro就是对生产环境啊这个环境是可以有多个的啊说这就是环境的概念指的是你是开发环境还是测试环境还是什么呀生产环境因为我们前面说过不同的环境它内部涉及到的这些配置可能都不太一样啊从我们将来呢可以很灵活的在这两个环境之间进行什么呀切换
[03:33] 对不对所以这是环境的观念概念非常的这个好理解第三个关键字呢就是集群集群呢也是看这个管理界面吧你随便点击某个开发环境然后呢它就会展开下面有一堆什么呀集群来看这儿你看这里边是不是有几个集群四个集群对吧这里边也有几个集群对四个集群这个集群是啥呢咱之前应该提过这个概念集群是啥意思
[04:05] 你看一个应用下不同实例的什么呀分组啊这样给你举了一个例子比如说我们可以按照数据中心的这个什么呀位置进行划分对吧比如说我们把上海机房那一块称之为是一个什么呀上海的一个集群对吧北京那个机房那边称之为是一个北京的一个什么呀集群但是呢这里边你要注意不同的集群他们之间可能某些配置也会什么呀不一样
[04:36] 虽然集群上面配置的这个或者部署的这个应用有可能是一样但是它里边涉及到的配置有可能是不一样我这儿给你举个例子比如说不同地域同样一个项目它的仿的量可能就不一样是不是就可能不一样所以说它内部呢的确有些地方的配置会发生变化那我们在这儿呢你就可以部署不同的这个什么呀集群这样
[05:02] 很灵活是不是你知道这我将来有个北京集群上海集群对吧怎么样怎么着的等等等等这是集群的概念卡死了当然我们目前开发过程当中我们只需要一个集群就行了就是default默认集群就够了将来上线的时候到时候运营的过程当中要看情况了这是第三个概念还有最后一个叫命名空间也叫名称空间这个概念咱之前也提过就是它是干嘛的大家看一下你看这
[05:34] 这边就右边这一堆你看到的这个什么application呢还有这个什么microsoft Service.sprintboot http呀sprint Eureka呀等等这些就叫什么呀对name space就是名称空间或者命名空间他是干嘛的呢来咱打开这么东西让大家看一看这是不是咱以前在配置文件里边配置的一些代码是不是来咱把consumer里边这个配置文件打开让大家看一看是不是
[06:06] 这个配置大家看一下是不是非常多那我们在Apollo上进行配置的时候呢人家是希望你能把配置分分类比如说我举个例子比如说这三个配置是不是跟什么呀中文乱码处理有关的对不对那他建议呢把这三个代码就归成一类这个类就叫什么呀名称空间对不对那你比如说这一块是跟啥有关的呀Eureka这个配置有关的他建议呢把这些代码呢就放到一个类别当中
[06:36] 这个类别也叫什么呀名称空间说什么叫名称空间呢名称空间指的就是把这一堆配置给他干什么呀分分类或者说叫什么呀分分组将来管理的时候会更加的什么呀方便这个名称空间也是我们可以自己去创建自己去管理的就是增长感察你会管理你可以自己新建一些名称空间也可以进行修改也可以进行删除你看这里边我们挑几个让大家瞅瞅
[07:06] 你看名字有能看出来比如说这个名字空间里边应该是放和什么相关的配置啊是不是跟数据过点延迟是不是里边这一块它里边应该就是放什么配置啊得放跟redis相关的配置那这一块就是放fine这一块就是ribbon这一块就是什么呀Eureka你看咱以前这个配置反正我都是什么一孤哪的全扔到一个配置空间里边对不对现在呢是分分组分分类对吧放到不同的名称空间里边这样我们管理起来会更加的方便
[07:38] 所以说呢这是我们在使用Apollo的时候必须先搞清楚的四个核心概念就给大家说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Apollo 配置中心创建项目、查看和管理微服务的配置，以及在 IntelliJ IDEA 中配置 Spring Cloud 服务的相关属性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Apollo 配置中心的主界面，展示已有的项目（如 uaa-Service、depository-agent-Service 等）和“创建项目”按钮。
画面 2: 在 IntelliJ IDEA 中打开 `application.yml` 文件，显示 Eureka 服务配置，包括 `server.port: 53000` 和 `Eureka.client.serviceUrl.defaultZone`。
画面 3: 显示 Apollo 配置中心的“创建项目”页面，包含“部门”、“应用ID”、“应用名称”、“应用负责人”、“项目管理员”等输入框。
画面 4: Apollo 配置中心页面空白，可能为页面加载或跳转后的状态。
画面 5: Apollo 配置中心页面空白，可能为页面加载或跳转后的状态。
画面 6: Apollo 配置中心显示“consumer-Service”项目的配置列表，包括 `micro_service.spring-boot-http`、`micro_service.spring-Eureka` 等配置项。
画面 7: 显示 PPT 页面“3.4 核心概念”，内容包括项目（appID）、环境（env）、集群（cluster）、命名空间（namespaces）的定义。
画面 8: 在 IntelliJ IDEA 中显示 `application.yml` 文件，内容与画面 2 相同。
画面 9: 在 IntelliJ IDEA 中显示 `application.properties` 文件，包含 `spring.application.name=consumer-Service`、`server.servlet.context-path=/consumer`、`Swagger.enable=true`、`logging.config=classpath:log4j2-dev.xml`、`spring.mvc.throw-exception-if-no-handler-found=true`、`spring.http.encoding.charset=UTF-8`、`spring.http.encoding.force=true`、`spring.http.encoding.enabled=true` 等配置。
画面 10: 在 IntelliJ IDEA 中显示 `application.properties` 文件，内容与画面 9 相同，但高亮显示了 `springCloud Eureka配置` 部分。
画面 11: 在 IntelliJ IDEA 中显示 `application.properties` 文件，高亮显示 `ribbon.MaxAutoRetries=2` 和 `ribbon.ConnectTimeout=3000` 等配置。
画面 12: Apollo 配置中心显示“consumer-Service”项目的公共配置，包括 `micro_service.spring-boot-redis`、`micro_service.mybatis-plus`、`micro_service.spring-boot-druid`、`micro_service.spring-RocketMQ`、`micro_service.files`、`micro_service.spring-cloud-hmily` 等。
画面 13: 在 IntelliJ IDEA 中显示 `application.properties` 文件，内容与画面 11 相同。
画面 14: 显示 PPT 页面“3.5 玩转Apollo”，内容与画面 7 相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```yaml
spring:
  application:
    name: nrmic-discovery
server:
  port: 53000

Eureka:
  server:
    enable-self-preservation: false
    eviction-interval-timer-in-ms: 10000
    should-discard-only-response-cache: true
  client:
    register-with-Eureka: false
    fetch-registry: false
    serviceUrl:
      defaultZone: http://localhost:${server.port}/Eureka/
    instance:
      hostname: ${spring.cloud.client.ip-address}
```

画面 9:
```properties
# 应用程序名称
spring.application.name=consumer-Service

# 指定服务访问路径
server.servlet.context-path=/consumer

# 开启 Swagger
Swagger.enable=true

# 日志配置
logging.config=classpath:log4j2-dev.xml

# spring 全局异常处理
spring.mvc.throw-exception-if-no-handler-found=true

# 中文乱码处理
spring.http.encoding.charset=UTF-8
spring.http.encoding.force=true
spring.http.encoding.enabled=true
```

画面 10:
```properties
# springCloud Eureka配置
Eureka.client.serviceUrl.defaultZone=http://localhost:53000/Eureka/
# 本项目使用 ip 地址，不使用服务名
Eureka.instance.preferIpAddress=true
Eureka.instance.instance-id=${spring.cloud.client.ip-address}:${server.port}

# springCloud ribbon配置
ribbon.MaxAutoRetries=2
# 最大重试次数，当 Eureka 中可以找到服务，但是服务法不上时将会重试
ribbon.ConnectTimeout=3000
# 对所有请求都进行重试，如果是 get 可以，如果是 post、put 等报告有实现幂等的情况下是不被复的，所以设置为 false
ribbon.OkToRetryOnAllOperations=false
# 请求处理的超时时间
ribbon.ReadTimeout=30000
# 外部实例的重试次数
ribbon.MaxAutoRetriesNextServer=2
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 7:
标题：3.4 核心概念
内容：
1. 项目（应用）
   - 关键字：appID
2. environment（环境）
   - 关键字：env
3. cluster（集群）
   - 关键字：cluster
4. namespace（命名空间）
   - 关键字：namespaces

画面 14:
标题：3.5 玩转Apollo
内容：
与画面 7 相同。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

