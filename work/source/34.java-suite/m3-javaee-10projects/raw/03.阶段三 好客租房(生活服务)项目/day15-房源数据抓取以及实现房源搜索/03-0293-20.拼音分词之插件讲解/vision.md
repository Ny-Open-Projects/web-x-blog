# 画面线理解：20.拼音分词之插件讲解

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\20.拼音分词之插件讲解【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:14, 00:34, 00:50, 01:07, 01:50, 02:13, 02:34, 02:53, 04:05, 04:24, 05:02, 05:40, 05:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:12:41

1) 这一组画面整体在讲如何在 Elasticsearch 中配置和测试拼音分词插件，以实现对中文姓名等文本的拼音搜索功能。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 Docker 创建 Elasticsearch 节点的命令，以及测试拼音分词的 PUT 请求示例。
画面2: 展示了课程文档中“6、拼音分词”章节，说明搜索时需要支持拼音，并提供了插件的 GitHub 地址和下载链接。
画面3: 展示了 GitHub 上的拼音分词插件文档，包含创建索引时的配置代码。
画面4: 展示了 Postman 中发送 PUT 请求创建索引的界面，请求体为创建索引的 JSON 配置。
画面5: 展示了 GitHub 文档中测试分词器的 GET 请求示例和返回结果。
画面6: 展示了 Postman 中发送 GET 请求测试分词器的界面。
画面7: 展示了课程文档中“6.2、测试拼音分词”章节，包含创建索引的 PUT 请求示例。
画面8: 展示了课程文档中“6.2、测试拼音分词”章节的末尾部分，包含插件参数说明。
画面9: 展示了 Postman 中发送 POST 请求测试分词器的界面，返回结果为分词后的 token。
画面10: 展示了课程文档中创建索引映射的 POST 请求示例，配置了 name 字段的类型和分词器。
画面11: 展示了课程文档中搜索请求的 POST 请求示例，配置了 match 查询和拼音分词器。
画面12: 展示了 Postman 中发送 POST 请求进行搜索的界面，输入框中输入“刘德华”并显示拼音搜索建议。
画面13: 展示了 Postman 中发送 POST 请求进行搜索的界面，请求体为 match 查询。
画面14: 展示了搜索结果的 JSON 响应，包含匹配到的文档信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```
docker create --name es-node02 --net host -v /haoke/es-
cluster/pinyin:/usr/share/elasticsearch/plugins/pinyin -v /haoke/es-
cluster/node02/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml
-v /haoke/es-cluster/node02/jvm.options:/usr/share/elasticsearch/config/jvm.options
-v /haoke/es-cluster/ik:/usr/share/elasticsearch/plugins/ik -v /haoke/es-
cluster/pinyin:/usr/share/elasticsearch/plugins/pinyin -v /haoke/es-
cluster/node02/data:/usr/share/elasticsearch/data elasticsearch:6.5.4
docker create --name es-node03 --net host -v /haoke/es-
cluster/pinyin:/usr/share/elasticsearch/plugins/pinyin -v /haoke/es-
cluster/node03/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml
-v /haoke/es-cluster/node03/jvm.options:/usr/share/elasticsearch/config/jvm.options
-v /haoke/es-cluster/ik:/usr/share/elasticsearch/plugins/ik -v /haoke/es-
cluster/pinyin:/usr/share/elasticsearch/plugins/pinyin -v /haoke/es-
cluster/node03/data:/usr/share/elasticsearch/data elasticsearch:6.5.4
```

画面3:
```
PUT /medcl/
{
  "index": {
    "analysis": {
      "pinyin_analyzer": {
        "tokenizer": "my_pinyin"
      }
    },
    "tokenizer": {
      "my_pinyin": {
        "type": "pinyin",
        "keep_separate_first_letter": false,
        "keep_full_pinyin": true,
        "keep_original": true,
        "limit_first_letter_length": 16,
        "lowercase": true,
        "remove_duplicated_term": true
      }
    }
  }
}
```

画面4:
```
{
  "index": {
    "analysis": {
      "pinyin_analyzer": {
        "tokenizer": "my_pinyin"
      }
    },
    "tokenizer": {
      "my_pinyin": {
        "type": "pinyin",
        "keep_separate_first_letter": false,
        "keep_full_pinyin": true,
        "keep_original": true,
        "limit_first_letter_length": 16,
        "lowercase": true,
        "remove_duplicated_term": true
      }
    }
  }
}
```

画面5:
```
GET /medcl/_analyze
{
  "text": ["刘德华"],
  "analyzer": "pinyin_analyzer"
}
```

画面6:
```
{
  "index": {
    "analysis": {
      "pinyin_analyzer": {
        "tokenizer": "my_pinyin"
      }
    },
    "tokenizer": {
      "my_pinyin": {
        "type": "pinyin",
        "keep_separate_first_letter": false,
        "keep_full_pinyin": true,
        "keep_original": true,
        "limit_first_letter_length": 16,
        "lowercase": true,
        "remove_duplicated_term": true
      }
    }
  }
}
```

画面7:
```
PUT /medcl/
{
  "index": {
    "analysis": {
      "pinyin_analyzer": {
        "tokenizer": "my_pinyin"
      }
    },
    "tokenizer": {
      "my_pinyin": {
        "type": "pinyin",
        "keep_separate_first_letter": false,
        "keep_full_pinyin": true,
        "keep_original": true,
        "limit_first_letter_length": 16,
        "lowercase": true,
        "remove_duplicated_term": true
      }
    }
  }
}
```

画面10:
```
POST /medcl/folks/_mapping
{
  "folks": {
    "properties": {
      "name": {
        "type": "keyword",
        "fields": [
          {
            "type": "text",
            "store": false,
            "term_vector": "with_offsets",
            "analyzer": "pinyin_analyzer",
            "boost": 10
          }
        ]
      }
    }
  }
}
```

画面11:
```
POST http://192.168.1.7:9200/medcl/folks_search
{
  "query": {
    "match": {
      "name.pinyin": {
        "query": "liu"
      }
    }
  }
}
```

画面12:
```
{
  "query": {
    "match": {
      "name.pinyin": {
        "query": "liu"
      }
    }
  }
}
```

画面13:
```
{
  "query": {
    "match": {
      "name.pinyin": {
        "query": "liu"
      }
    }
  }
}
```

画面14:
```
{
  "took": 7,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 1,
    "max_score": 0.3439677,
    "hits": [
      {
        "_index": "medcl",
        "_type": "folks",
        "_id": "DUNEHgBfypkpuB5eQxr3",
        "_score": 0.3439677,
        "_source": {
          "name": "刘德华"
        }
      }
    ]
  }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2: PPT 标题为“6、拼音分词”，内容说明搜索时需要支持拼音，并提供插件的 GitHub 地址和下载链接。
画面5: PPT 标题为“2.Test Analyzer, analyzing a chinese name, such as 刘德华”，内容包含测试分词器的 GET 请求示例和返回结果。
画面10: PPT 标题为“POST /medcl/folks/_mapping”，内容包含创建索引映射的 JSON 配置。
画面11: PPT 标题为“POST http://192.168.1.7:9200/medcl/folks_search”，内容包含搜索请求的 JSON 配置。
画面14: PPT 标题为“结果”，内容包含搜索结果的 JSON 响应。

5) 不要评价画面美观，不要输出与课程无关的内容。
