# 画面线理解：09.WebMagic抓取数据之导入数据到Elasticsearch（创建haoke索引库补充）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\09.WebMagic抓取数据之导入数据到Elasticsearch（创建haoke索引库补充）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:13, 00:17, 00:18, 00:30, 00:35, 00:49, 00:53, 01:22, 01:25, 01:35, 01:38, 01:41, 01:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:05:25

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Elasticsearch 中进行搜索、高亮显示，并通过修改字段映射（如将 index 设置为 false）来理解其对搜索的影响，同时展示如何使用 Docker 部署 Elasticsearch 集群。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示搜索请求的 JSON 结构，包含 match 查询和 highlight 高亮配置，用于搜索标题字段。
画面 2: 展示搜索返回结果，包含文档的详细信息，如 image、title、rent、floor 等字段。
画面 3: 展示搜索结果的高亮部分，高亮文本为“近(地铁/公交) 落北两房小区中间位置 中间楼层 楼房方便”。
画面 4: 展示搜索请求的 JSON 结构，包含 match 查询和 highlight 高亮配置，用于搜索标题字段。
画面 5: 展示使用 Postman 发起的 POST 请求，请求体为 JSON 格式，包含搜索查询和高亮配置。
画面 6: 展示搜索请求的 JSON 结构，包含 image、orientation、houseType、rentMethod、time、title、rent、floor、url 等字段。
画面 7: 展示使用 Postman 发起的 POST 请求，请求体为 JSON 格式，但未正确设置查询参数，导致返回 400 Bad Request。
画面 8: 展示 Postman 返回的错误信息，指出因字段 houseType 未被索引而无法搜索。
画面 9: 展示使用 Typora 编辑的 Docker 命令，用于创建和启动 Elasticsearch 集群节点。
画面 10: 展示 Elasticsearch 字段映射的 JSON 结构，其中 time、rent、floor 字段的 index 设置为 false。
画面 11: 展示搜索请求的 JSON 结构，包含 match 查询和 highlight 高亮配置，用于搜索标题字段。
画面 12: 展示搜索请求的 JSON 结构，包含 highlight 高亮配置，但未包含查询部分。
画面 13: 展示搜索请求的 JSON 结构，包含 match 查询和 highlight 高亮配置，用于搜索 houseType 字段。
画面 14: 展示测试代码，用于批量导入数据，读取 data.json 文件并构建请求体。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```json
POST http://192.168.1.7:9200/haoke/house_search
{
  "query": {
    "match": {
      "title": "地铁"
    }
  },
  "highlight": {
    "fields": {
      "title": {}
    }
  }
}
```

画面 2:
```json
{
  "took": 19,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "failed": 0
  },
  "hits": {
    "total": 1,
    "max_score": 0.2876821,
    "hits": [
      {
        "_index": "haoke",
        "_type": "house",
        "_id": "SH137695162426728448",
        "_score": 0.2876821,
        "_source": {
          "image": "https://imgael.ljcdn.com/31000-inspection/819b8a65-33ff-485c-9aba-88855a19f8",
          "orientation": "3m",
          "houseType": "2室1厅/卫",
          "rentMethod": "租借方式未知",
          "time": "需要装修",
          "title": "近地铁，南北两房小区中间位置 中间楼层 楼房方便",
          "rent": "6200",
          "floor": "高楼层/6层",
          "url": "https://sh.lianjia.com/zufang/SH137695162426728448.html"
        }
      }
    ]
  }
}
```

画面 3:
```json
{
  "took": 19,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "failed": 0
  },
  "hits": {
    "total": 1,
    "max_score": 0.2876821,
    "hits": [
      {
        "_index": "haoke",
        "_type": "house",
        "_id": "SH137695162426728448",
        "_score": 0.2876821,
        "_source": {
          "image": "https://imgael.ljcdn.com/31000-inspection/819b8a65-33ff-485c-9aba-88855a19f8",
          "orientation": "3m",
          "houseType": "2室1厅/卫",
          "rentMethod": "租借方式未知",
          "time": "需要装修",
          "title": "近地铁，南北两房小区中间位置 中间楼层 楼房方便",
          "rent": "6200",
          "floor": "高楼层/6层",
          "url": "https://sh.lianjia.com/zufang/SH137695162426728448.html"
        }
      }
    ]
  }
}
```

画面 4:
```json
POST http://192.168.1.7:9200/haoke/house_search
{
  "query": {
    "match": {
      "title": "地铁"
    }
  },
  "highlight": {
    "fields": {
      "title": {}
    }
  }
}
```

画面 5:
```json
{
  "hits": {
    "total": 1,
    "max_score": 0.2876821,
    "hits": [
      {
        "_index": "haoke",
        "_type": "house",
        "_id": "SH137695162426728448",
        "_score": 0.2876821,
        "_source": {
          "image": "https://imgael.ljcdn.com/31000-inspection/819b8a65-33ff-485c-9aba-88855a19f8",
          "orientation": "3m",
          "houseType": "2室1厅/卫",
          "rentMethod": "租借方式未知",
          "time": "需要装修",
          "title": "近地铁，南北两房小区中间位置 中间楼层 楼房方便",
          "rent": "6200",
          "floor": "高楼层/6层",
          "url": "https://sh.lianjia.com/zufang/SH137695162426728448.html"
        }
      }
    ]
  }
}
```

画面 6:
```json
{
  "image": "SH137695162426728448.jpg",
  "orientation": "3m",
  "houseType": "2室1厅/卫",
  "rentMethod": "租借方式未知",
  "time": "需要装修",
  "title": "近地铁，南北两房小区中间位置 中间楼层 楼房方便",
  "rent": "6200",
  "floor": "高楼层/6层",
  "url": "https://sh.lianjia.com/zufang/SH137695162426728448.html"
}
```

画面 7:
```json
{
  "query": {
    "match": {
      "title": "地铁"
    }
  },
  "highlight": {
    "fields": {
      "title": {}
    }
  }
}
```

画面 8:
```json
{
  "error": "query phase execution exception",
  "reason": "all shards failed",
  "shards": {
    "total": 1,
    "successful": 0,
    "failed": 1
  },
  "failures": [
    {
      "index": "haoke",
      "shard": 0,
      "node": "192.168.1.7:9200",
      "cause": {
        "type": "query_phase_execution_exception",
        "reason": "failed to create query: {\"match\": {\"houseType\": \"地铁\"}}",
        "index": "haoke",
        "type": "house",
