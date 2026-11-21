# 画面线理解：5.Gogs的安装和使用

- 阶段：10.阶段十 万信金融项目
- 章节：07_万信金融-项目实战/7-5 项目部署实战
- 源文件：10.阶段十 万信金融项目\07_万信金融-项目实战\7-5 项目部署实战\5.Gogs的安装和使用_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:16, 01:26, 03:34, 04:08, 04:52, 05:42, 06:14, 07:11, 07:31, 08:04, 08:31, 09:01, 09:20, 09:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:01:00

1) 这一组画面整体在讲如何使用 Gogs 作为私有 Git 仓库，并在 IDEA 中配置 Git 管理项目，最终将代码提交到 Gogs 仓库。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PPT 标题“3.1.3 P2P项目持续集成流程”，并配有流程图：上传代码 → git → 拉取代码 → CI Server (Maven) → 构建项目 → 镜像 → 容器 → 测试 → Docker。
画面2：浏览器打开 Gitee 网站，显示其宣传语和功能。
画面3：展示 Gogs 安装文档，其中包含 docker-compose.yml 文件内容：
gogs:
  image: docker.io/gogs/gogs:latest
  links:
    - mysql-gogs:mysql
  ports:
    - "10022:22"
    - "10080:3000"
  volumes:
    - "./data/data/gogs"
    - "./repo/data/gogs-repositories"
  restart: always
画面4：展示 docker-compose.yml 文件的后续内容，包括 environment 和 command 配置，以及启动命令：
2. 启动Gogs: docker-compose up
3. 浏览器访问：[http://127.0.0.1:10080](http://127.0.0.1:10080)
4. 初次访问需要等待一段时间，然后进行基本配置，填写数据库用户名和密码：gogs/gogs
画面5：展示 Gogs 注册页面，用户填写信息并点击“注册账户”。
画面6：展示 Gogs 新建仓库页面，标题为“二. 新建仓库”，并列出“1. 登录后，即可新建仓库”。
画面7：展示 Gogs 创建新仓库的表单，仓库名称为“ozp”，并提示“仓库名称应独一无二”。
画面8：展示 IDEA 设置 Git 的界面，配置了“Path to Git executable”为“C:\Program Files\Git\bin\git.exe”。
画面9：展示 IDEA 的“Version Control”设置界面，其中“Show directories with changed descendants”选项被勾选。
画面10：展示 IDEA 项目结构，显示了多个服务模块，如“wanning2p-account-service”等。
画面11：展示 IDEA 的 VCS 菜单，其中“Show Local Changes as VCS”选项被选中。
画面12：展示桌面，显示了多个软件图标，包括“黑马程序员”和“博学谷”的标志。
画面13：展示 IDEA 的“Commit File”对话框，其中“Commit File”选项被选中。
画面14：展示 IDEA 的“Commit File”对话框，其中“Commit File”选项被选中。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
gogs:
  image: docker.io/gogs/gogs:latest
  links:
    - mysql-gogs:mysql
  ports:
    - "10022:22"
    - "10080:3000"
  volumes:
    - "./data/data/gogs"
    - "./repo/data/gogs-repositories"
  restart: always

画面4：
2. 启动Gogs: docker-compose up
3. 浏览器访问：[http://127.0.0.1:10080](http://127.0.0.1:10080)
4. 初次访问需要等待一段时间，然后进行基本配置，填写数据库用户名和密码：gogs/gogs

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题“3.1.3 P2P项目持续集成流程”，流程图结构为：上传代码 → git → 拉取代码 → CI Server (Maven) → 构建项目 → 镜像 → 容器 → 测试 → Docker。
画面7：Gogs 创建新仓库表单，包含“拥有者”、“仓库名称”、“可见性”、“仓库描述”、“.gitignore”、“授权许可”、“自述文件”等字段。

5) 不要评价画面美观，不要输出与课程无关的内容。
