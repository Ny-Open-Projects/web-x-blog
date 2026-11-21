# 12.Mybatis-Plus-条件构造器-其它比较器

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\12.Mybatis-Plus-条件构造器-其它比较器【海量资源尽在 666java.com】.mp4
- 时长 5分36秒（音频 337s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那接下来我们继续来学习MyBitX Plus的条件勾召器下边我们看一下它有模糊查询模糊查询其实大家可以看到是不是有四种有likelike的话这种like最终拼出来的circle就是两边加百分号模糊查询not like就是不进行模糊查询like leftlike right那这个left就是在左边模糊这个right就是在右边模糊
[00:29] 这个大家能理解吗好我们来看一下吧其实这里边呢我们这个模糊查询就跟我们在这查是差不多一样的啊比如说这个name我们来看一下这里边名字name like那name like的话刚才我们说了嘛你是比如说这个这个这个这个曹曹曹我们要like right就是在右边模糊看见吧右边模糊
[01:02] 你看是不是就在右边加一个百分号看到吧那是左边模糊那你还能查出来吗查不出来了你要是两边模糊这肯定能查出来看到了吧所以这就是刚才我们说的这几种类型那么你要是去测试的话也比较好测你看Rubber它是不是有一个点like的方法那你说老师你这个百分号需要我们加吗不需要加
[01:29] 它自动给你加你要用like的话它自动会在这个什么你传输的数据两边加入自动加入百分号来我给你测一下看好然后这个方法我就不再写了注意看好我们主要是给你测出一个结果来这是一个什么曹操的曹字看好我现在是不是用了like我用的like最终最终mybattlesplus它会自动给你拼装
[01:58] 一个参数就是两边加百分号了你看往后往后翻各位你来看你看你传入的是一个槽字但是呢你看mybid is plus两边会自动给你加百分号对不对但如果说你说我这用什么呀我用like什么write那like write这就相当于是在槽的右边给你拼装百分号这是我们说的一种模糊的方法所以它这个
[02:26] MyBattiesPlus设计的还是非常灵活的你看没错吧其实这些东西我告诉你在MyBatties里边是没有的也就是MyBattiesPlus对它进行封装了提供了很多开发当中常用的方法它就有了这些方法非常适合我们去开发模糊查询其他的方法大家自己测一下好逻辑查询逻辑查询大家都知道我们是不是要拼装条件按的啊all呀是不是都有其实用的最多的应该是按的
[02:56] 对吧用的最多的应该是按的其实我们刚才我们测试这个rebel的话你会发现它要拼装很多条件这默认的就是什么默认的就是按的对吧但它也支持all也支持all它要是你要是想通过all的方式来写条件的话你就需要在这个什么呀在这个条件后边加一个all这个方法这时候它就通过all拼装了这个呢大家自己测一下我就不再演示了
[03:25] 好那么后边一个就是selectselect是啥意思就是我们平常查数据是不是就查询全部但你说现在我查询全部字段字段比较多我想只查询某几个字段这时候怎么弄这个时候我们就可以在这干嘛你用一个叫select我只想查询ID对吧我还只想查询name这时候我们是不是就只查俩字段
[03:54] 这个时候呢它就可以slack的ID name把这个查询的字段的这个列呢给它固定了那我们来看你看这时候结果就出来了这是不是ID逗号内幕看到吧就在这好那这个是指定我们要查询的列就知道了最后一个排序排序的话有三个方法一个是升序一个是降序大家可以看一下它这个是升序
[04:24] 它有一个order by asc那么当你传入id name这里边它会按照两个字段生讯也就是最终拼出的cycle是order by id asc name asc那降序其实和它差不多就是变成降序那么还有一个叫order by其实这种方法它就比上边的两种方法稍微灵活一点点为什么呢因为它可以让你自己去设置是否生讯
[04:53] 你要是这个什么出那就是升序否则呢就是降序所以这几个方法呢其实大家都可以去自行测试一下吧就比较简单啊然后呢我就不再去演示了大家测一下好那么到这儿呢我们的条件构造器这个小节呢我们就全部讲完了那这里边的重点我希望大家去基本比较操作里边的东西特别是Lambda
[05:19] 这个query wrapper以及通过这种Lambda query wrapper条件的方式去查询这个大家一定要注意练一下这个是Lambda query wrapper下面是不是就是表达式为处才拼装条件这种方式这个是重点好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

