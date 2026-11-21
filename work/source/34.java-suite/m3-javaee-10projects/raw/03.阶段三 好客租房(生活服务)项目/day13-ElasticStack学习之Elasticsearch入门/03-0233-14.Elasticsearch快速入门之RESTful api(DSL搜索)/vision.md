# 画面线理解：14.Elasticsearch快速入门之RESTful api（DSL搜索）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\14.Elasticsearch快速入门之RESTful api（DSL搜索）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:27, 02:40, 03:05, 03:12, 03:46, 04:12, 05:09, 06:41, 08:17, 08:33, 09:12, 10:07, 10:17, 10:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:32:47

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Elasticsearch 的 DSL 查询语句进行条件搜索，包括 match 查询、filter 查询和高亮显示功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 PDF 文档目录，当前位于“2.4.7、高亮显示”章节前，页面内容为空白。
画面 2: PDF 页面显示一个 JSON 格式的响应结果，包含 took、timed_out、_shards、hits 等字段。
画面 3: PDF 页面展示一个 POST 请求的 DSL 查询语句，包含 match 和 age 字段。
画面 4: PDF 页面展示一个用户文档的 _source 字段内容，并在下方表格中列出现有数据，包含 id、name、age、sex 字段。
画面 5: 浏览器中打开的 Elasticsearch Head 插件界面，显示索引为 user 的数据列表。
画面 6: PDF 页面展示一个 POST 请求的 DSL 查询语句，包含 bool 和 filter 字段。
画面 7: Postman 软件的“Create New”窗口，提供创建请求、集合、环境、文档、Mock Server 和监控等功能。
画面 8: Postman 中编辑一个 POST 请求，Body 部分包含一个 match 查询，同时显示一个搜索建议框。
画面 9: PDF 页面展示一个 POST 请求的 DSL 查询语句，包含 match 和 age 字段。
画面 10: PDF 页面展示一个 POST 请求的 DSL 查询语句，包含 match 和 name 字段。
画面 11: Postman 中编辑一个 POST 请求，Body 部分包含一个 match 查询，同时显示一个搜索建议框。
画面 12: PDF 页面展示一个 POST 请求的 DSL 查询语句，包含 match 和 name 字段，并在下方显示响应结果。
画面 13: PDF 页面展示一个 POST 请求的 DSL 查询语句，包含 match 和 age 字段，并在下方显示响应结果。
画面 14: PDF 页面展示“2.4.7、高亮显示”章节标题，下方是一个 POST 请求的 DSL 查询语句，包含 match 和 name 字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
{
  "took": 4,
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
    "hits": []
  }
}

画面 3:
POST http://172.16.55.185:9200/haoke/user_search
#请求体
{
  "query": {
    "match": { #match只是查询的一种
      "age": 20
    }
  }
}

画面 4:
{
  "_id": "1001",
  "_source": {
    "name": "张三",
    "age": 20,
    "sex": "男"
  }
}

画面 6:
POST http://172.16.55.185:9200/haoke/user_search
#请求数据
{
  "query": {
    "bool": {
      "filter": {
        "age": 20
      }
    }
  }
}

画面 8:
{
  "query": {
    "match": {
      "name": "张三 李四"
    }
  }
}

画面 11:
{
  "query": {
    "match": {
      "name": "张三 李四"
    }
  }
}

画面 12:
{
  "hits": [
    {
      "_index": "haoke",
      "_type": "user",
      "_id": "BBPe_WcB9rCnF3uebvr",
      "_score": 2.4079456,
      "_source": {
        "id": "1002"
      }
    }
  ]
}

画面 13:
POST http://172.16.55.185:9200/haoke/user_search
#请求体
{
  "query": {
    "match": {
      "age": 20
    }
  }
}

画面 14:
POST http://172.16.55.185:9200/haoke/user_search
#请求体
{
  "query": {
    "match": {
      "name": "张三 李四"
    }
  }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 4: 表格数据：
| _index | _type | _id | _score | id | name | age | sex |
|--------|-------|-----|--------|----|------|-----|-----|
| haoke | user | BbPe_WcB9rCnF3uebvr | 1 | 1002 | 李四 | 40 | 男 |
| haoke | user | 1001 | 1 | 1001 | 张三 | 20 | 男 |
| haoke | user | 1003 | 1 | 1003 | 王五 | 30 | 男 |
| haoke | user | 1004 | 1 | 1004 | 赵六 | 30 | 女 |

画面 5: 表格数据：
| _index | _type | _id | _score | id | name | age | sex |
|--------|-------|-----|--------|----|------|-----|-----|
| haoke | user | C1MDE2qB8S2DPOceRKH | 1 | 1001 | 张三 | 20 | 男 |
| haoke | user | DVMF82qB0S5tPceRlD7 | 1 | 1004 | 赵六 | 24 | 女 |
| haoke | user | D1MFR2qB0S5tPceRlD7 | 1 | 1005 | 孙七 | 23 | 男 |
| haoke | user | C1MFR2qB0S5tPceRlD7 | 1 | 1002 | 李四 | 21 | 女 |
| haoke | user | C1MFR2qB0S5tPceRlD7 | 1 | 1003 | 王五 | 22 | 男 |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
