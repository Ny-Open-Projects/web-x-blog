# 29.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\29.课程总结【海量资源尽在 ubkz.com】.mp4
- 时长 3分26秒（音频 206s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们对今天的课程呢做一个总结那么今天我们首先呢给大家去介绍了一下什么是ElectroStack那么相信大家呢也有一个这样的一个认识了那么后面呢我们就去重点去学习的是ElectroSearch然后呢先去做了一个简单的一个介绍包括后面它的一些这个安装以及它的一些版本的说明然后呢安装呢我们讲了有单机版的安装
[00:25] 还有我们的基于Docker的安装但是我们没有讲集群的安装集群的安装放到我们下一天来做一个讲解那么我们后面又安装了一个Elixir的一个Hand它的一个辅助工具的这样的一个使用那么它有四种安装方式我们推荐使用第二和第三种当然我最推荐的是第三种方式OK好那么下面我们又讲了一些
[00:49] Elexus中的一些基本的概念包括它的索引文档的映射文档类型等等然后后面我们是为了重点去讲了它的RESTful的API包括它的一些CLUD的一些操作对吧OK好那么这个我们就不详细再说了然后后面我们也讲了它的一些核心内容的一些详解那么包括我们讲了文档然后后面我们讲了响应的查询
[01:16] 以及我们去判断文档是否存在然后我们又去讲了什么批量的操作批量操作可以做批量的查询也可以做批量的插入也可以做批量的删除都是可以的
[01:32] 然后后面我们又讲了分页有了这个分页之后我们是不是就可以去做一个搜索这个页面中下面这个分页这样的一个功能然后在这个分页中其实我们重点给大家讲的是这个内容就是我们在集群系统中的一个深度的一个分页这个大家一定要有这样的一个意识OK后面我们也讲了我们这个映射那么去讲了它
[01:56] 的一些这个类型如何去制定它的定义它的一些字段的类型啊那这个我们都讲过然后呢后面我们讲了它结构化的现在查询啊包括有什么特末呢特末斯啊等等这个我们就不重复了然后后面我们讲了过滤查询那么在这个点呢其实我们一个重点会落到哪里或者落到这个位置来
[02:14] 就是我们的一个过滤查询跟我们的一个我们的一个条件查询那么可以得到相同的一个结果也可以实现相同的功能那究竟我们应该选择过滤查询还是我们的一个查询就是条件查询呢那么其实呢对吧也做了一些这样的一个分析也得出这样的一个建议对吧如果说你在做准确搜索的时候建议使用过滤那么如果是需要做一些分池进行搜索的话那么使用的就是我们的一个查询了OK
[02:39] 好那么在最后呢我们讲了这个中文分词那么首先我们讲的是什么是分词然后呢又讲了一些分词的一些API然后呢后面我们重点是不是讲了他的一些这个内置分词以及他的一些这个内置分词尤其重啊后面我们重点是不是讲了他的中文分词啊那么中文分词呢我们重点讲的是IK分词器的一个使用啊以及后面我们做了一个补充就是我们去演示了一下如何去做一个自定义词库的一个这样的一个操作哎OK
[03:09] 好那么到这里我们基本上就应该能够把electrode就基本的玩起来了对吧但是我们还没有去讲他的一些Java端的一些API怎么去使用这个能不能防到下一天的课程去做一个讲解OK好那么这个就是我们今天所有的课程的内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
本课程系统讲解了Elastic Stack（ELK）的组成、安装方式、RESTful API操作、以及中文分词机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：介绍Elastic Stack概念，说明ELK是Elasticsearch、Logstash、Kibana的简称，后加入Beats形成Elastic Stack。
画面2：介绍Elasticsearch是Elastic Stack的核心，是一个分布式、RESTful风格的搜索和数据分析引擎。
画面3：展示Elasticsearch官方下载页面，提供GA RELEASE和PREVIEW RELEASE选项，版本号为6.5.4，发布日期为2018年12月19日。
画面4：展示一个Docker-compose.yml配置文件，用于安装Elasticsearch集群，包含集群名称、版本、构建类型等信息。
画面5：展示Elasticsearch的Web界面，显示索引“haoke”及其文档ID，建议使用Chrome插件或Docker安装。
画面6：介绍RESTful API，展示创建非结构化索引的PUT请求，包含settings配置，如分片数和副本数。
画面7：展示在URL中添加“pretty”参数以美化JSON返回结果，示例为查询user/1005。
画面8：展示一个404 Not Found的HTTP响应，说明请求的资源不存在。
画面9：展示GET请求查询用户数据，返回结果包含命中文档的ID和得分。
画面10：介绍过滤查询，展示使用term过滤年龄为20岁的用户，使用POST请求。
画面11：介绍中文分词，说明分词是将中文文本切分为词元的过程。
画面12：展示“我爱炒肉丝”分词后的结果，包含三个词元：“我”、“爱”、“炒肉丝”，并标注了每个词元的起止位置。
画面13：介绍IK分词器，说明其支持多种分词模式，如Standard、Simple、Whitespace等，并推荐使用IK分词器。
画面14：展示“中国人”分词后的结果，包含一个词元“中国人”，并标注了其起止位置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4：
{
  "name": "wwwBb",
  "cluster_name": "Docker-cluster",
  "cluster_uuid": "jeVMessRT2k3vC500aW90g",
  "version": "6.5.4",
  "build_flavor": "default",
  "build_type": "tar",
  "build_hash": "dfe8a3",
  "build_date": "2018-12-17T21:17:40.788849Z",
  "build_snapshot": false,
  "lucene_version": "7.5.0",
  "minimum_index_compatibility_version": "5.6.0",
  "tagline": "You Know, for Search"
}

画面6：
PUT http://172.16.55.185:9200/haoke
{
  "settings": {
    "index": {
      "number_of_shards": "2", #分片数
      "number_of_replicas": "0" #副本数
    }
  }
}

画面7：
GET http://172.16.55.185:9200/haoke/user/1005?pretty

画面9：
GET http://172.16.55.185:9200/haoke/user/_search?size=1&from=2

画面10：
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

画面12：
{
  "-tokens": [
    {
      "token": "我",
      "start_offset": 0,
      "end_offset": 1,
      "type": "CN_CHAR",
      "position": 0
    },
    {
      "token": "爱",
      "start_offset": 1,
      "end_offset": 2,
      "type": "CN_CHAR",
      "position": 1
    },
    {
      "token": "炒肉丝",
      "start_offset": 2,
      "end_offset": 5,
      "type": "CN_WORD",
      "position": 2
    }
  ]
}

画面14：
{
  "tokens": [
    {
      "token": "我",
      "start_offset": 0,
      "end_offset": 1,
      "type": "CN_CHAR",
      "position": 0
    },
    {
      "token": "是",
      "start_offset": 1,
      "end_offset": 2,
      "type": "CN_CHAR",
      "position": 1
    },
    {
      "token": "中国人",
      "start_offset": 2,
      "end_offset": 5,
      "type": "CN_WORD",
      "position": 2
    }
  ]
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：标题为“1、Elastic Stack简介”，内容包括ELK的组成和Elastic Stack的形成过程。
画面2：标题为“Elastic Stack 的核心”，内容描述Elasticsearch作为核心的功能。
画面3：标题为“2.2.2、下载”，内容为Elasticsearch官方下载页面截图，包含版本号、发布日期和许可证信息。
画面4：标题为“2.2.5、Elasticsearch-head”，内容说明Elasticsearch-head的作用和安装方式。
画面5：标题为“2.3、基本概念”，内容为Elasticsearch的Web界面截图。
画面6：标题为“2.4、RESTful API”，内容为RESTful API的介绍和创建索引的示例。
画面7：标题为“3.2.1、pretty”，内容为在URL中添加“pretty”参数以美化JSON返回结果。
画面8：标题为“3.2.2、判断文档是否存在”，内容为HTTP响应状态码404 Not Found。
画面9：标题为“3.2.3、分页”，内容为GET请求查询用户数据并返回结果。
画面10：标题为“3.8、过滤查询”，内容为使用term过滤年龄为20岁的用户。
画面11：标题为“4、中文分词”，内容为中文分词的介绍。
画面12：标题为“4.1、什么是分词”，内容为“我爱炒肉丝”分词后的结果。
画面13：标题为“4.2、IK分词器”，内容为IK分词器的介绍和推荐使用。
画面14：标题为“4.2、中文分词”，内容为“中国人”分词后的结果。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

