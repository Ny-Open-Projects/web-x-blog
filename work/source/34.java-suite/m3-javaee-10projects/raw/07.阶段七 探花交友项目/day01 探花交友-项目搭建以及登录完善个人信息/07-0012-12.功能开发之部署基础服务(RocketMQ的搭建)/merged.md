# 12.功能开发之部署基础服务（RocketMQ的搭建）

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\12.功能开发之部署基础服务（RocketMQ的搭建）_【海量资源尽在 666java.com】.mp4
- 时长 4分20秒（音频 260s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来部署log的mq那么去拉取这个镜像呢我就不拉取了这个我已经拉取过了然后呢下面我们直接来创建容器啊那么在这个位置呢我们先创建单节点的我们这个log的mq那么先没有去组件集群那么我们首先需要创建的是它的一个name server然后呢我们再去创建它的一个
[00:24] 这个block server那么接下来呢我们先在这个位置先去注意啊先要退出到我们的一个主机然后呢去做一个执行那么我们把这个呢就拷贝过来拷贝一下再上那我们来看一下这个创建的一个脚本那么可以看到在这个位置呢我们指定了它端口的映射呢是9876然后呢这个容器的名字呢叫做什么呢这个rmq server
[00:52] 然后呢下面指定它一些参数啊这个是指定的jvm的一些参数啊等等好然后呢我们直接回车可以看到这个容器呢就创建好了那么接下来呢我们就需要创建一个这个文件啊那么这个文件呢是我们下面的broke这个服务它所需要的一个这样的文件那么在这个文件中呢我们需要指定我们的broke的ip地址以及我们name server的ip地址以及这个端口啊然后指定我们broke这个name啊这个是一个关键需要去指定一下
[01:22] 那我们来看一下这个文件啊这个文件我应该是已经存在的文件啊那么这个文件的路径要注意那么这个文件路径是可以随意去创建的啊但是一定要注意和下面的这个位置啊要对应起来啊这个位置要对应起来好嘞好那么这个文件呢跟我的蒋一东文件的内容是一样的那么我就不再重复去创建了那么接下来呢我就创建这个
[01:46] 这个容器就可以了那么在这个容器中其实可以看到我们需要指定两个端口的映射一个是10911一个是10909然后就指定一些我们的JVM的参数指定我刚刚所说的配置文件以及其他logsstore这样的一些配置OK好那么我们去把命令来拷贝一下到这个位置来做一个执行好那么到这里我们的容器也就创建好了
[02:15] 那么接下来我们需要把我们这两个容器分别都给它启动起来start启动当然了如果你有需求的话那么也可以把它stop以及或者把它删除掉好那么这个就是我们已经把Rock.mq的服务就已经跑起来了那么跑起来之后我们还需要一个它的一个管理工具那么我们把这管理工具也跑一下那么这个
[02:42] 管理工具是需要重新去拉取一个镜像的那么这个镜像我就不做一个拉取了那么因为我已经拉取过了那么接下来我就只需要去run或者说去创建这个容器就可以了那么这个容器它就是我们刚刚所拉取到的这个镜像然后我们去指定一些参数比如说我们来指定name server的一个地址这样就OK那么并且我们指定它访问的端口是8082
[03:10] 那么接下来呢我们来把这个命令呢拷贝一下到这个位置呢去做一个执行等待它的一个运行那么运行结束之后呢我们就可以尝试的来访问一下啊OK好那么要注意在这个位置它显示的是8080这个是容器内部的一个端口那么我们要去访问它呢要通过什么的8082去做一个访问好那我们一起来访问一下那么我们来打开我们这个浏览器来访问一下就是192.168
[03:38] 什么呢就是31.81下面的8082走那么其实可以看到我们已经访问到了我们的这个就是我们的管理工具然后呢我们切换一下这个语言切换成中文然后呢我们可以看到在这个位置集群是不是已经可以看到我们刚刚所看到的这样的一个集群的信息了OK那么到目前为止呢基本上呢我们这个RockMQ这个服务呢就搞定了那么我们把这个管理工具呢也部署好了
[04:08] 那我们就可以去正常使用了那么后面我们在开发开发的过程中就可以直接去使用它了ok好那么关于这个ROG MQ的一个环境的一个搭建那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Docker 部署 RocketMQ 服务（包括 NameServer 和 Broker），并搭建客户端进行测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 文档中关于 RocketMQ 的 Docker 部署脚本，包含拉取镜像、创建 NameServer 和 Broker 容器的命令。
画面2：在终端中使用 redis-cli 检查 Redis 集群节点状态，并执行 set、get、del 命令测试数据操作。
画面3：与画面2相同，终端中执行 Redis 命令，显示数据操作成功。
画面4：在 Typora 文档中，高亮显示创建 Broker 容器的 Docker 命令，包含配置文件路径和端口映射。
画面5：在 Typora 文档中，高亮显示创建 Broker 容器的 Docker 命令，包含配置文件路径和端口映射。
画面6：在 Typora 文档中，高亮显示创建 Broker 容器的 Docker 命令，包含配置文件路径和端口映射。
画面7：在 Typora 文档中，高亮显示启动、停止和删除容器的命令，以及拉取 RocketMQ 管理工具的命令。
画面8：在 Typora 文档中，高亮显示拉取 RocketMQ 管理工具的命令，以及运行管理工具的命令。
画面9：在 Typora 文档中，高亮显示运行 RocketMQ 管理工具的命令，以及客户端开发环境的安装说明。
画面10：在终端中启动 Spring Boot 应用，显示应用启动日志，包括 Tomcat 初始化和 Servlet 引擎启动。
画面11：在终端中显示 Spring Boot 应用启动日志，包括注册健康检查端点、指标端点等。
画面12：在浏览器中搜索并访问 RocketMQ 管理工具的地址。
画面13：在浏览器中访问 RocketMQ 管理工具，显示安全警告弹窗。
画面14：在 Typora 文档中，高亮显示运行 RocketMQ 管理工具的命令，以及客户端开发环境的安装说明。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```markdown
#拉取镜像
Docker pull foxiswho/RocketMQ:server-4.3.2
Docker pull foxiswho/RocketMQ:broker-4.3.2

#创建nameserver容器
Docker create -p 9876:9876 --name rmqserver \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v rmqserver-logs:/opt/logs \
-v rmqserver-store:/opt/store \
foxiswho/RocketMQ:server-4.3.2

#创建broker.conf文件
vim /itcast/rmq/rmqbroker/conf/broker.conf
brokerIP1=192.168.31.81
namesrvAddr=192.168.31.81:9876
brokerName=broker_tanhua
```

画面4：
```markdown
#创建broker容器
Docker create -p 10911:10911 -p 10909:10909 --name rmqbroker \
-e "JAVA_OPTS=-Duser.home=/opt" \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-v /itcast/rmq/rmqbroker/conf/broker.conf:/etc/RocketMQ/broker.conf \
-v rmqbroker-logs:/opt/logs \
-v rmqbroker-store:/opt/store \
foxiswho/RocketMQ:broker-4.3.2
```

画面7：
```markdown
#启动容器
Docker start rmqserver rmqbroker

#停止删除容器
Docker stop rmqbroker rmqserver
Docker rm rmqbroker rmqserver

#拉取RocketMQ的管理工具
Docker pull sty1atang/RocketMQ-console-ng:1.0.0

#启动管理工具
Docker run -e "JAVA_OPTS=-Drocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithIPChannel=false" -p 8080:8080 -t sty1atang/RocketMQ-console-ng:1.0.0
```

画面9：
```markdown
3.1.4. 搭建客户端
客户端点击前端团队进行开发，前端提供api对接，所以，需要我们安装安装的模拟端进行测试。

安装步骤：
• 首先安装VirtualBox-4.3.10-93012-Win.exe
• 其次安装genymotion 2.6.0.exe
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

