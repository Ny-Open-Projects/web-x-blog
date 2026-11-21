# 画面线理解：3-Azkaban-solo模式-安装

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\3-Azkaban-solo模式-安装【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:20, 00:30, 00:52, 01:29, 02:04, 02:25, 02:55, 03:32, 03:43, 04:17, 04:29, 04:48, 05:00, 05:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 10:33:53

1) 这一组画面整体在讲什么（一句话）：
演示如何在单节点模式下安装和配置 Azkaban 服务，并启动其 Web 界面。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 显示了 Typora 文档，标题为“2.2. Azkaban 单服务模式安装与使用”。
- 文档内容说明了 Azkaban 单服务模式只需一个安装包，数据存于 H2 数据库。
- 展示了第一步“解压”的命令：
  cd /export/software
  tar -zxvf azkaban-solo-server-0.1.0-SNAPSHOT.tar.gz -C ../servers/

画面2：
- 与画面1内容相同，仅时间戳不同（08:22:11），为同一操作的延续。

画面3：
- 显示了 SecureCRT 会话，用户在 node03 节点上查看 azkaban-db 目录下的 SQL 文件列表。
- 用户执行了 cd .. 命令并进入 install 目录。

画面4：
- 用户在 azkaban-solo-server 目录下执行了 cd build 命令。
- 用户执行了 cd ../distributions/ 命令，进入 distributions 目录。
- 用户执行了 cp azkaban-solo-server-0.1.0-SNAPSHOT.tar.gz /export/software/ 命令，将安装包复制到 /export/software/ 目录。

画面5：
- 用户在 /export/servers/ 目录下执行了 ls 命令，查看了 azkaban-solo-server-0.1.0-SNAPSHOT 目录的内容。
- 用户执行了 cd azkaban-solo-server-0.1.0-SNAPSHOT/ 命令，进入该目录。

画面6：
- 用户在 azkaban-solo-server-0.1.0-SNAPSHOT/ 目录下执行了 ls 命令，查看了目录内容。
- 用户执行了 cd azkaban-solo-server-0.1.0-SNAPSHOT/ 命令，进入该目录。

画面7：
- 显示了 Typora 文档，标题为“Step 2: 修改时区配置文件”。
- 文档内容显示了修改 azkaban.properties 文件的命令：
  cd /export/servers/azkaban-solo-server-0.1.0-SNAPSHOT/conf
  vim azkaban.properties
- 展示了修改后的配置项：
  default.timezone.id=Asia/Shanghai

画面8：
- 显示了 azkaban.properties 文件内容，其中包含配置项：
  default.timezone.id=Asia/Shanghai
  # Azkaban UserManager class
  user.manager.class=azkaban.user.XmlUserManager
  user.manager.xml.file=conf/azkaban-users.xml
  # Loader for projects
  executor.global.properties=conf/global.properties
  azkaban.project.dir=projects
  database.type=h2
  h2.path= /h2
  h2.create.tables=true
  # Velocity dev mode
  velocity.dev.mode=false
- 用户执行了 cd 命令，进入 plugins/jobtypes 目录。

画面9：
- 显示了 Typora 文档，标题为“修改 commonprivate.properties 配置文件”。
- 文档内容显示了修改 commonprivate.properties 文件的命令：
  cd /export/servers/azkaban-solo-server-0.1.0-SNAPSHOT/plugins/jobtypes
  vim commonprivate.properties
- 展示了修改后的配置项：
  execute.as.user=false

画面10：
- 用户在 azkaban-solo-server-0.1.0-SNAPSHOT/ 目录下执行了 ls 命令，查看了目录内容。
- 用户执行了 cd bin/ 命令，进入 bin 目录。

画面11：
- 用户在 bin 目录下执行了 ./start-solo.sh 命令，启动 Azkaban 服务。

画面12：
- 显示了浏览器地址栏输入 node03:50070。
- 页面显示了 NameNode 信息。

画面13：
- 显示了浏览器地址栏输入 node03:11000。
- 页面显示了 Google 搜索结果，包含 Azkaban Web Client 等链接。

画面14：
- 显示了 Azkaban Web Client 界面，标题为“Executing”。
- 页面显示了执行中的流程列表，包含 Execution Id、Executor Id、Flow、Project、User、Proxy、Start Time、End Time、Elapsed、Status、Action 等列。
