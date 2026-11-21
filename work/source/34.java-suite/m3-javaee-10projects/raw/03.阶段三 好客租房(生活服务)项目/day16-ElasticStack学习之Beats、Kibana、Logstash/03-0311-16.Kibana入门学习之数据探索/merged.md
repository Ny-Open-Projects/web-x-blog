# 16.Kibana入门学习之数据探索

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\16.Kibana入门学习之数据探索【海量资源尽在 ubkz.com】.mp4
- 时长 4分25秒（音频 265s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么下面我们就来了解一下KBAN所提供的一些功能那么下面这个图是它的菜单的一些描述然后去标注了一些中文那么首先可以看到它有什么叫数据的探索那么就是可以通过界面的形式来查看我们已来的设计中的一些数据然后可以做一些可视化的一些查看一表盘的时序空间的画布的经济学习的等等一些这个内容
[00:29] 那么我们可以大致的来点一下包括第一个你可以我们去去浏览这个数据一会我们来讲一下它然后可视化去创建一些我们的一些图表还有些DESPOD等等因为现在我们还没有去设置所以现在我们什么都看不了大致的可以去点一下然后这个也是对吧也是可以去做一些这种时间时间时序的这样的一些这样的一些展现然后这个是
[00:56] 比较炫的这样的一个这样的一个画布是吧OK然后这个是一些机器学习相关的一些内容这个就不一个去点了那么来看一下这个是一个开发者工具这个可以说一下就是我们可以在这个位置去写我们的查询语记然后我们去再点击执行那么就可以查询我们的数据那么也是非常方便的这样的一个工具
[01:21] 也可以去使用一下然后最后这个是一个management就是一些管理OK好那么接下来我们就来说一下这个数据的探索那么我们来看一下那么在这个里面那么我们会发现我们现在并没有去添加我们的一个索引所以首先需要去创建一个索引的一个patent那么你可以点击这个位置然后去创建点击这个new创建也可以点击这个management
[01:47] 然后点击这个位置去做一个创建都是一样的好的我们来看一下现在我们可用的有三个有三个那么我们可以比如说把这个matchbit的去拿过来对吧然后我们来一个更新好然后我们是不是匹配到一个点击这个下一步然后我们去选择一个时间选择一个时间作为它的一个filterfilter的一个字段可以看到是不是name filter
[02:16] 在timefield去做一个这样的过滤然后我们点击这个create就可以了那么现在它就创建成功那么创建成功之后我们就可以在这个位置去查看通过我们可视化界面的方式去查看我们的数据那么点击一下它然后现在没有数据吗应该是有我们来看一下刷新一下这个里面
[02:52] 好那么我们来继续刚刚没有数据是原因是我们这个时间设置有问题我们来看一下那么在上面这个位置可以去做一些筛选就筛选我们需要查看数据的一个时间你比如说我最近15分钟那么他就没有数据那么如果我给他选择比如最近4小时那么就会看到他已经有数据了通过这种方式就可以做一个展现对吧你比如说我们的这是一条条数据然后我们还可以去添加一些显示的字段
[03:21] 你比如说我们把这个bit name去添加过来那么是不是可以以这种图表这种表格的形式去做一个展现你比如说我们把这个host name添加过来OK然后还可以去添加一些就是我们的指标的一些名称对吧把它去添加过来这样的话是不是也是OK的那么通过这种方式是不是也是可以去查看我们的一些数据查看我们数据所以说这个就是一些
[03:50] 数据探索那么通过可视化的方式去做查看要比我们在这个里面去这样去查看是比较好好很多对吧那么我们来看一下比如说在这个里面去查看那么数据有这么多是不是肯定没有这样是不是要方便OK那么我们还是可以去选择一些查询的一些时间比如说我们选择最近30分钟怎么样的一些数据就可以去做一些展现OK好那么这个就是它的一个
[04:18] 这个数据探索的一些基本的一些这个使用好那么关于这个功能的一些这个使用我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Kibana 中创建索引模式并进行数据探索，包括使用 Dev Tools 执行查询、查看指标数据和可视化图表。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 讲义中关于 Kibana 功能说明的章节，右侧是 Kibana 界面截图，标注了主要功能模块：Discover（数据探索）、Visualize（可视化）、Dashboard（仪表盘）、Timelion（时序控件）、Canvas（画布）、Machine Learning（机器学习）。
画面 2: Kibana 界面，位于“Management / Kibana”下的“Create index pattern”页面，提示需要创建索引模式以可视化数据，页面正在“Checking for Elasticsearch data”。
画面 3: PDF 讲义中关于“4.4、数据探索”的章节，右侧是 Kibana 菜单截图，标注了功能模块：Dashboard（仪表盘）、Timelion（时序控件）、Canvas（画布）、Machine Learning（机器学习）、Infrastructure（基本信息）、Logs（日志数据展现）、APM（性能监控）、Dev Tools（开发者工具）、Monitoring（监控）、Management（管理）。
画面 4: Kibana Dev Tools 控制台，执行了 GET /_search 查询，返回结果中包含索引信息，如 "_index": "kibana_1", "_type": "doc", "space": { "name": "Default", "color": "#000000" }。
画面 5: Kibana 界面，位于“Management / Kibana”下的“Create index pattern”页面，提示需要创建索引模式以可视化数据，页面正在“Checking for Elasticsearch data”。
画面 6: Kibana 界面，位于“Management”页面，显示了 Elasticsearch 和 Kibana 的管理选项，包括 Index Management、Rollup jobs、License Management、Index Patterns、Saved Objects、Spaces、Reporting。
画面 7: Kibana 界面，位于“Management / Kibana”下的“Create index pattern”页面，提示“Create index pattern”，并显示“Creating index pattern...”。
画面 8: Kibana Discover 页面，选择“metricbeat*”索引，点击“Refresh”按钮，页面显示“Searching”状态。
画面 9: Kibana Discover 页面，显示“metricbeat*”索引的数据，包含时间戳和 source 字段内容。
画面 10: Kibana Discover 页面，显示“metricbeat*”索引的数据，右侧出现柱状图，显示按时间分组的计数。
画面 11: Kibana Discover 页面，显示“metricbeat*”索引的数据，右侧出现列表，包含字段如 network、load、process、info、cpu。
画面 12: Elasticsearch Head 界面，显示集群中各个节点（node01, node02, node03）的索引分布情况，每个节点对应不同的索引。
画面 13: Kibana Discover 页面，显示“metricbeat*”索引的数据，右侧出现柱状图，显示按时间分组的计数。
画面 14: PDF 讲义中关于“4.5、Metricbeat 仪表盘”的章节，右侧是 Kibana Discover 页面截图，显示了数据和图表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
```json
{
  "took": 35,
  "timed_out": false,
  "_shards": {
    "total": 12,
    "successful": 13,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 50822,
    "max_score": 2.0,
    "hits": [
      {
        "_index": "kibana_1",
        "_type": "doc",
        "_source": {
          "space": {
            "name": "Default",
            "color": "#000000",
            "reserved": true
          },
          "type": "space",
          "updated_at": "2019-01-15T14:07:25.532Z"
        },
        "_index": "kibana_1",
        "_type": "doc",
        "_id": "config6.5.4"
      }
    ]
  }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“4.3、功能说明”，右侧截图标注了 Kibana 的功能模块。
画面 3: PPT 标题为“4.4、数据探索”，右侧截图标注了 Kibana 的功能模块。
画面 14: PPT 标题为“4.5、Metricbeat 仪表盘”，右侧截图显示了 Kibana Discover 页面。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

