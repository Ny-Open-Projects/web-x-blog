# 画面线理解：15-SpringBoot整合mybatis

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/1.SpringBoot 第一天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\1.SpringBoot 第一天\15-SpringBoot整合mybatis_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:20, 02:44, 03:47, 05:07, 06:51, 08:05, 09:27, 10:37, 11:32, 12:29, 13:20, 14:42, 16:28, 17:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 02:39:08

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成 MyBatis，包括添加依赖、配置数据源、创建实体类、编写 Mapper 接口和测试。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示项目结构，选中 springboot-mybatis 模块，准备开始集成 MyBatis。
画面 2: 在 pom.xml 中添加 MyBatis 和 MySQL 的依赖。
画面 3: 在 mybatis 目录下创建 user.sql 和 UserMapper.xml 文件。
画面 4: 创建 User 实体类，定义 id 和 name 字段。
画面 5: 编辑 application.yml，配置数据库连接信息。
画面 6: 创建 UserMapper.java 接口，使用 @Repository 注解。
画面 7: 在 application.yml 中添加 driver-class-name 配置。
画面 8: 编写 SpringBootTest 测试类，注入 UserMapper 并测试 findAll 方法。
画面 9: 运行测试，控制台显示测试通过。
画面 10: 测试通过后，查看控制台日志，确认 HikariCP 数据源初始化成功。
画面 11: 在项目中右键点击 UserMapper.java，选择“Generate”生成 getter、setter 等方法。
画面 12: 在 application.yml 中配置 MyBatis 的 type-aliases-package 和 mapper-locations。
画面 13: 在测试类中使用 @Autowired 注解注入 UserMapper。
画面 14: 在 application.yml 中配置 mybatis 的 config-location，指向 UserMapper.xml 文件。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 2:
```xml
<properties>
    <java.version>1.8</java.version>
</properties>

<dependencies>
    <dependency>
        <groupId>org.mybatis.spring.boot</groupId>
        <artifactId>mybatis-spring-boot-starter</artifactId>
        <version>2.1.1</version>
    </dependency>

    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <scope>runtime</scope>
    </dependency>

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>

<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
    </plugins>
</build>
```

画面 4:
```java
package com.ithema.springbootmybatis.domain;

public class User {
    private int id;
    private String name;
}
```

画面 5:
```yaml
spring:
  datasource:
    url: jdbc:mysql:///springboot
    username: root
    password:
```

画面 6:
```java
package com.ithema.springbootmybatis.mapper;

import org.springframework.stereotype.Repository;
import org.apache.ibatis.annotations.Mapper;

@Repository
public interface UserMapper {
    List<User> findAll();
}
```

画面 7:
```yaml
spring:
  datasource:
    url: jdbc:mysql:///springboot
    username: root
    password: root
    driver-class-name: com.mysql.cj.jdbc.Driver
```

画面 12:
```yaml
mybatis:
  type-aliases-package: com.ithema.springbootmybatis.domain
  mapper-locations: classpath:mapper/*.xml
  config-location: classpath:mybatis-config.xml
```

画面 14:
```yaml
mybatis:
  type-aliases-package: com.ithema.springbootmybatis.domain
  mapper-locations: classpath:mapper/*.xml
  config-location: classpath:mybatis-config.xml
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
（以上内容已按要求输出）
