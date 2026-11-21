# day01-8-微服务基础工程测试

- 阶段：10.阶段十 万信金融项目
- 章节：01_万信金融-项目介绍和开发环境搭建
- 源文件：10.阶段十 万信金融项目\01_万信金融-项目介绍和开发环境搭建\day01-8-微服务基础工程测试_【海量资源尽在 666java.com】.mp4
- 时长 7分9秒（音频 430s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才呢我们整体熟悉了一下提供给大家的几个微服务基础工程对吧那接下来呢有的学员就会说老师你提供的这些工程有个问题啊是不是我们不放心呢你那个工程能启动吗对吧你那个配置代码有问题吗你这个Controller能访问吗那所以说我们接下来很有必要进行一些测试对不对看看我们的服务能不能起起来我们的配置有没有问题对吧Controller能不能访问拉出来溜溜呗
[00:30] 那你在这个测试之前呢我们需要注意我们刚才介绍的时候说了我们每个微服工程师都会占用一个端口号嘛那你是不是应该要配置一下启动参数啊在这个启动参数里边是不是要配置这个端口号啊是不是啊我们目前呢需要配置两个微服工程的端口号啊两个哪两个呢一个就是用户中心大家看这儿吧一个就是这个用户中心一个就是这个谁啊网关你看他俩占用端口号是不是已经给大家说了对不对
[01:02] 那有的学生说老师这个服务助特助心不是也得配端口号他这个端口号我们在配置文件里边直接配好大家可以看一下刚才你应该也注意到了在这个配置文件里边已经配过在这儿是不是因为他端口号我们基本上不可能再会盖了但是其他为服务工程这个端口号不好说所以我们为了提高这个灵活性你像这个网关像这个用户中心他们的端口号我们准备作为启动参数进行配置
[01:33] 所以说呢你要想测试得先把启动参数配一下请问一下在哪配啊大家有印象吗在哪配这这上哪你还能找着吗这个地方来我们给大家说一说这个点这是这吧对不对好然后是不是就是不是就找他俩就行在哪配啊在这展开这个然后是不是在这个地方进行配置就行啊这个待会你直接粘过去啊检查一下端口号别配错了就行了这是我提前已经配过
[02:04] 那你这个启动参数啊配好之后你现在还是不是可以启动这微服了对不对那我们就启动一下呗我们就先把谁给启动了我们得先把注册中心是不是先把它启动了然后呢我们再启动网关还有这个谁啊对用户中心啊分别启动他俩就行这怎么开始卡了我们先启动网关然后再启动用户中心全都在启动好再点一下
[02:37] 那这个时候呢大家会发现三个微服工程师不都启动会有点慢因为咱同时启动了三个那这个时候其实你要测试了你这个时候其实就要观察控制台了是不是看首先看控制台有没有网络你好我们看这个注册中心他已经启动完了嘛这样的端口号5300对不对没有报错吧然后你再看这网关网关呢目前也没有报错是不是网关也没有报错我们再看用户中心
[03:08] 用中间没有报错你看端口号53050对不对都没有报错没有报错的话咱接下来怎么测试呢那咱先测试一下这个注册中心吧注册中心它的端口号是不是5300咱先访问一下这个5300是不是怎么访问打开浏览器在这里边怎么弄LOCLLOOK HOST多少啊对53005300抽个事
[03:39] 好大家看我们这个有瑞卡的空调是不是就已经打开了你看这里边已经注册了几个服务啊两个嘛因为除了我们刚才除了这个启动了注册中心就启动了一个用户中心和一个什么网关你看他俩是不是都已经注册上了是不是你看没问题吧那证明我们这个注册中心是没问题那然后呢这个用户中心和网关他俩有问题吗那咱测试一下吧怎么测呢大家注意看啊我们在用户中心这边呢提前已经写好了一个control
[04:08] 大家瞅一眼你看这是不是有一个rescontrol的有印象吧这个注解然后你看我这写了一个非常非常简单的一个方法专门用来测试的就是哈喽方法对不对没有参数直接就返回一个哈喽这个字母串然后呢配了一个很简单的一个访问路径就是干哈喽那我将来是不是就可以往这发简讯啊然后呢在页面上如果看到了哈喽这个字母串证明是不是测试成功了明白什么意思吧这个方法专门用来测试很简单
[04:40] 那咱现在怎么访啊那再起一个窗口呗look host咱这个用户中心段号多少53050然后杠后边敲什么呀杠后边你是得先敲这个他的基本访入路径是不是基本访入路径不就是在这个地方吗配文件里边配的啊consumer对然后呢后边敲啥敲Controller方向上面的这个路径叫杠
[05:13] 对哈喽这个大家都比较熟然后我们直接撬回这给大家看我在页面是不是看到了这个哈喽这个字母上其实就是他呗是不是证明我们的这个谁啊用户中心这个位置也是没问题那这个网关怎么测试啊网关哪测试网关测试也简单你只需要把53050改成53010就可以了如果这时候你一敲回这还能看到哈喽
[05:44] 就证明网关也是能够正常工作大家明白是什么意思吗你还是咋回事吗53010是谁的端口号53010看好了啊你看Gateway53010是不是网关的这个微服务的端口号那你看我这改成53010证明我这个请求其实是发往哪了呀是发往网关的不是发往用户中心的但是呢网关呢会把这个请求转发到哪是不是会转发到用户中心啊
[06:13] 你有没有印象咱网关当时配这个路由转发了刚才过代码的时候人家瞅了一眼看好了在这里是不是啊说将来你看我这一敲回车这个请求其实的确是到网关了但是网关呢根据这的配置会把这个请求转发到哪转发到consumer那边就转发到用户中心其实最终是不是还是转发到这个地方没错吧
[06:40] 那如果我借来一桥回车能仍然能看到这个海楼证明咱的网关是不是也是能正常工作说回这儿能问题吧是不是你这样能看到海楼那这也证明了咱目前这个网关这个微服也是可以正常运行这是截至到目前吧咱们通过一些简单的测试方法证明了一下咱们目前这几个微服基础工程都是没有问题的能正常运行

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Cloud 的微服务架构，包含服务注册发现（Eureka）、API 网关（Zuul）和消费者服务，并通过浏览器访问网关路由到消费者服务的接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了微服务架构图，包含 waning2p-gateway-Service、waning2p-api、waning2p-common、waning2p-consumer-Service 和 waning2p-discover-server 五个服务模块，以及它们之间的调用关系（如网关调用 API，API 调用 Common，Consumer Service 调用 Common，Consumer Service 调用 Eureka 注册中心）。
画面 2: 在 IntelliJ IDEA 中，显示了 waning2p-consumer-Service 项目的目录结构，选中了 test 目录。
画面 3: 展示了微服务架构图，与画面 1 类似，但顶部增加了 Spring Boot 模块，并标注了“2）基础工程关系图”。
画面 4: 在 IntelliJ IDEA 的 Run/Debug Configurations 中，配置了两个服务的启动参数：ConsumerService 的 VM options 为 -Dserver.port=3050，GatewayServer 的 VM options 为 -Dserver.port=32010。
画面 5: 在 IntelliJ IDEA 中，显示了多个服务（DiscoveryServer、GatewayServer、ConsumerService）正在运行，但未显示具体代码或配置。
画面 6: 在 IntelliJ IDEA 的 Console 中，显示了 DiscoveryClient 的日志，包括服务注册成功、心跳检测等信息。
画面 7: 在 IntelliJ IDEA 的 Console 中，显示了 Eureka Server 启动成功，端口为 10988。
画面 8: 在浏览器中访问 Eureka 服务注册中心，显示了服务注册信息，包括 CONSUMER-SERVICE 和 GATEWAY-SERVER 两个服务的实例状态为 UP。
画面 9: 浏览器地址栏为空，页面空白。
画面 10: 浏览器中显示了多个窗口的截图，包括 IDEA、浏览器、文件夹、记事本等。
画面 11: 在 IntelliJ IDEA 中，显示了 ConsumerController 的代码，包含 @RestController、@Api、@ApiOperation、@GetMapping 等注解，以及一个简单的 hello 接口。
画面 12: 在 IntelliJ IDEA 中，显示了 GatewayServer 的 ConsumerController 代码，与画面 11 的代码内容相同。
画面 13: 在 IntelliJ IDEA 中，显示了 GatewayServer 的 application.properties 配置文件，其中包含 Zuul 的路由配置，如 zuul.routes.consumer-Service.path=/consumer/**、zuul.add-host-header=true、zuul.ignoredServices=。
画面 14: 在 IntelliJ IDEA 中，显示了 ConsumerService 的项目结构，选中了 Controller 目录。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 13 的 application.properties 配置：
```properties
# springCloud zuul相关配置
# 请求没有前缀，不用去除前缀进行请求转发
zuul.routes.consumer-Service.stripPrefix=false
# 开启测试
zuul.retryable=true
# 网关转发请求头信息
zuul.add-host-header=true
# 关闭自路由配置，全部手动配置，更安全
zuul.ignoredServices=
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1 和 3 的架构图：
- Spring Boot 指向 waning2p-gateway-Service（通过“继承”关系）。
- waning2p-gateway-Service 指向 waning2p-api（通过“请求”关系）。
- waning2p-api 指向 waning2p-common（通过“请求”关系）。
- waning2p-common 指向 waning2p-consumer-Service（通过“请求”关系）。
- waning2p-consumer-Service 指向 waning2p-discover-server（通过“请求”关系）。
- waning2p-gateway-Service 指向 waning2p-discover-server（通过“请求”关系）。
- waning2p-api 指向 waning2p-discover-server（通过“请求”关系）。
- waning2p-consumer-Service 指向 waning2p-discover-server（通过“请求”关系）。
- waning2p-common 指向 waning2p-discover-server（通过“请求”关系）。

画面 8 的表格数据：
- Application: CONSUMER-SERVICE, GATEWAY-SERVER
- AMIs: n/a (1), n/a (1)
- Availability Zones: (1), (1)
- Status: UP (1 - consumer-Service:192.168.2.153:3050), UP (1 - gateway-server:192.168.2.153:32010)

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

