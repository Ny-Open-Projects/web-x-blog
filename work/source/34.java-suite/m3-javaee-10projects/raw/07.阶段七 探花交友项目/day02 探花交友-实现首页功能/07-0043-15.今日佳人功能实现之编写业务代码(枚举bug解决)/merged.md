# 15.今日佳人功能实现之编写业务代码（枚举bug解决）

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\15.今日佳人功能实现之编写业务代码（枚举bug解决）_【海量资源尽在 666java.com】.mp4
- 时长 4分28秒（音频 269s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下在我们讲义中啊所写的这样的一个bug啊就是在我们测试的时候呢其实呢我们会出现一个空指针异常啊那么这个异常是在哪里呢其实是在这个位置就是我们去读取这个性别的时候会有一个空指针异常那么刚刚我们在测试的时候呢其实并没有发生这个空指针异常为什么呢是之前呢我们直接拷贝着我们讲义中的这个配置啊
[00:28] 然后我们数据库的连接并没有真正的去连接到我们麦炭花这样的一个数据库所以说会导致了一个就是它连接到默认连接到是
[00:42] 碳花这个数据库当然这两个数据是一样的但是在结构方面稍微有点不同那么关键的是在这个里面就是说它连接到正确的如果正确连接到我们这个数据库的话它会出现空子人异常那我们来测试一下那我把它改成这个麦碳花改成它然后我们去执行一下来看一下这个错误那么我们来看一下这个它的执行走走往下面走
[01:12] 好这个都没有问题啊那么在我们查询这个优质info之后呢它会有一个问题啊就是来看一下啊这个问题呢是在这里那么会发现我们这个sex这个性别呢没有拿到数据啊这个是一个有问题的就是存在一个bug啊所以说呢再往下面走我们去拿到这个sex的话就会直接报空指针异常那么我们要解决这个问题啊那么为什么会拿不到啊为什么会拿不到呢
[01:39] 那么原因是在我们这个位置我们使用的是mybattiesplus所提供的一个美举的这样的一个这样的一个操作就是我们可以很优雅的去使用这个美举应该是在优质info这个里面就是在这个优质info这个里面那么去使用这个美举但是这个并不是mybatties所原生支持的这样的一种用法那么这个是mybattiesplus所支持的一种用法
[02:08] 那么我们这个问题出现在哪里呢出现在我们的数据库表中的类型那么仔细来看啊那么在我们的这个数据库中的这个类型呢我们设置了这个tangent int那么这个类型呢在mybattie的plus在做处理的时候呢并没有处理这种类型就会导致这个字段拿到的是一个none啊所以说呢我们这个位置呢我们要把它改一下这个类型
[02:35] 那么这个其实也可以称之为是一个mybeta plus它的它本身的一个bug它没有处理这样的一个这个类型啊那我们只能把它改成什么呢改成这个int这种类型那么改成这种类型呢就没有问题了那么我们为了测试方面呢我们把这个13我们知道啊这个用户是不是就是我们得分最高的一个用户对不对
[02:57] 我们把它的性别之前是1那我们把它改成2改成2那我们来看一下他拿到的性别是不是女呢我们再来做一个测试然后走那我们来等待他的一个执行好那么我们来看一下执行的一个结果走走往下面走走到他好那我们来看一下这回拿到我们这个结果了没有是不是就拿到了这回就OK了对吧再往下面走这回就没有问题了
[03:25] 好那么通过我们来看一下这个最后的一个结果啊那么是不是也可以拿到这个什么呢woman啊当然我们在我们前段呢所需要的是一个这个woman这样的一个创作所以我们这样去做一个处理啊那么刚刚我们在debug可以看到他拿到的这个是不是就是一个女啊这样的一个性别那么这个问题是不是就解决了那么呃所以说呢在我们讲一段话说
[03:48] 提到的一个问题就是这样的问题啊就说我们在这个优质音货表中啊我们把这个sex呢设置为tinyint这样的一个类型的话那么每一句类型呢不能够正确的做一个映射啊不能去做一个正确的映射所以我们需要把它改为是一个int类型大家前面我也说了这个问题呢应该算作是mybeta的plus它本身的一个这个bug
[04:12] 但是我们现在不能够去直接去修改这个bug对吧所以我们只能去做兼容了那我们去改成什么改成int就ok了那么其他的就没有问题了跟我们刚刚所写的是一样的ok好那么关于这个mage的bug我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过单元测试验证“今日最佳”推荐服务的逻辑，包括查询用户信息、构建推荐对象并处理空值情况。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在 TestTodayBest.java 中，调用 todayBestService.queryTodayBest(token) 方法，并打印返回结果。
画面2：展示 application.properties 配置文件，其中包含 Spring Boot 应用名、端口、数据库连接信息、MyBatis Plus 和 Dubbo 配置。
画面3：在 application.properties 中，光标位于数据库 URL 的 “/tanhua” 部分，显示数据库连接配置。
画面4：在 application.properties 中，光标位于 MyBatis Plus 的 table-prefix 配置项，显示数据库表前缀配置。
画面5：在 TodayBestService.java 中，调试断点位于 if (todayBest == null) 语句处，查看变量值，此时 todayBest 为 null。
画面6：在 TodayBestService.java 中，调试断点位于 UserInfo userInfo = this.userInfoService.queryUserInfoById(...) 语句处，查看变量值，此时 userInfo 为 null。
画面7：在 TestTodayBest.java 中，测试失败，控制台显示 java.lang.NullPointerException 异常堆栈，指出在 TodayBestService.queryTodayBest 方法中发生空指针异常。
画面8：在 TodayBestService.java 中，光标位于 queryTodayBest 方法的注解 @Value("${tanhua.sso.default.user}") 上，显示默认用户 ID 的配置。
画面9：在 UserInfo.java 中，查看 User 类的定义，包含 id、nickName、logo、sex、age 等字段。
画面10：在 Navicat Premium 中，查看数据库表结构，显示 tb_user 和 tb_user_info 表的字段和注释。
画面11：在 User.java 中，查看 User 类的定义，包含 id、mobile、password 字段，并使用 @JsonIgnore 注解忽略 password 字段。
画面12：在 TodayBestService.java 中，调试断点位于 if (null != userInfo) 语句处，查看变量值，此时 userInfo 不为 null。
画面13：在 TestTodayBest.java 中，测试通过，控制台显示测试结果：nickname-heima_13, gender=woman, age=36, tags=[单身, 本科, 年龄相仿], fateValue=98。
画面14：在 Typora 编辑器中，显示 day02.md 文件的 2.5.4 节内容，展示测试类 TestRecommendUserApi 的代码，用于测试 RecommendUserService 的 queryTodayBest 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@TestQueryTodayBest() {
    String token = "eyJhbGciOiJIUzI1NiJ9.eyJhJb2JpGUIOiIxNzYwMjJyNjg2OCIsImlkIjoxFQ.OzoV79yJ
    .todayBest = this.todayBestService.queryTodayBest(token);
    .println(todayBest);
```

画面2：
```properties
spring.application.name = itcast-tanhua-server
server.port = 18081

spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/tanhua?useUnicode=true&cha
spring.datasource.username=root
spring.datasource.password=root

# 框架扫描包
mybatis-plus.type-enums-package=com.tanhua.server.enums
# 表名前缀
mybatis-plus.global-config.db-config.table-prefix=tb_
# 主键自增
mybatis-plus.global-config.db-config.id-type=auto

dubbo.application.name = itcast-tanhua-server
dubbo.registry.address = ZooKeeper://192.168.31.2181
```

画面5：
```java
return null;
}
TodayBest todayBest = this.recommendUserService.queryTodayBest(user, q
if (todayBest == null) {
    todayBest = new TodayBest();
    todayBest.setId(defaultUserId);
    todayBest.setTags("单身, 本科, 年龄相仿");
    todayBest.setFateValue(98);
}
```

画面6：
```java
UserInfo userInfo = this.userInfoService.queryUserInfoById(todayBest.
if (null != userInfo) {
    todayBest.setAge(userInfo.getAge());
    todayBest.setAvatar(userInfo.getLogo());
    todayBest.setGender(userInfo.getSex().name().toLowerCase());
    todayBest.setNickname(userInfo.getNickName());
}
```

画面7：
```text
2019-09-02 17:03:30.665 INFO 10876 --- [168.31.81:2181] org.apache.ZooKeeper.Cli
2019-09-02 17:03:32.275 WARN 10876 --- [168.31.81:2181] org.apache.ZooKeeper.Cli
2019-09-02 17:03:32.356 INFO 10876 --- [tor-EventThread] org.apache.ZooKeeper.Cli
2019-09-02 17:03:34.399 INFO 10876 --- [tor-EventThread] org.apache.ZooKeeper.Cli

java.lang.NullPointerException
    at com.tanhua.server.Service.TodayBestService.queryTodayBest(TodayBestService.
    at com.tanhua.server.TestTodayBest.testQueryTodayBest(TestTodayBest.java:21)
    at org.springframework.test.context.junit4.statements.RunAfterTestExecutionCal
```

画面8：
```java
@Value("${tanhua.sso.default.user}")
private Long defaultUserId;

public TodayBest queryTodayBest(String token) {
    //根据token查询当前登录的用户信息
    User user = this.userService.queryUserByToken(token);
    if (user == null) {
        return null;
    }
    TodayBest todayBest = this.recommendUserService.queryTodayBest(user, q
    if (todayBest == null) {
        todayBest = new TodayBest();
        todayBest.setId(defaultUserId);
        todayBest.setTags("单身, 本科, 年龄相仿");
        todayBest.setFateValue(98);
    }
```

画面9：
```java
package com.tanhua.server.pojo;
import ...
@Data
@NoArgsConstructor
@AllArgsConstructor
public class UserInfo extends BasePojo {
    private Long id;
    private String nickName; //昵称
    private String logo; //用户头像
    private String tags; //多个用逗号分隔
    private SexEnum sex; //性别
    private Integer age; //年龄
}
```

画面10：
```sql
CREATE TABLE `tb_user_info` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(20) DEFAULT NULL COMMENT '用户id',
  `nick_name` varchar(20) DEFAULT NULL COMMENT '昵称',
  `logo` varchar(60) DEFAULT NULL COMMENT '用户头像',
  `tags` varchar(100) DEFAULT NULL COMMENT '标签，以,分隔',
  `age` int(11) DEFAULT NULL COMMENT '年龄',
  `city` varchar(20) DEFAULT NULL COMMENT '城市',
  `birthday` varchar(20) DEFAULT NULL COMMENT '生日',
  `industry` varchar(20) DEFAULT NULL COMMENT '行业',
  `cover_pic` varchar(100) DEFAULT NULL COMMENT '对话背景',
  `income` varchar(20) DEFAULT NULL COMMENT '收入',
  `marriage` varchar(20) DEFAULT NULL COMMENT '婚姻状态',
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `tb_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8 COMMENT='用户信息表';
```

画面11：
```java
package com.tanhua.server.pojo;
import ...
@Data
@NoArgsConstructor
@AllArgsConstructor
public class User extends BasePojo {
    private Long id;
    private String mobile; //手机号
    @JsonIgnore
    private String password; //密码，json序列化时忽略
}
```

画面12：
```java
// 补全用户信息
UserInfo userInfo = this.userInfoService.queryUserInfoById(todayBest.
if (null != userInfo) {
    todayBest.setAge(userInfo.getAge());
    todayBest.setAvatar(userInfo.getLogo());
    todayBest.setGender(userInfo.getSex().name().toLowerCase());
    todayBest.setNickname(userInfo.getNickName());
}
```

画面13：
```text
nickname-heima_13, gender=woman, age=36, tags=[单身, 本科, 年龄相仿], fateValue=98
```

画面14：
```java
package com.tanhua.server.Service;
import com.tanhua.server.Service.RecommendUserService;
import com.tanhua.server.vo.TodayBest;
import org.junit.Test

