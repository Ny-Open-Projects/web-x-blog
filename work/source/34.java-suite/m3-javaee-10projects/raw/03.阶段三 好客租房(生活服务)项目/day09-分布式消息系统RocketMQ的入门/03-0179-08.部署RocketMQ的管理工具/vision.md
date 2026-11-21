# 画面线理解：08.部署RocketMQ的管理工具

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\08.部署RocketMQ的管理工具【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:28, 00:41, 01:13, 01:21, 01:30, 01:38, 01:44, 02:02, 02:12, 02:20, 02:41, 03:01, 03:10, 03:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:59:15

1) 这一组画面整体在讲如何部署和使用 RocketMQ 的管理控制台（rocketmq-console-ng），包括通过 Docker 和非 Docker 方式部署，并演示了控制台的界面功能。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 GitHub 上 rocketmq-console 的部署说明，包含 Docker 和非 Docker 两种部署方式的命令。Docker 方式命令为：docker pull styletang/rocketmq-console-ng，run it (change namesAddr and port yourself)，docker run -e JAVA_OPTS=-Drocketmq.namesrv.addr=172.16.55.185:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -p 8080 ...。非 Docker 方式命令为：require java 1.7，mvn spring boot:run，或 mvn clean package -Dmaven.test.skip=true，java -jar target/rocketmq-console-ng-1.0.0.jar。Tips 提示：if you download package slow, you can change maven's mirror (maven/settings.xml)，并展示了 <mirrors>...</mirrors> 配置片段。
画面 2: 展示了 PPT 页面，标题为“1.4.4. 部署RocketMQ的管理工具”，内容说明 RocketMQ 提供了 UI 管理工具名为 rocketmq-console，项目地址为 https://github.com/apache/rocketmq-externals/tree/master/rocketmq-console，该工具支持 docker 以及非 docker 安装，这里选择使用 docker 安装。
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
docker pull styletang/rocketmq-console-ng
run it (change namesAddr and port yourself)
docker run -e JAVA_OPTS=-Drocketmq.namesrv.addr=172.16.55.185:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -p 8080 ...
require java 1.7
mvn spring boot:run
or
mvn clean package -Dmaven.test.skip=true
java -jar target/rocketmq-console-ng-1.0.0.jar
Tips:
if you download package slow, you can change maven's mirror (maven/settings.xml)
<mirrors>
<mirror>
画面 2:
#拉取镜像
docker pull styletang/rocketmq-console-ng:1.0.0
#创建并启动容器
docker run -e JAVA_OPTS=-Drocketmq.namesrv.addr=172.16.55.185:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -p 8080:8080 -t styletang/rocketmq-console-ng:1.0.0
画面 12:
通过浏览器进行访问：http://172.16.55.185:8082/#/
切换语言到中文，所有的功能就一目了然了。

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 2: 标题“1.4.4. 部署RocketMQ的管理工具”，内容说明 RocketMQ 提供了 UI 管理工具名为 rocketmq-console，项目地址为 https://github.com/apache/rocketmq-externals/tree/master/rocketmq-console，该工具支持 docker 以及非 docker 安装，这里选择使用 docker 安装。
画面 12: 标题“通过浏览器进行访问：http://172.16.55.185:8082/#/”，提示“切换语言到中文，所有的功能就一目了然了。”，下方展示了 RocketMQ 控制台的界面截图。
画面 14: 标题与画面 2 相同，内容与画面 2 相同。

5) 无。
