# 画面线理解：15.MongoDB的JavaApi操作之插入数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\15.MongoDB的JavaApi操作之插入数据【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:28, 00:44, 00:55, 01:02, 01:08, 01:35, 01:55, 01:59, 02:11, 02:22, 02:28, 02:38, 02:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:43:03

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 中使用 MongoDB 客户端库进行数据查询和插入操作，包括条件查询、排序、字段投影和文档插入。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 testQuery 方法中使用 Filters.lt 和 Filters.gte 构建查询条件，查询 age<50 且 id>100 的用户。
画面 2: 代码光标移动到 Filters.and 方法，准备组合查询条件。
画面 3: 代码编辑器中光标位于 testQuery 方法内，显示了方法的完整结构。
画面 4: 代码光标移动到 testInsert 方法，准备编写插入数据的代码。
画面 5: 代码编辑器中光标位于 testInsert 方法内，显示了方法的完整结构。
画面 6: 代码编辑器中光标位于 testInsert 方法内，显示了方法的完整结构。
画面 7: 在 testInsert 方法中，使用 Document.append 方法为文档添加 "id"、"username" 和 "age" 字段。
画面 8: 代码编辑器中光标位于 testInsert 方法内，显示了方法的完整结构。
画面 9: 代码编辑器中光标位于 testInsert 方法内，显示了方法的完整结构。
画面 10: 代码编辑器中光标位于 testInsert 方法内，显示了方法的完整结构。
画面 11: 代码编辑器中光标位于 testInsert 方法内，显示了方法的完整结构。
画面 12: 代码编辑器中光标位于 testInsert 方法内，显示了方法的完整结构。
画面 13: 代码编辑器中光标位于 testInsert 方法内，显示了方法的完整结构。
画面 14: 代码编辑器中光标位于 testInsert 方法内，显示了方法的完整结构。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
// 查询age<50并且id>100的用户信息，并且按照id倒序排序，只返回id, age字段，不返回_id字段
@Test
void testQuery() {
    this.collection.find(
        Filters.lt(fieldNames: "age", value: 50),
        Filters.gte(fieldNames: "id", value: 100)
    ).sort(Sorts.descending(...fieldNames: "id"))
    .projection(Projections.fields(Projections.include(...fieldNames: "id", "age"),
        Projections.excludeId()))
    .forEach((Consumer<? super Document> document -> {
        System.out.println(document.toJson());
    }));
}
```

画面 4:
```java
@Test
public void testInsert() {
    this.collection.insertOne();
}
```

画面 7:
```java
@Test
public void testInsert() {
    Document document = new Document();
    document.append("id", 9999);
    document.append("username", "张三");
    document.append("age", 30);
    this.collection.insertOne(document);
}
```

画面 12:
```java
@Test
public void testInsert() {
    Document document = new Document();
    document.append("id", 9999);
    document.append("username", "张三");
    document.append("age", 30);
    this.collection.insertOne(document);
}
```

画面 14:
```java
@Test
public void testInsert() {
    Document document = new Document();
    document.append("id", 9999);
    document.append("username", "张三");
    document.append("age", 30);
    this.collection.insertOne(document);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
