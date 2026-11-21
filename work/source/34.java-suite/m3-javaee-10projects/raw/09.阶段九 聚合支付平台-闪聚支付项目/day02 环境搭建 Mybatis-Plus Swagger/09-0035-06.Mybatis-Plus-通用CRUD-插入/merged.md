# 06.Mybatis-Plus-通用CRUD-插入

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\06.Mybatis-Plus-通用CRUD-插入【海量资源尽在 666java.com】.mp4
- 时长 5分5秒（音频 305s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来测试一下MyBitX Plus的通用CRUD什么是通用CRUD呢就是咱们之前说过我们现在定义Mapper呢都是继承了一个叫BaseMapper对吧它这里面呢是不是有很多的现成的方法有增三改差那下面呢我们就来测试一下这些常用的方法好那我们在测试类当中我们来先写一个插入吧好插入
[00:30] 那现在我们要测试的是不是就是insert对吧好那么insert它这个Mapper它有什么方法我们来看一下是不是有一个叫你看是不是有insertinsert这里边我们是不是需要去new一个user我们要new出一个user好new出一个user这里边我们就往里面放一些东西由于现在我们来看我们这个数据库它的这个字段其实它是自增的你看见吗
[01:00] 所以这个ID呢你就不用再去设了你只需要设什么呢比如说这里边有很多的字段比如说namename比如说曹操吧好然后呢还有这里边还有什么呀还有年龄比如说20曹操20岁了是吧然后还有这里边是不是还有很多的那这里边呢我们就随意设置几个吧设完了之后呢
[01:31] 我们是不是就可以把它放进去对吧这里边你看有内幕还有一个叫日期你看见吗日期类型这里边有有个特殊的你看local date time是吧local date time咱们这里边来看一下local date time我们是需要用这个pass这个方法我们可以给它传一个具体的这个日期曹操是90后1990对吧然后因为
[01:59] 我们现在这个日期啊你看它这个类型它是个你看它是年月日十分秒的是吧所以其实你这个船子自负串啊你也必须是年月日十分秒这种格式啊但是在这个pass这个方法里头你看它是不是有一个东西有一个存在方法是不是有一个叫做datetimeformatter这个也就是说呀你必须给它指定它以一种什么样的格式对吧
[02:27] 那么这个格式呢你需要你告诉他说是这种年月日十分秒的格式对吧十分秒这样就OK了大家理解这意思吗所以其实我们可以怎么做呀我们先要把这个东西创建出来一个东西然后呢这里边呢我们来看就需要这样来加一个逗号
[03:10] 那我们是不是就把这个可以给它造一个日期因为我们要插入数据我们要插入数据的话就得造一个数据造一个数据是不是就OK然后最后是不是把这个user放进去各位user放进去user放进去你看它是不是返回一个什么一个变量值一个变量值其实这个变量值返回的是什么是这个最终插入成功的一个什么记录数记录数好那现在呢各位我们来瞧瞧吧
[03:39] 这里边我们来运行一插入啊我们现在看一下这个这里边应该有六条记录了报错了啊报错了看一下报啥错啊password是不能你看因为它没有没有默认值吗但是它是不能为空的是吧所以你需要去设置一个password这可以吧好然后我们继续来测好运行一下其实就是我们要测试它的就这隐色的方法是吧
[04:19] 就这时候你看它是爱等于一也就是插入成功一条然后我们进入数据库刷新各位对吧那有时候老师你看好像不太对啊那个这个这个这个这个组件它是不是就自增了吗自增了但是它怎么成为这么一个组组件了是不是哎那这时候呢一会儿呢我们就要学习它的这个mybtsplus的组件策略啊那现在我们先说这个方法我们是不是就测通了
[04:48] 这个方法我们测试完了之后各位是不是就这个记录已经成功的插进去了是吧好那各位我们现在这个通用CUD的插入操作这个测试我们就测完了稍后我们学习它的组件生成策略好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

