# 画面线理解：08.Mybatis-Plus-通用CRUD-更新操作

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\08.Mybatis-Plus-通用CRUD-更新操作【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:47, 01:10, 02:04, 03:00, 04:00, 04:35, 05:15, 05:39, 06:08, 06:57, 07:40, 08:00, 08:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:39:09

1) 这一组画面整体在讲 MyBatis-Plus 中基于 ID 和条件的更新操作，包括方法定义、代码实现和注意事项。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 MyBatis-Plus 文档中“4.2 更新操作”章节，重点是“4.2.1 根据id更新”，并给出了方法定义：`int updateById(@Param(Constants.ENTITY) T entity);`。
画面 2: 展示了 `UserMapperTest` 测试类中 `testUpdate()` 方法的初始代码，用于插入一个用户对象。
画面 3: 在 `testUpdate()` 方法中，创建了一个新的 `User` 对象，并展示了 `User` 类的属性设置方法。
画面 4: 在 `testUpdate()` 方法中，设置了 `User` 对象的 `id`、`age` 和 `password` 属性，并调用 `userMapper.updateById(user)`。
画面 5: 展示了 `testUpdate()` 方法执行后，控制台输出的 SQL 日志，显示了根据 ID 更新记录的 SQL 语句。
画面 6: 展示了 `BaseMapper` 接口中 `updateById` 方法的定义，以及 `QueryWrapper` 的相关方法。
画面 7: 在 `testUpdate()` 方法中，创建了一个 `QueryWrapper<User>` 对象，并调用 `eq` 方法设置更新条件。
画面 8: 展示了 `testUpdate()` 方法中使用 `QueryWrapper` 进行更新的代码，但测试失败，控制台显示测试失败。
画面 9: 展示了 MyBatis-Plus 文档中关于“根据条件更新”的测试用例代码，包括导入的包和方法定义。
画面 10: 展示了 `testUpdate()` 方法中使用 `QueryWrapper` 设置更新条件的代码，但测试失败。
画面 11: 在 `testUpdate()` 方法中，创建了一个 `UpdateWrapper<User>` 对象，并调用 `eq` 方法设置更新条件。
画面 12: 展示了 `testUpdate()` 方法中使用 `UpdateWrapper` 设置更新条件的代码，但测试失败。
画面 13: 展示了 MyBatis-Plus 文档中关于 MyBatis 主要模块的介绍，包括核心功能、注解和代码生成器。
画面 14: 展示了 MyBatis-Plus 文档中关于“根据条件更新”的代码示例，包括 `QueryWrapper` 和 `UpdateWrapper` 的使用。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
/**
 * 根据 ID 修改
 * @param entity 实体对象
 */
int updateById(@Param(Constants.ENTITY) T entity);
```

画面 2:
```java
user.setUserName("cacao");
DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofPattern("yyyy-MM-DD HH:mm:ss");
LocalDateTime localDateTime = LocalDateTime.parse(text, dateTimeFormatter);
user.setBirthday(localDateTime);
int i = userMapper.insert(user);
System.out.println(i);
```

画面 3:
```java
User user = new User();
```

画面 4:
```java
user.setId(100L);
user.setAge(100);
user.setPassword("12222");
int i = userMapper.updateById(user);
```

画面 5:
```sql
UPDATE tb_user SET password=?, age=? WHERE id=?
```

画面 6:
```java
int deleteById(@Param("id") Collection<? extends Serializable> idList);
int updateById(@Param("et") T entity);
int update(@Param("et") T entity, @Param("ew") Wrapper<T> updateWrapper);
List<T> selectById(Serializable id);
List<T> selectBatchIds(@Param("coll") Collection<? extends Serializable> idList);
List<T> selectByMap(@Param("cm") Map<String, Object> columnMap);
T selectOne(@Param("ew") Wrapper<T> queryWrapper);
```

画面 7:
```java
QueryWrapper<User> queryWrapper = new QueryWrapper<>();
queryWrapper.eq("name", "曹操");
int i = userMapper.update(user, queryWrapper);
System.out.println(i);
```

画面 9:
```java
package cn.itcast.mp;
import cn.itcast.mp.mapper.UserMapper;
import cn.itcast.mp.pojo.User;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.conditions.update.UpdateWrapper;
import net.minidev.json.writer.UpdaterMapper;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
```

画面 11:
```java
UpdateWrapper<User> updateWrapper = new UpdateWrapper<>();
updateWrapper.eq("name", "曹操");
```

画面 14:
```java
@Test
public void testUpdate() {
    User user = new User();
    user.setAge(22); // 更新的字段

    // 更新的条件
    QueryWrapper<User> wrapper = new QueryWrapper<>();
    wrapper.eq("name", "曹操");
    // 可以设置多个条件

    // 执行更新操作
    int result = this.userMapper.update(user, wrapper);
    System.out.println("result = " + result);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 13:
标题: MyBatis主要包含以下模块：
- 核心功能 (core)，基于Mybatis的封装，提供了Mybatis Plus的基础配置类与核心功能，如内置通用 Mapper, lambda表达式查询等。
- 注解(annotation)，提供了Mybatis Plus中注解的定义。
- 扩展功能(extension)，提供扩展及插件功能，包括分页插件 通用 Service扩展 性能分析插件等。
- 代码生成器(generator)：通过代码生成器可以快速生成 Mapper接口 Entity实体类 Mapper XML Service Controller 等各个模块的代码，极大的提升了开发效率。
执行流程：
(1) 扫描注解Entity，反提取注解信息如：表名 字段名称等信息。
(2) 分析注解信息并基于com.baomidou.mybatisplus.core.enums的SQL生成基本CRUD SQL。
(3) 最后将这些SQL注入到Mybatis环境中。
因此Mybatis plus无需编写CRUD SQL语句，只需继承BaseMapper，魔术般的拥有了CRUD功能(通用CRUD)。

5) 不要评价画面美观，不要输出与课程无关的内容。
