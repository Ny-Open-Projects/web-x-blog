# 画面线理解：05.MybatisPlus入门之快速入门

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\05.MybatisPlus入门之快速入门【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:16, 01:30, 02:56, 04:33, 05:38, 06:52, 07:52, 08:25, 10:03, 11:46, 12:56, 13:53, 14:25, 15:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:41:14

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 MyBatis-Plus 框架快速实现数据库表的创建、配置、实体类编写、Mapper 接口定义及测试查询功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 课程 PDF 页面显示“2.4.1、创建表”，提示“首先，创建数据库：haoke”，并展示 Navicat 中数据库“haoke”的结构。
画面 2: Navicat Premium 中显示 SQL 语句，用于在“haoke”数据库中创建名为“user”的表，包含 id、name、age、email 字段，并设置主键和字符集。
画面 3: 课程 PDF 页面显示“2.4.3、编写 application.properties 文件”，并展示部分配置内容。
画面 4: IntelliJ IDEA 中显示项目 pom.xml 文件，包含 Spring Boot 父依赖和 MyBatis-Plus 的 starter 依赖。
画面 5: IntelliJ IDEA 中显示 pom.xml 文件的 <build> 部分，展示 Maven 的配置项。
画面 6: 课程 PDF 页面显示“2.4.3、编写 application.properties 文件”和“2.4.4、创建 User 对象”，并展示 application.properties 配置和 User.java 实体类代码。
画面 7: IntelliJ IDEA 中显示 User.java 文件，右键菜单中选中“Show in Terminal”。
画面 8: 课程 PDF 页面显示“2.4.5、编写 UserMapper”和“2.4.6、编写 SpringBoot 启动类”，并展示 UserMapper 接口的代码结构。
画面 9: IntelliJ IDEA 中显示 BaseMapper.java 文件，展示其包含的 insert、deleteById、deleteByMap、deleteByQueryWrapper 等方法。
画面 10: IntelliJ IDEA 中显示创建新类 UserMapperTest 的弹窗。
画面 11: IntelliJ IDEA 中显示 UserMapper 接口的代码，准备编写测试类。
画面 12: IntelliJ IDEA 中显示 UserMapperTest.java 文件，编写测试类并导入相关依赖。
画面 13: IntelliJ IDEA 中显示 UserMapperTest.java 文件，编写 @Test 方法 testSelect，执行后控制台输出查询结果。
画面 14: 课程 PDF 页面显示测试结果，输出了 5 条用户数据，并说明“可以看到，通过简单的代码编写即可实现数据的查询操作”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2 SQL:
```sql
CREATE TABLE user (
    id bigint(20) NOT NULL COMMENT '主键ID',
    name varchar(30) DEFAULT NULL COMMENT '姓名',
    age int(11) DEFAULT NULL COMMENT '年龄',
    email varchar(50) DEFAULT NULL COMMENT '邮箱',
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

画面 3 XML:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.0.RELEASE</version>
    </parent>
    <groupId>cn.itcast.mybatisplus</groupId>
    <artifactId>itcast-mybatis-plus</artifactId>
    <version>1.0-SNAPSHOT</version>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        <!--mybatis-plus的springboot支持-->
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-boot-starter</artifactId>
            <version>3.0.5</version>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>5.1.47</version>
        </dependency>
    </dependencies>
</project>
```

画面 4 XML:
```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
    </plugins>
</build>
```

画面 6 application.properties:
```properties
spring.application.name = itcast-mybatis-plus
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://172.16.55.185:3306/haoke?useUnicode=true&characterEncoding=utf8&allowMultiQueries=true&autoReconnect=true
spring.datasource.username=root
spring.datasource.password=root
```

画面 6 User.java:
```java
package cn.itcast.mybatplus.pojo;

public class User {
    private Long id;
    private String name;
    private Integer age;
    private String email;
}
```

画面 8 UserMapper.java:
```java
package cn.itcast.mybatisplus.mapper;

import cn.itcast.mybatisplus.pojo.User;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
public interface UserMapper extends BaseMapper<User> {
}
```

画面 12 UserMapperTest.java:
```java
import cn.itcast.mybatisplus.pojo.User;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
import java.util.List;
import java.util.Map;
```

画面 13 UserMapperTest.java:
```java
@KunWith(SpringRunner.class)
@SpringBootTest
public class UserMapperTest {
    @Autowired
    private UserMapper userMapper;

    @Test
    public void testSelect() {
        List<User> users = this.userMapper.selectList(null);
        for (User user : users) {
            System.out.println(user);
        }
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 3: PPT 标题为“2.4.3、编写 application.properties 文件”。
画面 6: PPT 标题为“2.4.3、编写 application.properties 文件”和“2.4.4、创建 User 对象”。
画面 8: PPT 标题为“2.4.5、编写 UserMapper”和“2.4.6、编写 SpringBoot 启动类”。
画面 14: PPT 标题为“2.5、BaseMapper”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
