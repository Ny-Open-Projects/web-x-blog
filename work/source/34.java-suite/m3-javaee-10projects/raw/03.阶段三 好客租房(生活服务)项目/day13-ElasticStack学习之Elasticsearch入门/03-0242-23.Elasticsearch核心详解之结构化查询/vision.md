# 画面线理解：23.Elasticsearch核心详解之结构化查询

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\23.Elasticsearch核心详解之结构化查询【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:40, 01:39, 02:34, 03:26, 04:06, 05:29, 06:14, 06:39, 07:41, 08:36, 08:52, 10:00, 10:32, 11:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:38:17

1) 这一组画面整体在讲什么（一句话）：
讲解 Elasticsearch 中 term、terms、range、match、bool 等查询类型的语法与使用方法，并通过 Postman 发送请求进行演示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 内容：展示 PDF 文档中“3.7.1. term 查询”章节。
- 代码示例：
  {
    "term": {
      "age": 26
    }
  }
  {
    "term": {
      "date": "2014-09-01"
    }
  }
  {
    "term": {
      "public": true
    }
  }
  {
    "term": {
      "tag": "full_text"
    }
  }
- 示例请求：
  POST http://172.16.55.185:9200/person_search

画面 2：
- 内容：在 Postman 中发送一个 POST 请求，请求体为 JSON 格式。
- 代码示例：
  {
    "took": 8,
    "timed_out": false,
    "_shards": {
      "total": 2,
      "successful": 2,
      "skipped": 0,
      "failed": 0
    },
    "hits": {
      "total": 1,
      "max_score": 1,
      "hits": [
        {
          "_index": "itcast",
          "_type": "person",
          "_id": "EFPeCgB05DcPocxIgq",
          "_score": 1,
          "_source": {
            "name": "张三",
            "age": 20,
            "mail": "111@qq.com",
            "hobby": "羽毛球,足球,篮球"
          }
        }
      ]
    }
  }

画面 3：
- 内容：展示 PDF 文档中“3.7.2. terms 查询”章节。
- 代码示例：
  {
    "terms": {
      "tag": [
        "search",
        "full_text",
        "nosql"
      ]
    }
  }

画面 4：
- 内容：展示 PDF 文档中“范围操作符包含”部分。
- 代码示例：
  {
    "range": {
      "age": {
        "gte": 20,
        "lt": 30
      }
    }
  }

画面 5：
- 内容：展示 PDF 文档中“范围操作符包含”部分的示例。
- 代码示例：
  {
    "query": {
      "range": {
        "age": {
          "gte": 20,
          "lte": 22
        }
      }
    }
  }

画面 6：
- 内容：展示 Elasticsearch 的 Kibana 界面，显示了 person 索引中的数据。
- 数据表头：score, name, age, mail, hobby。
- 数据示例：
  score: 1, name: "张三", age: 20, mail: "111@qq.com", hobby: "羽毛球,足球,篮球"

画面 7：
- 内容：在 Postman 中发送一个 POST 请求，请求体为 JSON 格式。
- 代码示例：
  {
    "took": 5,
    "timed_out": false,
    "_shards": {
      "total": 2,
      "successful": 2,
      "skipped": 0,
      "failed": 0
    },
    "hits": {
      "total": 1,
      "max_score": 1,
      "hits": [
        {
          "_index": "itcast",
          "_type": "person",
          "_id": "EFPeCgB05DcPocxIgq",
          "_score": 1,
          "_source": {
            "name": "张三",
            "age": 20,
            "mail": "111@qq.com",
            "hobby": "羽毛球,足球,篮球"
          }
        }
      ]
    }
  }

画面 8：
- 内容：在 Postman 中发送一个 POST 请求，请求体为 JSON 格式。
- 代码示例：
  {
    "took": 5,
    "timed_out": false,
    "_shards": {
      "total": 2,
      "successful": 2,
      "skipped": 0,
      "failed": 0
    },
    "hits": {
      "total": 1,
      "max_score": 1,
      "hits": [
        {
          "_index": "itcast",
          "_type": "person",
          "_id": "EFPeCgB05DcPocxIgq",
          "_score": 1,
          "_source": {
            "name": "张三",
            "age": 20,
            "mail": "111@qq.com",
            "hobby": "羽毛球,足球,篮球"
          }
        }
      ]
    }
  }

画面 9：
- 内容：在 Postman 中发送一个 POST 请求，请求体为 JSON 格式。
- 代码示例：
  {
    "took": 5,
    "timed_out": false,
    "_shards": {
      "total": 2,
      "successful": 2,
      "skipped": 0,
      "failed": 0
    },
    "hits": {
      "total": 1,
      "max_score": 1,
      "hits": [
        {
          "_index": "itcast",
          "_type": "person",
          "_id": "EFPeCgB05DcPocxIgq",
          "_score": 1,
          "_source": {
            "name": "张三",
            "age": 20,
            "mail": "111@qq.com",
            "hobby": "羽毛球,足球,篮球"
          }
        }
      ]
    }
  }

画面 10：
- 内容：展示 PDF 文档中“3.7.5. match 查询”章节。
- 代码示例：
  {
    "match": {
      "tweet": "About Search"
    }
  }
- 说明文字：如果用 match 指定了一个确切值，在遇到数字，日期，布尔值或者 not_analyzed 的字符串时，它将为你搜索你给定的值。
- 代码示例：
  {
    "match": {
      "age": 26
    }
  }
  {
    "match": {
      "date": "2014-09-01"
    }
  }
  {
    "match": {
      "public": true
    }
  }
  {
    "match": {
      "tag": "full_text"
    }
  }

画面 11：
- 内容：展示 PDF 文档中“3.7.6. bool 查询”章节。
- 代码示例：
  {
    "bool": {
      "must": {
        "term": {
          "folder": "inbox"
        }
      },
      "must_not": {
        "term": {
          "tag": "spam"
        }
      },
      "should": [
        {
          "term": {
            "Starred": true
          }
        },
        {
          "term": {
            "Unread": true
          }
        }
      ]
    }
  }

画面 12：
- 内容：展示 PDF 文档中“2.4.7. 高亮显示”章节。
- 代码示例：
  {
    "query": {
      "match": {
        "name": "张三 李四"
      }
    }
  }

画面 13：
- 内容：展示 PDF 文档中“3.7.6. bool 查询”章节。
- 代码示例：
  {
    "bool": {
      "range": {
        "age": {
          "gt": 30
        }
      },
      "must": {
        "match": {
          "sex": "男"
        }
      }
    }
  }

画面 14：
- 内容：展示 PDF 文档中“3.7.6. bool 查询”章节。
- 代码示例：
  {
    "bool": {
      "must": {
        "term": {
          "folder": "inbox"
        }
      },
      "must_not": {
        "term": {
          "tag": "spam"
        }
      },
      "should": [
        {
          "term": {
            "Starred": true
          }
        },
        {
          "term": {
            "Unread": true
          }
        }
      ]
    }
  }

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
见上述各画面要点中的代码示例。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题、架构图/流程图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
