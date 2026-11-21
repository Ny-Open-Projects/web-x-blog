# 画面线理解：21.Elasticsearch核心详解之分页搜索

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\21.Elasticsearch核心详解之分页搜索【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:43, 00:58, 01:00, 01:02, 01:34, 01:37, 01:41, 01:49, 01:50, 01:51, 01:54, 02:39, 02:40, 04:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:36:51

1) 这一组画面整体在讲 Elasticsearch 中分页查询的实现原理与分片深度分页的问题。

2) 按时间顺序列出每张画面的要点：
画面1: 展示《讲义.pdf》第24.5节“分页显示”内容，说明分页查询参数 size 和 from，给出示例请求：GET /_search?size=5，GET /_search?size=5&from=5，GET /_search?size=5&from=10。
画面2: 在 Elasticsearch Head 插件界面展示索引 haoke 中的 user 类型数据，共5个文档，用于演示分页查询。
画面3: 在 Postman 中构造一个 POST 请求，用于批量删除索引 haoke 中的 user 类型文档，请求体为：{"delete": {"_index": "haoke", "_type": "user", "_id": "2001"}}。
画面4: 在 Postman 中构造一个 GET 请求，用于查询索引 haoke 中的 user 类型文档，URL 为 http://172.16.55.185:9200/haoke/user/_search?from=0&size=5。
画面5: 在 Postman 中展示 GET 请求的响应结果，JSON 格式，包含 took、_shards、hits 等字段，其中 hits 包含 5 个文档。
画面6: 在 Postman 中展示 GET 请求的响应结果，JSON 格式，包含 took、_shards、hits 等字段，其中 hits 包含 5 个文档。
画面7: 在 Postman 中展示 GET 请求的响应结果，JSON 格式，包含 took、_shards、hits 等字段，其中 hits 包含 5 个文档。
画面8: 在 Postman 中展示 GET 请求的响应结果，JSON 格式，包含 took、_shards、hits 等字段，其中 hits 包含 5 个文档。
画面9: 展示《讲义.pdf》第24.5节“分页显示”内容，说明分页查询参数 size 和 from，给出示例请求：GET http://172.16.55.185:9200/haoke/user/_search?size=1&from=2。
画面10: 展示《讲义.pdf》第24.5节“分页显示”内容，说明分页查询参数 size 和 from，给出示例请求：GET http://172.16.55.185:9200/haoke/user/_search?size=1&from=2。
画面11: 展示《讲义.pdf》第24.5节“分页显示”内容，说明分页查询参数 size 和 from，给出示例请求：GET http://172.16.55.185:9200/haoke/user/_search?size=1&from=2。
画面12: 展示《讲义.pdf》第24.5节“分页显示”内容，说明分页查询参数 size 和 from，给出示例请求：GET http://172.16.55.185:9200/haoke/user/_search?size=1&from=2。
画面13: 展示《讲义.pdf》第24.5节“分页显示”内容，说明分页查询参数 size 和 from，给出示例请求：GET http://172.16.55.185:9200/haoke/user/_search?size=1&from=2。
画面14: 展示《讲义.pdf》第3.6节“映射”内容，说明 Elasticsearch 自动判断字段类型，有时需要手动指定。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3:
```json
{
  "delete": {
    "_index": "haoke",
    "_type": "user",
    "_id": "2001"
  }
}
```
画面4:
```json
{
  "took": 22,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "failed": 0
  },
  "hits": {
    "total": 10,
    "max_score": 1,
    "hits": [
      {
        "_index": "haoke",
        "_type": "user",
        "_id": "C1ME2g8B5zDPceWICd",
        "_score": 1,
        "_source": {
          "name": "李四",
          "age": 21
        }
      }
    ]
  }
}
```
画面5:
```json
{
  "took": 22,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "failed": 0
  },
  "hits": {
    "total": 10,
    "max_score": 1,
    "hits": [
      {
        "_index": "haoke",
        "_type": "user",
        "_id": "C1ME2g8B5zDPceWICd",
        "_score": 1,
        "_source": {
          "name": "李四",
          "age": 21
        }
      }
    ]
  }
}
```
画面6:
```json
{
  "took": 22,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "failed": 0
  },
  "hits": {
    "total": 10,
    "max_score": 1,
    "hits": [
      {
        "_index": "haoke",
        "_type": "user",
        "_id": "C1ME2g8B5zDPceWICd",
        "_score": 1,
        "_source": {
          "name": "李四",
          "age": 21
        }
      }
    ]
  }
}
```
画面7:
```json
{
  "took": 22,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "failed": 0
  },
  "hits": {
    "total": 10,
    "max_score": 1,
    "hits": [
      {
        "_index": "haoke",
        "_type": "user",
        "_id": "C1ME2g8B5zDPceWICd",
        "_score": 1,
        "_source": {
          "name": "李四",
          "age": 21
        }
      }
    ]
  }
}
```
画面8:
```json
{
  "took": 22,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "failed": 0
  },
  "hits": {
    "total": 10,
    "max_score": 1,
    "hits": [
      {
        "_index": "haoke",
        "_type": "user",
        "_id": "C1ME2g8B5zDPceWICd",
        "_score": 1,
        "_source": {
          "name": "李四",
          "age": 21
        }
      }
    ]
  }
}
```
画面9:
```http
GET http://172.16.55.185:9200/haoke/user/_search?size=1&from=2
```
画面10:
```http
GET http://172.16.55.185:9200/haoke/user/_search?size=1&from=2
```
画面11:
```http
GET http://172.16.55.185:9200/haoke/user/_search?size=1&from=2
```
画面12:
```http
GET http://172.16.55.185:9200/haoke/user/_search?size=1&from=2
```
画面13:
```http
GET http://172.16.55.185:9200/haoke/user/_search?size=1&from=2
```
画面14:
```text
前面我们创建的索引及插入数据，都是由Elasticsearch进行自动判断类型，有时我们需要进行明确字段类型，否则，自动判断的类型和实际需求是不相符的。
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1: PPT标题为“24.5 分页显示”，内容为“size: 结果数，默认10。from: 跳过开始的结果数，默认0。如果你想每
