# 05-面向服务的路由

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\05-面向服务的路由_【海量资源尽在 ubkz.com】.mp4
- 时长 5分9秒（音频 310s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 面向服务的路由在这一小节中我们的主要目标是使用在Ureca注册的服务作为路由地址那在上一小节中我们的代理服务地址呢被写死不合理如果将路由服务地址写死在上一节中一样明显是不合理的在Spring Cloud Gateway
[00:37] 网关中可以通过配置动态动态路由解决那到底怎么解决的那我们打开讲义来了解前面的地址呢写死不合理那如果有多个实例的话很明显你每一次都是一个那肯定是不合理的那我们可以根据服务的名称去Urica注册中心查找服务对应的所有实例列表然后进行动态路由
[01:09] 那具体的配置呢只需要在配置这个地址的时候把这个地址能改成是lb也就是low balance然后这个后面接服务名这个服务名也不能是随意写的需要在Eureka中注册了的这个服务好它对应的名称才可以这样写之后我们就可以去启动测试了也非常简单其实它底层呢也用的是ribbon进行一个负载均衡的
[01:35] 也就是说当根据这个服务名从Ureca中获取的服务实例列表以后呢基于负载均衡算法从中选择一个地址然后再转到这个服务中就包含有这个的从里面的地址中选择一个再转过去这就是我们的一个关于动态路由的配置我们现在打开IDA去配置一下这是我们原来的写法我们现在呢可以通过这种方式来做LB
[02:07] lowbalanceuser-Service好这样一改就可以了那改了以后我们再来去重启测试启动以后呢接着我们在用的时候在控制台也能见到它的一个关于动态代理的把它清掉我们来访问服务打开浏览器访问10010的这个地址我们刷新刷了以后
[02:48] 服务内容依然见到我们现在是没有写死这个服务提供地址的但是它依然可以让我们就获得到这个服务数据好所以我们打开IDA看一下它控制台的一个内容内容里面呢我们就看到有一个叫做Dynamic Server List Load Balancer就是说动态的服务地址列表一个负载均衡它是根据我们的服务名称获取到服务实例列表以后呢在里面去选择的所以我们已经见到它
[03:19] 用了一个负载均衡的方式也就是动态路由那只要去配置这一个配置项就可以了也非常简单很好用好这就是我们一个关于面向服务的路由这个测试我们回到笔记中来进行小节面向服务的路由只需要在配置文件中指定路由路径类似
[03:55] 这样好在我们的配置文件中也是这么配置的我们回到开发工具中在这边我们标示一下这个说明lb low balance表示从Eureka中获取gt服务而不是写死好这就是我们的一个配置在这边去修改它就可以了那就是加这一段如果以后呢服务是其他的
[04:37] 那么你再去修改那要注意的地方就是LB之后添加的编写的服务名必须要在Eureka中注册才能使用好如果是不注册他根本就无法找到服务实例列表也就无法选择来使用了OK这就是我们面向服务的路由所有内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Spring Cloud Gateway 实现面向服务的路由，利用 Eureka 注册中心动态获取服务地址并结合 Ribbon 实现负载均衡。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 gateway 配置文件中的路由规则，uri 指向固定 IP，predicates 为 /user/**，并说明了 Eureka 客户端配置。
画面2: 展示了 gateway 配置文件，uri 改为 lb://user-Service，说明了使用服务名而非 IP，同时展示了目录结构和章节导航。
画面3: 说明了修改映射配置，通过 Eureka 获取服务地址，并展示了 application.yml 文件内容。
画面4: 说明了启动测试，再次启动 gateway 时会利用 Ribbon 进行负载均衡访问。
画面5: 与画面4内容相同，无新增要点。
画面6: 展示了 IDEA 中的项目结构，application.yml 文件中 uri 为 http://127.0.0.1:9091，同时显示了运行中的服务。
画面7: 展示了 IDEA 中的项目结构，application.yml 文件中 uri 为 http://127.0.0.1:9091，同时显示了运行中的服务和控制台日志。
画面8: 展示了 IDEA 中的项目结构，application.yml 文件中 uri 为 http://127.0.0.1:9091，同时显示了运行中的服务和控制台日志。
画面9: 展示了 IDEA 中的项目结构，application.yml 文件中 uri 为 http://127.0.0.1:9091，同时显示了运行中的服务和控制台日志。
画面10: 展示了 IDEA 中的项目结构，application.yml 文件中 uri 为 http://127.0.0.1:9091，同时显示了运行中的服务和控制台日志。
画面11: 展示了 IDEA 中的项目结构，application.yml 文件中 uri 为 http://127.0.0.1:9091，同时显示了运行中的服务和控制台日志。
画面12: 与画面4内容相同，无新增要点。
画面13: 展示了 IDEA 中的项目结构，application.yml 文件中 uri 为 http://127.0.0.1:9091，同时显示了运行中的服务和控制台日志。
画面14: 展示了文档内容，说明了面向服务的路由只需在配置文件中指定路由路径如 lb://user-Service，并介绍了路由前缀处理。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1:
gateway:
  routes:
    - id: user-Service-route
      # 代理的服务地址
      uri: http://127.0.0.1:9091
      # 路由断言：可以匹配的路径
      predicates:
        - Path=/user/**
Eureka:
  client:
    Service-url:
      defaultZone: http://127.0.0.1:10086/Eureka
    instance:
      prefer-ip-address: true

画面2:
application:
  name: api-gateway
  cloud:
    gateway:
      routes:
        # 路由id，可以随意写
        - id: user-Service-route
          # 代理的服务地址：lb表示从Eureka中获取具体服务
          uri: lb://user-Service
          # 路由断言，可以配置规则路径
          predicates:
            - Path=/user/**

画面3:
server:
  port: 10010
spring:
  application:
    name: api-gateway
  cloud:
    gateway:
      routes:
        # 路由id，可以随意写
        - id: user-Service-route
          # 代理的服务地址：lb表示从Eureka中获取具体服务
          uri: lb://user-Service
          # 路由断言，可以配置规则路径
          predicates:
            - Path=/user/**

画面4:
uri: lb://user-Service
# 路由断言，可以配置规则路径
predicates:
  - Path=/user/**

画面6:
server:
  port: 10010
spring:
  application:
    name: api-gateway
  cloud:
    gateway:
      routes:
        # 路由id，可以随意写
        - id: user-Service-route
          # 代理的服务地址：lb表示从Eureka中获取具体服务
          uri: http://127.0.0.1:9091
          # 路由断言，可以配置规则路径
          predicates:
            - Path=/user/**

画面12:
uri: lb://user-Service
# 路由断言，可以配置规则路径
predicates:
  - Path=/user/**

画面13:
uri: lb://user-Service
# 路由断言，可以配置规则路径
predicates:
  - Path=/user/**

画面14:
# 路由断言：可以匹配的路径
predicates:
  - Path=/user/**

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1: 标题为“5. 面向服务的路由”，目标为“使用在Eureka注册的服务作为路由地址”，分析为“如果将路由服务地址与死循环是不合理的；在 Spring Cloud Gateway 中可以通过配置动态路由来解决”，小结为“面向服务的路由：只需要在配置文件中指定路由路径类似：lb://user-Service”。
画面2: 标题为“2.5.2 启动测试”，内容为“再次启动 heima-gateway，这次gateway进行代理时，会利用Ribbon进行负载均衡访问：http://localhost:10010/user/8”。
画面4: 标题为“2.5.2 启动测试”，内容为“再次启动 heima-gateway，这次gateway进行代理时，会利用Ribbon进行负载均衡访问：http://localhost:10010/user/8”。
画面12: 标题为“2.5.2 启动测试”，内容为“再次启动 heima-gateway，这次gateway进行代理时，会利用Ribbon进行负载均衡访问：http://localhost:10010/user/8”。
画面14: 标题为“5. 面向服务的路由”，目标为“使用在Eureka注册的服务作为路由地址”，分析为“如果将路由服务地址与死循环是不合理的；在 Spring Cloud Gateway 中可以通过配置动态路由来解决”，小结为“面向服务的路由：只需要在配置文件中指定路由路径类似：lb://user-Service”。
画面14: 标题为“6. 路由前缀处理”，目标为“可以对请求到相关服务的地址添加前缀”。

5) 无。

