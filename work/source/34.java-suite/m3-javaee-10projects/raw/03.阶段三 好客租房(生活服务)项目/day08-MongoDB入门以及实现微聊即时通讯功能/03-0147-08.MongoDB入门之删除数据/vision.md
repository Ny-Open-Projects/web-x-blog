# 画面线理解：08.MongoDB入门之删除数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\08.MongoDB入门之删除数据【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:03, 01:26, 01:40, 01:46, 01:51, 02:21, 02:32, 02:58, 03:21, 03:33, 03:58, 04:08, 04:25, 04:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:37:49

1) 这一组画面整体在讲什么（一句话）：
演示 MongoDB 中删除操作的多种方法，包括根据条件删除、删除单条记录、删除所有记录，并对比不同删除方法的语法和效果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中关于 db.collection.remove() 方法的语法和参数说明，包含代码示例。
画面 2: 在 Xshell 中执行 db.user.update() 更新年龄为 25 的记录，然后执行 db.user.remove(age:25) 删除匹配的记录，显示删除结果。
画面 3: 继续在 Xshell 中执行 db.user.find() 查询所有记录，确认删除操作后的数据状态。
画面 4: 在 Xshell 中执行 db.user.remove(age:25) 删除年龄为 25 的记录，显示删除结果。
画面 5: 展示 PDF 文档中关于 db.user.remove() 方法的代码示例和注释，说明删除操作。
画面 6: 在 Xshell 中执行 db.user.remove(age:22, true) 删除年龄为 22 的记录，显示删除结果。
画面 7: 展示 PDF 文档中关于 db.user.remove() 方法的代码示例和注释，说明删除操作。
画面 8: 在 Xshell 中执行 db.user.remove(age:22, true) 删除年龄为 22 的记录，显示删除结果。
画面 9: 继续在 Xshell 中执行 db.user.remove() 删除所有记录，显示删除结果。
画面 10: 展示 PDF 文档中关于 db.user.remove() 方法的代码示例和注释，说明删除操作。
画面 11: 在 Xshell 中执行 db.user.deleteMany({}) 删除所有记录，显示删除结果。
画面 12: 展示 PDF 文档中关于 db.user.remove() 方法的代码示例和注释，说明删除操作。
画面 13: 在 Xshell 中执行 db.user.deleteMany({}) 删除所有记录，显示删除结果。
画面 14: 展示 PDF 文档中关于 db.collection.remove() 方法的语法和参数说明，包含代码示例。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
db.collection.remove(
  query,
  {
    justOne: <boolean>,
    writeConcern: <document>
  }
)

参数说明：
• query: (可选) 删除的文档的条件。
• justOne: (可选) 如果设置为 true 或 1, 则只删除一个文档, 如果不设置该参数, 或使用默认值 false, 则删除所有匹配条件的文档。
• writeConcern: (可选) 指定抛出的级别。

实例：
> db.user.remove(age:25)
WriteResult({ "nRemoved" : 2 }) #删除了2条数据

加入几条测试数据
db.user.insert({id:1,username: "zhangsan",age:20});
db.user.insert({id:2,username: "lisi",age:21});
db.user.insert({id:3,username: "wangwu",age:22});
db.user.insert({id:4,username: "zhaoliu",age:22});

画面 5:
> db.user.remove(Age:22),true)
WriteResult({ "nRemoved" : 1 })
#删除了1条数据

删除所有数据
> db.user.remove()

#说明：为了简化操作，官方推荐使用deleteOne()与deleteMany()进行删除数据操作。
> db.user.deleteOne({id:1}) #删除了1条数据
> db.user.deleteMany({}) #删除了所有数据

画面 14:
db.collection.remove(
  query,
  {
    justOne: <boolean>,
    writeConcern: <document>
  }
)

参数说明：
• query: (可选) 删除的文档的条件。
• justOne: (可选) 如果设置为 true 或 1, 则只删除一个文档, 如果不设置该参数, 或使用默认值 false, 则删除所有匹配条件的文档。
• writeConcern: (可选) 指定抛出的级别。

实例：
> db.user.remove(age:25)
WriteResult({ "nRemoved" : 2 }) #删除了2条数据

加入几条测试数据
db.user.insert({id:1,username: "zhangsan",age:20});
db.user.insert({id:2,username: "lisi",age:21});
db.user.insert({id:3,username: "wangwu",age:22});
db.user.insert({id:4,username: "zhaoliu",age:22});

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 5:
标题: 1.3.6. 查询数据
内容:
> db.user.remove(Age:22),true)
WriteResult({ "nRemoved" : 1 })
#删除了1条数据

删除所有数据
> db.user.remove()

#说明：为了简化操作，官方推荐使用deleteOne()与deleteMany()进行删除数据操作。
> db.user.deleteOne({id:1}) #删除了1条数据
> db.user.deleteMany({}) #删除了所有数据

画面 14:
标题: 1.3.6. 查询数据
内容:
> db.user.remove(Age:22),true)
WriteResult({ "nRemoved" : 1 })
#删除了1条数据

删除所有数据
> db.user.remove()

#说明：为了简化操作，官方推荐使用deleteOne()与deleteMany()进行删除数据操作。
> db.user.deleteOne({id:1}) #删除了1条数据
> db.user.deleteMany({}) #删除了所有数据

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
