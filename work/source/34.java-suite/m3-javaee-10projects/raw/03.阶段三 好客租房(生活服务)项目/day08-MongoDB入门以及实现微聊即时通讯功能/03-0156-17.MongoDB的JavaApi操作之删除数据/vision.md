# 画面线理解：17.MongoDB的JavaApi操作之删除数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\17.MongoDB的JavaApi操作之删除数据【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:05, 00:17, 00:36, 00:57, 01:02, 01:09, 01:28, 01:37, 01:48, 01:55, 02:07, 02:16, 02:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:44:13

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 中使用 MongoDB 客户端库执行更新、删除和查询操作，并展示对应的控制台日志输出。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 编辑器中显示 TestMongoDB.java 文件的 testUpdate() 方法。
- 代码内容：`this.collection.updateOne(eq(fieldName: "id", value: 9999), Updates.set("age", 35));` 用于更新文档。
- 代码内容：`this.collection.find(eq(fieldName: "id", value: 9999)).forEach((Consumer<? super Document>) document -> System.out.println(document1.toJson());` 用于查询并打印文档。
- 控制台显示测试通过。

画面 2:
- 编辑器中光标位于 testUpdate() 方法后，准备编写新方法。
- 代码内容：`public void` 开始定义新方法。

画面 3:
- 编辑器中显示代码补全建议，包含 `updateOne`、`find` 等方法签名。
- 光标位于 `this.collection.` 后，准备调用方法。

画面 4:
- 编辑器中显示正在编写 testDelete() 方法。
- 代码内容：`public void testDelete(){ this.collection.deleteMany(`。

画面 5:
- 编辑器中显示代码补全建议，包含 `Sorts`、`Bson` 等类。
- 光标位于 `this.collection.` 后，准备调用方法。

画面 6:
- 编辑器中显示 testDelete() 方法的完整代码。
- 代码内容：`DeleteResult deleteResult = this.collection.deleteMany(eq(fieldName: "age", value: 25)); System.out.println(deleteResult);`。

画面 7:
- 控制台显示 testDelete() 方法执行后的日志。
- 日志内容：`Opened connection [connectionId:localValue:2, serverValue:41] to 172.16.55.1` 和 `AcknowledgedDeleteResult{deletedCount=1}`。

画面 8:
- 控制台显示 testDelete() 方法执行后的日志。
- 日志内容：`Opened connection [connectionId:localValue:2, serverValue:43] to 172.16.55.1` 和 `AcknowledgedDeleteResult{deletedCount=1}`。

画面 9:
- 编辑器中显示代码补全建议，包含 `size`、`slice` 等方法。
- 光标位于 `this.collection.updateOne(...)` 后，准备调用方法。

画面 10:
- 编辑器中显示 testUpdate() 方法的完整代码。
- 代码内容：`UpdateResult updateResult = this.collection.updateOne(eq(fieldName: "id", value: 9999), Updates.set("age", 35)); System.out.println(updateResult);`。
- 控制台显示执行结果：`AcknowledgedUpdateResult{matchedCount=1, modifiedCount=0, upsertedId=null}` 和文档内容。

画面 11:
- 控制台显示 testUpdate() 方法执行后的日志。
- 日志内容：`Monitor thread successfully connected to server with description ServerDescription{address:172.16.55.195:27017, type=STANDALONE}` 和 `AcknowledgedUpdateResult{matchedCount=1, modifiedCount=0, upsertedId=null}`。

画面 12:
- 编辑器中显示代码补全菜单，包含“Copy”, “Paste”, “Find Usages”等选项。
- 光标位于 `this.collection.find(...).forEach(...)` 后，准备修改代码。

画面 13:
- 编辑器中显示 testUpdate() 方法的完整代码。
- 代码内容：`UpdateResult updateResult = this.collection.updateOne(eq(fieldName: "id", value: 9999), Updates.set("age", 40)); System.out.println(updateResult);`。
- 控制台显示执行结果：`AcknowledgedUpdateResult{matchedCount=1, modifiedCount=1, upsertedId=null}` 和文档内容。

画面 14:
- 编辑器中显示 testDelete() 方法的完整代码。
- 代码内容：`DeleteResult deleteResult = this.collection.deleteMany(eq(fieldName: "age", value: 25)); System.out.println(deleteResult);`。
- 控制台显示执行结果：`AcknowledgedDeleteResult{deletedCount=1}`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@Test
public void testUpdate() {
    this.collection.updateOne(eq(fieldName: "id", value: 9999), Updates.set("age", 35));
    this.collection.find(eq(fieldName: "id", value: 9999)).forEach((Consumer<? super Document>) document -> System.out.println(document1.toJson()));
}
```

画面 6:
```java
@Test
public void testDelete() {
    DeleteResult deleteResult = this.collection.deleteMany(eq(fieldName: "age", value: 25));
    System.out.println(deleteResult);
}
```

画面 10:
```java
@Test
public void testUpdate() {
    UpdateResult updateResult = this.collection.updateOne(eq(fieldName: "id", value: 9999), Updates.set("age", 35));
    System.out.println(updateResult);
    this.collection.find(eq(fieldName: "id", value: 9999)).forEach((Consumer<? super Document>) document -> System.out.println(document1.toJson()));
}
```

画面 13:
```java
@Test
public void testUpdate() {
    UpdateResult updateResult = this.collection.updateOne(eq(fieldName: "id", value: 9999), Updates.set("age", 40));
    System.out.println(updateResult);
    this.collection.find(eq(fieldName: "id", value: 9999)).forEach((Consumer<? super Document>) document -> System.out.println(document1.toJson()));
}
```

画面 14:
```java
@Test
public void testDelete() {
    DeleteResult deleteResult = this.collection.deleteMany(eq(fieldName: "age", value: 25));
    System.out.println(deleteResult);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
