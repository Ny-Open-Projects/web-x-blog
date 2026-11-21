# 08.Filebeat入门学习之输出到Elasticsearch

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\08.Filebeat入门学习之输出到Elasticsearch【海量资源尽在 ubkz.com】.mp4
- 时长 3分19秒（音频 199s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下将我们这个结果数据我们输出到elag search中那么在前面呢我们的一些测试中啊都是将我们的这个数据打印在啊或者说输出到我们那个标准那个输出那么就是在我们的这个控制台这个输出对吧那么我们希望他呢也可以去输出到我们的elag search那么怎么做呢也是非常简单的啊我们来看一下那么需要给他指定这么两个配置那么这样咱们把这两个配置呢先拷贝过来我们再说然后呢把它俩拷贝一下
[00:29] 然后我们打开我们的浩克浩克这个配置文件然后这样我们去我们去把这拷贝一下就是把这个文件拷贝一下然后我们再来创建一个文件叫做浩克-es然后我们打开这浩克-es这个文件然后我们把下面这个output就是之前这个输出我们给它去掉然后我们把这个拷贝过来要注意的是格式那么把后面的注释我们先拿掉
[00:59] 然后这个注释也拿掉这个注释拿掉然后下面的这个是指定指定我们那个索引的分片默认我给它设置为三个分片然后下面通过output就是一个输出输出到哪里输出到elac search中然后通过host通过host来指定我们的一些集群的一个节点那么目前我有三个节点那么我给它指定三个节点就可以了好那么我们保存退出
[01:29] 那么接下来我们依然还是通过我们刚刚这个命令去做一个启动那么我们来一个叫做failbit然后-e-c然后指定一个浩克浩克-es然后去做一个启动那么启动之后我们就尝试着去再次去修改数据那么我们就修改一个什么的这样我们先不做修改我们先来看一下我们这个索引中它有没有一个有没有一个failbit的一个索引发现并没有
[01:56] 然后我们在这里面输入一个数据比如说我们来一个叫222然后保存退出这个时候它显然就能够去拿到我们的数据对吧当然其实我们从这个日子中也可以看到它目前其实已经去连接到我们的elite设置中了对不对已经连接到了ok好嘞那么我们来看一下在我们的elite设置中它就会出现一个什么叫failbit这样的一个这样的一个索引并且这个索引是会按照这个日期
[02:25] 为天为单位每天去创建这样的一个索引库这个一定要注意ok好那么我们来看到它是不是有三个分片对吧这个是0 0 1 2三个分片我们来看这个数据有没有写进来我们点击浏览数据我们点击 failbit那么可以发现这个数据它是不是已经写不进来了ok那么来看一下这个的数据是11对吧然后下面这个数据是多少这个数据找那个message
[02:54] 然后456ok他是不是已经都把数据都写入进来了好那么到这里我们是不是就已经成功的去把我们的数据可以输出到我们的一个elac设置中那么我们已经把它输出到elac设置那么我们是不是就可以再基于elac设置然后再去做一些其他的处理了ok好那么ok那么这个就是我们所讲的输出到elac设置

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何配置 Filebeat 将日志文件输出到 Elasticsearch，并验证数据成功写入。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中 Filebeat 配置文件 `# haoke-log.yml` 的内容，其中包含 `filebeat.inputs`、`paths`、`tags`、`output.Elasticsearch.hosts` 等配置项。
画面 2: 在终端中显示 Filebeat 读取日志文件 `a.log` 的内容，输出为 JSON 格式，包含 `@timestamp`、`@metadata`、`input`、`beat`、`source`、`message` 等字段。
画面 3: PDF 文档中 `# haoke-log.yml` 文件的配置内容，光标位于 `from: haoke-im` 行。
画面 4: PDF 文档中 `# haoke-log.yml` 文件的配置内容，下方显示 Filebeat 版本信息 `filebeat-6.5.4-2019.01.12`，并提示“docs: 1 (2)”。
画面 5: 终端中显示 Filebeat 停止时的详细日志，包含 `Stopping filebeat`、`Stopping Crawler`、`Stopping Input`、`Ending Registrar` 等信息。
画面 6: 终端中显示 Filebeat 停止时的详细日志，光标位于命令行提示符 `root@itcast01:filebeat-6.5.4-linux-x86_64#`。
画面 7: 终端中用户执行命令 `cp haoke.yml haoke-es.yml`，将原配置文件复制为新文件。
画面 8: 终端中用户进入 `logs` 目录并打开 `a.log` 文件，准备编辑。
画面 9: 在 Elasticsearch Head 界面中，显示集群状态为绿色，包含节点 `node01`、`node02`、`node03`，并展示多个窗口的截图。
画面 10: 终端中显示 Filebeat 重新启动后连接到 Elasticsearch 的日志，包括 `Connection to backoff(Elasticsearch)`、`Connected to Elasticsearch v` 等信息。
画面 11: 在 Elasticsearch Head 界面中，用户点击“数据浏览”按钮，准备查看数据。
画面 12: 在 Elasticsearch Head 界面中，显示 `haoke` 索引的数据，包含 `@timestamp`、`beat`、`host`、`source`、`message`、`tags` 等字段。
画面 13: PDF 文档中 `# haoke-log.yml` 文件的配置内容，`output.Elasticsearch.hosts` 行被高亮选中。
画面 14: PDF 文档中显示“查看数据：”字样，右侧弹出窗口展示数据文档，包含编号为 0、1、2 的文档。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```yaml
# haoke-log.yml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /haoke/beats/logs/*.log
    tags: ["haoke-im"]
    fields:
      from: haoke-im
fields_under_root: false
setup.template.settings:
  index.number_of_shards: 3 #指定索引的分片数
output.Elasticsearch: #指定ES的配置
  hosts: ["192.168.1.7:9200","192.168.1.7:9201","192.168.1.7:9202"]
```

画面 2:
```json
{
  "@timestamp": "2019-01-15T09:38:05.752Z",
  "@metadata": {
    "beat": "filebeat",
    "type": "doc",
    "version": "6.5.4"
  },
  "input": {
    "type": "log"
  },
  "from": "haoke-im",
  "beat": {
    "name": "itcast01",
    "hostname": "itcast01",
    "version": "6.5.4"
  },
  "source": "/haoke/beats/logs/a.log",
  "offset": 8,
  "message": "111",
  "host": {
    "name": "itcast01"
  },
  "tags": [
    "web",
    "im"
  ]
}
```

画面 3:
```yaml
# haoke-log.yml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /haoke/beats/logs/*.log
    tags: ["haoke-im"]
    fields:
      from: haoke-im
```

画面 4:
```yaml
# haoke-log.yml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /haoke/beats/logs/*.log
    tags: ["haoke-im"]
    fields:
      from: haoke-im
fields_under_root: false
setup.template.settings:
  index.number_of_shards: 3 #指定索引的分片数
output.Elasticsearch: #指定ES的配置
  hosts: ["192.168.1.7:9200","192.168.1.7:9201","192.168.1.7:9202"]
```

画面 5:
```
INFO beater/filebeat.go:449 Stopping filebeat
INFO crawler/crawler.go:139 Stopping Crawler
INFO input/input.go:149 Stopping Input
INFO input/input.go:167 Stopping ticker
INFO registrar/registrar.go:356 Ending Registrar
INFO [monitoring] log/log.go:152 Total non-zero metrics { "mo
nitoring": { "metrics": { "beat": { "cpu": { "ticks": "60", "time": { "ms": "68"}, "total": { "ticks": "120", "time": { "ms": "132"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "64"}, "total": { "ticks": "120", "time": { "ms": "64"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "64"}, "total": { "ticks": "120", "time": { "ms": "64"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "64"}, "total": { "ticks": "120", "time": { "ms": "64"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "64"}, "total": { "ticks": "120", "time": { "ms": "64"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "64"}, "total": { "ticks": "120", "time": { "ms": "64"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "64"}, "total": { "ticks": "120", "time": { "ms": "64"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "64"}, "total": { "ticks": "120", "time": { "ms": "64"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "64"}, "total": { "ticks": "120", "time": { "ms": "64"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "64"}, "total": { "ticks": "120", "time": { "ms": "64"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "6

