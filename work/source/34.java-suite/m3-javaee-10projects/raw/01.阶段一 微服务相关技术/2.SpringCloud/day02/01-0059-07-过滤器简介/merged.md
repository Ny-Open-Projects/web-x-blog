# 07-过滤器简介

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\07-过滤器简介_【海量资源尽在 ubkz.com】.mp4
- 时长 9分9秒（音频 548s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 过滤器简介在这一小节中我们的主要目标是了解Gateway默认过滤器的用法和过滤器类型前面章节与大家说过网关的主要作用是路由和过滤在配置使用路由之后现在来了解学习SpinCloud Gateway网关的过滤功能那现在我们打开讲义来了解过滤器Gateway作为网关的其中一个重要功能就是实现请求的健全而这个动作往往通过网关提供的过滤器来实现的
[00:30] 那前面其实我们已经用了两个过滤器分别是添加前缀跟去除前缀的过滤器在这边也列了几个分别是第一个添加请求头添加请求参数添加响应头跟去除前缀的过滤器那具体呢Gateway自带过滤器有几十个我们来看下面这幅图这些过滤器都要去实现一个接口叫做Gateway Filter Factory
[01:02] 而且发现这些过滤器名称都包含有Gateway Filter Factory我们具体来打开它的一个官网链接来了解这些过滤器的作用和配置这是具体的过滤器名称这是它的一个作用还有它的配置那具体我们以这个来说明这叫添加请求头的一个过滤器它的作用是对我们的所有请求添加一个
[01:34] 名称和值请求头部的一个名称和值那具体的用法呢就是把后面的GatewayFieldFactory名给去掉以后前面部分作为配置文件中配置的过滤器名称然后第一个是它的属性名第二个是对应的属性值如果有多个那么你复制这一行就可以了好这就是它的一个作用还有配置
[02:02] 那具体呢我们在项目中也去添加一个来验证这个过滤器好我们加一个是添加响应头的一个过滤器来它的用法是一样的把这个过滤器名称去掉GatewayFunderFactory之后加上来第一个呢是添加的头部的属性名第二个是它对应的值那我们打开我们的IDA去添加在我们的网关服务项目中去添加我们加一个默认的过滤器
[02:35] 在这边来个default filters就加完了那我们来注释一下这个意思这是默认过滤器会对所有路由都生效因为它不是加到某个具体的路由下像我们前面加的关于路径的添加和去除的过滤器是加到某一个路由下就是这个路由下的
[03:09] 那对这个路由生效那现在是默认的过滤器会对所有的路由都生效我们就加完加完后呢去启动这个网关服务启动好以后呢我们去测试那现在因为我们的项目中是还在用一个去除前缀路径的一个过滤器所以我们一回访问的路径呢还要包含API user这么一个路径之后再去查看响应的头部中是否有这么一个
[03:38] 属性名和值当然这个是随便改的我们可以改一个不要用它默认的也行你用默认的也可以我们已经启动好了那就以默认的就是这种刚才复制过来的去查看打开浏览器访问一个地址这地址呢刚才跟大家说过要去加一个API我们回车我们再打开F12来查看响应Network刷新响应
[04:10] 这个请求地址中的响应头就它里面有我们刚才配置的也就是说过滤器是生效的那如果是要多个的话呢那就可以这样写比如说我们写一个叫做my name比如abc-my name那它值我们来写个黑码接着我们再来重启这时候就在响应的头中有两个属性都会出现
[04:42] 一个是它一个是这一个我们再来刷新刷新好了接着再去看它的响应头一个两个好以此类推如果有三个那就再复制一行就可以了这就是我们一个关于过滤器的配置回到讲义中来了解过滤器类型在配置上它有全局和局部两种分别第一个局部过滤器它是通过
[05:19] 在某一个路由下去配置FilmTest来实现对这一个路由进行过滤那如果像我们刚才配置的一样如果用了一个DefaultFilmTest的话呢会对所有路由都不生效这也算是一个全局的过滤器了只是这个实现的方式呢都要去实现一个接口叫做GatewayFilmTestFactory接口所以在实现上它还算是局部的过滤器那我们所说的全局过滤器呢是不需要在配置文件中去配置
[05:48] 直接就对所有的路由生效的那它实现的接口叫做Global Filter后面我们也会去应用它包括我们自定义局部过滤器也会去使用包括去测试验证这些过滤器那再来了解一个过滤器的执行生命周期周期的话呢有两个分别是在执行服务的之前跟之后都可以做一些事情就像是PMVC的拦截器
[06:18] 那蓝Supreme MVC 蓝解析有三个就是有一个前置后置还有完成时那我们的一个网关的过滤器里边有两个一个就是前置就是在执行服务之前可以做一些处理在执行服务之后可以经过一系列的过滤器执行一系列的方法也就是说当如果有需要在执行服务之前或之后要做一些事情的话可以在这个过滤器的方法中
[06:49] 调用服务之前处理一些事情之后也处理一些事情它不是具体有这两个Prick跟Pulse这两个方法而是说类似的在执行服务前后可以处理其他一些内容比如说我们一般的应用场景可以做一个鉴定权限就是当如果发现没有权限的时候呢直接返回空也就是在执行服务之前去进行权限的鉴定也可以做一个异常处理
[07:17] 当执行服务之后呢如果发生了异常的话我们可以在过滤器中去记录这些异常信息再是可以做一个服务时长的统计在执行前记一个时间戳执行后记录一个时间戳再去计算之间的一个花的时间长度有多长好这就是我们一般的使用场景那现在我们回到笔记中来小结刚才说到的这个过滤器那么刚才说到呢
[07:49] 这个过滤器的用法并且去配置了它那配置的做法呢就是这个就是用法在配置文件中指定要使用的过滤器名称过滤器名称指定后就可以了那这个要注意就是我们过滤器名称后面的GatewayFilterFactory是不需要指定的
[08:17] 而且呢这个在配置文件中配置的有两种一种是对某个路由一种是默认的过滤器会对所有路由都生效好要注意接着我们再去讲了一下它的类型它类型呢有两种在实现方式上的两种呢分别是局部还有是一个全局那后面我们会去自己编写这些类型的过滤器再是它的一个使用场景可以用在
[08:48] 比如说请求健全异常处理还有就是记录调用时长等这些场景都可以使用我们的网关中的过滤器的功能这就是我们过滤器简介的部分内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Spring Cloud Gateway 中的过滤器（Filter）机制，包括内置过滤器工厂、配置方式、执行生命周期及如何添加或去除请求头和路径前缀。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程文档中“2.7. 过滤器”章节的“2.7.1. 简介”，列出 Gateway 自带的过滤器名称及说明，如 AddRequestHeader、AddRequestParameters、AddResponseHeader、StripPrefix 等。
画面 2: 展示 IDE 中 Spring Cloud Gateway 的过滤器工厂类结构，列出如 AbstractGatewayFilterFactory、SecureHeadersGatewayFilterFactory、StripPrefixGatewayFilterFactory 等。
画面 3: 展示 Spring Cloud Gateway 官方文档“5.1 AddRequestHeader GatewayFilter Factory”部分，展示如何在 application.yml 中配置添加请求头。
画面 4: 展示 Spring Cloud Gateway 官方文档“5.2 AddRequestParameter GatewayFilter Factory”部分，展示如何在 application.yml 中配置添加请求参数。
画面 5: 展示 IDE 中 heima-gateway 项目的 application.yml 文件，配置了路由规则，其中 filters 部分包含 StripPrefix 和 AddResponseHeader 过滤器。
画面 6: 展示 Spring Cloud Gateway 官方文档“5.3 AddResponseHeader GatewayFilter Factory”部分，展示如何在 application.yml 中配置添加响应头。
画面 7: 展示浏览器开发者工具 Network 面板，请求 http://127.0.0.1:10010/api/user/8，响应头中包含 X-Response-Header: Bar。
画面 8: 展示 IDE 中 heima-gateway 项目的 application.yml 文件，配置了默认过滤器 default-filters，包含 AddResponseHeader 和 StripPrefix。
画面 9: 展示浏览器开发者工具 Network 面板，请求 http://127.0.0.1:10010/api/user/8，响应头中包含 X-Response-Header: Bar。
画面 10: 展示课程文档中“配置全局默认过滤器”部分，展示 application.yml 中的配置，包括 server、spring.application.name、gateway.default-filters 等。
画面 11: 展示课程文档中“2.7.2. 执行生命周期”部分，展示一个流程图，请求从上方进入，经过多个过滤器，最后到达微服务。
画面 12: 展示课程文档中“2.7.2. 执行生命周期”部分的流程图，图中显示请求和响应分别经过多个过滤器，然后流向微服务。
画面 13: 展示课程文档“7. 过滤器简介”和“8. 自定义局部过滤器”章节标题，说明过滤器的用法和类型（局部、全局）。
画面 14: 展示课程文档“7. 过滤器简介”和“8. 自定义局部过滤器”章节标题，与画面 13 相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: add_request_header_route
          uri: http://example.org
          filters:
            - AddRequestHeader=X-Request-Foo, Bar
```

画面 4:
```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: add_request_parameter_route
          uri: http://example.org
          filters:
            - AddRequestParameter=foo, bar
```

画面 5:
```yaml
spring:
  application:
    name: api-gateway
  cloud:
    gateway:
      routes:
        - id: user-Service-route
          uri: http://127.0.0.1:8091
          predicates:
            - Path=/api/user/**
          filters:
            - StripPrefix=1
            - AddResponseHeader=X-Response-Zoo, Bar
      default-filters:
        - AddResponseHeader=X-Response-Zoo, Bar
        - StripPrefix=1
    Eureka:
      client:
        Service-url:
          defaultZone: http://127.0.0.1:10086/Eureka
        prefer-ip-address: true
```

画面 6:
```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: add_request_header_route
          uri: http://example.org
          filters:
            - AddResponseHeader=X-Response-Foo, Bar
```

画面 8:
```yaml
spring:
  application:
    name: api-gateway
  cloud:
    gateway:
      default-filters:
        - AddResponseHeader=X-Response-Zoo, Bar
        - StripPrefix=1
    Eureka:
      client:
        Service-url:
          defaultZone: http://127.0.0.1:10086/Eureka
        prefer-ip-address: true
```

画面 10:
```yaml
server:
  port: 10010
spring:
  application:
    name: api-gateway
  cloud:
    gateway:
      default-filters:
        - AddResponseHeader=X-Response-Default-MyName, itcast
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 11: 标题为“2.7.2. 执行生命周期”，下方流程图显示“请求”从上方进入，经过“过滤器”、“过滤器”、“过滤器...”，最后指向“微服务”，响应从“微服务”返回，经过“过滤器”、“过滤器”、“过滤器...”，最后返回“请求”。
画面 12: 标题为“2.7.2. 执行生命周期”，下方流程图显示“请求”从上方进入，经过“过滤器”、“过滤器”、“过滤器...”，最后指向“微服务”，响应从“微服务”返回，经过“过滤器”、“过滤器”、“过滤器...”，最后返回“请求”。
画面 13: 标题为“7. 过滤器简介”和“8. 自定义局部过滤器”，其中“7. 过滤器简介”下有“目标”、“分析”、“小结”等子标题，“8. 自定义局部过滤器”下有“目标”、“分析”、“小结”等子标题。
画面 14: 标题为“7. 过滤器简介”和“8. 自定义局部过滤器”，与画面 13 相同。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已满足）

