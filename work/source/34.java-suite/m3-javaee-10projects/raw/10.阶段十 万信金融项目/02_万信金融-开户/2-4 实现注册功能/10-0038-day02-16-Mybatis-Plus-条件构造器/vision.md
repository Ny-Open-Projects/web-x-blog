# 画面线理解：day02-16-Mybatis-Plus-条件构造器

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day02-16-Mybatis-Plus-条件构造器_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:21, 04:43, 05:34, 07:01, 08:04, 09:24, 09:54, 10:52, 12:09, 12:46, 13:47, 14:50, 15:33, 16:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:24:23

1) 这一组画面整体在讲 MyBatis-Plus 条件构造器的使用，包括比较操作、模糊查询、排序和组合条件等。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程目录结构，当前章节为“4 条件构造器”，内容涉及开户、注册、登录等业务逻辑。
画面2：PPT页面标题为“4.1 比较操作”，列出比较操作符：eq（等于）、ne（不等于）、gt（大于）、ge（大于等于）、lt（小于）。
画面3：展示多个开发环境窗口，包括 IntelliJ IDEA、SQLyog、configService、ApolloPortal、adminService，下方代码为使用 QueryWrapper 查询用户列表。
画面4：与画面3内容相同，展示多个开发环境窗口和代码。
画面5：IDEA 编辑器中展示 QueryWrapper 的 API 方法，如 eq、orderByAsc、orderByDesc 等，并演示了设置条件的代码。
画面6：PPT页面标题为“4.2 模糊查询”，展示模糊查询的代码示例。
画面7：IDEA 编辑器中展示测试类 TestUserMapper 的 testEq 方法，执行查询并打印结果。
画面8：IDEA 编辑器中展示测试类 TestUserMapper 的 testEq 方法，执行查询并打印结果。
画面9：IDEA 编辑器中展示测试类 TestUserMapper 的 testLike 方法，用于模糊查询。
画面10：IDEA 编辑器中展示测试类 TestUserMapper 的 testLike 方法，执行模糊查询并打印结果。
画面11：PPT页面展示测试用例的代码结构，包括 import 语句和测试类 UserMapperTest。
画面12：IDEA 编辑器中展示测试类 TestUserMapper 的 testOrderBy 方法，用于排序查询。
画面13：IDEA 编辑器中展示测试类 TestUserMapper 的 testOrderBy 方法，执行排序查询并打印结果。
画面14：PPT页面展示测试用例的代码结构，包括 import 语句和测试类 UserMapperTest。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
```java
eq(String column, Object val)
lambda()
orderByAsc(String column)
or(boolean condition, Function<QueryWrapper<User>, QueryWrapper<User>> func)
or(Function<QueryWrapper<User>, QueryWrapper<User>> func)
orderByDesc(String column, String... columns)
orderByAsc(boolean condition, String... columns)
orderByDesc(boolean condition, String... columns)
```
```java
queryWrapper.eq("column", "password", val: "123456").ge("column", "age", val: 20);
```
画面6：
```java
//SELECT id,user_name,password,name,age,email FROM tb_user WHERE
//password = ? AND age >= ? AND name IN (?,?)
wrapper.eq("password", "123456")
       .ge("age", 20)
       .in("name", "...values")
```
画面7：
```java
@Test
public void testEq() {
    QueryWrapper<User> wrapper = new QueryWrapper<>();
    //SELECT id,user_name,password,name,age,email FROM tb_user WHERE
    //password = ? AND age >= ? AND name IN (?,?)
    wrapper.eq("password", "123456")
           .ge("age", 20)
           .in("name", "...values");
    List<User> users = this.userMapper.selectList(wrapper);
    for (User user : users) {
        System.out.println(user);
    }
}
```
画面9：
```java
@Test
public void testLike() {
    QueryWrapper<User> queryWrapper = new QueryWrapper<>();
    queryWrapper.like("name", "李");
    userMapper.selectList(queryWrapper);
}
```
画面12：
```java
@Test
public void testOrderBy() {
    QueryWrapper<User> queryWrapper = new QueryWrapper<>();
    queryWrapper.orderByDesc("age");
}
```
画面14：
```java
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
import java.util.List;

@RunWith(SpringRunner.class)
@SpringBootTest
public class UserMapperTest {

    @Autowired
    private UserMapper userMapper;

    @Test
    public void testOr() {
        QueryWrapper<User> wrapper = new QueryWrapper<>();
        //SELECT id,user_name,password,name,age,email FROM tb_user WHERE
        //name = ? OR age = ? OR
        wrapper.eq("name", "李四").or().eq("age", 24);
        List<User> users = this.userMapper.selectList(wrapper);
        for (User user : users) {
            System.out.println(user);
        }
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：PPT标题为“4.1 比较操作”，列出比较操作符：eq（等于）、ne（不等于）、gt（大于）、ge（大于等于）、lt（小于）。
画面6：PPT标题为“4.2 模糊查询”，展示模糊查询的代码示例。
画面11：PPT标题为“测试用例”，展示测试用例的代码结构。
画面14：PPT标题为“测试用例”，展示测试用例的代码结构。

5) 不要评价画面美观，不要输出与课程无关的内容。
