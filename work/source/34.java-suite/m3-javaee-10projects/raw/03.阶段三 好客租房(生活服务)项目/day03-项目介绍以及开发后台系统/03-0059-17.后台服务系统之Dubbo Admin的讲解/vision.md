# 画面线理解：17.后台服务系统之Dubbo Admin的讲解

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\17.后台服务系统之Dubbo Admin的讲解【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:35, 01:02, 01:20, 02:06, 03:02, 03:29, 03:44, 04:06, 04:39, 04:52, 05:58, 06:52, 07:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:36:41

1) 这一组画面整体在讲如何下载、配置并启动 Dubbo Admin 控制台，用于管理 Dubbo 服务。

2) 按时间顺序列出每张画面的要点：
画面1：在 Markdown 文档中介绍 Dubbo Admin，提供 GitHub 地址，并列出第一步下载并解压的命令。
画面2：展示 Dubbo 控制台的 GitHub 项目页面，包含“页面截图”和“前端部分”等说明。
画面3：通过 Xshell 连接到远程 Linux 服务器（IP: 172.16.55.185），登录后进入根目录。
画面4：在服务器上进入 `incubator-dubbo-ops` 目录，列出其内容，包括 `dubbo-admin-backend/` 和 `dubbo-admin-frontend/` 等子目录。
画面5：在服务器上进入 `incubator-dubbo-ops` 目录，列出其内容，包括 `dubbo-admin-backend/` 和 `dubbo-admin-frontend/` 等子目录。
画面6：在 Markdown 文档中展示第二步修改配置文件 `application.properties`，其中 `dubbo.registry.address` 被设置为 `zookeeper://172.0.0.1:2181`。
画面7：在 Markdown 文档中展示第三步使用 Maven 构建项目，包括上传并解压 Maven、配置环境变量、执行 `mvn clean package` 和 `mvn -projects dubbo-admin-backend spring-boot:run` 命令。
画面8：在 Xshell 中展示 Maven 配置文件 `settings.xml` 的内容，包含两个镜像配置：`<mirror>` 和 `<mirror>`。
画面9：在服务器上进入 `incubator-dubbo-ops` 目录，列出其内容，包括 `dubbo-admin-backend/` 和 `dubbo-admin-frontend/` 等子目录。
画面10：在服务器上执行 `mvn -projects dubbo-admin-backend spring-boot:run` 命令，开始启动后端服务。
画面11：在 GitHub 上展示 `incubator-dubbo-ops` 仓库的文件列表，包括 `README.md`、`LICENSE`、`pom.xml` 等。
画面12：在 Dubbo OPS 控制台中展示服务详情，包括服务名、分组、版本、提供者和消费者信息。
画面13：在 Markdown 文档中展示第三步使用 Maven 构建项目，包括上传并解压 Maven、配置环境变量、执行 `mvn clean package` 和 `mvn -projects dubbo-admin-backend spring-boot:run` 命令。
画面14：在 Markdown 文档中展示服务的负载均衡部分，包括“Random LoadBalance”及其说明。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
第一步，下载并解压：
1 git clone https://github.com/apache/incubator-dubbo-ops.git
2 解压使用命令解压到指定目录
```
画面6：
```
第二步，修改配置文件：
在 dubbo-admin-backend/src/main/resources/application.properties 中修改注册中心地址。
```
画面6：
```
dubbo.registry.address=zookeeper://172.0.0.1:2181
```
画面7：
```
第三步，使用maven进行构建项目：
如未安装maven请先安装maven
1. 上传解压apache-maven-3.6.0-bin.tar.gz
2. 配置环境变量：
   1. vim /etc/profile
   2. 添加如下内容：
      export MAVEN_HOME=/haoke/apache-maven-3.6.0
      export PATH=$MAVEN_HOME/bin:$PATH
构建命令：
   mvn clean package
第四步，通过maven插件启动程序：
   mvn -projects dubbo-admin-backend spring-boot:run
```
画面8：
```
<mirrors>
  <mirror>
    <id>mirrorId</id>
    <mirrorOf>central</mirrorOf>
    <name>Human Readable Name for this Mirror.</name>
    <url>http://my.repository.com/repo/path</url>
  </mirror>
  <mirror>
    <id>nexus-aliyun</id>
    <mirrorOf>*</mirrorOf>
    <name>Nexus aliyun</name>
    <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
  </mirror>
</mirrors>
```
画面10：
```
mvn -projects dubbo-admin-backend spring-boot:run
```
画面13：
```
第三步，使用maven进行构建项目：
如未安装maven请先安装maven
1. 上传解压apache-maven-3.6.0-bin.tar.gz
2. 配置环境变量：
   1. vim /etc/profile
   2. 添加如下内容：
      export MAVEN_HOME=/haoke/apache-maven-3.6.0
      export PATH=$MAVEN_HOME/bin:$PATH
构建命令：
   mvn clean package
第四步，通过maven插件启动程序：
   mvn -projects dubbo-admin-backend spring-boot:run
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“3.2.6. dubbo Admin”，内容包括“Dubbo提供了可视化界面管理工具，方便我们对服务进行管理，它就是dubbo admin，代码地址：https://github.com/apache/incubator-dubbo-ops”。
画面12：Dubbo OPS 控制台页面，包含“Service”、“App”、“Group”、“Version”等字段，以及“PROVIDERS”和“CONSUMERS”表格，表格中包含“IP”、“Port”、“Timeout(ms)”、“Serialization”和“Operation”列。
画面14：PPT 标题为“3.2.7. 服务的负载均衡”，内容包括“在集群服务均需用，Dubbo 提供了多种均衡策略，缺省为 random 随机策略，具体参看：http://dubbo.apache.org/zh-cn/docs/user/demos/loadbalance.html”，并列出“Random LoadBalance”及其说明。

5) 不要评价画面美观，不要输出与课程无关的内容。
