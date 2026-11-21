# 画面线理解：05.Filebeat入门学习之部署安装（第一个应用）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\05.Filebeat入门学习之部署安装（第一个应用）【海量资源尽在 ubkz.com】.mp4
- 抽帧：13 帧 @ 00:13, 00:49, 01:08, 01:24, 01:38, 01:51, 02:33, 02:57, 03:40, 04:15, 04:55, 05:13, 06:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:16:53

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 系统上部署和运行 Filebeat 日志采集器，并通过配置文件实现向标准输入读取数据并输出。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 Filebeat 官网页面，介绍其为轻量型日志采集器，提供下载和获取产品更新的入口。
画面 2：展示 PDF 文档《Filebeat 部署与运行》的第 2.2 节，内容包含下载命令和配置文件 haoke.yml 的示例。
画面 3：在终端中显示系统磁盘使用情况，列出多个 overlay 和 shm 目录的占用情况。
画面 4：在终端中列出当前目录下的文件，包含 Elasticsearch、Logstash、Kafka、Redis 等相关软件包。
画面 5：在终端中列出当前目录下的文件，与画面 4 类似，显示了多个软件包。
画面 6：在终端中列出 filebeat-6.5.4-linux-x86_64 目录下的文件，包括多个 .yml 配置文件和 LICENSE 等。
画面 7：展示 PDF 文档《Filebeat 部署与运行》的第 2.2 节，内容包含下载命令、配置文件 haoke.yml 的示例和启动命令。
画面 8：在终端中显示 filebeat 配置文件内容，包括 inputs、setup.template.settings、output.console 等配置项。
画面 9：在终端中显示 filebeat 配置文件内容，光标位于 enabled: true 行，准备编辑。
画面 10：在终端中执行解压命令，解压 filebeat-6.5.4-linux-x86_64.tar.gz，然后列出解压后的目录内容。
画面 11：在终端中显示 filebeat 配置文件内容，包括 timestamp、metadata、input、beat、host 等字段。
画面 12：在终端中显示 filebeat 启动后输出的日志，包含 Harvester started for file: - hello。
画面 13：在终端中显示 filebeat 启动后输出的日志，包含 Non-zero metrics in the last。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```
mkdir /haoke/beats
tar -xvf filebeat-6.5.4-linux-x86_64.tar.gz
cd filebeat-6.5.4-linux-x86_64
#创建如下配置文件 haoke.yml
filebeat.inputs:
  type: stdin
  enabled: true
setup.template.settings:
  index.number_of_shards: 3
output.console:
  pretty: true
enable: true
```
画面 7：
```
#创建如下配置文件 haoke.yml
filebeat.inputs:
  type: stdin
  enabled: true
setup.template.settings:
  index.number_of_shards: 3
output.console:
  pretty: true
enable: true
```
画面 8：
```
filebeat.inputs:
  type: stdin
  enabled: true
setup.template.settings:
  index.number_of_shards: 3
output.console:
  pretty: true
enable: true
```
画面 11：
```
{
  "@timestamp": "2019-01-15T06:31:56.023Z",
  "@metadata": {
    "beat": "filebeat",
    "type": "doc",
    "version": "6.5.4"
  },
  "offset": 0,
  "message": "hello",
  "prospector": {
    "type": "stdin"
  },
  "input": {
    "type": "stdin"
  },
  "beat": {
    "name": "itcast01",
    "hostname": "itcast01",
    "version": "6.5.4"
  },
  "host": {
    "name": "itcast01"
  },
  "source": ""
}
```
画面 12：
```
2019-01-15T14:31:44.803+0800 INFO log/harvester.go:254 Harvester started for file: - hello
```
画面 13：
```
2019-01-15T14:32:14.803+0800 INFO [monitoring] log/log.go:144 Non-zero metrics in the last
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2：PPT 标题为“2.2、部署与运行”，内容包含下载命令和配置文件 haoke.yml 的示例。
画面 7：PPT 标题为“2.2、部署与运行”，内容包含下载命令、配置文件 haoke.yml 的示例和启动命令。
画面 11：无 PPT 标题，仅显示配置文件内容。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
