# 画面线理解：13.MongoDB的JavaApi操作之建立连接、选择数据库、表等操作

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\13.MongoDB的JavaApi操作之建立连接、选择数据库、表等操作【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:29, 01:10, 01:38, 02:38, 03:26, 03:49, 04:31, 05:24, 05:56, 06:42, 07:31, 08:02, 08:29, 09:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:41:45

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
