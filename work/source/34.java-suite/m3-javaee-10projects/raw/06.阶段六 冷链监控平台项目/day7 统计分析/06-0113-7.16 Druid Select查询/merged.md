# 7.16 Druid Select查询

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.16 Druid Select查询_【海量资源尽在 666java.com】.mp4
- 时长 3分45秒（音频 225s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们来看看Droid的查询中的Select查询Select查询和我们的Search查询比较类似但是Select查询它是返回原始的Droid行并且支持分页我们知道Search的话它返回的并不是原始的数据行对不对那么Select它返回原始的数据然后支持一个分页我们看一看它的一个字段QueryType它的这个类型是Select
[00:26] 然后DataSource是表的名字Filter指的是过滤条件Descending是表示我们当前查询的结果是否进行排序Dimension的话指的是我按搜索的条件也就是说我如果是查询条件是什么然后呢我如果搜索字段是两个字段的我要设置两个字段那么我们只会在这两个字段内查询是否符合条件的这个搜索那么如果不设置的话那就会查询所有的这个字段
[00:53] Graduality指的是我们聚合的时间力度我反回的聚合力度Interval的话指的是我们查询的时间范围Magic指的是我们要选择的度量的字符帅的一个数组那么如果我空它就反回所有的一个度量Paging的一个spec是一个JSON的一个对象它表示我们的一个分页是一个扫描段的一个偏移量
[01:21] 像context的话可能就是一个附加的一个基层对象指定某些标识上下文等等这样的一个条件那我们来看一看我们的这个例子我们这个例子里边来讲的话是首先我们的query type就是我们的select然后我们datasource呢是我们的wikimedia然后呢deciding的话指的是我们是否就用排序不排序然后dimension那么是微空那就是查询所有的这个所有的这个字段
[01:51] 那么matrix也是尾空而且时间的力度是是一个小时查询时间周期啊就12号到13号那么它的分页的话是有是每页有失调记录然后呢执行分页从第一个开始啊这是这么一个那么我们来看一看我们整个在postman里面执行效果是什么样的ok它得到了我们的按小时来查询的一个数据是失调失调的话它是
[02:24] 查询了所有的字段返回所有的字段返回所有字段中的这个数据这个数据是按照分区分区ID然后事件这样的来查询的它是得到我们查询的一个结果那个类似于这种select比如说我们的这个我们这个什么呢比如说我们的dimensiondimension的话指的是我select某个字段某个字段那个如果不设置的话就是select新了对不对然后是这样的一个情况那么
[02:54] 大家需要注意的一点是我们建议的是用scan来查询而不建议用select查询select的话如果大量的数据分段的这种情况下select查询可能有比较高的内存和性能开销那么scan的话它虽然没有分页但是scan就是这种扫描这种查询它没有数据量的一个无限量的一个数据
[03:23] 所以说一方面最主要的是我们用Select可能会存在一个内存和性能的一个消耗消耗比较严重所以说一般情况下会建议我们建议使用的是Scan这种查询Scan查询我们下面会给大家详细的介绍这是我们的这种Select

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Druid 查询中的 Select 查询语句结构、参数说明及与 Scan 查询的区别，并通过 Postman 发送请求演示实际效果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Druid 官方文档中 1.7.6.2 Select 查询章节，列出 queryType、dataSource、filter、descending、dimensions、granularity、intervals、metrics、pagingSpec、context 等字段的描述及是否必填。
画面 2: 展示 Select 查询示例 JSON，包含 queryType、dataSource、descending、dimensions、granularity、intervals、pagingSpec 等字段。
画面 3: 展示 Select 查询示例 JSON，补充了 intervals 字段的具体时间范围值。
画面 4: 展示 Select 查询示例 JSON，完整包含 pagingSpec 字段，并在下方添加注意事项，说明 Select 查询在大数据量下可能内存溢出，建议使用 Scan 查询。
画面 5: 展示 Select 查询示例 JSON，光标位于 intervals 字段的时间范围值上。
画面 6: 在 Postman 中构造并发送一个 POST 请求，请求 URL 为 http://172.17.0.143:8888/druid/v2，请求体为 JSON 格式，包含 queryType、dataSource、query、sort、intervals 等字段。
画面 7: 在 Postman 中，光标位于请求体的 intervals 字段上，该字段值为 ["2015-09-12T00:00:00.000Z", "2015-09-12T00:00:00.000Z"]。
画面 8: 在 Postman 中，请求体中添加了 pagingSpec 字段，值为 {"pagingIdentifiers": {}, "threshold": 10}，并发送请求。
画面 9: 展示 Druid 官方文档中 1.7.6.3 Scan 查询章节的开头部分，介绍 Scan 查询的特点。
画面 10: 展示 Druid 官方文档中 1.7.6.3 Scan 查询章节的完整内容，说明 Scan 查询与 Select 查询的区别，以及 Scan 查询可以返回分页结果。
画面 11: 展示 Druid 官方文档中 1.7.6.2 Select 查询章节的表格，列出字段名、描述、是否必填。
画面 12: 展示 Druid 官方文档中 1.7.6.3 Scan 查询章节的完整内容，包括 Scan 查询的定义、特点和使用场景。
画面 13: 展示 Druid 官方文档中 1.7.6.2 Select 查询章节的表格，列出字段名、描述、是否必填。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
{
  "queryType": "select",
  "dataSource": "wikipedia",
  "descending": false,
  "dimensions": [],
  "granularity": "hour",
  "intervals": [],
  "metrics": [],
  "pagingSpec": {
    "pagingIdentifiers": [],
    "threshold": 10
  }
}

画面 2:
{
  "queryType": "select",
  "dataSource": "wikipedia",
  "descending": "false",
  "dimensions": [],
  "granularity": "hour",
  "intervals": [],
  "metrics": [],
  "pagingSpec": {
    "pagingIdentifiers": [],
    "threshold": 10
  }
}

画面 3:
{
  "queryType": "select",
  "dataSource": "wikipedia",
  "descending": "false",
  "dimensions": [],
  "granularity": "hour",
  "intervals": [
    "2015-09-12/2015-09-13"
  ],
  "metrics": [],
  "pagingSpec": {
    "pagingIdentifiers": [],
    "threshold": 10
  }
}

画面 4:
{
  "queryType": "select",
  "dataSource": "wikipedia",
  "descending": "false",
  "dimensions": [],
  "granularity": "hour",
  "intervals": [
    "2015-09-12/2015-09-13"
  ],
  "metrics": [],
  "pagingSpec": {
    "pagingIdentifiers": [],
    "threshold": 10
  }
}

画面 6:
{
  "queryType": "search",
  "dataSource": "wikipedia",
  "query": {
    "type": "inexact",
    "value": "an"
  },
  "sort": {
    "type": "lexicographic"
  },
  "intervals": [
    "2015-09-12T00:00:00.000Z/2015-09-12T00:00:00.000Z"
  ]
}

画面 8:
{
  "pagingSpec": {
    "pagingIdentifiers": {},
    "threshold": 10
  }
}

画面 12:
{
  "queryType": "select",
  "dataSource": "wikipedia",
  "descending": "false",
  "dimensions": [],
  "granularity": "hour",
  "intervals": [
    "2015-09-12T00:00:00.000Z/2015-09-12T00:00:00.000Z"
  ],
  "metrics": [],
  "pagingSpec": {
    "pagingIdentifiers": [],
    "threshold": 10
  }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

