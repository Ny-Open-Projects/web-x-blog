# 画面线理解：04-热门学科排名-NiFi采集用户选课数据&测试

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\04-热门学科排名-NiFi采集用户选课数据&测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:59, 01:33, 01:49, 02:11, 02:27, 02:38, 03:09, 04:43, 05:13, 06:22, 06:51, 07:05, 07:39, 07:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:12:11

1) 这一组画面整体在讲什么（一句话）：
演示如何在 NiFi 中配置 MySQL binlog 实时采集流程，并通过 Python 脚本生成测试数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程 PPT 页面，标题为“3.3.3 数据采集实现”，内容说明使用 NiFi 监控 MySQL binlog 实时采集数据，并列出 NiFi 采集调用流程：CaptureChangeMySQL → MySQLBinLogToHiveProcessor → PutHiveQL。
画面2：在文件资源管理器中选择 NiFi 流程配置文件，准备上传。
画面3：NiFi 界面空白画布，准备新建流程。
画面4：NiFi 控制服务配置页面，显示已配置的控制器服务，包括 DistributedMapCacheClientService、DistributedMapCacheServer 和 HiveConnectionPool。
画面5：启用 HiveConnectionPool 控制器服务的弹窗，显示其被 PutHiveQL 处理器引用。
画面6：NiFi 流程图，显示 CaptureChangeMySQL → RouteOnAttribute → MySQLBinLogToHiveProcessor → PutHiveQL 的数据流向。
画面7：NiFi 流程图，显示数据处理状态，PutHiveQL 处理器的输入和输出数据量。
画面8：点击 MySQLBinLogToHiveProcessor 处理器后弹出的“Empty Queue”对话框，询问是否清空队列。
画面9：清空队列后弹出的确认对话框，显示“20,037 FlowFiles (62.10 MB) were removed from the queue”。
画面10：回到课程 PPT 页面，标题为“3.3.3.2 流程代码”，显示 nifi 流程 xml 代码路径和目录结构。
画面11：浏览器新标签页，准备访问 NiFi。
画面12：NiFi 流程图，显示数据处理状态，PutHiveQL 处理器的输入和输出数据量。
画面13：课程 PPT 页面，标题为“3.3.4 NiFi 生产数据”，内容说明 NiFi 调用 Python 脚本生成测试数据。
画面14：课程 PPT 页面，标题为“3.3.4 NiFi 生产数据”，内容说明 NiFi 调用 Python 脚本生成测试数据，并列出生成数据逻辑。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
NiFi 采集调用流程：
CaptureChangeMySQL → RouteOnAttribute → MySQLBinLogToHiveProcessor → PutHiveQL
```
画面10：
```
nifi 流程 xml 代码路径：
├── 缓存资料
│   └── 热门学科排名
│       └── 热门学科排名-数据采集_用户选课.xml
```
画面13：
```
NiFi 调度使用 nifi 调用 python 脚本，产生模拟数据。此方法可以方便快速生成大量测试数据，生成数据逻辑如下：
1. MySQL 脚本程序(根据用户id，NiFi 调度传递给 Python 脚本
2. Python 脚本根据 id 和 userId 生成模拟数据
```
画面14：
```
NiFi 调度使用 nifi 调用 python 脚本，产生模拟数据。此方法可以方便快速生成大量测试数据，生成数据逻辑如下：
1. MySQL 脚本程序(根据用户id，NiFi 调度传递给 Python 脚本
2. Python 脚本根据 id 和 userId 生成模拟数据
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
标题：3.3.3 数据采集实现
流程图结构：CaptureChangeMySQL → RouteOnAttribute → MySQLBinLogToHiveProcessor → PutHiveQL
画面10：
标题：3.3.3.2 流程代码
目录结构：
├── 缓存资料
│   └── 热门学科排名
│       └── 热门学科排名-数据采集_用户选课.xml
画面13：
标题：3.3.4 NiFi 生产数据
内容：NiFi 调度使用 nifi 调用 python 脚本，产生模拟数据。此方法可以方便快速生成大量测试数据，生成数据逻辑如下：
1. MySQL 脚本程序(根据用户id，NiFi 调度传递给 Python 脚本
2. Python 脚本根据 id 和 userId 生成模拟数据
画面14：
标题：3.3.4 NiFi 生产数据
内容：NiFi 调度使用 nifi 调用 python 脚本，产生模拟数据。此方法可以方便快速生成大量测试数据，生成数据逻辑如下：
1. MySQL 脚本程序(根据用户id，NiFi 调度传递给 Python 脚本
2. Python 脚本根据 id 和 userId 生成模拟数据

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
