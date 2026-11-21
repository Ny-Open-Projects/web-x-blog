# 画面线理解：07.全文搜索之短语匹配

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\07.全文搜索之短语匹配【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:48, 01:55, 02:44, 03:40, 04:02, 04:12, 04:19, 04:26, 04:43, 05:11, 05:32, 05:40, 05:45, 06:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:47:34

1) 这一组画面整体在讲什么（一句话）：
演示如何在Elasticsearch中使用match_phrase查询进行短语匹配，并通过调整slop参数来放宽匹配条件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PDF文档中关于“短语匹配”的章节标题和内容，包含一个JSON格式的查询示例。
画面2：在Postman中发送一个包含match_phrase查询的POST请求，查询字段为“hobby”，查询值为“羽毛球”。
画面3：PDF文档中展示“短语匹配”的定义和示例，查询语句为：POST http://172.16.55.185:9200/itcast/person/_search
画面4：PDF文档中展示如何通过增加slop参数来允许跳过N个词进行匹配，示例查询语句为：POST http://172.16.55.185:9200/itcast/person/_search
画面5：在Postman中发送一个包含match_phrase查询的POST请求，查询字段为“hobby”，查询值为“羽毛球”。
画面6：在Postman中发送一个包含match_phrase查询的POST请求，查询字段为“hobby”，查询值为“羽毛球”。
画面7：在Postman中发送一个包含match_phrase查询的POST请求，查询字段为“hobby”，查询值为“羽毛球”，并显示了返回的JSON结果。
画面8：在Postman中发送一个包含match_phrase查询的POST请求，查询字段为“hobby”，查询值为“羽毛球”。
画面9：在Elasticsearch Head插件中显示了索引“person”的数据，包含字段“name”、“age”、“mail”、“hobby”。
画面10：PDF文档中展示“短语匹配”的定义和示例，查询语句为：POST http://172.16.55.185:9200/itcast/person/_search
画面11：PDF文档中展示“短语匹配”的定义和示例，查询语句为：POST http://172.16.55.185:9200/itcast/person/_search
画面12：PDF文档中展示查询结果的JSON结构，包含“took”、“timed_out”、“_shards”、“hits”等字段。
画面13：PDF文档中展示查询结果的JSON结构，包含“took”、“timed_out”、“_shards”、“hits”等字段。
画面14：PDF文档中展示查询结果的JSON结构，包含“took”、“timed_out”、“_shards”、“hits”等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
POST http://172.16.55.185:9200/itcast/person/_search
{
  "query": {
    "match_phrase": {
      "hobby": "羽毛球"
    }
  },
  "highlight": {
    "fields": {
      "hobby": {}
    }
  }
}

画面4：
POST http://172.16.55.185:9200/itcast/person/_search
{
  "query": {
    "match_phrase": {
      "hobby": "羽毛球足球"
    }
  },
  "highlight": {
    "fields": {
      "hobby": {}
    }
  }
}

画面5：
{
  "took": 40,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 1,
    "max_score": 1.007041,
    "hits": [
      {
        "_index": "itcast",
        "_type": "person",
        "_id": "U0CnDkghB1Sv6b+gZd2",
        "_score": 1.007041,
        "_source": {
          "name": "张三",
          "age": 20,
          "mail": "111@qq.com",
          "hobby": "羽毛球,乒乓球,足球"
        },
        "highlight": {
          "hobby": [
            "(cm)羽毛球(cm)(cm)乒乓球(cm)(cm)足球(cm)"
          ]
        }
      }
    ]
  }
}

画面10：
POST http://172.16.55.185:9200/itcast/person/_search
{
  "query": {
    "match_phrase": {
      "hobby": "羽毛球"
    }
  },
  "highlight": {
    "fields": {
      "hobby": {}
    }
  }
}

画面12：
{
  "took": 2,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 11,
    "max_score": null,
    "hits": []
  }
}

画面13：
{
  "took": 2,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 11,
    "max_score": null,
    "hits": []
  }
}

画面14：
{
  "took": 2,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 11,
    "max_score": null,
    "hits": []
  }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：PPT标题为“1.3、短语匹配”，内容为“在Elasticsearch中，短语匹配意味着不仅仅是词要匹配，并且词的顺序也要一致，如下：”，并附有查询示例。
画面4：PPT标题为“结果结合预期”，内容为“如果觉得这样太过于苛刻，可以增加slop参数，允许跳过N个词进行匹配。示例：”，并附有查询示例。
画面10：PPT标题为“1.3、短语匹配”，内容为“在Elasticsearch中，短语匹配意味着不仅仅是词要匹配，并且词的顺序也要一致，如下：”，并附有查询示例。
画面12：PPT标题为“设置跳过次数”，内容为“{ “query”: { } }”，并附有查询示例。
画面13：PPT标题为“设置跳过次数”，内容为“{ “query”: { } }”，并附有查询示例。
画面14：PPT标题为“设置跳过次数”，内容为“{ “query”: { } }”，并附有查询示例。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
