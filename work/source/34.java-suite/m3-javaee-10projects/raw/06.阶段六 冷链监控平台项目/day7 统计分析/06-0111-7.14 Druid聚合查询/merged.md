# 7.14 Druid聚合查询

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.14 Druid聚合查询_【海量资源尽在 666java.com】.mp4
- 时长 11分10秒（音频 670s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面我们来看一看JED它的一个聚合查询我们知道JED数据库它是一个实序数据库实序数据库里边我们需要对它进行一些聚合的一个统计包括对某一些字段的一个求和或者说是求平均值或者求所有的这种数学计算包括数学计算类的一些东西那么是基于时间维度来进行的那么这种聚合来讲的话
[00:30] 好多类那么主要包括那么三大类吧一类的话是叫做叫做Time SerialTime Serial的话它是对于某一段时间内的数据的一个汇总这样的一个查询我们看一看聚合查询中Time Serial它的一个数据的一些字段那首先的话是有一个叫Query Type那么Query Type的类型当前肯定是就是Time Serial
[00:58] 那么DataSource就是我们要查询的数据库的数据的一个集或者叫表结构表的名次那么Descending的话指的是是否是降序我们是否把结果按照降序来进行排列那另外一个字段的话叫做Graduality实际上就是我们进行聚合的时间力度还有一个的话是属于我们的时间范围而这个时间范围它需要符合我们是RSO的
[01:28] 8601这种格式那filter的话就是我们过滤条件了aggregation其实就是聚合的一个指标聚合的字段post这种aggregation是指的是聚合后的聚合也就是说我根据结果我开始的时候是有些字段我把字段进行聚合聚合之后我按照聚合之后的两个字段直相加
[01:53] 或者是两个自然值进行相除啊或者是进行平均值啊等等这种聚合叫做后聚合啊就是post post aggregation那还有一个的话就是contextcontext实际上是我们上下文上下文的话它会可以指定一些参数我们来举个例子还是我们的wikipedia
[02:13] VP.这个数据库这个数据库的表的结构我们前面已经介绍过了我们来看看这个查询的这个查询的条件那查询条件来讲的话query就是time server然后datasource呢就是表结个名字然后interval就是我们的查询的时间的间隔我们在这个时间段内的数据我们对它进行查询然后聚合的力度呢我们在
[02:36] 统一的在所有的数据进行聚合也就是说我会得到一个数据结果集那么我们的进行聚合的post aggregation呢我们不对呃呃为空设置为空就是不进行这种后聚合那么我们的聚合呢是把啊count这个字段来进行求和那么我们把这个条件拷贝到我们的poster man里边poster man的我们poster man的条件换你来
[03:07] 然后我们点击send它是post的一个方式对吧那此时它会得到我们所有的记录的这种count的求和了对不对我们可以看到我们的这个count有很多条记录嘛对不对这很多条记录的我们要把count进行求和这个就是我们的aggregation当然了这个type的话可能还包括好多种一个是count或者说是包括这个average
[03:34] 他三模啊等等这些的话可能都是我们要进行数据类型的一个求和求和的一个数据类型那如果是我们要进行比如说按按D或者是按R我们可以看看到如果按R的话它会有多条啊那么比如说我在这的时候我从12点的时候1点的时候1点就12点到1点这个范围内我的UV count是是是这些那么1点到
[04:06] 两点零点的时候有这样的数据然后一点的时候有这样的数据然后两点的时候它的数据数据求核是什么然后三点的时候数据求核是什么这个时候它其实取的就是一个我们的hour那如果是我们的minute呢那就就是按分钟了对不对如果是second呢就是按秒来聚合了那其实就可能就是没有聚合了或者说是聚合的数量就比较小了
[04:35] 这个是实际上是这个数据的聚合力度的这样的一个值OK那我们再看第二种的聚合查询第二种的聚合查询就是叫Top N所谓Top N的话是指我们按照某一个指标求取它的一个前几位前几条
[04:58] 举个例子来讲的话我们所有的数据啊所有的页面我们电商网站或者我们的网站里边的有很多个页面而每个页面呢它有一些点击那么我想查看一下过去一小时之内我们的某哪些页面它点击率最高或者说哪些页面的点击率是排在前五位的啊这个这种叫的叫的这种这种这个套奔那套奔的话它指定了它
[05:24] 如果我们查询TOPN的话它返回的是什么呢我们如果给指定了这种维度和排析字段那么我们就返回前一条这种记录它的字段包括我们的query type这query type就是TOPN了那DataSource和我们的Serial就是时间时间的这种去和查询是一样都是叫表的名字对吧
[05:44] interval就是时间范围,filter就是过滤条件aggregation就是聚合的哪一个字段进行聚合posteraggregation就是聚合后的聚合dimension指的就是维度了threshold实际上就是top10中的音质也就是说我要查询top10,top5我可以给threshold来设置这个值
[06:08] matrix的话实际上是统计并排序的一个指标context和我们的前面是一样的就是一个上下围的一个查询参数那么我们看一下我们这个事例这个事例的话query type就是topA然后我们的表名字叫wikipedia然后时间范围是12号的13号的然后查询的力度实际上是所有的all然后查询的指标呢是查询的page然后我们进行聚合的维度的话是按照account来解决的
[06:37] 来查的那么我们查询前十条那进行聚合的话是针对于count的count也就是说我们针对于count这个名字就叫count嘛字段的名字叫count但是我们的类型是要进行统计那么我们来执行一下我们的这个看看我们这个效果我们在postman里边还是把条件拷贝过来那我点一下sendok那此时的话它会
[07:06] 根据我们的查询然后查询了前10条前10个并且进行了一下排序那第一个来讲的话这个配置就是就叫就就是就是这个就是这个嘛对不对那他的counter是实际上是30我们可以在我们的这里边来query里边来查询where where配置等于等于这个值ok这个里面一共有有多少个你看现在是三页对吧
[07:40] 然后实际上如果是说50行50行的话一共是我们还是按11页11页的话一页是失调记录一页失调记录它其实就有那么三页对吧每页是10个所以说加一块的话是3030这样的一个字段第三页的话应该是我看看前面是每个都是1第三页的话应该是没有应该是9个
[08:10] 9个来讲的话加一块中间有一个是12所以加一块应该是30结果是30的这样的一个那如果是这个呢我们看最后一个最后一个的话我们如果配置等于它的时候它应该是15它的求和的这个值求count的这个值应该是15OK它是两页两页来讲的话第一页是10条第二页的话5条对吧所以说加一块的话正好是15个
[08:41] 这是我们的啊球我们针对于啊topo n的那么他进行了一个排序他取的他的时间力度实际上是是all的对不对我们当然我们也可以按照时间力度是这个hour按小时来进行聚合来进行查询那小时的查询来讲的话那就是每小时中的我要取30个比如说第一个第一个小时零点的零点的来讲的话他可能是3111a
[09:12] 是吧那到了一点的时候呢一点的时候他查询的这个按照相同的配置相同的页面的时候相同页面的他查询的那么就是这几个页面是前十位的那到了两点的时候又变成另外的时刻了对吧这是不同的查询力度以查询力度下的这种套牌都返回的一个结果那我们再看第三类的叫group by
[09:39] group by的话和circuitg的group by也是比较类似是一样的就是我们按照某一个字段进行一个分组按照多个维度进行分组那么它的一个查询的字段字段的值比如说我们的query typequery type的话这个字段值必须叫group by对吧datasource就是表的名字dimension就是我们维度的一个集合limit spec就是统计结果是否进行一个排序的一个
[10:06] 那么它的这个值呢也不是一个必须的然后having的话我们是对同期结果是否进行一个筛选然后我们的时间力度甚至于我们的后续和弃包括我们的查询时间范围这些东西其实都比较都比较类似的一个情况了我在这里边刚才因为刚才的时候我们在进行查询的时候开始也介绍过了所以说在这里边不做额外的一个处理了
[10:34] 那所以我们来回过头来来看一看我们的这个聚合查询啊所谓聚合查询就是说我按照某一些条件来查询查询之后呢我要得到按照某一些字段或者说某一些指标来返回我的结果那么当然这个情况就有一个叫聚合的力度的问题对吧我按照每天的或者按照每小时或者按照每分钟的来进行聚合聚合得到我们想要的一个结果无论是
[11:03] 呃时间序列的一个还是说我按照topoing的或者说我按照分组的啊这是我们的这个聚合查询

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Apache Druid 的聚合查询（Timeseries）、TopN 查询和 groupBy 查询的语法结构、参数说明及实际请求示例。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Druid 文档中 1.7.5.1 Timeseries 查询的字段说明表，包括 queryType、dataSource、granularity、intervals、filter、aggregations、postAggregations、context 等字段及其是否必需。
画面2：在 Postman 中构造一个 Timeseries 查询请求，JSON 请求体为：
{
  "queryType": "timeseries",
  "dataSource": "wikipedia",
  "granularity": "hour",
  "intervals": [
    "2015-09-12T00:00:00.000Z",
    "2015-09-12T01:00:00.000Z"
  ],
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}
画面3：Postman 中 Timeseries 查询的响应结果，包含两个时间戳和对应的 count 值。
画面4：展示 Druid 文档中 1.7.5.2 topN 查询的字段说明表，包括 queryType、dataSource、intervals、filter、aggregations、postAggregations、dimension、threshold、metric、context 等字段及其是否必需。
画面5：在文档页面中，鼠标悬停在 "metric" 字段上，显示其描述为“进行统计并排序的metric”。
画面6：在 Postman 中构造一个 topN 查询请求，JSON 请求体为：
{
  "queryType": "topN",
  "dataSource": "wikipedia",
  "intervals": [
    "2015-09-12T00:00:00.000Z",
    "2015-09-12T01:00:00.000Z"
  ],
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}
画面7：在 Apache Druid 的 Web UI 中，执行 SQL 查询 "select * from wikipedia"，返回多行数据，包含 _time、channel、cityName、comment、count 等字段。
画面8：在 Druid Web UI 中，执行 SQL 查询 "select * from wikipedia where page = 'Wikipedia:VandalismCidong'"，返回 3 行数据。
画面9：在 Druid Web UI 中，执行 SQL 查询 "select * from wikipedia where page = 'Wikipedia:VandalismCidong'"，滚动查看第 2 页数据。
画面10：在 Druid Web UI 中，执行 SQL 查询 "select * from wikipedia where page = 'Anthony Mantial'"，返回 1 行数据。
画面11：在 Postman 中，显示一个查询响应，包含多个 count 和 page 字段，如 "count": 19, "page": "Fanie Pometta"。
画面12：在 Postman 中构造一个 lookup 查询请求，JSON 请求体为：
{
  "queryType": "lookup",
  "dataSource": "wikipedia",
  "intervals": [
    "2015-09-12T00:00:00.000Z",
    "2015-09-12T01:00:00.000Z"
  ],
  "granularity": "hour",
  "descending": true,
  "metric": "count",
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}
画面13：展示 Druid 文档中 1.7.5.3 groupBy 查询的字段说明表，包括 queryType、dataSource、dimensions、limitSpec、having、granularity、postAggregations、intervals、context 等字段及其是否必需。
画面14：在文档页面中，鼠标悬停在 "dimensions" 字段上，显示其描述为“进行GroupBy查询的维度集合”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2：
{
  "queryType": "timeseries",
  "dataSource": "wikipedia",
  "granularity": "hour",
  "intervals": [
    "2015-09-12T00:00:00.000Z",
    "2015-09-12T01:00:00.000Z"
  ],
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}

画面3：
{
  "timestamp": "2015-09-12T00:00:00.000Z",
  "result": {
    "count": 266
  },
  "timestamp": "2015-09-12T01:00:00.000Z",
  "result": {
    "count": 133
  }
}

画面6：
{
  "queryType": "topN",
  "dataSource": "wikipedia",
  "intervals": [
    "2015-09-12T00:00:00.000Z",
    "2015-09-12T01:00:00.000Z"
  ],
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}

画面11：
{
  "count": 19,
  "page": "Fanie Pometta",
  "count": 17,
  "page": "Wikipedia:In the news/Candidates",
  "count": 17,
  "page": "Wikipedia:Benefits for page protection",
  "count": 16,
  "page": "Wikipedia:Administrators intervention against vandalism",
  "count": 15,
  "page": "Anthony Mantial"
}

画面12：
{
  "queryType": "lookup",
  "dataSource": "wikipedia",
  "intervals": [
    "2015-09-12T00:00:00.000Z",
    "2015-09-12T01:00:00.000Z"
  ],
  "granularity": "hour",
  "descending": true,
  "metric": "count",
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：标题为“1.7.5 聚合查询”，子标题“1.7.5.1 Timeseries”，下方为字段说明表。
画面4：标题为“1.7.5.2 topN”，下方为字段说明表。
画面13：标题为“1.7.5.3 groupBy”，下方为字段说明表。
画面14：标题为“1.7.5.3 groupBy”，下方为字段说明表，同时显示“1.7.6 搜索查询”标题。

5) 无。

