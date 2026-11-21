# 画面线理解：24.Elasticsearch核心详解之过滤查询

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\24.Elasticsearch核心详解之过滤查询【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:27, 00:36, 00:46, 00:51, 01:27, 01:31, 01:57, 02:03, 02:08, 03:21, 03:46, 04:03, 06:05, 06:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:38:54

1) 这一组画面整体在讲 Elasticsearch 中的 term 查询与过滤查询（filter）的区别与用法，通过 PDF 文档和 Postman 工具演示具体示例。

2) 按时间顺序列出每张画面的要点：
画面1: PDF 文档第3.7.1节，讲解 term 查询用于精确匹配，示例包括 age、date、public、tag 字段。
画面2: PDF 文档第3.7.1节，展示 term 查询的示例请求 URL。
画面3: Postman 工具中，向 http://172.16.55.185:9200/hacker/_search 发送包含 term 查询的 JSON 请求体。
画面4: Postman 工具中，JSON Viewer 弹窗显示了请求结果的结构。
画面5: Postman 工具中，展示 term 查询返回的响应结果，包含 hits 数组和文档信息。
画面6: Postman 工具中，展示 term 查询返回的响应结果，包含 hits 数组和文档信息。
画面7: PDF 文档第3.8节，讲解过滤查询，示例为查询年龄为20岁的用户。
画面8: PDF 文档第3.7.1节，展示 term 查询的示例请求 URL。
画面9: PDF 文档第3.8节，讲解过滤查询，示例为查询年龄为20岁的用户。
画面10: PDF 文档第3.7.1节，展示 term 查询的示例请求 URL。
画面11: PDF 文档第3.8节，讲解过滤查询，示例为查询年龄为20岁的用户。
画面12: PDF 文档第3.8节，展示 term 查询返回的文档结构，包含 _score、_source、age 等字段。
画面13: PDF 文档第3.8节，展示 term 查询返回的文档结构，包含 _score、_source、age 等字段。
画面14: PDF 文档第3.8节，展示过滤查询的示例请求 URL。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```json
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
示例：
POST http://172.16.55.185:9200/itcast/person/_search
```

画面3:
```json
{
  "took": 17,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 1,
    "max_score": 0,
    "hits": [
      {
        "_index": "person",
        "_type": "user",
        "_id": "CBE82885:OPccuLQ0",
        "_score": 0,
        "_source": {
          "name": "张三",
          "age": 20,
          "mail": "111@qq.com",
          "hobby": "羽毛球、乒乓球、足球"
        }
      }
    ]
  }
}
```

画面7:
```json
POST http://172.16.55.185:9200/itcast/person/_search
{
  "query": {
    "bool": {
      "filter": {
        "term": {
          "age": 20
        }
      }
    }
  }
}
```

画面12:
```json
{
  "_type": "person",
  "_id": "870M.2oB8cRnF3ux7ud",
  "_score": 0,
  "_source": {
    "name": "张三",
    "age": 20,
    "mail": "111@qq.com",
    "hobby": "羽毛球、乒乓球、足球"
  }
}
```

画面13:
```json
{
  "_type": "person",
  "_id": "870M.2oB8cRnF3ux7ud",
  "_score": 0,
  "_source": {
    "name": "张三",
    "age": 20,
    "mail": "111@qq.com",
    "hobby": "羽毛球、乒乓球、足球"
  }
}
```

画面14:
```json
POST http://172.16.55.185:9200/itcast/person/_search
{
  "query": {
    "bool": {
      "filter": {
        "term": {
          "age": 20
        }
      }
    }
  }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面12、13、14: PDF 文档中包含“查询和过滤的对比”列表，内容如下：
- 一条过滤语句会询问每个文档的字段值是否包含特定值。
- 查询语句会询问每个文档的字段与特定值的匹配程度如何。
- 一条过滤语句会计算每个文档与过滤语句的相关性，会给出一个相关性评分_score，并按照相关性对匹配的文档进行排序。这种评分方式非常适合用于一个没有完全搜索结果的全文搜索。
- 一个简单的文档列表，快速匹配运算并存入内存是十分方便的，每个文档仅需要1个字节。这些缓存的过滤结果集与后续请求的结合使用是非常高效的。
- 查询语句不仅要查找和匹配的文档，还需要计算每个文档的相关性，所以一般来说查询语句要比过滤语句更耗时，并且查询结果也不可缓存。
- 建议：

5) 不要评价画面美观，不要输出与课程无关的内容。
