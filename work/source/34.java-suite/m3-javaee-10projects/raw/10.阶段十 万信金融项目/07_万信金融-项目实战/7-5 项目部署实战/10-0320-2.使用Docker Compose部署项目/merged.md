# 2.使用Docker Compose部署项目

- 阶段：10.阶段十 万信金融项目
- 章节：07_万信金融-项目实战/7-5 项目部署实战
- 源文件：10.阶段十 万信金融项目\07_万信金融-项目实战\7-5 项目部署实战\2.使用Docker Compose部署项目_【海量资源尽在 666java.com】.mp4
- 时长 7分19秒（音频 440s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才呢我们整体上了解了一下什么是DevOps以及DevOps什么呀工具链这里边是有一堆工具是不是那咱接下来呢咱这个万新金融P2P这个项目已经开发完毕了接下来首先要做的是不是要把它部署到服务器上把它给刨起来是不是那我们自然就要用到DevOps工具链当中的某些什么呀某些工具了首先我们要用到的就是什么呀Docker
[00:30] 啊Docker这是咱们前面讲过也用过啊据来说的就是使用Docker Compose啊要把我们的这个项目给他干什么呀对部署到服务器上对吧我们要把生产环境搭起来哎然后呢就可以把这个项目部署上去然后给他跑起来那具体的话大家要看这个文档啊万信金融生产环境部署文档一个pdf文件里边呢有呃非常详细的
[01:00] 整个生产环境的搭建以及项目的一个部署大家看一下在这我们整体过一遍因为整个生产环境的搭建以及项目部署这个过程是需要你自己去完成的因为整个这里边不涉及到新的知识新的内容主要就是通过Docker或者Docker Compose来实现整个环境的搭建和项目的一个部署整体咱快速的过一遍
[01:29] 首先呢就是整个这个数据架构吧大家看前端对吧前端呢然后去发请求到我们的这个什么呀对后端就是微服对不对然后微服再往后呢就是他们各自使用的这个什么呀对数据库这个呢大家都很熟悉了嘛因为整个这个项目咱前一段一直在开发嘛这个大家都很熟悉然后服务架构大家看一看还是前端吧前端发请求先过什么呀网关啊网关再分发请求到各个什么呀
[01:57] 对微服务然后中间有一些公共的组件比如说这个什么呀注册中心然后这个什么呀统一配置中心Apollo这些大家都非常熟悉啊我们其他微服务是不是要注册到这个什么呀对这个这个注册中心然后要从这个Apollo这个配置中心要取这个什么获取配置是不是然后如果你要跟银行那边打交道的话要交互的话是不是都得通过这个什么呀对存管代理服等等等等吧这是整个这个架构这个大家比较熟我们
[02:26] 还是刚才说的吗前一段一直在开发这个项目啊这些大家都很熟悉呃这一块呢是咱们一会儿在部署的时候呢我们提前呢规定了一些什么呀对一些名字啊一些端口号一些路径啥的当然这个呢是这样啊大家尽量都按照咱这个规定来进行这个什么呀部署呃当然呢这里边有些这个东西不是说你不可以改肯定都是可以改的啊你比如说有朋友说老师这个306这个端口我由于种种原因
[02:57] 已经被占用了那你就改成307 308对不对那我们这呢只是建议建议大家尽量按照这个文档里边的要求对吧这个目录放到哪占用哪个端口对吧他映射的哪些哪些这个目录哪些路径他尽量都保持一致因为我我这个文档的下边下边他给的一些这个你像这个那个啥对DocCompass这里边的一些这个内容
[03:26] 像这些路径其实都是跟上面这儿是干什么呀对应着啊你要是自己改了改路径反正你自己部署的时候就那那个路径你都得注意要给他改一改啊我这儿呢是我们统一做了一个规划吧啊就部署之前统一做了一个规划这个下雨大家自己看一下就行了然后接下来就开始正式的进行这个生产环境的一个搭建那些首先是个点安装导客呀对不对你看你你这个服务器上有没有安装导客没有你需要安装一下啊注意一下
[03:55] 这个版本啥的咱也都要保持什么呀对保持一致安装启动对吧还要安装Docker Compose版本号啥的这个都是一些命令大家参考一下去操作就行了那么这个Docker Compose呢全部安装完之后呢我们接下来就要开始部署咱这个项目要做一些这个准备工作比如说我们要建一堆目录大家知道我们万一金融P2P项目要部署的东西可多了是不是微服务一堆前端两个是不是还有银行的那个系统
[04:27] 所以说呢为了这个将来我们部署的时候方便我们提前要建一堆目录将来呢我们要把相关的东西放到各自的这个什么呀目录里面你看这里边是不是还要装很多软件嘛对不对所以你按照咱这个文档的要求该建目录建目录谁是总目录谁是子目录对不对这个名字最好也不要随便乱起目录建好之后呢咱就开始先装软件嘛对不对生产环境你得先搭一搭比如说JDK这不再说了My Circle
[04:57] 是不是我们基本上都是通过Docker Compose来进行这个安装启动运行的啊这边该给的东西全部都有Apollo你看ApolloRocket MQ对吧SoKeeper ES LogStageRedis对吧这是相关的软件我们就装完了装完之后呢接下来就是要部署我们的这个什么微服务比如说验证吧还有我们的银行存管系统是不是还有我们整个万信金融的这个什么呀
[05:28] 后端的这一堆什么呀微服务是不是你就按照这个文档进行操作进行这个过程是就是要看他细心不细心甚至你有没有耐心啊因为整个这个搭建盛产环境的部署的这个过程他有时候会比较慢啊甚至他也会经常出错所以说你还得有耐心细心加耐心吧全都是通过这个Docker Compose来进行部署进行这个启动运行的
[06:01] 这里边有些这个数据你在用的时候要注意有些路径啊端口号啊有些参数啊你可以适当的根据你电脑个人电脑这个情况要做出修改你不能完全照抄这这个文档里边这个这个内容大家一定要注意还有前端是不是前端的这个地方大家要注意一下前端稍微特殊一些啊咱们开发过程当中是给大家发了这么一个前端对不对那么你现在在部署的时候就不能用它了它那里边的环境
[06:30] 不完整啊不完整那么咱本次这个课项里边提供了还有一个前端工程你用那个就行啊课项里边都有我给大家都准备好有些细节反正这个讲讲义里边或者这个文章里面都有啊就说你要细心的去看一看那整个前端后端生产环境全都部署好都启动起来你就可以像你平时一样对吧打开前端进行登录然后看看里边的一些数据一些功能你就操作操作就OK了这是整个生产环境的搭建以及项目的这个什么呀
[07:00] 不服还是我刚才说了啊细心加耐心啊参考这个文档然后自己去实现这是我们说的用Docker啊或者说Docker Compose把整个生产环境和这个项目给它部署上去

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解万信金融平台的 DevOps 工具链、服务部署架构及使用 Docker 和 Docker Compose 进行项目部署的实践步骤。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 DevOps 工具链的环形图，包含 CI/CD、自动化测试、部署等环节，图中列出多个工具如 Git、Docker、Jenkins、Kubernetes 等。
画面 2: 展示服务部署架构图，包含统一认证、用户中心、交易中心、还款中心等模块，以及 p2p_account、p2p_consumer、p2p_transaction、p2p_repayment 等数据服务，下方有标的/投标数据的分片存储。
画面 3: 展示服务部署架构的详细流程图，包含统一认证、用户中心、交易中心、还款中心、公共服务、配置中心、库存管理服务、银行存管系统前端、银行存管系统后台等模块，以及它们之间的调用关系。
画面 4: 展示服务部署配置表，包含服务名称、服务目录、端口、服务数据映射目录等信息，如 mysql、apollo、rmqnamesrv、rmqbroker、rmaconsole、elastic-search 等服务的配置。
画面 5: 展示安装 Docker 的命令，包括卸载旧版本、安装 Docker-ce、containerd.io、Docker-ce-cli 等包，以及启动 Docker 服务的命令。
画面 6: 展示卸载 Docker 版本的命令，以及检查 Docker 版本的命令。
画面 7: 展示安装 Docker 的命令，与画面 5 内容相同。
画面 8: 展示安装 JDK 1.8 和 MySQL 的步骤，包括在 mysql 目录下新建 init.sql 文件，从课程中找到 init.sql 并复制到该文件夹中。
画面 9: 展示编写 Docker-compose.yml 文件的内容，包括 apollo-configservice 和 apollo-adminservice 服务的配置，如 image、ports、volumes、environment 等。
画面 10: 展示部署验证码服务的步骤，包括在 sailing 目录下编写 Docker-compose.yml 文件。
画面 11: 展示在 IDEA 中打包各个微服务，并复制 jar 文件到对应的目录。
画面 12: 展示 Docker-compose.yml 文件中 waningzp-depository-agent-Service 服务的配置，包括 container_name、build、image、network_mode、ports、depends_on、restart 等。
画面 13: 展示部署万信平台前端的步骤，包括找到前端工程、复制到 web 目录、修改请求地址和文件服务地址，以及编写 Docker-compose.yml 文件。
画面 14: 展示 DevOps 工具链的环形图，包含 CI/CD、自动化测试、部署等环节，图中列出多个工具如 Git、Docker、Jenkins、Kubernetes 等，并说明之前学习过的 Docker、Git、Node、npm，以及本次学习的 Jenkins 和 Gogs 都属于 DevOps 工具链。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 9:
```yaml
version: "3"

services:
  apollo-configservice:
    container_name: apollo-configservice
    image: apollo-configservice:1.6.0
    ports:
      - "8080:8080"
    volumes:
      - "/logs/100003171:/opt/logs/100003171"
    environment:
      spring.datasource.url: "jdbc:mysql://127.0.0.1:3306/ApolloConfigDB?characterEncoding=utf8"
      spring.datasource.username: "root"
      spring.datasource.password: "123"
      JAVA_OPTS: "-Xms512m -Xmx512m -Xmn256m"
  apollo-adminservice:
    container_name: apollo-adminservice
```

画面 10:
```yaml
version: "3"

services:
  sailing:
    container_name: sailing
    build: .
```

画面 11:
```bash
# 万信金融平台服务
wanningzp-account-Service
wanningzp-consumer-Service
wanningzp-transaction-Service
wanningzp-depository-agent-Service
wanningzp-repayment-Service
```

画面 12:
```yaml
restart: always
volumes:
  - "/logs/logs"
environment:
  SERVER_PORT: "53060"
  JAVA_OPTS: "-Xms512m -Xmx512m -Xmn256m -Dserver.port=53060 -Denv=dev -Dapollo.cluster=DEFAULT"
wanningzp-depository-agent-Service:
  container_name: wanningzp-depository-agent-Service
  image: wanningzp-depository-agent-Service:1.0-SNAPSHOT
  network_mode: "host"
  ports:
    - "53070:53070"
  depends_on:
    - wanningzp-discover-server
  restart: always
```

画面 13:
```javascript
const Baseurl = "http://127.0.0.1:53010/"
const Fileserviceurl = "http://127.0.0.1:536082/Farming/"
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2:
- 标题：1.2 服务部署
- 架构图结构：
  - 统一认证 → 用户中心 → 交易中心 → 还款中心
  - 用户中心 → 交易中心
  - 交易中心 → 还款中心
  - 统一认证 → 公共服务
  - 公共服务 → 交易中心
  - 交易中心 → 还款中心
  - 还款中心 → 标的/投标数据
  - 标的/投标数据 → 分片存储（shard1、shard2、shard3）

画面 3:
- 标题：1.2 服务部署
- 架构图结构：
  - 统一认证 → 用户中心 → 交易中心 → 还款中心
  - 用户中心 → 交易中心
  - 交易中心 → 还款中心
  - 统一认证 → 公共服务
  - 公共服务 → 交易中心
  - 交易中心 → 还款中心
  - 还款中心 → 标的/投标数据
  - 标的/投标数据 → 分片存储（shard1、shard2、shard3）
  - 银行存管系统前端 → 银行存管系统后台

画面 4:
- 标题：服务部署配置表
- 表格数据：
  | 服务名称 | 服务目录 | 端口 | 服务数据映射目录 |
  | --- | --- | --- | --- |
  | mysql | /mysql | 3306 | 数据库文件：/db 初始化脚本：/init/init.sql |
  | apollo | /apollo/apollo-configservice | 8080 | 日志：/logs/100003171 |
  | apollo | /apollo/adminservice | 8090 | 日志：/logs/100003172 |
  | apollo | /apollo/portal | 8070 | 日志：/logs/100003173 |
  | rmqnamesrv | /rmq | 9876 | 数据：/data/store 日志：/data/logs |
  | rmqbroker | /rmq | 10909 | 配置：/data/broker/conf/broker.conf |
  | rmaconsole | /rmq | 60000 | 配置：/data/broker/conf/broker.conf |
  | elastic-search | /es | 9200 | 配置：/elasticSearch.yml |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

