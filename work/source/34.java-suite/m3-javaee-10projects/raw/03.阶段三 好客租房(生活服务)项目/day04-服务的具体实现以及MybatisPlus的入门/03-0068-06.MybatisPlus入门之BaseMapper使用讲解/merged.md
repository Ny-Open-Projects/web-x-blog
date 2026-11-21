# 06.MybatisPlus入门之BaseMapper使用讲解

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\06.MybatisPlus入门之BaseMapper使用讲解【海量资源尽在 ubkz.com】.mp4
- 时长 18分40秒（音频 1120s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下BaseMapper那么在我们前面所实现我们的一个快速入门的时候呢我们也使用了这个BaseMapper是不是我们写了一个UserMapper来继承这个BaseMapper那么当我们去继承BaseMapper之后呢我们其实也就拥有了BaseMapper中所定义的一系列的一些CLUD的一些方法
[00:23] 那么OK这个BaseMapper以后我们会经常会用到所以我们在这去单独的再来把它去给大家去讲一下那么在这需要特别说明的一点是在BaseMapper中它所定义的一些方法仅适用于什么单表的一些操作这个也要注意比如说我们查询一张或者说操作一张用户表还有一些item表是单表的操作OK
[00:48] 那么这个呢就是base Mapper那么下面我们来看一下在base Mapper中所定义的一些方法那么比如说呢你可以看到在这儿有一个什么insert的方法有什么delete by id啊还有delete by map还有delete操作啊等等然后呢它所定义的一些都是一些基本的一些clud的操作包括呢像后面还有一些呢是什么呢select配置是不是做什么呢做分页查询ok然后呢
[01:16] 这个select maps page这个也是做一个分页那么接下来呢我们就来给大家来演示一下这个base Mapper的一些基本的一些操作啊那么你比如说我们可以去通过ID做一个查询那么怎么查询呢来看一下public来一个word来一个什么呢test selectorby什么呢ID然后呢我们在这个位置呢去来一个test好在这呢我们就通过什么呢
[01:46] this.urlmap.select by id那么通过这个id呢我们给它去select by id去做通过id做一个查询那么我们来看这张表里面的id那么id它的类型是bigint的类型那么也就是说在我们的代码中我们使用这个要使用这个什么呢L是不是lang类型ok那么我们来看一下这里面有哪些数据呢有这么多数据对吧那么我们尝试查询一下tom这条数据那么它的id为3那么所以给它一个3
[02:16] 那么我们把这个结果拿到打印出来就是U的好那么我们来测试一下是否能够查到Tom这条数据呢那么我们来等待他去做一个执行来看一个效果好那么我们可以看到是吧我们已经成功的查询到了这个Tom这条数据所以这个方法是吧OK的好那么接下来我们来演示一下其他的查询那么叫什么非ID的查询那么其实这种非ID的查询呢
[02:44] 就是怎么的通过这个上面这种方法叫做slag list做查询那么我们来先测试一个比如说像like查询ect by什么呢like通过like去做一个查询那么这个应该怎么查呢那么我们就需要这么来玩this.yaml.什么呢select list我们要去使用的是这个方法
[03:12] 然后我们可以看到它是不是接收的是一个什么的rop这样的一个对象也就是我们的queryrop就是一个query的一个包装对象对吧好我们来看一下这个rop对象怎么去构造那么select我们来看一下select什么list那么我们给它去传递一个什么传递一个rop那么这个rop我们看来我们来看一下
[03:41] 他到底是什么样的一个对象啊他是一个抽象类对不对那么OK那我们就在这个位置给他定义一个那么抽象类他一定是什么呢一定是不是要有选择一下啊我们选择他啊那么叫drop吧然后呢他等于什么呢等于我们去new一个什么呢要注意那么抽象类是不是不能直接去new他一定有具体的实现类对吧
[04:10] 那么我们使用这个叫query-rop那么来看一下这query-rop怎么玩呢把这个rop传递给他好那么query-rop怎么玩是不是rop点什么呢是不是我们可以设置一个什么呢是不是like操作看到了吗是不是like操作那么我们可以调用这个方法对吧设置一个colon是不是就自断哪个自断like什么值是不是这样的一个设置所以我们给他来一个什么呢like操作
[04:40] 到这个位置来一个like操作那么like什么呢好那么like操作那么like我们来找一下like操作的这张表里比如说我们就名字名字名字中包含了包含了什么呢包含了这个o这个字母的这个人包含了o这个字母这个人我们来看一下他拿到有哪些数据呢那咱们就那就那就这样
[05:15] 这个不需要打返回值了是不是做了设置就可以了OK这个不需要做强转这个like操作是它的抽象内中没有的这样的一个方法那这样咱们这么定义好这么定义好这样的话是不是我们就可以看到是不是可以设置一个like操作对吧然后我们来看它的返回的一个值对吧返回值
[05:40] 那么我们你看这个位置并没有一个user对象对吧user对象那么这个时候呢我们就需要给它设置一个范形user设置一个user然后呢这个地方呢也是设置一个user好那么这样的话我们做了一个这个操作好嘞那么我们接下来呢还是用一个复循环我们把它去迭代出来然后呢来一个什么呢user来测试一下走
[06:12] 好那么我们其实呢也可以看到对吧那么他是不是就把这个名字中包含了这个欧的这个用户是不是就查询出来了OK这个呢就是一个lag操作当然了还有一些其他的一些操作对吧比如说像这种条件的操作比如说我们可以设置这个年龄小于20小于20的这样的操作那么这样咱把这个call一下掰什么呢LE对吧就是小于
[06:44] 那么我们来看一下他这个rop点什么呢小于什么呢谁小于谁呢比如说age年龄小于20的这个用户把它查询出来测试一下这个大家应该能够理解吧比如说我们是构造了一个查询的条件条件呢就是年龄小于20来看一下那么小于20的小于等于20的就是这个18 20那么我们来看一下数据对不对18 20OK
[07:15] 那么其他的三个都是大于20岁的好嘞那么就把这个小于等于这个20的用户是不是就查出来了那么通过这个链接呢大家可以去看一下那么它其实有很多的一些这个构造器对吧或者是构造这个wrap那么呢在这个wrap中呢构造有很多啊大家可以去看一下比如说像这个EQ就等于谁呢等于谁比如说这个name老王就是名字等于老王的这个还有only
[07:45] N呢就是不等于不等于老王的这个查出来那么这个GT呢就代表是大于那么GE呢是大于等于LT呢是小于LE是小于等于我们刚刚使用的是不是这个还有什么呢还有这个像一些什么like操作啊还有一些什么is not a not a not a硬啊等等一些系列操作啊这个硬操作我们后期是不是也可能会用到对吧OK
[08:13] 好那么更多的内容呢大家可以自行去阅读一下这个文档啊这个里面讲的也是非常的详细好那么这个就是我们相关的一个这个操作啊下面呢还有一些这个插入数据那么我就不去敲了啊我们直接把它拷过来我们来看一下它的一个测试吧那么我们来测试的这个是一个C5操作也就是我们要执行一个insert的这个操作那我们来看它是否能够成功的就插入进去呢我们执行走
[08:43] 那么等待他的一个执行的完成那么这个时候呢我们会发现他告诉我们说这个新增数据是不是成功了对吧好那我们来看一下有没有数据有没有写到表里面的有没问题是不是已经写到表里面去了但是大家要注意了那么在这个位置他的这个ID显然是不是有问题对吧那么他的ID应该是什么应该是6而不是这么一长段对吧那么这个显然是我们的这个ID的一个字叫
[09:12] 组件的一个生成的策略配置的有点问题那我们需要给他去设置一个至增长的ID那么我们就需要给我们这个User的ID上面去添加这样的一个注解叫做table ID那么我们找到User对象在这个User对象上面呢给他去添加一个这个叫table ID并且指定他的一个type呢就是ID type是autoauto呢就是做一个什么做一个至增长对吧做一个至增长那么这个
[09:41] plus这个框架呢就不参与这个ID的一个这个生成那么让数据库做一个自增长就可以了好那么接下来呢我们得还得这么去测啊要注意我先把这条数据呢给它删除掉然后呢要注意的是这里刷新一下看一下啊这张表的一个自增长的ID的值已经是变得很大了我们来看一下自增长ID哦他哦这个并没有设置自增长
[10:10] 对吧并没有设置自增长那么这样我们来给他设置一个自增长怎么设置呢在这个位置我们给他设置一个自动增长这个表结构中他并没有自增长所以我们来给他打个勾好那么我们再来做一个测试再来做一个测试当然了我们先这么去测一下我们先把这个注解先给他拿掉然后呢我们先在表中的给他设置一个自增长我们来看一下他的效果会怎么样
[10:39] 我们刷新一下这个大家能够理解吧那么我先把表的这个它的结构我们就改一下改成什么呢至增长那我再来做个测试我们来看一下它是否能够完成一个至增长的一个动作我们测试一下等待它的一个执行来看一下那么数据插入成功了那我们到这个里面表里面来看一下它的数据走你会发现对吧那么这个依然是有问题的对吧依然是有问题的
[11:09] 好那么接下来我们就要去给它调一下首先第一步你把这个优势中的这个注点打开好那我们设置它的一个ID的type呢就是叫autom就是自增长这种类型然后呢我们来刷新一下看一下这张表这张表呢我们可以看到它的一个自增长的一个值已经跑这么大了对吧所以这显然是有问题的我们给它调一下那么目前呢我们先把这条数据给它删掉
[11:36] 那我们自增长的值应该到几呢是不是应该到6才对啊所以呢我们在这个里面呢给它设置一个这个6这回就对了啊设置一个6保存一下哎OK6这就对了那么我们到这个里面刷新一下那么来看一下它的自增长的ID的值是不是就是6啊哎OK好然后呢我们回到刚刚的一个测试用力中我们再来做一个执行走那我们来看一下它最后的插入的一个结果会是怎么样的
[12:03] 那么是否是我们所期待的这个6呢对吧好来刷新看一下效果然后走那么可以看到这回是不是就正常了对吧当我们再次执行它插入的数据是不是就变成7了呢我们来看一下等待它的一个执行好那么到这个里面刷新走是不是就变成7了哎呀ok所以呢我们这样的话是不是设置了自身的ID哎这样就ok了对吧好那么接下来我们继续往下面看那么我们来测试的去删除一条数据
[12:31] 那么我们怎么删除呢我们首先呢通过这个ID去做一个删除你比如说我现在想要把这个ID为7的这条数据给它删除掉那么能不能删除掉呢走test这个deletedelete操纵来执行等待它的一个执行的完成好那么我们可以看到现在呢已经是删除成功了对吧好那我们刷新看一下效果那么那条数据是已经被删除了哎OK好没有任何问题那么我们接着继续往下面测试
[13:00] 那么我们来测试的是一个叫做update那么毕竟我们要测试的是一整套对吧CLUD嘛好那么我们来看一下这个update它是否能够去修改成功呢就是我们现在呢想要把这个ID为6的这个用户修改它的名字是什么呢修改名字为李四原来是什么呢我们来看一下原来是张三那么我们现在要把它改成李四并且我们设置它的一个什么呢就是update by ID是不是根据ID做一个修改
[13:29] 那么ID这个6将变成它的一个什么呢条件是不是就Val ID等于6然后update去修改这个内容那我们来看一下它是否能够去成功修改那么要注意的是我仅仅是不是给它设置了内容这个字段那么我们需要看两个内容第一个呢就是它的名字能不能改成李氏第一个内容第二个内容呢就是
[13:52] 这个内幕这个这个优势中的其他的一些字段是否会被制空呢我们来看一下效果刷新走那么我可以看到是不是只有这个字段做了修改其他字段并没有任何的一些改变也就是说他的一个修改就是什么呢修改的是
[14:10] 不为弄的制段作为我们的一个修改数据而我们的ID作为的是一个什么呢作为的是一个更新的条件啊更新的条件哎OK好这个呢就是做一个update啊好那么接下来呢我们来给大家演示一个这个分页查询啊分页查询那么分页查询呢他需要是这么来玩就是说我们想要去有分页呢我们首先得要在我们的这个环境中啊
[14:38] 给它添加一个分页的一个插件那我们把这个代码我们call一下拷贝到我们的这个启动内中然后在这个里面呢写一个这个bin写一个这个bin这个注解那么是不是就会向我们的Sprite容器中注册一个这个配置了这样的一个叫intercept是不是一个拦截器那么其实也就是一个分页的一个插件
[15:04] 好那么第一步我们把这个搞定那么第二步呢我们来看一下它的一个测试那么就需要我们去通过一个叫做select什么select page这样的一个方法去做一个查询那我们进入到我们的测试用例在测试用例中呢我们把这个方法靠过来我们来看一下它的一个写法那么我们要通过这个this.u的map select page去调用这个方法去做一个查询而这个方法呢可以传递两个参数
[15:33] 第一个参数呢是配置第二个参数呢就是我们那个查询条件那么这个配置呢我们通过定义一个配置这个对象然后呢设置它的一个这个是不是叫当前的一个页数对吧然后呢set代表的是每一页显示几条数据OK而后面的这个参数呢就是我们的一个
[15:53] 查询的一个条件那么这个是不是就跟我们上面这个写的是一样对吧你可以根据什么呢用户的年龄或者说做一些like操作或者做一些其他的一些操作那么都可以去构造一个我们的一个参数OK那么我们现在这个测试用力中的并没有设置这个参数那么只是给他设置了个分页效果我们来看一下那么下面呢通过这个返回值叫做user一个pager这样的一个对象那么就可以拿到他的一些相关分页的一些数据比如说总条数啊
[16:22] 当前的页面数当前页数然后每页显示的数据每页显示的一个数量对吧就是这个二对吧好那么拿到拿到拿到这个拿到的一个这次分页返回的一个数据然后把它打印出来那我们来测试一下看一下它看它是否能够完成一个分页的一个效果那么我们来看一下那么现在它所查询的就是就是什么呢来看一下那么当前页是一当前页是一
[16:51] 我总共呢要去拿两条数据那么也就是说我总数据是几条呢六条没有问题对吧那么当前月是几呢一然后呢总共每月显示几条数据呢拿两条数据那么我们先拿的数据呢就是一二没有任何问题对吧好那我们来测试一下那么我当前现成二那么会怎么样那么我是不是就应该拿的是三四啊这条数据啊对吧来走再测试一下看一下它的一个执行的一个效果
[17:16] 那么是否能够拿到这个34这条数据呢来看一下你看是不是拿到34这条数据哎呀OK那么我可以看到它的总条数以及拿到的数据是不是都是OK的没有任何问题所以呢这个分页是不是就搞定了哎呀OK好那么我们把这个呢分页的给大家再来强调一下分页要想玩分页要要有两步操作第一步呢你需要在Sprite的容器中给它注册一个分页的一个插件其实呢它是一个什么的拦截器对吧还是个拦截器
[17:46] 那么第二步呢就需要在我们做查询的时候呢我们需要先构造一个配置这个对象在我们去做查询的时候把这个配置传递进来传递进来然后呢通过XLag的配置去做一个这个分页的一个查询那么你就可以做到一个物理上的一个分页啊OK好那么这个呢就是关于这个base Mapper的一个基本的一个使用啊
[18:12] 那么我们呢就抓了几个典型给大家呢去讲一讲那么这个里面有很多的一些这个方法那我们就不做一一的一个测试了我希望啊同学们去做学习的时候呢可以把每一个方法都去测试一下这样的话呢你就可以做到对这个UrlMapper对这个BaseMapper呢就可以非常熟悉这个里面的一些方法以及它的用法OK好那么关于这个BaseMapper呢我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
 * Mapper 继承该接口后，无需编写 Mapper.xml 文件，即可获得CRUD功能
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

