# 画面线理解：2.使用Docker Compose部署项目

- 阶段：10.阶段十 万信金融项目
- 章节：07_万信金融-项目实战/7-5 项目部署实战
- 源文件：10.阶段十 万信金融项目\07_万信金融-项目实战\7-5 项目部署实战\2.使用Docker Compose部署项目_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:42, 02:23, 03:16, 03:27, 03:44, 04:00, 04:48, 05:06, 05:15, 05:51, 05:59, 06:17, 07:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:59:14

1) 这一组画面整体在讲什么（一句话）：
讲解万信金融平台的 DevOps 工具链、服务部署架构及使用 Docker 和 Docker Compose 进行项目部署的实践步骤。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 DevOps 工具链的环形图，包含 CI/CD、自动化测试、部署等环节，图中列出多个工具如 Git、Docker、Jenkins、Kubernetes 等。
画面 2: 展示服务部署架构图，包含统一认证、用户中心、交易中心、还款中心等模块，以及 p2p_account、p2p_consumer、p2p_transaction、p2p_repayment 等数据服务，下方有标的/投标数据的分片存储。
画面 3: 展示服务部署架构的详细流程图，包含统一认证、用户中心、交易中心、还款中心、公共服务、配置中心、库存管理服务、银行存管系统前端、银行存管系统后台等模块，以及它们之间的调用关系。
画面 4: 展示服务部署配置表，包含服务名称、服务目录、端口、服务数据映射目录等信息，如 mysql、apollo、rmqnamesrv、rmqbroker、rmaconsole、elastic-search 等服务的配置。
画面 5: 展示安装 Docker 的命令，包括卸载旧版本、安装 docker-ce、containerd.io、docker-ce-cli 等包，以及启动 Docker 服务的命令。
画面 6: 展示卸载 Docker 版本的命令，以及检查 Docker 版本的命令。
画面 7: 展示安装 Docker 的命令，与画面 5 内容相同。
画面 8: 展示安装 JDK 1.8 和 MySQL 的步骤，包括在 mysql 目录下新建 init.sql 文件，从课程中找到 init.sql 并复制到该文件夹中。
画面 9: 展示编写 docker-compose.yml 文件的内容，包括 apollo-configservice 和 apollo-adminservice 服务的配置，如 image、ports、volumes、environment 等。
画面 10: 展示部署验证码服务的步骤，包括在 sailing 目录下编写 docker-compose.yml 文件。
画面 11: 展示在 IDEA 中打包各个微服务，并复制 jar 文件到对应的目录。
画面 12: 展示 docker-compose.yml 文件中 waningzp-depository-agent-service 服务的配置，包括 container_name、build、image、network_mode、ports、depends_on、restart 等。
画面 13: 展示部署万信平台前端的步骤，包括找到前端工程、复制到 web 目录、修改请求地址和文件服务地址，以及编写 docker-compose.yml 文件。
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
wanningzp-account-service
wanningzp-consumer-service
wanningzp-transaction-service
wanningzp-depository-agent-service
wanningzp-repayment-service
```

画面 12:
```yaml
restart: always
volumes:
  - "/logs/logs"
environment:
  SERVER_PORT: "53060"
  JAVA_OPTS: "-Xms512m -Xmx512m -Xmn256m -Dserver.port=53060 -Denv=dev -Dapollo.cluster=DEFAULT"
wanningzp-depository-agent-service:
  container_name: wanningzp-depository-agent-service
  image: wanningzp-depository-agent-service:1.0-SNAPSHOT
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
