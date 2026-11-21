# 7.9 使用API查询Druid数据

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.9 使用API查询Druid数据_【海量资源尽在 666java.com】.mp4
- 时长 4分40秒（音频 280s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面我们来介绍第二种的一个查询方式就是API的一个查询我们通过API的方式来查询DRAID中的数据那通过第一种方式客户端我们知道我们在我们的这个DRAID的管理端上有一个Query的一个菜单或者是Query的一个功能而这个功能呢实际上是我们提交写一个Selecting from Wikipedia也就是说写一个Circle语句我们提交给后台那么后台给我们返回结果
[00:30] 大家想一下这个过程这个过程其实是说我把一个格式的数据一个格式的参数我传给后台的一个API那么这个后台的API就能够得到一个结果了对不对那同样的道理我们的API的调用方式就是这样的一个原理那本质上来讲的话我们提供了两类J的提供了两类方式一种是叫JSON格式的参数一种是我们的Circle格式的参数对吧
[00:59] 我们在web页面上来提供的调用的这样的一个circle语句的一个插询其实就是传递的参数是属于这种circle语句那么所以说在后台提交服务的时候就是一个circle语句我把这个传提交过去那么我们来先看我们的circle格式circle格式在我们的例子里边其实也有我们到我们的我们到我们的这个目录里边这个目录是我们的quicker
[01:32] Quick Start, Quick Start Tutorial然后在这个目录里边有一个Wikipedia Top Page Circle那么它本身这是一个json格式的数据然后呢它的内容实际上就是一个Circle一句那我们调用了我们的CUIR的这个命令来查询它我们仔细看一下这个调用的这个命令哈一个是CUIR, CUIR的话
[02:10] 调用到某一个接口CIR调用某一个接口而这个接口呢实际上是我们的8082端口然后它的API是J的V2的circle然后它的参数呢是我们的wikipedia top-pages-circle.json这个json文件是作为这个API的一个参数那么传输的方式呢是post的方式那传输的
[02:38] 文件的类型呢是一个json类型的那么一返回我们去实际上是调用了这个接口那返回的就是我们想要的一个结果了对不对这是我们使用了这个格式的参数来进行查询那还有一种格式是使用了这个json格式使用json格式json格式到底是一个什么样的格式我们在后边会给大家详细的介绍现在呢只是给大家做一个演示让大家有一个感性的一个认识
[03:05] 那么我们还是在我们的Quickstart也就是说我们的示例程序里边的示例程序的这个目录里边我们可以看到有一个wikipedia-top-page的这个json文件我们看一下这个文件这个文件它的内容我们现在不做过多的讲解只不过是让大家知道这就是一个json格式的一个传输的参数而这个json格式呢是想要我们
[03:32] 我们发送给我们后台坠的一个接口里面的一个参数这个参数肯定是有我们想要的一个结果以及我们想要提交的一些数据的参数那么在这个过程中我们用我们的CURL来调用我们的一个接口我要重新的把它拷贝过来那CURL以POST的方式提交的json格式的
[04:03] 文件而提交的参数呢就是我们刚才看到的这个数据这个参数然后提交轨型呢大家注意一点提交的是v2问号pretty它和我们刚才第一次提交的用circle的语言用circle的这个方式提交的不太一样circle方式是v2斜杠的一个circle但是我们使用json格式提交的就是v2的一个pretty这样的一个结果
[04:32] 那么此时我们就得到我们想要的一个结果了这是我们使用API方式查询罪的数据的两种方式

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

