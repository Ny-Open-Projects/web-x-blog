# 07.Filebeat入门学习之自定义标签和字段

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\07.Filebeat入门学习之自定义标签和字段【海量资源尽在 ubkz.com】.mp4
- 时长 6分11秒（音频 371s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么我们接着继续那么接下来呢我们来看一下自定义的制段那么这个是什么意思呢我们来看一下那么在前面呢我们是不是去输入这个内容之后呢我们下游呢就可以得到我们这样的一个数据但是有些时候呢我们是需要在这个数据中啊添加一些我们自定义的一些制段那么这个应该怎么去添加呢我们一起来看一下那么在我filebit中啊它支持两种方式
[00:25] 第一种方式就是这个tags这种方式去做一个添加就可以去打一些这个标签那么还有的是fill的这种方式等我们一起来看一下那么还是呢打开我们刚刚这个配置文件Hawk这个配置文件然后呢在下面这个位置啊我们给它添加一个叫什么呢tags然后呢冒号然后呢加一个中国号宿主比如说我们可以添加一个叫做什么web或者叫什么imok那么我们做一个测试那么现在我们是不是已经添加了两个
[00:54] 这个tag那么也就意味着我们这个failbit处理完的数据发送到下游的时候是不是一定会包含这两个tag对吧好然后呢保存退出来看一下那么我们接下来呢来执行一下是不是通过这个failbit这个命令-1-c指定这个号客然后呢我们去做一个执行然后呢接下来我们是不是就可以去向我们这个文件中去写入内容了对吧那我们是不是可以这样去写入一口输入一个123
[01:23] 然后到哪里是不是到我们这A点log下面然后我们来看它启动起来没有启动起来了然后我们走那么执行那么现在显然我们是不是已经写入了这个内容那么会发现我们写入内容是123它是不是已经就涵盖了或者携带了一个tags这样的一个属性然后它的两个值一个是web一个是imok那么在我们下游去拿到这个数据的时候是不是就可以根据这两个我们制定的业务的一个值
[01:51] 做我们的一些具体业务逻辑的一个处理了对吧OK好这个就是他个自定义的一个tag的一个作用当然了除了这个自定义tag之外呢我们还可以去自定义我们的一些这个字段那我们一起来看一下那么自定义这个字段呢我们是需要去写先写一个这什么呢叫fields然后呢在这个下面我们再去我们再去写他的一些具体的字段那么具体字段比如说你可以写一个from然后呢
[02:20] 比如form是来自于谁呢比如说来自于hawk-im还有一些其他字段比如说叫什么呢就叫itcast对吧然后呢我们然后呢写一个什么呢黑马黑马ok然后呢下面呢还有一个啊还有一个这个属性它是什么意思呢它是指我们所添加的这个字段啊它是不是要放到我们这个在结构中的这个根目录下面啊
[02:50] 那么我们这样我们先不添加我们先来做个测试我们来看效果吧走保存退出然后呢我们先把它呢也跑起来然后呢我们再像我们这个文件中啊重新写入内容比如说我们改成456456走OK然后呢我们来看它的一个处理那么看它能否去添加我们刚刚所写的两个字段对吧那么我们稍微等一下
[03:14] 那么我们等了一会儿能发现数据并没有过来那么会有点问题有问题就是我们这个数据我们这个文件的文件的行数并没有发生变化所以导致他不会读取到我们这个文件内容那么我们还是通过这种方式点log我们再添加一个比如说我们改成什么改成改成789然后保存退出一下看一下他能否执行过来那么我们看一下789这个数据稍微等一下
[03:41] OK那么现在我们看到这个789这条数据了可以看到啊message是不是这个789然后呢我们看一下我们制定一个字段是不是在这个位置对吧一个fields然后呢from这个浩克这个im然后呢itcast然后呢黑马刚才我们这个拼错了拼错了好那么我们这样我们是不是还有个属性没有设置对吧我们再来设置一下这个属性再来看一下啊那么刚刚我们itcastitcast拼错了
[04:11] 把这个重新写一下CAST那么下面呢还有一个属性我们一起来看一下那么是去指定它是否是在这个根结点啊那么这样我们先来做一个测试那么我们先把它设置为我们先把它设置为FORCE我们来看一下多了啊到这儿那么先设置为FORCE我们来看一下这个效果OK然后呢我们做一个启动
[04:39] 那么我们把这个看一下它已经有数据了那么我们来看一下它的一个field是不是以这样的一种方式去添加跟我们前面默认情况是不是一样的那么它会把我们的一些所定义的一些这个自定义的一些字段添加到一个field这个下面来那么如果现在注意那么如果现在我们把它改为什么呢改为chew那么看一下它会怎么样呢这个我们改为chew然后保存退出然后我们再次启动那我们来看一下
[05:08] 他会怎么样然后呢我们再去向我们这个里面去写入内容吧比如说我们写入一个111保存退出走然后呢我们来看他拿到的一个数据那么拿到数据呢是111没有问题那么要注意的是那么刚刚我们所制定的那个字段呢我们来找一下啊那么他并没有那个fill的那个字段而是怎么呢而是把我们的这个我们看一下啊而是把我们的所添加制定的字段直接添加到这个根节点下面可以看到了吗是不是一个itcast
[05:38] 黑马那么还有一个呢是上面这个在上面啊有一个叫做from一个from然后呢hawkimok那么就是这样的一个意思啊那么就是说这个参数呢就指定你添加的这个节点呢它是放到你的根节点还是非根节点啊ok好嘞那么如果为fals
[05:57] 那么就添加到哪里呢指节点下面去如果为处那就设置为添加到根体的下面来OK那么其他的也就都一样了好那么这个呢就是给大家所讲的自定义这个标签以及自定义的字段好那么这个我们先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何配置 Filebeat 的自定义字段，包括在配置文件中添加 tags 和 fields，并演示其效果。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 PDF 文档中关于 Filebeat 配置的说明，包含一个示例配置片段。
画面2: 展示 Filebeat 启动日志，显示其加载配置并开始读取日志。
画面3: 展示一个包含自定义字段的 Filebeat 配置片段，其中 offset 设置为 123。
画面4: 展示 Filebeat 停止的日志，显示其已停止读取日志。
画面5: 展示一个包含自定义字段的 Filebeat 配置片段，其中 fields 设置为 "web" 和 "im"。
画面6: 展示在终端中使用 echo 命令向 a.log 文件写入内容。
画面7: 展示在终端中再次使用 echo 命令向 a.log 文件写入内容。
画面8: 展示一个包含自定义字段的 Filebeat 配置片段，其中 fields 设置为 "haoke-im" 和 "heima"。
画面9: 展示在终端中编辑名为 haoke.yml 的配置文件。
画面10: 展示 Filebeat 启动日志，显示其加载配置并开始读取日志。
画面11: 展示一个包含自定义字段的 Filebeat 配置片段，其中 fields_under_root 设置为 false。
画面12: 展示一个包含自定义字段的 Filebeat 配置片段，其中 tags 设置为 "web" 和 "im"。
画面13: 展示一个包含自定义字段的 Filebeat 配置片段，其中 tags 设置为 "web" 和 "im"。
画面14: 展示 PDF 文档中关于 Filebeat 配置的说明，包含一个示例配置片段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```json
{
  "input": {
    "type": "log"
  },
  "beat": {
    "version": "6.5.4",
    "name": "itcast01",
    "hostname": "itcast01"
  },
  "host": {
    "name": "itcast01"
  },
  "source": "/hanke/beats/logs/a.log",
  "offset": 0,
  "message": "world"
}
```

画面3:
```json
{
  "type": "doc",
  "version": "6.5.4",
  "input": {
    "type": "log"
  },
  "prospector": {
    "type": "Log"
  },
  "beat": {
    "name": "itcast01",
    "hostname": "itcast01",
    "version": "6.5.4"
  },
  "host": {
    "name": "itcast01"
  },
  "source": "/haoke/beats/logs/a.log",
  "offset": "123",
  "message": "world"
}
```

画面5:
```yaml
filebeat.inputs:
  type: log
  enabled: true
  paths:
    - /haoke/beats/logs/*.log
  tags: ["web", "im"]
  fields:
    from: haoke-im
    itecast: heima
output.console:
  pretty: true
  enable: true
```

画面6:
```bash
root@itcast01:logs# vim a.log
root@itcast01:logs# echo "123" > a.log
root@itcast01:logs#
```

画面7:
```bash
root@itcast01:logs# vim a.log
root@itcast01:logs# echo "456" > a.log
root@itcast01:logs#
```

画面8:
```json
{
  "input": {
    "type": "log"
  },
  "beat": {
    "name": "itcast01",
    "hostname": "itcast01",
    "version": "6.5.4"
  },
  "host": {
    "name": "itcast01"
  },
  "source": "/haoke/beats/logs/a.log",
  "offset": 4,
  "message": "789",
  "prospector": {
    "type": "log"
  },
  "fields": {
    "from": "haoke-im",
    "itecast": "heima"
  }
}
```

画面9:
```yaml
filebeat.inputs:
  type: log
  enabled: true
  paths:
    - /haoke/beats/logs/*.log
  tags: ["web", "im"]
  fields:
    from: haoke-im
    itecast: heima
output.console:
  pretty: true
  enable: true
```

画面10:
```json
{
  "input": {
    "type": "log"
  },
  "beat": {
    "name": "itcast01",
    "hostname": "itcast01",
    "version": "6.5.4"
  },
  "host": {
    "name": "itcast01"
  },
  "source": "/haoke/beats/logs/a.log",
  "offset": 0,
  "message": "world"
}
```

画面11:
```yaml
filebeat.inputs:
  type: log
  enabled: true
  paths:
    - /haoke/beats/logs/*.log
  tags: ["web", "im"]
  fields:
    from: haoke-im
    itecast: heima
  fields_under_root: false
output.console:
  pretty: true
  enable: true
```

画面12:
```json
{
  "input": {
    "type": "log",
    "from": "haoke-im"
  },
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
  ],
  "prospector": {
    "type": "log"
  },
  "itcast": "heima"
}
```

画面13:
```json
{
  "input": {
    "type": "log",
    "from": "haoke-im"
  },
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
  ],
  "prospector": {
    "type": "log"
  },
  "itcast": "heima"
}
```

画面14:
```yaml
#配置读取文件 haoke-log.yml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /haoke/beats/logs/*.log
    tags: ["web", "im"]  #添加自定义tag，便于后续的处理
    fields:
      from: haoke-im
      itecast: heima
setup.template.settings:
  index.number_of_shards: 3
output.console:
  pretty: true
  enable: true
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

