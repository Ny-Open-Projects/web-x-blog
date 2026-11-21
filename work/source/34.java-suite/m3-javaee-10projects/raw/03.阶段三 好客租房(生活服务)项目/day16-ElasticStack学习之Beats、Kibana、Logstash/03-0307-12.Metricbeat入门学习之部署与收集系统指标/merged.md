# 12.Metricbeat入门学习之部署与收集系统指标

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\12.Metricbeat入门学习之部署与收集系统指标【海量资源尽在 ubkz.com】.mp4
- 时长 6分17秒（音频 377s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么接下来呢我们就来部署一下magicbit然后呢以及我们去搜集一下我们操作系统一些指标那么我们依然呢还是进入到我们这个目录啊就是beast这个目录然后呢我们去找到我们的一个安装包那么安装包呢是在我们前面的是在这一天的这个下面对吧在第13天这个下面有一个安装包然后呢我们把这个magicbit在这然后呢把它呢上传到我们的这个目录下面
[00:29] 那么我们等待他这个上传上传完成之后那么我们就去做一个解压解压之后我们就去进入目录然后去修改配置文件然后就OK了好那么我们去查看一下那么在这个里面我们去把我们刚刚去上传到我们这个服务器上面的这个压缩包去做一个解压那么解压完成之后我们就需要把它删除掉了新一点gz
[00:58] 好那么这样的话我们就进入magicbit这个目录然后在这个里面我们可以看到这个目录结构跟我们前面所讲的filebit基本上差不多基本上类似然后我们来看一下重点我们又看两个内容第一个就是这个magic的这个是一个magicbit这个是我们的执行脚本然后下面这个是magicbit的一个yaml是这个核心的配置文件
[01:22] 那么我们打开这个metricbit然后呢yaml文件那么这个里面我们会做一些这个修改那我们将去参考我们这个文档中内容啊去做一些这个修改那么要注意的是首先第一个可以看到那么它的我们看一下啊首先第一个它的一个配置呢就是去定义或者说配置指定我们这个moduleok然后呢我们继续往下面去看
[01:49] 那么当然你要注意它所配置目录是在这个modules d这个目录下面新典压编文件那我们就来看一下这个目录下面它有没有一些可以被读取到的我们的配置文件来看一下那么可以看到在这个下面是不是基本上都是disable但是要注意有一个并没有disable那么也就意味着什么呢它默认情况下面是不是就开启了系统system的一个相关的一些配置那么我们可以打开这个system
[02:17] 可以看一下那么在这个里面是不是可以看到这个是他的一个module这个名字然后这个是不是他一个采集的一个间隔就是每10秒钟去采集一次然后下面这个内容是不是就是他的一些采集的一些指标metric set这个我们前面是不是也说过OK好嘞那么这个是他的一些定义然后我们再回到刚刚我们所说的配置文件中我们来看一下在这个里面这个没有问题这个我继续往下面看
[02:46] 它是不是也没有问题那么它的这个就是我们的所以它分辨的默认是一你可以给它把它设置大一点比如说设置三都可以好那么接着我们继续往下面看那么下面还有哪些内容需要去做一些调整呢我们来看一下这开发的我们先不做一个调整后面我们再说然后这个是elag search它的一个配置那么我们把那个elag search的配置我们拷贝过来是在这个位置拷贝一下到这
[03:14] 然后我们去把它去丢到这来丢到这好那么这个就是Elasticsearch的一个配置那么下面的话就没有什么配置了非常简单只需要改一个Elasticsearch的一个配置就OK了然后保存退出然后接下来我们就可以去做一个启动了那么怎么样启动呢跟我们刚刚的failbit是一样的通过这个点斜杠match个bit
[03:41] 然后呢注意-1啊注意-1如果你没有-1的话它会在当前这个目录下面会有一个logs文件会把这个输出呢写到log文件中如果有意义的话那么就直接在我们的控制台去输出这样的话方便我们去做一个调试OK然后呢我们直接去启动就可以了不需要去指定配置文件为什么不需要呢原因是那么默认就会读取到这个配置文件啊OK好那么我们就可以直接做一个启动了走
[04:08] 那么现在呢我们其实就可以看到它已经启动起来了然后呢并且它已经连接到我们的elag search然后呢就说明它肯定已经是去发送数据了是不是好那我们就来看一下看一下我们这个elag search然后呢进入我们盖蓝这个页面中然后呢我们刷新一下那么可以看到在这个位置呢有个magic bit这样的一个所以那我们可以看到来查看它的数据啊那我点击这个magic bit然后呢会发现这个是不是它的一些这个数据啊那么我们可以
[04:37] 大概的我们来点击一下吧来查看一下这个数据点击它然后呢在后面吧我们来看一下这个它的一个magic set一个name就是指标的一些名字包括你可以看到这个是一些network网络相关的一些这个内容还有什么呢这个memory就是内存还有文件系统等等相关的一些这个内容了好那么我们就来点击一下这个文档的内容具体来查看一下那么我们可以看到这个是它的一个指标然后呢它的一个
[05:07] 这个这个network系统等等然后呢还有system一些网络的一些这个数据这个他的一些这个数据对吧具体一些指标的数据那么这个是网络因为网络呢就会有一个流进
[05:20] 而流入和流出那么所以这个是一个硬这个是一个outOK那么这个数据呢基本上我们还是能够看懂的OK那么这样的话呢我们是不是就非常简单的就可以去收集到我们系统的一些指标的数据并且呢把它已经就发送到elax的指桌那么后面我们是不是就可以基于这个数据把它通过这种图形化的界面的工具然后就可以展现出来了OK好那么我们接着继续往下面看这样的话呢就已经写的完成了
[05:49] 然后我们可以看一下系统module的一些配置这个我们刚刚其实也说过那么下面这个指标就是我们刚刚其实所看到的它收集到这个数据的这个指标这么几个好嘞好那么下面这个我们就不去查看了OK好那么这样的话我们其实就已经完成了我们的第一个magicbit的一个使用那么就是收集我们系统的一个指标好那这个我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面14: PPT 页面，展示 metricbeat.yml 的配置内容，包括 path、reload、setup.kibana、output.Elasticsearch 和 processors。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面3:
metricbeat-6.5.4-linux-x86_64
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-haproxy-backend.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-haproxy-http-frontend.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-haproxy-http-server.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-haproxy-overview.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-haproxy-visualizations.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-Kafka-overview.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-mongodb-overview.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-mysql-overview.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-RabbitMQ-overview.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-redis-overview.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-redis-system-overview.json
metricbeat-6.5.4-linux-x86_64/kibana/6/dashboard/Metricbeat-redis-windows-Service.json
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
output.Elasticsearch:
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
2019-01-15T00:46:32.028+0800 INFO pipeline/output.go:95 Connecting to backoff(Elasticsearch)
2019-01-15T00:46:32.028+0800 INFO pipeline/output.go:95 Connecting to backoff(Elasticsearch)
2019-01-15T00:46:33.039+0800 INFO Elasticsearch/client.go:713 Connected to Elasticsearch v
2019-01-15T00:46:33.039+0800 INFO Elasticsearch/client.go:713 Connected to Elasticsearch v
2019-01-15T00:46:33.051+0800 INFO pipeline/output.go:105 Connection to backoff(Elasticsearch)
2019-01-15T00:46:33.051+0800 INFO pipeline/output.go:105 Connection to backoff(Elasticsearch)
2019-01-15T00:46:33.055+0800 INFO template/load.go:129 Template already exists and will not
2019-01-15T00:46:33.055+0800 INFO template/load.go:129 Template already exists and will not
2019-01-15T00:46:33.063+0800 INFO pipeline/output.go:105 Connection to backoff(Elasticsearch)
2019-01-15T00:46:33.063+0800 INFO pipeline/output.go:105 Connection to backoff(Elasticsearch)

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

