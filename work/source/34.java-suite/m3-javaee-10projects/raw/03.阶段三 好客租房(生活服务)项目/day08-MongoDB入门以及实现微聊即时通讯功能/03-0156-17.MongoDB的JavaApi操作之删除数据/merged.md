# 17.MongoDB的JavaApi操作之删除数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\17.MongoDB的JavaApi操作之删除数据【海量资源尽在 ubkz.com】.mp4
- 时长 2分35秒（音频 155s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来我们就来看删除的操作那么public返回值word然后来一个test delete一t然后去做一个测试test好那么下面我们通过this.connection.deletedeleteone或者delete many都可以那么我们就deleteone给它删除一条数据那么删除一条数据比如说我们就把999这个数据给它删除掉ok
[00:30] 或者我们这样咱们不要忘了咱们直接来一个delete money这样的话删除的可能会多一点是吧肯定会多一点那么我们设置什么EQEQ什么就是年龄等于25岁的这样的一个数据全部给我删除掉那我怎么知道它删除掉几条数据呢所以我们就需要看它的一个返回值那么它的一个返回值叫delete result那么我们把这个delete result给它打印出来叫delete result
[00:59] 好来看一下那么他删除几条的走那么等待他这个执行我们来看一下他执行的一个结果好那么我们可以看到在这个位置他是不是也删除掉是不是delete count是1是不是删除掉一行那个数据ok那么我们可以再次执行来看一下效果那这条数据我相信肯定是不存在了对不对那么现在你可以看到delete的结果是不是就是0ok
[01:28] 那么在上面做update的时候其实它也有一个返回值我们也可以看一下叫做update result那么我们也可以把它这个结果得打印出来叫做update result我们再来测试一下这个就可以看到有没有修改几条数据或者说有没有修改那么删除几条数据通过这个result就可以看到它的一个结果那么我们可以看到它的一个结果就是上面这个位置就是你可以看到它匹配到一条
[01:57] 但是并没有做修改为什么因为数据是不是还是一样的对吧那么比如说我们改成40改成40那么原来35我们改成40来看一下那么等待它的一个执行那么看它有没有就做删除来看一下你看在这个位置它
[02:18] 已经匹配到一条是不是然后删除几条的会修改几条的修改了是不是一条OK那么最后一个结果是不是这个数据已经改成40了OK好嘞那么这个就是我们所讲的一个删除删除好那么关于这个删除我们就先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
- 日志内容：`Monitor Thread successfully connected to server with description ServerDescription{address:172.16.55.195:27017, type=STANDALONE}` 和 `AcknowledgedUpdateResult{matchedCount=1, modifiedCount=0, upsertedId=null}`。

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

