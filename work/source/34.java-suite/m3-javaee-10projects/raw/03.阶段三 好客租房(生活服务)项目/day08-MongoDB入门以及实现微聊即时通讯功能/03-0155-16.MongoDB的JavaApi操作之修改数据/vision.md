# 画面线理解：16.MongoDB的JavaApi操作之修改数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\16.MongoDB的JavaApi操作之修改数据【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:05, 00:09, 00:17, 00:23, 00:35, 00:39, 00:44, 00:54, 00:56, 01:11, 01:18, 01:21, 01:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:43:35

1) 这一组画面整体在讲如何使用 Java 代码通过 MongoDB Java Driver 实现对数据库的插入和更新操作。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 testInsert() 方法，用于向 MongoDB 集合插入一个包含 id、username 和 age 字段的文档。代码中使用 insertOne() 方法插入数据，并通过 find() 查询并打印插入的文档。
画面2: 高亮显示 testInsert() 方法中查询数据的代码行，展示如何使用 find() 方法查询 id 为 9999 的文档。
画面3: 高亮显示 testInsert() 方法中 System.out.println(document1.toJson()); 语句，展示查询结果的输出。
画面4: 展示 testUpdate() 方法的代码，用于更新 id 为 9999 的文档，将 age 字段值从 30 修改为 35。
画面5: 在 testUpdate() 方法中，光标位于 updateOne() 方法的调用位置，准备输入参数。
画面6: 在 testUpdate() 方法中，光标位于 updateOne() 方法的调用位置，准备输入参数。
画面7: 在 testUpdate() 方法中，光标位于 updateOne() 方法的调用位置，准备输入参数。
画面8: 在 testUpdate() 方法中，光标位于 updateOne() 方法的调用位置，准备输入参数。
画面9: 在 testUpdate() 方法中，光标位于 updateOne() 方法的调用位置，准备输入参数。
画面10: 在 testUpdate() 方法中，光标位于 updateOne() 方法的调用位置，准备输入参数。
画面11: 在 testUpdate() 方法中，光标位于 updateOne() 方法的调用位置，准备输入参数。
画面12: 在 testUpdate() 方法中，光标位于 updateOne() 方法的调用位置，准备输入参数。
画面13: 在 testUpdate() 方法中，光标位于 updateOne() 方法的调用位置，准备输入参数。
画面14: 在 testUpdate() 方法中，光标位于 updateOne() 方法的调用位置，准备输入参数。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```java
public void testInsert() {
    Document document = new Document();
    document.append("id", 9999);
    document.append("username", "张三");
    document.append("age", 30);
    this.collection.insertOne(document);

    // 查询该数据
    this.collection.find(eq(fieldName: "id", value: 9999)).forEach((Consumer<? super Document>) document1 -> {
        System.out.println(document1.toJson());
    });
}
```

画面2:
```java
// 查询该数据
this.collection.find(eq(fieldName: "id", value: 9999)).forEach((Consumer<? super Document>) document1 -> {
    System.out.println(document1.toJson());
});
```

画面3:
```java
System.out.println(document1.toJson());
```

画面4:
```java
@Test
public void testUpdate() {
    Document document = new Document();
    document.append("id", 9999);
    document.append("username", "张三");
    document.append("age", 30);
    this.collection.insertOne(document);

    // 查询该数据
    this.collection.find(eq(fieldName: "id", value: 9999)).forEach((Consumer<? super Document>) document1 -> {
        System.out.println(document1.toJson());
    });
}
```

画面5:
```java
this.collection.updateOne(
    eq(fieldName: "id", value: 9999),
    Updates.set("age", 35)
);
```

画面6:
```java
this.collection.updateOne(
    eq(fieldName: "id", value: 9999),
    Updates.set("age", 35)
);
```

画面7:
```java
this.collection.updateOne(
    eq(fieldName: "id", value: 9999),
    Updates.set("age", 35)
);
```

画面8:
```java
this.collection.updateOne(
    eq(fieldName: "id", value: 9999),
    Updates.set("age", 35)
);
```

画面9:
```java
this.collection.updateOne(
    eq(fieldName: "id", value: 9999),
    Updates.set("age", 35)
);
```

画面10:
```java
this.collection.updateOne(
    eq(fieldName: "id", value: 9999),
    Updates.set("age", 35)
);
```

画面11:
```java
this.collection.updateOne(
    eq(fieldName: "id", value: 9999),
    Updates.set("age", 35)
);
```

画面12:
```java
this.collection.updateOne(
    eq(fieldName: "id", value: 9999),
    Updates.set("age", 35)
);
```

画面13:
```java
this.collection.updateOne(
    eq(fieldName: "id", value: 9999),
    Updates.set("age", 35)
);
```

画面14:
```java
this.collection.updateOne(
    eq(fieldName: "id", value: 9999),
    Updates.set("age", 35)
);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
