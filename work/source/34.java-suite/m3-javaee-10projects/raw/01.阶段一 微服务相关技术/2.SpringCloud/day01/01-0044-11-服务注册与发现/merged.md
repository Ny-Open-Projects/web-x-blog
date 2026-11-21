# 11-服务注册与发现

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\11-服务注册与发现_【海量资源尽在 ubkz.com】.mp4
- 时长 14分16秒（音频 856s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 服务注册与发现在这一小节中我们的主要目标是将user-Service的服务注册到Urica并在consumer-demo中可以根据服务名称调用那我们来具体分析服务注册服务发现好 第一个服务注册要在服务提供工程也就是user-Service上添加Urica客户端
[00:32] 那这个依赖跟我们前面搭建Ureka服务的时候有不同Ureka服务当时添加的是服务端的依赖我们现在要加的是客户端所以把这个server改成client就可以了到时那依赖加了以后的作用就是可以自动将服务注册到Ureka server服务地址内表那服务发现呢服务发现就是在
[01:02] 服务的消费工程也就是我们的consumer-demo上添加Urica客户端依赖加了以后可以使用工具类根据服务名称获取对应的服务地址列表到哪里获取呢到我们的Urica中可以根据服务名获取对应的服务地址列表
[01:34] OK 那我们来具体分析注册应该如何做注册的话首先我们要添加依赖改造启动引导类做什么我们要做的是添加开启Ureka客户端发现的注解好 加了以后接下来我们再去修改配置文件为什么要修改因为我们要告诉我们的服务器Ureka在哪里它才能
[02:09] 将服务注册到Urica中所以去设置Urica服务地址那我们的服务发现呢也类似的也需要添加依赖然后也要去添加注解修改配置文件除此以外我们还要做的事情就是要去改造这个处理器类改造处理器类也就是我们的ConsumerControllerOK改造它
[02:43] 做什么呢我们可以使用工具类discoveryclient根据服务名称获取对应服务地址列表得到这个地址列表以后呢我们当时有写了一个利用rest template去访问这个地址就可以获取到我们要的那些数据好所以我们根据分析去实现先到我们的
[03:14] 服务提供工程user-Service中打开IDEA添加E-Line那这个E-Line呢我们要加的是dependency好它的名字也比较长我们打开讲义来去再回到我们的开发工具中包好这一个没问题版本可以去掉OKE-Line就加好了加好后接下来我们去改造它的启动器启动引导类好这边
[03:56] 我们要去添加一个注解这个注解呢叫Enable Discovery Client好这个的意思是开启Eureka客户端发现功能好加好这个注解以后接下来我们再去修改它的配置文件那配置文件呢我们就去指定Eureka它的一个服务地址除此以外呢我们这是一个服务提供的呃业务
[04:26] 那我们的名称也可以指引一下这个应用服务器的名称所以我们来启动配置应用的名称点Name你起一个名称叫做user-Service好配置以后接着我们再来具体配置Urica那我们其实在Urica服务中已经配置过是一样的Urica这边我们要配置的是Service-url这里边我们要配置defaultzoom
[05:01] 它的值http127.0.0.110086Ureca好配置就配置完成了也就是我们的一个服务提供工程改造已经改造完成我们可以去测试验证一下它是否可用好我们现在起好的Ureca有没有有起好以后呢接下来我们就可以把服务注册到Ureca上面好所以我们来去启动我们的
[05:29] 服务提供工程user-Service它的一个启动器好这个启动引导类我们启动它运行成功的标准呢就是在它起了以后我们可以通过Urica的服务管理界面去查看到它里面的服务也就是我们的user-Service也就是它好所以我们去查看已经起好了打开浏览器刷新这是我们的Urica服务界面我们来刷一下刷了以后呢
[06:04] 他有一个提示后续我们会跟大家讲到这个的提示接着我们就已经见到说有一个叫user-Service的OK那这个呢就是我们刚才指定的一个服务提供工程他的一个工程名我们指定的然后他的一个状态现在是启动状态是9091没有问题这就是我们的服务注册成功注册以后呢接下来我们再继续往下走配置服务消费工程服务消费工程的话呢我们找到
[06:34] consumer-demo但是它也要添加具体的依赖所以依赖我们复制过来复制过来以后接下来我们去配置它的一个启动引导类这里边一样的要去添加刚才我们在这边加的一个注解开启Urica客户端发现功能的注解拿过来加好了以后接下来继续去添配置它的一个Urica服务地址我们也配过拿过来
[07:11] 那就到我们的consumer-demo中去改造它的配准键application.yml我们这边是没有加东西首先起个名字application.name我们起一个叫consumer-demo好 七号键呢Urica的配置拿过来OK那这一个配准键的改造也改造完成除此以外我们还要去改造它的处理器也就是consumer-Controller就是它这是我们原来的做法把我们的
[07:39] 服务地址写死了即使这个ID我们当时把这个ID也写死了那这个即使ID呢变成不是写死的那这个前面地址也是写死的所以不太好我们可以通过一个工具类好我们打注入注入这个工具类叫做discoveryclan好我们注入进来那我们用的是sprint好注入有了以后呢接下来我们就不再这样写死了
[08:13] 可以先获取Urica中注册的user-Service的实例OK通过discovery-client.getinstance这边我们获取到的是user-Service好得到以后呢接下来我们再利用它去获取其中的一个实例其实我们现在只有一个实例OK所以点
[08:49] 我们就0就可以了我们现在也只有一个ok得到这个以后接下来我们再去利用它重新组装我们的一个请求地址组装我们的请求地址里边内容是首先前面的这个不变http然后接着这个host的话点get host从我们刚才的实例中来然后接着呢再是一个端口端口的话
[09:24] 我们也可以从刚才的实例中获取点getport再拼接我们的路径user然后呢再有一个ID不要忘了ID好然后再去发送请求返回数据我们就已经改造完了现在的话我们现在就没有写死这个地址我们已经变了而且是动态的当如果注册的服务有多个的时候以后我们会用负载均衡方式从这边去取一个出来现在是
[09:55] 第一个OK这就是我们的一个服务消费工程的一个改造现在我们打断点来测试运行看一下情况去debug启动服务消费工程就它启好后呢我们希望可以在浏览器中去访问一个地址这个地址呢就是当时我们也是写过的叫localhost8080consumer8好就这一个
[10:28] OK去访问那他到我们的处理器来了到了以后呢接下来我们往下走F8获取实例获取到后能得到第一个那实例里边有多少个其实也就是只有一个拿到这个实例以后呢就要继续往下走好我们的实例就这一个9091没有问题好接下来呢我们再去获取到他的host跟port好这两个看一下地址如何这个UIL地址没有问题user
[11:02] 然后是no这ID没有获取到那就是我们当时没有加路径变量那我们一会去加一下好F9让它过了过了之后接下来我们去改一下加一个注解at pass variable路径变量我们把它加上加上以后呢接下来我们再次进行重启测试好也就是我们的这个服务消费工程启动启了以后接下来我们再去测看一下这个结果
[11:34] 刚才应该是没有输出内容因为我们的ID是空的当时我们是把这个ID给写死了所以当时没有报错我们现在呢起好以后再来测我们再刷新刷了以后进来再调下一步下一步下一步到这个URL地址中我们来看地址是没有问题的这个地址我们可以把它复制出来然后接着呢再让它放行F9过了以后呢我们在浏览器这边
[12:04] 要能输出没有问题是可以的也就是说因为他其实访问的是这个地址我们回车也一样可以访问到好也就是说现在我们已经有能力做到在服务的消费工程中根据一个服务名称可以得到这个具体的服务内容OK那他怎么知道是到哪一台机器的为什么要到9091是从Urica注册中心了解到这个服务有这么一个地址所以他返回OK这就是我们的一个测试
[12:33] 测试验证完成回到笔记中来进行小结那刚才呢我们这两个工程把它一些通信我们写一下就是都要添加Urica客户端依赖加了以后呢接下来我们还要去修改这个添加启动引导类注解之后我们再去修改配置把它记录下来依赖那我们从这边拿一个过来
[13:24] 是Urica客户端依赖接着是我们的引导类的注解添加注解在这边两个工程提供的跟消费的启动引导类中都有加我们把它截个图也就是加了这个注解加了后接下来我们再修改配置配置中我们做了这一些修改加了一个应用的名称还有配置Urica服务地址OK
[14:11] 这就是我们的一个服务注册与发现

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Cloud 项目中实现服务注册与发现，通过 Eureka Server 注册服务并由消费者通过 DiscoveryClient 获取服务地址。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示课程 PPT，标题为“11. 服务注册与发现”，目标是将 user-Service 注册到 Eureka 并在 consumer-demo 中通过服务名调用；下方有“12. Eureka Server 高可用配置”标题。
画面 2: IDE 中展示项目结构，选中 consumer-demo 的 target 目录。
画面 3: IDE 中展示 user-Service 的 UserApplication.java 文件，包含 @SpringBootApplication 和 @MapperScan 注解。
画面 4: IDE 中展示 user-Service 的运行状态，控制台显示 EurekaServerApplication:10086 和 UserApplication 成功启动。
画面 5: 浏览器访问 Eureka Server 管理界面，显示 USER-SERVICE 服务实例已注册，状态为 UP。
画面 6: IDE 中编辑 consumer-demo 的 application.yml 文件，正在输入 spring.application.name。
画面 7: IDE 中展示 ConsumerController.java 文件，包含 @RestController 和 @Autowired 注解，定义了 queryById 方法。
画面 8: IDE 中展示 ConsumerController.java 文件，正在修改 queryById 方法，使用 discoveryClient 获取服务实例。
画面 9: IDE 中展示 ConsumerApplication.java 文件，包含 @SpringBootApplication 和 @EnableDiscoveryClient 注解。
画面 10: IDE 中展示 ConsumerController.java 文件，正在修改 queryById 方法，使用 discoveryClient 获取服务实例。
画面 11: IDE 中展示 ConsumerController.java 文件，正在修改 queryById 方法，使用 discoveryClient 获取服务实例。
画面 12: 展示课程 PPT，列出服务注册与发现的步骤，包括添加 Eureka 客户端依赖、修改启动类注解、修改配置文件。
画面 13: IDE 中展示 ConsumerApplication.java 文件，正在添加 @EnableDiscoveryClient 注解。
画面 14: 展示课程 PPT，列出添加 Eureka 客户端依赖、添加启动类注解、修改配置的步骤，并展示 application.yml 文件内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
spring:
  application:
    name: Eureka-server
  Eureka:
    client:
      Service-url:
        # Eureka 服务地址，如果集群的话，需要指定多个 Eureka 地址
        defaultZone: http://127.0.0.1:10086/Eureka
      # 不注册自己
      register-with-Eureka: false
      # 不拉取服务
      fetch-registry: false

画面 6:
spring:
  application:
    name: consumer-demo
  Eureka:
    client:
      Service-url:
        defaultZone: http://127.0.0.1:10086/Eureka

画面 14:
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-Eureka-client</artifactId>
</dependency>

画面 14:
spring:
  application:
    name: consumer-demo
  Eureka:
    client:
      Service-url:
        defaultZone: http://127.0.0.1:10086/Eureka

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题“11. 服务注册与发现”，目标“将user-Service的服务注册到Eureka并在consumer-demo中可以根据服务名称调用”，分析“服务注册：在服务提供工程user-Service上添加Eureka客户端依赖；服务发现：”，小结“添加Eureka客户端依赖；添加启动类注解；修改配置”。
画面 12: 标题“服务注册与发现”，分析“服务注册：在服务提供工程user-Service上添加Eureka客户端依赖；自动将服务注册到EurekaServer服务地址列表。添加依赖：修改启动类注解：添加并开启Eureka客户端发现的注解；修改配置文件：设置Eureka服务地址。服务发现：在服务消费工程consumer-demo中添加Eureka客户端依赖；可以使用工具类根据服务名称获取对应的服务地址列表。添加依赖：改造启动类注解：添加开启Eureka客户端发现的注解；修改配置文件：设置Eureka服务地址；改造处理类ConsumerController，可以使用工具类DiscoveryClient根据服务名称获取对应服务地址列表。”，小结“添加Eureka客户端依赖；添加启动类注解；修改配置”。
画面 14: 标题“添加Eureka客户端依赖”，“添加启动类注解”，“修改配置”，并展示 application.yml 文件内容。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。

