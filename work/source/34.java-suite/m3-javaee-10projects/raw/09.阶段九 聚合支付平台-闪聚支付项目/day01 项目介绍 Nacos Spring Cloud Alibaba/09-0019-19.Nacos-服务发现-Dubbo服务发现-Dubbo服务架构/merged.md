# 19.Nacos-服务发现-Dubbo服务发现-Dubbo服务架构

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\19.Nacos-服务发现-Dubbo服务发现-Dubbo服务架构【海量资源尽在 666java.com】.mp4
- 时长 6分32秒（音频 392s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好接下来我们学习double服务发现刚才我们学习RESTful服务发现指的是我们微服务暴露RESTful服务接口然后呢把微服务的这个RESTful的接口呢注册到注册中心好那现在我们学习double服务发现指的是我们微服务呢暴露double协议的接口然后呢注册到注册中心然后呢进行服务发现整个过程好double呢在前面我们学习过它是阿里
[00:30] 88公司开源的一个RPC框架那么很多微服务啊也会用Double呢来暴露接口那么Double协议相比Restful的协议呢它的好处就是速度快因为它是基于RPC协议是吧它的速度更快但是Double也有自己的缺点就是它的生态啊就是Double用Double开发的微服务注意它呢是没有Spring Cloud给我们提供的
[01:00] 微服务开发的组件齐全的那针对这个呢其实阿里巴巴公司是不是就新出了一个Spring Cloud的阿里巴巴呀那这套微服务开发框架呢其实就是基于Spring Cloud的标准呢所提供的一套微服务开发的框架集合那其中呢这套Spring Cloud的阿里巴巴这套框架集合就整合了Double什么意思呢也就是我们完全可以用Double来开发我们的微服务并且呢它的
[01:30] 微服务的开发的技术生态呢也是非常齐全的所以我们其实散具支付项目呢就会采用double服务来做门作为微服务的一个接口注册到服务中心供其他服务调用因为什么因为double服务的它的这个接口的这个速度它会比RESTful更快因为大家知道RESTful呢是基于http的对吧
[01:56] 而Double是基于RPC的远程过程调用的这种协议格式所以它的速度更快好那下面呢我们来介绍一下我们整个项目所采用的这个Double服务架构的一个架构的一个图来看一下首先客户端呢会发起请求那这个请求大家知道那客户端就是我们的前端呢它会基于HTTP来发起请求就是RESTful那到哪里到我们的网关
[02:23] 在后边我会给大家专门搭建网关这个网关的作用呢其实就是根据客户端的请求呢把这个请求路由到具体的微服那么同时呢网关还可以去过滤用户的请求对用户的这个请求进行这个认证健全等等好那现在呢客户端请求到网关网关呢网关其实接收到RESTful的请求呢它会把这个请求转发到我们的一个什么
[02:50] 叫application就是应用层的一个服务那应用层我们前面在讲技术架构的时候说过应用层其实就是针对前端呢来提供交互处理服务的假如说我现在要添加商品添加商品的话那应用层呢它就会有一个接口就是添加商品但是具体添加商品要向数据库写数据具体添加商品的这个业务处理是由我们微服务层来实现
[03:18] 但是微服务层我们考虑到性能问题我们微服务统一对外暴露什么double协议的接口所以应用层和微服务之间交互是不是就是通过double协议进行而网关和应用层交互或者说简单理解就是客户端和应用层之间的交互是通过RESTful大家理解吗对这就是我们整套double服务架构的一个简单的一个理解
[03:48] 其实大家看到不管是网关也好还是应用层还是微服务他们都需要把自己注册到我们的服务发现中心那有时候老师为啥呢那你想客户端请求到网关因为我们知道网关对接的是不是很多实力所以网关呢也是要通过负载均衡的方法从服务发现中心拿到一堆服务列表通过负载均衡获取他要转发的一个具体的应用的地址对吧那这个应用他也一样
[04:18] 要请求微服务那他也需要从服务发现中心拿到微服务的实例地址然后通过负载均衡进行获取地址然后进行转发请求对其实我们说每一层都需要把自己注册到服务发现中心这是整个一个double服务架构就是我们项目所采用的服务架构的一个什么具体的解释它包括什么客户端网关应用
[04:46] 以及微服务刚才我们就说完了它的优势是什么呢其实刚才我说过其实它的优势呢整个的架构其实你会发现它对外暴露的接口呢它的这个协议呢它不仅支持RESTful它还支持double你会发现我们的应用层对客户端是不是以RESTful的这个接口形式呢对外提供服务而我们底层的这些微服务呢
[05:15] 它向应用层是以double协议它对外提供服务因为我们知道我们的微服务是不是总类数量比较多他们之间的交互是不是特别平凡所以他们之间的交互的性能是非常重要的所以我们采用double对吧而我们说对于前端来说前端一定是采用比较通用的这种http RESTful的协议所以我们的应用层就对外暴露RESTful所以这应该是它的一个优势就是什么呀
[05:43] 我们的架构同时提供RedFull和Double对前端提供RedFull微服务对外提供Double另外由于我们使用了NexusNexus的一个优点它不光可以作为服务发现中心它还可以干嘛对作为配置管理中心一会儿我会讲所以Nexus是集服务发现和配置为一身其实这也是它的一个优点因为在很多的系统架构当中
[06:12] 配置中心是配置中心服务发现中心是服务发现中心现在Nikos呢把这两个功能都一起实现所以这也是它的一个优势好那以上呢就是我们对double服务架构呢进行一个基础的一个讲解后边呢我们会测试整个架构

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Spring Cloud Alibaba 中 Dubbo 服务发现与微服务架构的原理及实现。

2) 按时间顺序列出每张画面的要点：
画面 1:
- IDE 界面显示项目结构，包含 `Nacos-RESTful-provider` 和 `Nacos-RESTful-consumer` 模块。
- `RestConsumerController.java` 中定义了 `@RequestMapping(value = "/Service")` 和 `RestTemplate restTemplate`。
- `application.yml` 配置文件中包含 `spring.application.name: Nacos-RESTful-provider`。
- `RibbonLoadBalancerClient.class` 代码片段显示 `choose` 方法和 `execute` 方法。

画面 2:
- IDE 界面显示 `RestConsumerController.java` 中的 `@RequestMapping(value = "/Service")` 和 `RestTemplate restTemplate`。
- 代码中调用 `loadBalancerClient.choose(serviceId)` 获取服务实例。
- `application.yml` 配置文件中包含 `spring.application.name: Nacos-RESTful-provider`。

画面 3:
- PPT 页面标题为“2.4 Dubbo服务发现”。
- 文本内容：“Dubbo是阿里巴巴公司开源的RPC框架，在国内有着非常大的用户群体，但其微服务开发组件相对Spring Cloud来说并不那么完善。”
- 文本内容：“Spring Cloud Alibaba微服务开发框架集成了Dubbo，可实现微服务对外暴露Dubbo协议的接口，Dubbo协议相比RESTful协议速度更快。”
- 文本内容：“RPC：RPC是远程过程调用（Remote Procedure Call）的缩写与形式，调用RPC远程方法就像调用本地方法一样，非常方便，后边案例讲解具体过程。”

画面 4:
- PPT 页面标题为“2.4.1 Dubbo服务架构”。
- 图表显示“客户端”通过 HTTP 请求“API网关(Zuul)”，“API网关(Zuul)”通过 RESTful 调用“Application-1”，“Application-1”通过 dubbo 调用“Service-1”和“Service-2”，“Service-1”和“Service-2”通过 dubbo 相互调用，“Application-1”通过“服务注册&发现”指向“Nacos Server（服务发现中心）”。

画面 5:
- PPT 页面标题为“2.4.1 Dubbo服务架构”。
- 图表显示“客户端”通过 HTTP 请求“API网关(Zuul)”，“API网关(Zuul)”通过 RESTful 调用“Application-1”，“Application-1”通过 dubbo 调用“Service-1”和“Service-2”，“Service-1”和“Service-2”通过 dubbo 相互调用，“Application-1”通过“服务注册&发现”指向“Nacos Server（服务发现中心）”。

画面 6:
- PPT 页面标题为“2.4.1 Dubbo服务架构”。
- 图表显示“客户端”通过 HTTP 请求“API网关(Zuul)”，“API网关(Zuul)”通过 RESTful 调用“Application-1”，“Application-1”通过 dubbo 调用“Service-1”和“Service-2”，“Service-1”和“Service-2”通过 dubbo 相互调用，“Application-1”通过“服务注册&发现”指向“Nacos Server（服务发现中心）”。
- 文本内容：“组件说明：1、客户端：前端或外部系统 2、API网关：系统唯一入口，路由转发 3、application-1：应用1，前端提供Http接口，接收用户的交互请求 4、Service-1：微服务1，提供业务逻辑处理服务 5、Service-2：微服务2，提供业务逻辑处理服务 交互流程：1、网关负责客户端请求的统一入口，路由转发，前端通过网关请求后端服务。2、网关收到前端请求，转发请求给应用。3、应用接收前端请求，调用微服务进行业务逻辑处理 4、微服务为应用提供业务逻辑处理的支撑，为应用提供Dubbo协议接口”

画面 7:
- PPT 页面标题为“2.4.1 Dubbo服务架构”。
- 图表显示“客户端”通过 HTTP 请求“API网关(Zuul)”，“API网关(Zuul)”通过 RESTful 调用“Application-1”，“Application-1”通过 dubbo 调用“Service-1”和“Service-2”，“Service-1”和“Service-2”通过 dubbo 相互调用，“Application-1”通过“服务注册&发现”指向“Nacos Server（服务发现中心）”。
- 文本内容：“组件说明：1、客户端：前端或外部系统 2、API网关：系统唯一入口，路由转发 3、application-1：应用1，前端提供Http接口，接收用户的交互请求 4、Service-1：微服务1，提供业务逻辑处理服务 5、Service-2：微服务2，提供业务逻辑处理服务 交互流程：1、网关负责客户端请求的统一入口，路由转发，前端通过网关请求后端服务。2、网关收到前端请求，转发请求给应用。3、应用接收前端请求，调用微服务进行业务逻辑处理 4、微服务为应用提供业务逻辑处理的支撑，为应用提供Dubbo协议接口”

画面 8:
- PPT 页面标题为“2.4.1 Dubbo服务架构”。
- 文本内容：“交互流程：1、网关负责客户端请求的统一入口，路由转发，前端通过网关请求后端服务。2、网关收到前端请求，转发请求给应用。3、应用接收前端请求，调用微服务进行业务逻辑处理 4、微服务为应用提供业务逻辑处理的支撑，为应用提供Dubbo协议接口”
- 文本内容：“优势分析：此架构同时提供RESTful和Dubbo接口服务，应用层对前端提供RESTful接口，RESTful是互联网通用的轻量级交互协议，方便前端接入系统；微服务层向应用层提供Dubbo接口，Dubbo接口基于RPC通信协议速度更快。本架构采用阿里开源的Nacos，集服务发现和配置中心于一身，支持RESTful及Dubbo服务的注册。”
- 文本内容：“2.4.2 测试环境”

画面 9:
- PPT 页面标题为“2.4.2 测试环境”。
- 文本内容：“父工程：仍然使用Nacos.discovery。”
- 文本内容：“application1：使用Nacos-RESTful-consumer。”

画面 10:
- PPT 页面标题为“2.4.2 测试环境”。
- 文本内容：“父工程：仍然使用Nacos.discovery。”
- 文本内容：“application1：使用Nacos-RESTful-consumer。”

画面 11:
- PPT 页面标题为“2.4.1 Dubbo服务架构”。
- 文本内容：“组件说明：1、客户端：前端或外部系统 2、API网关：系统唯一入口，路由转发 3、application-1：应用1，前端提供Http接口，接收用户的交互请求 4、Service-1：微服务1，提供业务逻辑处理服务 5、Service-2：微服务2，提供业务逻辑处理服务 交互流程：1、网关负责客户端请求的统一入口，路由转发，前端通过网关请求后端服务。2、网关收到前端请求，转发请求给应用。3、应用接收前端请求，调用微服务进行业务逻辑处理 4、微服务为应用提供业务逻辑处理的支撑，为应用提供Dubbo协议接口”

画面 12:
- PPT 页面标题为“2.4 Dubbo服务发现”。
- 文本内容：“Dubbo是阿里巴巴公司开源的RPC框架，在国内有着非常大的用户群体，但其微服务开发组件相对Spring Cloud来说并不那么完善。”
- 文本内容：“Spring Cloud Alibaba微服务开发框架集成了Dubbo，可实现微服务对外暴露Dubbo协议的接口，Dubbo协议相比RESTful协议速度更快。”
- 文本内容：“RPC：RPC是远程过程调用（Remote Procedure Call）的缩写与形式，调用RPC远程方法就像调用本地方法一样，非常方便，后边案例讲解具体过程。”

画面 13:
- PPT 页面标题为“2.4 Dubbo服务发现”。
- 文本内容：“Dubbo是阿里巴巴公司开源的RPC框架，在国内有着非常大的用户群体，但其微服务开发组件相对Spring Cloud来说并不那么完善。”
- 文本内容：“Spring Cloud Alibaba微服务开发框架集成了Dubbo，可实现微服务对外暴露Dubbo协议的接口，Dubbo协议相比RESTful协议速度更快。”
- 文本内容：“RPC：RPC是远程过程调用（Remote Procedure Call）的缩写与形式，调用RPC远程方法就像调用本地方法一样，非常方便，后边案例讲解具体过程。”

画面 14:
- PPT 页面标题为“2.4.1 Dubbo服务架构”。
- 图表显示“客户端”通过 HTTP 请求“API网关(Zuul)”，“API网关(Zuul)”通过 RESTful 调用“Application-1”，“Application-1”通过 dubbo 调用“

