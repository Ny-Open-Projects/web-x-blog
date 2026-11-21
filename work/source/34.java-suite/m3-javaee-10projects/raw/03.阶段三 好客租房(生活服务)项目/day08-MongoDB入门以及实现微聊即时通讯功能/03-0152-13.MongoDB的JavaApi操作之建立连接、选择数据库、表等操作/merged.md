# 13.MongoDB的JavaApi操作之建立连接、选择数据库、表等操作

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\13.MongoDB的JavaApi操作之建立连接、选择数据库、表等操作【海量资源尽在 ubkz.com】.mp4
- 时长 9分18秒（音频 558s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来看一下MongoDB的Java API的一些相关的一些操作这个呢其实就和我们在使用MySQL数据库是一样的那么MySQL呢为Java提供了一个API那么也就是它的驱动包那么我们对MySQL呢就可以通过Java代码去做操作同样呢我们也可以通过Java代码呢对MongoDB做一个操作那么下面呢我们来创建一个工程那么这个工程呢我们就叫它ATCastMongoDB那么我们接下来创建这个工程
[00:29] 然后在这个位点击这个create new project然后我们点击它然后我们去等待它的一个loading然后我们点击下一步下一步呢,国外订的那就是cm.itcast.mongoDB然后artifact id就是这个itcast.mongoDBnext然后拷贝然后我们去做一个finish完成
[00:55] 那么接下来呢我们的工程呢就创建好了那么创建好之后呢我们就需要给他去引入一些必要的一些依赖啊我们来看一下那么在这个里面呢我们给他去导入一些依赖那么导入什么依赖呢哎把这个来写一下啊dependence啊然后呢我们去导入一些这个mongo db的一些驱动啊以及这个junit啊一些这个依赖因为我们后面呢要去写
[01:23] 关于我们的一些这个mongodb的一些测试单元测试所以我们导入这个unit那么下面我们还需要把这个longbook也导入进来是不是我们去编写portal的时候就会变得非常的方便看起来比较简洁一点ok好那么现在这三个就导入进来了但是要注意的一点是那么我们新建的工程那么他并没有自动帮我们去导入我们的manual的依赖我们在这个位置要去去
[01:53] 点一下它就是enable auto import那么这样的话它就会做一个自动的一个导入OK那么下面我们再把这个配置过来这个是不是指定我们的Java的一个编译的一个版本我们设置为它是1.8OK好那么到这里我们基本上我们这个工程就已经搭建好了下面我们就来来写一个测试用例那么我们首先要解决的问题就是在我们的这个Java客户端它如何去连接到我们的蒙古DB
[02:22] 对吧就和我们在使用这个MySQL一样你首先先得创建一个连接对吧我们使用GDPC的时候去创建一个connection然后再去做后续的一些相关的操作所以我们先要去建立一个连接对不对那么我们来创建一个类我们来写一个测试那么就叫包名就叫cn.itcast然后点什么的mongo db然后在下面我们再去给他去创建一个类
[02:50] 这个类的名字就随意因为我们做demo测试我们就这样来写就叫mongoMongoDb然后demo那就写个demo好了然后在这个里面我们写一个我们的麦方法这下面做一个测试那么首先我们需要与我们的mongoDB建立连接那么建立连接那么建立连接怎么去建立要通过一个mongomongoclientmongo
[03:22] db the mongol然后呢有一个叫做clientusclientus下面这个客户端子然后呢点有一个叫create这个方法然后呢可以看到在这个位置是不是有一个连接支付串根据一个连接支付串去做一个连接那么它的返回值呢就是谁的就是一个mongol db client那么这个连接支付串怎么去写那我们来看一下
[03:47] 那么连接字符串呢我们是需要通过这种方式去写那么要注意它不是GDPC它是MongoDB冒号双斜杠后面跟我们的IP地址再加我们这个端口就可以了那么咱们把这个来靠一下就它拷贝过来那么它这个连接的字符串就是这样的当然了你们在这个位置要改成自己的一个IP地址对不对
[04:10] 好 那么有了这个客户端之后那么我们就要去干嘛呢大家回想一下那么前面我们去操作我们的MongoDB的时候还有印象吗那么我们在这儿我们就去进入我们的MongoDB然后通过一个Mongo去连接到我们的MongoDB那么下面我们就需要去Use一个数据库对不对TestDB然后再做一些相关操作
[04:33] 那么同样的在我们这个代码这个位置呢也是一个相同的这样的一个操作那么就需要通过这个mongodbmongodb的client然后呢点我们应该在下面啊应该在下面这个位置这个叫选择选择我们的数据库啊然后呢通过一个mongodb client点get什么database啊get database然后呢去获取到我们的一个数据库那么数据库叫什么呢testdb对吧
[05:04] 这个就是我们的数据库那么它的返回值呢就是一个mongodb的一个database那么有了这个database之后呢下面我们是不是就需要对我们的数据的表是不是做操作啊OK那所以下面要选择这个什么表那么选择表呢要通过这个数据库然后呢get什么connection通过我们这个名字啊就connect name去选择我们的这个connection
[05:32] 那么我们的表名比如说我们叫user现在我们是不是有一张表叫user叫show一个什么呢show一个叫tablestables那么可以看到是不是有一张表叫user所以我们选择这个user这张表那么它的返回值呢就是一个这个叫connection那么我们把它叫user connection吧ok叫useruser connection好那么有了这个connection之后呢下面我们是不是就可以
[06:05] 对MongoDB是不是做一个操作对吧就这个表做操作那么操作那么做什么操作呢我们就先来写一个基本的一个操作就叫UraConnection.Find去做一个查找查找什么呢就没有条件去做一个查找查找这个表里面所有的数据但是我们知道这张表里面数据是不是非常多那我们来看一下有多少条数据是不是通过一个叫做DB.Ura.Find然后点是不是可以来一个Count去查看一下
[06:35] 这边有1003条这边非常多那么现在我们没必要去拿那么多比方说我们想拿10条怎么办呢这边通过一个点limit就可以拿到他的10条数据然后呢拿到数据之后呢我们希望把这个数据呢给他打印出来那么怎么样打印呢在这个位置有个叫做for each啊for each这样的一个循环那么ok那么我们就需要给他传递一个叫回调函数啊回调函数或者算是我们那个接口的一个实现
[07:02] 那我们就来去使用这个GDK1.8的一个新特性是吧就Lambda表达式去做一个编写那么使用它那么我们来看一下在这个里面呢它还会有个报错就是说这个for each呢其实它有两个有两个类型的对吧一个是上面的这个block一个是consumer那么我们要使用的是下面的这个所以呢我们需要在这个位置呢给它去做一个强制的一个转换来我们来看一下是它OK
[07:31] 然后呢这样的话呢我们就可以去打印了比如说我们把这个document.tojson把它的这个数据呢转成一个json去打印出来那么最后呢我们要别忘记要把什么呢mongo要关闭关闭这个连接释放资源释放资源然后呢我们通过这个mongo db client.close
[07:55] 把这个客户端给它关闭掉好那么下面我们就针对于我们这个写的这么几行代码我们做一个测试ok走先建立连接选择数据库选择表做操作最后关闭连接这个跟我们的操作我们的通过GDPCG操作MySQL非常的类似也非常的相像好那么我们来等待它的一个输出那么可以看到
[08:18] 在这个位置呢是不是已经就把这个数据是不是就打印出来了哎OK好那么已经拿到我们的想要这个数据了对不对好那么这个就是我们给大家写的第一个这个例子那么可以看到在这个例子中呢我们通过一个voice这个循环那么就可以去读取到我们这个查询之后的这个结果那么如果有同学对这个Lambda表达是可能不太熟悉的话那可以采用下面这种方式就是我们去定义它实现一个这个接口
[08:47] consumer接口也可以的也是一样道理只是我们使用这个Lambda表达式就可以更加简单的或者说更加便捷的来实现这样的一个回调函数或者说一个接口的实现类OK好那么到这里我们第一个demo就给大家演示完毕了那么这个里面我们是不是演示了我们的如何去建立连接那么又如何去选择数据库如何选择表如何进行做查询然后如何去做一个便利
[09:15] OK好那么这个demo呢我们就先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 IntelliJ IDEA 中创建并编写一个连接 MongoDB 数据库、操作数据表的 Java Demo 程序。

2) 按时间顺序列出每张画面的要点：
画面1：打开 IntelliJ IDEA，选择项目 "itcast-mongodb"。
画面2：在 pom.xml 文件中查看并编辑 Maven 依赖配置，光标位于 <dependencies> 标签内。
画面3：在 pom.xml 中添加 MongoDB 驱动和 JUnit 依赖，光标位于 <groupId>org.projectlombok</groupId> 行。
画面4：在项目结构中右键点击 "src/main/java"，选择 "New" -> "Java Class" 创建新类。
画面5：在 MongoDBDemo.java 文件中，光标位于 main 方法内，显示了 MongoDB 的相关类和方法。
画面6：在 PDF 文档中，显示了 "2.2、编写Demo" 的章节内容，介绍了如何连接 MongoDB、选择数据库和表、进行查询操作。
画面7：在 Xshell 中连接到 MongoDB 服务器，执行命令切换到 testdb 数据库。
画面8：在 MongoDBDemo.java 中，光标位于 "database." 后，准备调用数据库相关方法。
画面9：在 MongoDBDemo.java 中，光标位于 "collection - database.getC..." 后，准备获取集合。
画面10：在 MongoDBDemo.java 中，光标位于 "userCollection.find().limit(10).forEach(..." 后，准备进行查询操作。
画面11：在 MongoDBDemo.java 中，光标位于 "forEach((Consumer<? super Document>) document -> {" 后，准备进行查询操作。
画面12：在 MongoDBDemo.java 中，右键点击 "System.out.println"，弹出上下文菜单。
画面13：在 PDF 文档中，显示了 "2.2、编写Demo" 的章节内容，介绍了如何连接 MongoDB、选择数据库和表、进行查询操作。
画面14：在 PDF 文档中，显示了 "2.2、编写Demo" 的章节内容，介绍了如何连接 MongoDB、选择数据库和表、进行查询操作。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast.mongodb</groupId>
    <artifactId>itcast-mongodb</artifactId>
    <version>1.0-SNAPSHOT</version>
    <dependencies>
        <dependency>
            <groupId>org.mongodb</groupId>
            <artifactId>mongodb-driver-sync</artifactId>
            <version>3.11</version>
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.12</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.16</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>
</project>
```

画面5：
```java
package cn.itcast.mongodb;

import com.mongodb.client.*;
import org.bson.Document;

public class MongoDBDemo {
    public static void main(String[] args) {
        MongoClient mongoClient = MongoClients.create("mongodb://172.16.55.185:27017");
        // 选择数据库
        MongoDatabase database = mongoClient.getDatabase("testdb");
        // 选择表
        MongoCollection<Document> userCollection = database.getCollection("user");
        // 操作
        userCollection.find().limit(10).forEach((Consumer<? super Document> document -> {
            System.out.println(document.toJson());
        });
        // 关闭连接，释放资源
        mongoClient.close();
    }
}
```

画面6：
```java
package cn.itcast.mongodb;

import com.mongodb.client.*;
import org.bson.Document;
import java.util.function.Consumer;

public class MongoDBDemo {
    public static void main(String[] args) {
        // 建立连接
        MongoClient mongoClient = MongoClients.create("mongodb://172.16.55.185:27017");
        // 选择数据库
        MongoDatabase mongoDatabase = mongoClient.getDatabase("testdb");
        // 选择表
        MongoCollection<Document> userCollection = mongoDatabase.getCollection("user");
        // 查询数据
        userCollection.find().limit(10).forEach((Consumer<? super Document> document -> {
            System.out.println(document.toJson());
        });
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面6、13、14：PPT 标题为 "2.2、编写Demo"，内容为 "该demo中演示了，如何连接到MongoDB，如何选择数据库、表，进行查询的操作。"

5) 不要评价画面美观，不要输出与课程无关的内容。

