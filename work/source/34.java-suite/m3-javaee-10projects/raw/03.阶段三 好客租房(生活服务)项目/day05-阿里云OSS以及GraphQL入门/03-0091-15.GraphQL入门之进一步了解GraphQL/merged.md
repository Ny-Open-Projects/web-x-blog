# 15.GraphQL入门之进一步了解GraphQL

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\15.GraphQL入门之进一步了解GraphQL【海量资源尽在 ubkz.com】.mp4
- 时长 7分15秒（音频 435s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么通过前面我们对REST4它的一个问题的一个分析吧那么其实呢我们会发现那REST4呢在某些情况下呢并不是非常的友好的对吧所以呢我们需要进一步的再了解一下GraphQL它是如何去解决REST4中在使用过程中所暴露出来一些问题啊那我们来看一下那么首先第一个呢就是GraphQL呢它可以做到
[00:28] 按需索取避免浪费这个是什么意思呢其实我们可以看一下官方的一个这个在首页中有这样的一个效果来看一下那么我们去进入它的一个首页那么现在打开有点慢那么我们稍等一下那么看下它首页中有这样的一个效果那么其实就在下面的这个位置那么它就显示这样的效果你可以看到当它有两个属性的时候是不是下面显示两个你看
[00:58] 现在有一个那就是显示这个上面这个要注意啊来先讲解一下啊上面的这个是他的一个请求请求的一个参数啊而下面这个呢代表的是服务端的一个响应响应回来的一个数据啊那么我们来看他的一个动态的一个效果当你请求的时候如果有只有一个参数那么服务端就返回一个字段对吧当你有两个的时候能返回两个当你有三个的时候就返回三个那么这样的话是不是就实现这样的一个需求就是
[01:28] 请求你需要的数据不多不少那么你需要一个你就告诉服务员我需要这一个你给我返回一个就可以了我需要两个你给我返回两个就OK那么多余的就不需要再返回给我了所以叫做按需索取对吧按需索取那我们来看一下在我们这个文档中有这样的一个地址它其实也是官方这个文档只是它告诉大家是在
[01:55] 是在这个我们这个学习啊这个里面的有一个变更和查询这个下面吧有这样的一个呃演示啊有这样的演示我们可以看一下这个效果那么你比如说我们把下面的这个给他拿掉你看你会发现哎他所显示的是不是就是一个数据啊要注意的是啊左边这个是不是我们的一个请求请求的一个参数啊那么后面这个是我们的一个响应的一个数据
[02:21] 当我只有一个Name的时候那么它是不是返回一个Name如果我在这个位置有一个ID的时候那么你会发现响应的结果呢它就会有一个ID那么如果呢我这有一个我的一个Friends就是我的一个朋友然后呢朋友下面又显示什么内容呢就显示ID和Name的时候你会发现它是不是在右侧这个位置就会把他的一些这个朋友是吧然后的一些信息是不是就返回来
[02:48] 返回回来并且我们可以返回他的一些这个这个信息对吧这是一些这个所定义的一些枚举的信息到后面我们再说了好那么其实我们就会发现他是不是可以去根据我们请求的一些这个参数来返回我们这个数据对不对这样的话我们是不是就可以实现一个什么呢按需索取避免浪费哎OK
[03:14] 好那么这个就是他所解决的第一个这个问题那么第二个问题呢就是一次可以查询多个数据这个什么意思呢其实我们刚刚也做了演示了就说当我们去做查询这个用户信息的时候那么你是否把他的基本信息是拿到了在拿到同时呢我们也去查询他我们还需要查询他的一些这个朋友这个信息的时候那么是不是同样也可以去查询到
[03:44] 那么如果说我们在这个位置所采用的是RESTful的话是不是需要发送两个请求第一个请求是查询这个用户信息第二个查询这个用户的一些朋友的信息对不对需要发送两个这个请求而我们现在使用GraphQL的时候那么是不是就会使用一个就可以了那么我所定义的要查询他还需要查询他的一个些朋友的信息那么这个朋友的信息下面又查询什么样的信息OK然后呢发送
[04:13] 这个是发送一条信息发送一条这个请求那么服务端就可以做这样的一个响应哎呀OK好那么这个呢在官方的这个首页呢他也有一个动态的一个演示啊就在这来看一下你看下面这个呢是这个是我们的客户端下面是服务端啊来看一下这个动态的一个演示啊就是说你看我一次去请求这么多然后呢给我响应这么多的数据
[04:41] 是不是我就可以实现什么呢实现获取多个资源的时候呢只用一个请求哎OK好有这样的一个动画的一个效果啊大家可以观察去看一下啊他也很好的能够表明他这个意图哎OK好那么接着继续往下面看那么他还有一种这个他这Guybq还提供了一种这样的一个功能啊就是API的眼镜的无需划分这个版本什么意思呢我们还是去观察一下他下面的一个
[05:11] 这样的一个动态吧动态的一个效果在这那么我们可以看到左边的这个啊左边的这个呢依然是他的一个请求对吧这个是我他的一个版本信息啊那么最开始是这样的一个版本对吧然后呢随着这个时间推移呢我们会增加了这样的一个
[05:31] 一个版本但是我们调用我们我们服务端的我们客户端调用的时候你不需要去做一个更新你还是可以去调用之前的一个这个这个接口因为因为这个返回这个数据是由你的客户端的一个参数是不来决定的你是不是只需要传递这三个
[05:51] 那我就给你返回这三个数据就可以了而第四个这个数据我不需要给你返回对吧因为你没有请求对吧当然第四个数据是我新版本的一个接口那么其实我们不要去关心了他大概的表达的是这样的一个意思你看有这个加号的这个代表的就是我们的一些这个新增的对吧然后这个是被一个废弃掉的废弃掉的这样的一个这样的一个属性OK那么这个就是API这个演进就是当我们这个
[06:19] 接口的服务做一些版本升级的时候那么我们的客户端其实没有必要跟着去做一个升级对吧因为是由你来做一个决定的哎OK好这个就是他所体现出他的一个这样的一些这个优点吧或者他的一个优势啊哎OK好嘞好
[06:37] 那么这个就是我们通过这三个点其实我们就进一步的去了解GraphQL它到底是能够去实现什么样的一个效果或者说它想表达的是什么样的一个意思那么OK好那么是不是在我们进一步了解之后那么我们是不是就能够理解它的确是在这种
[07:01] 设计思想这个层面是不是要比rest4就是更先进一些对吧ok好那么关于进一步了解graphqr这个小的一些内容我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 GraphQL 的核心概念，包括按需查询避免浪费、一次查询多个数据、类型系统、以及 API 演进和规范。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中“6.3.1、按需索取数据，避免浪费”章节，图示一个 GraphQL 查询 `{ hero { name } }` 对应返回数据 `{ "data": { "hero": { "name": "R2-D2" } } }`。
画面 2: 展示 GraphQL 官网首页，标题为“一种用于 API 的查询语言”。
画面 3: PDF 文档中“6.3.1、按需索取数据，避免浪费”章节，图示一个 GraphQL 查询 `{ hero { name } }` 对应返回数据 `{ "data": { "hero": { "name": "R2-D2" } } }`。
画面 4: GraphQL 官网“Schema 和类型”页面，标题为“Schema 和类型”，左侧有“类型系统（Type System）”小节，右侧有导航菜单，下方有 GraphQL 查询示例。
画面 5: GraphQL 官网“Schema 和类型”页面，展示 GraphQL 查询 `{ hero { name appearsIn } }` 及其返回数据 `{ "data": { "hero": { "name": "R2-D2", "appearsIn": ["NEWHOPE", "EMPIRE", "JEDI"] } } }`，并列出查询步骤。
画面 6: PDF 文档中“6.3.1、按需索取数据，避免浪费”章节，图示一个 GraphQL 查询 `{ hero { name appearsIn } }` 对应返回数据 `{ "data": { "hero": { "name": "R2-D2", "appearsIn": ["NEWHOPE", "EMPIRE", "JEDI"] } } }`，并附有说明文字和链接 `http://GraphQL.cn/learn/schema/#type-system`。
画面 7: PDF 文档中“6.3.2、一次查询多个数据”章节，图示一个 GraphQL 查询 `{ hero { name id appearsIn friends { id } } }` 及其返回数据 `{ "data": { "hero": { "name": "R2-D2", "id": "2001", "appearsIn": ["NEWHOPE", "EMPIRE", "JEDI"], "friends": [{ "id": "1000" }] } } }`。
画面 8: GraphQL 官网页面，标题为“获取多个资源 只用一个请求”，配图展示三个服务器和一个手机。
画面 9: PDF 文档中“6.3.2、一次查询多个数据”章节，图示一个 GraphQL 查询 `{ hero { name id appearsIn friends { id } } }` 及其返回数据 `{ "data": { "hero": { "name": "R2-D2", "id": "2001", "appearsIn": ["NEWHOPE", "EMPIRE", "JEDI"], "friends": [{ "id": "1000" }] } } }`。
画面 10: GraphQL 官网“Schema 和类型”页面，展示 GraphQL 类型定义，包括 `type Character { name: String, friends: [Character], homeWorld: Planet, species: Species }`、`type Planet { name: String, climate: String }`、`type Species { name: String, lifespan: Int, origin: Planet }`。
画面 11: GraphQL 官网页面，展示两个 GraphQL 类型定义，左侧为 `type Film { title: String, episode: Int, releaseDate: String, openingCrawl: String }`，右侧为 `type Film { title: String, episode: Int, releaseDate: String, openingCrawl: String, director: String }`，右侧有蓝色框“API 演进 无需划分版本”。
画面 12: PDF 文档中“6.3.2、一次查询多个数据”章节，图示一个 GraphQL 查询 `{ hero { name id appearsIn friends { id } } }` 及其返回数据 `{ "data": { "hero": { "name": "R2-D2", "id": "2001", "appearsIn": ["NEWHOPE", "EMPIRE", "JEDI"], "friends": [{ "id": "1000" }] } } }`。
画面 13: PDF 文档中“6.4、GraphQL查询的规范”章节，图示 GraphQL 类型定义，包括 `type Film { title: String, episode: Int, releaseDate: String, openingCrawl: String, director: String @deprecated }` 和 `type Person { name: String, directed: [Film], actedIn: [Film] }`，并有红色箭头标注“废弃属性”。
画面 14: PDF 文档中“6.3.1、按需索取数据，避免浪费”章节，图示一个 GraphQL 查询 `{ hero { name } }` 对应返回数据 `{ "data": { "hero": { "name": "R2-D2" } } }`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```GraphQL
{
  hero {
    name
  }
}
```
```json
{
  "data": {
    "hero": {
      "name": "R2-D2"
    }
  }
}
```
画面 3:
```GraphQL
{
  hero {
    name
  }
}
```
```json
{
  "data": {
    "hero": {
      "name": "R2-D2"
    }
  }
}
```
画面 5:
```GraphQL
{
  hero {
    name
    appearsIn
  }
}
```
```json
{
  "data": {
    "hero": {
      "name": "R2-D2",
      "appearsIn": [
        "NEWHOPE",
        "EMPIRE",
        "JEDI"
      ]
    }
  }
}
```
画面 6:
```GraphQL
{
  hero {
    name
    appearsIn
  }
}
```
```json
{
  "data": {
    "hero": {
      "name": "R2-D2",
      "appearsIn": [
        "NEWHOPE",
        "EMPIRE",
        "JEDI"
      ]
    }
  }
}
```
画面 7:
```GraphQL
{
  hero {
    name
    id
    appearsIn
    friends {
      id
    }
  }
}
```
```json
{
  "data": {
    "hero": {
      "name": "R2-D2",
      "id": "2001",
      "appearsIn": [
        "NEWHOPE",
        "EMPIRE",
        "JEDI"
      ],
      "friends": [
        {
          "id": "1000"
        }
      ]
    }
  }
}
```
画面 10:
```GraphQL
type Character {
  name: String
  friends: [Character]
  homeWorld: Planet
  species: Species
}

type Planet {
  name: String
  climate: String
}

type Species {
  name: String
  lifespan: Int
  origin: Planet
}
```
画面 11:
```GraphQL
type Film {
  title: String
  episode: Int
  releaseDate: String
  openingCrawl: String
}
```
```GraphQL
type Film {
  title: String
  episode: Int
  releaseDate: String
  openingCrawl: String
  director: String
}
```
画面 13:
```GraphQL
type Film {
  title: String
  episode: Int
  releaseDate: String
  openingCrawl: String
  director: String @deprecated
}

type Person {
  name: String
  directed: [Film]
  actedIn: [Film]
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“6.3.1、按需索取数据，避免浪费”，图示一个 GraphQL 查询 `{ hero { name } }` 指向返回数据 `{ "data": { "hero": { "name": "R2-D2" } } }`。
画面 4: PPT 标题为“Schema 和类型”，左侧有“类型系统（Type System）”小节，右侧有导航菜单。
画面 5: PPT 标题为“类型系统（Type System）”，图示 GraphQL 查询 `{ hero { name appearsIn } }` 及其返回数据 `{ "data": { "hero": { "name": "R2-D2", "appearsIn": ["NEWHOPE", "EMPIRE", "JEDI"] } } }`，并列出查询步骤。
画面 6: PPT 标题为“6.3.1、按需索取数据，避免浪费”，图示一个 GraphQL 查询 `{ hero { name appearsIn } }` 指向返回数据 `{ "data": { "hero": { "name": "

