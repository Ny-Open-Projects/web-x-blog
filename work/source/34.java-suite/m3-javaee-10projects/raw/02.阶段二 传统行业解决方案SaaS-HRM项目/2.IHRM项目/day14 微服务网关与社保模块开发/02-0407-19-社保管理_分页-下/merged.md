# 19-社保管理：分页-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\19-社保管理：分页-下_【海量资源尽在 ubkz.com】.mp4
- 时长 11分27秒（音频 687s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了我们说过了对于咱们查询这个分页结果的话正常的情况其实是要借助微服务去得到用户数据接着再去查目设法但是由于我们数据库表呢其实放到一起了我们这边就不需要太去做这个复杂的操作所以这边的这种方式是我们推荐的但是咱们是教学目的所以我们这边说的稍微简单一点好了这边先不报错我先返回一个那那进来呢就是观察一下我们这个页面显示
[00:33] 好切换到我们的页面这边来看那我们左侧的这边呢其实是我们的用户的所有数据那右侧这边其实才是他还设保的一些参保的一些数据那我们都知道用户是肯定都存在的用户其实就是他的所有员工那对于这个新用户而言后边这些数据是不是目前来说还没有啊那所以我查询的结果左侧所有用户都必须有而这些参保数据可有可无所以这边涉及到两个表
[01:02] 以外连接的形式来查询没错吧所以这边呢咱们先把这个色候语句呢给它写出来那这边呢我打开我的色候样OK在里面呢咱们可以写一下色候语句那我们简单的来看一下一个表呢是我们的所有拥表BS另一个表呢就是我们这边关注的它这个社保的这个表userscottyscriti两张表那我们来以谁
[01:32] 为查询的依据是不是就以user来查询因为我们说过了左侧必须有所以我们查询的是所有用户那select新frombs下滑线user好了那接着左外连接leftadjoin去连接我们这张表ss下滑线user下滑线再来socal下滑线seOK这边直接有提示了好那接着他们两个连接的依据是什么我说一下
[02:02] 用户里面有ID代表的是用户ID那在这边呢还有一个就是我们这个社保这张表那社保这张表呢它的主件就是user ID所以我们连接的依据就是on前面起一个别名比如说叫user就叫u吧这边起一个米别名叫s那我们on的就是u.id等于s.user小号件ID没错吧好了那接着我们来看一下查询结果
[02:32] 好了这样一来呢各位会发现所有用户的数据都已经有了但是啊针对底下这几个用户好像就没有社保的这些设置没错吧那别忘了我们是一个SaaS系统后面呢再去加一条件where compy小型ID等于我们可以来一个1当然了这个企业ID呢是不是在哪个表其实是无所谓的这些表里面都有啊company ID我们就来一个等于1来试一下OK好了那这样一来
[03:04] 我们的数据呢就已经查出来了但是别忘了我们这边呢除了这个之外呢咱们是不是还涉及到要进行分页啊所以咱们的问题就又来了咱们要完成这个circle的一个查询我们需要自己去写分页并且呢要去设置他的什么他的分页的查询的这种规则那我们怎么办呢其实很简单在SpringData JPA这边啊
[03:31] 咱们可以在do当中写一个方法好了各位来看一下那至于这个方法呢就是使用就是基于就是circle的分页那基于这个circle的分页首先呢这边要跟各位说明一下好了我们这个方法那方法的这个返回值呢返回值注意这是一种约定这个方法的返回值呢就是page
[04:00] 那配置里面可以写的是你的一个对象你想要封装成什么样的对象进行分页就写这个对象那接下来的方法名叫什么无所谓我们可以起来试一下public好了我起一个方法publi public public page类型的反围值注意别选错包sprint封装的这个配置对象那里面究竟是什么范型我们一会再说起一个名字就叫做fender page
[04:31] 接下来这里面的参数第一个就是我们的死局类型的companyID我们刚才说过了是要根据企业ID查接下来还有注意我们要基于这种circle的这种分页的话这边还有一个参数是必不可少这边有一个参数这个参数就是pageable这么一个对象这个对象里面封装了就是分页的这些参数比如说我们的page和size其实跟我们那种specialization
[05:02] 分页其实差不多也需要这么一个参数那么这个参数呢也给它定义上pageable好了起一个就叫pageableOK好那接下来呢有的朋友说啊写到目前这种程度那这个circle语句写到什么位置那注意我们可以就是circle语句那circle语句就是使用at query去编写circle语句好了我们可以一起来试一下
[05:32] 那注意我们写的是sql语句那里面有一个native query我们就应该改成true这个描述的是我们要自己编写sql语句那还有就是有一个value属性value属性指的是我们的sql语句究竟是什么其实sql语句就在这边摆着直接call过来就可以了当然了对于分页而言其实还有一个就是必不可少的一个说明是什么呢就是说你如果要做分页是不是有个总记录条数
[06:00] 那这种query的形式进行查询点到注解里面看value指的是你要执行搜索语句count query那count query指的是你要统计总数它的搜索语句所以对于我们而言很简单了别忘了分页也有查询数据列表的语句还有我们统计总数的语句所以我们可以使用count query来进行统计count query拿过来那我们这个count query这个语句呢也是比较简单的
[06:27] 其实就是在我们刚才查询的这个结果之上把这个星是不是改成Count星就可以了OKCtrl C把这个拿过来那注意啊刚才我们后边有一个Community ID这个是写死的这回我们就可以以站位符的形式来进替换第一位是我们的Community ID那当然了还有一个SOHO语句在上面Value那这个Value呢其实我们这个SOHO语句您往这注意啊就应该是星啊
[06:55] 那各位你看这个星啊查询的字段就实在是太多了那我们要什么就是页面上显示什么我们是不是查什么就更加合适啊那这是第一个第二个我们要把这个对象封装成什么类型的对象注意就是配置里面装的是什么样的范形注意我这边为了简单我用一个map集合那这个map集合那是怎么进行体现出来的回到我们的思考语句一起来看一下好了那注意
[07:23] 那如果是使用这种MAP集合的返回值的话它会帮我们组装成一个一个MAP其中MAP的key代表字段MAP的value代表是当前这条记录的数据所以呢我这么一条它会帮我封装成一个MAPMAP的key有ID有mobile有username有password等等等等各位应该能够理解好了其实这个就是跟我们对象的那些参数是一致的只不过换了一种形式用MAP来描述了
[07:53] 其实代表的是对象的属性名只不过现在替换成MAP当中的KEY而已它最终通过JSON转化效果是一模一样可以吧好那接下来呢咱们就开始来看一下那我们都知道啊咱们这边要查询的是有ID有Mobile来看一下好了有姓名手机公号部门姓名呢我们就是B就是U点UserName
[08:25] 姓名好了当然除了这个之外呢还有很多这边我就不啰嗦了我已经在今天资料当中把这个搜索语句给各位准备好了OK好了我们一起找到今天这个资料在今天的资料里设法模块相关有这么一个搜索语句把这个搜索语句呢直接Ctrl C拿过来贴到我们这边一起来执行一下看效果好了这样一来就能得到我们最终的这个产业结果需要各位注意的是我们这回得到的这一个一个的字段啊
[08:56] 这些字段是我们请求接口所需要的所以我就做了一个小小的字段转型名字的一个别名的一个配置都是比较简单的需要哪个字段我就给它起一个别名而已好那接下来把这个社会句Ctrl C贴到这边好了找到我们的DU里面放到value这边靠过去
[09:21] 这样一来我们这个语句就已经写好了那在我们的survey层呢就可以调用的do完成整个代码的一个逻辑啊好了do点我们叫做fender page那fender page需要把company id传递进去那注意第二个呢还需要一个对象那这个对象呢各位肯定不陌生分页咱们之前都玩过好了比如说呢咱们之前随意找一个工程里面都有分页的这种逻辑在里面
[09:54] 比如说随便来一个咱们之前写过的这个没有这个也没有我们找一个肯定有的吧在user当中Service层user Service好了其实需要的就是这么一个配置对象就是它Ctrl C把这玩意Ctrl V拿过来咱们做一个修改配置后面第二个就是配置那注意这样一来它也会得到一个分页对象这个范形我们不需要了
[10:29] 那得到的这个分页对象的不是我们所需要的配置result所以我们需要自己构造一个配置result出来好了这个构造的规则各位应该还记着第一个.getTotalElements代表的是总数.getContents代表的是我们的数据列表好了那这样一来我们这个相应的分页的逻辑就已经写好了那在这边我们重新启动一下我们的微服务
[10:56] 好了找到页面部分咱们耐心等待一下它启动成功看一下我们最终的结果好了这个启动还是有点慢各位耐心等待一下回到这边刷新来试一下刷新各位来看现在的数据呢其实就已经出来了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过自定义 SQL 查询和分页功能，实现对用户社交数据的查询，并最终在前端页面展示分页结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IntelliJ IDEA 中，展示 `UserSocialService.java` 文件，其中 `findALL` 方法调用 `userSocialSecurityDao.findPage`，并使用 `PageResult` 包装返回值。
画面 2: 在 SQLyog 中，执行 SQL 查询 `SELECT * FROM hs_user LEFT JOIN ss_user_social_security ...`，查询用户社交数据。
画面 3: SQLyog 查询结果展示，显示了多条用户记录，包含用户名、手机号、部门、入职时间等字段。
画面 4: 在 IntelliJ IDEA 中，展示 `UserSocialSecurityDao.java` 文件，其中 `Page<T>` 类型的返回值被选中，用于定义分页方法。
画面 5: 在 IntelliJ IDEA 中，展示 `UserSocialSecurityDao.java` 文件，定义了 `findPage` 方法，使用 `@Query` 注解。
画面 6: 在 IntelliJ IDEA 中，`@Query` 注解的 `nativeQuery` 属性被设置为 `true`，并准备编写 SQL。
画面 7: 在 IntelliJ IDEA 中，编写了 `@Query` 注解的 `value` 属性，用于查询用户社交数据的 SQL。
画面 8: 在文件资源管理器中，展示项目结构，`SocialSecurityController.java` 文件位于 `Controller` 目录下。
画面 9: 在 SQLyog 中，执行 SQL 查询 `SELECT bu.username, bu.mobile, ...`，查询用户社交数据。
画面 10: 在 IntelliJ IDEA 中，编写了 `findPage` 方法的完整 SQL 查询语句，包含 `SELECT` 和 `LEFT JOIN`。
画面 11: 在 IntelliJ IDEA 中，展示 `UserService.java` 文件，其中定义了 `findUserByMobile` 方法和 `departmentFeignClient` 字段。
画面 12: 在 IntelliJ IDEA 中，`UserSocialService.java` 文件中，`findPage` 方法的返回值被设置为 `PageResult`。
画面 13: 在 IntelliJ IDEA 中，展示项目结构，`SocialSecurityApplication.java` 文件位于 `src/main/java` 目录下。
画面 14: 在浏览器中，展示前端页面，显示了分页查询结果，包含用户信息和分页控件。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.ihrm.social.Service;
import ...
@Service
public class UserSocialService {
    @Autowired
    private UserSocialSecurityDao userSocialSecurityDao;
    //分页查询用户的社交数据
    public PageResult findAll(Integer page, Integer pageSize, String companyId) {
        //需要借助Feign调用远程服务获取用户的数据
        //直接获取社交数据信息
        return ;
    }
}
```

画面 2:
```sql
SELECT * FROM hs_user LEFT JOIN ss_user_social_security s ON u.id = s.user_id WHERE company_id=?
```

画面 3:
```sql
SELECT * FROM hs_user LEFT JOIN ss_user_social_security s ON u.id = s.user_id WHERE company_id=?
```

画面 4:
```java
public Page<T> findPage(String companyId, Pageable pageable);
```

画面 5:
```java
@Query
public Page findPage(String companyId, Pageable pageable);
```

画面 6:
```java
@Query(nativeQuery = true,
       value = "",
       countQuery = "")
```

画面 7:
```java
@Query(nativeQuery = true,
       value = "SELECT COUNT(*) FROM hs_user u LEFT JOIN ss_user_social_security s ON u.id = s.user_id WHERE company_id=?1",
       countQuery = "SELECT COUNT(*) FROM hs_user u LEFT JOIN ss_user_social_security s ON u.id = s.user_id WHERE company_id=?1")
public Page findPage(String companyId, Pageable pageable);
```

画面 8:
```
Controller
├── SocialSecurityController.java
```

画面 9:
```sql
SELECT bu.username, bu.mobile, bu.work_number, bu.department_name, bu.time_of_entry, bu.time_of_dimission, bu.participating_in_the_city, bu.participating_in_the_city_id, bu.providing_fund_city_id, bu.providing_fund_city_name, bu.social_security_base, bu.social_security_base_id, bu.providing_fund_base FROM hs_user bu LEFT JOIN ss_user_social_security ss ON bu.id = ss.user_id WHERE company_id=?
```

画面 10:
```java
@Query(nativeQuery = true,
       value = "SELECT bu.id, bu.username, bu.mobile, bu.work_number, bu.department_name, bu.time_of_entry, bu.time_of_dimission, bu.participating_in_the_city, bu.participating_in_the_city_id, bu.providing_fund_city_id, bu.providing_fund_city_name, bu.social_security_base, bu.social_security_base_id, bu.providing_fund_base FROM hs_user bu LEFT JOIN ss_user_social_security ss ON bu.id = ss.user_id WHERE company_id=?1",
       countQuery = "SELECT COUNT(*) FROM hs_user bu LEFT JOIN ss_user_social_security ss ON bu.id = ss.user_id WHERE company_id=?1")
public Page<Map> findPage(String companyId, Pageable pageable);
```

画面 11:
```java
@Service
public class UserService extends BaseService {
    @Autowired
    private UserDao userDao;
    @Autowired
    private RoleDao roleDao;
    @Autowired
    private IdWorker idWorker;
    //根据手机号查询用户
    public User findByMobile(String mobile) { return userDao.findByMobile(mobile); }
    @Autowired
    private DepartmentFeignClient departmentFeignClient;
    //批量保存用户
}
```

画面 12:
```java
return new PageResult(page.getTotalElements(), page);
```

画面 13:
```
src/main/java
├── com.ihrm.system
│   ├── client
│   ├── Controller
│   ├── dao
│   ├── Service
│   ├── constant
│   ├── domain
│   └── vo
└── SocialSecurityApplication.java
```

画面 14:
```
// 前端页面内容
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

