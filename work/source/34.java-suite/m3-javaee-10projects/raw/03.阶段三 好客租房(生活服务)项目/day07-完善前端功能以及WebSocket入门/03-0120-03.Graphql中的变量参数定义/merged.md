# 03.Graphql中的变量参数定义

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\03.Graphql中的变量参数定义【海量资源尽在 ubkz.com】.mp4
- 时长 6分0秒（音频 360s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来讲一下GrabQL中的参数啊其实呢在前面呢我们也用过这个参数啊只是呢我们都是把这个参数呢写成什么静态的方式因为在我们下面去实现房源的列表查询的过程中啊我们会传递参数啊所以呢我们需要去来看一下GrabQL中的一个参数怎么去设置啊
[00:27] 那么我们来看一下在前面我们去使用的话往往是通过这种形式去做一个使用那么下面是我们查询的一些字段对不对然后上面这个位置就是我们查询的参数ID呢等于8OK那我们来看一下那么点击做一下测试点击这个位置然后走可以看到是不是可以正常查询到数据对不对但是呢其实我们可以想一下这个8呢我们是什么是不是写死了对不对相当于是一个静态的参数那么显然呢这种静态的参数
[00:57] 它是无法去满足我们多样的一些这种需求的所以我们必须要去寻找它是一种什么的变量的参数那么GrabQL中有没有这样的一些这个规定或者是规范呢其实是有的那么在GrabQL中那么它对于我们这种变量参数的一些这个规范是有些定义的我们来一起看一下那我们找到GrabQL的官网
[01:24] 那么我们找到哪个下面找到在这个下面有一个叫做变量变量我们来看一下这个变量呢他讲的意思就是说可以给他设置参数什么意思呢我们来看一下你看下面这个呢从这儿看这个是我们之前那个查学对吧然后呢我们在这个位置给他设置这样的一个参数然后呢在这个查学的这个位置就可以引用这个变量而不是写死到这个位置那我们来看一下
[01:53] 这个究竟他怎么去写他的语法结构是怎么样的呢我们一起来看一下他其实语法结构是这样的啊就是这个是我们原有的一个查询对不对然后呢在我们原有这个查询的外面我们再加一个关键的叫queryquery什么呢我们随便写个名字啊随便写个名字比如叫hk就浩克啊浩克那么这个hk呢是任意啊随意
[02:18] 它只是一个操作的一个名称而已那么这个无所谓啊我们给它随便起名字就可以了然后呢在这个里面呢做一个参数的一个定义比如说我们定义一个参数呢叫ID注意定义参数通过这个dollar去做一个定义然后呢ID这个类型什么类型呢是int类型OK那么通过这样的一个定义呢我们就把这个ID这个参数定义好了那么当我们定义好之后呢我们在下面这个位置8这个位置呢我们不用再写8了
[02:48] 我们就直接通过这个dollar这个ID那么就可以去引用到我们传入这个参数那么问题就是我们那个8如何去做一个传递呢我们来看一下把这个做一个格式化OK然后在下面这个位置下面这个位置在这个位置呢我们给他设置一个他的一个变量那么变量呢他设置的也是通过json的结构去做一个设置那么我们设置他的一个参数名是不是ID那么他的值呢就是8那么通过这种方式
[03:18] 去做一个参数的一个设置那么这样的话呢我们就可以做一个发起这样的一个请求OK那么我们尝试的去看一下当然了我如果现在我点击啊我点击这个查询那么肯定才查不到数据为什么呢因为我们的后端是不是并没有去处理这个参数或者是处理这个变量啊并没有处理但是呢我们可以看一下当我们去发起这个请求的时候他发起的请求是长什么样子的对吧可以看一下然后呢走
[03:47] 看一下那么他所发起的请求我们来看一下是不是找到他的请求这个他的请求那么请求的一个参数或者请求的一个数据是不是就是整体来讲它是一个json对象在json对象中它是不是有两个属性一个是query就是我们前面所看到这个query另外一个是不是就玩aboss这个是不是就是我们的设置的一个参数那么也就是说
[04:16] 我们的一个前端是不是就将我们所设的这个变量是不是也一起发送到了我们的服务端那么接下来其实我们要做的事情是不是就是需要在我们的服务端是不是去处理去传入的这个变量OK好那我们来看一下我们这个讲义那么在我们讲义中其实我们也看到在GrabQ中是不是
[04:40] 对于这个参数的一个变量这样的一个传递呢其实有些定义了对吧哎通过这样的方式做一个定义那么他怎么用呢来看一下那这个跟我们刚刚写的是一样的啊在我们原有的注意你看这个我画一下啊这个到这这个是我们原有的一个查询对不对在原有的查询外面的我们加一个query什么什么这个HK可以任意做一个命名然后呢在这个位置注意
[05:08] 在这个位置呢就要设置它的一些参数或者叫变量我们设置了一个变量呢是这个$id然后它的类型呢是个none类型然后呢我们在下面这个位置就可以去使用我们上面所定义的一个变量然后呢在我们去发起请求的这个下面呢我们给它设置什么呢设置这个参数设置参数在这个位置设置参数那么设置参数呢它就会跟随着我们的一个请求去提交到我们的服务端
[05:36] 那么提交到我们服务端那么前端客户端所做的事情是不是就做完了那么接下来是不是就需要服务端去解析提交的参数以及它的参数的值OK那么至于说服务端如何处理参数那么我们下一个视频我们再来做一个讲解那么OK关于WebQL中的参数的一个规范的定义我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 GraphQL 查询中如何使用变量（Variables）来动态传递参数，以避免硬编码和提高查询灵活性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中关于 GraphQL 参数传递的介绍，提及 id:8 是静态参数，并引出如何动态传递参数的问题。
画面 2: 在 Altair GraphQL 客户端中，成功执行了一个查询，返回了 HouseResources 对象的详细数据，包括 id、title、estateId、buildingUnit、buildingFloorNum、mobile、useArea、pic 等字段。
画面 3: PDF 文档中讲解片段（Fragment）的概念，用于复用查询字段，并展示了一个包含两个角色（Luke Skywalker 和 Leia Organa）的查询示例。
画面 4: PDF 文档中讲解使用变量的三步操作：用 $variableName 替代静态值、声明变量、将变量值通过 JSON 传输。并展示了一个使用变量的查询示例。
画面 5: 在 Altair GraphQL 客户端中，显示了一个查询语句，但未提供变量，请求 URL 为 http://127.0.0.1:18080/GraphQL。
画面 6: 在 Altair GraphQL 客户端中，请求正在加载，显示“Loading...”状态。
画面 7: 在 Altair GraphQL 客户端中，执行了一个查询，返回了错误信息：“Validation error of type VariableTypeMismatch. Variable type 'Int' doesn't match expected type 'Long'”。这表明变量类型不匹配。
画面 8: 在 Altair GraphQL 客户端中，查看请求的 Headers 和 Payload，显示请求方法为 POST，Content-Type 为 application/json，请求体包含 query 和 variables。
画面 9: 在 Altair GraphQL 客户端中，查看请求的 Payload，显示变量 { "id": 8 }。
画面 10: PDF 文档中提到，目前参数写在查询字符串内，但在很多应用中，参数可能是动态的，例如下拉菜单或搜索区。
画面 11: PDF 文档中再次强调使用变量的三步操作，并展示了一个使用变量的查询示例。
画面 12: PDF 文档中讲解设置参数值，展示了一个简单的 JSON 对象 { "id": 8 }。
画面 13: PDF 文档中展示了一个 GraphQL 查询语句，定义了参数 $id: Long，并查询 HouseResources(id: $id) 的所有字段。
画面 14: PDF 文档中展示了一个简单的 JSON 对象 { "id": 8 }，作为变量值。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```javascript
Promise.all([swipc, menu, info, fag, house]).then((result) => {
```
```GraphQL
{
  HouseResources(id: 8) {
    id
    title
    estateId
    buildingUnit
    buildingFloorNum
    mobile
    useArea
    pic
  }
}
```
画面 2:
```GraphQL
{
  "data": {
    "HouseResources": {
      "id": "8",
      "title": "2222",
      "estateId": "1002",
      "buildingUnit": "1",
      "buildingFloorNum": "1",
      "mobile": "1",
      "useArea": "4",
      "pic": "http://ikfast-haole.css.cn/qingdao.allyuncs.com/images/20181117/1715423896060254118.jpg,http://ikfast-haole.css.cn/qingdao.allyuncs.com/images/20181117/1715423896064306516.jpg"
    }
  }
}
```
画面 3:
```GraphQL
query HeroComparison($first: Int = 3) {
  leftComparison: hero(episode: EMPIRE) {
    ...comparisonFields
  }
  rightComparison: hero(episode: JEDI) {
    ...comparisonFields
  }
}

fragment comparisonFields on Character {
  name
  friendsConnection(first: $first) {
    edges {
      node {
        name
      }
    }
  }
}
```
画面 4:
```GraphQL
{
  "GraphQL": true,
  "variables": {
    "episode": "JEDI"
  }
}
query HeroNameAndFriends($episode: Episode) {
  hero(episode: $episode) {
    name
    friends {
      name
    }
  }
}
```
画面 5:
```GraphQL
query hk($id: Int) {
  HouseResources(id: $id) {
    id
    title
    estateId
    buildingUnit
    buildingFloorNum
    mobile
    useArea
    pic
  }
}
```
画面 7:
```json
{
  "errors": [
    {
      "message": "Validation error of type VariableTypeMismatch. Variable type 'Int' doesn't match expected type 'Long'",
      "locations": []
    }
  ]
}
```
画面 8:
```json
{
  "query": "query hk($id: Int) { HouseResources(id: $id) { id title estateId buildingUnit buildingFloorNum mobile useArea pic } }",
  "variables": {
    "id": 8
  }
}
```
画面 9:
```json
{
  "id": 8
}
```
画面 11:
```GraphQL
{
  "GraphQL": true,
  "variables": {
    "episode": "JEDI"
  }
}
query HeroNameAndFriends($episode: Episode) {
  hero(episode: $episode) {
    name
    friends {
      name
    }
  }
}
```
画面 12:
```json
{
  "id": 8
}
```
画面 13:
```GraphQL
query hk($id: Long) {
  HouseResources(id: $id) {
    id
    title
    estateId
    buildingUnit
    buildingFloorNum
    mobile
    useArea
    pic
  }
}
```
画面 14:
```json
{
  "id": 8
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PDF 文档标题为“2、GraphQL中的参数”，内容包括 GraphQL 查询中需要设置参数的示例。
画面 3: PDF 文档标题为“在片段内使用变量”，内容包括片段的概念和使用变量的示例。
画面 4: PDF 文档标题为“使用变量之前，我们将做三件事”，内容包括使用变量的三步操作和示例。
画面 10: PDF 文档标题为“目前为止，我们将参数写在了查询字符串内”，内容包括参数可能动态的情况。
画面 11: PDF 文档标题为“2.1、查询时传递参数”，内容包括使用变量的三步操作和示例。
画面 12: PDF 文档标题为“2.2、设置参数值”，内容包括设置参数值的示例。
画面 13: PDF 文档标题为“说明”，内容包括操作名称和参数类型的说明。
画面 14: PDF 文档标题为“variables”，内容包括变量值的示例。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

