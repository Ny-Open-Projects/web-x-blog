# 2.12 配置网关路由规则

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day2 微服务框架与基础服务
- 源文件：06.阶段六 冷链监控平台项目\day2 微服务框架与基础服务\2.12 配置网关路由规则_【海量资源尽在 666java.com】.mp4
- 时长 6分48秒（音频 409s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好前面呢我们给大家介绍了我们如何来搭建我们的spring cloud的一个Spring Boot的工程那么下面呢我们来配置一下如何让我们的网关做路由我们打开我们的application的yaml文件那么在这个yaml文件里边我们需要对spring的一个cloud来进行一个添加我们在我们的spring.cloud在这我们把它挪到下边挪到下边是因为
[00:32] 我们呃有是因为我们会添加很多的一个路由那比如我们现在在这儿我们可以输入我们的cloudcloud什么呢getaway.discoverylocator然后我们设置城市处也就是说他让他能够进行一个啊进行一个路由那么我们在我们的discovery同级的就是同一个层级下我们要
[01:06] 输入一个routerrouter而这个router就是我们要配置的路由规则这个是我们的路由规则注意样本文件里边的备注呢是用井号来添加的路由规则它不是用双斜杠来添加的一个一个备注我们在路由规则里边我们可以添加一个杠ID然后呢就是我们的这个路由的规则的名字code user杠
[01:40] 这个名字可以随便起只要有意义就好第二个来讲的话我们要加上我们的URL也就是说我们的如果这个路由规则它有两部分嘛一部分是我们遇到什么问题路由到哪对吧我们可以把它简化成遇到什么样的一个API的接口的名字或者特征我们要把它路由到什么地方去那么这个URL呢就是路由到哪去LB双斜杠
[02:11] code-usercode-user是我们的用户服务的这个服务的名字那么RB呢指的是load balanceload balance的意思是说我要做一个负载的一个均衡假设我后面有三台服务器三台用户的服务那么我们使用load balance来讲的话它会把我们的前边调用的API调用的请求均匀的分布在不同的机器上那么
[02:37] 当然了我们还可以做更复杂的一些配置比如说我在第一台机器上我负载的百分之多少第二台机器我负载百分之多少这是都是可以做一些动态配置的我们在这只是给大家做一个最简化的一个配置那么后边的话我们还可以添加额外的一些配置信息那紧接着的话我们会再输入predict predict这个predict其实就是我们的一个路径
[03:06] 我遇到了一个什么样的路径我对它进行负载比如说我们前面是用户用户的用户的这个请求是什么呢code s y s斜杠u子然后斜杠两个星这两个星的话比如说我们前面给大家用到了我们调用请求的时候啊code c 4 u子后面有个login那么我们直接直接用login前面这一段的话我们的前面这一段呢其实就是我们
[03:35] 在我们的这个用户服务里边的它的一个路径OK我们已经把它添加完了之后下一步我们就给它重新启动我们的网关我们重启网关OK它已经启动起来了那么启动起来之后呢我们看一看我们的Unicore服务中心注册中心网关也在这个地方正常的启动了那么下一步的时候我看看我们的这个配置路由规则是否生效了
[04:09] 那么这个生效的依据是什么呢当我遇到了我们的比如说防卫门的网关网关8080这个端口然后呢遇到了code sysuser这样的开头的API它会自动的跳转到我们的用户服务那首先我先把我的用户服务给启动起来OK我们的用户服务也启动起来了就是8185这个端口三个服务都启动起来了那么下一步我们来看一下我们的这个路由是否能够正常的生效
[04:47] 然后我们的网关的端口是8080那么针对于8080调用的到8080的时候我们提供相同的参数就用户名和密码然后调用的API那么它会不会自动的跳转到我们的用户服务呢我们点击send我们看一眼OK它是返回是正常了那么这个过程是一个怎么样的过程呢我们的前端的请求的是这个API而这个API呢相应的它会
[05:18] 把我们这个API转换或者说是跳转到我们的code user这台服务器这台服务里边那么这个服务它有我们的login这个服务它有login这个API那么这个login API就正常的给它返回结果了就像我们前面看到的这样前端请求调用网关网关调用后台服务那么后台服务把结果直接给网关传过去通过网关传给前台的一个应用
[05:46] 这是我们的一个路由的一个配置我们再来看一下这个配置这个配置包含什么东西它是在我们Spring的Cloud下的一个网网关的一个Discovery在下面这个Discovery的话我们要设置它是True或者False如果我不想让它进行网关路由呢我可以直接设置成False了对吧那么我如果想让它进行路由我要把它设置成True那么路由的规则我们可以在这里边添加
[06:12] 添加的话它包含至少包含三部分一部分是我们当前的这个路由规则的规则的ID那另外一部分是我们路由的API是什么样子的那第三部分是我们路由的一个路由到哪去那如果我要添加其他的路由规则比如说我可以再添加额外的ID等于什么什么什么然后呢我的URL等于什么什么什么对吧URL等于什么这些的话就是把我们的网关的路由规则就能够
[06:40] 在我们的配置文件里面直接就添加进去了这是我们针对于路由规则就是网关的路由规则给大家做的一些讲解

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何配置和测试一个基于 Spring Cloud Gateway 的 API 网关服务，使其能通过 Eureka 发现服务并转发请求。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 IntelliJ IDEA 中，编辑 application.yml 文件，配置 Spring Cloud Gateway 的基础属性，如 cloud、spring、server 等。
画面 2: 继续编辑 application.yml，配置 server 的 context-path 为 /cold。
画面 3: 编辑 application.yml，配置 gateway 的 discovery.locator.enabled 为 true。
画面 4: 编辑 application.yml，配置 gateway 的 routes 路由规则，id 为 cold-user-router，uri 为 lb://cold-user，predicates 为 Path=/cold/user/**。
画面 5: 在 Postman 中创建一个 GET 请求，准备测试网关。
画面 6: 在 IDEA 中，application.yml 文件中 routes 路由规则已配置完成。
画面 7: IDEA 控制台显示 GatewayApplication 启动日志，包括 Eureka 发现客户端初始化和端口更新。
画面 8: 浏览器访问 Eureka 服务注册中心页面，显示 COLD-GATEWAY 和 COLD-USER 服务已注册。
画面 9: IDEA 控制台显示 GatewayApplication 启动日志，包括 Eureka 注册和初始化。
画面 10: 浏览器访问 Eureka 服务注册中心页面，显示 COLD-GATEWAY 和 COLD-USER 服务已注册，但出现 Eureka 可能错误地将实例标记为 UP 的警告。
画面 11: 在 Postman 中创建一个 POST 请求，用于测试用户登录接口。
画面 12: 在 Postman 中，请求体中填写用户名和密码，准备发送登录请求。
画面 13: 展示 PPT 页面，标题为“使用 API 网关后的优点”，并包含一个架构图，显示 Web 前端通过 API 网关访问后端服务。
画面 14: IDEA 控制台显示 GatewayApplication 启动日志，包括 DispatcherServlet 初始化和用户服务启动。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: cold-user-router
          uri: lb://cold-user
          predicates:
            - Path=/cold/user/**
```

画面 2:
```yaml
server:
  context-path: /cold
```

画面 3:
```yaml
spring:
  cloud:
    gateway:
      discovery:
        locator:
          enabled: true
```

画面 4:
```yaml
spring:
  cloud:
    gateway:
      discovery:
        locator:
          enabled: true
      routes:
        - id: cold-user-router
          uri: lb://cold-user
          predicates:
            - Path=/cold/user/**
```

画面 6:
```yaml
spring:
  cloud:
    gateway:
      discovery:
        locator:
          enabled: true
      routes:
        - id: cold-user-router
          uri: lb://cold-user
          predicates:
            - Path=/cold/user/**
```

画面 13:
架构图结构：
- Web 前端 → API 网关
- API 网关 → 服务
- API 网关 → 服务
- API 网关 → 服务

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 13:
标题：使用 API 网关后的优点：
- 易于监控。可以在网关收集监控数据并将其发送到外部系统进行分析。
- 易于认证。可以在网上进行认证，然后再将请求转发到后端的服务，而无需在每个微服务中进行认证。
- 减少了客户端与各个微服务之间的交互次数。

架构图结构：
- Web 前端 → API 网关
- API 网关 → 服务
- API 网关 → 服务
- API 网关 → 服务

表格数据：
画面 8 和 10:
| Application | AMIs | Availability Zones | Status |
|-------------|------|--------------------|--------|
| COLD-EUREKA-SERVER | n/a (1) | (1) | UP (1) - 192.168.145.128:cold-Eureka-server:8001 |
| COLD-GATEWAY | n/a (1) | (1) | UP (1) - 192.168.145.128:cold-gateway:8080 |
| COLD-USER | n/a (1) | (1) | UP (1) - 192.168.145.128:cold-user:8185 |

画面 10:
| Name | Value |
|------|-------|
| total-avail-memory | 33mb |
| environment | test |
| num-of-cpus | 4 |

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。

