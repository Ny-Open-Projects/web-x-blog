# 画面线理解：14.今日佳人功能实现之编写业务代码（下）

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\14.今日佳人功能实现之编写业务代码（下）_【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:03, 02:12, 03:05, 04:15, 05:12, 06:13, 07:09, 09:16, 10:29, 11:41, 12:31, 13:21, 14:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:26:50

1) 这一组画面整体在讲如何实现一个基于 Spring Boot 和 Dubbo 的“今日最佳”推荐服务，包括服务端代码编写、测试、配置以及前端接口调用和 Nginx 反向代理的部署。

2) 按时间顺序列出每张画面的要点：
画面1：展示 `TodayBestService` 服务类代码，其中包含根据 token 查询用户、创建 TodayBest 对象并填充用户信息的逻辑。
画面2：展示 `my-tanhu-dubbo-service` 项目的 `application.properties` 配置文件，配置了 Dubbo 服务名、协议、端口、注册中心地址和 MongoDB 数据库连接。
画面3：展示使用 Advanced REST client 发起一个 POST 请求到 `/user/login` 接口，请求体为 JSON 格式，包含 token。
画面4：展示 `TodayBestController` 控制器代码，使用 `@GetMapping` 注解定义了 `/todayBest` 接口，通过 `@RequestHeader("Authorization")` 获取 token。
画面5：展示 `TestTodayBest` 单元测试类，使用 `@SpringBootTest` 和 `@RunWith(SpringJUnit4ClassRunner.class)` 注解，测试 `TodayBestService`。
画面6：展示 `TestTodayBest` 测试类中 `queryTodayBest` 方法的断点调试，查看 `user` 对象的值。
画面7：展示测试运行时控制台输出的异常日志，提示 `RpcException: Failed to invoke the method queryWithMaxScore`。
画面8：展示测试运行时控制台输出的异常日志，提示 `MongoSocketOpenException: Exception opening socket`。
画面9：展示 `TodayBestService` 服务类中填充用户信息的代码逻辑。
画面10：展示 `ServerApplication` 启动时控制台输出的异常日志，提示 `MongoSocketOpenException: Exception opening socket`。
画面11：展示 `ServerApplication` 类中 `@MapperScan` 注解的配置，用于扫描 Mapper 接口。
画面12：展示 `TodayBestController` 控制器类中 `@GetMapping` 注解的代码。
画面13：展示 Typora 编辑器中的文档，内容为“2.6. 统一接口服务入口”，并包含“2.6.1. 部署安装nginx”和“2.6.2. 修改配置”的说明，其中包含启动 Nginx 的命令和修改 `nginx.conf` 文件的配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public TodayBest queryTodayBest(String token) {
    //根据token查询当前登录的用户信息
    User user = this.userService.queryUserByToken(token);
    if (user == null) {
        return null;
    }

    TodayBest todayBest = this.recommendUserService.queryTodayBest(user.getId());
    if(todayBest == null) {
        todayBest = new TodayBest();
        todayBest.setId(defaultUserId);
        todayBest.setRateValue(95L);
    }

    // 补全用户信息
    UserInfo userInfo = this.userInfoService.queryUserInfoById(todayBest.getId());
    if(null != userInfo) {
        todayBest.setAge(userInfo.getAge());
        todayBest.setAvatar(userInfo.getLogo());
        todayBest.setGender(userInfo.getSex().name().toLowerCase());
        todayBest.setNickname(userInfo.getNickName());
        todayBest.setTags(StringUtils.split(userInfo.getTags(), separatorChar));
    }
    return todayBest;
}
```

画面2：
```properties
spring.application.name=itcast-tanhu-dubbo-service

dubbo.scan.basePackages=com.tanhu.dubbo.server
dubbo.application.name=dubbo-provider-tanhu

dubbo.protocol.name=dubbo
dubbo.protocol.port=20880

dubbo.registry.address=zookeeper://192.168.31.81:2181
dubbo.registry.client=zkclient

spring.data.mongodb.uri=mongodb://192.168.31.81:27017/tanhu
```

画面3：
```json
{
  "token": "1766236353"
}
```

画面4：
```java
@AutoWired
private TodayBestService todayBestService;

@GetMapping("/todayBest")
public TodayBest queryTodayBest(@RequestHeader("Authorization") String token) {
    return this.todayBestService.queryTodayBest(token);
}
```

画面5：
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@SpringBootTest
@RunWith(SpringJUnit4ClassRunner.class)
public class TestTodayBest {
    @Autowired
    private TodayBestService todayBestService;
}
```

画面6：
```java
private RecommendUserService recommendUserService;
@Value("${tanhu.sso.default.user}")
private Long defaultUserId;
```

画面7：
```java
com.alibaba.dubbo.rpc.RpcException: Failed to invoke the method queryWithMaxScore
java.lang.NoSuchFieldError: LongId
at java.lang.Class.getDeclaredFields0(Native Method)
at java.lang.Class.privateGetDeclaredFields(Class.java:2598)
at com.alibaba.com.caucho.hessian.io.JavaDeserializer.getFieldMap(JavaDeserializer.java:122)
at com.alibaba.com.caucho.hessian.io.JavaSerializerFactory.getDefaultDeserializer(JavaSerializerFactory.java:118)
at com.alibaba.com.caucho.hessian.io.SerializerFactory.getDeserializer(SerializerFactory.java:118)
```

画面8：
```java
com.mongodb.MongoSocketOpenException: Exception opening socket
at com.mongodb.internal.connection.SocketStream.open(SocketStream.java:67)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.DefaultServerMonitor$ServerMonitorRunnable.run(DefaultServerMonitor.java:74)
at java.lang.Thread.run(Thread.java:748)
Caused by: java.net.ConnectException: Connection refused: connect
at java.net.DualStackPlainSocketImpl.waitForConnect(Native Method)
at java.net.AbstractPlainSocketImpl.doConnect(AbstractPlainSocketImpl.java:380)
at java.net.AbstractPlainSocketImpl.connect(AbstractPlainSocketImpl.java:177)
at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:172)
at java.net.Socket.connect(Socket.java:589)
at java.net.Socket.connect(Socket.java:538)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:180)
at com.mongodb.internal.connection.InternalStreamConnection.open(InternalStreamConnection.java:18
