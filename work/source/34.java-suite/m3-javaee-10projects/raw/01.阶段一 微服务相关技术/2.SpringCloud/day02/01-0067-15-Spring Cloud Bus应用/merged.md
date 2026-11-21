# 15-Spring Cloud Bus应用

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\15-Spring Cloud Bus应用_【海量资源尽在 ubkz.com】.mp4
- 时长 15分37秒（音频 937s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] Spring Cloud Bus应用在这一小节中我们的主要目标是启动RevitMQ通过修改马云中的配置文件后发送Post请求实现及时更新用户微服务中的配置项那具体需求呢我们要做的事情就是在马云的Git仓库中修改user-dev.yml配置文件实现不重启user-
[00:32] Service 的情况下可以及时更新配置文件那如何去实现这么一个需求我们可以使用 Spring Cloud Bus具体实现步骤来分析一下一我们的 Spring Cloud Bus是用 RabbitMQ 进行一个应用程序之间通信的所以你要启动你的 RabbitMQ好所以是启动 RabbitMQ
[01:08] 要启动启动好以后呢我们的配置中心工程刚才从我们的图里边可以看到他是要发送一个消息到RevMQ也就是要执行一个请求地址叫做bus-refresh这么一个地址才能够去发消息到RevMQ好所以呢我们要去修改配置中心也就是说我们的config-server这一个工程修改后接下来还要去修改我们的服务提供
[01:39] 工程user.gum.Service这里边我们要去接收来自Revit MQ的消息并且呢要去实现这个最新配置项的同步修改的话要去改一些代码好那这是我们的第三步最后我们再去进行一个测试验证当如果在马云中修改了配置项以后不重启服务的话是否能做到及时的把这个配置项给读取下来输出到我们的
[02:08] 开发工具控制台上好这就是我们的一个实现步骤现在按照我们的实现步骤呢打开IDA去实现启动RabbitMQ我这边已经起了大家自己要去验证你如果在用的时候呢要保证的RabbitMQ是起了的那我这边呢应该是启动了我们打开来看一下服务这边去找一下RabbitMQ有没有启动如果你用的是Linux版本的那就也去验证一下是否起我们我这边是已经起了的也就是在本地
[02:39] 起了以后呢接下来再去修改我们的配置中心工程就是它好这边我们要添加具体的依赖那这个依赖呢我们打开讲义来复制过来好格式化一下依赖就加过来了好加过来以后接下来去配置好他说我们这边有错我们看一下什么错说我这边的依赖呢这个应该是没有删到好删再保存
[03:27] 好可以了接着呢我们再到配置文件中去修改它的配置首先你要告诉我们的这个配置服务工程RabbitMQ在哪里所以我们要去配置RabbitMQ的一些信息那RabbitMQ的配置RabbitMQ我们要配置的比如说有host好这个配置是在本地的好所以是localhost那接下来这一个节呢就是配置RabbitMQ
[04:03] 配置RabbitMQ信息因为其实我们接下来配置的这些配置项都是有默认值的如果是都与默认值一致则不需要配置了那其实我这边是用默认值就可以的那么也可以写清楚端口呢是56725672也没有变然后我们用的用户名我们就用它默认的guess
[04:33] 密码也是guess如果你想用你自己的这个用户名和密码的话那你可以去改变除此以外呢我们跟跟大家说过还要去有一个地址呢去刷新我们配置中心就是发送消息的RevitMQ好所以我们要去配置一个叫做暴露地址的exposeexposure应该是include好这个不对我们来看一下配置文件打开配置文件来看
[05:09] 叫做vap回来好就是它你指定一个名称叫做refresh那这个是做什么的呢这个是做这么一件事情的就是暴露触发消息总线的地址也就是在我们这一幅图里面的这个意思我们回到讲义中执行这个刚才我们配着
[05:54] buzz干reflash之后呢他会发一个消息到我们的rebi mq所以这个配置是少不了的我们后续也需要在修改了git仓库的配置文件之后去访问这个地址去发个消息好那老师这个发了以后不是一样的还是相当于重启那么麻烦因为你想象一下以后我们的这个v服呢可有可能几十个如果要重启要起几十次那我们现在只要一个请求就可以实现几十个的
[06:22] 服务及时更新配置那还是比较便利的好我们回来到开发工具中这个已经配置好了配置好后呢接下来你去配置服务提供工程一样的要去添加启动器依赖启动器依赖呢打开讲义要添加这些依赖格式化好依赖就加好了加好以后呢接下来我们再去配置也就是也要知道Rev&Q的
[07:11] 地址所以从我们的配置服务中心这边拿过来关于RabbitMQ的配置项到我们的服务提供工程也就是boostrate.yml这里边去配置一下好配置完成完了以后呢我们要去改造一下我们的controllercontroller中要去刷新刷新配置add refresh scope这个意思就是刷新配置
[07:49] 当如果这一个配置项有改变的话及时的用最新的配置项的意思好所以我们要去添加这么一个注解那老师如果以后配置项有很多其他地方都要怎么办都要加因为我们其实及时要去刷新的配置项不会太多的你只要在有需要及时刷新最新的配置项的那一个control了中去添加它就可以了好那现在我们加了加了以后接下来我们去验证测试我们改的有
[08:20] 配置中心的重启一下服务提供的工程也要重启但是呢这个要先等我们的配置中心重启完因为它的配准件要根据我们的配置中心而来所以我们等它启完启了以后我们再来启我们的服务提供工程user-Service它也继续启好 启了以后呢我们之后再去进行一个测试测试的点那就是先不修改我们先访问测试验证一下有没有
[08:52] 启动失败如果有失败我们解决问题好如果没有那就去测试我们仓库中修改的文件能不能及时更新到好正在启动中发现到了配置服务中心好12000的没问题好都可以的完了以后呢接下来我们去测试首先呢是没有改我们访问这一个在后台查看黑马二没问题再打开马云去修改把这个能改成是三
[09:30] 黑马3提交改了以后是真的就可以了吗也是不可以的因为跟大家说过我们这幅图里面就已经提到你要去刷新要去访问这个地址才能发MQ消息也就是这个地址我们再来刷一下我们已经改成黑马3但是我现在是故意的没有执行那个刷新的动作现在控制台输出的内容还是黑马2好我现在没有重启但是现在呢我们打开一个
[10:08] restclan的工具大家也可以使用postman好那就看你喜欢了那我这边用的是restclan发送一个post请求那这个地址呢是要刷新的是配置中心服务里面的actuatorbus-refresh好这一个呢是我们配置中心中配置的地址那这个是固定不变的好actuator
[10:43] 然后接着我们是Post请求发送的是Jason一定要注意我在讲义中也有截图大家自己在跟进做的时候呢要注意选清楚然后接着呢我们再去发送成功的标准那这边至少是绿色的OK204没问题OK然后呢接下来我们已经刷了以后再刷新这个8我服务是没有重启的再刷新8刷新这个8的地址刷了以后接下来我们再回到控制台查看
[11:15] 控制台黑马3就见到了好如果我们再来测试打开浏览器你再去改一个改一个黑马4黑马3这是黑马4改后呢再来去提交提交以后接下来马上呢又一样的去刷新好然后他会发消息到我们的RabbitMQ发了以后接下来我们的这个服务提供工程就监听到这个配置项的改变就及时更新好接下来我们再刷再发送
[11:46] 发了以后呢接下来我们再去访问这个地址查看它是否更新到黑马4再刷再查看黑马4没问题好也就是我们已经可以做到用spin cloud bus去及时同步仓库中配置文件的修改让我们各个微服呢可以及时同步到获取到最新的配置项好这就是我们的spin cloud bus那刚才讲的内容在我们的讲义中
[12:17] 也都有详细的步骤好那我们刚才执行的这个地址的作用就是访问配置中心的消息总线服务也就是我们刚才的config-server接收到这个请求后呢会向消息队列也就是我们的RevitMQ发送消息而各个微服务呢会监听消息队列也就是我们的RevitMQ当微服务接收到队列中的消息之后那么会重新从配置中心获取最新的配置信息
[12:49] 这就是为什么我们刚才黑马34都可以接收到这就是我们的一个spin cloud bus的一个应用那么把这些配置项在我们的笔记中给记录起来在我们的配置中心中我们加了的依赖能有这两个回到笔记记录config-server的依赖添加还有是config-server的配置
[13:26] 文件添加内容依赖的话我们加了这一些然后如果是我们的配置文件那我们加了这一些配置文件把它拿过来其实是这一段rebitmq和这一部分management之后呢再是我们的user-Service的依赖添加内容还有是它的配置
[14:22] 最后还有一个是我们的处理器这一个的 Eli 内容我们加了三个 Eli配置也同样的是要加我们 RabbitMQ 的好 我们来看一下具体的内容找到我们的 Eli.pwn.sml 文件我们刚才加的配置有这一些这三个 bus 部分配置那就是只有 RabbitMQ 的配置还有是我们这个 Controller 的修改
[15:18] Control了我们就加了一个注解好这就是我们Spring Cloud Bust应用的全部内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Spring Cloud Bus（基于 RabbitMQ）实现配置中心的配置文件热更新，无需重启服务。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了课程PPT的第14、15、16节标题，其中第15节“Spring Cloud Bus应用”目标是“自动RabbitMQ通过修改码云中的配置文件后发送Post请求实现及时更新用户微服务中的配置项”。
画面2: 展示了IDEA中 config-server 项目的结构，以及其 bootstrap.yml 配置文件内容，包含服务端口、Eureka 注册中心地址等。
画面3: 展示了 config-server 的 application.yml 配置文件，其中定义了 Git 仓库地址、用户名密码、Eureka 注册中心地址等。
画面4: 展示了 Spring Cloud 配置中心的架构图，包含 Git 仓库、配置中心、RabbitMQ、Eureka 以及多个服务实例，箭头表示数据流向。
画面5: 展示了 config-server 的 application.yml 配置文件中 management.endpoint.web.exposure.include 配置项，用于暴露 /bus-refresh 端点。
画面6: 展示了 user-Service 的 UserController.java 代码，其中包含一个测试方法 queryById，用于模拟查询用户信息。
画面7: 展示了 user-Service 的 UserController.java 代码，其中 queryById 方法中添加了打印配置文件中 name 值的逻辑。
画面8: 展示了浏览器访问 http://127.0.0.1:12000/user/5 的结果，返回了用户信息 JSON 数据。
画面9: 展示了码云（Gitee）上 user-devm.yml 配置文件的内容，包含数据库连接、服务名、Eureka 地址等。
画面10: 展示了课程PPT的第4.6节“Spring Cloud 体系技术综合应用概览”。
画面11: 展示了课程PPT的第15节“Spring Cloud Bus应用”中的“实现步骤”和“小结”，并列出了 config-server 需要添加的依赖。
画面12: 展示了课程PPT的第15节“Spring Cloud Bus应用”中的“小结”，并列出了 user-Service 需要添加的依赖。
画面13: 展示了 user-Service 的 pom.xml 文件，其中添加了 Spring Cloud Bus 和 RabbitMQ 的依赖。
画面14: 展示了课程PPT的第15节“Spring Cloud Bus应用”中的“实现步骤”和“小结”，并列出了 config-server 需要添加的依赖。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面2 bootstrap.yml:
spring:
  config:
    import:
      - classpath:/application.yml
  cloud:
    config:
      server:
        git:
          uri: https://gitee.com/goheima/heima-config.git
          # 配置RabbitMQ消息：如果是想与默认值一致则不需要配置
          RabbitMQ:
            host: localhost
            port: 5672
            username: guest
            password: guest
      Service-url:
        defaultZone: http://127.0.0.1:10086/Eureka

画面3 application.yml:
server:
  port: 12000
spring:
  application:
    name: config-server
  cloud:
    config:
      git:
        uri: https://gitee.com/goheima/heima-config.git
        # 配置RabbitMQ消息：如果是想与默认值一致则不需要配置
        RabbitMQ:
          host: localhost
          port: 5672
          username: guest
          password: guest
      Service-url:
        defaultZone: http://127.0.0.1:10086/Eureka
      management:
        endpoints:
          web:
            exposure:
              # 暴露触发消息总线的地址
              include: bus-refresh

画面4 架构图无代码。
画面5 application.yml:
management:
  endpoints:
    web:
      exposure:
        # 暴露触发消息总线的地址
        include: bus-refresh

画面6 UserController.java:
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {
    @Autowired
    private UserService userService;
    private String name;
    @GetMapping("/user")
    public User queryById(Long id) {
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return userService.queryById(id);
    }
}

画面7 UserController.java:
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {
    @Autowired
    private UserService userService;
    private String name;
    @GetMapping("/user")
    public User queryById(Long id) {
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("配置文件中的name值：" + name);
        return userService.queryById(id);
    }
}

画面8 无代码。
画面9 user-devm.yml:
server:
  port: ${port:9001}
spring:
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/Spring Cloud
    username: root
    password: root
  application:
    name: user-Service
  mybatis:
    type-aliases-package: com.itheima.user.pojo
  client:
    Service-url:
      defaultZone: http://127.0.0.1:10086/Eureka
      instance:
        prefer-ip-address: true
    ip-address: 127.0.0.1

画面11 config-server 依赖：
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-bus</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-stream-binder-rabbit</artifactId>
</dependency>

画面12 user-Service 依赖：
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-bus</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-stream-binder-rabbit</artifactId>
</dependency>

画面13 pom.xml:
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-bus-rabbit</artifactId>
</dependency>

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面4 架构图结构：
- Git 仓库 → 配置中心（通过“获取”指向）
- 配置中心 → 服务A、服务B、服务X（通过“配置”指向）
- 服务A、服务B、服务X → 本地配置缓存（通过“获取”指向）
- 配置中心 → RabbitMQ（通过“监听”指向）
- RabbitMQ → 服务A、服务B、服务X（通过“监听”指向）
- 服务A、服务B、服务X → 配置中心（通过“注册”指向）
- 配置中心 → Eureka（通过“注册”指向）
- Eureka → 服务A、服务B、服务X（通过“监控”指向）
- 服务A、服务B、服务X → 配置中心（通过“监听配置”指向）
- 配置中心 → 服务A、服务B、服务X（通过“推送、修改”指向）
- 服务A、服务B、服务X → 配置中心（通过“配置中心启动后会缓存到本地”指向）

画面10 标题：4.6 Spring Cloud 体系技术综合应用概览

画面11 标题：15. Spring Cloud Bus应用
内容：
目标：自动RabbitMQ通过修改码云中的配置文件后发送Post请求实现及时更新用户微服务中的配置项
分析：
需求：在码云的git仓库中修改user-dev.yml配置文件，实现不重启user-Service的情况下可以及时更新配置文件。
实现步骤：
1. 启动RabbitMQ；
2. 修改配置中心(config-server)；
3. 修改服务提供工程user-Service；
4. 测试
小结：
- config server的依赖添加内容
  <dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-bus</artifactId>
  </dependency>
  <dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-stream-binder-rabbit</artifactId>
  </dependency>

画面12 标题：16. Spring Cloud 体系技术综合应用说明
目标：了解Spring Cloud中的Eureka、GateWay、Config、Bus、Feign等技术的综合应用

5) 无。

