# 画面线理解：19.Nacos-服务发现-Dubbo服务发现-Dubbo服务架构

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\19.Nacos-服务发现-Dubbo服务发现-Dubbo服务架构【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:16, 02:03, 02:07, 04:39, 04:43, 04:53, 04:55, 05:51, 06:10, 06:18, 06:22, 06:24, 06:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:26:34

1) 这一组画面整体在讲 Spring Cloud Alibaba 中 Dubbo 服务发现与微服务架构的原理及实现。

2) 按时间顺序列出每张画面的要点：
画面 1:
- IDE 界面显示项目结构，包含 `nacos-restful-provider` 和 `nacos-restful-consumer` 模块。
- `RestConsumerController.java` 中定义了 `@RequestMapping(value = "/service")` 和 `RestTemplate restTemplate`。
- `application.yml` 配置文件中包含 `spring.application.name: nacos-restful-provider`。
- `RibbonLoadBalancerClient.class` 代码片段显示 `choose` 方法和 `execute` 方法。

画面 2:
- IDE 界面显示 `RestConsumerController.java` 中的 `@RequestMapping(value = "/service")` 和 `RestTemplate restTemplate`。
- 代码中调用 `loadBalancerClient.choose(serviceId)` 获取服务实例。
- `application.yml` 配置文件中包含 `spring.application.name: nacos-restful-provider`。

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
- 文本内容：“组件说明：1、客户端：前端或外部系统 2、API网关：系统唯一入口，路由转发 3、application-1：应用1，前端提供Http接口，接收用户的交互请求 4、service-1：微服务1，提供业务逻辑处理服务 5、service-2：微服务2，提供业务逻辑处理服务 交互流程：1、网关负责客户端请求的统一入口，路由转发，前端通过网关请求后端服务。2、网关收到前端请求，转发请求给应用。3、应用接收前端请求，调用微服务进行业务逻辑处理 4、微服务为应用提供业务逻辑处理的支撑，为应用提供Dubbo协议接口”

画面 7:
- PPT 页面标题为“2.4.1 Dubbo服务架构”。
- 图表显示“客户端”通过 HTTP 请求“API网关(Zuul)”，“API网关(Zuul)”通过 RESTful 调用“Application-1”，“Application-1”通过 dubbo 调用“Service-1”和“Service-2”，“Service-1”和“Service-2”通过 dubbo 相互调用，“Application-1”通过“服务注册&发现”指向“Nacos Server（服务发现中心）”。
- 文本内容：“组件说明：1、客户端：前端或外部系统 2、API网关：系统唯一入口，路由转发 3、application-1：应用1，前端提供Http接口，接收用户的交互请求 4、service-1：微服务1，提供业务逻辑处理服务 5、service-2：微服务2，提供业务逻辑处理服务 交互流程：1、网关负责客户端请求的统一入口，路由转发，前端通过网关请求后端服务。2、网关收到前端请求，转发请求给应用。3、应用接收前端请求，调用微服务进行业务逻辑处理 4、微服务为应用提供业务逻辑处理的支撑，为应用提供Dubbo协议接口”

画面 8:
- PPT 页面标题为“2.4.1 Dubbo服务架构”。
- 文本内容：“交互流程：1、网关负责客户端请求的统一入口，路由转发，前端通过网关请求后端服务。2、网关收到前端请求，转发请求给应用。3、应用接收前端请求，调用微服务进行业务逻辑处理 4、微服务为应用提供业务逻辑处理的支撑，为应用提供Dubbo协议接口”
- 文本内容：“优势分析：此架构同时提供RESTful和Dubbo接口服务，应用层对前端提供RESTful接口，RESTful是互联网通用的轻量级交互协议，方便前端接入系统；微服务层向应用层提供Dubbo接口，Dubbo接口基于RPC通信协议速度更快。本架构采用阿里开源的Nacos，集服务发现和配置中心于一身，支持RESTful及Dubbo服务的注册。”
- 文本内容：“2.4.2 测试环境”

画面 9:
- PPT 页面标题为“2.4.2 测试环境”。
- 文本内容：“父工程：仍然使用nacos.discovery。”
- 文本内容：“application1：使用nacos-restful-consumer。”

画面 10:
- PPT 页面标题为“2.4.2 测试环境”。
- 文本内容：“父工程：仍然使用nacos.discovery。”
- 文本内容：“application1：使用nacos-restful-consumer。”

画面 11:
- PPT 页面标题为“2.4.1 Dubbo服务架构”。
- 文本内容：“组件说明：1、客户端：前端或外部系统 2、API网关：系统唯一入口，路由转发 3、application-1：应用1，前端提供Http接口，接收用户的交互请求 4、service-1：微服务1，提供业务逻辑处理服务 5、service-2：微服务2，提供业务逻辑处理服务 交互流程：1、网关负责客户端请求的统一入口，路由转发，前端通过网关请求后端服务。2、网关收到前端请求，转发请求给应用。3、应用接收前端请求，调用微服务进行业务逻辑处理 4、微服务为应用提供业务逻辑处理的支撑，为应用提供Dubbo协议接口”

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
