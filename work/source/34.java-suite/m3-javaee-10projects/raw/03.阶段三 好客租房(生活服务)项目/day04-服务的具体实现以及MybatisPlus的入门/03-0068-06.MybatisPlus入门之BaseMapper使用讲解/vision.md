# 画面线理解：06.MybatisPlus入门之BaseMapper使用讲解

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\06.MybatisPlus入门之BaseMapper使用讲解【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 01:49, 03:03, 04:43, 06:23, 07:33, 08:29, 10:16, 11:32, 12:31, 13:44, 15:20, 17:28, 18:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:42:10

1) 这一组画面整体在讲 MyBatis-Plus 中 BaseMapper 的 CRUD 操作及分页查询功能。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 MyBatis-Plus 文档中关于 BaseMapper 的介绍，说明继承 BaseMapper 后可获得 CRUD 方法，并强调这些方法仅适合单表操作。
画面2: 在 IntelliJ IDEA 中，展示了测试类 UserMapperTest 中的 testSelect() 方法，调用 userMapper.selectList(null) 查询所有用户数据。
画面3: 在 IntelliJ IDEA 中，展示了 testSelectById() 方法的编写过程，其中使用了 this.userMapper.selectById(3L) 查询 ID 为 3 的用户。
画面4: 在 IntelliJ IDEA 中，展示了 testSelectByLike() 方法的编写过程，其中使用了 QueryWrapper 进行模糊查询。
画面5: 在 IntelliJ IDEA 中，展示了 testSelectByLike() 方法的完整代码，其中使用了 QueryWrapper 的 like 方法进行模糊查询，并打印了查询结果。
画面6: 展示了 MyBatis-Plus 官网文档中 AbstractWrapper 的介绍，说明 QueryWrapper 和 UpdateWrapper 用于生成 SQL 的 where 条件。
画面7: 在 IntelliJ IDEA 中，展示了 testSelectByLike() 方法的完整代码，其中使用了 QueryWrapper 的 like 方法进行模糊查询，并打印了查询结果。
画面8: 在 Navicat Premium 中，展示了数据库表 user 的结构，包含 id、name、age、email 字段。
画面9: 在 Navicat Premium 中，展示了数据库表 user 的结构，包含 id、name、age、email 字段。
画面10: 在 IntelliJ IDEA 中，展示了 testSave() 方法的代码，其中创建了一个 User 对象并调用 userMapper.insert(user) 插入数据。
画面11: 在 IntelliJ IDEA 中，展示了 testDelete() 和 testUpdate() 方法的代码，其中 testDelete() 调用 userMapper.deleteById(1L) 删除数据，testUpdate() 调用 userMapper.updateById(user) 更新数据。
画面12: 在 IntelliJ IDEA 中，展示了 testSelectPage() 方法的代码，其中创建了一个 Page 对象并调用 userMapper.selectPage(page, null) 查询分页数据。
画面13: 在 IntelliJ IDEA 中，展示了 testSelectPage() 方法的完整代码，其中使用了 Page 对象进行分页查询，并打印了总条数、当前页数和每页显示条数。
画面14: 展示了 MyBatis-Plus 文档中关于 BaseMapper 的介绍，说明继承 BaseMapper 后可获得 CRUD 方法，并强调这些方法仅适合单表操作。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```java
/**
 * Mapper 继承该接口后，无需编写 mapper.xml 文件，即可获得CRUD功能
 * 这个 Mapper 支持 id 这些
 */
@Author hubin
@Since 2016-01-23
public interface BaseMapper<T> {
```

画面2:
```java
public void testSelect() {
    List<User> users = this.userMapper.selectList(queryWrapper: null);
    for (User user : users) {
        System.out.println(user);
    }
}
@Test
public void testSelectById() {
    this.userMapper.selectById(3L);
}
```

画面3:
```java
@Test
public void testSelectById() {
    User user = this.userMapper.selectById(3L);
    System.out.println(user);
}
@Test
public void testSelectByLike() {
    this.
```

画面4:
```java
@Test
public void testSelectByLike() {
    QueryWrapper<User> wrapper = new QueryWrapper<User>();
    ((QueryWrapper) wrapper).like("name", "a");
    this.userMapper.selectList(wrapper);
}
```

画面5:
```java
@Test
public void testSelectByLike() {
    QueryWrapper<User> wrapper = new QueryWrapper<User>();
    wrapper.like("name", "a");
    List<User> list = this.userMapper.selectList(wrapper);
    for (User user : list) {
        System.out.println(user);
    }
}
```

画面6:
```java
/**
 * allEq
 * QueryWrapper(LambdaQueryWrapper) 和 UpdateWrapper(LambdaUpdateWrapper) 的类
 * 用于生成 sql 的 where 条件，entity 属性用于生成 sql 的 where 条件
 * 
 * 全部参数说明：
 * params: key 为实体类字段名 value 为字段值
 * nullEq: 为 true 则在 map 的 value 为 null 时调用 isNull 方法（为 false 时则忽略）
 * value 为 null 的
 * 
 * 例：allEq({id=1, name='王工'}) -> id = 1 and name = '王工'
 * 
 * allEq(Map, V, boolean nullEq, boolean nullEq)
 * allEq(boolean condition, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
 * 
 * allEq(Map, V, filter, Map, V, params, boolean nullEq)
 * allEq(boolean condition, Map, V, filter, Map, V, params, boolean nullEq)
