# 画面线理解：06.Mybatis-Plus-通用CRUD-插入

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\06.Mybatis-Plus-通用CRUD-插入【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:17, 00:41, 01:06, 01:34, 01:48, 02:16, 03:19, 03:43, 03:55, 04:12, 04:22, 04:41, 05:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:37:59

1) 这一组画面整体在讲如何在 MyBatis-Plus 中使用 LocalDateTime 类型进行数据库插入操作，包括创建实体类、编写测试方法、使用 DateTimeFormatter 格式化日期字符串，并通过调试查看执行过程。

2) 按时间顺序列出每张画面的要点：
画面1：展示 User.java 实体类，包含 name、age、email、birthday 字段，其中 birthday 使用 @TableField 注解。
画面2：展示 BaseMapper 接口，其中包含 insert 方法。
画面3：在 UserMapperTest.java 中，编写 testInsert 方法，准备调用 userMapper.insert()。
画面4：在 testInsert 方法中，通过代码补全选择 set 方法，准备设置 User 对象属性。
画面5：选择 setAge 方法，准备设置用户年龄。
画面6：在代码中调用 LocalDateTime.parse() 方法，弹出方法参数提示。
画面7：查看 LocalDateTime.parse() 方法的 Javadoc 文档。
画面8：在 testInsert 方法中，使用 DateTimeFormatter.ofPattern() 设置日期格式，并调用 LocalDateTime.parse() 解析字符串。
画面9：在控制台查看 SQL 执行日志，确认插入语句已执行。
画面10：切换到数据库管理工具，查看数据库表结构和数据。
画面11：测试失败，控制台显示异常堆栈信息。
画面12：进入调试模式，查看变量值，发现 user 对象的 birthday 字段值为 null。
画面13：在调试模式下，将 user 对象的 birthday 字段设置为 LocalDateTime 对象。
画面14：展示 PPT 页面，标题为“4.1.1 方法定义”，内容为 MyBatis-Plus 的 CRUD 方法列表，当前高亮显示“insert”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
private String name;
@TableField("AGE")
private Integer age;
@TableField("EMAIL")
private String email;
@TableField("birthday")
private LocalDateTime birthday;
```

画面2：
```java
public interface BaseMapper<T> {
    int insert(T entity);
    int deleteById(Serializable id);
    int deleteByMap(@Param("ew") Wrapper<T> wrapper);
    int deleteBatchIds(@Param("coll") Collection<? extends Serializable> idList);
    int updateById(@Param("et") T entity, @Param("ew") Wrapper<T> updateWrapper);
    T selectById(Serializable id);
}
```

画面3：
```java
public void testInsert() {
    userMapper.insert();
}
```

画面4：
```java
user.setAge(20);
user.setName("caocao");
user.setEmail("caocao@163.com");
user.setPassword("123456");
user.setUserName("caocao");
user.setBirthday(LocalDateTime.now());
```

画面6：
```java
LocalDateTime.parse(CharSequence text, DateTimeFormatter formatter)
```

画面7：
```java
/**
 * Obtains an instance of {@code LocalDateTime} from a text string using a specific formatter.
 * The text is parsed using the formatter, returning a date-time.
 * @param text the text to parse, not null
 * @param formatter the formatter to use, not null
 * @return the parsed local date-time, not null
 * @throws DateTimeParseException if the text cannot be parsed
 */
public static LocalDateTime parse(CharSequence text, DateTimeFormatter formatter) {
    return formatter.parse(text, LocalDateTime::from);
}
```

画面8：
```java
DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofPattern("yyyy-MM-DD HH:mm:ss");
LocalDateTime localDateTime = LocalDateTime.parse(text, dateTimeFormatter);
user.setBirthday(localDateTime);
```

画面11：
```java
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context.junit4.statements.RunnerTestExecutionCallbacks.evaluate(RunnerTestExecutionCallbacks.java:81)
at org.springframework.test.context
