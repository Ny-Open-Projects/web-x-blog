# 23.Logstash入门学习之数据发送到Elasticsearch

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\23.Logstash入门学习之数据发送到Elasticsearch【海量资源尽在 ubkz.com】.mp4
- 时长 7分48秒（音频 469s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下我们把数据呢最终呢发送到elag设置中那么前面呢我们只是在控制台上面打印出来啊好那我们来看一下怎么样去做一个发送呢相对还是比较容易的那么我们就需要去添加这样的一个配置啊那么拷贝一下然后呢我们去打开logstates然后呢我们去做一下这个修改那么我们先把它拷贝到我们的下面这个位置来那么我们简单做一些这个处理
[00:29] 把这个处理一下然后呢这个也处理一下那么我们就需要把上面的原来这个output就给它去注释掉吧那么就加一个警号去注释掉好那么这样的话呢我们就已经注释掉了那么注释掉之后呢我们来看一下output的一个输出输出呢我们指向了elite search并且指定了一个host我们的一个这样的一个集群好那么保存退出那么这样的话呢我们这个配置是不是就已经搞定了
[00:59] 那么搞定之后呢我们就可以来启动它了对吧跟我们刚刚启动是一样的好那我们来启动走那么等待它的一个执行好那么现在呢我们来看一下有没有数据写进来呢我们去找到我们的elect search然后呢我们去到概述这个里面啊然后呢我们来看一下那么在这个里面呢我们来看一下failbitfailbit呢已经是现在我们再来刷新一下吧那去我们去不断刷新一下多产生几条数据
[01:28] 然后我们到这个里面再去看一下处理现在这个里面已经是有了那么有日志的输出然后我们到这个里面来看一下这个可能我现在看不到输出我们来刷新一下那么会发现这个里面有个failbit它会failbit我们来看一下那么failbit一个是1月15failbit不是看这个应该我们看logstates看它
[01:56] 那么这个数据这个数据也这个所以也有那么这样我们来浏览一下数据那么我们找到我们的logstate那么这个是不是就是刚刚我们请求的数据呢需要去看一下那么现在是五条数据五我看啊16条命中那我们来再刷新几次看一下效果那么看他的这个最终的这个情况然后呢我们等待他得等待一会儿因为他要稍微处理一下
[02:27] 然后我们刷新一下那么发现数据是不是变多了现在是不是有25条数据那么也就是说我们这个数据它其实已经就重新的是不是就写入进来了对吧OK好那么我们简单的我们来看一下这个里面就它的一些请求的数据那么我们看到这个内容其实就知道这个就是index的一个日志的数据好那么现在我们是不是已经就
[02:54] 把数据写入到elac设置中了那么接下来我们是不是就可以在我们的kbana中去做一个查看呢我们来一起看一下那么怎么样去做查看呢我们还是去进入的kbana好来看一下那么我们到这个里面去去发现一下去查找一下那么我们先去添加我们的一个所以那么我们再来去添加一个create创建一个
[03:21] 然后我们去找一下logstatelogstate那就是它对吧logstate然后来个logstate新做一个匹配然后下一步然后我们选择依然选择time time stamp去作为我们的一个时间过滤的条件走然后创建所以创建完成之后在这个里面就可以去查看数据了我们来看一下我们这个里面没有
[03:50] 我们需要刷新一下他可能现在这个地方没有没看到刷新一下然后我们下拉看一下在这个下面有一个logstate就他我们选择他然后来看一下我数据那么这个是不是就是刚刚我们所请求数据总数是25对吧然后我们可以多刷新几次看效果多刷新刷新然后我们回到这个里面来刷新一下看总数25现在可能数据还没来还没有来
[04:23] 那么我们就给他这个时间四小时也行哎OK那么是不是有新的这个请求来了对吧是在0.0.05分的时候然后呢去有20个这样的一个请求OK好嘞好那么我们现在数据是不是就已经可以去在我们的K8当中是不是去查看到这样的一个数据了那么其实基于这个数据啊我们也可以去设置一些我们的一些这个图形化的一些图形化的一些转性啊
[04:52] 就是我们的一些比如说设置一个柱形图对吧那么怎么样设置呢是在这个可视化里面那么我们就可以去在这个位置呢我们去点击这个添加添加一个什么呢添加我们的一个这个柱形图然后呢选择我们的一个这个索引那么选择这个logstate然后呢这个注意他这个他的一个X轴这个是Y轴Y轴呢是一个count就是我们的数量
[05:20] 那我们需要去设置一个X轴那么X轴呢我们就给他我们就选择一个我们的一个时间吧作为我们的一个这个X轴然后呢我们去做一个运行那么这样的话会发现是不是有住行图是不是就出来了你可以看到啊在这个点有25这个点呢有20然后呢我们可以再刷新一次刷新刷新刷新那么一会儿呢我们可以来看一下它的一个这个效果那么我们大家也可以去
[05:49] 哎现在这个是不是就来了这个就来了啊那么还可以去做一些这个刷新然后呢呃我们来看一下那么他有一些这个其他参数啊我们可以调一下比如说呃这个设置为这个烂那么看一下效果会怎么样哎是这样是不是这样的一个趋势啊这样的一个效果那么这个呢是我们来看一下是这样的一种啊这样的展现方式呃然后呢呃还有呢就是呃常规的就是这样的一种展现方式啊ok好那么我们呃也可以呢去给他
[06:19] 把这个保存下来做一个税务保存比如说叫我的我的一个这个住行图住行图然后呢他呢去显示的是不是就是我们的ngx的日志OK好了那么我们做一个保存那保存之后呢我们就可以在我们在我们这个可视化里面直接去找到他比如说我们就找一下谁呢找一下这个ngx那么去搜索一下
[06:52] 那么在下面呢到下一页你可以看到是不是我们刚刚所保存的这个我们的一个这个图表呢就保存在这里了点击它就可以打开那么打开之后呢就可以看到我们刚刚的这个数据了当然我们现在数据比较少那么如果数据比较多的话就可以看到比较好看的一个这样的一个效果了OK好那么当然你可以也可以设置颜色颜色也可以的那么我们比如设置一个这个紫色好那么就是这样的一个效果
[07:19] OK那么大家的其他的就类似了做饼图的还是做其他图就非常类似了好那么当我们其实把我们的索引添加到我们的这个KBAN的中呢就可以去添加各种各样的一些这个图表出来然后呢就可以去去创建各种各样的一些DESPOT的就这样的一个这个效果了OK好那么关于我们的最后一个这个点呢就是我们把数据发送到ELAC设置中那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何配置 Filebeat 将 Nginx 访问日志发送到 Logstash，再由 Logstash 处理后写入 Elasticsearch，并在 Kibana 中进行数据可视化。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中关于“5.3.5、发送到Elasticsearch”的配置说明，其中包含 Filebeat 配置文件 `haoke-pipeline.conf` 的部分内容，用于定义输入源（port 5044）和过滤规则（grok）。
画面 2: 展示终端中 Logstash 启动后因错误（`[ERROR] org.logstash.Logstash`）而终止，提示用户检查配置文件。
画面 3: 展示 Elasticsearch Head 插件的空白页面，表示尚未进行任何操作。
画面 4: 展示 Elasticsearch Head 插件中集群状态为绿色（26 of 26），并列出多个索引及其状态，包括 `metricbeat-6.5.4`、`haoke`、`filebeat-6.5.4` 等。
画面 5: 展示 Elasticsearch Head 插件中索引列表，包含 `logstash-2019.01.15`、`metricbeat-6.5.4`、`haoke` 等索引及其文档数量。
画面 6: 展示 PDF 文档中关于“5.3.5、发送到Elasticsearch”的配置说明，其中包含 Logstash 配置文件 `logstash.conf` 的部分内容，用于定义输出到 Elasticsearch 的 hosts。
画面 7: 展示 Kibana 的“Create index pattern”页面，正在创建索引模式。
画面 8: 展示 Kibana 的 Discover 页面，显示搜索结果，包含字段如 `@timestamp`、`beat.name`、`host.name`、`metricset.name`。
画面 9: 展示 Kibana 的 Discover 页面，时间范围设置为“Last 4 hours”，并显示数据。
画面 10: 展示 Kibana 的“Select visualization type”页面，提供多种可视化类型选择。
画面 11: 展示 Kibana 的“New Visualization”页面，配置了“Date Histogram”图表，X轴为 `@timestamp`，Y轴为 Count。
画面 12: 展示 Kibana 的“Save visualization”弹窗，标题为“New Visualization”。
画面 13: 展示 Kibana 的“New Visualization”页面，图表显示数据，鼠标悬停在柱状图上显示“Count 35 @timestamp per 5 minutes 00:05”。
画面 14: 展示 PDF 文档中关于“5.3.5、发送到Elasticsearch”的配置说明，其中包含 Filebeat 配置文件 `haoke-pipeline.conf` 的部分内容，用于定义输入源（port 5044）和过滤规则（grok）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
input {
  beats {
    port => "5044"
  }
}

filter {
  grok {
    patterns_dir => "/haoke/logstash-6.5.4/Nginx-patterns"
    match => { "message" => "%{NGINX_ACCESS}" }
    remove_tag => ["_grokparsefailure"]
    add_tag => ["nginx_access"]
  }
}
```

画面 6:
```
output {
  Elasticsearch {
    hosts => ["192.168.1.7:9200","192.168.1.7:9201","192.168.1.7:9202"]
  }
}
```

画面 14:
```
input {
  beats {
    port => "5044"
  }
}

filter {
  grok {
    patterns_dir => "/haoke/logstash-6.5.4/Nginx-patterns"
    match => { "message" => "%{NGINX_ACCESS}" }
    remove_tag => ["_grokparsefailure"]
    add_tag => ["nginx_access"]
  }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 6: PPT 标题为“5.3.5、发送到Elasticsearch”，内容包含 Logstash 配置文件 `logstash.conf` 的输出部分，其中 `hosts` 字段指向 Elasticsearch 的三个节点地址。
画面 7: Kibana 页面标题为“Create index pattern”，提示“Kibana uses index patterns to retrieve data from Elasticsearch indices for things like visualizations.”。
画面 8: Kibana Discover 页面显示搜索结果，包含字段如 `@timestamp`、`beat.name`、`host.name`、`metricset.name`。
画面 9: Kibana Discover 页面显示时间范围为“Last 4 hours”，并显示数据。
画面 10: Kibana 页面标题为“Select visualization type”，提供多种可视化类型选择。
画面 11: Kibana 页面标题为“New Visualization”，配置了“Date Histogram”图表，X轴为 `@timestamp`，Y轴为 Count。
画面 12: Kibana 页面标题为“Save visualization”，弹窗标题为“New Visualization”。
画面 13: Kibana 页面标题为“New Visualization”，图表显示数据，鼠标悬停在柱状图上显示“Count 35 @timestamp per 5 minutes 00:05”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

