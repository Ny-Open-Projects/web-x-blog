# 画面线理解：15.今日佳人功能实现之编写业务代码（枚举bug解决）

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\15.今日佳人功能实现之编写业务代码（枚举bug解决）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:25, 00:40, 01:00, 01:12, 01:29, 01:35, 01:49, 01:57, 02:47, 03:09, 03:16, 03:36, 04:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:27:40

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
dubbo.registry.address = zookeeper://192.168.31.2181
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
2019-09-02 17:03:30.665 INFO 10876 --- [168.31.81:2181] org.apache.zookeeper.Cli
2019-09-02 17:03:32.275 WARN 10876 --- [168.31.81:2181] org.apache.zookeeper.Cli
2019-09-02 17:03:32.356 INFO 10876 --- [tor-EventThread] org.apache.zookeeper.Cli
2019-09-02 17:03:34.399 INFO 10876 --- [tor-EventThread] org.apache.zookeeper.Cli

java.lang.NullPointerException
    at com.tanhua.server.service.TodayBestService.queryTodayBest(TodayBestService.
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
package com.tanhua.server.service;
import com.tanhua.server.service.RecommendUserService;
import com.tanhua.server.vo.TodayBest;
import org.junit.Test
