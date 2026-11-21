# 08.WebMagic抓取数据之导入数据到Elasticsearch（创建haoke索引库）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\08.WebMagic抓取数据之导入数据到Elasticsearch（创建haoke索引库）【海量资源尽在 ubkz.com】.mp4
- 时长 5分47秒（音频 347s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么前面呢我们已经成功的向我们的集群中添加了IK分子器那么下面呢我们就来看一下如何去创建我们的锁影然后呢以及锁影的一个定义那么下面我们来看一下这个mapping的一个定义那么我们这个锁影的名字叫做后刻然后呢我们这个type呢是这个house然后呢我们来看一下它的一个setting在setting中呢我们会发现它有两个配置项
[00:28] 一个这个呢6代表着配置的我们是一个6个分片对吧然后呢这个1代表的是我们是每一个分片会有一个复文然后呢下面我们来看一下这个mappingmapping中呢首先指定的是type的名称叫做host然后呢注意这个我们前面可能没说过它呢是demonic就是是否是动态的我们把它设置为force那么它默认是什么呢来看一下默认的是true默认是true表示什么呢如果我们这个结构中
[00:57] 当我们去插入一条数据的时候那么如果我们在结构里面没有定义这样的一个字段的话它会自动新增一个字段那么如果为false的话就代表着什么呢我们不允许自动新增这个字段但是文档可以去写入但是对文档的文档的这个对于这个字段就没有办法进行做查询的一些操作了那我们选择把它设置为false然后还有一种是严格模式就是说如果当你插入一条数据的时候
[01:24] 发现携带了一个我们之前没有定义的一个字段的话那么就会爆出是这样的意思所以我们选择把它设置为False然后接着继续往下面看那么下面就是一系列的我们的字段标题我们把它设置为是一个Text就是可以被索引的或者说被分词的这样的一种类型然后它的分词器指定的是IK分词器然后下面的一些图片还有我们的这个是
[01:51] 这个是我们那个平均数就是我们大小然后还是房屋的这个户型结构等等然后在这些里面我们全部把它设置为是一个K word就是说不需要做一个分词不需要做分词了并且我们把它设置为index等于force猫号forceindex又是什么意思就代表着这个字段能不能作为一个查询的条件去做一个或者查询的一个字段去做一个查询
[02:19] 那么如果在这个位置把它设置为false的话那么就意味着这个字段是不能不能够通过这个索引这样的字段去做查询的那么其实我们可以想一下那么我们现在要做的是不是就是去搜索房源数据那么我们其实仅仅需要根据这个标题去做一个搜索就足够了那么下面字段是不是就没有必要去做一个搜索了所以说我们把这个index全部给它设置为falseOK就是这样的一个意思
[02:47] 好那么下面呢我们把这个索引库来创建一下那把这个代码呢我们来拷贝一下好那么我们来创建一下在这个位置呢我们把它拷贝过来然后呢这个检查一下啊19168 1.7 9200好客没有问题然后呢发起是一个put请求那么我们把这个下面的内容呢都拷贝过来那么我们就先拷到先拷到这个jsonvue中然后呢我们做一个格式化
[03:14] 然后呢把下面的这个内容我们拷贝一下一直拷贝到这儿然后呢网站一丢format一下然后呢做一个拷贝然后呢我们去添加一个请求的一个body然后呢类型呢是json类型然后呢网站一丢这个就是我们的这样的一个结构然后呢点击一个上载发送那我们来看一下这个索引库能不能创建成功呢从这个位置来看它已经创建成功了
[03:42] 那么从我们这个工具里面查看一下走那么会发现现在我们这个浩克的这个索引库是不是就已经创建成功了它有0到5对吧0到5说明它有6个这个节点每一个节点都有一个副本一个副本一个副本OK好那么现在我们是不是就已经把我们这个mapping是不是都已经设置好了那么接下来我们尝试着去先插入一条数据我们来做一个测试
[04:11] 那么我们把这个地址我们拷贝过来然后呢我们去给他发起一个post请求把我们这个数据拿过来这个数据呢就是我们刚刚所拿到的数据那么再大家提一下啊就是我们这个数据呢是在我们的这个课前的那个资料里面的大家能够找到完整的去这样的一份数据的啊那我们把这个就拷贝过来那么拷贝到我们的这个postman里面然后呢我们做一个提交
[04:38] 这样的话我们就新增了一条数据对吧好那么接下来我们是不是就可以尝试的去做一下搜索那么来看一下怎么搜索呢比如说我们去搜一下这个地铁对吧地铁关键字然后呢把它我们把它拷贝一下把它拷贝过来然后呢拷贝到这个位置然后呢下面这个位置是不是要加一个下滑线这个斜杠下滑线来一个什么search做一个搜索走
[05:08] 那么我们的查询关键证是地铁那么来看一下查询的结果显然能够匹配到我们这条数据并且对地铁这个词已经做了高亮显示那就说明我们现在IK分子器没有问题那么我们索引库的创建没有问题你看可以看到在这个位置是不是都是我们的原数据没有任何问题对吧并且我们现在也成功的去可以插入数据去搜索没有问题了那么接下来我们其实要做的事情是不是就可以把我们前面抓取的数据
[05:38] 全部都导入到我们的这个elite设置中是不是就可以了OK好那么关于这个mapping的一个创建我们先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
Docker stop es-node01 es-node02 es-node03
Docker rm es-node01 es-node02 es-node03
# 重新创建容器，挂载ik目录的插件
Docker create --name es-node01 -net host -v /haoke/es-cluster/node01/elasticsearc.yml:/usr/share/Elasticsearch/config/elasticsearc.yml -v /haoke/es-cluster/node01/jvm.options:/usr/share/Elasticsearch/config/jvm.options -v /haoke/es-cluster/ik:/usr/share/Elasticsearch/plugins/ik -v /haoke/es-cluster/node01/data:/usr/share/Elasticsearch/data Elasticsearch:6.5.4
Docker create --name es-node02 -net host -v /haoke/es-cluster/node02/elasticsearc.yml:/usr/share/Elasticsearch/config/elasticsearc.yml -v /haoke/es-cluster/node02/jvm.options:/usr/share/Elasticsearch/config/jvm.options -v /haoke/es-cluster/ik:/usr/share/Elasticsearch/plugins/ik -v /haoke/es-cluster/node02/data:/usr/share/Elasticsearch/data Elasticsearch:6.5.4
Docker create --name es-node03 -net host -v /haoke/es-cluster/node03/elasticsearc.yml:/usr/share/Elasticsearch/config/elasticsearc.yml -v /haoke/es-cluster/node03/jvm.options:/usr/share/Elasticsearch/config/jvm.options -v /haoke/es-cluster/ik:/usr/share/Elasticsearch/plugins/ik -v /haoke/es-cluster/node03/data:/usr/share/Elasticsearch/data Elasticsearch:6.5.4

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

