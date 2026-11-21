# 15.MongoDB的JavaApi操作之插入数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\15.MongoDB的JavaApi操作之插入数据【海量资源尽在 ubkz.com】.mp4
- 时长 2分56秒（音频 176s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么下面我们来看一下数据的新增那我们在写之前呢我们先把前面写的这个查询的代码呢简单的优化一下就是在这个位置我们可以看到是通过一个类去静态的使用它静态方法就按的那这种写法呢看起来不是很优雅我们可以把它做一个静态的一个导入那么这样的话呢它呢就不只就可以直接去做这样那个引用了对吧直接写这样的方法就可以了OK这样写起来是不是更加的
[00:28] 简单一点或者简洁一点那么我们把这个sort也给它去做一个静态的一个引用那么这个projection也去做一个静态的一个引用ok这样的话代码就显得更简洁一些了好那么下面我们来看一下我们的这个插入数据叫test insert那么加一个test好那么下面我们是不是要用this.connection.什么的
[00:54] insert one,差五一条数据那么他需要什么一个document对象那么我们就给他new一个document对象new一个document对象然后我们去给他去设置一些制作通过这个document对象点append去添加你叫做id比方说9999然后加三个你还有一个叫做url name
[01:24] 然后这个值就叫,比方说叫张三然后来看一下还有一个叫做age比方说年龄的30好,那么现在我们是不是就构造好了这个document这个数据然后做一个insert插入这个数据是不是就插不进去了对吧然后下面我们可以测试一下去查询该数据把这个数据我们查询出来看大家这个对不对能不能查到那么通过类似点connection点什么fund
[01:54] 我们给他设置一个条件设置一个fill条件是不是就通过一个EQ相等是吧谁等于谁呢比如说我们通过ID等于999949的一个这样的一个查询他是不是拿到一个数据那我们给他设置一个叫for eachfor each循环那么这个里面通过Lambda表达式OK然后我们在这个位置给他去做一个数据的类型的一个强准然后我们在这把它打印出来document1.
[02:24] 点图接驶好嘞那我们来看一下这个数据能不能够查误成功他能不能打印出来呢如果下面能够打印出来那就说明上面肯定是已经查误成功了对不对好来看一下结果那么在这个结果中呢我们可以看到是不是已经查询到这条数据
[02:42] 对吧那就说明这个数据它肯定已经就写到我们的芒果DB中了要不然的话肯定你也查不到是不是OK好这个就是数据的一个插入OK那么关于数据的一个插入我们就先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

