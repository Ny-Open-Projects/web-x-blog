# 19.Elasticsearch核心详解之判断文档是否存在

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\19.Elasticsearch核心详解之判断文档是否存在【海量资源尽在 ubkz.com】.mp4
- 时长 2分7秒（音频 127s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么接下来呢我们来看一下判断文档是否存在大家可以想一下如果现在我们有这样的一个需求的话那么我们应该怎么去做呢我们一个常规的做法是不是我们可以去向我们这个地址去发起一个get请求去查询这条数据那么如果能够查询到数据那就说明这个文档存在如果查询不到的话那就说明这个文档
[00:24] 不存在对不对但是大家可以想一下那么我们现在需求呢仅仅是判断它是否存在而不是想要去获取这条数据那么如果通过get请求它是不是也会获取到这条数据啊对吧这显然是啊不是特别合理的对吧那么在yes中呢它也提供这样的一个操作就是我们可以对我们这个地址然后呢去发起一个什么呢head请求注意不是get请求啊是head请求那么如果响应200要代表着这条数据存在但是呢它不返回数据
[00:53] 仅仅是给你一个状态码告诉你是存在那么如果要不存在的话那就响应的是404那么接下来我们来做一个测试我们来看一下那么我们来看一下那么这个呢是我们所存在的一个数据对吧然后呢如果我们给他发起一个head请求head请求然后呢点击send走那么可以看到他的响应状态码是不是就200那就代表什么呢这条数据存在但是呢他没有任何的数据返回
[01:18] 没有入境任何的数据返回那么如果我们随便写一个比如改成一随便写一个走那么可以看到这条数据那么它的状态能404那就说明什么呢说明这条数据不存在OK那么有了这样的一个操作那么当我们需要去判断某一个文档是否存在的时候是不是就变得非常的容易并且非常非常的高效对吧OK好那么这个就是我们所讲的所讲的这个判断文档是否存在
[01:45] 当然了在下面这个点还有一个友情那个提示啊就说在我们查询的一刻表示文档不存在但不代表以后是不是也不存在啊另外一个进程可能在这个期间去创建了新的文档啊就这个意思啊这个大家应该能够去理解只是代表这个时刻它不存在OK好那么这个就是我们所讲的判断文档是否存在的操作

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

