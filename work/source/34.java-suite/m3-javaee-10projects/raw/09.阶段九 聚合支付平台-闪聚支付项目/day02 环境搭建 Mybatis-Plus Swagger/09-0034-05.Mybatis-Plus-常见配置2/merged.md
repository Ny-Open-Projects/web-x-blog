# 05.Mybatis-Plus-常见配置2

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\05.Mybatis-Plus-常见配置2【海量资源尽在 666java.com】.mp4
- 时长 7分1秒（音频 422s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 另外还有一些配置叫什么叫做别名的配置别名的配置这个我们之前学习MapTest都知道啊那别名是啥意思什么别名啊别名的配置的话其实就是我们准备把POGO里边的这个什么这个类名我们准备在映射文件当中啊就不用写这个路径了如果你配这个这个别名的这个映射那么你就不需要啊你就不需要干嘛
[00:30] 你再写这个全路径的呀你这个全路径是不是太麻烦我就直接可以写个user你看看嘛哎这样也行你不相信试试走所以前提是你在这要配置什么要配置这个别名的这个映射路径对吧它又会自动的去根据你的这个别名找到它对应的user类嗯好然后还有什么呢还有一个叫什么呢叫做是否开启自动驼峰命名这是啥意思
[00:59] 因为大家知道在数据库自断名大家习惯是用这个下滑线来定义看见吗叫user下滑线内幕这user下滑线内幕呢这个mybates它其实是支持一种叫驼峰映射命名的方法它就会自动的把这种下滑线自断下滑线的映射成什么驼峰的这个属性名举个例子现在我的这个user下滑线内幕它对应
[01:28] 我们的这个模型类当中是不是就是这个U的内部那你告诉我它这个是不是就是中间有个下滑线对吧那么MyBetis呢它就会自动的来做这么一件事就是把这个字段映射成什么映射成这种驼峰的方式就是下滑线去掉把这个怎么样这是不是写错了U的内部是吧它就把它这个N变成大写这就是驼峰命名方式
[01:58] 那有时候老师那我该怎么测呢各位我这儿指定了这个table field是不是就是这个属性对应这个子弹了那如果各位如果我把它屏蔽掉如果把它屏蔽掉的话那么现在各位我现在就需要去干嘛我需要去开启这个驼峰命名的方式那么这个时候呢注意它就会自动把字
[02:25] 这个字段当中有这个下滑线的映射成我这个驼峰的这种属性来看一下啊现在我是不是就开启了那么只要你字段当中有这个下滑线的它就会自动的去找你这个模型类比里边符合这个规则的这个驼峰的属性好那现在呢各位我们来看一下你看它能不能映射成功呢怎么判断映射成功呢那只要查出来的这个数据哎已经报错了报啥错
[02:58] 哎抱了个错你看见吧说这个属性这个configuration和这个configure location不能干嘛啊在一起使用看吧那是啥意思哎这个属性我告诉你学习MapleDatePlus的时候遇到的很多你说现在各位你看到我这是不是有一个叫configuration你看见吗对吧而上面我我这个加载的映射文件是不是有一个叫
[03:23] 这个MapTest的这个Configure配置文件就是这两项不能同时使用对吧那怎么办那你肯定要保留一项嘛你要么保留这个MapTest-Configure配置文件就是在这个配置文件里面配要么干嘛要么在你保留这个我们这个Spring Boot这个配置那这边我们选一种我们我们不在这配这种方式了我们在这在这个MapTest-Configure当中来配来配什么来配这个
[03:53] 是否开启驼峰可以吧然后来我们在这呢那怎么配呢这当初学习过mybates各位我们是不是就在这配就OK啊看一下啊好我们加一个注释然后我们我们现在要配的是不是就是它那你是不是把这个参数干嘛你把它拷到这然后这个处呢你把它弄到这是不是就OKmybates当初这个参数我跟你说它是默认是false的就是mybatesplus默认是处了
[04:27] 但是这个参数呢咱们不能这么配啊不能这么配因为你要配的是谁啊其实你就配这一个参数就是这个是我开启这个驼峰命名映射的啊那么你要把它改成这个注意啊就是在Spring Boot里边配的话你可以用这个里边这个短杠不对啊我写错了U是吧这是T然后这是C这是C对吧这就算开启了
[04:59] 这就算开启了那这么开启了之后呢注意开启了之后各位你要注意我的测试的目的刚才我是不是把这个table field给屏蔽了屏蔽那就意味着这个属性就没有办法和我们的字段进行映射对应是吧但是由于你开启了驼峰映射那么mybts plus就会看这个字段名是下滑线这种规则它就会自动找
[05:28] 与它对应的驼峰的属性如果找到了看好运行那你会发现我们就可以把这个user name给查出来user nameuser name注意看是不是就找到了有吧就说明我们这个开启这个驼峰映射是不是有效理解吗那有时候老师如果你关闭呢对如果我要是关闭了我告诉你它就映射不成功你不相信试试因为什么因为它又不知道你这个规则吗
[05:58] 你看大家看懂吗对不对所以这就是我们说的驼峰映射对吧驼峰映射默认的MacBatis Plus是开启的那这里边我要强调一点的是什么呢就是说你会发现我们有些字段是符合驼峰映射规则的有些呢它是不符合的那有时候老是符合的我们是不是就不用加这个table field那不符合的我们是不是要加上table field那基于这种情况我其实都建议你加
[06:29] 因为这样你的代码可动性更强大家理解了吗好这就是我们说的开启驼峰映射的配置以上我们讲了四个配置一个是指定mypages-configure的配置一个是指定Mapper文件的配置Mapper映射文件的配置一个是指定
[06:48] 别名扫描的这个路径的配置一个是开启托付映射的配置这四项呢是非常常用的那我们就暂时讲这四项然后呢基于更详细的买杯TESLA PLUS的配置呢大家可以访问这个网址好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 MyBatis-Plus 的配置项 mapUnderscoreToCamelCase 的作用及如何通过配置文件解决字段映射问题。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 MyBatis-Plus 的配置项 mapperLocations 的说明，以及项目结构中 UserMapper.java 和 UserMapper.xml 文件的路径关系。
画面2: 展示了 application.properties 文件中的 MyBatis-Plus 配置，包括数据源、配置文件路径、映射文件路径和类型别名包。
画面3: 展示了 UserMapper.xml 文件中的 SQL 查询语句，以及测试类 UserMapperTest 中的测试方法。
画面4: 展示了 MyBatis-Plus 的配置项 mapUnderscoreToCamelCase 的说明，包括其类型、默认值和注意事项。
画面5: 展示了 application.properties 文件中的 MyBatis-Plus 配置，包括数据源、配置文件路径、映射文件路径和类型别名包。
画面6: 展示了 User 类的 Java 代码，其中包含 @TableField 注解来指定字段名。
画面7: 展示了测试失败的日志，提示 Property 'configuration' and 'configLocation' cannot be specified with together。
画面8: 展示了 application.properties 文件，其中配置了 MyBatis-Plus 的类型别名包。
画面9: 展示了 mybatis-config.xml 文件中的配置，包括 mapUnderscoreToCamelCase 设置为 true。
画面10: 展示了 User 类的 Java 代码，其中包含 @TableField 注解来指定字段名。
画面11: 展示了测试通过的日志，显示查询结果。
画面12: 展示了 mybatis-config.xml 文件中的配置，包括 mapUnderscoreToCamelCase 设置为 false。
画面13: 展示了 User 类的 Java 代码，其中包含 @TableField 注解来指定字段名。
画面14: 展示了 MyBatis-Plus 的配置项 mapUnderscoreToCamelCase 的说明，包括其类型、默认值和注意事项。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面1:
mapperLocations即MyBatis Mapper 所对应的 Mapper配置文件位置，如果您在 Mapper 中有自定义方法（XML 中有自定义实现），需要进行配置，告诉 Mapper 所对应的 XML 文件位置。
如果不配置mapperLocations时，Mapper的xml文件存放路径需要和Mapper class文件保持一致，文件名保持一致，如下：
画面2:
spring.datasource.driver-class-name=com.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/mp?useUnicode=true&characterEncoding=utf-8
spring.datasource.username=root
spring.datasource.password=mysql
#指定mybatis-config.xml配置
mybatis-plus.config-location = classpath:mybatis/mybatis-config.xml
#指定Mapper文件位置
mybatis-plus.Mapper-locations = classpath:mybatis/Mapper/*.xml
#类型别名包
mybatis-plus.type-aliases-package = cn.itcast.mp.pojo
#日志配置
logging.level.root: debug
画面3:
<select id="findId" resultType="User" parameterType="java.lang.Long">
    select * from t_user where id = #{id}
</select>
画面4:
类型：boolean
默认值：true
是否开启自动驼峰命名规则（camel case）映射，即从经典数据库列名 A_COLUMN（下划线命名）到经典 Java 属性名 aColumn（驼峰命名）的类似映射。
注意：
在 MyBatis-Plus 中此属性默认值为true，用于生成最终的 SQL 语句
如果您您的数据库命名符合规则则无需使用 @TableField 注解指定数据库字段名
测试：
#开启自动驼峰映射，注意：配置configuration.map_underscore_to_camel_case则不能配置config_location
mybatis-plus.configuration.map_underscore_to_camel_case=true
画面5:
spring.datasource.username=root
spring.datasource.password=mysql
#指定mybatis-config.xml配置
mybatis-plus.config-location = classpath:mybatis/mybatis-config.xml
#指定Mapper文件位置
mybatis-plus.Mapper-locations = classpath:mybatis/Mapper/*.xml
#类型别名包
mybatis-plus.type-aliases-package = cn.itcast.mp.pojo
#日志配置
logging.level.root: debug
画面6:
@TableId("id")//指定主键的字段名
private Long id;
// @TableField("user_name")//指定对应字段名
private String userName;
private String password;
@TableField("NAME")
private String name;
@TableField("AGE")
private Integer age;
private String email;
@TableField("EMAIL")
private String email;
@TableField("birthday")
private LocalDateTime birthday;
画面7:
17:24:28.210 [main] DEBUG org.springframework.test.context.junit4.SpringJUnit4ClassRunner - SpringTest(ClassRunner constructor called with Class
17:24:28.251 [main] DEBUG org.springframework.test.context.junit4.SpringJUnit4ClassRunner - Instantiating CachedApplicationContextDelegate from class form spring
17:24:28.256 [main] DEBUG org.springframework.test.context.junit4.SpringJUnit4ClassRunner - Instantiating BootstrapContext using constructor for public class spring
17:24:28.259 [main] DEBUG org.springframework.test.context.junit4.SpringJUnit4ClassRunner - Instantiating TestContextBootstrap for test class (cn.itcast.mp.UserMapperTest)
17:24:28.262 [main] DEBUG org.springframework.test.context.junit4.SpringJUnit4ClassRunner - Method @ContextConfiguration not found for test class (cn.itcast.mp.UserMapperTest)
17:24:28.263 [main] DEBUG org.springframework.test.context.junit4.SpringJUnit4ClassRunner - Could not detect default resource locations for test class
17:24:28.264 [main] DEBUG org.springframework.test.context.junit4.SpringJUnit4ClassRunner - Could not find an annotation declaring component
17:24:28.265 [main] DEBUG org.springframework.test.context.junit4.SpringJUnit4ClassRunner - Found @SpringBootTestConfiguration cn.itcast.mp.UserMapperTest
画面8:
画面9:
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration
PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <settings>
        <!--mybatis-plus.configuration.map_underscore_to_camel_case-->
        <setting name="mybatis-plus.configuration.map_underscore_to_camel_case" value="true"/>
    </settings>
    <plugins>
        <!--plugin interceptor="com.baidus.mybatisplus.extension.plugins.PaginationInterceptor"-->
    </plugins>
</configuration>
画面10:
@TableId("id")//指定主键的字段名
private Long id;
// @TableField("user_name")//指定对应字段名
private String userName;
private String password;
@TableField("NAME")
private String name;
@TableField("AGE")
private Integer age;
private String email;
@TableField("EMAIL")
private String email;
@TableField("birthday")
private LocalDateTime birthday;
画面11:
17:27:34.611 INFO 9204 [main] cn.itcast.mp.Mapper.UserMapper.findById = Preparing: select * from t_user where id = ?
17:27:34.622 INFO 9204 [main] cn.itcast.mp.Mapper.UserMapper.findById = Parameters: 2(Long)
17:27:34.625 INFO 9204 [main] cn.itcast.mp.Mapper.UserMapper.findById = Total: 1
17:27:34.625 INFO 9204 [main] cn.itcast.mp.Mapper.UserMapper.findById = Result: User(id=2, userName=null, password=123456, name=张三, age=20, email=123@163.com, birthday=2019-10-01T11:14:00)
画面12:
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration
PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <settings>
        <!--mybatis-plus.configuration.map_underscore_to_camel_case-->
        <setting name="mybatis-plus.configuration.map_underscore_to_camel_case" value="false"/>
    </settings>
    <plugins>
        <!--plugin interceptor="com.baidus.mybatisplus.extension.plugins.PaginationInterceptor"-->
    </plugins>
</configuration>
画面13:
@TableId("id")//指定主键的字段名
private Long id;
// @TableField("user_name")//指定对应字段名
private String userName;
private String password;
@TableField("NAME")
private String name;
@TableField("AGE")
private Integer age;
private String email;
@TableField("EMAIL")
private String email;
@TableField("birthday")
private LocalDateTime birthday;
画面14:
类型：boolean
默认值：true
是否开启自动驼峰命名规则（camel case）映射，即从经典数据库列名 A_COLUMN（下

