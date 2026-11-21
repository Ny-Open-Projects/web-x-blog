# 28-日志实时分析-DruidSQL介绍 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

我们接着讲解罪的CQ

那在讲解罪的CQ之前呢

我们先看一下我们刚才这个查询

这个查询呢

其实就像一条CQ语句一样

简单明了

但其实罪的早期并不是这么做

罪的早期呢

它其实是基于节省语句来实现的

我们看一下早期

这个写成一个节省是怎么写的

在这一块点击一下

这个就是早期的一个节省操作

点击Open Query

这里我们解读一下

Query Type Scanner

这个就是查询方式

查询的数据源是谁

查询的列有哪些

这个看起来太臃肿了

几乎都不想用

对不对

执行一次查询

跟之前的结果一样

那这个地方写起来这么麻烦

于是我们Apache罪的就开始

定制了一套对应的

CQ语句

来取代我们这个节省的查询

那这个CQ语句呢

就是我们这儿要讲的Dread SQL

我们来简单讲解一下Dread SQL

Dread SQL是一个内置的SQL层

是Dread基于节省的查询语言的替代品

Dread SQL将SQL的转换在Broker中进行

转换之后

它会把转换之后的数据

传给我们

所以我们可以看到

数据进程

那这一块会在我们Broker上

有一个转换的过程

那这个转换过程呢

会有一个额外的开销

但这个开销并不大

我们可以忽略不计

这就是我们的Dread SQL

那如果用之前这个

节省数据去写

我们得写的类似

所以这个Dread SQL

它的意义还是很大的

接着我们来讲解一下

Dread SQL的一个语法

每个Dread SQL的语法

Dread数据源这一块

它都会显示双引号

加上数据源的名字

你看我们这里就是一样的

双引号

数据源的名字

我们继续接着看

这个也是默认模式

Dread数据源引用Dread.DataSourceName

或者简单引用DataSourceName

这个是啥意思呢

就是说我们的数据源都是在Dread下面的

我们看一下

这一块是不是怎么回事

你看Dread下面有一个数据源

两个数据源

这是这一块

我们再来看一下

它的一些相关的别的语法

我们使用Dread SQL的时候

如果去执行查询的话

要注意这么个事

要用双引号引用数据源或者是列名

我们来执行一下

你看这是数据源

我们用双引号把它引起来了

如果我们要查询一个列也要引用起来

比如URI

最好不要这样写

最好用双引号引起来

这样查询

要在标识符中

如果有转义符的话

就是说我们这一块如果有转义符

那该怎么办呢

注意如果是转义符

请用两个双引号

两个双引号

这就表示转义符

它这一块是区分大小写的

好

我们Dread SQL区分大小写

如果我们在Dread SQL里面有文字出现

这个时候你就要用单引号引起来

用单引号

我举个例子

大家看我写个查询

信号form logsitems

where

我写个叫URI等于

这样子写等于某个值

这样子

这么做文字用单引号引起来

这是这一块

好

我们接着再往后面继续看

如果是数字直接写数字就行了

如果是伏点数字就直接写伏点数字

如果是科学技术法

你还可以写科学技术法

如果你是对时间进行运算

那么这一块咋写呢

这一块时间写timeStamp

如果你要对它进行运算的话

这有个interval1,2表示一小时的时间间隔

如果你写个1写个对了

一天的时间间隔

好OK

我们来举个例子

比如我想查询所有的数据

这个时间呢

我要求是什么时间的呢

是一小时以内的

一小时以内怎么办

把这个点击一下

就有一个last out

最后一小时的数据

看到没有

当前时间减去一小时

interval1,2

也就是减一小时

这个合起来一小时

这是这一块

行

这个最多C口的语法呢

我们就介绍到这里

像它的一个完整语法

下面这里有所介绍

大家可以参考这个去学习一下

Select all distinct from table will

group by having

group by

limit

unit

这都支持

是非常强大的

包括我们的排序都支持

好这是我们

最多C口的一个讲解

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段为一个关于 **Apache Druid** 数据库的实操教学课程。讲师通过 **Druid 的统一控制台 (Unified Console)** 进行演示，主要讲解了如何使用 Druid SQL 进行数据查询。演示内容包括：
- 在控制台中执行基础的 `SELECT * FROM logs` 查询。
- 展示查询结果，数据包含时间戳、IP地址、Token 和 URL 等字段。
- 介绍 Druid SQL 的语法特点，如默认的“Druid”模式、标识符的引用方式（双引号）以及时间格式的写法。
- 通过切换到 PPT 页面，讲解了 Druid SQL 的核心概念和语法结构，包括 `SELECT`、`FROM`、`WHERE`、`GROUP BY`、`HAVING`、`ORDER BY` 和 `LIMIT` 等标准 SQL 子句。
- 展示了 Druid SQL 的查询优化功能，如 `EXPLAIN PLAN FOR`。
- 通过切换多个开发工具窗口（如 Typora、Postman、Kafka Workstation），展示了 Druid 在整个数据处理链路中的位置。

整个视频旨在帮助学习者理解 Druid SQL 的基本用法和其在实时分析场景中的应用。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中各画面的绝对时间点，以下章节按画面出现的逻辑顺序排列：

- **00:00 - 00:03**: **课程开场与环境介绍**。画面显示 Druid 控制台，执行了 `SELECT * FROM logs` 查询，展示了查询结果。讲师可能在介绍课程目标和环境。
- **00:03 - 00:06**: **基础查询演示**。讲师在控制台中输入并执行了 `SELECT * FROM logs`，并展示了返回的四条记录，包含 `_time`、`ip`、`token` 和 `url` 字段。
- **00:06 - 00:09**: **SQL 语法与函数介绍**。讲师在查询语句中添加了 `WHERE` 条件，并演示了函数自动补全功能（如 `SPLIT`, `SUBSTR` 等），并展示了 `WHERE` 条件过滤后的结果。
- **00:09 - 00:12**: **切换至 PPT 讲解**。画面切换到 Typora 编辑器中的 PPT 页面，标题为“4.2.4 Druid SQL”，讲师开始讲解 Druid SQL 的概念和语法。
- **00:12 - 00:15**: **Druid SQL 概念详解**。讲师在 PPT 上详细解释了 Druid SQL 是一个内置的 SQL 层，用于替代基于 JSON 的查询语言，并介绍了其基于 Apache Calcite 的解析器。
- **00:15 - 00:18**: **Druid SQL 语法结构**。讲师在 PPT 上展示了 Druid SQL 的标准查询结构，包括 `SELECT`, `FROM`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `LIMIT` 等子句。
- **00:18 - 00:21**: **时间格式与查询优化**。讲师在 PPT 上讲解了时间格式的写法（如 `INTERVAL '1' HOUR`）和查询优化功能（如 `EXPLAIN PLAN FOR`）。
- **00:21 - 00:24**: **多工具环境展示**。讲师切换到一个包含多个开发工具窗口的视图（如 Typora、Postman、Kafka Workstation），展示了 Druid 在整个数据处理链路中的位置。
- **00:24 - 00:27**: **课程总结与展望**。讲师可能在总结 Druid SQL 的优势，并预告后续课程内容。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

- **PPT 内容**:
  - **章节标题**: `4.2.4 Druid SQL`。
  - **4.2.4.1 简介**: “Apache Druid SQL 是一个内置的 SQL 层，是 Druid 基于 JSON 的查询语言的替代品，由基于 Apache Calcite 的解析器和规划器提供支持。Druid SQL 将 SQL 转换为 Broker 本机 Druid 查询，然后将其传递给数据进程。除了在 Broker 上转换 SQL 的（轻量）开销之外，与本机查询相比，没有额外的性能损失。”
  - **4.2.4.2 语法**: “每个 Druid 数据源都显示为 'Druid' 模式，这也是默认模式。Druid 数据源引用为 `druid.dataSourceName` 或者简单引用 `dataSourceName`。可以选择使用双引号引用数据源和列名等标识符。要在标识符中转义双引号，请使用另一个双引号，例如 `My "cat" identifier`。所有标识符都区分大小写。”
  - **时间格式**: “文字字符串应用单引号，如 'foo'。文字数字字符串可以用 100（表示整数）、100.0（表示浮点值）或 1.0e5（科学记数法）等形式编写。时间戳可以写成 TIMESTAMP '2000-01-01 00:00:00'。时间算法，可以这样写 INTERVAL '1' HOUR，INTERVAL '1 02:03' DAY TO MINUTE，INTERVAL '1-2' YEAR TO MONTH，等等。”
  - **SQL 结构**: “Druid SQL 支持具有以下结构的 SELECT 查询：
    ```sql
    [ EXPLAIN PLAN FOR ]
    SELECT [ ALL | DISTINCT ] [ * | exprs ]
    FROM table
    [ WHERE expr ]
    [ GROUP BY exprs ]
    [ HAVING expr ]
    [ ORDER BY expr [ ASC | DESC ], expr [ ASC | DESC ], ... ]
    [ LIMIT limit ]
    ```
  - **图表**: 无。

- **代码**:
  - **Druid SQL 查询**:
    ```sql
    SELECT * FROM logs
    ```
    ```sql
    SELECT * FROM logs WHERE _time > '2020-05-07T00:00:00.000Z'
    ```
    ```sql
    SELECT * FROM logs WHERE ip = '192.168.211.1'
    ```
    ```sql
    SELECT * FROM logs WHERE token = 'ITHEMA'
    ```
    ```sql
    SELECT * FROM logs WHERE url LIKE '%/web/items%'
    ```
    ```sql
    SELECT * FROM logs WHERE _time BETWEEN '2020-05-07T00:00:00.000Z' AND '2020-05-07T23:59:59.999Z'
    ```
    ```sql
    SELECT * FROM logs WHERE _time > '2020-05-07T00:00:00.000Z' AND _time < '2020-05-08T00:00:00.000Z'
    ```
    ```sql
    SELECT * FROM logs WHERE _time > '2020-05-07T00:00:00.000Z' AND _time < '2020-05-08T00:00:00.000Z' AND ip = '192.168.211.1'
    ```
    ```sql
    SELECT * FROM logs WHERE _time > '2020-05-07T00:00:00.000Z' AND _time < '2020-05-08T00:00:00.000Z' AND token = 'ITHEMA'
    ```
    ```sql
    SELECT * FROM logs WHERE _time > '2020-05-07T00:00:00.000Z' AND _time < '2020-05-08T00:00:00.000Z' AND url LIKE '%/web/items%'
    ```
    ```sql
    SELECT * FROM logs WHERE _time > '2020-05-07T00:00:00.000Z' AND _time < '2020-05-08T00:00:00.000Z' AND ip = '192.168.211.1' AND token = 'ITHEMA'
    ```
    ```sql
    SELECT * FROM logs WHERE _time > '2020-05-07T00:00:00.000Z' AND _time < '2020-05-08T00:00:00.000Z' AND ip = '192.168.211.1'
