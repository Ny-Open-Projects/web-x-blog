# 画面线理解：25.Spring Data Elasticsearch使用之工程搭建以及新增数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\25.Spring Data Elasticsearch使用之工程搭建以及新增数据【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:14, 01:16, 02:05, 02:49, 04:12, 04:45, 05:31, 07:17, 07:50, 08:22, 08:58, 09:35, 10:45, 11:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:58:15

1) 这一组画面整体在讲如何使用 Spring Boot 整合 Elasticsearch 实现数据的增删改查功能。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Elasticsearch Head 插件界面，显示名为 "house" 的索引中包含多个房屋数据记录，包括 id、title、price 等字段。
画面2：展示 PDF 文档第4.1节，说明采用 Spring Boot 整合方式，并列出 Maven 依赖的父项目配置。
画面3：展示 PDF 文档第4.1节，列出具体的 Maven 依赖，包括 elasticsearch-rest-client、elasticsearch-rest-high-level-client、junit、jackson-databind、lombok 等。
画面4：展示 IntelliJ IDEA 中的 application.properties 配置文件，设置 spring.application.name 为 itcast-elasticsearch，以及 Elasticsearch 集群名称和节点地址。
画面5：展示 PDF 文档第4.3节，说明编写启动类，并给出 MyApplication.java 的代码示例。
画面6：展示 IntelliJ IDEA 中的 MyApplication.java 文件，显示包名 cn.itcast.es 和 main 方法。
画面7：展示 Elasticsearch Head 插件界面，页面为空白，未显示任何索引或数据。
画面8：展示 IntelliJ IDEA 中的 User.java 文件，定义了 User 实体类，包含 id、name、age、hobby 字段，并使用 @Field 注解。
画面9：展示 IntelliJ IDEA 中的 TestSpringBootES.java 文件，显示 @RunWith(SpringRunner.class) 注解。
画面10：展示 IntelliJ IDEA 中的 TestSpringBootES.java 文件，导入必要的测试和 Elasticsearch 相关包。
画面11：展示 IntelliJ IDEA 中的 TestSpringBootES.java 文件，声明私有属性 ElasticsearchTemplate。
画面12：展示 IntelliJ IDEA 中的 TestSpringBootES.java 文件，创建 User 对象并调用 index 方法。
画面13：展示 IntelliJ IDEA 中的 TestSpringBootES.java 文件，设置 User 对象的属性并构建 IndexQuery。
画面14：展示 PDF 文档第4.4.1节，显示 testSave() 方法的完整代码，用于测试保存数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
        http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.0.RELEASE</version>
    </parent>
```

画面3：
```xml
<dependency>
    <groupId>org.elasticsearch.client</groupId>
    <artifactId>elasticsearch-rest-client</artifactId>
    <version>6.5.4</version>
</dependency>
<dependency>
    <groupId>org.elasticsearch.client</groupId>
    <artifactId>elasticsearch-rest-high-level-client</artifactId>
    <version>6.5.4</version>
</dependency>
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.12</version>
</dependency>
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.9.4</version>
</dependency>
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.4</version>
</dependency>
```

画面4：
```properties
spring.application.name=itcast-elasticsearch
spring.data.elasticsearch.cluster-name=es-itcast-cluster
spring.data.elasticsearch.cluster-nodes=172.16.55.185:9300,172.16.55.185:9301,172.16.55.185:9302
```

画面5：
```java
package cn.itcast.es;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

画面8：
```java
public class User {
    @Id
    private Long id;
    @Field(store = true)
    private String name;
    @Field
    private Integer age;
    @Field(store = true)
    private String hobby;
}
```

画面10：
```java
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.data.elasticsearch.core.ElasticsearchTemplate;
import org.springframework.test.context.junit4.SpringRunner;
```

画面11：
```java
@Autowired
private ElasticsearchTemplate elasticsearchTemplate;
```

画面12：
```java
User user = new User();
```

画面13：
```java
user.setId(1001L);
user.setName("张三");
user.setAge(20);
user.setHobby("足球、篮球、听音乐");
IndexQuery indexQuery = new IndexQueryBuilder()
        .withObject(user).build();
String index = this.elasticsearchTemplate.index(indexQuery);
System.out.println(index);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面5：PPT标题为“4.3、编写启动类”，内容为 Spring Boot 启动类的代码示例。
画面14：PPT标题为“4.4.1、编写 User 对象”，内容为 testSave() 方法的完整代码。

5) 不要评价画面美观，不要输出与课程无关的内容。
