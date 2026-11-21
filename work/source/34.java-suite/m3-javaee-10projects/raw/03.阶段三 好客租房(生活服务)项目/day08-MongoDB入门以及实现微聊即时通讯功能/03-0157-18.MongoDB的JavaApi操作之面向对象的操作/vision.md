# 画面线理解：18.MongoDB的JavaApi操作之面向对象的操作

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\18.MongoDB的JavaApi操作之面向对象的操作【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:40, 01:19, 01:54, 02:51, 03:46, 04:36, 05:11, 05:41, 06:32, 07:17, 07:50, 08:33, 08:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:45:05

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Java 面向对象方式操作 MongoDB，包括创建实体类、初始化连接、增删改查操作及测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中“2.4、面向对象操作”章节，介绍通过面向对象方式操作 MongoDB，并展示 Person 和 Address 类的代码结构。
画面 2: PDF 文档中高亮显示 Person 类的代码，包含 Lombok 注解和私有字段。
画面 3: PDF 文档中展示 Address 类的代码，包含 street、city、zip 字段。
画面 4: IDE 中展示 TestMongoDBDemo.java 文件的 init() 方法，用于初始化 MongoDB 连接和集合。
画面 5: IDE 中展示 TestMongoDBDemo.java 文件的 init() 方法，高亮显示创建 MongoClient 和选择数据库的代码。
画面 6: IDE 中展示 TestMongoDBDemo.java 文件的 testInsert() 方法，用于插入单个 Person 对象。
画面 7: IDE 中展示 TestMongoDBDemo.java 文件的 testInsert() 方法，终端显示“插入数据成功”，测试通过。
画面 8: IDE 中展示 TestMongoDBDemo.java 文件的 testInserts() 方法，用于批量插入多个 Person 对象。
画面 9: IDE 中展示 TestMongoDBDemo.java 文件的 testQuery() 方法，用于查询 name 为“张三”的 Person 对象。
画面 10: IDE 中展示 TestMongoDBDemo.java 文件的 testUpdate() 方法，用于更新 name 为“张三”的 Person 对象的 age 字段。
画面 11: PDF 文档中展示“3、SpringBoot整合MongoDB”标题，以及 Person 和 Address 类的代码。
画面 12: IDE 中展示 TestMongoDBDemo.java 文件的 testDelete() 方法，用于删除 name 为“张三”的 Person 对象。
画面 13: PDF 文档中展示“2.4、面向对象操作”章节，以及 Person 和 Address 类的代码。
画面 14: PDF 文档中展示“2.4、面向对象操作”章节，以及 Person 和 Address 类的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package cn.itcast.mongod8;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.bson.types.ObjectId;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Person {
    private ObjectId id;
    private String name;
    private int age;
    private Address address;
}
```

画面 2:
```java
package cn.itcast.mongod8;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.bson.types.ObjectId;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Person {
    private ObjectId id;
    private String name;
    private int age;
    private Address address;
}
```

画面 3:
```java
package cn.itcast.mongod8;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.bson.types.ObjectId;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Address {
    private String street;
    private String city;
    private String zip;
}
```

画面 4:
```java
public void init() {
    // 定义对象的解码注册器
    CodecRegistry pojoCodecRegistry = CodecRegistries
            .fromRegistries(MongoClientSettings.getDefaultCodecRegistry(),
                    CodecRegistries.fromProviders(PojoCodecProvider.builder().automatic(true).build()));
    // 建立连接
    MongoClient mongoClient = MongoClient.create("mongodb://172.16.55.185:27017");
    // 选择数据库，并且 注册解码器
    MongoDatabase mongoDatabase = mongoClient.getDatabase(databaseName: "testdb")
            .withCodecRegistry(pojoCodecRegistry);
    // 选择表
    this.personCollection = mongoDatabase
            .getCollection(collectionName: "person", Person.class);
}
```

画面 5:
```java
public void init() {
    // 定义对象的解码注册器
    CodecRegistry pojoCodecRegistry = CodecRegistries
            .fromRegistries(MongoClientSettings.getDefaultCodecRegistry(),
                    CodecRegistries.fromProviders(PojoCodecProvider.builder().automatic(true).build()));
    // 建立连接
    MongoClient mongoClient = MongoClient.create("mongodb://172.16.55.185:27017");
    // 选择数据库，并且 注册解码器
    MongoDatabase mongoDatabase = mongoClient.getDatabase(databaseName: "testdb")
            .withCodecRegistry(pojoCodecRegistry);
    // 选择表
    this.personCollection = mongoDatabase
            .getCollection(collectionName: "person", Person.class);
}
```

画面 6:
```java
@Test
public void testInsert() {
    Person person = new Person(ObjectId.get(), name: "张三", age: 20, new Address(street: "人民路", city: "上海", zip: "666666"));
    this.personCollection.insertOne(person);
    System.out.println("插入数据成功");
}
```

画面 7:
```java
@Test
public void testInsert() {
    Person person = new Person(ObjectId.get(), name: "张三", age: 20, new Address(street: "人民路", city: "上海", zip: "666666"));
    this.personCollection.insertOne(person);
    System.out.println("插入数据成功");
}
```

画面 8:
```java
@Test
public void testInserts() {
    List<Person> personList = Arrays.asList(
            new Person(ObjectId.get(), name: "张三", age: 20, new Address(street: "人民路", city: "上海", zip: "666666")),
            new Person(ObjectId.get(), name: "李四", age: 21, new Address(street: "北京西路", city: "上海市", zip: "666666")),
            new Person(ObjectId.get(), name: "王五", age: 22, new Address(street: "南京东路", city: "上海市", zip: "666666")),
            new Person(ObjectId.get(), name: "赵六", age: 23, new Address(street: "陕西南路", city: "上海市", zip: "666666")),
            new Person(ObjectId.get(), name: "孙七", age: 24, new Address(street: "南京西路", city: "上海市", zip: "666666"))
    );
    this.personCollection.insertMany(personList);
    System.out.println("插入数据成功");
}
```

画面 9:
```java
@Test
public void testQuery() {
    this.personCollection.find(Filters.eq("name", "张三"))
            .forEach((Consumer<? super Person>) person -> {
                System.out.println(person);
            });
}
```

画面 10:
```java
@Test
public void testUpdate() {
    UpdateResult updateResult = this.personCollection.updateMany(
            eq(fieldName: "name", value: "张三"),
            Updates.set("age", 22)
    );
    System.out.println(updateResult);
}
```

画面 11:
```java
@Test
public void testUpdate() {
    UpdateResult updateResult = this.personCollection.updateMany(
            eq(fieldName: "name", value: "张三"),
            Updates.set("age", 22)
    );
    System.out.println(updateResult);
}
```

画面 12:
```java
@Test
public void testDelete() {
    DeleteResult deleteResult = this.personCollection.deleteOne(eq(fieldName: "name", value: "张三"));
    System.out.println(deleteResult);
}
```

画面 13:
```java
@Test
public void testInserts() {
    List<Person> personList = Arrays.asList(
            new Person(ObjectId.get(), name: "张三", age: 20, new Address(street: "人民路", city: "上海", zip: "666666")),
            new Person(ObjectId.get(), name: "李四", age: 21, new Address(street: "北京西路", city: "上海市", zip: "666666")),
            new Person(ObjectId.get(), name: "王五", age: 22, new Address(street: "南京东路", city: "上海市", zip: "666666")),
            new Person(ObjectId.get(), name: "赵六", age: 23, new Address(street: "陕西南路", city: "上海市", zip: "666666")),
            new Person(ObjectId.get(), name: "孙七", age: 24, new Address(street: "南京西路", city: "上海市", zip: "666666"))
    );
    this.personCollection.insertMany(personList);
    System.out.println("插入数据成功");
}
```

画面 14:
```java
package cn.itcast.mongod8;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.bson.types.ObjectId;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Person {
    private ObjectId id;
