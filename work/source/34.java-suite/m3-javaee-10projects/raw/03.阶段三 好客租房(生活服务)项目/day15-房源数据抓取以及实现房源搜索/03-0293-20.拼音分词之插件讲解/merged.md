# 20.拼音分词之插件讲解

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\20.拼音分词之插件讲解【海量资源尽在 ubkz.com】.mp4
- 时长 6分4秒（音频 364s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么现在我们这个集群呢就跑起来了没有问题那么下面呢我们来测试一下我们这个拼一分词看有没有问题啊那么我们还是采用这个就是这个官方的这样的一个测试啊我们来测一下这样吧我们打开它这个打开这个插件的一个地址这样的话我们拷贝这个它的一个代码会相对会比较方便一点啊那么首先第一个呢它的一个测试呢是这样的就发起一个put请求创建这样的一个索引那我们先根据它的一个测试啊
[00:29] 这么来一下然后呢9200然后呢到这然后呢我们把这个拷贝过来然后呢做一个做一个什么呢做一个put星球put星球走等待他的一个执行好创建好了那么来看一下那么这个所以呢他就已经创建完成了好嘞好搞定然后呢我们接着继续往下面看那么然后我们接着继续
[01:03] 现在这个就搞定了然后我们来看一下下面它的一个操作就是我们去尝试去做一个分词它通过刘德华去做一个分词然后我们需要注意的是在我们刚刚所创建的索引中它其实是做了一个分词器的定义叫做这个叫P1Underlayer分词器的一个定义然后这个token使用的是myP1下面对myP1做了一些定义
[01:33] 做了这样的一个配置就是这个意思然后我们来测试一下就是我们把它拷贝到这个里面来多了一个斜杠是吧多了一个斜杠0到这斜杠然后我们去尝试的去对这个刘德华去做一个拼音的一个分词看他会怎么样走那么拼音的这个分词可以他接受的是一个post走然后可以看到的结果是不是就是一个你看刘
[02:01] 是吧德华刘德华然后呢LDH简写德华哎OK那么显然是不是已经对拼音是不是做了一个支持了哎OK好嘞那么这个呢就他的一个基本的一个小例子啊当然了在这个在这个他的参数也有一些系列参数啊那么有一些这个参数大家可以自己去阅读一下包括这个第一个参数是不是我们要开启这个简写这种啊然后呢还有是这个
[02:30] 他剪写的一个长度是多少啊啊等等的这个我们就不详细说这个参数了啊那我们保一般保持默认他这个默认就可以了呃然后呢这个是做一个测试这个是结果ok然后呢也可以去创建一个这个麦品去写一些数据然后呢做一些这个搜索那么我们下面给他创建一个这个麦品啊创建一个麦品那么我们来操作一下吧那把它拿过来然后呢呃这个
[02:58] 最要注意的是在这个Mapping里面可能跟我们前面讲的稍微有一点不一样就是这个里面他使用了一个注意来看一下这个是他的一个type对吧type然后下面这个是他的proposy然后呢name是他的一个字段然后呢这个字段的一个类型然后下面呢要注意这个就有点不太一样了在这个位置呢是指定了一个他这个字段的一个子的一个字段他内部这个字段是谁呢拼音这样的意思
[03:26] 那么这个是什么意思就是说在elastic中它支持为一个字段添加子字段这样做的目的就是我们可以对一个字段进行不同的搜索你可以比如说我可以我对我内母可以做ik分子器也可以通过拼音分子器去做做这样去做那么我可以添加不同的一个字段是这个意思叫子字段ok通过field来完成好嘞那么我们来把这个创建出来
[03:57] 然后呢把它丢到这个位置来往上面去丢走走那么可以看到是不是已经创建OK好那么下面我们来测试一下测试一下那么比如说我们去插入这么一条数据插入一条数据然后呢做一个测试大家就能够明白了那么发起pose请求把这个刘德华这个数据我们插入进去走那么这个数据是不是就已经插入完成了那么下面我们来做一个搜索
[04:25] 那么我们就在下面这个下改成一个下滑线一个search然后查询的一个查询的一个字符串我们来看一下查询字符串叫query match那么我们就我们的目的写一下了那么就自己写那就写一个叫做query然后它所匹配的是一个什么的match匹配谁是个匹配的是一个我们先这样测
[04:57] 不是title是内母内母谁呢内母刘德华那么这个能不能匹配到呢看一下是不是他可以查询到书记没有问题那么如果我们查询这个刘德华要查询这个刘德华这个他能查到吗查不到那为什么查不到呢你并不是你不能通过这个内母这段查询你要通过这个内母的子字段去做查询去点拼音这个字段去查询看他能不能查到你会发现
[05:29] 它可以查到数据OK其实这个就是一个拼音分子器的一个使用拼音分子器的使用那么OK好那么我们接着继续往下面看那么通过这种方式是不是做查询当然了你也可以设置它的一个简写叫刘德华然后走来看一下那么是不是就是这样一个效果也是一样的也是一样的OK好那么这个就是
[05:55] 我们所演示的一个这样的一个拼音这个插件的一个使用OK好那么关于这个拼音插件的使用呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Elasticsearch 中配置和测试拼音分词插件，以实现对中文姓名等文本的拼音搜索功能。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 Docker 创建 Elasticsearch 节点的命令，以及测试拼音分词的 PUT 请求示例。
画面2: 展示了课程文档中“6、拼音分词”章节，说明搜索时需要支持拼音，并提供了插件的 GitHub 地址和下载链接。
画面3: 展示了 GitHub 上的拼音分词插件文档，包含创建索引时的配置代码。
画面4: 展示了 Postman 中发送 PUT 请求创建索引的界面，请求体为创建索引的 JSON 配置。
画面5: 展示了 GitHub 文档中测试分词器的 GET 请求示例和返回结果。
画面6: 展示了 Postman 中发送 GET 请求测试分词器的界面。
画面7: 展示了课程文档中“6.2、测试拼音分词”章节，包含创建索引的 PUT 请求示例。
画面8: 展示了课程文档中“6.2、测试拼音分词”章节的末尾部分，包含插件参数说明。
画面9: 展示了 Postman 中发送 POST 请求测试分词器的界面，返回结果为分词后的 token。
画面10: 展示了课程文档中创建索引映射的 POST 请求示例，配置了 name 字段的类型和分词器。
画面11: 展示了课程文档中搜索请求的 POST 请求示例，配置了 match 查询和拼音分词器。
画面12: 展示了 Postman 中发送 POST 请求进行搜索的界面，输入框中输入“刘德华”并显示拼音搜索建议。
画面13: 展示了 Postman 中发送 POST 请求进行搜索的界面，请求体为 match 查询。
画面14: 展示了搜索结果的 JSON 响应，包含匹配到的文档信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```
Docker create --name es-node02 --net host -v /haoke/es-
cluster/pinyin:/usr/share/Elasticsearch/plugins/pinyin -v /haoke/es-
cluster/node02/Elasticsearch.yml:/usr/share/Elasticsearch/config/Elasticsearch.yml
-v /haoke/es-cluster/node02/jvm.options:/usr/share/Elasticsearch/config/jvm.options
-v /haoke/es-cluster/ik:/usr/share/Elasticsearch/plugins/ik -v /haoke/es-
cluster/pinyin:/usr/share/Elasticsearch/plugins/pinyin -v /haoke/es-
cluster/node02/data:/usr/share/Elasticsearch/data Elasticsearch:6.5.4
Docker create --name es-node03 --net host -v /haoke/es-
cluster/pinyin:/usr/share/Elasticsearch/plugins/pinyin -v /haoke/es-
cluster/node03/Elasticsearch.yml:/usr/share/Elasticsearch/config/Elasticsearch.yml
-v /haoke/es-cluster/node03/jvm.options:/usr/share/Elasticsearch/config/jvm.options
-v /haoke/es-cluster/ik:/usr/share/Elasticsearch/plugins/ik -v /haoke/es-
cluster/pinyin:/usr/share/Elasticsearch/plugins/pinyin -v /haoke/es-
cluster/node03/data:/usr/share/Elasticsearch/data Elasticsearch:6.5.4
```

画面3:
```
PUT /medcl/
{
  "index": {
    "analysis": {
      "pinyin_analyzer": {
        "tokenizer": "my_pinyin"
      }
    },
    "tokenizer": {
      "my_pinyin": {
        "type": "pinyin",
        "keep_separate_first_letter": false,
        "keep_full_pinyin": true,
        "keep_original": true,
        "limit_first_letter_length": 16,
        "lowercase": true,
        "remove_duplicated_term": true
      }
    }
  }
}
```

画面4:
```
{
  "index": {
    "analysis": {
      "pinyin_analyzer": {
        "tokenizer": "my_pinyin"
      }
    },
    "tokenizer": {
      "my_pinyin": {
        "type": "pinyin",
        "keep_separate_first_letter": false,
        "keep_full_pinyin": true,
        "keep_original": true,
        "limit_first_letter_length": 16,
        "lowercase": true,
        "remove_duplicated_term": true
      }
    }
  }
}
```

画面5:
```
GET /medcl/_analyze
{
  "text": ["刘德华"],
  "analyzer": "pinyin_analyzer"
}
```

画面6:
```
{
  "index": {
    "analysis": {
      "pinyin_analyzer": {
        "tokenizer": "my_pinyin"
      }
    },
    "tokenizer": {
      "my_pinyin": {
        "type": "pinyin",
        "keep_separate_first_letter": false,
        "keep_full_pinyin": true,
        "keep_original": true,
        "limit_first_letter_length": 16,
        "lowercase": true,
        "remove_duplicated_term": true
      }
    }
  }
}
```

画面7:
```
PUT /medcl/
{
  "index": {
    "analysis": {
      "pinyin_analyzer": {
        "tokenizer": "my_pinyin"
      }
    },
    "tokenizer": {
      "my_pinyin": {
        "type": "pinyin",
        "keep_separate_first_letter": false,
        "keep_full_pinyin": true,
        "keep_original": true,
        "limit_first_letter_length": 16,
        "lowercase": true,
        "remove_duplicated_term": true
      }
    }
  }
}
```

画面10:
```
POST /medcl/folks/_mapping
{
  "folks": {
    "properties": {
      "name": {
        "type": "keyword",
        "fields": [
          {
            "type": "text",
            "store": false,
            "term_vector": "with_offsets",
            "analyzer": "pinyin_analyzer",
            "boost": 10
          }
        ]
      }
    }
  }
}
```

画面11:
```
POST http://192.168.1.7:9200/medcl/folks_search
{
  "query": {
    "match": {
      "name.pinyin": {
        "query": "liu"
      }
    }
  }
}
```

画面12:
```
{
  "query": {
    "match": {
      "name.pinyin": {
        "query": "liu"
      }
    }
  }
}
```

画面13:
```
{
  "query": {
    "match": {
      "name.pinyin": {
        "query": "liu"
      }
    }
  }
}
```

画面14:
```
{
  "took": 7,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 1,
    "max_score": 0.3439677,
    "hits": [
      {
        "_index": "medcl",
        "_type": "folks",
        "_id": "DUNEHgBfypkpuB5eQxr3",
        "_score": 0.3439677,
        "_source": {
          "name": "刘德华"
        }
      }
    ]
  }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2: PPT 标题为“6、拼音分词”，内容说明搜索时需要支持拼音，并提供插件的 GitHub 地址和下载链接。
画面5: PPT 标题为“2.Test Analyzer, analyzing a chinese name, such as 刘德华”，内容包含测试分词器的 GET 请求示例和返回结果。
画面10: PPT 标题为“POST /medcl/folks/_mapping”，内容包含创建索引映射的 JSON 配置。
画面11: PPT 标题为“POST http://192.168.1.7:9200/medcl/folks_search”，内容包含搜索请求的 JSON 配置。
画面14: PPT 标题为“结果”，内容包含搜索结果的 JSON 响应。

5) 不要评价画面美观，不要输出与课程无关的内容。

