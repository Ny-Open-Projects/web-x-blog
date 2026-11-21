# 画面线理解：03系统集成测试-代码重新打包-上传NiFi容器

- 阶段：08.阶段八 智慧学成项目
- 章节：06.第六章 智慧学成-系统集成测试
- 源文件：08.阶段八 智慧学成项目\06.第六章 智慧学成-系统集成测试\03系统集成测试-代码重新打包-上传NiFi容器_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:29, 00:48, 00:58, 01:15, 01:30, 01:49, 03:04, 03:28, 04:04, 05:59, 06:16, 06:35, 07:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 00:10:17

1) 这一组画面整体在讲如何通过 Maven 打包 Java 项目并部署到 Nifi 平台进行数据处理和分析。

2) 按时间顺序列出每张画面的要点：
画面1：展示 IntelliJ IDEA 中的 Maven 项目结构，执行了 package 阶段，构建成功，输出了各模块的编译时间。
画面2：展示 PPT 页面，说明 Nifi 已配置好，打包好的程序可直接在 Maven 中的“package”阶段打包，同时展示 Nifi 的调度策略配置界面，标注了“Timer driven”和“Run Schedule: 9000 sec”。
画面3：与画面1相同，展示 Maven 构建成功后的日志。
画面4：展示文件资源管理器，定位到项目目录下的 target 文件夹，显示了生成的 jar 文件。
画面5：展示文件资源管理器，定位到 xc-service-offline 模块的 target 文件夹，显示了 pom.xml 文件。
画面6：展示 Xshell 远程连接界面，已连接到 xc-online-s 服务器。
画面7：在 Xshell 中登录后，执行了命令“sudo apt install -y clear”，但提示“command 'clear' not found”，并尝试使用“sudo apt install -y clear”。
画面8：在 Xshell 中执行了命令“docker exec -it xc-online-nifi bash”，进入 Nifi 容器的 shell。
画面9：在浏览器中访问 Nifi 的 Web 界面，显示了 Nifi 的启动页面。
画面10：在 Nifi 的流程图界面，展示了三个处理器节点：“GenerateFlowFile”、“InstantQueryStep11”和“InstantQueryStep2ToHBaseAndES”，并标注了“Name output stream”。
画面11：在 Nifi 的流程图界面，展示了两个处理器节点：“数据生产-用户学习(在线学习)ToHDFS”和“数据清洗统计-用户学习”，并标注了“Queued”和“Read/Write”状态。
画面12：在 Nifi 的“Configure Processor”界面，配置了处理器的“Required field”，输入了路径“/user/hive/external/data_source/learning_source_online_source/”。
画面13：展示 PPT 页面，说明 Nifi 已配置好，打包好的程序可直接在 Maven 中的“package”阶段打包，同时展示 Nifi 的调度策略配置界面，标注了“Timer driven”和“Run Schedule: 9000 sec”，并说明“这里选择的调度策略为”。
画面14：展示 PPT 页面，说明 Nifi 已配置好，打包好的程序可直接在 Maven 中的“package”阶段打包，同时展示 Maven 的“package”阶段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
画面1：无直接代码或配置。
画面2：无直接代码或配置。
画面3：无直接代码或配置。
画面4：无直接代码或配置。
画面5：无直接代码或配置。
画面6：无直接代码或配置。
画面7：命令“sudo apt install -y clear”。
画面8：命令“docker exec -it xc-online-nifi bash”。
画面9：无直接代码或配置。
画面10：无直接代码或配置。
画面11：无直接代码或配置。
画面12：配置路径“/user/hive/external/data_source/learning_source_online_source/”。
画面13：无直接代码或配置。
画面14：无直接代码或配置。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2：PPT 标题为“6.2 NiFi采集-清洗-统计分析”，内容说明“Nifi已配置好，无需配置，这里只需知道是在那里配置即可”，并展示 Nifi 的调度策略配置界面，标注了“Timer driven”和“Run Schedule: 9000 sec”，并说明“这里选择的调度策略为”。
画面10：Nifi 流程图，节点“GenerateFlowFile”指向“InstantQueryStep11”，节点“InstantQueryStep11”指向“InstantQueryStep2ToHBaseAndES”，并标注了“Name output stream”。
画面11：Nifi 流程图，节点“数据生产-用户学习(在线学习)ToHDFS”和“数据清洗统计-用户学习”并列，无直接连接。
画面12：Nifi 配置界面，配置了“Required field”，输入了路径“/user/hive/external/data_source/learning_source_online_source/”。
画面13：PPT 标题为“6.2 NiFi采集-清洗-统计分析”，内容说明“Nifi已配置好，无需配置，这里只需知道是在那里配置即可”，并展示 Nifi 的调度策略配置界面，标注了“Timer driven”和“Run Schedule: 9000 sec”，并说明“这里选择的调度策略为”。
画面14：PPT 标题为“6.2 NiFi采集-清洗-统计分析”，内容说明“Nifi已配置好，无需配置，这里只需知道是在那里配置即可”，并展示 Maven 的“package”阶段。

5) 不要评价画面美观，不要输出与课程无关的内容。
