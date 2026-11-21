# 画面线理解：22.Elasticsearch核心详解之映射

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\22.Elasticsearch核心详解之映射【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:19, 04:16, 04:24, 04:37, 05:45, 06:07, 06:26, 06:44, 07:05, 07:21, 07:39, 08:02, 08:19, 08:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:37:25

1) 这一组画面整体在讲如何使用 Postman 工具对 Elasticsearch 进行索引映射创建、数据批量插入和基于字段的搜索操作。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PDF 文档中关于 Elasticsearch 支持的数据类型说明，包括 JSON 类型与对应 Elasticsearch 类型的映射表。
画面2：Postman 中准备发送一个 PUT 请求到 /_mapping 路径，用于创建索引映射。
画面3：PDF 文档中展示了一个具体的索引映射 JSON 结构，定义了 person 类型下 name、age、mail、hobby 字段的类型。
画面4：Postman 中将 PDF 中的映射 JSON 结构粘贴到请求体中，准备发送 PUT 请求。
画面5：Postman 中发送了 PUT 请求，成功返回了索引映射的 JSON 结构，显示了字段定义。
画面6：Postman 中显示了 GET 请求返回的索引映射 JSON 结构，与之前 PUT 请求结果一致。
画面7：Postman 中准备发送一个 POST 请求到 /_bulk 路径，用于批量插入数据。
画面8：Elasticsearch Head 插件界面，显示了索引 "icast" 中的数据列表，包含 name、age、mail、hobby 字段。
画面9：PDF 文档中展示了另一个索引映射 JSON 结构，与画面3的结构类似。
画面10：Postman 中准备发送一个 POST 请求到 /person_search 路径，用于执行搜索。
画面11：Postman 中显示了 JSON Viewer 窗口，展示了一个简单的查询 JSON 结构。
画面12：Postman 中发送了 POST 请求，返回了搜索结果，包含 total、hits 等字段。
画面13：Postman 中发送了包含 "name": "王五" 的搜索请求，返回了匹配的文档。
画面14：PDF 文档中再次展示了 Elasticsearch 支持的数据类型说明表。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面3：
```json
{
  "mappings": {
    "person": {
      "properties": {
        "name": {
          "type": "text"
        },
        "age": {
          "type": "integer"
        },
        "mail": {
          "type": "keyword"
        },
        "hobby": {
          "type": "text"
        }
      }
    }
  }
}
```

画面4：
```json
{
  "mappings": {
    "person": {
      "properties": {
        "name": {
          "type": "text"
        },
        "age": {
          "type": "integer"
        },
        "mail": {
          "type": "keyword"
        },
        "hobby": {
          "type": "text"
        }
      }
    }
  }
}
```

画面7：
```json
{
  "index": "icast",
  "type": "person",
  "properties": {
    "age": {
      "type": "integer"
    },
    "hobby": {
      "type": "text"
    },
    "mail": {
      "type": "keyword"
    },
    "name": {
      "type": "text"
    }
  }
}
```

画面10：
```json
{
  "query": {
    "match": {
      "hobby": "看电影"
    }
  }
}
```

画面12：
```json
{
  "total": 1,
  "max_score": 1.9056605,
  "hits": [
    {
      "_index": "icast",
      "_type": "person",
      "_id": "EFP6CgB832DPOccxIBq",
      "_score": 1.9056605,
      "_source": {
        "name": "王五",
        "age": 24,
        "mail": "555@qq.com",
        "hobby": "看电影、听音乐、看小说"
      }
    }
  ]
}
```

画面13：
```json
{
  "index": "icast",
  "type": "person",
  "_id": "EFP6CgB832DPOccxIBq",
  "_score": 0.4029972,
  "_source": {
    "name": "王五",
    "age": 24,
    "mail": "555@qq.com",
    "hobby": "看电影、听音乐、看小说"
  }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1、画面14：PPT 标题为“3.6、映射”，表格数据如下：
| JSON type | Field type |
| --- | --- |
| Boolean: true or false | "boolean" |
| Whole number: 123 | "long" |
| Floating point: 123.45 | "double" |
| String, valid date: "2014-09-15" | "date" |
| String: "foo bar" | "string" |

画面3、画面9：PPT 表格数据如下：
| 类型 | 表示的数据类型 |
| --- | --- |
| String | string, text, keyword |
| Whole number | byte, short, integer, long |
| Floating point | float, double |
| Boolean | boolean |
| Date | date |

5) 无。
