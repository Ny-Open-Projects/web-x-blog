# 画面线理解：12.Metricbeat入门学习之部署与收集系统指标

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\12.Metricbeat入门学习之部署与收集系统指标【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:28, 00:52, 01:30, 02:04, 02:45, 03:02, 03:25, 04:03, 04:17, 04:33, 05:34, 06:02, 06:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:22:17

1) 这一组画面整体在讲如何部署和配置 Metricbeat，使其采集系统指标并发送到 Elasticsearch 和 Kibana。

2) 按时间顺序列出每张画面的要点：
画面1: 进入 Metricbeat 安装目录。
画面2: 无新操作，延续上一画面。
画面3: 展示 Metricbeat 安装包及配套配置文件列表。
画面4: PPT 页面，标题为“3.2、部署与收集系统指标”，列出部署步骤：解压、进入目录、编辑 metricbeat.yml。
画面5: 进入 modules 目录，列出所有模块配置文件（.disabled）。
画面6: 显示 metricbeat.yml 配置文件内容，包含 Modules 配置和 Elasticsearch 模板设置。
画面7: 显示 metricbeat.yml 中 Kibana 设置部分。
画面8: 显示 metricbeat.yml 中输出配置部分，包含 Elasticsearch 和 Logstash 输出设置。
画面9: 进入 system 模块目录，查看 metricbeat.yml 文件。
画面10: 启动 Metricbeat，终端显示加载配置、连接到 Elasticsearch 成功。
画面11: 在 Kibana 中查看 Elasticsearch 的索引，显示 metricbeat 收集的数据。
画面12: 在 Kibana 中查看 metricbeat 收集的系统指标数据。
画面13: PPT 页面，展示 system 模块的配置内容，包括 metrics 和 processors。
画面14: PPT 页面，展示 metricbeat.yml 的配置内容，包括 path、reload、setup.kibana、output.elasticsearch 和 processors。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面3:
metricbeat-6.5.4-linux-x86_64
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-haproxy-backend.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-haproxy-http-frontend.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-haproxy-http-server.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-haproxy-overview.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-haproxy-visualizations.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-kafka-overview.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-mongodb-overview.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-mysql-overview.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-rabbitmq-overview.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-redis-overview.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-redis-system-overview.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-redis-windows-service.json
metricbeat-6.5.4-linux-x86_64/kibana/6/index-pattern/metricbeat.json
metricbeat-6.5.4-linux-x86_64/LICENSE.txt
metricbeat-6.5.4-linux-x86_64/metricbeat.yml
metricbeat-6.5.4-linux-x86_64/metricbeat.reference.yml

画面4:
tar -xvf metricbeat-6.5.4-linux-x86_64.tar.gz
cd metricbeat-6.5.4-linux-x86_64
vim metricbeat.yml
metricbeat.config.modules:

画面5:
cd modules/d
ll

画面6:
# This file is an example configuration file highlighting only the most common
# options. The metricbeat.reference.yml file from the same directory contains all the
# supported options with more comments. You can use it as a reference.
# You can find the full configuration reference here:
# https://www.elastic.co/guide/en/beats/metricbeat/index.html
# Modules configuration
metricbeat.config.modules:
  # Glob pattern for configuration loading
  path: ${path.config}/modules.d/*.yml
  # Set to true to enable config reloading
  reload.enabled: false
  # Period on which files under path should be checked for changes
  #reload.period: 10s
# Elasticsearch template setting
setup.template.settings:
  index.number_of_shards: 1
  index.codec: best_compression

画面7:
# Kibana
# Starting with Beats version 6.0.0, the dashboards are loaded via the Kibana API.
# This requires a Kibana endpoint configuration.
setup.kibana:
  # Kibana Host
  # Scheme and port can be left out and will be set to the default (http and 5601)
  # In case you specify and additional path, the scheme is required: http://localhost:5601/path
  # IPv6 addresses should always be defined as: https://[2001:db8::1]:5601
  #host: "localhost:5601"
  # Kibana Space ID
  # ID of the Kibana Space into which the dashboards should be loaded. By default,
  # the Default Space will be used.
  #space.id:

画面8:
# Configure what output to use when sending the data collected by the beat.
output.elasticsearch:
  # Array of hosts to connect to
  hosts: ["192.168.1.7:9200","192.168.1.7:9201","192.168.1.7:9202"]
  # Optional protocol and basic auth credential.
  #protocol: "https"
  #username: "elastic"
  #password: "changeme"
#output.logstash

画面9:
cd system
vim system.yml
cd
ll

画面10:
2019-01-15T00:46:32.028+0800 INFO cfgfile/reload.go:205 Loading of config files completed.
2019-01-15T00:46:32.028+0800 INFO pipeline/output.go:95 Connecting to backoff(elasticsearch)
2019-01-15T00:46:32.028+0800 INFO pipeline/output.go:95 Connecting to backoff(elasticsearch)
2019-01-15T00:46:33.039+0800 INFO elasticsearch/client.go:713 Connected to Elasticsearch v
2019-01-15T00:46:33.039+0800 INFO elasticsearch/client.go:713 Connected to Elasticsearch v
2019-01-15T00:46:33.051+0800 INFO pipeline/output.go:105 Connection to backoff(elasticsearch)
2019-01-15T00:46:33.051+0800 INFO pipeline/output.go:105 Connection to backoff(elasticsearch)
2019-01-15T00:46:33.055+0800 INFO template/load.go:129 Template already exists and will not
2019-01-15T00:46:33.055+0800 INFO template/load.go:129 Template already exists and will not
2019-01-15T00:46:33.063+0800 INFO pipeline/output.go:105 Connection to backoff(elasticsearch)
2019-01-15T00:46:33.063+0800 INFO pipeline/output.go:105 Connection to backoff(elasticsearch)

画面11:
Index: monitoring-es-6-2019.01.15
Type: doc
Score: 1
Cluster_uuid: aqznlBSOYB6TA9QCA
Timestamp: 2019-01-15T00:46:32.027Z
Metricset.name: system
Metricset.module: system

画面12:
Index: monitoring-es-6-2019.01.15
Type: doc
Score: 1
Cluster_uuid: aqznlBSOYB6TA9QCA
Timestamp: 2019-01-15T00:46:32.027Z
Metricset.name: system
Metricset.module: system
