# 画面线理解：11.任务的创建与执行

- 阶段：01.阶段一 微服务相关技术
- 章节：5.持续集成与容器管理
- 源文件：01.阶段一 微服务相关技术\5.持续集成与容器管理\11.任务的创建与执行_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:35, 01:06, 01:32, 01:44, 02:10, 02:37, 03:38, 05:06, 05:12, 05:25, 05:44, 06:10, 06:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:21:04

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Jenkins 中创建并执行一个 Maven 项目构建任务，包括配置源码管理、构建步骤和 Docker 镜像推送。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在 Git 仓库中浏览 tensquare 项目结构，显示了多个子模块如 tensquare_article、tensquare_base 等。
画面2：在 Jenkins 首页选择“新建一个自由风格的软件项目”。
画面3：配置 Jenkins 任务的“项目名称”为“tensquare”，并设置“描述”字段。
画面4：在“源码管理”部分配置 Git 仓库，分支指定为“master”。
画面5：在“构建触发器”中勾选“Build whenever a SNAPSHOT dependency is built”。
画面6：在“构建”部分选择“Maven 项目”，并设置“Root POM”为“pom.xml”。
画面7：在“构建”部分设置“Root POM”为“tensquare_base/pom.xml”，并配置“Goals and options”为“clean package docker:build -DpushImage”。
画面8：在 Jenkins 任务列表中显示“tensquare”任务，状态为“没有”上次成功。
画面9：在 Jenkins 任务控制台输出中显示构建过程，包括 Maven 依赖解析、编译和打包。
画面10：继续显示构建过程，包括资源复制、测试编译和 JAR 包构建。
画面11：显示 Docker 镜像构建和推送日志，包括镜像层构建和推送成功。
画面12：再次显示构建过程，包括 Maven 依赖解析和编译。
画面13：在终端中执行 Docker 命令，拉取 gogs 镜像并运行容器。
画面14：在 Markdown 文档中显示 Jenkins 构建配置，包括“命令”为“clean package docker:build -DpushImage”，并提示“最后点击‘保存’按钮”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4：
Branch Specifier (blank for any): master

画面6：
Enter an item name
tensquare_eureka

画面7：
Root POM: tensquare_base/pom.xml
Goals and options: clean package docker:build -DpushImage

画面13：
docker run -d --name gogs -p 10022:22 -p 3000:3000 -v /var/gogsdata:/data gogs/gogs

画面14：
命令：
clean package docker:build -DpushImage

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面6：
标题：2.7 任务的创建与执行
子标题：(1) 回到首页，点击新建任务，如下图，输入名称，选择创建一个 Maven 项目，点击 OK
子标题：(2) 源码管理，选择 Git

画面14：
标题：2.7 任务的创建与执行
子标题：(3) Build
子标题：(4) 执行任务
标题：3 容器管理工具 Rancher
子标题：3.1 什么是 Rancher

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
