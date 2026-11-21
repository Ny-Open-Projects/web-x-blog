# 17.后台服务系统之Dubbo Admin的讲解

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\17.后台服务系统之Dubbo Admin的讲解【海量资源尽在 ubkz.com】.mp4
- 时长 7分22秒（音频 442s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下double的这个admin啊那么这个呢是double为我们提供的一个可视化的一个界面的管理工具啊那么它的目的呢其实就是方便我们对服务进行管理那么这个就是double这个admin啊那么它的一个代码的一个地址呢是在github上面我们来看一下是在这个位置啊是在这个位置那么它下面呢
[00:26] 它下面也有一个中文的书名大家可以去看一下那么它的一个WD控制台界面大概长这样的一个界面一会我们来去搭建一下带大家去搭建一下好那我们来看一下那么部署的一个步骤那么我们来一步一步给大家讲解一下那么首先第一步去做一个克隆克隆KitHub上面这个项目就是把这个项目刚刚我们所看到的这个项目你克隆到你的本地
[00:56] 我们这个服务器上面去做一个部署啊那么是这么来玩的哎那就这样吧好然后呢我进入我在这儿有在根目录下面有一个号客这个呃这个目录然后呢我在这儿呢做一个克隆他就会有这样的一个目录去生成那么就会把一些相关的一些文件呢全部都克隆下来这个是我克隆到我本地的这样的一个呃结果啊这样的情况是这样的
[01:25] 好那么我们下面看第一步就完成了如果说你不想去使用克隆的话那么你可以去使用我们在资料中给大家提供的一个压缩包那么也可以使用它做一个解压也可以ok
[01:37] 好第二步呢是需要你去修改一个配置文件在这个application的properties中指定一个注册中心的一个地址那么它默认的就是配置的本机的一个2181那么我刚好呢我的这个注册中心呢就在我本机啊所以说呢也不需要做修改了但是呢如果说你不一样的话你也需要去修改一下这是第二步
[01:59] 第三步呢我们通过一个需要通过一个man文的命令做构建就是进入到我们这个目录啊就是他的这个项目的根目录在这个里面输入个命令叫做mvn clean然后呢package啊package然后呢就这个命令通过这个命令去做构建那么所以呢大家需要注意的是那么你需要在这个上面通过一个man文的命令做构建那么也就意味着你在这个机器上面你的服务器这个上面啊要装有这个man文的这个
[02:29] 装有Maven那么如果说你没有装Maven的话那么这个命令你肯定是不能使用的对不对所以我们需要先去安装一个Maven那么Maven的安装是比较简单的在这我就不做演示了我简单说一下就是你上传一个Maven的安装包这个在我们资料中也有为大家做一个提供来看一下那么是在这个里面在这有一个安装包来找一下开发环境相关
[02:58] 然后在这个下面是不是有一个Apache Mavic 3.6.0的这样的一个安装包然后你上传到你的服务器之后然后把它解压开来解压开来去配置一个环境变量就可以了那么可以看一下我现在的目前的已经是装好了是不是就在这个位置把它解压然后去配置一个环境变量就OK了配置环境变量在这配到这来就OK了
[03:24] 当然了那么我们还需要给Maren做一个配置就是去修改他的一个私服的一个仓库那么我们在这采用的是阿里云的这个私服那么找一下找这个Mirror在这这个大家应该都配置过那么配置一个他那么就我们可以使用这个
[03:48] 阿里云给我们提供的一个这个Mainware的一个仓库这样的话我们要比从直接从这个中央仓库下载呢要快很多啊好那么这个呢当我们把这个Mainware安装好之后啊就可以去输入下面这个命令那么输入命令呢就可以做个构建那么要注意的是那么它整个构建过程呢是比较长的啊所以呢我在这就不做演示了那么只要你你的这个环境啊按照我所说的这个环境做一个
[04:16] 安装部署然后我相信通过一个Mainway这样的去构建的话是没有任何问题的去构建出来的那么但是时间会相对比较长一点需要大家耐心的去等待一下那么第四步就是我们通过Mainway的一个插件去启动那么我们在这进入到这个项目目录然后把这个mini靠过来然后启动一个Spring Boot的这个做那么我就不做一个启动了因为我前面这个窗口已经启动起来了大概就是这样的一个输出好
[04:44] 那么我们接下来的就可以去来访问一下我们这个页面啊这个页面的要访问你的这个机器然后呢端口呢是8080然后呢我们去访问一下啊在这172啊8080就他走
[04:59] 那么我们显然就可以访问到我们这个admin的这个一个项目啊那么在这个里面呢我们呃他有些功能的还没有做实现啊那我们可以在第一个来查看一下就是说Service的一个search那么我们可以去搜一下搜一下我们现在是不是已经有一个服务了对吧那我们点击这个通过这个application去搜一下demo是不是我们自己写的这个demo的工程然后点击这个search搜索然后呢可以看到
[05:25] 在搜索的这个relaunch的结果中是不是有一个我们的一个服务就是这个user Service这个服务版本是1.0然后它所在应用的是privileged demo而这个值在哪里配置是不是在我们刚刚的这个里面在我们这个Service下面是不是有一个配置是不是在这有一个这个的配置在这这个的配置就是应用的名称了应用的名称点击后面有个detail
[05:52] 来查看他的一个详情那么在这个详情中你可以看到一些基本的basic的info就基本的信息还可以看一些server的信息那么这个是provider的信息那么我们现在有一个提供者服务的提供者那么他的url那么就是这样的url鼠标移到上面就会有一个显示然后可以看到他使用的协议是double协议然后这个是consumerconsumer现在没有
[06:16] 那么我们的consumer已经就结束了它就没有啊哎OK好那么如果你有正在consumer正在运行的话就可以看到有consumer的信息下面的还有些meta信息我们现在没有一些meta信息好那么其他的呢包括一些什么路由啊动态的一些这个config啊等等的那么我们就不做一个这个介绍讲解了那么大家呢也可以自行去做一些这个研究啊哎OK好那么我们来看一下我们的讲义啊
[06:44] 那么可以看到去搜索服务也可以看到我们的提供者的详情包括我们那些消费者的详情等等一些内容好那么关于Admin我们就讲到这里大家也可以把它去做一些部署然后做一些构建然后去使用一下还是比较好用的这样的一个工具那么在这多说一句Admin工具要比
[07:05] 早期的Admin工具要好看很多早期的Admin是一个比较丑的这样的一个Admin好那么关于Admin我们就先讲到这里下面我们要给大家讲解的是服务的负载均衡好那么Admin我们就讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何下载、配置并启动 Dubbo Admin 控制台，用于管理 Dubbo 服务。

2) 按时间顺序列出每张画面的要点：
画面1：在 Markdown 文档中介绍 Dubbo Admin，提供 GitHub 地址，并列出第一步下载并解压的命令。
画面2：展示 Dubbo 控制台的 GitHub 项目页面，包含“页面截图”和“前端部分”等说明。
画面3：通过 Xshell 连接到远程 Linux 服务器（IP: 172.16.55.185），登录后进入根目录。
画面4：在服务器上进入 `incubator-dubbo-ops` 目录，列出其内容，包括 `dubbo-admin-backend/` 和 `dubbo-admin-frontend/` 等子目录。
画面5：在服务器上进入 `incubator-dubbo-ops` 目录，列出其内容，包括 `dubbo-admin-backend/` 和 `dubbo-admin-frontend/` 等子目录。
画面6：在 Markdown 文档中展示第二步修改配置文件 `application.properties`，其中 `dubbo.registry.address` 被设置为 `ZooKeeper://172.0.0.1:2181`。
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
dubbo.registry.address=ZooKeeper://172.0.0.1:2181
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

