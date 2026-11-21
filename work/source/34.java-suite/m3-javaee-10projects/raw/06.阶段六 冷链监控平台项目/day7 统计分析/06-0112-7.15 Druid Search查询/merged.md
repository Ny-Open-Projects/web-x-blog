# 7.15 Druid Search查询

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.15 Druid Search查询_【海量资源尽在 666java.com】.mp4
- 时长 7分19秒（音频 439s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面我们来查询Apache Dread它的一个设置查询设置查询返回的是符合我们设置查询条件的一个查询结果那么我们来看一看这个查询条件里边包含了有哪些字段第一个字段来讲的query type这个大家应该都能理解它就是我们的一个查询类型查询类型对于设置查询那么这个字段的值必须就是设置了那么Data Source就是要查询的数据集的表的名字 对吧
[00:28] 那么filter的话指的是我查询的一个过滤条件limit我也查询的返回的数据结果数量那这个字段默认是100如果是不提供的话如果不提供这个字段的话它的默认值是1000那么search dimension的话是指的话搜索的维度那么如果我们不搜索不设置这个选项的话那么它搜索所有的这个维度
[00:56] 那举个例子来讲的话假设我的数据库的这个表里边这个表里边有那么十个字段那么十个字段的话假设我要搜索条件我是搜索某某等于搜索某个字段某个某个这个字符串那么此时如果我设置搜索维度的时候那它只是在这两个字段里边假设我设置两个搜索维度
[01:17] 那么我只是在这两个搜索的维度上我查询这个字符算那么如果我不设置这个搜索维度那么我就会在所有的字段里面都搜索是否包含这个字符算那么时间力度granularity其实前面大家应该都应该了解了我按照什么时间来返回结果我按照天的还是按照小时的或者按照年甚至按照月这样的
[01:45] 查询条件肯定就是我们search的一个主要的搜索条件了这是必须的一个字段那么intervals的话指的是我们的查询的时间范围sort的话是我们要对搜索结果进行排序context的话一般不大用用的话也就上下文的查询这些参数传过来的我们看一看我们query的这种类型包含什么也就是说虽然是query但是query是有好多种的
[02:13] 一种来讲的话叫做insensitive的content也就是非敏感包含的如果我们的查询维度里边要查询某一个字段要查询某一个字符段那么如果我设置它的query的类型是insensitive的content那个content是包含对不对insensitive指的是那个非敏感也就是说我查询abc
[02:40] 那如果是大写的ABC小写的ABC甚至中间有大写有小写的ABC那我都会把它结果当做命中了当做查询出来的这就是非敏感包含的那还有一个第二类的话是指的是FragmentFragment来讲的话是指如果维度值的任何部分包含了搜索条件搜索查询规范中指定的值无论默认情况如何都会满足匹配
[03:09] 那换句话说我其实是想要的是如果是说比如说我们看下面这个例子下面的例子如果他的查询例型是fragmentfragment的时候如果我们case sensitivecase sensitive指的是忽略大小写是否大小写大小写的话如果他设置false那么我们查询条件里边的这两个字段那么只要满足了只要包含了这两个字两个字不出来
[03:35] 那么我们当天这条记录都会被查询出来的对吧那content的话相对来讲也比较容易理解content是包含的意思对吧包含的话如果是包含同时我们看这个例子是包含类型的然后呢不忽略大小写那么我们查询到某一个值这就是我们的这个content那还有一个正则表达式正则表达式就是说我用正则表达式然后判断某些字段是否
[04:02] 包含什么样的条件啊这就是我们的这个正能表达式基本上来讲的话就是说我的这个进行色试查询的时候我要查询某一个字段是否忽略大小写然后是否是符合等于或者说部分等于某一个字符率这样的就是一个色试查询那么我们来举一个例子这个也是用我们的wikipedia作为色试查询然后查询的力度呢是hour然后
[04:30] 就是说查询返回的一个时间力度实际上叫hour那么我们查询的维度是在channel和city name里面那么我们的假设我们的channel有这些对不对然后呢我们的city name实际上是另外一个字段我们在这两个字段里面查询那么我们查询的一个结果我查询的是insensitive content就是说非什么呢非这种叫做大小写敏感的一个包含
[05:00] 我只要包含了这AR这个字段然后我使用的是这个这种这种排序然后呢我的查询的这个时间范围是这样的一个时间范围那我们来看一看我们的直接的一个执行的一个结果吧OK我在Postman里边把参数传进去然后呢它得到了我们想要的一个结果这个结果的话是首先我们的我们的什么呢
[05:34] 首先我们的是按时间维度来排的0点的时候我得到一个结果是这样的挺多的是吧OKOK这个是有一个时间范围的吧12点到13点0点的时间范围是这个然后在12点的时候它包含了这个那其实是它查询结果如果是这样的情况下那可能就没有一个在12点到1点之间它就没有这个1点
[06:09] 它现在是12点的时候会查询出来的但是1点到2点之间呢应该就没有这个数字了那我们再查询另外的一个字另外的一个字段比如说我要查询1n点我要查询这个结果我不是不查询a2了我查询1n点OK查询1n点的话我只是在这个里边查询到了查询掉了一条我看看查询到了一条一条不对一条的数据是不对的因为它是
[06:45] 我们至少能看到了两个音点对吧两个音点但是他返回结果哦哦哦是这样的是这样的是这样的他是一个求和的一个啊对因为我们在查询的时候我们的聚合的力度是要是需要对他进行一个啊求和求和操作的这个时候的一个外流等于这个然后看他等于这个但是他就这个这个这个结果也是对的啊这是我们的啊
[07:15] 色识的一个插线

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Druid 查询语句中 Search 查询的参数结构、查询类型（如 insensitive_contains、fragment、contains、regex）及实际调用示例，并演示通过 Postman 发送请求和查看返回结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Druid 查询语句中 Search 查询的参数表，包括字段名、描述和是否必填。参数包括：queryType、dataSource、filter、limit、searchDimensions、granularity、query、intervals、sort、context。并说明 queryType 包括 insensitive_contains（非敏感包含）。

画面2：展示 queryType 的三种类型：fragment（片段匹配）、contains（包含）、regex（正则匹配），并给出每种类型的 JSON 语法示例。

画面3：展示一个完整的 Search 查询示例 JSON，包含 queryType、dataSource、granularity、searchDimensions、query、sort、intervals 字段。

画面4：再次展示 queryType 的三种类型及其 JSON 示例，与画面2内容一致。

画面5：展示 queryType 的三种类型及其 JSON 示例，与画面2、4内容一致。

画面6：展示一个完整的 Search 查询示例 JSON，包含 queryType、dataSource、granularity、searchDimensions、query、sort、intervals 字段，并在 intervals 字段中设置了时间范围。

画面7：在画面6的基础上，对 JSON 中的 queryType、dataSource、granularity、searchDimensions、query、sort、intervals 字段进行了高亮显示。

画面8：在 Postman 中发送一个 POST 请求，请求地址为 http://172.17.0.143:8888/druid/v2，请求体为 JSON 格式，内容为：
{
  "queryType": "count",
  "dataSource": "wikipedia",
  "granularity": "hour",
  "query": {
    "type": "count"
  },
  "intervals": [
    "2015-09-12T00:00:00.000/2015-09-13T00:00:00.000"
  ],
  "threshold": 10,
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}

画面9：展示 Postman 返回的 JSON 响应结果，包含时间戳和结果数组，每个结果包含 dimension、value、count 字段。

画面10：展示文档中 1.7.6.2 Select 查询的标题和说明文字。

画面11：展示多个终端窗口，显示 Druid 服务启动日志，包括 coordinator、broker、historical 等组件的启动和退出信息。

画面12：在 Postman 中发送一个 POST 请求，请求地址为 http://172.17.0.143:8888/druid/v2，请求体为 JSON 格式，内容为：
{
  "queryType": "search",
  "dataSource": "wikipedia",
  "granularity": "hour",
  "searchDimensions": [
    "channel",
    "cityName"
  ],
  "query": {
    "type": "insensitive_contains",
    "value": "en"
  },
  "sort": {
    "type": "lexicographic"
  },
  "intervals": [
    "2015-09-12T00:00:00.000/2015-09-13T00:00:00.000"
  ]
}

画面13：展示终端窗口中 Druid 服务启动日志，包括 coordinator、broker、historical 等组件的启动和退出信息。

画面14：展示文档中 1.7.6.2 Select 查询的标题和说明文字，与画面10内容一致。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
queryType
dataSource
filter
limit
searchDimensions
granularity
query
intervals
sort
context

参数query的type类型包括：
• insensitive_contains：非敏感包含

画面2：
• fragment：如果维度值的任何部分包含此搜索查询规范中指定的值，则无论默认情况如何，都会满足“匹配”
{
  "query": {
    "type": "fragment",
    "case_sensitive": false,
    "values": ["fragment1", "fragment2"]
  }
}

• contains：如果维度值的任何部分包含搜索查询规范中指定的值，则满足“匹配”。
{
  "query": {
    "type": "contains",
    "case_sensitive": true,
    "value": "some_value"
  }
}

• regex：正则匹配
{
  "query": {
    "type": "regex",
    "pattern": "some_pattern"
  }
}

画面3：
{
  "queryType": "search",
  "dataSource": "wikipedia",
  "granularity": "hour",
  "searchDimensions": [
    "channel",
    "cityName"
  ],
  "query": {
    "type": "insensitive_contains",
    "value": "en"
  },
  "sort": {
    "type": "lexicographic"
  },
  "intervals": [
    "2015-09-12T00:00:00.000/2015-09-13T00:00:00.000"
  ]
}

画面6：
{
  "queryType": "search",
  "dataSource": "wikipedia",
  "granularity": "hour",
  "searchDimensions": [
    "channel",
    "cityName"
  ],
  "query": {
    "type": "insensitive_contains",
    "value": "en"
  },
  "sort": {
    "type": "lexicographic"
  },
  "intervals": [
    "2015-09-12T00:00:00.000/2015-09-13T00:00:00.000"
  ]
}

画面8：
{
  "queryType": "count",
  "dataSource": "wikipedia",
  "granularity": "hour",
  "query": {
    "type": "count"
  },
  "intervals": [
    "2015-09-12T00:00:00.000/2015-09-13T00:00:00.000"
  ],
  "threshold": 10,
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}

画面12：
{
  "queryType": "search",
  "dataSource": "wikipedia",
  "granularity": "hour",
  "searchDimensions": [
    "channel",
    "cityName"
  ],
  "query": {
    "type": "insensitive_contains",
    "value": "en"
  },
  "sort": {
    "type": "lexicographic"
  },
  "intervals": [
    "2015-09-12T00:00:00.000/2015-09-13T00:00:00.000"
  ]
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“1.7.6.1 Search查询”，下方表格列出了 Search 查询的参数及其描述和必填属性。

画面10：PPT 标题为“1.7.6.2 Select查询”，下方文字说明“Select查询返回原始Druid行并支持分页。”

画面14：PPT 标题为“1.7.6.2 Select查询”，下方文字说明“Select查询返回原始Druid行并支持分页。”

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

