# 画面线理解：09.Mybatis-Plus-通用CRUD-删除操作

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\09.Mybatis-Plus-通用CRUD-删除操作【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:26, 00:43, 01:24, 01:56, 02:11, 02:37, 02:58, 03:28, 03:52, 04:07, 04:32, 05:09, 05:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:39:40

1) 这一组画面整体在讲 MyBatis-Plus 框架中删除操作的实现，包括根据 ID 删除、条件删除和批量删除三种方式。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 MyBatis-Plus 文档中 4.3.1 deleteById 方法的定义和操作步骤，包含 Java 代码片段。
画面 2: 展示 MyBatis-Plus 课程目标和 1.1 MyBatis-Plus 介绍的 PPT 页面，列出课程学习内容。
画面 3: 展示 IDEA 编辑器中 UserMapperTest.java 文件的 update 方法测试代码，以及测试通过的控制台日志。
画面 4: 展示数据库管理工具中 user 表的数据，用于后续删除操作的测试数据。
画面 5: 展示 IDEA 编辑器中 UserMapperTest.java 文件的 delete 方法测试代码，以及测试通过的控制台日志。
画面 6: 展示 IDEA 编辑器中 UserMapperTest.java 文件的 delete 方法测试代码，其中设置了年龄为 111 的条件。
画面 7: 展示 IDEA 编辑器中 UserMapperTest.java 文件的 delete 方法测试代码，其中设置了年龄为 100 的条件。
画面 8: 展示 IDEA 编辑器中 UserMapperTest.java 文件的 delete 方法测试代码，其中设置了姓名为“曹操”的条件。
画面 9: 展示 IDEA 编辑器中 UserMapperTest.java 文件的 delete 方法测试代码，其中设置了姓名为“曹操”的条件。
画面 10: 展示 IDEA 编辑器中 UserMapperTest.java 文件的 delete 方法测试代码，以及测试通过的控制台日志，显示了 SQL 删除语句。
画面 11: 展示 IDEA 编辑器中 UserMapperTest.java 文件的 delete 方法测试代码，以及测试通过的控制台日志。
画面 12: 展示 IDEA 编辑器中 UserMapperTest.java 文件的 delete 方法测试代码，以及测试通过的控制台日志。
画面 13: 展示 IDEA 编辑器中 UserMapperTest.java 文件的 delete 方法测试代码，以及测试通过的控制台日志。
画面 14: 展示 MyBatis-Plus 文档中 4.3.3 deleteBatchIds 方法的定义和操作步骤，包含 Java 代码片段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
/**
 * 根据 ID 删除
 * @param id 主键ID
 */
int deleteById(Serializable id);
```

画面 6:
```java
@Test
public void testDelete(){
    //设置条件
    QueryWrapper<User> queryWrapper = new QueryWrapper<>();
    queryWrapper.eq("age", 111);
    //执行删除
    int delete = userMapper.delete(queryWrapper);
    System.out.println(delete);
}
```

画面 7:
```java
@Test
public void testDelete(){
    //设置条件
    QueryWrapper<User> queryWrapper = new QueryWrapper<>();
    queryWrapper.eq("age", 100);
    //执行删除
    int delete = userMapper.delete(queryWrapper);
    System.out.println(delete);
}
```

画面 8:
```java
@Test
public void testDelete(){
    //设置条件
    QueryWrapper<User> queryWrapper = new QueryWrapper<>();
    queryWrapper.eq("name", "曹操");
    //执行删除
    int delete = userMapper.delete(queryWrapper);
    System.out.println(delete);
}
```

画面 10:
```java
//设置条件
QueryWrapper<User> queryWrapper = new QueryWrapper<>();
queryWrapper.eq("age", 100);
//执行删除
int delete = userMapper.delete(queryWrapper);
System.out.println(delete);
```

画面 12:
```java
//设置条件
QueryWrapper<User> queryWrapper = new QueryWrapper<>();
queryWrapper.eq("name", "曹操");
//执行删除
int delete = userMapper.delete(queryWrapper);
System.out.println(delete);
```

画面 14:
```java
/**
 * 删除（根据ID 批量删除）
 * @param idList 主键ID列表(不能为 null 以及 empty)
 */
int deleteBatchIds(@Param(Constants.COLLECTION) Collection<? extends Serializable> idList);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: PPT 标题为“1 MyBatis-Plus介绍”，下方列出课程目标：
- 了解MyBatis-Plus
- 整合MyBatis-Plus
- 通用CRUD
- MyBatis-Plus的配置
- 条件构造器
- MyBatis-Plus 的Service封装
- 代码生成器

5) 不要评价画面美观，不要输出与课程无关的内容。
