# 11.Mybatis-Plus-条件构造器-基本比较器

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\11.Mybatis-Plus-条件构造器-基本比较器【海量资源尽在 666java.com】.mp4
- 时长 10分41秒（音频 641s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来看一下MyBetisPlus的条件构造器其实在前边我们学习增三改查的过程中我们都会用到一个叫Rabber的这么一个东西我们来设置条件Rabber呢其实它是一个什么它是一个接口那它其实实现的有好多对吧它实现的有QueryRabber还有这个什么UpdateRabber等等好多那么我们主要学习什么呢
[00:29] 这个Rubber你会发现嘛它是一个抽象类是不是啊抽象类它这里边呢你要想看的话其实它的原码呢也有好多嘛你可以看一下啊我给你打开Rubber是吧然后呢你可以看一下它的实现有多少啊是不是有好多呀还有这个Lambd的这个QueryRubber一会儿我们可以测一下还有UpdateRubber
[00:52] 是吧有好多好那现在呢我们来看一下啊我们要怎么测试这个条件构造器呢前边其实我们已经在测试增三改的时候啊包括查询啊我们都用到这个core wrap设置条件嘛只不过现在我们系统的把它拿出来来学习一下啊它的最基本的操作有好多有等于不等于你看就是它这个里面有好多方法
[01:20] 刚才咱们也说了你看这个GT是不是就是大于对不对它还有其实比如还有一个GE就是大于等于对吧EQ就是什么呀等于对吧还有一个什么NE就是不等于对吧好多那这里边在文档当中啊我都给你列出来了最常用的还有小于啊小于等于between呢not between呢是吧这些那现在呢既然我们拿出来学习这个什么rever那我们呢
[01:49] 就单独写一个测试方法吧来看一下啊顺便呢我们主要讲什么呢主要讲一个Lambda用Lambda的这种方式呢来这个使用这个条件拼装好来看一下这里边呢我们准备往里边设置一堆条件是吧设置一堆条件设什么条件呢比如说原来我们设置是不是有这个EQ是吧等于啥啥啥那现在呢我们是不是也可以设置
[02:19] 大于什么什么其实原来我们设置都是一个比较综合的这种条件了只不过我们还可以再综合一下比如说这个是什么呢这个内幕等于比如说曹操行吧然后呢还有我们是不是还可以设置这里面有好多我们印行不行印印的话那我们怎么设你随意弄个字段就可以嘛比如说我们让这个ID在一个地方或者内幕都可以
[02:47] 然后呢ID呢我们来印一下看一下比如印这里边有1235然后呢ID不太好啊用这个用啥呀用user下滑线name行不行可以吧这有一个曹操是不是啊我们这么弄让他这个user下滑线name这是字段名你要用的话你得用我们的这个属性对不对叫name是不是啊这么弄然后呢他呢是曹操
[03:21] 这样行不行然后我们是不是就可以来slack的了对那slack的前面我们学过查询嘛你slack的listslack的这个分页是不是都可以slack的pageslack的list是不是都可以其实这个不是主要的主要的是我们主要是来测试这个条件构造器嘛我们把它放进去那是不是就出现了这么一个结果呀那好现在我们来测试一下吧
[03:50] 那主要测试就是我们一会跑起来之后我们主要看伺候语句主要看伺候语句是不是符合我们的要求报错了你看见吗报错了报答错了有问题他不认识这个列那这个时候各位我们通过测试就知道了这里边这个内幕你看这就是列名列名你一定是和列名保持一致对不对好继续走再来
[04:19] 那我们现在测试的是什么呀大于出来数据啊这里边我们说查询出四条主要看Circle语句看看Circle语句是不是符合我们的要求inin在这么一个范围当中是不是啊是不是跟我们刚才说这个符合我们的要求吧那这种是通过这个Query Rubber其实它还有一个就是通过Lamb的这种方式因为我们当初学
[04:44] 加把基础的时候是不是学过Lamb的表达式啊那这里边呢它是怎么做的呢好啊我们这么做它有一个叫做Lamb的然后呢Corey Rubber看见吧其实这个方法倒很简单你看对不对但你现在用的是啥呀你现在用的是不是就是这个Lamb的这个Corey Rubber那Lamb的这个表达式的写法可不是这么写的呀它要咋写呀它这么写
[05:13] 比如user我要取什么呀我要取name那你这么写它是agent嘛agent那你就usergetagent好吧这么弄然后呢这个看好get username看用它的好处你会发现吗你这是写这个数据库里边的这个列名对不对那你其实我觉得应该是
[05:44] 对用Lambda表达式的好处就是直接我们可以造着我们的这个对应的模型类型来写我们的这个条件构造的这个代码就这个我觉得还是比较方便的要比直接写数据库的列明方便对吧那现在呢我们再来执行Lambda的这种表达式的这种方法来看看它能不能行看好啊这时候你看也查出来四条吧你看这个四口语句我觉得应该和刚才是一样的没问题吧
[06:14] 对好那这个就是我们说的什么条件构造器的一个基本用法我们刚才是不是讲了使用Query Reber和使用Lambda Query Reber这两种方式另外还有一个它的功能其实很丰富的其实新系的同学都发现了你看这儿你注意看很有意思就是说它在这儿你看GT比如说这个不用印你看
[06:43] 这个in的时候你看这是不是都是一堆的in呢但是这个一堆的in方法你看它有存在方法它总有一个第一个参数是condition就是条件这是啥意思呢这个的意思就表示啥呢就表示说当这个条件这个第一个参数为true的时候呢它就会拼装这个条件啥意思啊你可以想象一下其实很多我们项目的功能啊都是
[07:13] 用户输入一个条件根据条件来查询对不对其实我们说当用户输入内幕等于曹操的情况下我们再去拼装我觉得这个是比较合适的你看我一测试一下我一测试一下我再写一个这个是三你注意看现在我们准备怎么做我记得这个印这个条件先不用我给你测出效果现在我们去测试的结果你注意
[07:42] 我测试三啊你会发现它是内幕等于曹操年龄大于20的记录各位是不是就查询出来了吧对不对那我们说当符合一定的条件我再去拼装这个内幕等于曹操啥意思这个时候呢我们说在项目开发的时候很多情况下它会在页面输入一个什么输入一个内幕
[08:11] 叫名称然后呢根据传入的名称啊我们来拼装条件你有印象吗说这个时候我们就会用到刚才我说的那个我们怎么说呢它不是有一个条件吗那你就是它这个这个这个不等于空当输入的内幕不等于空并且我们要判断字符串的话一般我们是还要让它不等于什么呀空字符串
[08:43] 这个我觉得大家应该熟悉吧对不对当内幕不等于空并且它不等于空串表示一定传入内幕值了此时我们再去拼装条件大家理解我的意思吧那这个A节也是我们说当看好A节integer对吧A节那A节现在是20吗那我们也可以说当传入的这个A节不等于空
[09:20] 并且不等于空就行了如果你传进数据了那我就给你拼大家理解吗好那现在我们来测试一下你说老师这效果是啥呀这效果应该是和刚才我们的测试效果一样因为你没发现吧这个曹操20我都传入数据了吗就我的有意就是要让他拼装条件你看一样吧也是四条吧但是你要注意的看好我把它改成空
[09:45] 有表示这个条件没有传进去的情况下那我问你这个时候它就不是四条了吧那啥意思啊它都不光只查曹操的它查所有的人呢你懂我意思吗所以这时候我们再来查数据它就变成七条你会发现怎么弄啊它就没有刚才内幕等于曹操那个条件了大家理解我的意思吗所以这个condition就用在这就是符合一定的什么条件的情况下然后呢再拼装这个查询条件
[10:14] 就这个表达式必须为处后边才拼对这个在我们开发当中是非常常用的大家一定要注意这就是我们说的什么基本的一个比较查询基本比较查询呢这一边我们主要讲了一个Lambda的这种QueryRabber和我们说根据表达式是否为处来拼装条件的方式那这个是我们项目当中最常用的方法希望大家呢去好好练一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

