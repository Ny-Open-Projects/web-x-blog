# day02-18-Mybatis-Plus业务层封装

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day02-18-Mybatis-Plus业务层封装_【海量资源尽在 666java.com】.mp4
- 时长 9分49秒（音频 589s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好截止到目前呢我们已经把MP相关的一些东西就给大家介绍完了我们给大家介绍的都是最常用的一些东西啊没有介绍到的话咱后边用到时候再说目前这些东西就基本上够大家开发用虽然MP的相关的这个基本的东西已经讲完了但是MP给我们带来的惊喜其实还没完所以说我们接下来还要讲最后一块东西这一块什么东西呢咱接下来看看啊
[00:31] 看这块代码你熟悉吗大家知道我们在开发的时候是不是分为三层吗有一项表现层右层数据访问层对吧那一般是谁调用谁原来层调用右层右层调用数据访问层然后你看看这块代码是哪一层调用哪一层呢是不是右层注入了这是Mapper对象是不是注入了数据访问层是不是调用他的方法这代码很简单对不对
[01:05] 所以这是我给大家写了一个咱们传统的业务层的玩法啊就是注入数据法案层的对象然后调他的什么呀增杀改善的一些方法没问题吧那么大家注意了MP呢对业务层也进行了封装因为MP也知道啊知道你你业务层你就是这么玩的嘛固定了一个套路干脆这些东西你不用写了这个东西你也不用写了这些活我帮你干了不就完事了吗对不对
[01:34] 我一封装好你到时候继承我的一个一个什么接口啊一个什么类搞定了对不对多简单所以说呢这样呢我们最后要给大家讲的就是我们说MP啊他对业务层也进行了封装让我们的开发效率更高让我们开发更爽是不是所以说我们前面说了吗MP是咱的好基友他知道我们心里在想啥他知道我们需要啥那么他对业务层的封装最终
[02:03] 能达到什么效果以及怎么去使用咱家一起看一下啊非常简单那首先第一个要求呢就是他要求业务层的接口就咱自定义的啊业务层的接口必须继承他提供的这个iService这个接口第二个要求呢就是我们业务层的实现类啊我们业务层自己定义的实现类必须继承他提供的这个ServiceiMPR这个类然后完事了就这么简单
[02:34] 就这么简单这时候你会发现我们业务层的接口包括业务层的实现类你会发现是不是空的对不对你以前这里边是得定义一堆增山改查的方法还要注入什么呀买份接口然后还要调用它里边的方法现在不用了你只需要让你业务层的接口继承MP的接口让你业务层的实现类继承MP的一个实现类就完事了其他代码统统不用写但是你会发现增山改查照样能用咱们俩试试吧对不对
[03:05] 我都感觉不相信是不是咱进来试一试啊咱就怎么着呢咱就在你看我这是不是有个Service一个包对不对这就是要层呗我们新建一个接口就叫user services e r v i c e点击ok然后我们就自己定义了一个要层的接口对吧但是呢我们有要求现在啊这个接口必须继承什么呀
[03:38] 对MP提供的一个叫i什么呀Service的这个接口然后里边还要提供实体类的翻形啊这就是这个样子那然后呢咱这个接口其实你什么方法都不用定义这跟以前不一样吧咱以前用层这个接口里边是要定义一堆方法的啊那为啥不用定义呢因为在这个i Service里边都定义好了呗我们跟踪一下原吧我们看到这个实现率就行对不对这里边我们可以瞅一瞅
[04:10] 你看里边给他把ID这个建名之一对吧get one list方法配给分页方法删除对不对等等等等啊把我save是不是这是接口然后有了接口之后呢我们接下来还要定义什么呀实现类呗实现类我们起个名字叫user Service vse啊imimpl
[04:40] 当然呢他一定是要干什么要实现咱刚才的那个接口对吧叫useruseruseruser然后呢他还需要干什么继承MP提供的一个类叫serviceimplviseimpl
[05:04] 大家注意啊这个类呢要求提供两个范围形一个是Mapper接口一个是实体类Mapper接口呢我们就叫user对Mapper实体类呢就叫什么呀user对然后呢咱这个实验类当中你就这么空的扔到这就行了不用写任何代码但是实际上实际上这个类当中已经有了一堆增删改查的方法答案是不是都记成字这对吧
[05:35] 而且呢你这里边你也不用注入什么呀什么Mapper对象也不用再写这些方法非常方便啊非常方便那这些东西做完之后呢咱怎么测试呢对吧怎么证明呢那你接下来就写测试类呗写测试类的时候呢在测试类当中注入这个Service你就调到它里边方法哎只要也能进行增伤改善不就OK了是不是那咱接下来写测试类这个测试类呢在这写好了啊就是test user Service在这里边呢我们进行测试就行先来个测试方法
[06:07] public void咱先测试个啥其实增加感察我们挑一个就行了比如说 insert 或 save 都行对不对这里边怎么玩你要注意我们是不是得先把业务层给它干什么注进来你才能测试add out to worldprivate user Service其实这个时候相当于我们这个测试类是不是相当于是 Controller 对不对
[06:44] 猪的腰层当然呢我们刚才大家看到这个腰层是不是写的异常简单对不对里边几乎都是什么呀空的但实际上它不会空然后呢然后就该调用方法了呀有学生说老师这有方法吗对不对我这个心里没底啊感觉这里边都是空的呀我跟他说呢你继承他了嘛他里边有的方案你有没有你也有那都能调什么方案你点一下你瞅瞅呗对不对你瞅瞅你认识的这总有你认识的单词吧get ID应该认识吧
[07:15] get one list 对不对见名之意嘛配给remove哎你看这有个方法叫叫叫叫在哪 save他不叫insert啊右层复装完之后他叫save那上面代码你应该能猜到是写啥的吧自己造一个优点对象呗对不对然后呢把它扔到这这就完成了插入或者完成了什么呀保存就这么简单曹操一啊那咱们接下来走一下试试走哎抱错了抱
[08:00] 错了他说啊他说什么呀他说什么不止一个好稍等一下啊我们看这是哪写错了吗是不是少加注解了吧我们看一看我们是不是少加了这个ad Service这个注解给忘记了啊这你不加你在这个用的时候怎么可能注进来啊是不是他也不能倒包啊怎么办啊然后你在这是不是才可以注进来使用吗咱再走一次试试
[08:44] 这次绿了是不是啊证明执行成功了你看跟之前效果一样吧但是我们是不是更省事了是不是啊然后咱去表里边瞅一瞅刷新曹操一对吧没错然后呢其他方案就不再演示了都一样吧你保存能成功其他都一样吧咱简单一点有你看这个根据主件查询的叫get by id然后这个什么呀根据主件进行更新的叫upd by id根据主件进行删除的叫remove by id等等等等
[09:13] 啊好包括其他方法你点一下自己查一查就行了啊因为这一块比较简单只需要大家明白啊MP呢他对业务层也进行了封装非常的贴心啊是我们的好基友啊可以让我们的开发效率非常非常的高对不对当然呢如果说这个你开发的时候根据需求啊这个你要实现的这个功能的确是他里边没提供的那你跟之前一样你该注入Mapper注入Mapper该自己定义方法自己定义方法啊该自己实现该怎么着怎么着
[09:43] 这个我们要跟大家说清楚这是MP对叶子层的封装我们就说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 MyBatis-Plus 框架实现用户服务层的接口定义、实现类编写及单元测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了项目结构目录，包含 Service、Mapper、pojo 等包。
- 代码编辑器中显示了 UserServiceImpl 类的片段，包含 @Autowired 注解和 save() 方法。
- 代码片段：public class UserServiceImpl { @Autowired private UserMapper usermapper; public void save() { usermapper.insert(...); } }

画面2：
- PPT 页面内容，讲解 MyBatis-Plus 的 Service 接口实现。
- 代码片段：public interface UserService extends IService<User> { }

画面3：
- IDE 中显示 UserService 接口定义，位于 cn.itcast.mp.Service 包下。
- 代码片段：public interface UserService extends IService<User> { }

画面4：
- IDE 中显示 ServiceImpl 类的源码，展示其继承结构和方法。
- 代码片段：public class UserServiceImpl extends ServiceImpl<UserMapper, User> implements UserService { }

画面5：
- IDE 中显示 UserServiceImpl 类的继承结构，包含 ServiceImpl、UserMapper 和 UserService。
- 代码片段：public class UserServiceImpl extends ServiceImpl<UserMapper, User> implements UserService { }

画面6：
- PPT 页面内容，讲解测试类的编写。
- 代码片段：@RunWith(SpringRunner.class) @SpringBootTest public class TestUserService { @Autowired private UserService userService; @Test public void testInsert() { User user = new User(); user.setEmail("123@itcast.cn"); user.setAge(301); user.setUserName("cacao1"); user.setPassword("123456"); } }

画面7：
- IDE 中显示 TestUserService 类的代码，包含 @Transactional 注解。
- 代码片段：@Transactional @Test public void testInsert() { }

画面8：
- IDE 中显示 TestUserService 类的完整代码，包含 import 语句和测试方法。
- 代码片段：import cn.itcast.mp.Service.UserService; import org.junit.runner.RunWith; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.boot.test.context.SpringBootTest; import org.springframework.test.context.junit4.SpringRunner; @RunWith(SpringRunner.class) @SpringBootTest public class TestUserService { @Autowired private UserService userService; @Test public void testInsert() { } }

画面9：
- IDE 中显示 TestUserService 类的测试方法，调用 userService.save()。
- 代码片段：public void testInsert() { userService.save(); }

画面10：
- IDE 中显示测试结果，测试失败，日志显示 HikariPool-1 关闭连接。
- 日志片段：HikariPool-1 - Closing connection with mysql.jdbc... Process finished with exit code -1

画面11：
- IDE 中显示测试失败的原因，提示 UserService 类未被 Spring 容器管理。
- 错误信息：Caused by: org.springframework.beans.factory.NoSuchBeanDefinitionException: No qualifying bean of type 'cn.itcast.mp.Service.UserService' available: expected at least 1 bean which qualifies as autowire candidate

画面12：
- IDE 中显示测试通过，日志显示 Spring 测试上下文缓存统计和 HikariPool-1 关闭连接。
- 日志片段：Spring test ApplicationContext cache statistics: DefaultContextCache#ff6a76d size - 1, maxSize - 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

