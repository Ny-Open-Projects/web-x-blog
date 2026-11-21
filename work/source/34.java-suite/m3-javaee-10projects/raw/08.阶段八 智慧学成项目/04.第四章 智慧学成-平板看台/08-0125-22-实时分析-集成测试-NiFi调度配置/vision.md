# 画面线理解：22-实时分析-集成测试-NiFi调度配置

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\22-实时分析-集成测试-NiFi调度配置_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:40, 01:39, 01:55, 02:28, 02:52, 03:24, 03:47, 04:00, 04:25, 04:47, 05:26, 05:53, 07:43, 08:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:51:54

1) 这一组画面整体在讲如何通过 Nifi 平台部署并运行统计分析的实时数据处理流程，并配合本地代码打包和脚本上传。

2) 按时间顺序列出每张画面的要点：
画面1：在 IDEA 中打开项目结构，展示 `application.properties` 文件，目录结构中可见 `xc-service-rt` 模块，右侧 Maven 生命周期显示 `package` 阶段。
画面2：展示 PPT 页面，标题为“5.2.2 统计分析 NIFI 调度”，内容说明需将 `xc-service-rt-jar-with-dependencies.jar` 文件上传至 `xc-online-nifi` 容器的 `/opt/run/jars` 目录，并将 `.sh` 脚本上传至 `/opt/run/script` 目录。
画面3：与画面2内容相同，为同一 PPT 页面。
画面4：在 Windows 资源管理器中，显示 `shell` 文件夹内包含三个 Shell 脚本：`real_time_buy.sh`、`real_time_new_user.sh`、`real_time_visit.sh`。
画面5：在 Nifi Web 界面中，弹出“Success”提示框，内容为“Template successfully imported.”，表示模板已成功导入。
画面6：在 Nifi Web 界面中，显示“数据采集-新增用户-Mysql-ToKafka-实时采集”组件，状态为初始状态。
画面7：在 Nifi Web 界面中，弹出“Upload Template”对话框，提示选择模板文件“新增用户-实时统计分析.xml”。
画面8：在 Nifi Web 界面中，空白画布，准备新建流程。
画面9：在 Nifi Web 界面中，已放置三个组件：“数据采集-新增用户-Mysql-ToKafka-实时采集”、“数据采集-新增用户-Mysql-ToKafka-实时采集”、“新增用户-实时统计分析”。
画面10：在 Nifi Web 界面中，三个组件已放置，其中“新增用户-实时统计分析”组件被选中。
画面11：在 IDEA 中，右键点击 `xc-service-rt` 模块，弹出“Build”菜单，执行 `package` 命令，终端显示构建成功信息。
画面12：在 IDEA 中，打开终端，执行 `cp` 命令将 `xc-service-rt-jar-with-dependencies.jar` 文件复制到远程服务器的 `/opt/run/jars` 目录。
画面13：在远程服务器终端中，执行 `ls` 命令，列出 `/opt/run/script` 目录下的脚本文件。
画面14：与画面2内容相同，为同一 PPT 页面。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1：无代码或配置。
画面2：无代码或配置。
画面3：无代码或配置。
画面4：无代码或配置。
画面5：无代码或配置。
画面6：无代码或配置。
画面7：无代码或配置。
画面8：无代码或配置。
画面9：无代码或配置。
画面10：无代码或配置。
画面11：无代码或配置。
画面12：无代码或配置。
画面13：无代码或配置。
画面14：无代码或配置。

4) PPT 标题、架构图/流程图的结构、表格数据：
画面2、3、14：PPT 标题为“5.2.2 统计分析 NIFI 调度”，内容说明需将 `xc-service-rt-jar-with-dependencies.jar` 文件上传至 `xc-online-nifi` 容器的 `/opt/run/jars` 目录，并将 `.sh` 脚本上传至 `/opt/run/script` 目录。
画面7：弹出“Upload Template”对话框，提示选择模板文件“新增用户-实时统计分析.xml”。
画面9：在 Nifi Web 界面中，已放置三个组件：“数据采集-新增用户-Mysql-ToKafka-实时采集”、“数据采集-新增用户-Mysql-ToKafka-实时采集”、“新增用户-实时统计分析”。
画面10：在 Nifi Web 界面中，三个组件已放置，其中“新增用户-实时统计分析”组件被选中。

5) 不要评价画面美观，不要输出与课程无关的内容。
