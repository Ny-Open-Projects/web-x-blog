# 画面线理解：04-课程分析-课程购买量-NiFi采集MySQL配置

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\04-课程分析-课程购买量-NiFi采集MySQL配置_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:21, 00:29, 01:04, 01:12, 01:16, 01:31, 01:41, 02:01, 02:24, 02:27, 02:51, 03:02, 03:07
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:01:00

1) 这一组画面整体在讲如何在 NiFi 中创建并配置一个用于实时采集 MySQL binlog 数据并写入 Hive 的数据流。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了课程文档中关于 NiFi MySQL binlog 处理流程的说明，包含流程图和 XML 路径。
画面2: 与画面1内容相同，为同一文档页面。
画面3: 与画面1、2内容相同，为同一文档页面。
画面4: 在 NiFi 界面中弹出“Upload Template”对话框，用于上传模板。
画面5: NiFi 界面空白画布，准备创建新流程。
画面6: 弹出“Add Template”对话框，选择“课程购买量-Mysql实时采集”模板。
画面7: 显示“1. 数据采集: 课程购买量-Mysql-To-Hive Configuration”配置页面的 GENERAL 标签页，设置 Process Group Name 和 Comments。
画面8: 在 CONTROLLER SERVICES 标签页，显示已配置的服务列表，包括 DistributedMapCacheClientService、DistributedMapCacheServer 和 HiveConnectionPool。
画面9: 在 CONTROLLER SERVICES 标签页，鼠标悬停在 DistributedMapCacheClientService 上，选中并高亮显示。
画面10: 在 NiFi 界面中，点击菜单栏的“+”按钮，弹出“1. 数据采集: 课程购买量-Mysql-To-Hive”流程组的属性面板。
画面11: 显示 NiFi 流程图，包含 CaptureChangeMySQL、RouteOnAttribute、MySQLBinLogToHiveProcessor 和 PutHiveQL 四个处理器，按顺序连接。
画面12: 与画面11内容相同，为同一流程图。
画面13: 与画面1、2、3内容相同，为同一文档页面。
画面14: 与画面13内容相同，为同一文档页面。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
画面1、2、3、13、14 中的 XML 路径：
xml路径：
  搜索资料
    第3章-课程分析
      nifi/课程购买量/课程购买量-Mysql实时采集.xml

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1、2、3、13、14 中的 PPT 标题：
2.3.3.1.2 NiFi 调度流程
NiFi监控MySQL binlog处理通用流程如下：CaptureChangeMySQL → RouteOnAttribute → MySQLBinLogToHiveProcessor → PutHiveQL
NiFi通用流程图，如下图所示：

流程图结构：
CaptureChangeMySQL → RouteOnAttribute → MySQLBinLogToHiveProcessor → PutHiveQL

画面7 中的表格数据：
Process Group Name: 1.数据采集: 课程购买量-Mysql-To-Hive
Process Group Comments: MySQL实时采集数据，监控insert, update

画面8 中的表格数据：
Name | Type | Bundle | State | Scope
DistributedMapCacheClientService | DistributedMapCacheClientService 1.0 | org.apache.nifi-nifi-distributed-cache | Enabled | 1.数据采集: 课程购买量-Mysql-To-Hive
DistributedMapCacheServer | DistributedMapCacheServer 1.9.2 | org.apache.nifi-nifi-distributed-cache | Enabled | NiFi Flow
HiveConnectionPool | HiveConnectionPool 1.9.2 | org.apache.nifi-nifi-hive-nar | Disabled | 1.数据采集: 课程购买量-Mysql-To-Hive

画面11 中的流程图结构：
CaptureChangeMySQL → RouteOnAttribute → MySQLBinLogToHiveProcessor → PutHiveQL

5) 无
