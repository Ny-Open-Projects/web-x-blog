# 10.轮播广告实现之分析数据结构以及表结构

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\10.轮播广告实现之分析数据结构以及表结构【海量资源尽在 ubkz.com】.mp4
- 时长 3分26秒（音频 207s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来实现啊首页的这个轮播广告的这个功能啊那么在首页中呢我们可以看到是不是有这个轮播这个广告啊就上面的他啊那么接下来呢我们就来分析一下这个功能我们该如何去实现啊那我们来找一下他的一个请求这个是他的请求啊打了这个显然是Obsense啊那么显然肯定是需要通过跨域请求那么这个我们后面再说我们先来看一下
[00:29] 他具体的请求的数据啊这个就是他请求的数据那么请求的数据呢最后是长这个样子的对吧啊长这个样子的啊那么也就是说我们最后可以看到他的数据结构呢就是这样的一个数据结构那么其实我们可以看到在这个里面关键的是不是就是这个URL图片URL我们给他传递这个URL是不是就他能够就把图片是不是就显示出来了哎OK那么比较简单的一种数据结构啊
[00:56] 其实他用数据结构也是相对比较复杂一点的分装还是比较深的这样的一个数据结构这个具体我们到后面我们再分析那么现在我们其实知道
[01:08] 我们只要服务端给他返回这样的一个图片地址那么就能够去实现这样的一个效果那么直到这样就可以了所以接下来我们就需要去来思考一下在我们去为我们的前端提供这样的一个服务的话那么我们应该怎么去做那么我们首先来去看一下我们所设计的一个表结构我们这张表叫TBAD注意我们AD叫做什么的广告对吧
[01:36] 要注意的是我们这张表并不仅仅是为我们的首页的轮播的一个广告去提供一个数据的存储而是为我们整个网站提供一个广告的存储所以我们把这个表命名为叫做AD就广告的意思那么在这个里面我们给它设计了这么几个字段
[02:00] 第一个呢显然这个就不用说了肯定就是ID对吧然后第二个呢是Type就是广告的类型广告类型可能会有很多包括你是首页的广告还是这个其他页面的广告对吧要做一个这样的区分然后呢我们这个里面有一个Title就是你对这个广告的一个描述那么也许有些位置它是需要显示一些文本信息的OK所以呢我们有一个这个Title这样的一个描述还有呢就是关键的一个URL地址
[02:29] 然后下面这两个就可以的update这两个没什么好说的OK好那么我们来看一下我们的表结构表结构那么我们这个表结构显然就是刚刚我们所看到的这样的一个表结构对吧OK好那么这个是我们的表结构那么并且我们给他也做了一些初始数据我们初始了有四条数据这个图片是我们已经上传到我们的
[02:55] 这个阿里云上面对吧这样的一个数据啊其实真实可以访问的一个图片的一个数据OK好那么我们接着继续往下面看那么有了这个表结表结构之后啊那么我们就需要去实现啊我们的一些功能了OK那么具体的这个功能的实现呢我们放到后面啊那么关于我们这个广告位啊
[03:19] 就是轮波广告的一个数据结构以及我们的表结构的设计我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 GraphQL 的前端应用如何通过网络请求获取并展示广告轮播图数据，同时展示后端数据库表结构和数据插入操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 浏览器开发者工具 Network 面板显示对 `/homes/menu` 的 GET 请求，响应状态码 200，响应头包含 `Content-Type: application/json; charset=utf-8`。
画面 2: 浏览器开发者工具 Network 面板显示对 `/homes/slide` 的 GET 请求，响应状态码 200，响应头包含 `Content-Type: application/json; charset=utf-8`。
画面 3: 浏览器开发者工具 Network 面板显示对 `/homes/slide` 的 GET 请求的响应体，内容为 JSON 格式，包含 `meta` 和 `data` 字段，`data` 字段是一个数组，包含多个对象，每个对象包含 `original` 字段，值为图片 URL。
画面 4: 浏览器开发者工具 Network 面板显示对 `/homes/slide` 的 GET 请求的响应体，内容为 JSON 格式，包含 `meta` 和 `data` 字段，`data` 字段是一个数组，包含多个对象，每个对象包含 `original` 字段，值为图片 URL。
画面 5: PDF 文档页面，标题为“3.2、数据库表设计”，显示 SQL 语句 `CREATE TABLE 'tb_ad' ( ... ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='广告表';`。
画面 6: PDF 文档页面，标题为“3.2、数据库表设计”，显示 SQL 语句 `CREATE TABLE 'tb_ad' ( ... ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='广告表';`。
画面 7: PDF 文档页面，标题为“3.2、数据库表设计”，显示 SQL 语句 `CREATE TABLE 'tb_ad' ( ... ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='广告表';`。
画面 8: Navicat Premium 数据库管理工具界面，显示数据库 `myhome` 中的表 `tb_ad` 的 DDL 语句，与 PDF 中的 SQL 语句一致。
画面 9: Navicat Premium 数据库管理工具界面，显示表 `tb_ad` 的数据，选中第 4 行，该行数据为 `id: 4, type: 1, title: '上海周边 爱心 首付38万', url: 'http://itcast-haoke.oss-cn-qingdao.aliyuncs.com/images/2018/11/26/1543203306723104.jpg', created: '2018-11-26 11:28:51', updated: '2018-11-26 11:28:51'`。
画面 10: 浏览器打开一个图片 URL，显示一张房地产广告图片，内容为“融创海逸长洲”、“80-130m² 乐园里的一线海景洋房 首付38万”。
画面 11: PDF 文档页面，标题为“3.3、实现查询接口（dubbo服务）”，显示 SQL 语句 `INSERT INTO 'tb_ad' (...) VALUES ('1', '1', 'Unicity万科天空之城', 'http://itcast-haoke.oss-cn-qingdao.aliyuncs.com/images/2018/11/26/1543202909706227.jpg', '2018-11-26 11:28:49', '2018-11-26 11:28:51');`。
画面 12: PDF 文档页面，标题为“3.3、实现查询接口（dubbo服务）”，显示 SQL 语句 `INSERT INTO 'tb_ad' (...) VALUES ('1', '1', 'Unicity万科天空之城', 'http://itcast-haoke.oss-cn-qingdao.aliyuncs.com/images/2018/11/26/1543202909706227.jpg', '2018-11-26 11:28:49', '2018-11-26 11:28:51');`。
画面 13: PDF 文档页面，标题为“3.1、查看数据结构”，显示请求地址字段，但未显示具体内容。
画面 14: PDF 文档页面，标题为“3.3、实现查询接口（dubbo服务）”，显示 SQL 语句 `INSERT INTO 'tb_ad' (...) VALUES ('1', '1', 'Unicity万科天空之城', 'http://itcast-haoke.oss-cn-qingdao.aliyuncs.com/images/2018/11/26/1543202909706227.jpg', '2018-11-26 11:28:49', '2018-11-26 11:28:51');`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
Request URL: http://127.0.0.1:8086/homes/menu
Request Method: POST
Status Code: 200 OK
Remote Address: 127.0.0.1:8086
Referer Policy: no-referrer-when-downgrade

Response Headers
Access-Control-Allow-Origin: http://localhost:9000
Connection: keep-alive
Content-Length: 597
Content-Type: application/json; charset=utf-8
Date: Tue, 27 Nov 2018 14:08:44 GMT
Vary: Origin
```

画面 2:
```
Request URL: http://127.0.0.1:8086/homes/slide
Request Method: POST
Status Code: 200 OK
Remote Address: 127.0.0.1:8086
Referer Policy: no-referrer-when-downgrade

Response Headers
Access-Control-Allow-Origin: http://localhost:9000
Connection: keep-alive
Content-Length: 212
Content-Type: application/json; charset=utf-8
Date: Tue, 27 Nov 2018 14:08:44 GMT
Vary: Origin
```

画面 3:
```
(data: {}, meta: {status: 200, msg: "请求成功"})
data: [
  {
    "original": "http://127.0.0.1:8086/public/1.png",
    "original": "http://127.0.0.1:8086/public/2.png"
  },
  {
    "original": "http://127.0.0.1:8086/public/3.png"
  },
  {
    "original": "http://127.0.0.1:8086/public/4.png"
  }
]
meta: {status: 200, msg: "请求成功"}
```

画面 5:
```
CREATE TABLE 'tb_ad' (
  'id' bigint(20) NOT NULL AUTO_INCREMENT,
  'type' int(10) DEFAULT NULL COMMENT '广告类型',
  'title' varchar(100) DEFAULT NULL COMMENT '描述',
  'url' varchar(200) DEFAULT NULL COMMENT '图片url地址',
  'created' datetime DEFAULT NULL,
  'updated' datetime DEFAULT NULL,
  PRIMARY KEY ('id')
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='广告表';
```

画面 8:
```
CREATE TABLE 'tb_ad' (
  'id' bigint(20) NOT NULL AUTO_INCREMENT,
  'type' int(10) DEFAULT NULL COMMENT '广告类型',
  'title' varchar(100) DEFAULT NULL COMMENT '描述',
  'url' varchar(200) DEFAULT NULL COMMENT '图片url地址',
  'created' datetime DEFAULT NULL,
  'updated' datetime DEFAULT NULL,
  PRIMARY KEY ('id')
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='广告表';
```

画面 9:
```
id	type	title	url	created	updated
1	1	Unicity万科天空之城	http://itcast-haoke.oss-cn-qingdao.aliyuncs.com/images/2018/11/26/1543202909706227.jpg	2018-11-26 11:28:49	2018-11-26 11:28:51
2	1	天地海海蓝前	http://itcast

