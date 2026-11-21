# 09.Mybatis-Plus-通用CRUD-删除操作

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\09.Mybatis-Plus-通用CRUD-删除操作【海量资源尽在 666java.com】.mp4
- 时长 5分36秒（音频 337s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来看一下mybattlesplus的删除操作删除操作这里边呢我们讲几个方法一个是根据ID组件来删除只要传入一个组件呢就可以把这个组件的记录呢给删除掉那这个比较简单一会儿呢大家自己演示就可以了好那后边还有一个就是根据条件来删除这个呢主要是设置符合条件的记录都会删除最后一个批量删除好
[00:27] 根据组件删除呢这个比较简单大家自己测试就可以了来我给大家演示一个根据条件来删除好上面刚才是个更新是不是就做完了那我们来打打一个分隔然后呢接下来这里面我们要做什么呀是不是就是test delete对吧那么这个test delete我们刚才说嘛一个是根据组件一个是根据条件现在我们根据条件来删除根据条件删除怎么做呀你看你可以user Mapper然后呢
[00:59] 点一下然后这里边是不是有一个叫做delete看是不是有很多方法呀其中有第一个方法delete里边有一个叫rever看见吧我们就可以传条件那传怎么传条件呢上面我们是不是说过这个条件呀你看我们是不是就可以这么做这是不是就是设置条件对不对设置条件好那现在设置条件的话我们怎么设啊比如说这么设啊看我们扫三几个比如说这个是
[01:29] 111岁行不行我们准备把A几等于111的把它删掉行不行可以看好A几等于111然后呢你把它放进去这就OK了那这个返回的这个数据结果呢其实还是删除了数据记录的个数来执行我们是不是就可以来把它删掉注意看
[01:59] 没了吧那你说老师我想不光根据A节等于111我还想怎么弄啊我还想根据这个内母就是A节等于100岁对吧然后呢内母再等于某一个值那你其实你就多设几个就行了你看这个条件是不是可以设多个呀对吧那这个就是草草1行不行我把这个删掉那这个其实这里面是没有记录的所以呢
[02:30] 其实你执行删除啊它是删不掉的对吧你可以跑一下试试但是我们可以观察Circle语句就可以知道是不是按照我们的预期去执行的删除大家来看看好这里边是不是就是有一个叫做DeleteFromTPUser然后呢哎你看是不是Agent等于谁Name等于谁你看是不是就是根据两个条件来删除啊哎对这就是根据条件删除
[02:56] 其实根据条件删除的话以上这个我是不是通过这个query wrapper来设置的条件其实还有一种设置条件的方式嗯另一种设置条件的方式是这么做的你看啊我定一个user定user干啥呢这个user呀你可以往里边放置一些属性你比如说我现在设置100看啊我是不是设了一个条件我不是设了一个属性吗那你在
[03:23] 定义这个rever的时候你注意你可以把user放进去你看见吗它就会自动根据user里边不为空的这个属性来拼装成一个什么条件对你说老师这个会这么智能吗其实我告诉你很简单因为它只要检测这个属性不为空它就把它作为rever的一个条件就可以了你看我这么做其实也是可以的那这里面是不是把user放到这个query rever的一个构造参数了对吧你往下看看circle
[03:52] 是不是跟刚才一样啊是不是这个社会语言没问题这就是根据条件删除好还有一种就是批量删除这批量删除是干嘛呀是不是就根据ID就是我传一堆ID来删那这个是怎么做呀看好啊我们复制一个代码然后呢现在这就是批量删除批量删除的话其实它就比较简单了为什么因为它是根据ID3嘛根据ID3你只要设一堆ID就可以了
[04:22] 那这里边我们主要是就不用设条件了这里边我们直接就什么呀delete你看是不是有一个叫delete batch ids对吧那这里头你看它是不是放一个什么集合的对象对吧放集合的对象那集合对象里边是不是有一对 id 啊那我们其实就可以怎么做呀嗯我们其实可以往里边放比如说弄几个 id 边比如说101行不行哎然后呢
[04:53] 102然后103我是不是可以这么做然后它是不是就批量删除了这个方法是啥这个方法就是把这一堆数组啊转成一个集合然后它传给这个delete batch 这个方法好其实我们主要看circle一句看那最终它拼成的一个circle啊你看它拼成一个什么样的circle是不是就是id in一堆的数据这就是批量删除对吧没问题好那么来
[05:24] 继续我们往后看吧这就是我们说的什么删除操作根据组件删除还有根据条件删除然后呢批量删除那大家呢自行练习一下好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

