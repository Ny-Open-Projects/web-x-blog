# day02-15-Mybatis-Plus-增删改查操作

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day02-15-Mybatis-Plus-增删改查操作_【海量资源尽在 666java.com】.mp4
- 时长 15分22秒（音频 921s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才咱们通过一个快速入门案例体验了一把MP对吧这我觉得还不过瘾因为咱刚才只介绍了一个方法就是根据主件进行查询是不是那咱接下来继续再给大家介绍几个常用的方法这些方法其实就是最基本的增删盖查那当然了这些方法大家也都猜出来了
[00:31] 都来自于哪个接口啊对base map就是这一堆方法啊咱们再挑几个最基本的最常用的给大家演示一下那在演示这些方法的时候无非就是直接是不是调用一下这些方法就OK了非常简单那咱再找一个测试类就是这个测试类啊test user Mapper我们在这里边呢继续给大家演示一些常用的数据库操作
[01:00] 你看这儿呢它是不是已经把user Mapper这个对象导进来了是吧导进来之后呢咱就写测试方法直接进行演示就行了那咱看一下讲义咱先演示谁呢咱先演示一个插入操作就对应的方法叫insert大家看一下这个接口base Mapper其实就是第一个方法对不对就是它那我们观察一下吧这个方法它有一个参数是不是要一个实体对象吧对不对
[01:30] 那我们就是要把这个实体对象呢保存到表里边做一条记录是不是那它也有一个硬碳类型的反应值啊这个反应值什么意思呢一会儿再说那咱接下来的话就演示一下这个插入操作那我就需要在这儿啊写一个测试方法public void testnsert然后呢在这个方法上面一定要记得加上test注解对不对
[02:02] 然后在这里边呢我们就直接通过user Mapper的什么方法对insert方法来进行数据的保存就行了那我们要保存的数据不就是一个user对象吗是不是user对象啊就是他那我们得在insert之前自己造一个什么呀user对象这个都比较简单了这样呢我们导一下包吧导一下包
[02:42] 那有的对象创奖之后是不是得调set方法给属性干什么呀是不是复职对吧什么邮件年龄啊等等之类的一堆啊这个我就不再给大家敲了我们把讲义的直接粘过来是不是放到这就行了对不对曹操是不是然后呢我们把这个谁啊对user对象放到这就OK了对非常简单不用写伺候语句啊由insert的方法帮我们自动生成
[03:13] 然后我们刚才提到这个方式有一个印象类型的反位值是不是那这个反位值表示什么意思呢咱一起看一下讲一里边说了这个反位值是受影响的函数可不是那个主件的ID不是这个ID人家看我这里边给ID的值呢没有给ID负值是不是主件没有负值没有负值行不行呢咱一会再说咱先试一试吧对不对但人家说了这个因此的话反位值是受影响的函数可不是这个什么
[03:45] 主键的直块查了你要注意当然我们也可以把它打印出来看一看我们就接收一下int i s u l t是不是然后把它打印一下i is out就这样了接下来测试一下走然后我们观察控制台我们在入门里边给他说要观察什么东西要观察控制台打印的搜扣语句是不是咱找一找搜扣语句是在
[04:20] 哪里呢找一找应该是在下边这一块才在这这这这这是不是因三人因兔对不对然后一个参数是一个对象吗然后一这应该是受影响的函数那咱去表里边瞅瞅有没有这个插入成功刷新有吧是不是你看他这个主见的值是不是他应该是通过某种算法生成的这个咱一会会单独讲主见生成策略
[04:53] 这证明我们是已经怎么着超成功了然后咱看控制台打印的那个那个那个反而值是多少控制台打印的值跑哪去这去哪瞅在这儿一明显是不是不是这个主见的值不是啊一就是受影响的函数那有同学说老师我想得到这个主见的值怎么办那咱讲一边也说了啊这个主见的值啊你保存完之后呢这个值会自动放到这个user对象里回填自动回填你不信你可以试试
[05:23] 你可以打印一下叫叫叫什么user.get什么呀id是不是他自动都放进去了你都不用管那我们再次运行一下看是不是如此走我们是不是又插入了一个曹操是不是啊咱就观察空间台的打印的值就行了你看这是什么呀3457对不对3457你看表里边来刷新一下这是不新插入的3457没错吧
[05:58] 所以说呢这是什么操作呀对insert操作这样简单调一下这个方法搜狗局帮我们生成那这里边我们是不是涉及到这个主建的生成策略对不对那咱看看讲一我们看看MP里边关于主建的生成策略它是都有哪些套路是不是咱看看你看他说了在刚才的例子当中呢数据的确是保存了数据库了但是ID的值呢不是我们期望的自增长的确不是是不是
[06:28] 你看我们要是自尊的话应该是12345该6了嘛对不对但是他是生成的这这个一长串东西他能做主见的值吗当然能啊当然能这是他内部默认的一种策略那我们也可以自己去设置这个ID的生成策略可以的啊主见的生成策略通过谁呢通过ID type这个类ID type这个类呢是MP提供的一个类啊通过它呢可以设置这个主见生成策略那我们看一下这个ID type这个类其实是一个枚举类一个枚举类
[07:00] 那这里边你看都有哪些取值啊第一个凹凸他表示数据库就是什么呀自赃是不是还有什么呀那是吧不设置还有什么input input应该是自己提供值吧好uid对不对咱刚才这个应该是uid吧我觉得啊有可能是uid就生成了一个不重复的一个一个一个一个一个主线的一个值反正他有好几种这个生成策略
[07:30] 那我们现在需要什么呀需要自增是不是需要数据库自增说要数据库自增的话我们需要怎么设置一下呢来咱看讲义很简单你看在这儿这个注键你还有印象吗这个注键来咱看咱的实体内U字的咱打开在哪是不是这个对吧我们当时讲到这的时候说过我们这个推过ID是专门映射谁啊主键字段的非主键字段是用TableField对
[08:00] 那你要想人为的去设置主见生成策略的话就在这个注解里边加上一个type属性啊然后呢啊复一个id type的某个取值就行了比方刚才说的凹凸就表示什么呀自动增长那我们这改一下就行啊在哪改啊对就是在这个地方改啊当然了这个东西呢你可以删掉为啥可以删掉因为它这个属性名跟字段名是一致的对不对你其实不写是可以的啊
[08:31] 那我们就直接写一个什么呀type然后叫什么名ID对type我们选择哪个auto这就表示呢我们这个主件的值是自增的自动增长那到底行不行呢咱再做一个测试呗那还是这个方法我直接就运行了看看这次新插入的数据那个主件的值会是什么样咱不看控制台了咱直接去表里边刷新一下看一看有没有自增啊
[09:03] 这是啥玩意儿啊对不对这个也叫自增啊你看上面是什么呀3457这就变成什么呀3458它自增是看最后那一行是在它的计划性增低增的啊这是7这就变成什么呀8当然了你要是把这三行数据全删掉再差不了的话应该就是减应该是6它是基于这进行自动增长啊所以咱这个也是效果出来了啊也是自动增长这是什么操作呀
[09:32] 插入操作的也是到这了接下来就是更新操作那么更新操作对应的方法叫update by id建名之意是根据什么来进行修改的是不根据组件对不对根据组件也就是说我要修改某一行里边的这个数据传进来的是不是一个实体对象因为我在修改某一行的时候我可能会修改这行里边好多字段的值这些值是不是都封装到实体对象里边是不是
[10:01] 那咱接下来呢就演示一下这个update by id方法那咱也是单独写一个测试方法public testupdateupdate by什么呀id方法那我们也是直接先尝试着去调用这个方法update这个啊update by id是不是还是要一个user对象对不对那我们就可以
[10:36] 在调这个发之前啊也是准备一个什么呀对有了对象有想这个我就跟讲义保持一致了你看我是不是自己准备了一个什么呀对user对象然后ID主件给值了没给了主件一定得给值给的是666有吗这个6那没有啊没有那就给个谁呀五倍孙七倍是不是这个你要根据表里边数据进行修改啊五
[11:06] 因为我们说了嘛这个update by id是根据主件进行修改所以你主件一定得给值啊另外呢你要修改哪些字段的值你修改谁就调用setter方给他复个新值就行你比如孙七原来的年龄是24我现在准备给他改成什么呀21啊那如果我想改这个什么密码或者啥的怎么办你要改密码你接下来就要调用他的什么呀setter password的方再给个新值就行你知道什么意思吧很简单啊然后呢把这个谁啊给优待对象放到这就行
[11:35] 那这个方案有没有返回值呢这少一个 void 啊那这个方案有没有返回值呢好咱看一下你要返回值是不是 int 印他这边是什么意思呢应该也是受影响的什么呀行数也是受影响的行数啊他这没有说但是咱基本上也能分析出来你也可以接收一下给他打印都可以好然后我们接下来呢打印一下啊阿姨好不知道好咱接下来走跑一下啊
[12:15] 还是要观察控制台这次应该是生成的是update的语句吧对不对update语句在瞅瞅啊这个在哪呢在这你看这个语句比较短吧update我们是不是只改了一个年龄根据主件嘛对不对你看反正只是1就受影响好像是1嘛那表里边动了没有啊原来是24刷新1是不是变成21了没错吧这就是这个什么操作呀对更新操作其实就是修改
[12:48] 然后再最后一个呢就是删除操作删除对应的方法叫delete by id简明之意很简单了就是给我一个主键我就把这一行数据给干掉非常非常简单那接下来直接单独写一个测试方法进行演示public void testdelete by id
[13:17] 然后呢我们这个就更简单了直接调用他的delete by id方法你想删谁你看谁不顺眼你就删谁呗你看谁不顺眼还孙七吧他今天有倒霉是不是五主键是我主键是我直接写个五就OK了反正咱们不用搭理他咱就直接反正只要删掉就行了完了吗那咱看讲义是不是就非常简单对不对
[13:47] 咱检验还打印了一下这个日子啊日子啊其实也是受影响的行数啊我这就不再打印了就跟上面更新是一样的那我接下来就直接进行测试了走咱观察一下控制台瞅一瞅这个输出的语句在什么地方在这儿看看对吧delete from这个表根据主件受影响的行数是不是一行吗对吧传过去的这个值是不是五吗对不对这个五吗
[14:17] 然后咱去表里边瞅一眼呗刷新孙青的哥们就没了对不对这是什么操作呀删除操作我们也给大家演示了一下那还有吗还有一个查询操作slack by id这个我就不再给大家演示了因为在入门案例的时候是不是演示的就是这个slack的by id这个也非常简单给个主件的值就做了这个什么查询给你主件进行查询这个入门案例讲过了就不再说了这是
[14:48] 我们把MP当中最基本的增删改查这几个方法给大家介绍了一下最后呢我们还是给大家强调一下啊就是使用MP呢是非常的简单不用我们编写搜寄语句因为它可以根据什么呀根据你调用的方法然后结合什么呀实体类当中配置的这种叫什么叫映射关系对吧就可以很聪明的帮我们自动生成这些什么呀搜寄语句的
[15:18] 这一点大家一定要注意

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 MyBatis-Plus 在 Spring Boot 项目中如何实现用户数据的增删改查操作，重点讲解了 BaseMapper 接口、实体类注解、以及测试方法的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示了 IDE 中的项目结构，包含 `src/main/java` 下的 `TestMybatisSpringBoot`、`UserMapper`、`BaseMapper.class`、`TestUserMapper.java` 等文件。
- 右侧编辑器显示 `BaseMapper.class` 的反编译代码，其中包含 `insert(T entity)`、`deleteById(Serializable id)`、`updateById(T entity)` 等方法。

画面 2：
- 显示 `TestUserMapper.java` 文件，其中包含 `@Autowired` 注解的 `UserMapper` 字段和 `@SpringBootTest` 注解的测试类。
- 代码中定义了 `public UserMapper userMapper;` 和 `@Test public void testInsert() { ... }` 方法。

画面 3：
- 显示 PPT 页面，标题为“3.1.1 insert方法”，内容包括 `User user = new User();`、`user.setEmail("123@itcast.cn");`、`user.setAge(30);` 等设置用户属性的代码。
- 代码中包含 `int result = userMapper.insert(user);` 和 `System.out.println(result);` 用于插入数据并打印影响行数。

画面 4：
- 显示测试结果，输出为 `None`，并列出 `Unconditional classes`，包括 `org.springframework.boot.autoconfigure.context.ConfigurationPropertiesAutoConfiguration` 和 `org.springframework.boot.autoconfigure.context.PropertyPlaceholderAutoConfiguration`。

画面 5：
- 显示测试结果，输出为 `None`，并列出 `Unconditional classes`，包括 `org.springframework.boot.autoconfigure.context.ConfigurationPropertiesAutoConfiguration` 和 `org.springframework.boot.autoconfigure.context.PropertyPlaceholderAutoConfiguration`。
- 同时显示了 `TestUserMapper.testInsert()` 方法的测试日志，包括 `Preparing: INSERT` 和 `Updates: 1`。

画面 6：
- 显示 PPT 页面，标题为“3.1.1 insert方法”，内容包括 `User user = new User();`、`user.setEmail("123@itcast.cn");`、`user.setAge(30);` 等设置用户属性的代码。
- 代码中包含 `int result = userMapper.insert(user);` 和 `System.out.println(result);` 用于插入数据并打印影响行数。

画面 7：
- 显示 PPT 页面，标题为“3.1.1 insert方法”，内容包括 `User user = new User();`、`user.setEmail("123@itcast.cn");`、`user.setAge(30);` 等设置用户属性的代码。
- 代码中包含 `int result = userMapper.insert(user);` 和 `System.out.println(result);` 用于插入数据并打印影响行数。

画面 8：
- 显示 `User` 类的 `@TableId` 注解，其中 `keyType = IdType.AUTO`，表示主键自增。
- 同时显示了 `@TableField` 注解用于映射字段。

画面 9：
- 显示 `User` 类的 `@TableId` 注解，其中 `keyType = IdType.AUTO`，表示主键自增。
- 同时显示了 `@TableField` 注解用于映射字段。

画面 10：
- 显示数据库管理工具中的 `tb_user` 表，包含 `id`、`user_name`、`password`、`name`、`age`、`email` 等字段。
- 表中数据包括 `id=1`、`user_name="zhangsan"`、`password="123456"`、`name="张三"`、`age=18`、`email="test1@itcast.cn"` 等记录。

画面 11：
- 显示 `TestUserMapper.testUpdateById()` 方法，其中包含 `user.setId(1L);`、`user.setAge(21);`、`int result = userMapper.updateById(user);` 和 `System.out.println(result);`。
- 同时显示了测试日志，包括 `Preparing: UPDATE` 和 `Updates: 1`。

画面 12：
- 显示 `TestUserMapper.testUpdateById()` 方法，其中包含 `user.setId(1L);`、`user.setAge(21);`、`int result = userMapper.updateById(user);` 和 `System.out.println(result);`。
- 同时显示了测试日志，包括 `Preparing: UPDATE` 和 `Updates: 1`。

画面 13：
- 显示 `TestUserMapper.testDeleteById()` 方法，其中包含 `userMapper.deleteById(id);`。
- 同时显示了测试日志，包括 `Preparing: DELETE` 和 `Updates: 1`。

画面 14：
- 显示 `User` 类的 `@TableId` 注解，其中 `keyType = IdType.AUTO`，表示主键自增。
- 同时显示了 `@TableField` 注解用于映射字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

public class TestUserMapper {
    @Autowired
    private UserMapper userMapper;
    @Test
    public void testInsert() {
        User user = new User();
        user.setEmail("123@itcast.cn");
        user.setAge(30);
        user.setUserName("张三");
        user.setPassword("123456");
        int result = userMapper.insert(user);
        System.out.println(result);
    }
}
```

画面 2：
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

public class TestUserMapper {
    @Autowired
    private UserMapper userMapper;
    @Test
    public void testInsert() {
        User user = new User();
        user.setEmail("123@itcast.cn");
        user.setAge(30);
        user.setUserName("张三");
        user.setPassword("123456");
        int result = userMapper.insert(user);
        System.out.println(result);
    }
}
```

画面 3：
```java
User user = new User();
user.setEmail("123@itcast.cn");
user.setAge(30);
user.setUserName("张三");
user.setPassword("123456");
int result = userMapper.insert(user);
System.out.println(result);
```

画面 4：
```java
None

Unconditional classes:
org.springframework.boot.autoconfigure.context.ConfigurationPropertiesAutoConfiguration
org.springframework.boot.autoconfigure.context.PropertyPlaceholderAutoConfiguration
```

画面 5：
```java
@Test
public void testInsert() {
    User user = new User();
    user.setEmail("123@itcast.cn");
    user.setAge(30);
    user.setUserName("张三");
    user.setPassword("123456");
    int result = userMapper.insert(user);
    System.out.println(result);
}
```

画面 6：
```java
User user = new User();
user.setEmail("123@itcast.cn");
user.setAge(30);
user.setUserName("张三");
user.setPassword("123456");
int result = userMapper.insert(user);
System.out.println(result);
```

画面 7：
```java
User user = new User();
user.setEmail("123@itcast.cn");
user.setAge(30);
user.setUserName("张三");
user.setPassword("123456");
int result = userMapper.insert(user);
System.out.println(result);
```

画面 8：
```java
@TableId(type = IdType.AUTO)
private Long id;
@TableField("user_name")
private String userName;
@TableField("PASSWORD")
private String password;
```

画面 9：
```java
@TableId(type = IdType.AUTO)
private Long id;
@TableField("user_name")
private String userName;
@TableField("PASSWORD")
private String password;
```

画面 10：
```sql
CREATE TABLE tb_user (
    id BIGINT(20) NOT NULL AUTO_INCREMENT COMMENT '用户ID',
    user_name VARCHAR(30) DEFAULT NULL COMMENT '用户名',
    password VARCHAR(30) DEFAULT NULL COMMENT '密码',
    name VARCHAR(30) DEFAULT NULL COMMENT '姓名',
    age INT(11) DEFAULT NULL COMMENT '年龄',
    email VARCHAR(50) DEFAULT NULL COMMENT '邮箱',
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

画面 11：
```java
User user = new User();
user.setId(1L);
user.setAge(21);
int result = userMapper.updateById(user);
System.out.println(result);
```

画面 12：
```java
User user = new User();
user.setId(1L);
user.setAge(21);
int result = userMapper.updateById(user);
System.out.println(result);
```

画面 13：
```

