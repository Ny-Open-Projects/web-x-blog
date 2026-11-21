# 画面线理解：18.Kibana入门学习之Filebeat仪表盘

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\18.Kibana入门学习之Filebeat仪表盘【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:28, 00:36, 00:49, 01:11, 01:15, 01:34, 01:42, 01:58, 02:04, 02:09, 02:27, 02:34, 02:44
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:26:02

1) 这一组画面整体在讲如何通过 Filebeat 配置监控 Redis 日志并将其数据可视化到 Kibana 仪表盘。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PDF 文档中 Filebeat 配置文件内容，包含 inputs、output.elasticsearch、setup.kibana 等配置项，以及安装仪表盘的命令。
画面2：终端显示 metricbeat 服务停止的日志信息。
画面3：终端显示空的命令行界面，准备执行后续操作。
画面4：终端显示进入 Filebeat 目录并列出文件，包含 haoke-redis.yml 配置文件。
画面5：终端执行 ./filebeat -c haoke-redis.yml setup 命令，成功加载索引模板和仪表盘配置。
画面6：终端显示命令执行完成，提示加载仪表盘。
画面7：Kibana Dashboard 页面显示多个 Metricbeat 相关仪表盘。
画面8：在 Kibana Dashboard 页面搜索框中输入 "redis"，筛选出 Filebeat Redis 仪表盘。
画面9：进入 Filebeat Redis 日志页面，显示日志数据。
画面10：在 Filebeat Redis 仪表盘中，显示“无结果”。
画面11：在 Filebeat Redis 仪表盘中，显示“无结果”。
画面12：在 Kibana 日志页面，同时打开 PDF 文档，显示配置文件内容。
画面13：PDF 文档中显示 Filebeat 配置文件内容，聚焦于 output.elasticsearch 和 setup.kibana 配置。
画面14：PDF 文档中显示 Filebeat 配置文件内容，聚焦于 setup.kibana 配置。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1：
#修改配置文件
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /haoke/log/*.log
setup.template.settings:
  index.number_of_shards: 3
filebeat.config.modules:
  path: ${path.config}/modules.d/*.yml
  reload.enabled: false
output.elasticsearch:
  hosts: ["192.168.1.7:9200","192.168.1.7:9201","192.168.1.7:9202"]
setup.kibana:
  host: "192.168.1.7:5601"
#安装仪表盘到kibana
./filebeat -c haoke-redis.yml setup

画面4：
root@itcast01:filebeat-6.5.4-linux-x86_64# ll
drwxr-xr-x 7 root root 4096 Jan 15 18:05 logs/
drwxr-xr-x 6 root root 4096 Jan 15 22:13 .build.hash.txt
drwxr-xr-x 2 root root 41 Dec 18 04:24 .data/
-rw-r--r-- 1 root root 100372 Dec 18 04:22 fields.yml
-rw-r--r-- 1 root root 35930715 Dec 18 04:22 filebeat*
-rw-r--r-- 1 root root 68183 Dec 18 04:21 filebeat.reference.yml
-rw-r--r-- 1 root root 324 Jan 15 17:51 haoke-es.yml
-rw-r--r-- 1 root root 308 Jan 15 19:49 haoke.yml
-rw-r--r-- 1 root root 227 Jan 15 17:37 haoke.yml
-rw-r--r-- 1 root root 13675 Dec 18 04:17 LICENSE.txt
-rw-r--r-- 1 root root 802 Jan 15 19:34 log/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 NOTICE.txt
-rw-r--r-- 1 root root 802 Jan 15 19:34 README.md
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw
