# 04.Filebeat入门学习之架构

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\04.Filebeat入门学习之架构【海量资源尽在 ubkz.com】.mp4
- 时长 1分45秒（音频 106s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来我们来看一下failbit的一个架构那么首先我们可以看到在这个位置是需要有一个input输入
[00:09] 那么我们想要去搜集日志那么你肯定先得去指定这个日志文件在哪里对吧OK就是需要指定它的一个这个目录路径然后需要注意的是在这个路径中可以采用什么的通配服这种形式比如说新点log那么所有以log结尾的文件都会被读取到比如说这个system log和这个WiFi log都可以被读取到
[00:31] 然后在下面这个也是一个input可以看到下面这个是不是它也是一个input那么也就意味着什么也就意味着我们这个输入可以有多个对吧可以有多个然后当我们去读取到我们这个文件之后会通过它内部的一个组件叫Haiwaist那么这个组件它翻译成中文叫什么叫收割机然后它就可以不断去收购我们这个文件对吧收割文件那么收割文件之后也就是拿到我们的数据了
[00:59] 拿到数据之后他需要怎么办呢通过一个spot那么这个什么意思这个是翻译成中文叫卷轴就是类似于传送带一样然后把我们这个数据源源不断的去传送给我们的下游的服务包括你可以把这个数据
[01:15] 发送给Eraq Search也可以发送给什么Log States也可以发送给Kafka也可以发送给LadiesOK那么都可以做一个发送这样不断的去做一个采集然后不断去做一个发送它这个速度是非常快的非常快的这样的一个速度OK所以说这两个名词它称呼的是非常的形象的对吧
[01:34] OK好那么这个就是它的一个基本架构那么下面我们也是基于这样的一个架构来做一个学习OK好那么关于 failp 的架构我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Filebeat 如何采集不同目录下的日志文件并将其发送到 Spooler，再由 Spooler 分发至 Elasticsearch、Logstash、Kafka 和 Redis 等下游组件。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 Filebeat 的日志采集架构图，包含 Input 1（/var/log/*.log）和 Input 2（/var/log/apache2/*）两个数据源，分别通过 Harvester 采集 system.log 和 wifi.log、error.log，进入 Spooler，再分发至 Elasticsearch、Logstash、Kafka 和 Redis。
画面 2: 与画面 1 相同，无新增要点。
画面 3: 在画面 1 的基础上，对 system.log 和 wifi.log 的 Harvester 节点添加了红色下划线，可能用于强调。
画面 4: 与画面 1 相同，无新增要点。
画面 5: 画面内容变化，Input 2 的路径改为 /var/log/apache2/*，并新增了 error.log 文件，同时在图下方标注了“2.2. 部署与运行”。
画面 6: 在画面 5 的基础上，底部添加了下载信息：“下载（或使用课件中提供的安装包，版本为：filebeat 6.5.4）：https://www.elastic.co/downloads/beats”。
画面 7: 与画面 1 相同，无新增要点。
画面 8: 与画面 1 相同，无新增要点。
画面 9: 与画面 1 相同，无新增要点。
画面 10: 与画面 1 相同，无新增要点。
画面 11: 在画面 1 的基础上，用红色箭头从 Spooler 指向 Elasticsearch、Logstash、Kafka 和 Redis，明确表示数据流向。
画面 12: 与画面 5 相同，无新增要点。
画面 13: 与画面 1 相同，无新增要点。
画面 14: 与画面 1 相同，无新增要点。

3) 画面中出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
PPT 标题：2.2. 部署与运行
架构图结构：
- Input 1: /var/log/*.log → system.log → Harvester → Spooler → Elasticsearch, Logstash, Kafka, Redis
- Input 2: /var/log/apache2/* → error.log → Harvester → Spooler → Elasticsearch, Logstash, Kafka, Redis
- 在画面 11 中，Spooler 通过红色箭头分别指向 Elasticsearch、Logstash、Kafka 和 Redis。

5) 无。

