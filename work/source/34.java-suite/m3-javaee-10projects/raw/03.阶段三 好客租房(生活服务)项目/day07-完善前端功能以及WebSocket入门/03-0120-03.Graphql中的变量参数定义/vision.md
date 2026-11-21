# 画面线理解：03.Graphql中的变量参数定义

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\03.Graphql中的变量参数定义【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:47, 01:24, 01:54, 03:20, 03:47, 03:54, 04:17, 04:30, 04:38, 04:46, 05:27, 05:36, 05:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:19:31

1) 这一组画面整体在讲什么（一句话）：
讲解 GraphQL 查询中如何使用变量（Variables）来动态传递参数，以避免硬编码和提高查询灵活性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中关于 GraphQL 参数传递的介绍，提及 id:8 是静态参数，并引出如何动态传递参数的问题。
画面 2: 在 Altair GraphQL 客户端中，成功执行了一个查询，返回了 HouseResources 对象的详细数据，包括 id、title、estateId、buildingUnit、buildingFloorNum、mobile、useArea、pic 等字段。
画面 3: PDF 文档中讲解片段（Fragment）的概念，用于复用查询字段，并展示了一个包含两个角色（Luke Skywalker 和 Leia Organa）的查询示例。
画面 4: PDF 文档中讲解使用变量的三步操作：用 $variableName 替代静态值、声明变量、将变量值通过 JSON 传输。并展示了一个使用变量的查询示例。
画面 5: 在 Altair GraphQL 客户端中，显示了一个查询语句，但未提供变量，请求 URL 为 http://127.0.0.1:18080/graphql。
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
```graphql
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
```graphql
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
```graphql
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
```graphql
{
  "graphql": true,
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
```graphql
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
```graphql
{
  "graphql": true,
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
```graphql
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
