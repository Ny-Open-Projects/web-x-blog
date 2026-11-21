# 24.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\24.课程总结【海量资源尽在 ubkz.com】.mp4
- 时长 3分25秒（音频 205s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们对今天的课程呢做一个小节那么今天呢我们就已经把ELAC stack技术战中的一些所有的这个相关的技术呢都基本上做了一些这个入门的一些学习那么基本上就就能够整个流程都能够跑通了啊
[00:16] 那么我们来分别来看一下首先我们对Bits做了一些了解那么它的作用其实就是去做一些数据的采集它可以采集一切的数据然后后面我们分别讲的是FailbitFailbit主要处理的事情就是去读取一些日志文件然后我们对它做了一些部署
[00:37] 以及安装然后他可以去读取文件也可以去做一些自定义自断的一些添加还可以把数据输出到我们的elite设置中也可以在我们的标准的控制台去做一些输出都是ok的然后我们还学习了failbit的一些工作的原理以及它后面的一些module那么有了module之后我们的处理就会变得更加的轻松更加的便捷了ok那么在我们学完failbit之后我们学了
[01:05] Magic Bit那我Magic Bit呢它呢是主要是用于收集什么呢收集我们一些指标的指标数据的一些收集然后呢我们是不是去去看它的一些这个module然后呢去使用了一下Redis的module当然前面我们还是用的是它的一个system的一个moduleOK然后呢后面学了什么呢KibanaKibana主要是去展现我们数据的它就是一个web项目然后呢去做一些这个展现
[01:32] 然后我们讲过它的一个安装包的方式的安装也讲了Docker的一个安装那么又分别去简单的演示了它的一些基本的一些功能然后在我们后面去整合到LogStats中是不是做了一些功能的演示那么我们可以通过这种数据探索的这种功能去通过界面的方式来查询我们的数据就不需要再去到我们的Elac设置中再去查询数据了
[01:59] 好那么然后我们后面也讲他一些仪表盘的一些使用对吧包括指标的一些仪表盘以及我们的failbit一些仪表盘的一些使用然后最后我们讲的是logstashlogstash它的主要的一个任务有两个第一就是数据采集第二就是数据的一个处理或者转换那么数据的采集被bit已经替代掉了所以说它的功能就剩下什么数据的一些处理
[02:25] OK那么刚刚我们也做了一些这样的演示包括我们讲了他的一些这个部署的安装以及我们去把我们的Failbit跟我们Logstates去整合起来最后把数据发送到我们的ELAC设置中然后最后也就进入到我们的Kibana中做一些展现OK那么这个就是我们今天所讲的一些所有的一些这个内容那么今天的内容其实就是需要
[02:48] 我们要把能够熟练的去把我们的这个Elect stack就是我们最初的这个状态这个图那么能够去把它全部都搭建起来那么数据的一个流向一个处理应该非常清晰的哪一块在做什么事情然后呢它的下游又是谁那么我数据该怎么样去处理等等等等那么能够把这个搭起来那么这个Elect stack这个技术站那么基本上你就学了一个你就基本上入门了
[03:16] 就要入门了OK好那么这个呢就是今天我们所讲的一些内容好那么关于今天的一些内容总结那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Elastic Stack（特别是 Beats 组件）的架构、配置与使用，涵盖 Filebeat、Metricbeat、Redis Module、Kibana 和 Logstash 的相关内容。

2) 按时间顺序列出每张画面的要点：
画面1：展示 ElasticStack 架构图，包含 Beats（Filebeat、Metricbeat、Winlogbeat、Packetbeat、Heartbeat）、Elasticsearch、Logstash 和 Kibana 四个核心组件及其数据流向。
画面2：介绍 Filebeat 作为轻量型日志采集器，用于监控和收集服务器日志文件。
画面3：展示 Filebeat 自定义字段配置文件 `haoke-log.yml` 的内容。
画面4：介绍 Filebeat 的 Module 功能，列出可用的模块列表。
画面5：展示 Redis Module 的配置文件 `modules.d/redis.yml` 内容，包含 hosts、network、maxconn、password 等配置项。
画面6：介绍 Kibana 作为 Elastic Stack 的数据可视化窗口。
画面7：展示 Kibana 的功能说明，包括 Discover、Visualize、Dashboard、Timelion 等功能模块。
画面8：展示 Kibana 的数据探索功能，包括 Canvas、Machine Learning、Infrastructure、Logs、APM、Dev Tools、Monitoring、Management 等模块。
画面9：展示 Metricbeat 的配置文件内容，包含 host 和安装仪表盘的命令。
画面10：展示 Filebeat 仪表盘，包含 CPU、内存、磁盘等系统监控图表。
画面11：展示 Kibana 中的仪表盘列表，包括 Metricbeat 和 Filebeat Redis 的仪表盘。
画面12：展示 Filebeat 和 Logstash 整合的架构图，以及安装 Nginx 的命令 `apt install Nginx -y`。
画面13：页面标题为“2、Filebeat”，内容为空白。
画面14：重复展示 ElasticStack 架构图。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面3：
```yaml
#修改该配置文件 haoke-log.yml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /haoke/beats/logs/*.log
    tags: ["web"]  #添加自定义tag,便于后端的处理
    fields:
      from: haoke-im
    setup.template.settings:
      index.number_of_shards: 3
    output.console:
      pretty: true
    enable: true
```

画面4：
```
./filebeat modules list
Enabled:
Disabled:
apache2
auditd
Elasticsearch
haproxy
Tcinga
tis
Kafka
kibana
```

画面5：
```yaml
#启用redis module
./metricbeat modules enable redis
#修改redis module配置
vim modules.d/redis.yml
# Redis module
module: redis
metricsets:
  - info
  # - keyspace
period: 10s

# Redis hosts
hosts: ["192.168.1.7:6379","192.168.1.7:6380","192.168.1.7:6381"]

# Network type to be used for redis connection. Default: tcp
#Network: tcp

# Max number of concurrent connections. Default: 10
#maxconn: 10

# Redis AUTH password. Empty by default.
#password: foobared
```

画面7：
```bash
#创建容器
Docker create --name kibana --net host -v /haoke/beats/kibana:/usr/share/kibana/config/kibana.yml kibana:6.5.4
#启动kibana
Docker logs -f kibana
```

画面9：
```yaml
#修改metricbeat配置
setup.kibana:
  host: "192.168.1.7:5601"

#安装仪表盘到Kibana
./metricbeat setup --dashboards
```

画面12：
```bash
apt install Nginx -y
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：架构图，从“采集一切数据的Beats”指向“核心存储和检索引擎”（Elasticsearch），再指向“数据可视化”（Kibana），中间有“Ship”和“Parse & Transform”箭头。
画面2：标题“轻量型日志采集器”，内容为文字说明。
画面3：无图表。
画面4：无图表。
画面5：无图表。
画面6：标题“您使用 Elastic Stack 的窗口”，内容为文字说明。
画面7：展示 Kibana 功能模块，包括 Discover、Visualize、Dashboard、Timelion。
画面8：展示 Kibana 数据探索功能模块，包括 Canvas、Machine Learning、Infrastructure、Logs、APM、Dev Tools、Monitoring、Management。
画面9：展示 Metricbeat 配置和安装仪表盘的命令。
画面10：展示 Filebeat 仪表盘，包含 CPU、内存、磁盘等系统监控图表。
画面11：展示 Kibana 中的仪表盘列表，包括 Metricbeat 和 Filebeat Redis 的仪表盘。
画面12：展示 Filebeat 和 Logstash 整合的架构图，从“Nginx”指向“日志文件”，从“日志文件”指向“Filebeat”，从“Filebeat”指向“Logstash”。
画面13：无图表。
画面14：重复展示架构图。

5) 无。

