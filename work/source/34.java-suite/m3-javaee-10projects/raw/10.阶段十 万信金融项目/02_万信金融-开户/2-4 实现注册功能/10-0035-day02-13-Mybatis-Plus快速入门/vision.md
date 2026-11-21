# 画面线理解：day02-13-Mybatis-Plus快速入门

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day02-13-Mybatis-Plus快速入门_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:37, 01:48, 02:49, 03:54, 05:41, 06:52, 08:46, 09:55, 10:55, 11:38, 13:02, 14:23, 15:07, 16:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:21:53

1) 这一组画面整体在讲如何使用 MyBatis-Plus 框架在 Spring Boot 项目中配置数据库连接、定义实体类、编写 Mapper 接口及对应的 XML 映射文件。

2) 按时间顺序列出每张画面的要点：
画面 1: 创建名为 "mp" 的数据库，字符集为 "utf8 -- UTF-8 Unicode"。
画面 2: Maven 项目导入依赖，显示 "ArtifactId: icast-mp-springboot"，版本 "1.0-SNAPSHOT"。
画面 3: 展示 `pom.xml` 文件内容，包含 Spring Boot、MyBatis-Plus、MySQL 等依赖配置。
画面 4: 展示 `application.properties` 文件内容，配置了 Spring Boot 应用名、数据库驱动、连接 URL、用户名和密码。
画面 5: 展示 `application.properties` 文件内容，包含数据库配置和 MyBatis-Plus 的配置项，如 `mybatis-plus.type-aliases-package`。
画面 6: 展示 PPT 页面，标题为 "2.2.5 编写 mapper 接口和配置文件"，并显示了 `User` 类的注解说明。
画面 7: 在 IDEA 中新建 `User.java` 文件，准备编写实体类。
画面 8: 在 `User.java` 中导入 `lombok.Data` 注解。
画面 9: 在 `User.java` 中添加 `@TableId` 注解，指定主键字段。
画面 10: 在 `User.java` 中为其他字段添加 `@TableField` 注解，指定数据库列名。
画面 11: 在 IDEA 中新建 `UserMapper.java` 文件，准备编写 Mapper 接口。
画面 12: 展示 PPT 页面，标题为 "2.2.6 修改启动类"，并显示了 `MyApplication` 类的导入语句。
画面 13: 展示 `mybatis-config.xml` 文件内容，包含 MyBatis 的配置信息。
画面 14: 展示 `User.java` 文件内容，已添加 `@TableId` 和 `@TableField` 注解。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <scope>test</scope>
</dependency>
<!-- 自定义代码的工具包 -->
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
</dependency>
<dependency>
    <groupId>com.baidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>1.1.0</version>
</dependency>
```

画面 4:
```properties
spring.application.name=icast-mp-springboot
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/mp?useUnicode=true&characterEncoding=utf8&autoReconnect=true&allowMultiQueries=true
spring.datasource.username=root
spring.datasource.password=123
```

画面 5:
```properties
spring.application.name=icast-mp-springboot
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/mp?useUnicode=true&characterEncoding=utf8&autoReconnect=true&allowMultiQueries=true
spring.datasource.username=root
spring.datasource.password=123
# 设置Mapper接口所对应的XML文件位置，如果放在Mapper接口中自定义方法，需要进行动态配置
mybatis-plus.mapper-locations=classpath:mybatis/*.xml
# 设置每个包扫描路径，通过注解属性可以给包中的类注解别名
mybatis-plus.type-aliases-package=cn.itcast.mp.pojo
```

画面 6:
```java
@TableId("ID")
private Long id;
private String userName; // 姓名字段，但无需注解
private String password;
private String name;
private Integer age;
private String email;
```

画面 7:
```java
package cn.itcast.mp.pojo;
```

画面 8:
```java
import lombok.Data;
```

画面 9:
```java
@TableId
private Long id;
```

画面 10:
```java
@TableId("id")
private Long id;
@TableField("user_name")
private String userName;
@TableField("PASSWORD")
private String password;
@TableField("NAME")
private String name;
@TableField("AGE")
private Integer age;
private String email;
```

画面 11:
```java
package cn.itcast.mp.mapper;
import com.baidou.mybatisplus.core.mapper.BaseMapper;
public interface UserMapper extends BaseMapper<User> {
}
```

画面 12:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="cn.itcast.mp.mapper.UserMapper">
</mapper>
```

画面 13:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="cn.itcast.mp.mapper.UserMapper">
</mapper>
```

画面 14:
```java
@TableId("id")
private Long id;
@TableField("user_name")
private String userName;
@TableField("PASSWORD")
private String password;
@TableField("NAME")
private String name;
@TableField("AGE")
private Integer age;
private String email;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 5: PPT 标题为 "2.2.4 编pojo"，内容包含 MyBatis-Plus 的配置说明。
画面 6: PPT 标题为 "2.2.5 编写 mapper 接口和配置文件"，内容包含 `User` 类的注解说明。
画面 12: PPT 标题为 "2.2.6 修改启动类"，内容包含 `MyApplication` 类的导入语句。

5) 不要评价画面美观，不要输出与课程无关的内容。
