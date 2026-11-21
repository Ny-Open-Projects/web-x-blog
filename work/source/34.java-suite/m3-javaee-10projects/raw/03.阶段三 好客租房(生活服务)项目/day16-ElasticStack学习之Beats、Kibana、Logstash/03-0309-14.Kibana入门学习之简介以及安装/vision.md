# 画面线理解：14.Kibana入门学习之简介以及安装

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\14.Kibana入门学习之简介以及安装【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:38, 01:22, 01:59, 02:09, 02:25, 02:48, 02:59, 03:20, 03:52, 04:26, 04:49, 05:08, 05:37, 05:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:23:28

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 系统中解压、配置并启动 Kibana，使其能与 Elasticsearch 协同工作并提供数据可视化功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 PDF 文档中关于 Kibana 的介绍页，内容为“您使用 Elastic Stack 的窗口”，并附有世界地图点状图。
画面 2：展示 Kibana 官网页面，标题为“您使用 Elastic Stack 的窗口”，并包含“Kibana 101：入门必知的所有内容，观看视频”按钮。
画面 3：展示 Kibana 官网页面，内容包括“用 Machine Learning 探索异常情况”和“通过 Canvas，发挥无限创意”两个功能模块。
画面 4：展示 Kibana 官网页面，内容为“通过 Canvas，发挥无限创意”，并展示销售漏斗图等可视化图表。
画面 5：展示终端界面，显示 Metricbeat 的日志输出，包含系统监控信息和动态配置重载停止的记录。
画面 6：展示终端界面，执行 `cd` 命令进入 `beats` 目录，然后列出目录内容，显示 `metricbeat.yml`、`modules.d/` 等文件。
画面 7：展示终端界面，进入 `kibana-6.5.4-linux-x86_64` 目录，列出 `node_modules/` 下的文件。
画面 8：展示终端界面，进入 `kibana-6.5.4-linux-x86_64` 目录下的 `config/` 子目录，列出 `kibana.yml` 等文件。
画面 9：展示终端界面，打开并显示 `kibana.yml` 配置文件内容，包含 `#Elasticsearch.ssl.verificationMode`、`#Elasticsearch.pingTimeout` 等注释。
画面 10：展示 PDF 文档中“4.1、配置安装”章节，内容包括解压命令、修改配置文件命令和启动命令。
画面 11：展示终端界面，进入 `kibana-6.5.4-linux-x86_64/bin/` 目录，列出 `kibana` 可执行文件。
画面 12：展示浏览器地址栏，输入 `192.168.1.7:9200` 后跳转至 Google 搜索页面，显示搜索建议。
画面 13：展示 Kibana 登录页面，提示“Help us improve the Elastic Stack...”，并显示“Add Data to Kibana”功能模块。
画面 14：展示 PDF 文档中“4.1、配置安装”章节，内容与画面 10 相同，包含解压命令、修改配置文件命令和启动命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5：无直接代码或配置。
画面 6：
```
root@itcast01:beats# cd
root@itcast01:beats# ll
total 39164
drwxr-xr-x 2 root root 4096 Jan 15 22:04 .
drwxr-xr-x 4 root root 4096 Dec 18 04:29 metricbeat
drwxr-xr-x 2 root root 4096 Dec 18 04:29 metricbeat.yml
drwxr-xr-x 2 root root 4096 Dec 18 04:29 modules.d/
drwxr-xr-x 2 root root 4096 Dec 18 04:29 README.md
```
画面 7：
```
kibana-6.5.4-linux-x86_64/node_modules/@elastic/eui/lib/components/header/header_alert/index.js
```
画面 8：
```
root@itcast01:config# ll
total 16
drwxr-xr-x 2 itcast itcast 4096 Dec 18 05:33 .
drwxr-xr-x 11 itcast itcast 5054 Dec 18 05:23 kibana.yml
```
画面 9：
```
# To disregard the validity of SSL certificates, change this setting's value to 'none'.
#Elasticsearch.ssl.verificationMode: full

# Time in milliseconds to wait for Elasticsearch to respond to pings. Defaults to the value of
#Elasticsearch.pingTimeout: 1500

# Time in milliseconds to wait for responses from the back end or Elasticsearch. This value
# must be a positive integer.
#Elasticsearch.requestTimeout: 30000

# List of Elastic client-side headers to send to Elasticsearch. To send "no" client-side
# headers, set this value to [] (an empty list).
#Elasticsearch.requestHeadersWhitelist: []

# Header names and values that are sent to Elasticsearch. Any custom headers cannot be overwritten
# by client-side headers, regardless of the elasticsearch.requestHeadersWhitelist configuration.
#Elasticsearch.customHeaders: {}

# Time in milliseconds for Elasticsearch to wait for responses from shards. Set to 0 to disable.
#Elasticsearch.shardTimeout: 30000

# Time in milliseconds to wait for Elasticsearch at Kibana startup before retrying.
#Elasticsearch.startupTimeout: 5000
```
画面 10：
```
#解压安装包
tar -xvf kibana-6.5.4-linux-x86_64.tar.gz
#修改配置文件
vim config/kibana.yml
#启动
./bin/kibana
#通过浏览器进行访问
http://192.168.1.7:5601/app/kibana
```
画面 11：
```
root@itcast01:config# cd bin/
root@itcast01:bin# ll
total 20
drwxr-xr-x 2 itcast itcast 4096 Dec 18 05:38 .
```
画面 14：
```
#解压安装包
tar -xvf kibana-6.5.4-linux-x86_64.tar.gz
#修改配置文件
vim config/kibana.yml
#启动
./bin/kibana
#通过浏览器进行访问
http://192.168.1.7:5601/app/kibana
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1：PPT 标题为“4. Kibana”，内容为“您使用 Elastic Stack 的窗口”，并附有世界地图点状图。
画面 2：官网标题为“您使用 Elastic Stack 的窗口”，并包含“Kibana 101：入门必知的所有内容，观看视频”按钮。
画面 3：官网标题为“用 Machine Learning 探索异常情况”，并包含“通过 Canvas，发挥无限创意”功能模块。
画面 4：官网标题为“通过 Canvas，发挥无限创意”，并展示销售漏斗图等可视化图表。
画面 10：PPT 标题为“4.1、配置安装”，内容包括解压命令、修改配置文件命令和启动命令。
画面 14：PPT 标题为“4.1、配置安装”，内容与画面 10 相同。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
