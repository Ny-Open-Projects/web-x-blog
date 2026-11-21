# 画面线理解：21.搭建微聊系统以及编写基础代码

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\21.搭建微聊系统以及编写基础代码【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:35, 01:32, 02:13, 02:44, 03:32, 03:56, 04:21, 04:50, 06:39, 08:14, 09:28, 11:50, 12:56, 13:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:47:01

1) 这一组画面整体在讲什么（一句话）：
搭建一个基于 Spring Boot 和 MongoDB 的即时通讯系统，包括创建工程、编写 Message 和 User 对象、以及构造用户数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程讲义 PDF 的第 4 章“搭建微聊系统”，说明使用 Spring WebSocket 和 Spring-data-MongoDB 技术。
画面 2: IntelliJ IDEA 界面，提示项目已存在，准备创建 Maven 项目。
画面 3: 显示 pom.xml 文件内容，包含项目的基本配置。
画面 4: 展示 pom.xml 中的 <dependencies> 部分，列出 Spring Boot Web、MongoDB Driver、WebSocket 等依赖。
画面 5: 展示 pom.xml 中的测试依赖，包括 JUnit。
画面 6: 讲义 PDF 中的“4.2. 编写 Message 对象”，开始编写 Message 类。
画面 7: 讲义 PDF 中的“4.2. 编写 Message 对象”，继续展示 Message 类的代码。
画面 8: IntelliJ IDEA 中编写 Message.java，使用 @Indexed 注解。
画面 9: IntelliJ IDEA 中编写 Message.java，添加 @Field 注解。
画面 10: IntelliJ IDEA 中编写 Message.java，添加 @Indexed 注解。
画面 11: IntelliJ IDEA 中编写 User.java，定义 User 类。
画面 12: 讲义 PDF 中的“构造用户数据”，展示 UserDate 类的代码。
画面 13: IntelliJ IDEA 中显示 UserDate.java 的代码。
画面 14: 讲义 PDF 中的“4.2. 编写 Message 对象”，展示 Message 类的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast.haoke.im</groupId>
    <artifactId>itcast-haoke-im</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>
```

画面 4:
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-mongodb</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.mongodb</groupId>
        <artifactId>mongodb-driver-sync</artifactId>
        <version>3.9.1</version>
    </dependency>
</dependencies>
```

画面 5:
```xml
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.12</version>
    <scope>test</scope>
</dependency>
```

画面 6:
```java
package cn.itcast.haoke.im.pojo;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;
import java.util.Date;
@Data
@Builder
public class Message {
```

画面 8:
```java
@Indexed
private Date readDate;
```

画面 9:
```java
@Field("send_date")
@Indexed
private Date sendDate;
@Field("read_date")
@Indexed
private Date readDate;
```

画面 11:
```java
package cn.itcast.haoke.im.pojo;
import lombok.Data;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.NoArgsConstructor;
public class User {
    private Long id;
    private String username;
}
```

画面 12:
```java
package cn.itcast.haoke.im.pojo;
import java.util.HashMap;
import java.util.Map;
public class UserData {
    public static final Map<Long, User> USER_MAP = new HashMap<>();
    static {
        USER_MAP.put(1001L, User.builder().id(1001L).username("zhangsan").build());
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“4. 搭建微聊系统”，副标题“下面我们将开发微聊系统，实现好客房屋项目的即时通讯功能。”，技术列表为“Spring WebSocket”、“Spring-data-MongoDB”。
画面 6: PPT 标题为“4.2. 编写 Message 对象”。
画面 12: PPT 标题为“构造用户数据”，代码部分为“USER_MAP.put(1001L, User.builder().id(1001L).username("zhangsan").build());”等。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
