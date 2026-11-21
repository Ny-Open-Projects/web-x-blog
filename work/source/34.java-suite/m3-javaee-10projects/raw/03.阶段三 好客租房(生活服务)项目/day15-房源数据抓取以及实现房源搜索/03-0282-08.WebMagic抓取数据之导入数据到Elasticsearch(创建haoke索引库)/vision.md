# 画面线理解：08.WebMagic抓取数据之导入数据到Elasticsearch（创建haoke索引库）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\08.WebMagic抓取数据之导入数据到Elasticsearch（创建haoke索引库）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:14, 00:51, 01:57, 02:46, 02:56, 03:11, 03:20, 03:34, 04:04, 04:15, 04:33, 04:39, 05:09, 05:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:04:36

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 HTTP 请求配置 Elasticsearch 索引的映射（mapping），并插入和搜索测试数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了用于创建索引的 PUT 请求，包含 settings 和 mappings 部分，其中 settings 设置了 number_of_shards 和 number_of_replicas。
画面 2: 展示了文档中关于 dynamic 和 index 参数的说明。
画面 3: 展示了索引映射中各个字段的详细配置，包括 title、image、orientation、housetype、rentMethod、time 和 rent 字段。
画面 4: 重复了画面 2 的说明内容。
画面 5: 展示了 Postman 中的 GET 请求界面，用于测试或查看。
画面 6: 展示了 Typora 中的 shell 命令，用于创建三个 Docker 容器（es-node01、es-node02、es-node03）。
画面 7: 展示了 JSON Viewer 中的索引映射配置，与画面 1 内容一致。
画面 8: 展示了 Postman 中的 PUT 请求，用于创建索引，请求体为 JSON 格式，包含 settings 和 mappings。
画面 9: 重复了画面 2 的说明内容。
画面 10: 展示了 Postman 中的 PUT 请求，用于创建索引，请求体为 JSON 格式，包含 settings 和 mappings。
画面 11: 展示了 PDF 文档中用于插入测试数据的 POST 请求和搜索请求的示例。
画面 12: 展示了 Postman 中的 POST 请求，用于插入测试数据，请求体为 JSON 格式。
画面 13: 展示了 Postman 中的 POST 请求，用于执行搜索，请求体为 JSON 格式。
画面 14: 重复了画面 11 的内容，展示搜索请求的示例。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
PUT http://192.168.1.:9200/haoke
{
  "settings": {
    "index": {
      "number_of_shards": 6,
      "number_of_replicas": 1
    }
  },
  "mappings": {
    "house": {
      "dynamic": false,
      "properties": {
        "title": {
          "type": "text",
          "analyzer": "ik_max_word"
        },
        "image": {
          "type": "keyword",
          "index": false
        },
        "orientation": {
          "type": "keyword",
          "index": false
        },
        "housetype": {
          "type": "keyword",
          "index": false
        },
        "rentMethod": {
          "type": "keyword",
          "index": false
        },
        "time": {
          "type": "keyword",
          "index": false
        },
        "rent": {
          "type": "keyword"
        }
      }
    }
  }
}

画面 3:
"title": {
  "type": "text",
  "analyzer": "ik_max_word"
},
"image": {
  "type": "keyword",
  "index": false
},
"orientation": {
  "type": "keyword",
  "index": false
},
"housetype": {
  "type": "keyword",
  "index": false
},
"rentMethod": {
  "type": "keyword",
  "index": false
},
"time": {
  "type": "keyword",
  "index": false
},
"rent": {
  "type": "keyword"
}

画面 6:
cd /haoke/es-cluster/ik
# 停止，删除现有容器
docker stop es-node01 es-node02 es-node03
docker rm es-node01 es-node02 es-node03
# 重新创建容器，挂载ik目录的插件
docker create --name es-node01 -net host -v /haoke/es-cluster/node01/elasticsearc.yml:/usr/share/elasticsearch/config/elasticsearc.yml -v /haoke/es-cluster/node01/jvm.options:/usr/share/elasticsearch/config/jvm.options -v /haoke/es-cluster/ik:/usr/share/elasticsearch/plugins/ik -v /haoke/es-cluster/node01/data:/usr/share/elasticsearch/data elasticsearch:6.5.4
docker create --name es-node02 -net host -v /haoke/es-cluster/node02/elasticsearc.yml:/usr/share/elasticsearch/config/elasticsearc.yml -v /haoke/es-cluster/node02/jvm.options:/usr/share/elasticsearch/config/jvm.options -v /haoke/es-cluster/ik:/usr/share/elasticsearch/plugins/ik -v /haoke/es-cluster/node02/data:/usr/share/elasticsearch/data elasticsearch:6.5.4
docker create --name es-node03 -net host -v /haoke/es-cluster/node03/elasticsearc.yml:/usr/share/elasticsearch/config/elasticsearc.yml -v /haoke/es-cluster/node03/jvm.options:/usr/share/elasticsearch/config/jvm.options -v /haoke/es-cluster/ik:/usr/share/elasticsearch/plugins/ik -v /haoke/es-cluster/node03/data:/usr/share/elasticsearch/data elasticsearch:6.5.4

画面 8:
PUT http://192.168.1.7:9200/haoke
{
  "settings": {
    "index": {
      "number_of_shards": 6,
      "number_of_replicas": 1
    }
  },
  "mappings": {
    "house": {
      "dynamic": false,
      "properties": {
        "title": {
          "type": "text",
          "analyzer": "ik_max_word"
        },
        "image": {
          "type": "keyword",
          "index": false
        },
        "orientation": {
          "type": "keyword",
          "index": false
        },
        "housetype": {
          "type": "keyword",
          "index": false
        },
        "rentMethod": {
          "type": "keyword",
          "index": false
        },
        "time": {
          "type": "keyword",
          "index": false
        },
        "rent": {
          "type": "keyword"
        }
      }
    }
  }
}

画面 11:
POST http://192.168.1.7:9200/haoke/house
{
  "image": "SH21769516242678448.jpg",
  "orientation": "53m",
  "housetype": "2室1厅1卫",
  "rentMethod": "租赁方式未知",
  "title": "房屋装修，品牌家具，建桥四号线地铁口精装两房，",
  "time": "6200",
  "floor": "高楼层/6层",
  "url": "https://sh.lianjia.com/zufang/SH21769516242678448.html"
}

POST http://192.168.1.7:9200/haoke/_search
{
  "query": {
    "match": {
      "title": "租房"
    }
  }
}

画面 12:
POST http://192.168.1.7:9200/haoke/house
{
  "image": "SH21769516242678448.jpg",
  "orientation": "53m",
  "housetype": "2室1厅1卫",
  "rentMethod": "租赁方式未知",
  "title": "房屋装修，品牌家具，建桥四号线地铁口精装两房，",
  "time": "6200",
  "floor": "高楼层/6层",
  "url": "https://sh.lianjia.com/zufang/SH21769516242678448.html"
}

画面 13:
POST http://192.168.1.7:9200/haoke/_search
{
  "query": {
    "match": {
      "title": "租房"
    }
  }
}

画面 14:
POST http://192.168.1.7:9200/haoke/_search
{
  "query": {
    "match": {
      "title": "租房"
    }
  }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
