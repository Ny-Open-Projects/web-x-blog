# 06.Filebeat入门学习之读取日志文件

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\06.Filebeat入门学习之读取日志文件【海量资源尽在 ubkz.com】.mp4
- 时长 4分10秒（音频 250s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么我们接着继续那么接下来呢我们来看一下这个读取文件那么前面我们写的第一个这个例子呢我们是通过我们的控制台的标准的输入去做一个输入对吧那么下面我们来看一下如何我们去读取一个文件那么读取文件呢是需要做两个设置第一个呢是指定这个type为log第二个呢是我们需要指定一个pass就是我们的一个log文件这样的一个目录
[00:24] OK好那么我们来做一个测试那么现在我们进入这个biz这个目录然后我们创建一个目录叫做什么logs然后我们进入logs下面我们去创建一个文件比如说叫a.log好嘞那么我们现在只创建了空的一个log文件什么都没有然后我们进入到我们刚刚的failbit中然后我们去打开有个后刻
[00:50] 点YAML文件那么在这个里面我们给他去把配置文件的修改一下把我们改成什么的改成log第一个改动是他第二个改动就需要在这个位置添加一个什么叫pass然后我们重新拷贝一下刚才拷贝有点问题然后到这个位置来一个pass然后在这个下面
[01:20] 注意那么在这个下面我们还是需要给他去设置一个横杠横杠代表什么可以有多个那么来一个横杠空格再去加一个目录是一样的那么OK那就他然后我们可以使用通配服去拿到下面所有的日志文件OK好那么我们保存退出然后接下来我们把我们failbit跑起来那么来一个failbit让他-e-c然后来一个浩克点Yaml走
[01:48] 那么我们为了测试我们再开一个窗口再开一个窗口然后我们进入到我们刚刚所创建的目录浩克下面的bis下面一个logs这个目录这个目录下面是不是本身有一个A.log这个文件对吧A.log这个文件我们其实可以看到
[02:05] 在这个位置它是不是已经加载到我们logs下面的一个新点log对吧ok那么它应该是在这个位置你看在这它已经是找到我们的一个文件是不是就是下面b是下面log下面的a点log这个文件ok好那么我们再来做一个测试就是我们向我们 a点log里面去写内容比如说我这个里面写一个
[02:29] 123内容然后保存退出走看效果那我们回到这个里面来看一下它是否能够感知到我们这个文件的一个变化然后并且我们看到一个输出
[02:39] OK那么现在可以看到这个文件它是不是已感知到文件的一个变化然后已经就读取到这个文件中的一个内容内容是什么呢前面我们说过是不是它会丢到这个message的这个里面它的内容是不是就是123对吧123然后其他的都是一些附属的一些信息我们再来做一个测试我再来写一个比如说我再写一个456那么再写一个什么呢下面写一个456保存退出然后我们再来观察
[03:10] 你看这个里面他这个message456是不是就来了那么假设我们现在有一个应用程序不断的向我们这个log文件中去写入内容的话那么我们的failbit是不是就会不断的去感知到我们这个日志的一个变化然后就会读取到你新增的这个日志这样的一个数据然后就继续向下游传递了OK好那么这个就是我们所讲的所讲的我们去读取我们这个文件读取这个文件OK那么这个是不是我们刚刚的一个
[03:37] 测试那么关键点的就是我们需要把它设置为类型为log并且指定一个pass然后在下面我们需要在我们的日志文件中我们去给它输入一些内容来做一些测试最后就可以看到我们所期望的这样的一个效果OK那么是不是我们日志文件一旦更新就会被读取到然后去输出到我们的控制台当然目前我们所配置的是控制台对吧
[04:05] OK好那么关于这个文件的一个读取那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何配置并运行 Filebeat 来读取日志文件并输出到控制台。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 PDF 文档中 Filebeat 的配置文件示例，包含输入和主机信息。
画面2: 在终端中列出日志目录内容，进入 Filebeat 安装目录。
画面3: 在终端中编辑配置文件，显示 filebeat.inputs 和 output.console 配置。
画面4: 在终端中编辑配置文件，显示 filebeat.inputs 和 output.console 配置。
画面5: 在终端中列出 Filebeat 目录内容。
画面6: SSH 登录 Ubuntu 服务器，显示系统信息和终端提示符。
画面7: 在终端中切换到日志目录并列出文件。
画面8: 在终端中查看 Filebeat 启动日志，显示加载输入和启动成功。
画面9: 在终端中显示 Filebeat 输出的 JSON 格式日志。
画面10: 在终端中查看 a.log 文件内容，显示 "123"。
画面11: 在终端中列出日志目录内容。
画面12: 在终端中显示 Filebeat 输出的 JSON 格式日志，包含 "message": "456"。
画面13: 展示 PDF 文档中 Filebeat 的配置文件示例，包含输入和主机信息。
画面14: 展示 PDF 文档中 Filebeat 的配置文件示例，包含输入和主机信息。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1:
```yaml
#配置读取文件项 haoke-log.yml
filebeat.inputs:
  - type: log
  enabled: true
  paths:
    - /haoke/beats/logs/*.log
setup.template.settings:
  index.number_of_shards: 3
output.console:
  pretty: true
  enable: true
```

画面3:
```yaml
filebeat.inputs:
  - type: log
  enabled: true
output.console:
  pretty: true
  enable: true
```

画面4:
```yaml
filebeat.inputs:
  - type: log
  enabled: true
output.console:
  pretty: true
  enable: true
```

画面8:
```
2019-01-15T17:08:58.137+0800 WARN beater/filebeat.go:374 Filebeat is unable to load the Ingest Node pipelines for the configured modules because the Elasticsearch output is not configured/enabled. If you have already loaded the Ingest Node pipelines or are using Logstash pipelines, you can ignore this warning.
2019-01-15T17:08:58.137+0800 INFO crawler/crawler.go:72 Loading Inputs: 1
2019-01-15T17:08:58.137+0800 INFO log/input.go:138 Configured paths: [/haoke/beats/logs]
2019-01-15T17:08:58.137+0800 INFO crawler/crawler.go:106 Loading and starting Inputs complete
2019-01-15T17:08:58.137+0800 INFO log/harvester.go:254 Harvester started for file: /haoke/beats/logs/a.log
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-

