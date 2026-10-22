# 87. Go APM 监控系统实战: Logstash 日志清洗与入库实战

## 纲要

- Logstash 配置三段式：input（输入）、filter（过滤清洗）、output（输出），可配多个输入 / 输出源
- 第一步打通：Filebeat → Logstash（5044），Logstash 先 output 到控制台验证
- 痛点：原始日志全在 `message` 字段（text 类型，分词），无法按 `uid=0` 这类结构化条件精确匹配
- JSON 过滤：filter 里用 json 插件把 `message` 解析到变量，再用 mutate 抽出 `time`/`level`/`app`/`hostname` 作为文档顶层字段
- ES 会对每个字段建索引，抽出的字段即可被检索与聚合
- 索引命名：用模板 `dogAPM-%{app}-%{YYYY.MM.dd}`，按天建索引；清理多余的解析变量字段节省存储
- 收尾：Logstash output 改为 ES，并在 Kibana 建 `dogAPM*` 索引模式（时间字段 `@timestamp`）

## 素材索引

```mermaid
flowchart LR
    FB[Filebeat :5044] --> LS[Logstash]
    LS -->|input| IN[beats{5044}]
    IN --> F[filter: json+mutate]
    F --> O[output: ES]
    O --> ES[(Elasticsearch dogAPM-* 索引)]
    ES --> K[Kibana Index Pattern]
```

## Logstash 配置骨架

docker-compose 里新增 Logstash 服务，它的配置文件分三部分：

- **input**：数据从哪来（可配多个）；
- **filter**：对日志做分析与处理（本节的重心）；
- **output**：数据到哪去（可配多个）。

先把链路跑通：Filebeat 的 output 已指向 Logstash 的 5044 端口，Logstash 这边先不配 filter，output 也先打到控制台——确认 Filebeat 发来的日志能被 Logstash 收到即可。

## 为什么要清洗：message 字段的局限

Logstash 收到的日志结构里，应用真正打印的内容都在 `message` 字段，且它是 **text 类型（分词）**。这意味着：「查 `uid=0` 的日志」无法被正确匹配——text 会把整段文本按词切开，而非按 JSON 里的 `uid` 属性检索。

而 ES 会对文档**每个字段**建索引。所以我们目标是：把 `uid` 这类需要的属性，从 `message` 这段文本里**单独抽出来**，变成文档的顶层字段，ES 才能对它们建索引、做搜索和聚合。同理还要抽出 `host`、`app` 等维度。

## filter：解析 + 抽字段

由于 `message` 是 JSON 字符串，filter 里用 **json** 插件把它解析，并把解析结果放进一个变量（讲稿称 `parsed`）；后续 mutate 都用这个变量：

```yaml
# logstash/pipeline.conf —— 根据讲稿逻辑补充
input {
  beats { port => 5044 }
}

filter {
  # 把 message 里的 JSON 文本解析出来
  json {
    source => "message"
    target => "parsed"      # 解析结果存入 parsed 变量
  }
  # 从 parsed 抽出顶层字段，供 ES 建索引
  mutate {
    add_field => {
      "time"     => "%{parsed[time]}"      # 日志打印时间（注意区别于 @timestamp）
      "level"    => "%{parsed[level]}"     # 日志等级，便于搜 error
      "app"      => "%{parsed[app]}"       # 应用服务名
      "hostname" => "%{parsed[host]}"      # 打印日志的主机
    }
  }
  # 解析变量已无用，移除以节省存储
  mutate {
    remove_field => ["parsed"]
  }
}

output {
  elasticsearch {
    hosts => ["http://elasticsearch:9200"]
    # 索引按 app + 日期命名，每天一个新索引
    index => "dogAPM-%{app}-%{YYYY.MM.dd}"
  }
}
```

注意 `time`（日志打印时间）与 `@timestamp`（Filebeat 采集到文件的时间）不是一回事，检索时要分清。

## output 改为 ES 并建索引模式

filter 配好后，把 output 从控制台改为 ES：指定 ES 地址、用模板生成索引名 `dogAPM-%{app}-%{YYYY.MM.dd}`（每天一个索引）。重启 Logstash 容器生效，发几个错误请求后，能在 ES 里看到 `dogAPM-*` 前缀的索引，且 `hostname`/`app`/`level`/`time` 都成了可检索字段。

最后在 Kibana 建 **Index Pattern**：前缀填 `dogAPM`，时间字段选 `@timestamp`，即可在 Discover 里检索这些日志。

## 应用侧：写出带可抽字段的日志

下面 Go 程序写出 Logstash 期望的结构化日志（根据讲稿逻辑补充，自包含可运行）：

```go
// appjson/main.go —— 根据讲稿逻辑补充
package main

import (
	"github.com/sirupsen/logrus"
)

func main() {
	log := logrus.New()
	log.SetFormatter(&logrus.JSONFormatter{})
	// 这些字段会被 Logstash 的 mutate 抽出为 ES 顶层字段
	log.WithFields(logrus.Fields{
		"uid":    0,
		"app":    "order",
		"host":   "node-1",
		"level":  "error",
	}).Error("invalid order id")
}
```

## 技术点总结

- Logstash = input + filter + output 三段，输入输出可多源
- text 类型的 `message` 无法按 JSON 属性精确检索，必须抽字段
- json 插件解析 message → mutate 抽 `time`/`level`/`app`/`hostname` 为顶层字段 → ES 自动建索引
- 索引按 `dogAPM-%{app}-%{YYYY.MM.dd}` 按天切分；清掉解析变量省存储
- 时间字段认 `@timestamp`（采集时间），非日志打印时间

