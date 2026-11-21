# 画面线理解：17.Kibana入门学习之Metricbeat仪表盘

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\17.Kibana入门学习之Metricbeat仪表盘【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:36, 00:56, 01:25, 01:58, 02:21, 02:48, 03:10, 03:34, 03:55, 04:38, 04:55, 05:24, 05:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:25:12

1) 这一组画面整体在讲什么（一句话）：
演示如何配置并使用 Metricbeat 将系统指标数据导入 Kibana 并展示仪表盘。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 讲义第 4.5 节“Metricbeat 仪表盘”，说明 Metricbeat 数据可在 Kibana 中展示，并显示配置文件 `setup.kibana` 的内容：`#修改metricbeat配置 setup.kibana: host: "192.168.1.7:5601"`。
画面 2: 展示 Kibana 中 Metricbeat 系统概览仪表盘，包含 CPU、内存、负载、网络流量等指标图表。
画面 3: 展示 PDF 讲义第 4.6 节“Filebeat 仪表盘”，并显示 Kibana 中仪表盘列表，包含 Metricbeat 各模块的仪表盘。
画面 4: 展示终端中 Metricbeat 配置文件 `setup.kibana` 的内容，其中 `host` 设置为 `"localhost:5601"`。
画面 5: 展示终端中进入 Metricbeat 安装目录并执行 `./metricbeat setup --dashboards` 命令，加载仪表盘。
画面 6: 展示 Kibana 中仪表盘正在加载的状态。
画面 7: 展示终端中执行 `./metricbeat setup --dashboards` 命令后，提示“Loaded dashboards”。
画面 8: 展示 Kibana 中 Metricbeat 系统主机概览仪表盘，显示 CPU、内存、磁盘等指标，提示“无数据可显示”。
画面 9: 展示 Kibana 中“按 CPU 使用率的主机直方图”，鼠标悬停显示 CPU 使用率 22.4%。
画面 10: 展示 Kibana 中“网络流量（数据包）”和“网络流量（字节）”图表，以及“按内存排序的进程”和“按 CPU 排序的进程”图表。
画面 11: 展示 Kibana 中“Redis 客户端”仪表盘，显示连接客户端数量、主机信息、服务器版本等。
画面 12: 展示 Kibana 中“Redis 服务器模式”仪表盘，显示集群和 epoll 模式。
画面 13: 展示 Kibana 中 Metricbeat 各模块仪表盘列表，包括 Docker、Apache、Golang、HAProxy、MySQL 等。
画面 14: 重复画面 2 的内容，展示 Kibana 中 Metricbeat 系统概览仪表盘。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
#修改metricbeat配置
setup.kibana:
  host: "192.168.1.7:5601"
```
画面 4:
```
#setup.dashboards.enabled: false

# The URL from where to download the dashboards archive. By default this URL
# has a value which is computed based on the Beat name and version. For released
# versions, this URL points to the dashboard archive on the artifacts.elastic.co
# website.
#setup.dashboards.url:

# Starting with Beats version 6.0.0, the dashboards are loaded via the Kibana API.
# This requires a Kibana endpoint configuration.
setup.kibana:
  # Kibana Host
  # Scheme and port can be left out and will be set to the default (http and 5601)
  # In case you specify and additional path, the scheme is required: http://localhost:5601/path
  # IPv6 addresses should always be defined as: https://[2001:db8:1]:5601
  host: "localhost:5601"
```
画面 5:
```
root@itcast01:metricbeat-6.5.4-linux-x86_64# ./metricbeat setup --dashboards
Loading dashboards (Kibana must be running and reachable)
Loaded dashboards
```
画面 7:
```
root@itcast01:metricbeat-6.5.4-linux-x86_64# ./metricbeat setup --dashboards
Loading dashboards (Kibana must be running and reachable)
Loaded dashboards
```
画面 11:
```
Hosts [Metricbeat Redis]
metricset.host: Descending
Uptime (s)  PID  Memory  CPU used(user)  CPU used (system)
192.168.1.76579  10.142  1  1.506MB  16.16  26.324
192.168.1.76380  10.142  1  1.506MB  16.408  26.516
192.168.1.76381  10.142  1  1.506MB  16.456  26.696
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: PPT 标题为“4.6. Filebeat 仪表盘”，展示 Kibana 仪表盘，包含多个指标图表。
画面 3: PPT 标题为“4.6. Filebeat 仪表盘”，展示 Kibana 仪表盘列表，包含 Metricbeat 各模块的仪表盘。
画面 13: PPT 标题为“Metricbeat 各模块仪表盘”，展示仪表盘列表，包括 Docker、Apache、Golang、HAProxy、MySQL 等。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
