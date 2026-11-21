# 画面线理解：17.GraphQL入门之Schema和类型规范

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\17.GraphQL入门之Schema和类型规范【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:38, 00:43, 00:45, 01:59, 02:00, 02:04, 03:34, 04:21, 04:22, 04:50, 04:52, 05:31, 05:59, 06:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:59:52

1) 这一组画面整体在讲什么（一句话）：
讲解 GraphQL Schema 的定义结构、标量类型、枚举类型和接口类型。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中 GraphQL Schema 定义结构的代码示例，包含 schema、query 和 type User 的定义。
画面 2: 展示 GraphQL 官方文档页面，介绍 Schema 和类型系统。
画面 3: 展示 GraphQL 官方文档中关于类型系统的示例，包含一个查询 { hero { name appearsIn } }。
画面 4: 展示 PDF 文档中 GraphQL 标量类型（Scalar Types）的说明，列出 Int、Float、String、Boolean 和 ID 五种类型。
画面 5: 展示 PDF 文档中 GraphQL Schema 定义结构的代码示例。
画面 6: 展示 PDF 文档中 GraphQL 标量类型（Scalar Types）的说明。
画面 7: 展示 PDF 文档中 GraphQL 标量类型（Scalar Types）的说明，光标在 ID 类型的描述上。
画面 8: 展示 PDF 文档中 GraphQL 枚举类型（enum Episode）和接口类型（Type Human）的定义。
画面 9: 展示 PDF 文档中 GraphQL 接口类型（interface Character）的定义。
画面 10: 展示 PDF 文档中 GraphQL 接口类型（interface Character）和实现接口的类型（type Human implements Character）的定义。
画面 11: 展示 PDF 文档中 GraphQL 接口类型（interface Character）和实现接口的类型（type Human implements Character）的定义。
画面 12: 展示 PDF 文档中 GraphQL 接口类型（interface Character）和实现接口的类型（type Droid implements Character）的定义。
画面 13: 展示 PDF 文档中 GraphQL Schema 定义结构的代码示例。
画面 14: 展示 PDF 文档中 GraphQL Schema 定义结构的代码示例。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```graphql
schema { #定义查询
  query: UserQuery
}
type UserQuery { #定义查询的类型
  user(id:ID) : User #指定对象以及参数类型
}
type User { #定义对象
  id:ID! # !表示该属性是非空项
  name:String
  age:Int
}
```

画面 4:
```text
GraphQL规范中，默认定义了5种类型：
• Int : 有符号 32 位整数。
• Float : 有符号双精度浮点值。
• String : UTF-8 字符序列。
• Boolean : true 或者 false。
• ID : ID 标量类型表示一个唯一标识符，通常用以重新获取对象或者作为缓存中的键。
```

画面 8:
```graphql
enum Episode { #定义枚举
  NEWHOPE
  EMPIRE
  JEDI
}
Type Human {
  id: ID!
  name: String!
  appearsIn: [Episode]! #使用枚举类型
  homePlanet: String
}
```

画面 10:
```graphql
interface Character { #定义接口
  id: ID!
  name: String!
  friends: [Character]
  appearsIn: [Episode]!
}
#实现接口
type Human implements Character {
  id: ID!
  name: String!
  friends: [Character]
  appearsIn: [Episode]!
  starships: [Starship]
  totalCredits: Int
}
```

画面 12:
```graphql
type Droid implements Character {
  id: ID!
  name: String!
  friends: [Character]
  appearsIn: [Episode]!
  primaryFunction: String
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
