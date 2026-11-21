# 画面线理解：18.Elasticsearch核心详解之查询响应

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\18.Elasticsearch核心详解之查询响应【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:24, 00:51, 01:06, 01:15, 01:23, 01:28, 01:36, 02:05, 02:40, 03:01, 03:27, 03:33, 03:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:34:47

1) 这一组画面整体在讲什么（一句话）：
讲解 Elasticsearch 查询响应的格式，包括如何使用 pretty 参数美化输出，以及如何指定返回的字段。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中“3.2.1. pretty”小节，说明可在查询 URL 后添加 pretty 参数使 JSON 更易读，并展示带 pretty 参数的查询结果。
画面 2: 浏览器打开一个新标签页，准备进行后续操作。
画面 3: 浏览器地址栏中输入了 Elasticsearch 的查询 URL，准备发送请求。
画面 4: PDF 文档中“3.2.1. pretty”小节，展示带 pretty 参数的查询结果，包含用户信息。
画面 5: Postman 工具中，展示一个 POST 请求，用于查询用户信息，请求体包含 JSON 数据。
画面 6: Postman 工具中，展示一个 GET 请求，用于查询用户信息，请求 URL 包含查询参数。
画面 7: PDF 文档中“3.2.2. 指定响应字段”小节，说明可以指定需要返回的字段，并展示一个 GET 请求示例。
画面 8: Postman 工具中，展示一个 GET 请求，用于查询用户信息，请求 URL 包含查询参数。
画面 9: Postman 工具中，展示一个 GET 请求，用于查询用户信息，请求 URL 包含查询参数。
画面 10: PDF 文档中“3.2.2. 指定响应字段”小节，说明可以指定需要返回的字段，并展示一个 GET 请求示例。
画面 11: PDF 文档与 Postman 工具并排显示，展示如何通过指定字段来获取用户信息。
画面 12: PDF 文档中“3.2.2. 指定响应字段”小节，展示一个 GET 请求示例，仅返回 _source 字段。
画面 13: Postman 工具中，展示一个 GET 请求，用于查询用户信息，请求 URL 包含查询参数。
画面 14: PDF 文档中“3.2.2. 指定响应字段”小节，展示一个 GET 请求示例，仅返回 _source 字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```json
{
  "_index": "haoke",
  "_type": "user",
  "_id": "1006",
  "_version": 1,
  "found": true,
  "_source": {
    "id": 1006,
    "name": "孙七",
    "age": 37,
    "sex": "女",
    "card": {
      "card_number": "123456789"
    }
  }
}
```

画面 4:
```json
{
  "_index": "haoke",
  "_type": "user",
  "_id": "1006",
  "_version": 1,
  "found": true,
  "_source": {
    "id": 1006,
    "name": "孙七",
    "age": 37,
    "sex": "女",
    "card": {
      "card_number": "123456789"
    }
  }
}
```

画面 7:
```http
GET http://172.16.55.185:9200/haoke/user/1005?_source=id,name
```

画面 10:
```http
GET http://172.16.55.185:9200/haoke/user/1005?_source=id,name
```

画面 12:
```http
GET http://172.16.55.185:9200/haoke/user/1005?_source=id,name
```

画面 14:
```http
GET http://172.16.55.185:9200/haoke/user/1005?_source
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
