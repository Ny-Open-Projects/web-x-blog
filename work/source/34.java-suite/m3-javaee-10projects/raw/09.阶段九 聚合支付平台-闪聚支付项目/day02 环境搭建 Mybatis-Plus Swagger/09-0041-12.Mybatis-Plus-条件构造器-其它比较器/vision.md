# 画面线理解：12.Mybatis-Plus-条件构造器-其它比较器

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\12.Mybatis-Plus-条件构造器-其它比较器【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:36, 01:38, 02:00, 02:17, 02:37, 02:53, 03:08, 03:29, 03:59, 04:13, 04:59, 05:21, 05:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:41:36

1) 这一组画面整体在讲 MyBatis-Plus 中 QueryWrapper 和 LambdaQueryWrapper 的条件构造器用法，包括模糊查询、逻辑查询、字段选择和排序等功能。

2) 按时间顺序列出每张画面的要点：
画面1：展示文档中“5.2 模糊查询”章节，列出 like、notLike、likeLeft、likeRight 的用法及示例。
画面2：展示数据库表 tb_user 的结构，包含字段 id、user_name、password、age、email、birthday 及主键索引。
画面3：展示 Java 代码，使用 QueryWrapper 构造模糊查询条件，使用 .like("name", "王")。
画面4：展示 IDEA 中的测试类 UserMapperTest，代码中使用 QueryWrapper 构造模糊查询条件，但未执行。
画面5：展示 IDEA 中的测试类 UserMapperTest，代码中使用 QueryWrapper 构造模糊查询条件，使用 .likeRight("name", "王")。
画面6：展示 IDEA 中的测试类 UserMapperTest，代码中使用 QueryWrapper 构造模糊查询条件，使用 .likeRight("name", "王")，并执行成功。
画面7：展示文档中“5.3 逻辑查询”章节，列出 or、and 的用法及示例。
画面8：展示 Java 代码，使用 QueryWrapper 构造逻辑查询条件，使用 .eq("name", "李四").or().eq("age", 24)。
画面9：展示文档中“5.4 select”章节，说明在 MP 查询中默认查询所有字段，也可通过 select 方法指定字段。
画面10：展示 IDEA 中的测试类 UserMapperTest，代码中使用 QueryWrapper 构造模糊查询条件，使用 .select("id", "name")。
画面11：展示 Java 代码，使用 QueryWrapper 构造模糊查询条件，使用 .eq("name", "李四").or().eq("age", 24)。
画面12：展示文档中“5.5 排序”章节，列出 orderByDesc、orderByAsc、orderBy 的用法及示例。
画面13：展示 Java 代码，使用 LambdaQueryWrapper 构造条件，使用 .eq(User::getPassword, "123456").in(User::getName, "李四", "王五", "赵六")。
画面14：展示文档中“5.2 模糊查询”章节，列出 like 的用法及示例。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
@Autowired
private UserMapper userMapper;

@Test
void testWrapper() {
    QueryWrapper<User> wrapper = new QueryWrapper<>();
    //SELECT id,user_name,password,name,age,email FROM tb_user WHERE name LIKE ?
    //Parameters: %五( String)
    wrapper.like("name", "五");
    List<User> users = this.userMapper.selectList(wrapper);
    for (User user : users) {
        System.out.println(user);
    }
}
```

画面5：
```java
//SELECT id,user_name,password,name,age,email FROM tb_user WHERE name LIKE ?
//Parameters: %王( String)
wrapper.likeRight("name", "王");
```

画面6：
```java
//SELECT id,user_name,password,name,age,email FROM tb_user WHERE name LIKE ?
//Parameters: %王( String)
wrapper.likeRight("name", "王");
```

画面8：
```java
//SELECT id,user_name,password,name,age,email FROM tb_user WHERE name = ? OR age = ?
wrapper.eq("name", "李四")
    .or()
    .eq("age", 24)
    .select("id", "name", "age");
```

画面10：
```java
//SELECT id,user_name,password,name,age,email FROM tb_user WHERE name LIKE ?
//Parameters: %王( String)
wrapper.likeRight("name", "王");
```

画面11：
```java
//SELECT id,user_name,password,name,age,email FROM tb_user WHERE name = ? OR age = ?
wrapper.eq("name", "李四")
    .or()
    .eq("age", 24)
    .select("id", "name", "age");
```

画面13：
```java
LambdaQueryWrapper<User> wrapper = new LambdaQueryWrapper<>();
//SELECT id,user_name,password,name,age,email FROM tb_user WHERE password = ? AND age >= ? AND name IN (?, ?, ?)
wrapper.eq(User::getPassword, "123456")
    .ge(User::getAge, 20)
    .in(User::getName, "李四", "王五", "赵六");
List<User> users = this.userMapper.selectList(wrapper);
for (User user : users) {
    System.out.println(user);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：标题为“5.2 模糊查询”，内容包括 like、notLike、likeLeft、likeRight 的用法及示例。
画面7：标题为“5.3 逻辑查询”，内容包括 or、and 的用法及示例。
画面9：标题为“5.4 select”，内容说明在 MP 查询中默认查询所有字段，也可通过 select 方法指定字段。
画面12：标题为“5.5 排序”，内容包括 orderByDesc、orderByAsc、orderBy 的用法及示例。
画面14：标题为“5.2 模糊查询”，内容包括 like 的用法及示例。

5) 不要评价画面美观，不要输出与课程无关的内容。
