# 画面线理解：7.Jenkins构建任务测试

- 阶段：10.阶段十 万信金融项目
- 章节：07_万信金融-项目实战/7-5 项目部署实战
- 源文件：10.阶段十 万信金融项目\07_万信金融-项目实战\7-5 项目部署实战\7.Jenkins构建任务测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:41, 02:06, 03:32, 04:21, 05:03, 05:51, 06:30, 07:06, 09:37, 10:02, 10:28, 11:42, 12:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:02:19

1) 这一组画面整体在讲什么（一句话）：
演示如何在Jenkins中配置并执行一个基于Git和Docker Compose的持续集成构建任务，涉及Gogs代码仓库、构建脚本和部署流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PDF文档目录，当前页为“3.3.1 创建构建任务”，内容是关于Jenkins的介绍。
画面2：PDF文档内容，标题为“3.2 搭建持续集成环境”，子章节“3.2.1 安装Git/Gogs”，介绍Gogs作为Git仓库的优势。
画面3：PDF文档空白页，底部有“北京市昌平区建材城西路金燕龙办公楼一层 电话：400-618-9090”。
画面4：Jenkins界面，配置“源码管理”为Git，Repository URL为“http://172.16.0.203:10000/zhangdengkai/p2p.git”，Credentials为“zhupcyuan@zcast.cn”。
画面5：PDF文档内容，与画面2相同，再次强调Gogs的优势。
画面6：PDF文档内容，展示“Post Steps”配置，Execute shell命令为“sh /home/p2p/scripts/deployP2P.sh”。
画面7：PDF文档内容，展示部署脚本的头部，包含“#时间date -date +%Y%m%d%H%M%S”和“#version app_version="1.0-SNAPSHOT"”。
画面8：多窗口界面，展示Jenkins、Gogs、Docker等工具的运行状态，以及脚本执行过程。
画面9：Jenkins界面，显示“3.3.4 执行构建任务”，并提示“1、进入任务页面，点击‘立即构建’”。
画面10：Jenkins界面，显示“Build Now”按钮，提示“2、开始构建，查看控制台日志输出”。
画面11：Jenkins控制台日志，显示构建成功，包含多个服务的构建信息，如“wanxingp2p-account-service”等。
画面12：Jenkins控制台日志，显示Git操作和Maven构建过程，包含“git clone”和“Executing Maven”等命令。
画面13：Jenkins界面，显示“Build Now”按钮，提示“2、开始构建，查看控制台日志输出”。
画面14：Jenkins任务列表页面，显示多个任务的状态，如“farming”、“li jibo”、“MyP2P”等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4：
Repository URL: http://172.16.0.203:10000/zhangdengkai/p2p.git
Credentials: zhupcyuan@zcast.cn

画面6：
Execute shell
Command: sh /home/p2p/scripts/deployP2P.sh

画面7：
#!/bin/sh
#时间date -date +%Y%m%d%H%M%S
#version
app_version="1.0-SNAPSHOT"
#all service
service1="wanxingp2p-account-service"
service2="wanxingp2p-consumer-service"
service3="wanxingp2p-depository-agent-service"
service4="wanxingp2p-discover-server"
service5="wanxingp2p-gateway-server"
service6="wanxingp2p-repayment-service"
service7="wanxingp2p-transaction-service"
service8="wanxingp2p-uaa-service"

画面11：
[INFO] Building jar: /var/lib/jenkins/workspace/p2p/wanxingp2p-reconciliation-service/target/wanxingp2p-reconciliation-service-1.0-SNAPSHOT.jar
[INFO] Replacing jar artifact with repackaged archive
[INFO] Building jar: /var/lib/jenkins/workspace/p2p/wanxingp2p-reconciliation-service/target/wanxingp2p-reconciliation-service-1.0-SNAPSHOT.jar
[INFO] Total time: 61 54 min
[INFO] Finished at: 2019-12-11T06:54:00

画面12：
git clone -b master http://172.16.0.203:10000/zhangdengkai/p2p.git
git checkout -b develop
git add .
git commit -m "commit"
git push origin develop
git tag -a v1.0.0 -m "v1.0.0"
git push origin v1.0.0
git clone -b master http://172.16.0.203:10000/zhangdengkai/p2p.git
git checkout -b develop
git add .
git commit -m "commit"
git push origin develop
git tag -a v1.0.0 -m "v1.0.0"
git push origin v1.0.0

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：PPT标题为“3.2 搭建持续集成环境”，子标题“3.2.1 安装Git/Gogs”，内容为Git和Gogs的介绍。
画面9：PPT标题为“3.3.4 执行构建任务”，内容为“1、进入任务页面，点击‘立即构建’”。
画面10：PPT标题为“2、开始构建，查看控制台日志输出”。
画面14：PPT标题为“Jenkins任务列表”，表格数据包括任务名称、上次成功、上次失败、上次构建时间等。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
