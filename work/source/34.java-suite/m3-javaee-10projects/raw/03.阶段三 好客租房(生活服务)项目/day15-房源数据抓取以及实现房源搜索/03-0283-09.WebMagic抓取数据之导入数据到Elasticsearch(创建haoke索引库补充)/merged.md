# 09.WebMagic抓取数据之导入数据到Elasticsearch（创建haoke索引库补充）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\09.WebMagic抓取数据之导入数据到Elasticsearch（创建haoke索引库补充）【海量资源尽在 ubkz.com】.mp4
- 时长 1分46秒（音频 106s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么我们接着继续那么刚刚我们是通过我们这个query就是我们去title这个字段去做一个query查询那么发现是OK的那么我们可以尝试一下就是假设我们使用其他的一些字段去做一个查询那么看会怎么样那么前面我们是不是已经创建了很多的一些这个字段对吧那么比如说叫一个host type那么我们去搜索一下看它会怎么样
[00:25] 那么前面我们在设置我们mapping的时候是不是设置了一些其他其他字段都是不可被索引的是不是那么我们来测试一下把这个title我们改成一个host type然后我们就把这个内容拷贝过来去做一个搜索然后拷贝到这个位置来然后多了一个引号少了一个引号好了这就对了然后点击send发送走那么会发现它是不是会报错
[00:51] 对吧会报错那么我们来看一下他这个错误内容是什么呢说不能去搜索在这个字段上面去做一个这个搜索那么他不是一个被索引的这样的一个字段那么OK那么也就是会告诉我们什么呢如果以后呢我们在做项目的时候那么我们是不是要去分析一下我们这个mapping中的这些字段哪些需要被索引哪些是不需要被索引的那么一定要搞清楚那么如果不被
[01:18] 不需要被索引的一些字段把它设置为index等于force就可以了你比如说像我们这个里面典型的水像这种图片那么你觉得这个它需要索引吗它一定不需要对吧一定不需要那么OK好那么像这样一些字段就把它设置为force就可以了OK当然这个需要去结合我们的业务来完成好那么这个就是给大家来补充去讲的一个内容对吧我们去做一个这样的一个测试OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

