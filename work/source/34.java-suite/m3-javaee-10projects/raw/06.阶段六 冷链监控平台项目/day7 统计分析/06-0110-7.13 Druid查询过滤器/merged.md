# 7.13 Druid查询过滤器

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.13 Druid查询过滤器_【海量资源尽在 666java.com】.mp4
- 时长 5分41秒（音频 341s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面我们来看一看我们DRAID查询它的一个过滤区那么什么叫过滤区呢我把一个数据然后对它进行过滤把某个东西进行过滤那么过滤的条件其实就是叫做过滤区 对不对那类似于我们使用Circle语句来查询MyCircle数据库里边的Value条件针对于DRAID这个查询的时候我们如果使用这种API或者是使用JSON传递这个数据传递的这个参数
[00:28] 那么此时我们可以使用这个过滤区而这个一个过滤区呢其实也是一个啊JSON的一个对象是一个这种过滤条件那么过滤JSON的它查询过滤区包含了好多种类型的一种叫做Selector Filter它是一个啊还有一种叫做我们的正则表达式的包括我们的逻辑表达式的一个过滤区和英镑的
[00:56] 这种过滤区以及search和java script等等这种各种各样的一种过滤区那么我们先看一看这个select过滤区那么select过滤区它是类似于一个well条件这个语句中的well条件某一个指标等于某一个指标的值那么
[01:15] 在G-Sync中,我们知道在G-Sync里边它是传递的参数是一个整个的G-Sync串这个G-Sync串里边有一个叫filter那么在filter,在G-Sync的格式里是一个filter然后它类型type就等于select然后它的指标是指标的名称然后value是这个指标的值那么这种过滤区就类似于where某一个dimension就是某一个指标等于某个指标的值
[01:44] 那第二种呢叫做正则表达式的一个过滤器正则表达式过滤器它是类似于哎我有一个filter而这个filter它的类型叫regestregest是叫做正则表达式嘛对吧那么它的指标呢就是我们指标的值那么表达式指标的值等于某一个表达式比如说我这个指标是某个手机号而这个手机号呢是手机号不能是为字母
[02:10] 用证则表达式来给它表示出来这个可以作为一个查询条件我查询出所有的手机号码包含字母的那我就把错误的一些手机号码错误的一些数据给它过滤出来了对不对那第三类的话叫逻辑表达式的一种过滤器逻辑表达式什么是逻辑逻辑的话就是语或非嘛对不对
[02:31] 语或非然后它的一个表达式这种表达式是比如说filterfilter type等于and等于not等于等于not等于all等于not这样的一个方式这种方式来讲的话是我们在比如说and的时候它可以是多个条件比如说and某一个指标等于什么and某个指标等于什么and某一个指标等于什么and
[03:01] 某个指标等于什么它是一个相互之间的一个语的关系那么all的话其实就相对简单了只要有一个为真就可以了对不对其实是中间的这个字段里边包含了多个这个表达式这个表达式的话中间只要有一个为真那整个的就是为真了对不对那么not的话正好相反我不是一个也不能说相反吧就是说不是这种的是非的一种表达式那还有一个是因表达式
[03:30] 音的过滤区,那音的过滤区是类似于某某某,well什么什么音某一个列表里面,或者某一个数据机里面那它的形式就是filter,filter的话filter里面是type,是等于音,然后某一个指标某个指标可能存在的这个值的集合,对吧那么还有一个范围表,就是音棒的
[03:55] 这种表达式英镑的表达式来讲的话类似于某一个字段大于什么小于什么那其实就是dimension就是指标它的年龄比21岁要小于21岁或者说它大于31岁应该是大于21岁小于31岁对不对这个期间的同时它是一个数字形的那么
[04:21] 针对于范围过滤器的话就是中间这一部分对不对它是取得一个范围的一个作用加乎Square来讲的话就是我们用GS的一个公式GS的一个方法或者说GS的一个函数来表示我们的这个指标那么此时我们用到的一个表达式这也是一种玩法吧所以说这是我们提供的这几种表达式
[04:51] 另外一个的表达过滤器这种过滤器的话就是色尺过滤器色尺过滤器和select过滤器不太一样select是一个相等的关系但是色尺的实际上是类似于什么呢类似于包含关系的类似于那种like所以说是我要搜索ABC那么我搜索ABC这个字符出来那么包含ABC字符出来的某一个字段包含ABC字符出来的我都可以把它过滤出来
[05:20] 那包括我前面的是有ABC的或者中间是有ABC的那其实就是类似于那种Light这个是色识的Select就是相等的对吧所以说这个就是我们的过滤区过滤区包含了几种类型每种类型到底适应于什么样的范围什么样的一个作用等等这是我们的过滤区

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Druid 查询中的过滤器（filter）类型及其 JSON 格式定义，包括 Selector、正则表达式、逻辑表达式、IN、范围、JavaScript 和 Search 过滤器。

2) 按时间顺序列出每张画面的要点：
画面 1:
- 标题：1.7.4.1 Selector 过滤器
- 内容：介绍 Selector 过滤器，等价于 WHERE <dimension_string> = '<dimension_value_string>'，并给出 JSON 格式示例：
  {
  "filter": {
    "type": "selector",
    "dimension": <dimension_string>,
    "value": <dimension_value_string>
  }
  }

画面 2:
- 标题：1.7.4.2 正则表达式过滤器
- 内容：介绍正则表达式过滤器，等价于 Selector 过滤器，但使用正则表达式，给出 JSON 格式示例：
  {
  "filter": {
    "type": "regex",
    "dimension": <dimension_string>,
    "pattern": <pattern_string>
  }
  }

画面 3:
- 标题：1.7.4.3 逻辑表达式过滤器
- 内容：介绍逻辑表达式过滤器，包含 AND、OR、NOT 三种类型，给出 JSON 格式示例：
  AND:
  {
  "filter": {
    "type": "and",
    "fields": [<filter>, <filter>, ...]
  }
  }
  OR:
  {
  "filter": {
    "type": "or",
    "field": <filter>
  }
  }
  NOT:
  {
  "filter": {
    "type": "not",
    "field": <filter>
  }
  }

画面 4:
- 标题：1.7.4.4 IN 过滤器
- 内容：介绍 IN 过滤器，等价于 SQL 中的 IN 语句，给出 JSON 格式示例：
  {
  "type": "in",
  "dimension": "outlaw",
  "values": ["good", "bad", "ugly"]
  }

画面 5:
- 标题：1.7.4.3 逻辑表达式过滤器（AND/OR/NOT）
- 内容：重复展示逻辑表达式过滤器的 JSON 格式示例。

画面 6:
- 标题：1.7.4.3 逻辑表达式过滤器（AND/OR/NOT）
- 内容：重复展示逻辑表达式过滤器的 JSON 格式示例。

画面 7:
- 标题：1.7.4.5 范围过滤器
- 内容：介绍范围过滤器，给出 JSON 格式示例：
  {
  "type": "bound",
  "dimension": "age",
  "lower": "21",
  "upper": "31",
  "ordering": "numeric"
  }

画面 8:
- 标题：1.7.4.5 范围过滤器
- 内容：重复展示范围过滤器的 JSON 格式示例。

画面 9:
- 标题：1.7.4.6 JavaScript 过滤器
- 内容：介绍 JavaScript 过滤器，给出 JSON 格式示例：
  {
  "type": "javascript",
  "dimension": <dimension_string>,
  "function": "function(value) { ... }"
  }

画面 10:
- 标题：1.7.4.7 Search 过滤器
- 内容：介绍 Search 过滤器，给出 JSON 格式示例：
  {
  "filter": {
    "type": "search",
    "dimension": "product",
    "query": {
      "type": "insensitive_contains",
      "value": "foo"
    }
  }
  }

画面 11:
- 标题：1.7.4.7 Search 过滤器
- 内容：重复展示 Search 过滤器的 JSON 格式示例。

画面 12:
- 标题：1.7.4.1 Selector 过滤器
- 内容：重复展示 Selector 过滤器的 JSON 格式示例。

画面 13:
- 标题：1.7.4.5 范围过滤器
- 内容：重复展示范围过滤器的 JSON 格式示例。

画面 14:
- 标题：1.7.5 聚合查询
- 内容：介绍 Timeseries 聚合查询，给出查询参数表：
  | 字段名     | 描述                         | 必须 |
  |------------|------------------------------|------|
  | queryType  | 查询类型，这里填写timeseries查询 | 是   |
  | dataSource | 要查询的数据源               | 是   |
  | descending | 是否降序                     | 否   |
  | granularity | 查询进行聚合的时间粒度       | 是   |
  | intervals  | 查询的时间范围，默认是ISO-8601格式 | 是   |

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 1:
{
"filter": {
"type": "selector",
"dimension": <dimension_string>,
"value": <dimension_value_string>
}
}

画面 2:
{
"filter": {
"type": "regex",
"dimension": <dimension_string>,
"pattern": <pattern_string>
}
}

画面 3:
AND:
{
"filter": {
"type": "and",
"fields": [<filter>, <filter>, ...]
}
}
OR:
{
"filter": {
"type": "or",
"field": <filter>
}
}
NOT:
{
"filter": {
"type": "not",
"field": <filter>
}
}

画面 4:
{
"type": "in",
"dimension": "outlaw",
"values": ["good", "bad", "ugly"]
}

画面 5:
AND:
{
"filter": {
"type": "and",
"fields": [<filter>, <filter>, ...]
}
}
OR:
{
"filter": {
"type": "or",
"field": <filter>
}
}
NOT:
{
"filter": {
"type": "not",
"field": <filter>
}
}

画面 6:
AND:
{
"filter": {
"type": "and",
"fields": [<filter>, <filter>, ...]
}
}
OR:
{
"filter": {
"type": "or",
"field": <filter>
}
}
NOT:
{
"filter": {
"type": "not",
"field": <filter>
}
}

画面 7:
{
"type": "bound",
"dimension": "age",
"lower": "21",
"upper": "31",
"ordering": "numeric"
}

画面 8:
{
"type": "bound",
"dimension": "age",
"lower": "21",
"upper": "31",
"ordering": "numeric"
}

画面 9:
{
"type": "javascript",
"dimension": <dimension_string>,
"function": "function(value) { ... }"
}

画面 10:
{
"filter": {
"type": "search",
"dimension": "product",
"query": {
"type": "insensitive_contains",
"value": "foo"
}
}
}

画面 11:
{
"filter": {
"type": "search",
"dimension": "product",
"query": {
"type": "insensitive_contains",
"value": "foo"
}
}
}

画面 12:
{
"filter": {
"type": "selector",
"dimension": <dimension_string>,
"value": <dimension_value_string>
}
}

画面 13:
{
"type": "bound",
"dimension": "age",
"lower": "21",
"upper": "31",
"ordering": "numeric"
}

画面 14:
| 字段名     | 描述                         | 必须 |
|------------|------------------------------|------|
| queryType  | 查询类型，这里填写timeseries查询 | 是   |
| dataSource | 要查询的数据源               | 是   |
| descending | 是否降序                     | 否   |
| granularity | 查询进行聚合的时间粒度       | 是   |
| intervals  | 查询的时间范围，默认是ISO-8601格式 | 是   |

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 14:
- 标题：1.7.5 聚合查询
- 子标题：1.7.5.1 Timeseries
- 表格数据：
  | 字段名     | 描述                         | 必须 |
  |------------|------------------------------|------|
  | queryType  | 查询类型，这里填写timeseries查询 | 是   |
  | dataSource | 要查询的数据源               | 是   |
  | descending | 是否降序                     | 否   |
  | granularity | 查询进行聚合的时间粒度       | 是   |
  | intervals  | 查询的时间范围，默认是ISO-8601格式 | 是   |

5) 无。

