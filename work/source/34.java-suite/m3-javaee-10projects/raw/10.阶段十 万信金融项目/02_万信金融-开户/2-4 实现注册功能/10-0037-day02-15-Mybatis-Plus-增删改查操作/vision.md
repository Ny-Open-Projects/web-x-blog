# 画面线理解：day02-15-Mybatis-Plus-增删改查操作

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day02-15-Mybatis-Plus-增删改查操作_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:32, 01:49, 03:21, 04:24, 05:25, 06:14, 07:26, 08:38, 09:34, 10:58, 12:17, 13:06, 14:02, 15:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:23:44

1) 这一组画面整体在讲什么（一句话）：
演示 MyBatis-Plus 在 Spring Boot 项目中如何实现用户数据的增删改查操作，重点讲解了 BaseMapper 接口、实体类注解、以及测试方法的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示了 IDE 中的项目结构，包含 `src/main/java` 下的 `TestMybatisSpringBoot`、`UserMapper`、`BaseMapper.class`、`TestUserMapper.java` 等文件。
- 右侧编辑器显示 `BaseMapper.class` 的反编译代码，其中包含 `insert(T entity)`、`deleteById(Serializable id)`、`updateById(T entity)` 等方法。

画面 2：
- 显示 `TestUserMapper.java` 文件，其中包含 `@Autowired` 注解的 `UserMapper` 字段和 `@SpringBootTest` 注解的测试类。
- 代码中定义了 `public UserMapper userMapper;` 和 `@Test public void testInsert() { ... }` 方法。

画面 3：
- 显示 PPT 页面，标题为“3.1.1 insert方法”，内容包括 `User user = new User();`、`user.setEmail("123@itcast.cn");`、`user.setAge(30);` 等设置用户属性的代码。
- 代码中包含 `int result = userMapper.insert(user);` 和 `System.out.println(result);` 用于插入数据并打印影响行数。

画面 4：
- 显示测试结果，输出为 `None`，并列出 `Unconditional classes`，包括 `org.springframework.boot.autoconfigure.context.ConfigurationPropertiesAutoConfiguration` 和 `org.springframework.boot.autoconfigure.context.PropertyPlaceholderAutoConfiguration`。

画面 5：
- 显示测试结果，输出为 `None`，并列出 `Unconditional classes`，包括 `org.springframework.boot.autoconfigure.context.ConfigurationPropertiesAutoConfiguration` 和 `org.springframework.boot.autoconfigure.context.PropertyPlaceholderAutoConfiguration`。
- 同时显示了 `TestUserMapper.testInsert()` 方法的测试日志，包括 `Preparing: INSERT` 和 `Updates: 1`。

画面 6：
- 显示 PPT 页面，标题为“3.1.1 insert方法”，内容包括 `User user = new User();`、`user.setEmail("123@itcast.cn");`、`user.setAge(30);` 等设置用户属性的代码。
- 代码中包含 `int result = userMapper.insert(user);` 和 `System.out.println(result);` 用于插入数据并打印影响行数。

画面 7：
- 显示 PPT 页面，标题为“3.1.1 insert方法”，内容包括 `User user = new User();`、`user.setEmail("123@itcast.cn");`、`user.setAge(30);` 等设置用户属性的代码。
- 代码中包含 `int result = userMapper.insert(user);` 和 `System.out.println(result);` 用于插入数据并打印影响行数。

画面 8：
- 显示 `User` 类的 `@TableId` 注解，其中 `keyType = IdType.AUTO`，表示主键自增。
- 同时显示了 `@TableField` 注解用于映射字段。

画面 9：
- 显示 `User` 类的 `@TableId` 注解，其中 `keyType = IdType.AUTO`，表示主键自增。
- 同时显示了 `@TableField` 注解用于映射字段。

画面 10：
- 显示数据库管理工具中的 `tb_user` 表，包含 `id`、`user_name`、`password`、`name`、`age`、`email` 等字段。
- 表中数据包括 `id=1`、`user_name="zhangsan"`、`password="123456"`、`name="张三"`、`age=18`、`email="test1@itcast.cn"` 等记录。

画面 11：
- 显示 `TestUserMapper.testUpdateById()` 方法，其中包含 `user.setId(1L);`、`user.setAge(21);`、`int result = userMapper.updateById(user);` 和 `System.out.println(result);`。
- 同时显示了测试日志，包括 `Preparing: UPDATE` 和 `Updates: 1`。

画面 12：
- 显示 `TestUserMapper.testUpdateById()` 方法，其中包含 `user.setId(1L);`、`user.setAge(21);`、`int result = userMapper.updateById(user);` 和 `System.out.println(result);`。
- 同时显示了测试日志，包括 `Preparing: UPDATE` 和 `Updates: 1`。

画面 13：
- 显示 `TestUserMapper.testDeleteById()` 方法，其中包含 `userMapper.deleteById(id);`。
- 同时显示了测试日志，包括 `Preparing: DELETE` 和 `Updates: 1`。

画面 14：
- 显示 `User` 类的 `@TableId` 注解，其中 `keyType = IdType.AUTO`，表示主键自增。
- 同时显示了 `@TableField` 注解用于映射字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

public class TestUserMapper {
    @Autowired
    private UserMapper userMapper;
    @Test
    public void testInsert() {
        User user = new User();
        user.setEmail("123@itcast.cn");
        user.setAge(30);
        user.setUserName("张三");
        user.setPassword("123456");
        int result = userMapper.insert(user);
        System.out.println(result);
    }
}
```

画面 2：
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

public class TestUserMapper {
    @Autowired
    private UserMapper userMapper;
    @Test
    public void testInsert() {
        User user = new User();
        user.setEmail("123@itcast.cn");
        user.setAge(30);
        user.setUserName("张三");
        user.setPassword("123456");
        int result = userMapper.insert(user);
        System.out.println(result);
    }
}
```

画面 3：
```java
User user = new User();
user.setEmail("123@itcast.cn");
user.setAge(30);
user.setUserName("张三");
user.setPassword("123456");
int result = userMapper.insert(user);
System.out.println(result);
```

画面 4：
```java
None

Unconditional classes:
org.springframework.boot.autoconfigure.context.ConfigurationPropertiesAutoConfiguration
org.springframework.boot.autoconfigure.context.PropertyPlaceholderAutoConfiguration
```

画面 5：
```java
@Test
public void testInsert() {
    User user = new User();
    user.setEmail("123@itcast.cn");
    user.setAge(30);
    user.setUserName("张三");
    user.setPassword("123456");
    int result = userMapper.insert(user);
    System.out.println(result);
}
```

画面 6：
```java
User user = new User();
user.setEmail("123@itcast.cn");
user.setAge(30);
user.setUserName("张三");
user.setPassword("123456");
int result = userMapper.insert(user);
System.out.println(result);
```

画面 7：
```java
User user = new User();
user.setEmail("123@itcast.cn");
user.setAge(30);
user.setUserName("张三");
user.setPassword("123456");
int result = userMapper.insert(user);
System.out.println(result);
```

画面 8：
```java
@TableId(type = IdType.AUTO)
private Long id;
@TableField("user_name")
private String userName;
@TableField("PASSWORD")
private String password;
```

画面 9：
```java
@TableId(type = IdType.AUTO)
private Long id;
@TableField("user_name")
private String userName;
@TableField("PASSWORD")
private String password;
```

画面 10：
```sql
CREATE TABLE tb_user (
    id BIGINT(20) NOT NULL AUTO_INCREMENT COMMENT '用户ID',
    user_name VARCHAR(30) DEFAULT NULL COMMENT '用户名',
    password VARCHAR(30) DEFAULT NULL COMMENT '密码',
    name VARCHAR(30) DEFAULT NULL COMMENT '姓名',
    age INT(11) DEFAULT NULL COMMENT '年龄',
    email VARCHAR(50) DEFAULT NULL COMMENT '邮箱',
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

画面 11：
```java
User user = new User();
user.setId(1L);
user.setAge(21);
int result = userMapper.updateById(user);
System.out.println(result);
```

画面 12：
```java
User user = new User();
user.setId(1L);
user.setAge(21);
int result = userMapper.updateById(user);
System.out.println(result);
```

画面 13：
```
