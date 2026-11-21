# 画面线理解：18-flume拦截器-配置文件编写

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\18-flume拦截器-配置文件编写【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:43, 01:06, 02:36, 04:23, 05:16, 06:02, 06:58, 07:24, 07:51, 08:11, 08:43, 10:39, 11:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 08:36:18

1) 这一组画面整体在讲什么（一句话）：
演示如何在 node01 和 node02 服务器上配置 Flume 的采集端配置文件，以实现对不同日志文件的采集并传输至 node03 服务器。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了 Flume 配置文件的编辑界面，文件路径为：/export/servers/apache/flume-1.6.0-cdh5.4.0/bin/conf
- 配置文件内容为：
  ```
  # Name the components on this agent
  a1.sources = r1 r2 r3
  a1.sinks = k1
  a1.channels = c1

  # Describe/configure the source
  a1.sources.r1.type = exec
  a1.sources.r1.command = tail -F /export/servers/taillogs/access.log

  # Describe the sink
  a1.sinks.k1.type = avro
  a1.sinks.k1.hostname = node03
  a1.sinks.k1.port = 41414

  # Use a channel which buffers events in memory
  a1.channels.c1.type = memory
  a1.channels.c1.capacity = 20000
  a1.channels.c1.transactionCapacity = 10000

  # Bind the source and sink to the channel
  a1.sources.r1.channels = c1
  a1.sources.r2.channels = c1
  a1.sources.r3.channels = c1
  a1.sinks.k1.channel = c1
  ```

画面2：
- 展示了 Flume Agent 启动后日志输出，显示 agent 正在等待 runner 线程退出，表明 agent 已启动但尚未完成初始化或正在等待数据。

画面3：
- 展示了 Flume 配置文件中关于 source r3 的拦截器配置，用于为事件添加静态 header。
- 配置内容为：
  ```
  a1.sources.r3.interceptors.i3.type = static
  a1.sources.r3.interceptors.i3.key = type
  a1.sources.r3.interceptors.i3.value = web
  ```

画面4：
- 展示了 Flume 官方文档中关于 Static Interceptor 的说明。
- 文档内容包括：
  ```
  Static Interceptor allows user to append a static header with static value to all events.
  The current implementation does not allow specifying multiple headers at one time. Instead user might chain multiple static interceptors each defining a static header.
  ```
- 属性表：
  ```
  Property Name    Default    Description
  type             type      The component type name, has to be exist
  preserveExisting true      If configured header already exists, should it be preserved - true or false
  key              key       Name of header that should be created
  value            value     Static value that should be created
  ```

画面5：
- 展示了 Flume 配置文件中关于 source r2 和 r3 的完整配置，包括命令和拦截器。
- 配置内容为：
  ```
  a1.sources.r2.type = exec
  a1.sources.r2.command = tail -F /export/servers/taillogs/nginx.log
  a1.sources.r2.interceptors = i2
  a1.sources.r2.interceptors.i2.type = static
  a1.sources.r2.interceptors.i2.key = type
  a1.sources.r2.interceptors.i2.value = nginx

  a1.sources.r3.type = exec
  a1.sources.r3.command = tail -F /export/servers/taillogs/web.log
  a1.sources.r3.interceptors = i3
  a1.sources.r3.interceptors.i3.type = static
  a1.sources.r3.interceptors.i3.key = type
  a1.sources.r3.interceptors.i3.value = web
  ```

画面6：
- 展示了配置文件编辑完成并保存后，终端提示“[New] 42L, 1392C written”，表示文件已成功写入。
- 同时显示了 Notepad++ 编辑器窗口，其中包含配置文件内容。

画面7：
- 展示了将配置文件 `exec_source_avro_sink.conf` 从 node01 服务器复制到 node02 服务器的过程。
- 命令为：
  ```
  [root@node01 conf]# scp exec_source_avro_sink.conf node02:$PWD
  ```
- 复制进度显示为 100%，传输速度为 1.4KB/s，耗时 00:00。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
见上文第2点各画面要点中的代码和命令。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- 画面1中 PPT 标题为“4、实现”，内容包括服务器 IP 地址和采集端配置文件开发。
- 画面4中 Flume 官方文档包含表格数据，见上文第2点画面4要点。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）
