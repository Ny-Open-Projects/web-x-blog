# 07.项目技术架构-技术架构和技术栈

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\07.项目技术架构-技术架构和技术栈【海量资源尽在 666java.com】.mp4
- 时长 8分7秒（音频 487s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,下面呢我们来学习一下闪去支付项目的技术架构那在有了微服务架构的理解基础之上呢我们来看一下本项目的技术架构那闪去支付呢是采用当前流行的前后端分离架构进行开发那前后端分离指的是前端和服务端完全分离其实前端指的就是这里面的UI层
[00:27] 然后呢服务端指的就是我们这个图上面的微服务层那么整个的这个架构呢其实它是基于微服务架构的思想来进行构建的只不过把前端和服务端进行完全分开那么从上往下我们来看它有很多的这个层组层啊来我们首先看一下最上边是用户层用户层就相当于我们的用户
[00:55] 我们系统所支持的用户客户端类型比如有PC有手机APP还有H5网页等等这种这些客户端类型的我们系统都支持还有CDNCDN呢后边我会详细的去讲你现在可以理解为它是一种什么缓存层CDN叫内容
[01:16] 分发它是一种缓存层就是加快我们系统的访问速度其实你可以看到这里面有什么网页有图片有视频等等这些都可以放在CDN这一块来加速用户的访问后边我会详细讲这里面我就不再详细的去说CDN的技术后边还有负载均衡负载均衡这个词大家应该理解对吧因为我们后边可能会我们这个负载均衡的
[01:45] 后端会部署很多的这个什么集群对吧通过负载均衡呢可以把我们用户的请求负载到各个节点来提高我们访问的性能UI层其实就是我们说的前端了这里边大家可以看到有很多前端有商户平台的前端运营平台前端还有官网的前端管理平台的前端这些都属于前端前端指的就是主要负责用户的操作界面对吧
[02:15] 那前端要发起一个请求的话首先要进入什么网关要通过网关通过网关呢进入到我们的应用层大家可以看到这里边是不是有各种应用啊这个应用呢是面向前端提供服务的比如我现在要添加一个什么商户注册一个商户那是会请求到应用请求到商户平台的应用那么请到这里干嘛呢应用嘛
[02:43] 就是为前端提供服务的但是真正供应用来调用的微服务就是微服务层里面的东西就微服务层相当于是给应用层做支撑那么注册一个商户前端发起请求到网关然后到商户平台的应用
[03:04] 那么商务平台应用的要向数据库是不是要写商户信息啊那这里边呢他就会请求微服务层的商户服务来完成商户注册的业务大家理解整个流程了吧好
[03:18] 但其实在微服务层这里边大家可以看到它是比如有基础的微服务有业务的微服务包括我们我刚才说的商户服务是不是就针对业务的微服务但是也有一些基础的比如说日志监控文件等等这些都属于各个业务微服务都要用到的公共的这些基础微服务另外再往下看它就是数据层每一个微服务都有自己对应的数据库数据层就是存放数据的地方
[03:48] 大家可以看到不光有mycycle还有什么消息对链缓存索引文件等等这些都属于数据层当中的东西那么在整个架构图的右边大家可以看到右边指的就是第三方系统的商户应用你比如说现在商户自己有自己的一个平台他要使用我们的支付功能他是不是需要接入我们聚合支付平台这里边这是商户应用
[04:18] 它接入聚合支付平台的一个什么大概流程回头我会详细的去讲这个接入的过程然后后面再来看第三方支付就是支付宝微信因为我们作为聚合支付平台它是不是要把第三方支付类似于支付宝微信的这些支付渠道都聚合在我们平台当中供用户去支付所以这里边以我们平台也要和第三方支付做接口这就是整个的技术
[04:45] 加工图那下边有详细的分层描述大家呢可以看看讲义那么整个加工图呢我说完了之后呢大家可以看一下我们整个技术架构哎里边所采用的各个技术站从最上边的前端啊前端我们啊主要用H5啊V5哎当然还有APP那这个首先我们这个项目呢前端采用的是啊ViuJS
[05:11] 当然也有一部分的其他的这个技术回头我在说到的时候呢讲到这一块的时候会给大家详细的去说还有接入这个接入这一块呢我们知道因为通过网关啊然后呢请求是不是要先过网关然后到我们的应用然后才到微服务啊所以这个接入这一块呢就会用到一些什么认证的技术比如说有Spring Cloud的这个
[05:39] Security是吧还有这个入网关还有GWT令牌等等这些都属于接入层的技术还有组件这一块呢其实就是我们微服务层里边所用到的一些组件这里边我们所有的微服务都是基于Spring Boot进行开发然后呢我们微服务层这一块所采用的技术呢都是基于Double服务基于Double协议来构造的服务还有日志的呀还有一些工具类呀
[06:08] 还有这个模板引擎啊任务调度啊接口的描述定义分库分表还有这个这个大家应该属于MapBetis Plus是吧针对MapBetis的一个什么升级版本还有基础设施层这里边我们说你的数据层是不是要用MySQL啊还有消息队列缓存另外包括文件存储所以这些都是基础设施层
[06:32] 然后这个Diamond Ops是啥意思呢大家看到右侧Diamond Ops呢指的是我们开发运维相关的一些什么工具啊Maven大家应该不陌生吧进行项目构建的一个非常好用的工具还有Jackens就是系统持续集成的工具还有这个这个我原来好像说过大家应该有印象是吧叫配置中心Nexus还有Git版本控制
[07:00] 这个Docker容器化技术还有等等这些都是我们DevOps里面相关的工具那么我们的重点要放在哪里我们整个开发的过程中重点其实我们的重点应该是在下边这两块看到了吗那么上面这个前端这一块不是大家的开发重点因为大家作为Java工程师到企业当中是不用去开发前端的因为前后端已经分离了对不对
[07:29] 那么对于接入这一块应该是架构师他所关心的技术而对于我们加把开发控制师你需要关注的是整个微服务开发所涉及到的一些技术好那么以上就是我们整个系统的技术架构是基于前后端分离架构分成了由用户层CDN负载均衡UI接入微服务数据层等各层所组成的这么一个微服务架构的一个系统架构
[07:58] 图包括技术jar 包括我们的重点大家要清楚OK那么技术架构和技术战呢我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲闪聚支付项目的技术架构与技术栈，包括前后端分离架构、各层级组件及所使用的技术框架。

2) 按时间顺序列出每张画面的要点：
画面1：展示技术架构图的顶层，包含用户层（PC、APP、H5）、CDN层、负载均衡层、微服务层、数据层，以及各层内部模块。
画面2：展示技术架构图的详细结构，包括用户层、CDN层、负载均衡层、微服务层、数据层，以及各层内部模块和交互关系。
画面3：展示技术架构图的顶层，包含用户层（PC、APP、H5）、CDN层、负载均衡层、微服务层、数据层，以及各层内部模块。
画面4：展示技术架构图的详细结构，包括用户层、CDN层、负载均衡层、微服务层、数据层，以及各层内部模块和交互关系。
画面5：展示技术架构图的详细结构，包括用户层、CDN层、负载均衡层、微服务层、数据层，以及各层内部模块和交互关系。
画面6：展示技术架构图的详细结构，包括用户层、CDN层、负载均衡层、微服务层、数据层，以及各层内部模块和交互关系。
画面7：展示技术架构图的详细结构，包括用户层、CDN层、负载均衡层、微服务层、数据层，以及各层内部模块和交互关系。
画面8：展示技术架构图的详细结构，包括用户层、CDN层、负载均衡层、微服务层、数据层，以及各层内部模块和交互关系。
画面9：列出技术架构的各层说明：用户层、CDN层、负载均衡层、UI层、微服务层、数据层。
画面10：展示技术栈图，包括视图层（H5、Vue）、接入层（Spring Cloud Zuul、Spring Cloud Security、Spring Cloud OAuth2、Sentinel、JWT）、组件层（Spring boot、Druid、Dubbo Spring Cloud、Log4j2、Guava、Mybatis plus、sharding-jdbc、Swagger、XXL-job、Freemarker）、基础设施层（Mysql、RocketMQ、Redis、七牛云、腾讯云）、DevOps层（Maven、Jenkins、Nacos Config、Git/Gogs、Docker、ELK、Nacos Discovery、Zipkin）。
画面11：展示技术栈图，包括视图层（H5、Vue）、接入层（Spring Cloud Zuul、Spring Cloud Security、Spring Cloud OAuth2、Sentinel、JWT）、组件层（Spring boot、Druid、Dubbo Spring Cloud、Log4j2、Guava、Mybatis plus、sharding-jdbc、Swagger、XXL-job、Freemarker）、基础设施层（Mysql、RocketMQ、Redis、七牛云、腾讯云）、DevOps层（Maven、Jenkins、Nacos Config、Git/Gogs、Docker、ELK、Nacos Discovery、Zipkin）。
画面12：展示项目介绍，包括项目背景、产业结构图。
画面13：展示技术架构图的详细结构，包括用户层、CDN层、负载均衡层、微服务层、数据层，以及各层内部模块和交互关系。
画面14：展示技术栈图，包括视图层（H5、Vue）、接入层（Spring Cloud Zuul、Spring Cloud Security、Spring Cloud OAuth2、Sentinel、JWT）、组件层（Spring boot、Druid、Dubbo Spring Cloud、Log4j2、Guava、Mybatis plus、sharding-jdbc、Swagger、XXL-job、Freemarker）、基础设施层（Mysql、RocketMQ、Redis、七牛云、腾讯云）、DevOps层（Maven、Jenkins、Nacos Config、Git/Gogs、Docker、ELK、Nacos Discovery、Zipkin）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：标题“2.2 技术架构”，架构图结构：用户层（PC、APP、H5）→ CDN层 → 负载均衡层 → 微服务层 → 数据层 → 客户端应用。
画面2：标题“2.2 技术架构”，架构图结构：用户层（PC、APP、H5）→ CDN层 → 负载均衡层 → 微服务层 → 数据层 → 客户端应用。
画面3：标题“2.2 技术架构”，架构图结构：用户层（PC、APP、H5）→ CDN层 → 负载均衡层 → 微服务层 → 数据层 → 客户端应用。
画面4：标题“2.2 技术架构”，架构图结构：用户层（PC、APP、H5）→ CDN层 → 负载均衡层 → 微服务层 → 数据层 → 客户端应用。
画面5：标题“2.2 技术架构”，架构图结构：用户层（PC、APP、H5）→ CDN层 → 负载均衡层 → 微服务层 → 数据层 → 客户端应用。
画面6：标题“2.2 技术架构”，架构图结构：用户层（PC、APP、H5）→ CDN层 → 负载均衡层 → 微服务层 → 数据层 → 客户端应用。
画面7：标题“2.2 技术架构”，架构图结构：用户层（PC、APP、H5）→ CDN层 → 负载均衡层 → 微服务层 → 数据层 → 客户端应用。
画面8：标题“2.2 技术架构”，架构图结构：用户层（PC、APP、H5）→ CDN层 → 负载均衡层 → 微服务层 → 数据层 → 客户端应用。
画面9：表格数据：用户层、CDN层、负载均衡层、UI层、微服务层、数据层。
画面10：标题“2.3 技术栈”，架构图结构：视图层（H5、Vue）→ 接入层（Spring Cloud Zuul、Spring Cloud Security、Spring Cloud OAuth2、Sentinel、JWT）→ 组件层（Spring boot、Druid、Dubbo Spring Cloud、Log4j2、Guava、Mybatis plus、sharding-jdbc、Swagger、XXL-job、Freemarker）→ 基础设施层（Mysql、RocketMQ、Redis、七牛云、腾讯云）→ DevOps层（Maven、Jenkins、Nacos Config、Git/Gogs、Docker、ELK、Nacos Discovery、Zipkin）。
画面11：标题“2.3 技术栈”，架构图结构：视图层（H5、Vue）→ 接入层（Spring Cloud Zuul、Spring Cloud Security、Spring Cloud OAuth2、Sentinel、JWT）→ 组件层（Spring boot、Druid、Dubbo Spring Cloud、Log4j2、Guava、Mybatis plus、sharding-jdbc、Swagger、XXL-job、Freemarker）→ 基础设施层（Mysql、RocketMQ、Redis、七牛云、腾讯云）→ DevOps层（Maven、Jenkins、Nacos Config、Git/Gogs、Docker、ELK、Nacos Discovery、Zipkin）。
画面12：标题“1.1 项目背景”，产业结构图：口令、e洗亿、美团、大众点评、资源、58同城、中国银联、中国人民银行清算中心、百度支付。
画面13：标题“2.2 技术架构”，架构图结构：用户层（PC、APP、H5）→ CDN层 → 负载均衡层 → 微服务层 → 数据层 → 客户端应用。
画面14：标题“2.3 技术栈”，架构图结构：视图层（H5、Vue）→ 接入层（Spring Cloud Zuul、Spring Cloud Security、Spring Cloud OAuth2、Sentinel、JWT）→ 组件层（Spring boot、Druid、Dubbo Spring Cloud、Log4j2、Guava、Mybatis plus、sharding-jdbc、Swagger、XXL-job、Freemarker）→ 基础设施层（Mysql、RocketMQ、Redis、七牛云、腾讯云）→ DevOps层（Maven、Jenkins、Nacos Config、Git/Gogs、Docker、ELK、Nacos Discovery、Zipkin）。

5) 无。

