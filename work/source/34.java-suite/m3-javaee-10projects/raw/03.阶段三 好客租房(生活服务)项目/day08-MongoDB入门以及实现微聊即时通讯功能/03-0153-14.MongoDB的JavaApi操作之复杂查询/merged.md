# 14.MongoDB的JavaApi操作之复杂查询

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\14.MongoDB的JavaApi操作之复杂查询【海量资源尽在 ubkz.com】.mp4
- 时长 9分5秒（音频 546s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么接下来我们来看一下它的Ciud的操作前面我们只是对它做了一些这个简单的一个操作就是做了一些连接然后去做了一个简单的一个查询OK好那么下面我们来看一下写一个测试用力我们去对它做一些Ciud的操作那么我们就在下面的这个test这个包里面去写一个单元测试测试用力那么cn.itcast然后再来一个什么叫mongomongo db
[00:29] 然后呢我们在这个下面给他去创建一个测试类对吧就要test叫mongodbmongodb啊然后呢我们在下面是不是就可以写他一系列一些方法那么我们可以先写一个什么呢呃就是叫init对吧init的方法去做一些初始化的操作这个我们写一个叫做比复啊比复这么在执行之前先来执行他那么这个里面的代码我们是不是就可以把刚刚我们所写这几个代码呢
[00:59] 把它贴过来对吧先去建立这个连接下面呢是不是做一些这个操作OK那么把这个我们定义到外面去然后呢定义一个Connection好那么下面呢是不是就是直接做一个复制就好了好嘞那么接下来我们下面是不是就针对于这个Connection做一系列的这个操作就可以了那么下面呢我们先来写一个操作就是我们的这个查询然后呢叫test query
[01:29] 然后呢给他加一个注解是不是就叫test好那么这个里面要写什么内容呢就是我们要实现什么样的需求呢我们来看一下讲义啊那么咱们实现一个相对比较复杂一点的这个查询能把这个先拿过来来看一下他的一个需求是什么就是我们要去查询一个年龄小于等于50并且ID呢大于等于100的一个用户的信息那么我们并且呢需要按照ID呢做一个倒序的排序
[01:59] 并且只返回ID和A者这个字段不返回这个下滑线ID这个字段那么所以你可以看到这个查询还是比较复杂的一个查询对不对好那么我们就来看一下它到底怎么样去实现怎么实现呢我们是不是可以调用this.connects.去做一个fund的一个查询对不对那么fund的查询查询的条件是什么这样我们先给它来一个for each我们先做便利先做便利
[02:28] 去一个一个添加上面的这个条件好那么这个里面缺一个他把它去然后呢把这个给他做一个类型的一个强短转成一个consumer然后呢在这个里面呢我们把这个document然后document.to json把它打印出来那么这个里面我们其实要解决的问题就是这个query就是这个查询对吧犯了什么查询呢
[02:58] 那么在芒果DB中呢它通过一个类叫做FiltreFiltreFiltre是这个包下面的一些这个方法来构造一个过滤的一个条件那么我们现在要做的呢是来看一下啊它是一个两个条件对吧前面是年龄小于等于50后面的是ID大于等于100所以这两个条件是一个and的关系所以我们先要来一个什么呢是and
[03:28] 然后呢在这个里面呢我们再来添加他的一些其他的一些这个条件那么我们来看一下A值是小于等于50那就是LTE对不对那LTE然后呢他的名字字段的名字叫A值然后呢值呢就是50然后呢我们再来给他添加一个就是Field点什么呢GTE是不是就大于等于100那么就是
[03:56] ID然后呢逗号然后大于等于100这个是不是就他的一个查询的一个条件呀对不对查询的一个条件OK好那么我们可以先来执行一下吧看他能不能够返回我们所需要的这个数据就是年龄要小于等于50但是ID呢要大于等于100这样的一个用户的一个数据我们来看一下他能不能够去查到我们想要的数据呢
[04:22] 可以看到是不是已经查到小鱼的数据了来看一下对不对我们的ID是不是要大于等于100那么可以看到是不是都是100以上的这样的一个ID的数据那么年龄要小于等于50那么小于等于50我来看一下那么是不是最大是不是就到50所以这个数据返回的是OK的也就是说我们第一个这个是不是就搞定了第一个我们这个就搞定了
[04:49] 第二个呢是要按照ID去做一个倒序的一个排序那我们可以看到现在这个数据呢它呢是一个正序的一个排序对不对你看从101开始一直到140那么我们来给它做一个排序怎么样做排序呢我们在这个Fed后面啊再加一个什么呢Sort做一个排序那么这个排序呢通过一个SortSort4啊然后点我们通过一个这个什么呢叫DESC
[05:18] DSA是不是做一个倒序的排序什么做一个倒序的排序呢是不是ID通过这个支撑去做一个倒序的一个排序那么我们再去做一个测试来看一下效果等待它的一个执行我们来看一下好来看一下这个结果那么这个结果呢显然我们可以看到这个数据它所返回的是不是就是从140一直倒序到101
[05:49] 那么跟我们刚刚看到顺序是不是就刚好相反了OK这个是不是就给他增加了一个什么呢排序对不对啊增加了一个排序那我们来看一下那么他还有还有一个要求就是只返回ID和我们的AGE之段不返回呢下完线ID这个之段那么由于我们现在的数据呢可以看到他返回的呢有ID和Unename还有AGE这样的一个这个之段那么我们现在要求呢只返回的是他和后面的这个
[06:19] 这个呢中间这个我们是不需要的哎OK那我们来看一下这个怎么做呢我们依然呢需要在后面的继续给他点去设置一个什么呢projection那么就是去设置他的一个投影就是返回的一个字段那么这个里面怎么玩呢我们要通过这个projection是点field去设置他的一些这个返回的一些这个字段那么我们通过这个projections然后呢来一个include
[06:47] 就是我需要包含什么字段呢包含我的这个ID以及什么呢我的一个ID逗号再加一个什么呢AgeOK那我们来看一下走运行那么看一下是否能够直接返回ID和Age这两个字段呢其他的不做返回来看一下
[07:07] 那么我们可以看到返回的数据中是不是有这个ID和AIDS那么显然前面的优势内容是不是已经不做返回了对不对但是它现在还有一个下滑线的这个ID也就是它的一个唯一的一个维建对吧或者它的组件那么我们现在需求是不返回这个阶段当然了这个需求它不一定是真实的但是我们就为了给大家做这样的演示就是我们不返回这个
[07:36] 那不返回这个怎么办呢我们就需要在我们的这个就是fill的中再给他做一个设置咱们把这个回测一下这样看起来会好看一点方便一点那么我们需要再给他去设置一个什么呢设置一个叫排除排除一个什么字段呢不是这个应该叫什么呢我们去排除他的ID他有一个专门的方法就是排除他的一个ID
[08:04] 这个制度把这个制度给它排除掉加一个逗号就是说我们不需要它返回我们内置的 id 组件不需要返回这个组件那么ok这样写就可以了加个图示吧就是排除下滑线 id 制度ok 也说我这个也不需要返回然后走我们来看一下它的一个执行的结果
[08:35] OK那么我们可以看到返回的一个结果是不是就是这样的结果那么显然的这个结果是不是就是比较符合我们这个需求了OK大了我还是在重塑重做一遍就是这个需求不一定合理但是我们仅仅是为了给大家去演示它的API的使用OK
[08:53] 好那么第一个这个查询我们是不是就搞定了好那么我们先把这个视频呢我们先停一下后面的一些新增了修改三组呢我们后面再讲啊哎OK那么关于查询我们就先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

