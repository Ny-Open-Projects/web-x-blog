# 19.spring-data-mongodb的使用之搭建环境以及保存数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\19.spring-data-mongodb的使用之搭建环境以及保存数据【海量资源尽在 ubkz.com】.mp4
- 时长 9分24秒（音频 564s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来看一下使用这个Spring Boot去整合MongoDB那么前面呢我们是直接使用了MongoDB提供的Java API去做一些使用这个呢是偏向于更底层一点的那么其实我们在做项目的时候呢往往呢不太可能直接去使用它的API去做我们项目的开发那么更多呢我们会去整合到我们的Spring充去做这样的一些开发
[00:25] 而Spring Data它有个项目叫做Spring Data MongoDB其实就是去整合了一些MongoDB的API的一些使用然后可以让它的使用变得更加的简单这个就是这个项目的一个初衷那么感兴趣的同学可以去点击这个网址然后去打开Spring Data MongoDB的一个官网去看一下它的一些介绍在这我们就不去看了
[00:51] 那么我相信大家呢应该是看到这个项目就应该能够明白他要做什么因为SpringData或包括Spring他的一些定位就是这样的可以让一些我们的一些呃这种操作啊变得就更加的简单吧哎OK好那么所以我们在做项目的时候呢我们更多的会选用啊这样的一种方式去做使用而不会直接去选择他的API去做一些使用哎OK好那么下面我们就来看一下怎么样去使用呢
[01:17] 那么首先我们需要导入一些依赖那么我们首先要说明的一点是我们现在使用的是SpinBoot这个框架是做我们的项目的开发那么SpinBoot并没有说对MongoDB做支持而是SpinBoot对着MongoDB做了支持但是SpinBoot中是没有整合了它所以我们可以直接去使用我们的MongoDB了所以说我们还是先要导入的是SpinBoot的依赖那么我们要给它设置一个parent那我们来看一下
[01:45] 那么我们去找到我们这个POP文件在POP文件中我们来给他设置一个parent就是我们的Spring Boot的一个parent然后下面我们来给他导入一些依赖导入什么导入这个Spring Data的MongoDB以及下面的一个Spring Boot的一个测试单元测试的一个依赖能把这个拷进来OK然后我们把它拷贝到这个位置好那么到这里我们相关的依赖就已经全部都导入进来了
[02:15] 那么导入进来之后我们就可以去做一些开发了OK那么第二步我们去编写一个配置文件就是我们的applicationpublish文件这个配置文件就是spring的一个这样的配置文件对不对全局的配置文件OK来拷贝一下然后我们在resource这个下面我们去创建一个文件就是applicationpublish文件把下面这个内容我们贴过来来看一下那么在这个里面我们可以看到
[02:44] 这个呢是我们的一个应用的一个名字而下面的这个就是芒果DB的一个连接的一个字符创那么我们可以看到是不是他连接到是不是就是我们那个testdb啊这样的一个地址这个跟我们刚刚写写我们这个demo的时候地址是不是一模一样啊来看一下地址是不是一样的哎OK大家呢可能会有点不一样的是后面他没有一个这个数据库对吧而在sprintd中的一个
[03:11] 这个连接字符串中呢是不是已经包含了一个这个数据库了哎OK好那么下面呢我们就来编写代码来去看一下SpringData MongoDB啊它的API怎么去用那么我们在这个下面呢创建一个包就叫Spring那么我们把一些相关的一些呃代码呢都写到这个里面来然后呢下面呢我们创建一个类啊就叫PersonDAO
[03:37] 那么这个里面显然就是一些CLUD的操作对不对所以我们需要把它作为是一个component实际我们在做项目开发的时候它应该是写一个接口然后我们再去写这个接口的实现类但是我们在这个位置仅仅是去测试它的API所以我们就不去写一个接口了我们直接写这个类来做这样的一个测试那么下面我们在这个位置需要去注入一个spring
[04:05] DataMongoDB中所提供的一个叫做MongoMongo什么呢Template模板那么Spring是不是非常擅长玩的就是模板对吧所以我们把它拿过来用它之后使用起来就会变得非常的方便了那么下面我们来看一下怎么样去做一个使用那么我们在下面我们先写一个保存新增的这样的一个方法
[04:33] 就public返回值返回一个word然后做一个sale person然后我们来看一下显然他肯定要传递一个参数叫什么personok那么person就需要调用this.mongo-template.sale做sale操作要注意的是在这个位置我们可以看到sale有两个选择第一个是一个参数第二个是两个参数
[04:58] 那么第二个参数呢多一个叫connect name其实就是我们的一个表明那么我们如果不去传递这个表明的话他默认就会使用我们这个对象的一个名字当然了手字们要进行小写啊这样的一个数据库作为他这个保存的一个数据库啊那么我们给他使用默认就可以了所以我们选择第一个啊这个方法就OK了好那么我们做一个save的一个操作那么save把这个person啊传递过来哎呀OK这样的话其实他就完成了一个操作那么我们来看他有没有返回值呢
[05:27] 它的返回值是一个t那么其实就是我们的一个t是不是就代表就是我们这个保存这个对象啊所以呢我们是不是可以这样让它returnreturn什么的这个person哎ok它呢是这样的一个逻辑啊ok那么到这里呢我们这个方法是不是就已经写完了那么写完之后呢我们是不是就可以去写我们的一个启动类
[05:51] 然后我们再去做一些相关的一些测试对吧那么我们先来去写它的启动类然后写测试用力先测试这么一个方法后面的方法我们再去做一个测试然后在这个位置我们写它的一个Spring Boot的启动类那么就叫Mongo MongoDB叫Mongo吧Application这个类然后我们去写一个PSVM然后我们去给它加一个注解就叫什么呢Spring Boot Application
[06:21] 然后下面使用一个叫做spring-application.raw,raw谁呢是不是就是我们这个类对吧点,点,class然后参数就是args好这样的话我们这个spring-boot的应用是不是就跑起来了那么接下来我们就需要去编写它的一个测试用例那么我们就在这个下面这个下面去创建一个类那么我们就叫test一个spring然后person好那么
[06:52] 这个呢,显然就是我们去测试Spring的一个这样的一个玩法那么我们再加一个注解叫run with, with什么呢Spring一个runner.class然后呢,再去给他加一个注解就叫Spring boot test这样的一个注解那么下面呢我们是不是就可以直接去注入我们刚刚所写的这个什么呢PersonPerson什么的DAO把他是不是注入进来是不是做测试就可以了做一个注入
[07:22] 然后下面我们是不是写一个方法去做测试word test什么叫c5好来看一下那么在这个位置我们去写一个test然后下面这个内容怎么写是不是可以调用类似点person.do.c5操作对吧那么我们来给它去构造一个person等于new一个personOK那么这个代码我们就call一下
[07:52] 在我们前面是不是写过这个操作啊写过这个操作那么我们来靠一下啊靠一个这个posten就他吧哎ok好那把它靠过来那么那就我们就不一个去设置值了啊那么我们就使用他就可以了哎ok那么这样的话我们是不是就可以做一个保存了呢咱们把这个里面内容呢我们去改一下吧在这个名字改成什么刘德华然后呢年龄啊50
[08:20] 然后呢它的地址呢是香港对吧香港是人民路吧香港好那么然后呢这个邮编就随便了给它默认为6然后呢我们做一个这个save操作那我们来看一下我们就直接执行吧来看一下它能不能够把数据保存到我们的数据库呢好那么现在呢就执行结束了没有报错没有报错好那么下面我们就来看一下
[08:53] 我们的数据有没有保存到我们的芒果DB里面来做一个file查找那么显然我们可以看到在这个位置是不是我们已经把数据保存进来了对吧这个名字就是刘德华这样的一个用户已经是保存进来了ok好那么当然了要注意的是你可以看到在sweep保存完之后它有一个class代表的就是这个类是哪个类class保存进来了ok
[09:20] 好那么这个呢就是我们所讲的第一个这个sale这个操作啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

