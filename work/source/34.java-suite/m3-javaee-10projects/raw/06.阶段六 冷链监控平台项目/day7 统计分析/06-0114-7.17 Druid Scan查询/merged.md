# 7.17 Druid Scan查询

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.17 Druid Scan查询_【海量资源尽在 666java.com】.mp4
- 时长 5分6秒（音频 306s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面我们来看一看Droid它的Scan查询Scan查询的话就是扫描查询扫描查询以流模式返回我们原始的数据行它和Select一样都是返回原始的数据行但是Select和Scan的最大区别在于Scan查询在查询在返回到客户端之前不会在内存中保留所有返回的行那么Select会在内存中保留
[00:28] 保留行如果返回的行数太多的情况下就会造成内存的压力比较大就有可能把我们的内存给吃满了那么scan查询可以返回所有的行但是呢它并不进行一个分页查询那么我们除了向布尔克这个节点发出scan查询的这样的一个用法外我们还可以直接向我们的historical进程
[00:54] 发出这种scan查询也就是说broker来讲的话是那个属于什么呢属于我们的这种broker是属于我们的实时的一个查询那么historical的话是属于我们的历史节点的一个查询那么在这种情况下其实scan来讲的话是比较符合我们大数据量的一个查询结果的虽然它没有分解但是它可以一次性返回非常多的这种数据它是以这种数据流的形式返回给现代的
[01:21] 我们看一看scan查询它的一些字段字段的含义query type的话很简单就是一个scan了对吧data source就是我们的数据库的表结构interval就是我们的查询的时间范围result format这个稍微有点点意思它表示是我们返回的表达方式到底是个list或者说是一个compact list或者是value vector
[01:48] 那么目前的话呢只是支持list和compactlist那么默认是list也就是说大家把它认为就是我返回就是一个结果集就可以了那filter的话是指的是查询的过滤条件和其他都是一样的我什么条件来查询的columns是指的是要扫描的维度和度量的字符串的数组那换句话说我select新或者说select某一个字段
[02:15] 实际上是where某哪些字段里面的值我要扫描这些东西那么bit size的话指的是我们的在返回到客户端之前我的数据流中缓存的最大行数它不是在内存中缓存的大家在这个地方需要注意的scan的话它的数据得到了之后它并没有在内存中
[02:42] 做一个在内存中存储一下然后呢再返回给我的前台而是直接就以数据流的形式返回给前台那么它的这个Base Size指的是我的数据流的一个缓缓充池它的一个大小默认是20480然后Limit指的话是要返回多少行如果没指定就返回所有的行了这个时候大家需要稍微注意一点了它会返回所有行如果不指定这个LimitOrder的话是
[03:09] 按时间戳是否进行排序然后这个legacy的话它的返回的是与旧的scan查询这种control live扩展一致的一个结果默认的话实际上是属于我们的这个dread queryscanlegacy设置的值该值默认的实际上是一个falsecontext的话其实就指定某些标识这个我不多说那我们看这样我们的这个例子这个例子来讲的话我们的
[03:38] query type是一个scan我们查询的表明是这个然后返回结果是类似的然后返回的是所有的字段我们把所有字段都返回过来然后我们的interval就是执行查询的时间范围是12号到13号然后查询的返回值的缓冲就是在数据流的缓冲池中的缓冲实际上是2048480然后返回三条
[04:06] 我们来看一看我们的执行效果首先我们拷贝过来我们poster man里面此时它返回的就是三条数据对吧这个也比较明显三条数据一条两条三条对不对一文条是这样的然后返回的字段我们没设置字段可以把所有的都给返回过来了还有的方式是假设我返回10条其实就是在范围内的数据返回了10条对吧我把
[04:41] 字段里面的数据返回了失调这是我们的这个scan一定要注意scan和这个select一个差别啊select的话是在内存中存现在内存中存储的然后它就存在内存中的一些这个性能开销比较严重容易造成内存问题然后scan的话不会产生什么这样的问题

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲Druid的Scan查询语句的参数说明及通过Postman发送查询请求的实战演示。

2) 按时间顺序列出每张画面的要点：
画面1: 展示Druid文档中1.7.6.3 Scan查询章节，列出Scan查询的参数表，包括queryType、dataSource、intervals、resultFormat、filter、columns、batchSize、limit、order、legacy、context等字段及其描述和是否必需。
画面2: 文档页面向下滚动，展示order和legacy字段的描述。
画面3: 文档页面继续向下滚动，展示context字段描述及下方的“示例：”标题和一个JSON格式的Scan查询示例。
画面4: 文档页面显示“示例：”标题下的JSON示例，但示例内容区域为空白。
画面5: 切换到Postman界面，显示一个POST请求的Body部分，请求地址为http://172.17.0.143:8888/druid/v2，Body中包含JSON格式的查询参数，如"dimensions": ["l1"], "dataSource": "wikipedia", "granularity": "hour", "intervals": ["2015-09-12/2015-09-13"]，"queryType": "scan"。
画面6: Postman界面中，Body部分的JSON数据被滚动显示，展示更多字段，如"comment": "الصفحة العربية لـ [[https://encyc.reefnet.gov.sy/page-entry/610=138275]]"。
画面7: Postman界面中，Body部分的JSON数据被滚动显示，展示"columns"字段的值为["time", "channel", "cityName", "countryIsoCode", "countryName", "isAnonymous", "isBot", "isRobot", "isSpam", "language", "page", "regionIsoCode", "regionName", "user"]。
画面8: Postman界面中，Body部分的JSON数据被滚动显示，展示"intervals"字段的值为["2015-09-12/2015-09-13"]，"batchSize": 20480，"limit": 10。
画面9: Postman界面中，Body部分的JSON数据被滚动显示，展示"comment"字段的值为"الصفحة العربية لـ [[https://encyc.reefnet.gov.sy/page-entry/610=138275]]"。
画面10: Postman界面中，Body部分的JSON数据被滚动显示，展示"sum_deleted": 55，"sum_select": 115，"sum_retrocode": 0，"count": 1。
画面11: 切换回Druid文档页面，显示“示例：”标题下的JSON示例，但示例内容区域为空白。
画面12: 切换回Druid文档页面，显示“示例：”标题下的JSON示例，示例内容为：
{
  "queryType": "scan",
  "dataSource": "wikipedia",
  "resultFormat": "list",
  "columns": [],
  "intervals": [
    "2015-09-12/2015-09-13"
  ],
  "batchSize": 20480,
  "limit": 10
}
画面13: 切换回Druid文档页面，显示“1.7.6.3 Scan查询”章节，展示Scan查询的参数表，包括queryType、dataSource、intervals、resultFormat、filter、columns、batchSize、limit、order、legacy、context等字段及其描述和是否必需。
画面14: 切换回Druid文档页面，显示“1.7.6.3 Scan查询”章节，展示Scan查询的参数表，包括queryType、dataSource、intervals、resultFormat、filter、columns、batchSize、limit、order、legacy、context等字段及其描述和是否必需。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5: 
{
  "dimensions": ["l1"],
  "dataSource": "wikipedia",
  "granularity": "hour",
  "intervals": ["2015-09-12/2015-09-13"],
  "queryType": "scan"
}

画面6: 
{
  "dimensions": ["l1"],
  "dataSource": "wikipedia",
  "granularity": "hour",
  "intervals": ["2015-09-12/2015-09-13"],
  "queryType": "scan",
  "comment": "الصفحة العربية لـ [[https://encyc.reefnet.gov.sy/page-entry/610=138275]]"
}

画面7: 
{
  "dimensions": ["l1"],
  "dataSource": "wikipedia",
  "granularity": "hour",
  "intervals": ["2015-09-12/2015-09-13"],
  "queryType": "scan",
  "comment": "الصفحة العربية لـ [[https://encyc.reefnet.gov.sy/page-entry/610=138275]]",
  "columns": [
    "time",
    "channel",
    "cityName",
    "countryIsoCode",
    "countryName",
    "isAnonymous",
    "isBot",
    "isRobot",
    "isSpam",
    "language",
    "page",
    "regionIsoCode",
    "regionName",
    "user"
  ]
}

画面8: 
{
  "dimensions": ["l1"],
  "dataSource": "wikipedia",
  "granularity": "hour",
  "intervals": ["2015-09-12/2015-09-13"],
  "queryType": "scan",
  "comment": "الصفحة العربية لـ [[https://encyc.reefnet.gov.sy/page-entry/610=138275]]",
  "columns": [
    "time",
    "channel",
    "cityName",
    "countryIsoCode",
    "countryName",
    "isAnonymous",
    "isBot",
    "isRobot",
    "isSpam",
    "language",
    "page",
    "regionIsoCode",
    "regionName",
    "user"
  ],
  "batchSize": 20480,
  "limit": 10
}

画面9: 
{
  "dimensions": ["l1"],
  "dataSource": "wikipedia",
  "granularity": "hour",
  "intervals": ["2015-09-12/2015-09-13"],
  "queryType": "scan",
  "comment": "الصفحة العربية لـ [[https://encyc.reefnet.gov.sy/page-entry/610=138275]]",
  "columns": [
    "time",
    "channel",
    "cityName",
    "countryIsoCode",
    "countryName",
    "isAnonymous",
    "isBot",
    "isRobot",
    "isSpam",
    "language",
    "page",
    "regionIsoCode",
    "regionName",
    "user"
  ],
  "batchSize": 20480,
  "limit": 10
}

画面10: 
{
  "dimensions": ["l1"],
  "dataSource": "wikipedia",
  "granularity": "hour",
  "intervals": ["2015-09-12/2015-09-13"],
  "queryType": "scan",
  "comment": "الصفحة العربية لـ [[https://encyc.reefnet.gov.sy/page-entry/610=138275]]",
  "columns": [
    "time",
    "channel",
    "cityName",
    "countryIsoCode",
    "countryName",
    "isAnonymous",
    "isBot",
    "isRobot",
    "isSpam",
    "language",
    "page",
    "regionIsoCode",
    "regionName",
    "user"
  ],
  "batchSize": 20480,
  "limit": 10,
  "sum_deleted": 55,
  "sum_select": 115,
  "sum_retrocode": 0,
  "count": 1
}

画面12: 
{
  "queryType": "scan",
  "dataSource": "wikipedia",
  "resultFormat": "list",
  "columns": [],
  "intervals": [
    "2015-09-12/2015-09-13"
  ],
  "batchSize": 20480,
  "limit": 10
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3: PPT标题为“2 Druid实战”，子标题为“2.1 数据存储”。

