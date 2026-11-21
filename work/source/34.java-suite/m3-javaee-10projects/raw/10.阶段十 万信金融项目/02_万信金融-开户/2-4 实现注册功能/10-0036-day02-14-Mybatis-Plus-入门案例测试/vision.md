# 画面线理解：day02-14-Mybatis-Plus-入门案例测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day02-14-Mybatis-Plus-入门案例测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:19, 01:00, 01:43, 02:29, 02:52, 03:22, 03:30, 03:37, 03:50, 03:58, 04:04, 04:19, 04:49, 05:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:22:47

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 MyBatis 框架，通过编写测试类来验证 UserMapper 的 selectById 方法能否成功查询数据库并返回用户数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 User.java 实体类，其中包含 @TableId 和 @TableField 注解，用于映射数据库表 tb_user 的字段。
画面2：展示 TestMybatisSpringBoot.java 测试类，其中定义了 @Autowired 注解的 UserMapper 字段。
画面3：在 TestMybatisSpringBoot.java 中，测试方法 testSelect() 内部调用 userMapper.selectById(2)。
画面4：展示 UserMapper.java 接口，它继承自 BaseMapper<User>，用于定义 MyBatis 的 Mapper 接口。
画面5：在 TestMybatisSpringBoot.java 中，测试方法 testSelect() 内部调用 userMapper.selectById(2) 并打印结果。
画面6：运行测试，控制台显示测试通过，日志中包含 HikariCP 连接池和 MyBatis 的初始化信息。
画面7：测试通过后，控制台显示 MyBatis 的自动配置信息，包括 MyBatisConfiguration 和 PersistenceExceptionTranslationAutoConfiguration。
画面8：测试通过后，控制台显示 MyBatis 的自动配置信息，包括 MyBatisConfiguration 和 JdbcOperations。
画面9：测试通过后，控制台显示 MyBatis 的自动配置信息，包括 MyBatisAutoConfiguration 和 SqlSessionFactory。
画面10：测试通过后，控制台显示 MyBatis 的自动配置信息，包括 MyBatisAutoConfiguration 和 JdbcRepository。
画面11：测试通过后，控制台显示 MyBatis 的自动配置信息，包括 MyBatisAutoConfiguration 和 SqlSessionFactory。
画面12：测试通过后，控制台显示 MyBatis 的自动配置信息，包括 MyBatisAutoConfiguration 和 SqlSessionFactory。
画面13：测试通过后，控制台显示 MyBatis 的自动配置信息，包括 MyBatisAutoConfiguration 和 SqlSessionFactory。
画面14：测试通过后，控制台显示 MyBatis 的自动配置信息，包括 MyBatisAutoConfiguration 和 SqlSessionFactory。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.stereotype.Repository;

@TableId("id")
private long id;

@TableField("user_name")
private String userName;

@TableField("PASSWORD")
private String password;

@TableField("NAME")
private String name;

@TableField("AGE")
private String age;
```

画面2：
```java
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@SpringBootTest
@RunWith(SpringRunner.class)
public class TestMybatisSpringBoot {

    @Autowired
    private UserMapper userMapper;

    @Test
    public void testSelect() {
    }
}
```

画面3：
```java
@Test
public void testSelect() {
    userMapper.selectById(2);
}
```

画面4：
```java
package cn.itcast.mp.mapper;

import cn.itcast.mp.pojo.User;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;

public interface UserMapper extends BaseMapper<User> {
}
```

画面5：
```java
@Test
public void testSelect() {
    User user = userMapper.selectById(2);
    System.out.println(user);
}
```

画面6：
```
Tests passed: 1 of 1 - 601 ms
main [org.springframework.test.context.cache.-DEBUG] Spring test ApplicationContext cache statistics: DefaultContextCache[10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
