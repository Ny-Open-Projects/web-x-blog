# 画面线理解：11.Mybatis-Plus-条件构造器-基本比较器

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\11.Mybatis-Plus-条件构造器-基本比较器【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:47, 01:13, 01:52, 02:41, 03:48, 04:22, 05:17, 06:05, 06:44, 07:54, 09:32, 09:55, 10:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:41:02

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 MyBatis-Plus 的 QueryWrapper 和 LambdaQueryWrapper 进行条件查询，包括基本比较操作和 Lambda 方式构造条件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了 UserMapperTest.java 中的 testSelectPage 方法，使用 QueryWrapper 进行分页查询。
- 代码：`int pageindex = 2; //当前页码 int size = 8; //每页记录数 Page<User> page = new Page<>(pageindex, size); IPage<User> userPage = userMapper.selectPage(page, queryWrapper); long pages = userPage.getPages(); long total = userPage.getTotal(); //记录列表 List<User> records = userPage.getRecords(); System.out.println(records);`

画面2：
- 展示了 MyBatis-Plus 的 QueryWrapper 类的继承结构，突出 LambdaQueryWrapper。
- 代码：`public abstract class Wrapper<T> implements ISqlSegment`

画面3：
- 展示了 PPT 页面，标题为“5.1 基本比较操作”，列出了 eq、ne、gt、ge、lt、le、between、notBetween 等操作。

画面4：
- 展示了 UserMapperTest.java 中的 testEq 方法，使用 LambdaQueryWrapper 构造条件查询。
- 代码：`@Test public void testEq() { QueryWrapper<User> wrapper = new QueryWrapper<>(); //SELECT id,user_name,password,name,age, FROM tb_user WHERE password = ? AND age >= ? AND name IN (?,?) wrapper.eq("password", "123456") .ge("age", 20) .in("name", "李四", "王五", "赵六"); List<User> users = this.userMapper.selectList(wrapper); for (User user : users) { System.out.println(user); } }`

画面5：
- 展示了 PPT 页面，标题为“5.1 基本比较操作”，列出了 eq、ne、gt、ge、lt、le、between、notBetween 等操作。

画面6：
- 展示了 UserMapperTest.java 中的 testEq 方法，使用 QueryWrapper 构造条件查询。
- 代码：`public void testEq() { QueryWrapper<User> queryWrapper = new QueryWrapper<>(); queryWrapper.eq("name", "李四"); //等于 queryWrapper.gt("age", 20); //大于 queryWrapper.in("user_name", "coco"); List<User> users = userMapper.selectList(queryWrapper); System.out.println(users); }`

画面7：
- 展示了测试结果，显示 testEq 方法执行成功。
- 控制台输出：`Tests passed: 1 of 1 test`

画面8：
- 展示了 UserMapperTest.java 中的 testEq2 方法，使用 LambdaQueryWrapper 构造条件查询。
- 代码：`@Test public void testEq2() { LambdaQueryWrapper<User> queryWrapper = new LambdaQueryWrapper<>(); queryWrapper.eq(User::getUserName, "李四"); //等于 queryWrapper.gt(User::getAge, 20); //大于 }`

画面9：
- 展示了测试结果，显示 testEq2 方法执行成功。
- 控制台输出：`Tests passed: 1 of 1 test`

画面10：
- 展示了 UserMapperTest.java 中的 testEq3 方法，使用 LambdaQueryWrapper 构造条件查询。
- 代码：`@Test public void testEq3() { LambdaQueryWrapper<User> queryWrapper = new LambdaQueryWrapper<>(); queryWrapper.eq(User::getUserName, "李四"); //等于 queryWrapper.gt(User::getAge, 20); //大于 }`

画面11：
- 展示了测试结果，显示 testEq3 方法执行成功。
- 控制台输出：`Tests passed: 1 of 1 test`

画面12：
- 展示了 UserMapperTest.java 中的 testEq5 方法，使用 LambdaQueryWrapper 构造条件查询。
- 代码：`@Test public void testEq5() { LambdaQueryWrapper<User> queryWrapper = new LambdaQueryWrapper<>(); String name = "李四"; Integer age = 20; queryWrapper.eq(name != null && name.equals("李四"), User::getUserName, name); queryWrapper.gt(age != null, User::getAge, age); }`

画面13：
- 展示了测试结果，显示 testEq5 方法执行成功。
- 控制台输出：`Tests passed: 1 of 1 test`

画面14：
- 展示了 PPT 页面，标题为“5.1 基本比较操作”，列出了 eq、ne、gt、ge、lt、le、between、notBetween 等操作。
- 文本：在MP查询中，还可以使用lambda方式查询，降低数据库列表写错的风险。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1：
```java
//用向后方法设置查询条件，每页记录数
int pageindex = 2; //当前页码
int size = 8; //每页记录数
Page<User> page = new Page<>(pageindex, size);
IPage<User> userPage = userMapper.selectPage(page, queryWrapper);
long pages = userPage.getPages();
long total = userPage.getTotal(); //记录总数
//记录列表
List<User> records = userPage.getRecords();
System.out.println(records);
```

画面2：
```java
public abstract class Wrapper<T> implements ISqlSegment
```

画面4：
```java
@Test
public void testEq() {
    QueryWrapper<User> wrapper = new QueryWrapper<>();
    //SELECT id,user_name,password,name,age, FROM tb_user WHERE password = ? AND age >= ? AND name IN (?,?)
    wrapper.eq("password", "123456")
        .ge("age", 20)
        .in("name", "李四", "王五", "赵六");
    List<User> users = this.userMapper.selectList(wrapper);
    for (User user : users) {
        System.out.println(user);
    }
}
```

画面6：
```java
public void testEq() {
    QueryWrapper<User> queryWrapper = new QueryWrapper<>();
    queryWrapper.eq("name", "李四"); //等于
    queryWrapper.gt("age", 20); //大于
    queryWrapper.in("user_name", "coco");
    List<User> users = userMapper.selectList(queryWrapper);
    System.out.println(users);
}
```

画面8：
```java
@Test
public void testEq2() {
    LambdaQueryWrapper<User> queryWrapper = new LambdaQueryWrapper<>();
    queryWrapper.eq(User::getUserName, "李四"); //等于
    queryWrapper.gt(User::getAge, 20); //大于
}
```

画面10：
```java
@Test
public void testEq3() {
    LambdaQueryWrapper<User> queryWrapper = new LambdaQueryWrapper<>();
    queryWrapper.eq(User::getUserName, "李四"); //等于
    queryWrapper.gt(User::getAge, 20); //大于
}
```

画面12：
```java
@Test
public void testEq5() {
    LambdaQueryWrapper<User> queryWrapper = new LambdaQueryWrapper<>();
    String name = "李四";
    Integer age = 20;
    queryWrapper.eq(name != null && name.equals("李四"), User::getUserName, name);
    queryWrapper.gt(age != null, User::getAge, age);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：
- 标题：5.1 基本比较操作
- 内容：
  - eq
    - 等于 =
  - ne
    - 不等于 <>
  - gt
    - 大于 >
  - ge
    - 大于等于 >=
  - lt
    - 小于 <
  - le
    - 小于等于 <=
  - between
    - BETWEEN 值1 AND 值2
  - notBetween

画面14：
- 标题：5.1 基本比较操作
- 内容：
  - eq
    - 等于 =
  - ne
    - 不等于 <>
  - gt
    - 大于 >
  - ge
    - 大于等于 >=
  - lt
    - 小于 <
  - le
    - 小于等于 <=
  - between
    - BETWEEN 值1 AND 值2
  - notBetween
- 文本：在MP查询中，还可以使用lambda方式查询，降低数据库列表写错的风险。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
