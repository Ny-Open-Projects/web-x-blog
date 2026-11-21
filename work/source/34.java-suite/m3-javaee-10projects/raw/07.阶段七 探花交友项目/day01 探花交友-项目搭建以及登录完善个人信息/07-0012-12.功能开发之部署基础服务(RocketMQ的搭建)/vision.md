# 画面线理解：12.功能开发之部署基础服务（RocketMQ的搭建）

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\12.功能开发之部署基础服务（RocketMQ的搭建）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:31, 00:38, 01:02, 01:27, 01:44, 02:16, 02:24, 02:52, 03:18, 03:23, 03:39, 03:44, 04:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:05:59

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
docker pull foxiswho/rocketmq:server-4.3.2
docker pull foxiswho/rocketmq:broker-4.3.2

#创建nameserver容器
docker create -p 9876:9876 --name rmqserver \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v rmqserver-logs:/opt/logs \
-v rmqserver-store:/opt/store \
foxiswho/rocketmq:server-4.3.2

#创建broker.conf文件
vim /itcast/rmq/rmqbroker/conf/broker.conf
brokerIP1=192.168.31.81
namesrvAddr=192.168.31.81:9876
brokerName=broker_tanhua
```

画面4：
```markdown
#创建broker容器
docker create -p 10911:10911 -p 10909:10909 --name rmqbroker \
-e "JAVA_OPTS=-Duser.home=/opt" \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-v /itcast/rmq/rmqbroker/conf/broker.conf:/etc/rocketmq/broker.conf \
-v rmqbroker-logs:/opt/logs \
-v rmqbroker-store:/opt/store \
foxiswho/rocketmq:broker-4.3.2
```

画面7：
```markdown
#启动容器
docker start rmqserver rmqbroker

#停止删除容器
docker stop rmqbroker rmqserver
docker rm rmqbroker rmqserver

#拉取RocketMQ的管理工具
docker pull sty1atang/rocketmq-console-ng:1.0.0

#启动管理工具
docker run -e "JAVA_OPTS=-Drocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithIPChannel=false" -p 8080:8080 -t sty1atang/rocketmq-console-ng:1.0.0
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
