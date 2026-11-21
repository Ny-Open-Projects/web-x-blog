# 08.Mybatis-Plus-通用CRUD-更新操作

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\08.Mybatis-Plus-通用CRUD-更新操作【海量资源尽在 666java.com】.mp4
- 时长 8分35秒（音频 515s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面呢我们来看一下MyBetis Plus通用CLUD的更新操作更新呢在我们实际的项目开发当中也是比较常用的比如说修改一个对象的信息对吧好 那现在更新怎么做呢这里边我们讲几个方法一个是Update by ID通过这个方法呢大家应该知道它是根据组件来更新是吧 更新那怎么做呢来 看一下啊咱们打开它的这个测试文件
[00:26] 这里边呢以上呢是不是就是上边是不是就是我们说的这个插入的对吧下边我们要做更新了啊好更新的话刚才我们是不是说了有一个叫做update by id啊那这里边呢我们就可以直接拿来这个user Mapper我们点update by id看见了吗那么在这个by id里边各位给您看一下
[00:56] 它是不是传入一个对象传入一个对象的话那怎么做呢你比如说user看好啊new一个user那你new一个user有人说老师那你往里边设置什么属性呢首先设置ID为啥因为你是update by ID这是不是就是要更新的对要更新记录的什么组件值你说你要更新哪一个记录呢那你要更新比如说更新100
[01:26] 行不行那你就设置100但有时候老师那我想更新某一个字段那我怎么设对不对比如说我想把这个年龄我想更新成100岁各位那我怎么弄那你就设置A就等于100就行了理解吗有时候老师我想把这个密码我想更新一个那你就设密码很简单看下吗但是
[01:58] 我如果说没有设置的比如说你看这个U的对象里边我只设了三个属性第一个属性是组件另外两个属性是要更新的值这是要更新的值是不是那我没有设置的那些属性它会更新吗它会更新到数据库吗不会所以这个方法它的特点是什么它只会将什么对只将对象当中不为闹的值
[02:28] 更新到什么数据库中那所以说我们现在如果我们去更新执行一下更新它返回的也是一个什么更新的一个记录的一个条数啊然后我们运行你就其实可以观察观察什么呢观察它打出的SQL日志看好要观察那你看这里边你看它是不是发了一个update语句
[02:56] 是不是where id是不是就是组件更新两个字段是不是和我们预期的是一样的对这就是根据id进行更新那么有人说老师我想除了id呢我想根据比如说某个条件进行更新那怎么做也就是根据一定的什么条件进行更新这怎么做呀那这时候其实它还有另外一个什么方法
[03:23] 你看它这里边还有一个叫update什么只有一个update里边传入一个user看吧然后呢这里边可以输入条件它这么多那么我们说这个是user对吧user这user到底是啥嘞那还要组件吗不需要了user还是要更新的值就user里边只要不围空的都会把它更新到数据库当中但是有人说老师那你条件呢根据条件你的条件在哪设呢
[03:53] 这个条件我们可以单独设设置什么条件设置条件这个设置条件你看它这里边的这个参数是不是有一个叫叫啥叫rever是吧那我们就应该可以设置一个什么设置一个update rever当然你这个是条件嘛你这个条件的话我们就需要用这个另外一个rever就是叫做什么呀叫做query rever
[04:22] 就是它好那这个query wrapper它是啥意思呢它是专门用来设置条件的看好很有意思你有一个query wrapper那怎么设条件呢比如说呀我们说内幕凡是内幕等于曹操的看好你要注意我的这个数据库的这个记录当中啊你会发现它有很多的记录内幕是不是都是曹操
[04:49] 对我现在呢想批量只要内部的你曹操了我就准备更新更新成我把A姐呢更新成100岁你觉得行不行你看这是不是还有五条记录都是曹操呀A姐是20岁对吧现在如果我这么一执行的话对他就会进行一个什么按条件进行更新看好那我们其实还是观察他的Circle预矩根据Circle预矩呢我们就可以来看
[05:17] 它到底发出没有发出我们想要的思考你看内幕等于曹操是吧更新两个字段那其实你这时候刷新你看这是不是就是根据条件更新根据条件更新但有人说老师根据条件更新刚才说了它只会将对象当中不为空的值更新到表中那其实我现在有一个需求我有啥需求呢我就想把内幕等于曹操的
[05:47] 我把这个Bursley全部更新成空这怎么做这怎么做这时候就不能用query wrapper了那你需要用什么注意这里边我再教给大家一方要用update wrapper叫update wrapper它就可以来实现这么一个什么就可以把为空的这个记录更新到数据库中因为有人说有这个需求吗
[06:18] 其实有的有时候你去更新的时候你如果没有设置值它就会把这个字段里边内容更新成空懂吗所以这里边呢我们可以将什么围空的这个值更新到数据库这样的话怎么做呢刚才我们看到了吗它其实是用一个东西叫啥呀叫update叫update wrapper这个东西咋用啊和刚才我们的query wrapper有啥区别
[06:49] 我告诉你它非常简单跟刚才的CoreRubber差不多但是呢这里边你可以设置比如说我想根据内幕等于什么曹操来更新怎么更新呢更新哪些东西我更新那就写set我更新写setset是什么我就准备把这个Boss的这个字段更新成空各位
[07:20] 这句大家能理解吗就是内幕等于曹操的我把Bars的这个字段更新成空是吧很简单那原来这第一个参数你看这是不是有一个user是吧user里面是不是要更新的值现在你就不用传了写成now就行了但是现在你要把update wrapper写进去注意这一种方式就可以把空值更新到数据库对原来是只能更新不为空的值现在可以把空值更新到数据库了你刷新你看没问题吧其实你当然大家要注意的还是看这个
[07:49] 日志你看日志当中看是不是就是内部的一槽槽的Boss的那一槽槽的你是不是就更新到我们的数据库了以上呢就是我们学习的这个更新操作根据组件来更新然后呢在这个对象当中设置主见值一定要设置主见值然后就是更新的字段还有根据条件来更新那你就主要是设置啥呀一个是要更新的这个对象的里边的这个数据另外还有一个就是
[08:19] 更新的条件但是前边我刚才说的这个根据组件和根据条件来更新都是只能将不唯空的值更新到数据库最后我们是不是学了一种叫可以将唯空的这个数据更新到数据库对吧好那这就是更新操作好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import cn.itcast.mp.Mapper.UserMapper;
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

