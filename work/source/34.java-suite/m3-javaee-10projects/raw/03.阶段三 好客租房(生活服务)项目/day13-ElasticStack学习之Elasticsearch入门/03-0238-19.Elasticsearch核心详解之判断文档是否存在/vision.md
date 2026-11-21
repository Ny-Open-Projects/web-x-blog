# 画面线理解：19.Elasticsearch核心详解之判断文档是否存在

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\19.Elasticsearch核心详解之判断文档是否存在【海量资源尽在 ubkz.com】.mp4
- 抽帧：8 帧 @ 01:01, 01:10, 01:40, 01:41, 01:42, 01:44, 02:00, 02:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:35:12

1) 这一组画面整体在讲如何使用 Postman 发起 HTTP 请求并结合 PDF 讲义学习文档是否存在、批量查询等操作。

2) 按时间顺序列出每张画面的要点：

画面 1:
- 使用 Postman 发起 GET 请求，目标 URL 为 http://172.16.55.185:9200/haoke/user/C1ME2g8B5dPceoWlCd
- 请求体（Body）为 JSON 格式，内容为：
  {
    "index": "haoke",
    "type": "user",
    "id": "C1ME2g8B5dPceoWlCd",
    "operation": "get",
    "found": true,
    "source": {
      "id": "1001",
      "name": "张三",
      "age": "21",
      "sex": "男"
    }
  }

画面 2:
- 在 Postman 中将请求方法从 GET 改为 HEAD。
- 点击“Send”按钮发送请求。
- 请求 URL 与画面 1 相同。

画面 3:
- PDF 讲义第 25 页，标题为“3.3、判断文档是否存在”。
- 文本说明：“如果我们只需要判断文档是否存在，而不是查询文档内容，那么可以这样：”
- 展示了一个 HEAD 请求示例：
  HEAD http://172.16.55.185:9200/haoke/user/1005
- 展示了响应结果：
  Status 200 OK Loading time 12 ms
  Request headers: User-Agent, Content-Type, Accept, Accept-Encoding, Accept-Language
  Response headers: content-type, content-length

画面 4:
- PDF 讲义第 25 页，标题为“3.4、批量操作”。
- 子标题“3.4.1、批量查询”。
- 展示了一个 POST 请求示例：
  POST http://172.16.55.185:9200/haoke/user/_mget
- 请求体为：
  {
    "ids": ["1001", "1003"]
  }

画面 5:
- PDF 讲义第 25 页，标题为“3.3、判断文档是否存在”。
- 文本说明：“如果我们只需要判断文档是否存在，而不是查询文档内容，那么可以这样：”
- 展示了 HEAD 请求示例：
  HEAD http://172.16.55.185:9200/haoke/user/1005
- 展示了响应结果：
  Status 200 OK Loading time 12 ms
  Request headers: User-Agent, Content-Type, Accept, Accept-Encoding, Accept-Language
  Response headers: content-type, content-length

画面 6:
- PDF 讲义第 25 页，标题为“3.3、判断文档是否存在”。
- 文本说明：“如果我们只需要判断文档是否存在，而不是查询文档内容，那么可以这样：”
- 展示了 HEAD 请求示例：
  HEAD http://172.16.55.185:9200/haoke/user/1005
- 展示了响应结果：
  Status 200 OK Loading time 12 ms
  Request headers: User-Agent, Content-Type, Accept, Accept-Encoding, Accept-Language
  Response headers: content-type, content-length
- 页面底部显示公司地址和电话。

画面 7:
- PDF 讲义第 25 页，标题为“3.4、批量操作”。
- 子标题“3.4.1、批量查询”。
- 展示了一个 POST 请求示例：
  POST http://172.16.55.185:9200/haoke/user/_mget
- 请求体为：
  {
    "ids": ["1001", "1003"]
  }

画面 8:
- PDF 讲义第 25 页，标题为“3.3、判断文档是否存在”。
- 文本说明：“如果我们只需要判断文档是否存在，而不是查询文档内容，那么可以这样：”
- 展示了 HEAD 请求示例：
  HEAD http://172.16.55.185:9200/haoke/user/1005
- 展示了响应结果：
  Status 200 OK Loading time 12 ms
  Request headers: User-Agent, Content-Type, Accept, Accept-Encoding, Accept-Language
  Response headers: content-type, content-length
- 页面底部显示公司地址和电话。
