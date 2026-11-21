# 16.MongoDB的JavaApi操作之修改数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\16.MongoDB的JavaApi操作之修改数据【海量资源尽在 ubkz.com】.mp4
- 时长 1分31秒（音频 92s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么我们接着继续下面我们来测试修改数据那么咱们把这个方法去call一下然后我们去改造一下这个修改就出来了好,那么我们这个改成test什么的不是insert是改成update然后我们来看一下这个位置怎么玩呢我们就要用它的方法就是点什么呢点updateupdate1是吧,可以看到是不是有两个条件或者说两个参数
[00:28] 那么在这个位置是第一个是failed就是你的查询条件第二个就是你更新的数据ok那么我们的条件怎么写这个我们就不需要了我们就来更新我们上面所写的一张数据那么我们通过一个条件是不是就EQ对吧EQ谁是不是就是我们这个ID它的值等于99999这样的一个数据然后去修改它的怎么数据它通过一个updates.setset什么我们修改它的年龄
[00:58] 把它改成35岁35OK这样的话是不是就已经把它修改完成了就是一个根据一个条件去做一个查找然后呢去修改它的一个数据就可以了好那么我们下面的依然把它打印出来来看一下执行看一下它是否已经把这个年龄修改成35岁这样的一个年龄等待它的一个执行好执行成功了那么可以看到这个年龄是不是已经被修改成这个35了哎呦OK
[01:27] 好那么这个数据的一个修改的我们就讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

