# 画面线理解：04.全文搜索之多词搜索

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\04.全文搜索之多词搜索【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:17, 00:37, 01:01, 01:14, 01:34, 03:24, 03:52, 04:47, 05:27, 08:09, 08:38, 09:00, 09:38, 10:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:45:16

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Elasticsearch 中使用 match 查询进行多词搜索，并通过设置 minimum_should_match 参数控制匹配阈值，同时展示高亮（highlight）功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 Postman 中发送一个 POST 请求到 http://172.16.55.185:9200/itcast/person/_search，请求体为 JSON 格式，查询结果包含一个文档，其 hobby 字段值为“羽毛球、篮球、音乐、听音乐”。高亮字段显示为“羽毛球、篮球、音乐、听音乐”。

画面 2: 在 Postman 中，请求体 JSON 数据被修改，hobby 字段值变为“跑步、游泳、<cm>篮球</cm>”。高亮字段显示为“跑步、游泳、<cm>篮球</cm>”。

画面 3: 在 Postman 中，请求体 JSON 数据被修改，hobby 字段值变为“跑步、游泳、<cm>篮球</cm>、音乐、听音乐”。高亮字段显示为“跑步、游泳、<cm>篮球</cm>、音乐、听音乐”。

画面 4: Adobe Reader 中打开的 PDF 文档，显示了 Elasticsearch 的 JSON 查询结构，其中 hobby 字段值为“跑步、游泳、<cm>篮球</cm>”。下方有文字说明“可以看到结果符合预期”。

画面 5: 在 Postman 中，发送请求后返回的 JSON 响应结果，显示查询成功，返回一个文档，其 hobby 字段值为“羽毛球、篮球、音乐、听音乐”。

画面 6: 在 Postman 中，请求体 JSON 数据被修改，query 部分的 match 字段中 hobby 字段值为“篮球 手机”，并设置了 highlight 部分的 fields 为 hobby。

画面 7: 在 Postman 中，请求体 JSON 数据被修改，query 部分的 match 字段中 hobby 字段值为“篮球 手机”，并设置了 highlight 部分的 fields 为 hobby。发送请求后返回状态码为 400 Bad Request。

画面 8: 在 Postman 中，发送请求后返回的 JSON 响应结果，显示查询成功，返回一个文档，其 hobby 字段值为“羽毛球、篮球、音乐、听音乐”。

画面 9: Adobe Reader 中打开的 PDF 文档，显示了 Elasticsearch 的 JSON 查询结构，其中 hobby 字段值为“跑步、游泳、<cm>篮球</cm>”。下方有文字说明“前面我们测试了“OR”和“AND”搜索，这是两个极端，其实在实际场景中，并不会选取这两个极端，更有可能是选取这种，或者说，只需要符合一定的相似度就可以查到数据，在 Elasticsearch 中也支持这样的查询，通过 minimum_should_match 来指定匹配度，如：70%；示例：”。

画面 10: 在 Postman 中，请求体 JSON 数据被修改，query 部分的 match 字段中 hobby 字段值为“篮球”，并设置了 highlight 部分的 fields 为 hobby。

画面 11: 在 Postman 中，请求体 JSON 数据被修改，query 部分的 match 字段中 hobby 字段值为“篮球”，并设置了 highlight 部分的 fields 为 hobby。同时，设置了 minimum_should_match 为“80%”。

画面 12: 在 Postman 中，请求体 JSON 数据被修改，query 部分的 match 字段中 hobby 字段值为“篮球”，并设置了 highlight 部分的 fields 为 hobby。同时，设置了 minimum_should_match 为“10%”。

画面 13: Adobe Reader 中打开的 PDF 文档，显示了 Elasticsearch 的 JSON 查询结构，其中 hobby 字段值为“跑步、游泳、<cm>篮球</cm>”。下方有文字说明“#结果：省略显示：#相似度为80%的情况下，查询到4条数据”。

画面 14: Adobe Reader 中打开的 PDF 文档，显示了 Elasticsearch 的 JSON 查询结构，其中 hobby 字段值为“跑步、游泳、<cm>篮球</cm>”。下方有文字说明“#设置40%进行测试：”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
{
  "score": 8.8163220,
  "_source": {
    "name": "王五",
    "mail": "333@qq.com",
    "hobby": "羽毛球、篮球、音乐、听音乐"
  },
  "highlight": {
    "hobby": [
      "羽毛球、篮球、音乐、听音乐"
    ]
  }
}

画面 2:
{
  "score": 8.8163220,
  "_source": {
    "name": "王五",
    "mail": "333@qq.com",
    "hobby": "跑步、游泳、<cm>篮球</cm>"
  },
  "highlight": {
    "hobby": [
      "跑步、游泳、<cm>篮球</cm>"
    ]
  }
}

画面 3:
{
  "score": 8.8163220,
  "_source": {
    "name": "王五",
    "mail": "333@qq.com",
    "hobby": "跑步、游泳、<cm>篮球</cm>、音乐、听音乐"
  },
  "highlight": {
    "hobby": [
      "跑步、游泳、<cm>篮球</cm>、音乐、听音乐"
    ]
  }
}

画面 4:
{
  "index": "itcast",
  "type": "person",
  "id": "uFGrNagQH-ht6w8-LpdkZ",
  "score": 0.5027054,
  "_source": {
    "name": "王五",
    "mail": "333@qq.com",
    "hobby": "羽毛球、篮球、音乐、听音乐"
  }
}

画面 5:
{
  "took": 18,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 1,
    "max_score": 1.3192271,
    "hits": [
      {
        "_index": "itcast",
        "_type": "person",
        "_id": "uFGrNagQH-ht6w8-LpdkZ",
        "_score": 1.3192271,
        "_source": {
          "name": "王五",
          "mail": "333@qq.com",
          "hobby": "羽毛球、篮球、音乐、听音乐"
        },
        "highlight": {
          "hobby": [
            "羽毛球、篮球、音乐、听音乐"
          ]
        }
      }
    ]
  }
}

画面 6:
{
  "query": {
    "match": {
      "hobby": "篮球 手机"
    },
    "highlight": {
      "fields": {
        "hobby": {}
      }
    }
  }
}

画面 7:
{
  "query": {
    "match": {
      "hobby": "篮球 手机"
    },
    "highlight": {
      "fields": {
        "hobby": {}
      }
    }
  }
}

画面 8:
{
  "took": 18,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 1,
    "max_score": 1.3192271,
    "hits": [
      {
        "_index": "itcast",
        "_type": "person",
        "_id": "uFGrNagQH-ht6w8-LpdkZ",
        "_score": 1.3192271,
        "_source": {
          "name": "王五",
          "mail": "333@qq.com",
          "hobby": "羽毛球、篮球、音乐、听音乐"
        },
        "highlight": {
          "hobby": [
            "羽毛球、篮球、音乐、听音乐"
          ]
        }
      }
    ]
  }
}

画面 9:
{
  "query": {
    "match": {
      "hobby": "跑步 羽毛球"
    },
    "highlight": {
      "fields": {
        "hobby": {}
      }
    }
  }
}

画面 10:
{
  "query": {
    "match": {
      "hobby": "篮球"
    },
    "highlight": {
      "fields": {
        "hobby": {}
      }
    }
  }
}

画面 11:
{
  "query": {
    "match": {
      "hobby": "篮球"
    },
    "highlight": {
      "fields": {
        "hobby": {}
      }
    }
  },
