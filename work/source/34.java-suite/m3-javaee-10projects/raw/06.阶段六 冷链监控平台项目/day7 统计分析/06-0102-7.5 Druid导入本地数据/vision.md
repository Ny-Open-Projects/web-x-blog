# 画面线理解：7.5 Druid导入本地数据

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.5 Druid导入本地数据_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:36, 02:11, 02:32, 02:43, 03:03, 03:53, 04:19, 05:35, 05:53, 06:28, 07:09, 07:34, 07:52, 08:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:41:10

1) 这一组画面整体在讲如何通过 Apache Druid 的图形化界面完成数据的加载、转换和发布流程。

2) 按时间顺序列出每张画面的要点：
画面 1: 显示 Druid 数据加载器的初始界面，提示用户选择原始数据的位置，提供 HTTP(s)、AWS S3、Google Cloud Storage 和 Local disk 等选项。
画面 2: 在终端中执行命令，尝试创建目录并查看 JSON 文件，但提示文件或目录不存在。
画面 3: 在终端中显示了 JSON 数据的样本内容，包含时间戳、频道、评论等字段。
画面 4: 终端中继续显示 JSON 数据样本，包含更多评论记录。
画面 5: Druid 数据加载界面，处于“Connect and parse raw data”阶段，右侧显示“Firehose type”为 local，“Base directory”为 /path/to/files，提示路径必须在所有 Druid 服务器的本地文件系统上。
画面 6: 数据加载界面，已选择“local”作为 Firehose type，Base directory 为 /path/to/tutorial，File filter 为空，右侧显示警告信息“此路径必须在所有 Druid 服务器的本地文件系统上”。
画面 7: 数据加载界面，处于“Transform and configure schema”阶段，提示用户选择解析器（Parser to use）为 json，并提供“Add column flattening”和“Preview”按钮。
画面 8: 数据加载界面，处于“Transform and configure schema”阶段，提示用户可以添加列过滤器（Add column filter）和全局过滤器（Add global filter），并提供“Preview”按钮。
画面 9: 数据加载界面，处于“Transform and configure schema”阶段，提示用户可以添加列转换（Add column transform），并提供“Preview”按钮。
画面 10: 数据加载界面，处于“Transform and configure schema”阶段，显示了数据列的预览表，包括 time、added、channel、cityName、comment、countryCode、countryName、deleted、delta、isAno 等列，并配置了时间戳规范（Timestamp spec），从“time”列提取，格式为“ISO”。
画面 11: 数据加载界面，处于“Publish configuration”阶段，显示数据源名称为“tutorial”，并设置“Append to existing”为 False。
画面 12: 数据源页面，显示“Datasources”标题，下方无数据源信息，有“Refresh”、“Go to SQL”和“Show disabled”按钮。
画面 13: 任务页面，显示“Supervisors”和“Tasks”两个部分，Supervisors 中有一个名为“all_device_message”的 Kafka 数据源，状态为“Running”。
画面 14: 数据加载界面，处于“Connect and parse raw data”阶段，显示了数据样本，右侧显示“Firehose type”为 local，“Base directory”为 /path/to/tutorial，File filter 为空，提示路径必须在所有 Druid 服务器的本地文件系统上。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面 2:
```bash
[root@node2-w06 tutorial]# bash quickstart/tutorial
bash quickstart/tutorial: No such file or directory
[root@node2-w06 tutorial]# quickstart/tutorial
quickstart/tutorial: No such file or directory
[root@node2-w06 tutorial]# bash quickstart/tutorial
bash quickstart/tutorial: No such file or directory
[root@node2-w06 tutorial]# cat wikipedia-top-pages.json
{
  "queryType": "topk",
  "dataSource": "wikipedia",
  "intervals": ["2025-09-12/2025-09-13"],
  "granularity": "all",
  "dimension": "page",
  "metric": "count",
  "threshold": 10,
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无。

5) 无。
