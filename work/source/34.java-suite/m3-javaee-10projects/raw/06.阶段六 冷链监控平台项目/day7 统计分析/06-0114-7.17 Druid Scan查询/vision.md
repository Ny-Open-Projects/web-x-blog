# 画面线理解：7.17 Druid Scan查询

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.17 Druid Scan查询_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:16, 03:10, 04:07, 04:09, 04:11, 04:19, 04:27, 04:32, 04:36, 04:41, 04:46, 04:48, 05:03, 05:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:48:48

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
