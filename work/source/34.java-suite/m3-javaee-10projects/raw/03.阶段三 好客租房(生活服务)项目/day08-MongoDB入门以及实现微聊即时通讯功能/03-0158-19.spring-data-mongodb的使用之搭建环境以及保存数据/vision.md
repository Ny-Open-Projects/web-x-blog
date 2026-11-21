# 画面线理解：19.spring-data-mongodb的使用之搭建环境以及保存数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\19.spring-data-mongodb的使用之搭建环境以及保存数据【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:19, 01:42, 02:16, 03:12, 04:12, 04:46, 05:44, 06:18, 06:40, 07:05, 07:33, 07:55, 08:41, 09:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:45:38

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中集成 MongoDB，并实现对 Person 实体的增删改查操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档，介绍 Spring Boot 整合 MongoDB，使用 spring-data-mongodb 简化操作，并提供官方文档链接。
画面 2: 展示 Maven 依赖配置，添加 spring-boot-starter-parent 和 spring-boot-starter-data-mongodb 依赖。
画面 3: 展示配置文件 application.properties，设置 Spring Boot 应用名称和 MongoDB 连接 URI。
画面 4: 展示 IntelliJ IDEA 中 application.properties 文件内容，确认 MongoDB 连接配置，并显示测试通过。
画面 5: 展示 PersonDAO 类的初始结构，声明 private MongoTemplate 成员变量。
画面 6: 展示 PersonDAO 类，添加 @Autowired 注解注入 MongoTemplate。
画面 7: 展示 PersonDAO 类，添加 savePerson 方法，使用 mongoTemplate.save(person) 保存数据。
画面 8: 展示 MongoApplication.java 文件，设置包名 cn.itcast.mongodb。
画面 9: 展示 MongoApplication.java 文件，添加 @SpringBootApplication 注解。
画面 10: 展示 TestSpringPerson.java 文件，添加 @RunWith(SpringRunner.class) 注解。
画面 11: 展示 TestSpringPerson.java 文件，添加 @SpringBootTest 注解。
画面 12: 展示 TestSpringPerson.java 文件，添加 @Test 注解的 testSave 方法。
画面 13: 展示 TestSpringPerson.java 文件，创建 Person 对象并调用 personDAO.savePerson(person) 方法。
画面 14: 展示 MongoDB Shell 中查询结果，显示 Person 实体数据，包括 name、age、address 等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>1.0.RELEASE</version>
</parent>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-mongodb</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
```

画面 3:
```properties
# Spring boot application
spring.application.name = itcast-mongodb
spring.data.mongodb.uri=mongodb://172.16.55.185:27017/testdb
```

画面 5:
```java
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.stereotype.Component;

@Component
public class PersonDAO {
    private MongoTemplate mongoTemplate;
}
```

画面 6:
```java
import org.springframework.stereotype.Component;

@Component
public class PersonDAO {
    @Autowired
    private MongoTemplate mongoTemplate;
}
```

画面 7:
```java
import org.springframework.stereotype.Component;

@Component
public class PersonDAO {
    @Autowired
    private MongoTemplate mongoTemplate;

    public Person savePerson(Person person) {
        return this.mongoTemplate.save(person);
    }
}
```

画面 8:
```java
package cn.itcast.mongodb;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MongoApplication {
    public static void main(String[] args) {
        SpringApplication.run(MongoApplication.class, args);
    }
}
```

画面 10:
```java
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class TestSpringPerson {
}
```

画面 11:
```java
import cn.itcast.mongodb.spring.PersonDAO;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class TestSpringPerson {
    @Autowired
    private PersonDAO personDAO;
}
```

画面 12:
```java
@Test
public void testDelete() {
    DeleteResult deleteResult = this.personCollection.deleteMany(eq("name", "张三"));
    System.out.println(deleteResult);
}
```

画面 13:
```java
@Test
public void testSave() {
    Person person = new Person(ObjectId.get(), "张三", 20, "上海市", "南京西路", "666666");
    this.personDAO.savePerson(person);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
