# 画面线理解：06.全文搜索之权重

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\06.全文搜索之权重【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 02:06, 02:08, 02:20, 02:38, 02:44, 03:03, 03:08, 03:16, 03:21, 03:44, 03:49, 03:57, 04:57, 05:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:46:52

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Elasticsearch 中使用权重（boost）来调整搜索结果中特定字段的得分，并通过 Postman 发送请求和查看响应。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中关于“权重”的章节，内容为“搜索关键字为‘游泳篮球’，如果结果中包含了‘音乐’权重为10，包含了‘散步’权重为2。”，并附带一个 JSON 查询结构示例。
画面 2: PDF 文档中“1.2.5. 权重”章节，展示一个包含“match”和“should”条件的 JSON 查询结构，其中“query”: “游泳篮球”，“operator”: “and”。
画面 3: Postman 中发送的 POST 请求，URL 为 http://172.16.55.185:9200/icast/person_search，Body 为 JSON 格式，包含一个“bool”查询，其中“must”条件为“match”查询“hobby”: “游泳篮球”，“operator”: “and”。
画面 4: Postman 中显示的响应结果，包含“total”: 2, “took”: 12ms, “hits”数组中包含两个文档，第一个文档的“hobby”字段值为“跑步、游泳、篮球”。
画面 5: Postman 中显示的响应结果，包含“total”: 2, “took”: 12ms, “hits”数组中包含两个文档，第二个文档的“hobby”字段值为“跑步、游泳、篮球”。
画面 6: Postman 中显示的响应结果，包含“total”: 2, “took”: 12ms, “hits”数组中包含两个文档，第二个文档的“hobby”字段值为“跑步、游泳、篮球”。
画面 7: PDF 文档中“1.2.5. 权重”章节，展示一个包含“match”和“should”条件的 JSON 查询结构，其中“match”: “hobby”: “跑步”，“boost”: 10。
画面 8: PDF 文档中“1.2.5. 权重”章节，展示一个包含“match”和“should”条件的 JSON 查询结构，其中“match”: “hobby”: “跑步”，“boost”: 10。
画面 9: Postman 中显示的响应结果，包含“total”: 2, “took”: 12ms, “hits”数组中包含两个文档，第一个文档的“hobby”字段值为“跑步、游泳、篮球”。
画面 10: Postman 中显示的响应结果，包含“total”: 2, “took”: 12ms, “hits”数组中包含两个文档，第二个文档的“hobby”字段值为“跑步、游泳、篮球”。
画面 11: Postman 中显示的响应结果，包含“total”: 2, “took”: 12ms, “hits”数组中包含两个文档，第二个文档的“hobby”字段值为“跑步、游泳、篮球”。
画面 12: Postman 中显示的响应结果，包含“total”: 2, “took”: 12ms, “hits”数组中包含两个文档，第二个文档的“hobby”字段值为“跑步、游泳、篮球”。
画面 13: PDF 文档中“1.2.5. 权重”章节，展示一个包含“match”和“should”条件的 JSON 查询结构，其中“match”: “hobby”: “跑步”，“boost”: 10。
画面 14: PDF 文档中“1.2.5. 权重”章节，展示一个包含“match”和“should”条件的 JSON 查询结构，其中“match”: “hobby”: “跑步”，“boost”: 10。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```json
POST http://172.16.55.185:9200/icast/person_search
{
  "query": {
    "bool": {
      "must": {
        "match": {
          "hobby": "游泳篮球",
          "operator": "and"
        }
      },
      "should": []
    }
  }
}
```

画面 3:
```json
{
  "query": {
    "bool": {
      "must": {
        "match": {
          "hobby": "游泳篮球",
          "operator": "and"
        }
      }
    }
  }
}
```

画面 4:
```json
{
  "total": 2,
  "took": 12,
  "hits": [
    {
      "_index": "icast",
      "_type": "person",
      "_id": "nullWeight-mid.xwMwPf",
      "_score": 1.630734,
      "_source": {
        "name": "超六",
        "age": 23,
        "mail": "444@qq.com",
        "hobby": "跑步、游泳、篮球"
      }
    }
  ]
}
```

画面 5:
```json
{
  "total": 2,
  "took": 12,
  "hits": [
    {
      "_index": "icast",
      "_type": "person",
      "_id": "nullWeight-mid.xwMwPf",
      "_score": 1.630734,
      "_source": {
        "name": "超六",
        "age": 23,
        "mail": "444@qq.com",
        "hobby": "跑步、游泳、篮球"
      }
    }
  ]
}
```

画面 6:
```json
{
  "total": 2,
  "took": 12,
  "hits": [
    {
      "_index": "icast",
      "_type": "person",
      "_id": "nullWeight-mid.xwMwPf",
      "_score": 1.630734,
      "_source": {
        "name": "超六",
        "age": 23,
        "mail": "444@qq.com",
        "hobby": "跑步、游泳、篮球"
      }
    }
  ]
}
```

画面 7:
```json
{
  "query": {
    "bool": {
      "must": {
        "match": {
          "hobby": "跑步",
          "boost": 10
        }
      },
      "should": []
    }
  }
}
```

画面 8:
```json
{
  "query": {
    "bool": {
      "must": {
        "match": {
          "hobby": "跑步",
          "boost": 10
        }
      },
      "should": []
    }
  }
}
```

画面 9:
```json
{
  "total": 2,
  "took": 12,
  "hits": [
    {
      "_index": "icast",
      "_type": "person",
      "_id": "nullWeight-mid.xwMwPf",
      "_score": 1.630734,
      "_source": {
        "name": "超六",
        "age": 23,
        "mail": "444@qq.com",
        "hobby": "跑步、游泳、篮球"
      }
    }
  ]
}
```

画面 10:
```json
{
  "total": 2,
  "took": 12,
  "hits": [
    {
      "_index": "icast",
      "_type": "person",
      "_id": "nullWeight-mid.xwMwPf",
      "_score": 1.630734,
      "_source": {
        "name": "超六",
        "age": 23,
        "mail": "444@qq.com",
        "hobby": "跑步、游泳、篮球"
      }
    }
  ]
}
```

画面 11:
```json
{
  "total": 2,
  "took": 12,
  "hits": [
    {
      "_index": "icast",
      "_type": "person",
      "_id": "nullWeight-mid.xwMwPf",
      "_score": 1.630734,
      "_source": {
        "name": "超六",
        "age": 23,
        "mail": "444@qq.com",
        "hobby": "跑步、游泳、篮球"
      }
    }
  ]
}
```

画面 12:
```json
{
  "total": 2,
  "took": 12,
  "hits": [
    {
      "_index": "icast",
      "_type": "person",
      "_id": "nullWeight-mid.xwMwPf",
      "_score": 1.630734,
      "_source": {
        "name": "超六",
        "age": 23,
        "mail": "444@qq.com",
        "hobby": "跑步、游泳、篮球"
      }
