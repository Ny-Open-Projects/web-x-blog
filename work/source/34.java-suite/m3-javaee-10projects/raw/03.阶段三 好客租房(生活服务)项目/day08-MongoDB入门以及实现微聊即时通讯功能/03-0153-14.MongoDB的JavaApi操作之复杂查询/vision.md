# 画面线理解：14.MongoDB的JavaApi操作之复杂查询

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\14.MongoDB的JavaApi操作之复杂查询【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:33, 01:10, 01:37, 02:40, 03:26, 04:02, 04:30, 04:59, 05:19, 06:23, 07:08, 08:09, 08:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:42:37

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Java 语言通过 MongoDB Java 驱动程序执行查询操作，包括构建查询条件、排序和投影。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档中关于 MongoDB CURD 操作的代码片段，包含查询和关闭连接的代码。
画面2：在 IntelliJ IDEA 中展示 TestMongoDB.java 文件，演示如何建立 MongoDB 连接并获取数据库和集合。
画面3：在 IntelliJ IDEA 中展示 TestMongoDB.java 文件，演示如何初始化 MongoDB 连接和选择集合。
画面4：展示 PDF 文档中关于 CURD 操作的代码片段，包含 TestCRUD 类的导入语句。
画面5：在 IntelliJ IDEA 中展示 TestMongoDB.java 文件，演示如何构建查询条件并使用 forEach 遍历结果。
画面6：在 IntelliJ IDEA 中展示 TestMongoDB.java 文件，演示如何使用 Filters 类构建查询条件。
画面7：在 IntelliJ IDEA 中展示 TestMongoDB.java 文件，演示如何使用 Filters.and() 方法组合查询条件。
画面8：在 IntelliJ IDEA 中展示 TestMongoDB.java 文件，运行 testQuery 方法后，终端显示 MongoDB 连接成功并输出查询结果。
画面9：在 IntelliJ IDEA 中展示 TestMongoDB.java 文件，终端显示 testQuery 方法的测试结果，输出了符合条件的文档。
画面10：在 IntelliJ IDEA 中展示 TestMongoDB.java 文件，演示如何在查询中添加排序。
画面11：在 IntelliJ IDEA 中展示 TestMongoDB.java 文件，终端显示 testQuery 方法的测试结果，输出了按 id 降序排列的文档。
画面12：在 IntelliJ IDEA 中展示 TestMongoDB.java 文件，终端显示 testQuery 方法的测试结果，输出了按 id 降序排列的文档。
画面13：在 IntelliJ IDEA 中展示 TestMongoDB.java 文件，演示如何使用 Projections 类进行字段投影。
画面14：展示 PDF 文档中关于插入操作的代码片段，包含 testInsert 方法，用于向集合中插入文档。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
// 查询数据
userCollection.find().limit(10).forEach(new Consumer<Document>() {
@Override
public void accept(Document document) {
System.out.println(document.toJson());
}
});
// 关闭连接
mongoClient.close();
```

画面2：
```java
public static void main(String[] args) {
// 建立连接
MongoClient mongoClient = MongoClients.create("mongodb://172.16.55.1");
// 选择数据库
MongoDatabase database = mongoClient.getDatabase(databaseName: "testdb");
// 选择表
MongoCollection<Document> userCollection = database.getCollection(collectionName: "user");
// 操作
usercollection.find().limit(10).forEach(new Consumer<?> super Document> {
System.out.println(document.toJson());
});
// 关闭连接，释放资源
mongoClient.close();
}
```

画面3：
```java
import com.mongodb.client.MongoDatabase;
import org.bson.Document;
import org.junit.Before;

public class TestMongoDB {
@Before
public void init() {
// 建立连接
MongoClient mongoClient = MongoClients.create("mongodb://172.16.55.185:27017");
// 选择数据库
MongoDatabase database = mongoClient.getDatabase(databaseName: "testdb");
// 选择表
MongoCollection<Document> userCollection = database.getCollection(collectionName: "user");
}
```

画面4：
```java
package cn.itcast.mongodb;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.model.Projections;
import com.mongodb.client.model.Sorts;
import com.mongodb.client.result.DeleteResult;
import com.mongodb.client.result.UpdateResult;
import org.bson.Document;
import org.junit.Before;
import org.junit.Test;
import static com.mongodb.client.model.Filters.*;
import java.util.function.Consumer;
```

画面5：
```java
// 查询age<50并且id>100的用户信息，并且按照id倒序排序，只返回id. age字段，不返回_id字段
@Test
public void testQuery() {
this.collection.find().forEach(document -> {
```

画面6：
```java
// 查询age<50并且id>100的用户信息，并且按照id倒序排序，只返回id. age字段，不返回_id字段
@Test
public void testQuery() {
this.collection.find().and(
```

画面7：
```java
// 查询age<50并且id>100的用户信息，并且按照id倒序排序，只返回id. age字段，不返回_id字段
@Test
public void testQuery() {
this.collection.find(
Filters.and(
Filters.lte(fieldName: "age", value: 50),
Filters.gte(fieldName: "id", value: 100)
)
).forEach((Consumer<?> super Document> document -> {
System.out.println(document.toJson());
});
}
```

画面8：
```java
// 查询age<50并且id>100的用户信息，并且按照id倒序排序，只返回id. age字段，不返回_id字段
@Test
public void testQuery() {
this.collection.find(
Filters.and(
Filters.lte(fieldName: "age", value: 50),
Filters.gte(fieldName: "id", value: 100)
)
).forEach((Consumer<?> super Document> document -> {
System.out.println(document.toJson());
});
}
```

画面9：
```java
// 查询age<50并且id>100的用户信息，并且按照id倒序排序，只返回id. age字段，不返回_id字段
@Test
public void testQuery() {
this.collection.find(
Filters.and(
Filters.lte(fieldName: "age", value: 50),
Filters.gte(fieldName: "id", value: 100)
)
).forEach((Consumer<?> super Document> document -> {
System.out.println(document.toJson());
});
}
```

画面10：
```java
// 查询age<50并且id>100的用户信息，并且按照id倒序排序，只返回id. age字段，不返回_id字段
@Test
public void testQuery() {
this.collection.find(
Filters.and(
Filters.lte(fieldName: "age", value: 50),
Filters.gte(fieldName: "id", value: 100)
)
).sort(Sorts.descending(fieldNames: "id"))
.forEach((Consumer<?> super Document> document -> {
System.out.println(document.toJson());
});
}
```

画面11：
```java
// 查询age<50并且id>100的用户信息，并且按照id倒序排序，只返回id. age字段，不返回_id字段
@Test
public void testQuery() {
this.collection.find(
Filters.and(
Filters.lte(fieldName: "age", value: 50),
Filters.gte(fieldName: "id", value: 100)
)
).sort(Sorts.descending(fieldNames: "id"))
.forEach((Consumer<?> super Document> document -> {
System.out.println(document.toJson());
});
}
```

画面12：
```java
// 查询age<50并且id>100的用户信息，并且按照id倒序排序，只返回id. age字段，不返回_id字段
@Test
public void testQuery() {
this.collection.find(
Filters.and(
Filters.lte(fieldName: "age", value: 50),
Filters.gte(fieldName: "id", value: 100)
)
).sort(Sorts.descending(fieldNames: "id"))
.forEach((Consumer<?> super Document> document -> {
System.out.println(document.toJson());
});
}
```

画面13：
```java
// 查询age<50并且id>100的用户信息，并且按照id倒序排序，只返回id. age字段，不返回_id字段
@Test
public void testQuery() {
this.collection.find(
Filters.and(
Filters.lte(fieldName: "age", value: 50),
Filters.gte(fieldName: "id", value: 100)
)
).sort(Sorts.descending(fieldNames: "id"))
.projection(
Projections.fields(
Projections.include("id", "age"),
Projections.excludeId()
)
)
.forEach((Consumer<?> super Document> document -> {
System.out.println(document.toJson());
});
}
```

画面14：
```java
this.mongoCollection.find()
.and(
lte("age", 50),
gte("id", 100)
)
.sort(Sorts.descending("id"))
.projection(
Projections.fields(
Projections.include("id", "age"),
Projections.excludeId()
)
)
.forEach((Consumer<?> super Document> document -> {
System.out.println(document.toJson());
});
@Test
void testInsert() {
Document document = new Document("id", 10001)
.append("name", "张三")
.append("age", 30);
this.mongoCollection.insertOne(document);
System.out.println("插入数据成功！");
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
