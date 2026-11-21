# 画面线理解：7.9 使用API查询Druid数据

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.9 使用API查询Druid数据_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:56, 00:59, 01:15, 01:27, 01:53, 02:01, 02:52, 03:00, 03:22, 03:51, 04:10, 04:22, 04:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:43:42

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Apache Druid 的 Web Console 和 HTTP API 查询维基百科编辑数据，包括 SQL 和 JSON 格式两种查询方式，并展示查询结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Apache Druid Web Console 界面，执行 SQL 查询 `select * from wikipedia`，返回结果包含时间、页面、用户等字段。
画面 2: 显示 Typora 编辑器中的文档，内容为 Druid API 查询的 JSON 格式参数示例。
画面 3: 与画面 1 相同，显示 Druid Web Console 查询结果。
画面 4: 显示 Typora 文档中 SQL 格式参数的 JSON 示例，以及下方的查询示例命令。
画面 5: 显示 Xshell 终端，执行 `dsqlb select * from wikipedia limit 10;` 查询，返回结果包含时间、页面、用户等字段。
画面 6: 显示 Xshell 终端，执行 `cat wikipedia-top-pages.sql` 命令，显示 SQL 查询语句。
画面 7: 显示 Typora 文档中 SQL 格式参数的 JSON 示例，以及下方的查询示例命令。
画面 8: 显示 Typora 文档中 SQL 格式参数的 JSON 示例，以及下方的查询示例命令。
画面 9: 显示 Typora 文档中 JSON 格式参数的示例。
画面 10: 显示 Xshell 终端，执行 `ll` 命令，列出目录内容，包含多个 .json 文件。
画面 11: 显示 Typora 文档中查询示例命令，以及下方的查询结果。
画面 12: 显示 Xshell 终端，执行 `curl -X POST -H "Content-Type:application/json" -d @wikipedia-top-pages.json http://localhost:8002/druid/v2/sql` 命令。
画面 13: 显示 Xshell 终端，执行 `cat wikipedia-top-pages.sql` 命令，显示 SQL 查询语句。
画面 14: 显示 Typora 文档中查询示例命令，以及下方的查询结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```json
{
  "queryType": "topN",
  "dataSource": "wikipedia",
  "intervals": ["2015-06-12/2015-06-13"],
  "granularity": "all",
  "dimension": "page",
  "metric": "count",
  "threshold": 10,
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}
```
画面 4:
```json
{
  "query": "SELECT page, COUNT(*) AS Edits FROM wikipedia WHERE \"_time\" BETWEEN TIMESTAMP '2015-06-12 00:00:00' AND TIMESTAMP '2015-06-13 00:00:00' GROUP BY page ORDER BY Edits DESC LIMIT 10"
}
```
画面 6:
```sql
SELECT page, COUNT(*) AS Edits FROM wikipedia WHERE "_time" BETWEEN TIMESTAMP '2015-06-12 00:00:00' AND TIMESTAMP '2015-06-13 00:00:00' GROUP BY page ORDER BY Edits DESC LIMIT 10
```
画面 7:
```json
{
  "query": "SELECT page, COUNT(*) AS Edits FROM wikipedia WHERE \"_time\" BETWEEN TIMESTAMP '2015-06-12 00:00:00' AND TIMESTAMP '2015-06-13 00:00:00' GROUP BY page ORDER BY Edits DESC LIMIT 10"
}
```
画面 12:
```bash
curl -X POST -H "Content-Type:application/json" -d @wikipedia-top-pages.json http://localhost:8002/druid/v2/sql
```
画面 14:
```json
{
  "queryType": "topN",
  "dataSource": "wikipedia",
  "intervals": ["2015-06-12/2015-06-13"],
  "granularity": "all",
  "dimension": "page",
  "metric": "count",
  "threshold": 10,
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
