# 画面线理解：05.全文搜索之组合搜索

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\05.全文搜索之组合搜索【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:16, 00:50, 01:24, 02:14, 02:47, 03:50, 04:55, 05:24, 05:53, 06:20, 06:55, 07:57, 08:18, 08:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:46:02

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Elasticsearch 中使用 bool 查询的 must、should 条件组合，并通过 minimum_should_match 参数控制 should 条件的匹配阈值，以及高亮（highlight）字段的配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 Postman 中构造一个包含 match、must、highlight 的 JSON 查询体，用于搜索 hobby 字段包含“羽毛球”的文档。
画面 2: 展示查询返回结果，高亮显示了“羽毛球”、“篮球”、“游泳”、“听音乐”等关键词。
画面 3: 在 Postman 中修改查询体，将 match 条件改为 hobby: "音乐"，并添加了 minimum_should_match: 2。
画面 4: 展示查询返回结果，高亮显示了“音乐”、“跑步”、“游泳”、“篮球”等关键词。
画面 5: 在 Postman 中修改查询体，将 match 条件改为 hobby: "跑步"，并添加了 minimum_should_match: 2。
画面 6: 展示 PDF 讲义中关于 highlight 配置的说明，以及一个查询结果示例。
画面 7: 展示 PDF 讲义中关于 should 条件的说明，以及一个包含三个 hobby 条件的查询示例。
画面 8: 在 Postman 中构造一个包含三个 hobby 条件的 should 查询体。
画面 9: 展示 PDF 讲义中关于 minimum_should_match 参数的说明，以及一个包含三个 hobby 条件的查询示例。
画面 10: 在 Postman 中修改查询体，将 minimum_should_match 设置为 2。
画面 11: 展示查询返回结果，高亮显示了“跑步”、“游泳”、“篮球”等关键词。
画面 12: 展示查询返回结果，高亮显示了“跑步”、“游泳”、“篮球”等关键词。
画面 13: 展示 PDF 讲义中关于 should 条件的说明，以及一个包含三个 hobby 条件的查询示例。
画面 14: 展示 PDF 讲义中关于权重（weight）的说明，以及一个搜索“游泳篮球”时，根据权重计算得分的示例。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```json
{
  "query": {
    "match": {
      "hobby": "羽毛球"
    }
  },
  "highlight": {
    "fields": {
      "hobby": {}
    }
  }
}
```

画面 2:
```json
{
  "score": 0.8684934,
  "_source": {
    "name": "王四",
    "age": 21,
    "hobby": "跑步、游泳、篮球、足球",
    "mail": "444@qq.com"
  },
  "highlight": {
    "hobby": "跑步、<em>游泳</em>、<em>篮球</em>、足球"
  }
}
```

画面 3:
```json
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "hobby": "跑步"
          }
        }
      ]
    }
  }
}
```

画面 4:
```json
{
  "score": 2.135748,
  "_source": {
    "name": "王五",
    "age": 23,
    "hobby": "羽毛球、篮球、游泳、听音乐",
    "mail": "333@qq.com"
  },
  "highlight": {
    "hobby": "羽毛球、<em>篮球</em>、<em>游泳</em>、听<em>音乐</em>"
  }
}
```

画面 5:
```json
{
  "query": {
    "bool": {
      "should": [
        {
          "match": {
            "hobby": "跑步"
          }
        },
        {
          "match": {
            "hobby": "篮球"
          }
        }
      ]
    }
  }
}
```

画面 6:
```json
{
  "highlight": {
    "fields": {
      "hobby": {}
    }
  }
}
```

画面 7:
```json
{
  "query": {
    "bool": {
      "should": [
        {
          "match": {
            "hobby": "游戏"
          }
        },
        {
          "match": {
            "hobby": "篮球"
          }
        },
        {
          "match": {
            "hobby": "音乐"
          }
        }
      ]
    }
  }
}
```

画面 8:
```json
{
  "query": {
    "bool": {
      "should": [
        {
          "match": {
            "hobby": "跑步"
          }
        },
        {
          "match": {
            "hobby": "篮球"
          }
        },
        {
          "match": {
            "hobby": "音乐"
          }
        }
      ]
    }
  }
}
```

画面 9:
```json
{
  "query": {
    "bool": {
      "should": [
        {
          "match": {
            "hobby": "游戏"
          }
        },
        {
          "match": {
            "hobby": "篮球"
          }
        },
        {
          "match": {
            "hobby": "音乐"
          }
        }
      ],
      "minimum_should_match": 2
    }
  }
}
```

画面 10:
```json
{
  "query": {
    "bool": {
      "should": [
        {
          "match": {
            "hobby": "跑步"
          }
        },
        {
          "match": {
            "hobby": "篮球"
          }
        },
        {
          "match": {
            "hobby": "音乐"
          }
        }
      ],
      "minimum_should_match": 2
    }
  }
}
```

画面 11:
```json
{
  "score": 2.135748,
  "_source": {
    "name": "王五",
    "age": 23,
    "hobby": "羽毛球、篮球、游泳、听音乐",
    "mail": "333@qq.com"
  },
  "highlight": {
    "hobby": "羽毛球、<em>篮球</em>、<em>游泳</em>、听<em>音乐</em>"
  }
}
```

画面 12:
```json
{
  "score": 2.135748,
  "_source": {
    "name": "王五",
    "age": 23,
    "hobby": "羽毛球、篮球、游泳、听音乐",
    "mail": "333@qq.com"
  },
  "highlight": {
    "hobby": "羽毛球、<em>篮球</em>、<em>游泳</em>、听<em>音乐</em>"
  }
}
```

画面 13:
```json
{
  "query": {
    "bool": {
      "should": [
        {
          "match": {
            "hobby": "游戏"
          }
        },
        {
          "match": {
            "hobby": "篮球"
          }
        },
        {
          "match": {
            "hobby": "音乐"
          }
        }
      ]
    }
  }
}
```

画面 14:
```json
{
  "highlight": {
    "fields": {
      "hobby": {}
    }
  }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 6: PDF 讲义标题为“1.2.5、权重”，内容为“搜索关键字‘游泳篮球’，如果结果中包含了‘音乐’（权重为10），包含了‘跑步’（权重为2）”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
