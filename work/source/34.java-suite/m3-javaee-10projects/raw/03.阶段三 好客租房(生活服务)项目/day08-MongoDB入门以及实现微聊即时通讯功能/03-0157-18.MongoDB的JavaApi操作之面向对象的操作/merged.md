# 18.MongoDB的JavaApi操作之面向对象的操作

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\18.MongoDB的JavaApi操作之面向对象的操作【海量资源尽在 ubkz.com】.mp4
- 时长 9分1秒（音频 541s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来看一下面向对象的操作或者说要基于对象的操作啊那么前面呢我们都是通过基于Document对象对我们的MongoDB做了一些操作比如说像这个Insert的时候呢使用都是Document那么其实呢我们这样编写的时候呢对我们在编写代码的时候呢其实并不太方便啊那我们更希望是通过一些对象比如说叫User对象或者Person对象去做一些这样的操作会更方便一点
[00:28] 那么MongoDB也提供了这样的一个操作那我们来一起来看一下那么首先我们来创建这么两个对象一个是person一个是addressOK那么这个是我们的用户这个对象那么咱们就把它拷贝一下然后丢到我们代码中就是丢到这个里面来吧丢到这然后有个person然后下面还有一个address把它也来拷贝一下我再一call好嘞那么把代码格式简单的去
[00:59] 整理一下person把这格式简单的给他整理一下好那么这样的话我们就有了两个类一个是person一个是address这两个类那么下面我们就基于这两个类去做一些使用当然他们类里面的一些字段都是一些比较基础性的一些字段ok好那么下面我们来看一下他的一些操作下面我们编写一个test person这样的一个用例
[01:26] 测试用力我们去做一个这样的一个测试然后呢在这个里面呢我们去写一个这个init啊这个方法把这个拷过来拷一下拷过来我们去解读一下这个代码那么在这个里面呢就做了一些初始化的一些这个操作跟我们前面所写的这个连接啊也差不多只是呢它有一点点不同啊有一点点不同在哪呢就是在这个位置我们定义了一个
[01:58] 对象的一个解码器对象的解码器那么这个代码大家就按照这个代码的固定格式去写就可以了那么得到一个注册的代码的解码器那么通过这个解码器之后我们就可以去给我们的一个database去注册这样的一个解码器那么也就是说它会将我们的这个document跟我们的对象之间做这样的一个映射OK好那么
[02:25] 然后我们在下面在选择表的时候我们给他设置一个对象叫personGetConnection然后后面指定一个person的class我们来看一下前面我们所写的getConnection并没有指定后面的class对不对在这个位置所指定的classok那么就是这个类型的person这种类型的一个mongo的一个connection那么有了它之后就可以做一系列的clu的操作
[02:53] 那我们就还是去拷贝代码吧我们去看一下他的一些代码编写就可以了大家应该很容易就能够看懂那么咱们把这个拷过来一直拷贝到这OK好那么我们来看一下在这个位置我们是不是定义了一个person这样的一个对象然后他的一些他的 id是不是我们把它设置为是object id这个就是去生成他的一个
[03:23] 那个组件的一个IDget通过这个get这个方法就生成一个组件那么这个张三的就是我们那个名字然后呢这个年龄20他的地址是一个对象注意在这个位置是一个对象就是说在我们这个portion中他其实不简单的是一些这个属性而是有一个对象的一个属性那我们来看一下他是如何去就是说插入到数据库里面是什么样的一个结构那我们来看一下
[03:52] 我们直接执行这个音色的一个方法那么数据是不是差不多成功了那我们来看一下那么我们通过db点什么的person吧点friend是不是去查看那么这个里面呢是不是就会有一条这个数据那么要注意的是这个advance它本身的又是一个对象看到了吗本身是不是又是一个对象哎OK好那么这个是不是就是属于对象的一个嵌套对象的一个嵌套
[04:27] 好嘞那么这个就是我们的一个插入数据插入一条数据那么我们还可以让他什么插入多条数据来看一下到这这个是这个应该是拷贝过来的格式的问题那么是有换行了到这然后到这有换行会报错好把它拿过来把这个市也拿过来像上海市ok
[05:00] 好,那么我们构造了这么几条数据然后怎么做一个insert的一个money就是去插入多条数据来看一下他能不能把这么几条数据都插进去呢哎呀ok好,那么我们来看一下是不是插入了多条数据啊哎呀ok这个呢就是插入多条数据的一个演示啊这个代码都比较简单啊大家一看就能看懂那么下面我们来看一下他的一个查询啊他这个查询这个查询啊这个查询跟我们之前所写那个查询呢
[05:31] 差不多只是呢他返回的是一个什么对象返回的是一个person对象那么我们直接去拿到对象就可以了而不是一个一个字段去拿OK好那么我们来去看一下Fed查学一样代码机或者一样的只有在这个位置有点不一样好嘞那我们走那我们拿到的是一个对象而不是一个那个document好那我们把这个person给它打印出来那么可以看到这是不是就是我们打印出来的一个对象
[06:01] 那么直接就会把数据分装到我们对象中这样的话我们使用起来是不是更加的方便OK好嘞那么我们接着继续往下面看下面的这个是做一个update那么update我们来看一下它是怎么玩的呢基于对象的一个操作通过这connection update many更新多条数据那么依然设置一个查询条件是不是通过EQ对吧当然了这个我们给它设置为静态对吧EQ
[06:31] 就是内幕等于张三的时候然后呢去给他去修改一个什么呢年龄改成22岁哎OK好那么咱们好那么这样的话是不是就做了这样的一个修改那么走这个修改就非常的一样了啊非常类似了好来看一下他的更新的一个结果那么可以看到更新的结果呢是他匹配了这两条然后呢修改了这两条啊那么也就是说现在已经修改了两条数据了
[07:03] 那么我们是不是可以来查看一下吧张三这条数据啊有没有被修改成年龄为22那么找一下这个这一条这一条哎这两条可以看到是不是都已经被修改成22了哎OK好这个呢就是更新下面我们来看一下删除把这个拷过来那删除这个操作代码呢跟我们前面写代码呢是一样的啊呃只是呢只是这个
[07:30] 面向对象这种操作只是我们在做查询的时候是不是是不一样一些那么其他的更新和删除都是一样的ok好那么我们就把这个名字等于张三的数据都给他删掉走来看一下能不能删除掉那么可以看到他是不是已经删除掉一条数据了对吧ok为什么是一条我们明明有两条对吧在这个位置我们调用的是delete one
[08:02] 那么显然是不是他就删除一条是对的啊没有问题好嘞那么我们如果删除多条那么是就来一个delete什么的money是不是就可以了哎ok好那么再删除他也是一条了因为张三只有一条了哎来看一下这样的话也可以删除好那么这个我就不多演示了啊大家可以去再构造几条这个张三的数据然后呢去让他去做一个删除他一定呢也是删除多条数据啊
[08:31] OK好那么关于这个面向对象的一个操作我们就讲到这那么其实在这个里面的主要是给大家演示的不同的点其实就是在我们的数据的插入跟我们的一个数据的一个查询在一块它直接操作的是一个我们自定义的一个对象而不是我们的一个它内置的一个document的对象OK主要是要表达这个意思那么显然这种方式是不是我们用起来会更加的方便一点OK好那么面向对象的这个操作我们就讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面 11: PDF 文档中展示“3、Spring Boot整合MongoDB”标题，以及 Person 和 Address 类的代码。
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

