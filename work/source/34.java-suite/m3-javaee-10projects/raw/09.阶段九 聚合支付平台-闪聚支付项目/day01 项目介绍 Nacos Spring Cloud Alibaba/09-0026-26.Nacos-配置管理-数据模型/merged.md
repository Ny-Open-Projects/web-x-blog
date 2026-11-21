# 26.Nacos-配置管理-数据模型

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\26.Nacos-配置管理-数据模型【海量资源尽在 666java.com】.mp4
- 时长 5分11秒（音频 312s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下边呢我们来学习一下配置管理的数据模型那么我们如何去定位到一个具体的配置项呢那这里边呢注意我们要看一下它的数据模型那通过这个图呢大家可以看到最外层是不是就是Namespace这个就是命名空间用于隔离对吧这个和我们当初学习服务发现的时候是一样的它呢可以用于隔离环境对吧那也就是说在我们的这个Necros上面各位我们是不是建了很多
[00:29] 这个环境啊你看有DV默认的是不是一个public当然我们还可以建test生产等等各种环境那么环境是做隔离用的那里头呢还有一个group然后最下边是一个data id或Service这个Service就是指的是服务发现当初我们已经讲过就不再说了这里边有一个data id好这里边我们打开配置来看一下刚才我们是不是新建了一个配置你看
[00:57] 这里边是不是就是一个Data ID和Group大家看到了吗那么这个Data ID是不是就是一个配置文件的名称啊那这个配置文件的名称我在演示成这个基本流程的时候咱们看到其实它的过程呢其实就是通过Application Name这个服务的名称啊然后呢加上扩展名称就可以组成一个配置文件的名称这个名称
[01:25] 就对应到我们Necros里边的这个什么Data ID了要注意这个对应关系好另外那Group是什么呢Group默认的是Default Group但是Group在我们项目当中去正儿八经用的时候要注意它通常可以定义为一个具体的什么具体的项目名称具体的项目名称有时候老师这是啥意思你比如说举个例子我们有一个学生管理系统要用Necros
[01:55] 那学生管理系统是不是有很多的这个什么微服务是吧那每个微服务是不是也有很多配置文件呢所以这里边我们说我们就可以用group把这个什么配置集就是我们说的data id呢给它分组全部归到一个具体的项目组当中那这个学生管理系统我们可以给它定一个组名叫student group所以呢这时候我们说学生管理系统所有的配置集就是data id
[02:25] 那么他们统一归为Student Groups主对这就是我们说的这几个信息我们来总结一下Name Space命名空间用于隔离我们通常是建不同的环境这个和服务发现是一样的那配置集是Data ID它对应到一个具体的配置文件的名称那具体的对用方式其实就是Application的Name加配置文件的什么扩展名就自动拼装成一个配置文件的名称
[02:51] 好另外还有一个叫配置项配置项呢其实就是配置文件里边的各种什么各种key value的这些配置项目好最后一个就是配置分组配置分组我们说不用配它但是呢它具有一定的意义就是说Necros在设计的时候它很灵活看各个开发团体怎么用你像我们在进行开发实践的时候呢我们建议把配置分组配成我们项目的这个具体的名称
[03:21] 比如说我们散聚支付那我们就可以配成比如说叫散聚配下滑线group那所有散聚支付项目的配置它呢统一都归属为这个项目组好这就是我们说的什么配置管理的什么数据模型那最佳实践刚才我也说过了这namespace相当于环境group相当于什么项目
[03:47] 就是项目就是group这个分组还有data id就是指定到具体的配置文件这里边有一个对应关系大家可以看到但是每一个什么每一个项目组它的使用方法可能不是很一样但是我们最佳实践我们在进行开发实践的时候我们发现这么来使用Necros的配置管理是比较合理有效的所以就推荐给大家
[04:12] 这里边呢我想说一下的就是NetClose设计是比较灵活的就看大家怎么去用所以这里边我们针对Namespace Group Data ID的定义和我们实际项目当中的环境项目工程做一个什么具体的定义对应关系那Data ID刚才不是说过是个配置文件吗那配置文件你也知道这个项目它总有一个主配置文件是吧那主配置文件可能就是一个你比如说我们说的这个我们这个项目
[04:41] 那么它的主配置文件其实就对应了谁其实就是这个Networks RESTful Consumer.yml这就是它的一个对应关系具体的代码获取其实刚才我们已经演示过了发布配置获取配置那么我们可以回顾一下刚才发布获取配置的流程就可以了好那么到这里我们就了解了Networks配置管理的一个什么数据模型包括NamespaceGroup以及DataID

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Nacos 配置管理模型，包括 Namespace、Group、Data ID 的概念及其在配置集中的作用。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 Nacos 配置管理模型的 PPT 页面，包含一个三层嵌套的图示（Namespace 包含 Group，Group 包含 Service / DataId），并说明通过 Namespace、group、Data ID 能够定位到一个配置集。
画面2: Nacos 控制台界面，显示了配置管理页面，Namespace 为 public，Group 为 dev，Data ID 为 Nacos RESTful consumer.yml，Group 为 DEFAULT_GROUP。
画面3: Nacos 控制台界面，显示了配置管理页面，Namespace 为 public，Group 为 dev，Data ID 为空，Group 为 DEFAULT_GROUP。
画面4: IDEA 编辑器界面，显示了 RestConsumerController.java 文件中的代码，其中包含 @RequestMapping(value = "/configs") 和 return applicationContext.getEnvironment().getProperty("common.name");。
画面5: Nacos 控制台界面，显示了编辑配置页面，Data ID 为 Nacos RESTful consumer.yml，Group 为 DEFAULT_GROUP，配置内容为：
# common:
# name: application config
画面6: PPT 页面，说明配置集（Data ID）的概念，一个配置文件通常就是一个配置集，一个配置集可以包含系统的各种配置信息，例如，一个配置集可能包含了数据源、线程池、日志级别等配置项。每个配置集都可以定义一个有意义的名称，就是配置集的 ID 即 Data ID。
画面7: PPT 页面，展示配置集（Data ID）的定义，与画面6内容相同。
画面8: Nacos 控制台界面，显示了配置管理页面，Data ID 为 Nacos RESTful consumer.yml，Group 为 DEFAULT_GROUP。
画面9: PPT 页面，说明配置分组（Group）的概念，配置分组是对配置集进行分组，通过一个有意义的字符串（如 Buy 或 Trade）来表示，不同的配置分组下可以有相同的配置集（Data ID）。当您在 Nacos 中创建一个配置时，如果未填写配置分组的名称，则配置分组的名称默认采用 DEFAULT_GROUP。
画面10: PPT 页面，展示配置分组（Group）的定义，与画面9内容相同。
画面11: IDEA 编辑器界面，显示了 application.yml 文件中的配置内容，包括：
server:
  port: 8080
spring:
  application:
    name: Nacos-RESTful-consumer # 服务名
  cloud:
    Nacos:
      discovery:
        server-addr: 127.0.0.1:8848 # 服务发现中心地址
        namespace: alf8e63-3117-48c4-9dd3-e9ddc2af98a8 # 开发环境
        group: DEFAULT_GROUP # xx业务组
画面12: PPT 页面，说明获取某配置集的代码，需要指定 Nacos 服务地址、namespace、group、datalog。并给出了配置示例：
config:
  server-addr: 127.0.0.1:8848 # 配置中心地址
  file-extension: yaml
  namespace: alf8e63-3117-48c4-9dd3-e9ddc2af98a8 # 开发环境
  group: DEFAULT_GROUP # xx业务组
spring:
  application:
    name: Nacos-RESTful-consumer
  cloud:
    Nacos:
      discovery:
        server-addr: 127.0.0.1:8848 # 服务发现中心地址
        namespace: alf8e63-3117-48c4-9dd3-e9ddc2af98a8 # 开发环境
        group: DEFAULT_GROUP # xx业务组
画面13: PPT 页面，说明 Nacos 配置管理模型中 Namespace、Group、DataId 的具体含义：Namespace 代表不同环境，如开发、测试、生产环境；Group 代表不同项目，如 XX 医疗项目、XX 电商项目；DataId：每个项目下往往有若干个工程，每个配置集（DataId）是一个工程的主配置文件。并附带一个图示，展示 Namespace 包含 Group，Group 包含 DataId，以及 DataId 与工程的对应关系。
画面14: PPT 页面，展示配置管理模型的图示，与画面1内容相同。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面5 配置内容：
# common:
# name: application config

画面11 application.yml 配置：
server:
  port: 8080
spring:
  application:
    name: Nacos-RESTful-consumer # 服务名
  cloud:
    Nacos:
      discovery:
        server-addr: 127.0.0.1:8848 # 服务发现中心地址
        namespace: alf8e63-3117-48c4-9dd3-e9ddc2af98a8 # 开发环境
        group: DEFAULT_GROUP # xx业务组

画面12 配置示例：
config:
  server-addr: 127.0.0.1:8848 # 配置中心地址
  file-extension: yaml
  namespace: alf8e63-3117-48c4-9dd3-e9ddc2af98a8 # 开发环境
  group: DEFAULT_GROUP # xx业务组
spring:
  application:
    name: Nacos-RESTful-consumer
  cloud:
    Nacos:
      discovery:
        server-addr: 127.0.0.1:8848 # 服务发现中心地址
        namespace: alf8e63-3117-48c4-9dd3-e9ddc2af98a8 # 开发环境
        group: DEFAULT_GROUP # xx业务组

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1: 标题为“3.2.3 配置管理模型”，图示为三层嵌套结构：最外层为 Namespace，中间层为 Group，最内层为 Service / DataId。
画面6: 标题为“配置集(Data ID)”，内容为“在系统中，一个配置文件通常就是一个配置集，一个配置集可以包含了系统的各种配置信息，例如，一个配置集可能包含了数据源、线程池、日志级别等配置项。每个配置集都可以定义一个有意义的名称，就是配置集的ID即Data ID。”
画面9: 标题为“配置分组(Group)”，内容为“配置分组是对配置集进行分组，通过一个有意义的字符串（如 Buy 或 Trade）来表示，不同的配置分组下可以有相同的配置集（Data ID）。当您在 Nacos 中创建一个配置时，如果未填写配置分组的名称，则配置分组的名称默认采用 DEFAULT_GROUP。”
画面13: 标题为“Nacos 配置管理模型”，图示为三层嵌套结构：最外层为 Namespace，中间层为 Group，最内层为 DataId，并附带一个图示，展示 Namespace 包含 Group，Group 包含 DataId，以及 DataId 与工程的对应关系。
画面14: 标题为“配置管理模型”，图示为三层嵌套结构：最外层为 Namespace，中间层为 Group，最内层为 Service / DataId。

5) 无。

