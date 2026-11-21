# 08.部署RocketMQ的管理工具

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\08.部署RocketMQ的管理工具【海量资源尽在 ubkz.com】.mp4
- 时长 3分25秒（音频 205s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么我们接着继续前面我们通过Docker的形式去将我们的RockDMQ的服务就部署起来了那么接下来我们来部署一下它的管理工具RockDMQ也提供了一个UI的管理工具还是一个比较炫酷的一个UI工具好,那我们来看一下它的一个UI工具的名字叫做RockDMQ Console这样的一个名字项目地址在这那么我们可以点击这个地址来看一下它的这个项目
[00:29] 那么我们其实可以看到它这个项目其实支持有两种方式的安装第一种就是Docker的安装第二种就是非Docker的安装当然了我们比较建议使用的是Docker的安装那么我们先把它去安装起来对吧然后去拉取镜像这样去拉取然后把这个命令我们拷贝出来来看一下拷贝出来那么要注意的是拷贝出来之后它的格式会有一点问题把这个格式我们去调整一下
[00:58] 然后到这去调一下那么要注意的是在这个位置它扫了一个横杠扫了一个横杠那么没有这个横杠也是不对的好那么我们把它拷贝过来到这走那么可以看到我们这个容器就创建并且启动起来了那么这个是不是大家非常的熟悉这是什么其实这个是不是就是我们的这个Spring Boot的启动是吧OK
[01:28] 好嘞那么现在呢我们是不是就已经啊启动起来了那么启动起来之后呢他可能会有一些错误啊这个我们暂时不管他了那么我们来看一下那么我们通过什么呢通过这个172啊然后呢8082就做一个访问那么就可以访问到我们这个管理工具啊他可能这个数据啊稍微有点问题那么在这个位置呢其实我们可以看到他有一些呃功能对吧功能还是比较全的然后呢有什么集群呢有什么主题呢
[01:56] 相关的一些这个内容那么后面呢我们也会去根据这个UI工具然后去查看这边一些内容包括去查看它集群那些这个状态一些它的信息等等这个里面的内容还是非常的丰富非常的丰富OK好嘞那么然后呢可以看到主题消费者这个就都差不多了因为呢它是中文的对吧看起来是比较爽的
[02:24] 当然了你可以在这个位置做一个语言切换那么大家你们在访问的时候可能默认采用的是英语对吧English这个那么你可以把它切换成我们简体中文OK好这样做一个切换大家这样切换效果就是这样的一个效果了OK如果你比较喜欢看英文的话就可以切换成英文如果喜欢看中文的话就切换成中文就可以了OK这个就是咱们这个国人写这个软件的一个优势对吧有这个中文版好嘞
[02:53] 好那么这个就是它的一个UI工具的一个使用吧那么到这里呢我们就把这个UI工具是不是就搭起来了那么里面的一些内容呢就不做一个详细的一个讲解了因为它本身就中文的啊大家呢就一些功能就一目了然了OK好嘞那么到这里呢我们这个工具UI工具呢就搭建完成了也希望大家呢动手去搭建一下然后呢去把它去搭建起来看一下它里面的一些功能啊去做一些这个研究
[03:20] OK好那么这个UI工具的搭建我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何部署和使用 RocketMQ 的管理控制台（RocketMQ-console-ng），包括通过 Docker 和非 Docker 方式部署，并演示了控制台的界面功能。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 GitHub 上 RocketMQ-console 的部署说明，包含 Docker 和非 Docker 两种部署方式的命令。Docker 方式命令为：Docker pull styletang/RocketMQ-console-ng，run it (change namesAddr and port yourself)，Docker run -e JAVA_OPTS=-Drocketmq.namesrv.addr=172.16.55.185:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -p 8080 ...。非 Docker 方式命令为：require java 1.7，mvn Spring Boot:run，或 mvn clean package -Dmaven.test.skip=true，java -jar target/RocketMQ-console-ng-1.0.0.jar。Tips 提示：if you download package slow, you can change maven's mirror (maven/settings.xml)，并展示了 <mirrors>...</mirrors> 配置片段。
画面 2: 展示了 PPT 页面，标题为“1.4.4. 部署RocketMQ的管理工具”，内容说明 RocketMQ 提供了 UI 管理工具名为 RocketMQ-console，项目地址为 https://github.com/apache/RocketMQ-externals/tree/master/RocketMQ-console，该工具支持 Docker 以及非 Docker 安装，这里选择使用 Docker 安装。
画面 3: 展示了远程终端的启动日志，显示了 logback 配置初始化和 RocketMQ 控制台启动过程。
画面 4: 展示了 Spring Boot 应用启动日志，显示了 Tomcat 启动、初始化 WebApplicationContext 等信息。
画面 5: 展示了 Spring Boot 应用启动时的异常堆栈信息，显示了 org.apache.catalina.core.ApplicationFilterChain 等类的调用链。
画面 6: 展示了浏览器空白页面，可能是页面加载或切换过程。
画面 7: 展示了 RocketMQ 控制台的首页，包含“Broker TOP 10”和“Broker 5min trend”等图表，但提示“This date haven't data!”。
画面 8: 展示了 RocketMQ 控制台的“集群”页面，左侧有多个操作按钮。
画面 9: 展示了 RocketMQ 控制台的“Broker”配置详情页面，显示了 broker_haoke_im 的配置项，如 flushCommitLogLeastPages: 4，expectConsumerNumUseFilter: 32，messageDelayLevel: 1s 5s 10s 30s 1m 2m 3m 4m 5m 6m 7m 8m 9m 10m 20m 30m 1h 2h 等。
画面 10: 展示了 RocketMQ 控制台的“主题”页面，列出了多个主题如 BenchmarkTest、DefaultCluster 等，每个主题下方有“状态”、“路由”、“CONSUMER 管理”、“TOPIC 配置”、“发送消息”、“查看消费点”、“删除”等操作按钮。
画面 11: 展示了 RocketMQ 控制台的“消费者”页面，列出了多个消费者组如 SELF_TEST_C_GROUP、TOOLS_CONSUMER 等，每个消费者组下方有“CLIENT”、“CONSUME DETAIL”、“CONFIG”、“DELETE”等按钮。
画面 12: 展示了 PPT 页面，内容为“通过浏览器进行访问：http://172.16.55.185:8082/#/”，并提示“切换语言到中文，所有的功能就一目了然了。”，下方展示了 RocketMQ 控制台的界面截图。
画面 13: 展示了 PPT 页面，内容与画面 12 相同，但鼠标光标在“工具”菜单上。
画面 14: 展示了 PPT 页面，内容与画面 2 相同，再次强调了 RocketMQ 管理工具的部署方式和项目地址。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
Docker pull styletang/RocketMQ-console-ng
run it (change namesAddr and port yourself)
Docker run -e JAVA_OPTS=-Drocketmq.namesrv.addr=172.16.55.185:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -p 8080 ...
require java 1.7
mvn Spring Boot:run
or
mvn clean package -Dmaven.test.skip=true
java -jar target/RocketMQ-console-ng-1.0.0.jar
Tips:
if you download package slow, you can change maven's mirror (maven/settings.xml)
<mirrors>
<mirror>
画面 2:
#拉取镜像
Docker pull styletang/RocketMQ-console-ng:1.0.0
#创建并启动容器
Docker run -e JAVA_OPTS=-Drocketmq.namesrv.addr=172.16.55.185:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -p 8080:8080 -t styletang/RocketMQ-console-ng:1.0.0
画面 12:
通过浏览器进行访问：http://172.16.55.185:8082/#/
切换语言到中文，所有的功能就一目了然了。

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 2: 标题“1.4.4. 部署RocketMQ的管理工具”，内容说明 RocketMQ 提供了 UI 管理工具名为 RocketMQ-console，项目地址为 https://github.com/apache/RocketMQ-externals/tree/master/RocketMQ-console，该工具支持 Docker 以及非 Docker 安装，这里选择使用 Docker 安装。
画面 12: 标题“通过浏览器进行访问：http://172.16.55.185:8082/#/”，提示“切换语言到中文，所有的功能就一目了然了。”，下方展示了 RocketMQ 控制台的界面截图。
画面 14: 标题与画面 2 相同，内容与画面 2 相同。

5) 无。

