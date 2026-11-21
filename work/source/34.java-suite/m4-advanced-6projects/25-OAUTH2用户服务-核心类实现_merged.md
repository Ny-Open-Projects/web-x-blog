# 25-OAUTH2用户服务-核心类实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着的话呢

咱们就开始对核心类进行编码实现

那首先呢

咱们要确保用户服务呢

添加了对应的POM依赖

在这里呢

咱们都已经加入进去了

在那个stock user下面的POM

对不对

好添加完依赖之后呢

接着的话呢

咱们还要确保common DAO下面呢

添加了对应的POM依赖

下面的话呢

有哪些依赖呢

主要是mybatties的

还有一个数据库连接池

以及呢

mycircle的一个连接软件

在这里呢

咱们也已经将它添加进去

在common DAO下面

可以看到

好

确保这些依赖呢

都已经添加成功

那接着的话呢

咱们就会开始呢

去实现它的一些核心代码

首先呢

咱们将其中类呢

做个实现

咱们呢

创建stock user application

好

在我们的启动包下面

右键new class

然后读它的名称

创建完成之后呢

要将它的代码拷贝过来

这里呢

我们将它引入进来

好

大家注意一下

在这里面的话呢

要开启哪些注解呢

这个呢

是spring boot的程序

对不对

然后呢

要开启那口试的

不注册发现

要开启呢

正的客户端的一个标用

然后呢

那个compend

主键的扫描

在这里面的话呢

扫描comitcast的基础的一个包

然后呢

map scan

我们是采用ipad体式

做了一个circle数据层的这个实现

所以呢

这里呢

要采用map scan

下面呢

要enable transaction manager

开启了它的事务管理器

好

这些呢

是它的一个必要的标注

在这里面的话呢

咱们要把这些注解呢

都确保了完全添加成功

好

那下面的话呢

咱们就来实现了

它的数据层istockuser.do

咱们呢

去创建一下

在do包下面

new interface java class

在这里面选择interface

这里面呢

咱们添加一个接口就可以

什么接口呢

根据用户编号来查找用户对象

get by user number

这里呢

要传递user number

传输

然后上面的话呢

要给它一个注解

标识呢

它是一个数据层的标注

我们呢

要加上对应的注释

这个注释的话呢

根据用户编号获取用户对象信息

因为咱们呢

是要提供用户的登录接口

对不对

必须要找对应的用户

接着的话呢

咱们要实现它的一个map

这个map呢

我们将它放在DAO下面创建一个package

这个名称呢

就叫map

MAPER

创建完map之后呢

咱们还给它创建一个文件

new file类型

然后呢

是stocker user map

写上面

咱们呢

将这个map里面的circle信息呢

copy进来

完整copy

要注意呢

它的一些namespace

这个namespace咱们要检查一下

按住control

然后手机移到上面

这里能找到的说明这个路径配置是ok的

Nt的路径配置是ok的

这样的话呢

咱们也要确保是呃

填写是正确的

下面呢

就是它的一个属性页的映射

然后呢

就是它的circle查询的实现

这个circle咱们可以看到

它getby user number对应的就是咱们这个数据层接口方法

那它的一个circle查询呢

就是根据用户编号呢

去查找用户对象

这个呢

是它数据层的接口

那接下来呢

咱们就要实现了它的服务层接口

服务层接口呢

它是一个用户登录

对整个接口来讲呢

比较简单

那咱们呢

就直接引入进去

在这里面的话呢

咱们去创建一个

首先创建它的一个接口吧

S.usr

这个接口的话呢

咱们要注意它的命名规范

接着话呢

咱们再去创建它的时间内

那在下面的创建一个时间内的包

implement

那咱们把这个内的创建进去

还有呢

去实现

咱们的

那个接口

这里啊

就直接扩幅进来

感谢

注意了

还有没有报错

咱们先将对应的这个外网了

先引入进来

然后呢

咱们再对整个逻辑呢

做一个讲解

接在这一块呢

也比较简单

对不对

它只是实现了用户登录接口的一个处理

那咱们呢

再将那个controller层这块呢

实现一下回头呢

咱们再讲一下它整理了一个逻辑

有加class

stop users

在这里呢

全选

让class呢

替换更新一下

注意了

看它有没有报错

这里呢

它这种就是什么

对不对

还差一个什么

i stop users

在这里面呢

咱们并没有定义它的接口

对不对

那咱们就做呢

有种快速的方法

咱们呢

就直接选中

然后呢

reflect

formen bus app

在这里面的话呢

对吧

是勾选这个方法

然后呢

reflect

咱们撤回一下

因为咱们在这里呢

没把注释拖比过去

咱们再给大家演示一下

右键reflect

formen bus app

然后呢

在这里选中copy

这样呢

它就会将这个方法上面的注释呢

会一起拖比到接口当中

然后reflect

回头呢

咱们再看一下

在这里呢

是不是就已经加了对应的接口了

这样呢

就比较快捡对不对

那咱们再回到刚才那个controller

这样呢

它就没有报错了

好

那咱们呢

来看一下它这一块tool里的逻辑是什么时间的

咱们呢

就可以看到controller

在这里呢

它是引入了user的业务层接口

那么controller层呢

是提供了一个用户登录的接口

对不对

它要传递什么传输啊

传递用户的账号和密码

在这里面呢

咱们给了它的传输

这个名称要做了对应的一个映射

然后呢

下面是怎么去做呢

外层是一个check cache

对不对

咱们还记不记得

就是在整个的dao

service以及web

拯救的层当中呢

咱们是把异常呢

释放在最外层web层去捕获的

在这里去捕获呢

可以辨语它的统一封装

对不对

比如说你要返回错误消息

返回系统错误

对不对

都可以呢

很方便的去做一个统一的包装处理

这呢是它的一个成功的响应

咱们来看一下userlogin它具体的实现

它在属性当中呢

是注入了userdao的数据层接口

然后呢

首先是根据用户账号去查找呢

这个用户对象对不对

这个呢是第一步

如果说你连用户对象都没找到

说明了这个账号是有问题的

那么呢就会抛出一个异常

接下来逻辑呢也就不用再做处理

如果找到用户对象之后呢

接着就是对用户密码做一个判断

那怎么判断呢

因为咱们呢是以密文方式做处理

对不对

所以呢要先对用户传过来的密码呢

要做一个加密处理

然后呢再跟咱们的数据库密码做一个比对

如果两边加密密码

是一致的就认为呢

它是登录成功

那如果是不一致呢

在这里就会抛出一个异常

说你这个用户账户密码是输入有问题

这个呢就是它的一个登录的处理的部件

那接着的话呢

咱们来实现它的配置类

这个配置类的话呢

就是呢

跟Spring Security的OS2的一个集成安全配置

那咱们来去创建这个配置类

那咱们来去创建这个配置类

那咱们来去创建这个配置类

那咱们来去创建这个配置类

那咱们来去创建这个配置类

创建一下

在这里呢

它去实现了一个接口

这个接口的话呢

是resource server config

这个接口实现完整之后呢

咱们要去做一个实现

两个可选的实现

在实现之前呢

咱们先要注入它的需要用到的手机

Value Remote Token Service

这个咱们看一下它哪个包下面了

它是在呢

Spring Security OS2下面的

对不对

好

将这个注入一下

这个呢

是用于远程Token的一个调用

信息的图例

Buy with

Rest

Template

在这里呢

也将它注入一下

注入完成之后呢

咱们看一下该怎么去配置呢

Remote Token Service

在这里呢

要set REST template

这样呢

它才能实现远程的调用和访问

然后呢

Resource

Servo

Security

Copiger.

在这里面的话呢

直接引入进来

Token Service

这个Token Service呢

就是Remote Token Service

像它呢

放置在这个Resource对象里面

接着的话呢

就是资源的一个安全配置

资源的安全配置

咱们来看一下该怎么去解呢

在这里咱们先把

注入进去

方式呢

远程调用

采用了REST

Template方式

在这里呢

它这个方法

主要是对资源服务的

安全配置

那咱们来看一下

这一块的具体配置

在这里呢采用CSRF

这样呢

将它关闭

CSRF呢是跨站请求伪造

接着的话呢是any match

这个呢是配置它

需要认证的接口

然后呢

我们来去执行一下它的form logic

locking page

locking的接口

然后呢再点一下它的一个view

其他的失败页面是跳在哪里

最后呢就是落论的

success的

成功页面

这样呢

咱们就完成了服务的安全配置

如果是有其他的接口呢需要暴露

或者是

需要排除的话呢

咱们也可以去参照

像那个AUX里面

在这里面呢

也做了具体的一个配置

Web Security Config

比如说你要去

排除

它能够进行讨论

就加上这一段就可以了

那么在这里面的话呢

这些的话呢需要进行一个认证处理

那么咱们呢再加快一点

然后把这个

下面的这一段代码呢

直接复制进来

这个呢

它是什么作用呢

它是ListTerm里远程调用的一个配置

咱们可以看到在这里呢

它可以支持load balance

负载均衡的一个处理

然后呢

将它的add handle

做了一个补破

也就是在这里面的话呢

只要补是等于battle request

那在

那它的一个处理呢

就将它的handle handle

response放到handle里面去

除了这个

除此之外其他的错误行动呢

它都会进行add handle的一个

错误的补破

好

这一块呢是ListTemplate

它的这个配置

以及呢整个资源服务的它的安全性配置

资源服务呢咱们要注意一定要开启EnableResource

然后还有一个注解呢是EnableGlobalMessageSecurity

这个呢是方法级别的一个安全控制

注解呢

这个注解呢有一个属性对不对

就是在Post的

这个

预先呢要做一个

开启处理

好

再往下面呢咱们再来看

它的一个工程配置

工程配置呢创建比较简单

我们呢

先实现一下

在Resource下面

View File

好将工程呢

文件创建好

然后再将这里面的配置内容呢

扩给评计

我们来看一下主要有哪些配置呢

上面呢是服务的基本信息配置

像它的服务端口

名称然后Narcos等配置信息

然后下面呢就是数据软

DLUID

数据配置

再往下面呢就是Splint Security它的一个

链接配置

Splint Security之前讲认证服务呢也给大家做了一个讲解对不对

那么作为资源服务呢你要配置它的一个特别介面接口

以及呢你的Client的它的预置信息

好

最后呢就是MyBedist

一个配置

在这里呢咱们要注意一下如果说你的路径发生了调整这个路径呢一定要匹配正确咱们要核对一下对不对

Com ID Cache

然后在这里呢

它的路径

要调整对不对

Bus Start User

然后下面的话是DLMap

确保这一块呢是能够

成功的

省略到咱们呢只能入境

这样呢MyBedist的数据层接口呢才能够正常生效

在这里咱们就实现了它的核心内的

一个代码的

分析

以及呢

它整个的工程配置

那这一讲呢咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于一个名为“bulls-stock-user”的 Spring Boot 项目中“用户服务”模块的开发与实现。课程内容主要围绕如何构建一个完整的用户登录功能，该功能涉及多个层次的代码实现：从控制器（Controller）接收请求，到服务层（Service）处理业务逻辑，再到数据访问层（DAO）与数据库交互，最后通过安全配置（Security）进行认证授权。视频还讲解了如何配置项目以使其作为资源服务（Resource Server）运行，并通过 `RestTemplate` 调用认证服务。整个过程体现了分层架构、接口设计、异常处理和安全配置的完整开发流程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:20**: 课程引入，展示项目结构和当前学习目标。
*   **00:20 - 00:40**: 讲解用户服务的工程结构，包括 `controller`, `dao`, `service` 等包。
*   **00:40 - 01:00**: 介绍核心类的实现，首先创建 `StockUserDao` 接口。
*   **01:00 - 01:20**: 创建 `IStockUserService` 服务接口。
*   **01:20 - 01:40**: 在 `StockUserController` 中定义用户登录接口 `userLogin`。
*   **01:40 - 02:00**: 在 `StockUserServiceImpl` 中实现 `userLogin` 方法，包含获取用户对象和抛出异常的逻辑。
*   **02:00 - 02:20**: 讲解安全配置，展示 `ResourceSecurityConfigurer` 类。
*   **02:20 - 02:40**: 在 `ResourceSecurityConfigurer` 中配置 `configure(HttpSecurity http)` 方法，禁用 CSRF 保护。
*   **02:40 - 03:00**: 讲解资源服务的配置，展示 `@EnableResourceServer` 注解和 `@EnableGlobalMethodSecurity` 注解的作用。
*   **03:00 - 03:20**: 展示 `bootstrap.yml` 配置文件，设置服务端口、应用名称和 Nacos 配置中心。
*   **03:20 - 03:40**: 展示 `application.yml` 中的资源服务配置，包括 `token-info-uri`, `client-id`, `scope` 等。
*   **03:40 - 04:00**: 讲解 MyBatis 的配置，设置 `mapper-locations`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “3.4 核心类实现说明”、“3.5 启动与验证”。
    *   **关键概念**: “用户服务”、“资源服务”、“@EnableResourceServer”、“@EnableGlobalMethodSecurity”、“RestTemplate”。
    *   **配置文件**: `bootstrap.yml`、`application.yml`。

*   **代码关键内容**:
    *   **`pom.xml` 依赖**:
        ```xml
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        ```
    *   **`StockUserApplication` (启动类)**:
        ```java
        @SpringBootApplication
        public class StockUserApplication {
            public static void main(String[] args) {
                SpringApplication.run(StockUserApplication.class, args);
            }
        }
        ```
    *   **`IStockUserDao` (DAO 接口)**:
        ```java
        @Repository
        public interface IStockUserDao {
            // 根据用户编号获取用户对象
            TradeUser getUserByUserNo(String userNo);
        }
        ```
    *   **`IStockUserService` (Service 接口)**:
        ```java
        @Service
        public interface IStockUserService {
            TradeUser userLogin(String userNo, String userPwd) throws ComponentException;
        }
        ```
    *   **`StockUserController` (Controller)**:
        ```java
        @RestController
        @RequestMapping("/user")
        @Log4j2
        public class StockUserController {
            @Autowired
            private IStockUserService stockUserService;

            @RequestMapping("/userLogin")
            public ApiRespResult userLogin(@RequestParam("userNo") String userNo,
                                          @RequestParam("userPwd") String userPwd) {
                ApiRespResult result = null;
                try {
                    // 调用服务层
                    result = stockUserService.userLogin(userNo, userPwd);
                } catch (Exception e) {
                    // 处理异常
                }
                return result;
            }
        }
        ```
    *   **`StockUserServiceImpl` (Service 实现)**:
        ```java
        @Service
        public class StockUserServiceImpl implements IStockUserService {
            @Autowired
            private IStockUserDao stockUserDao;

            @Override
            public TradeUser userLogin(String userNo, String userPwd) throws ComponentException {
                // 1. 获取用户对象
                TradeUser tradeUser = stockUserDao.getUserByUserNo(userNo);
                if (null == tradeUser) {
                    throw new ComponentException(ApplicationErrorCodeEnum.USER_NOT_FOUND);
                }
                // 2. 验证密码
                if (!tradeUser.getUserPwd().equals(userPwd)) {
                    throw new ComponentException(ApplicationErrorCodeEnum.USER_PWD_ERROR);
                }
                // 3. 返回用户对象
                return tradeUser;
            }
        }
        ```
    *   **`ResourceSecurityConfigurer` (安全配置)**:
        ```java
        @Configuration
        @EnableResourceServer
        @EnableGlobalMethodSecurity(prePostEnabled = true)
        public class ResourceSecurityConfigurer {
            @Autowired
            private RemoteTokenServices remoteTokenServices;

            @Override
            public void configure(HttpSecurity http) throws Exception {
                http.csrf().disable();
                http.authorizeRequests()
                    .antMatchers("/user/**").authenticated()
                    .anyRequest().permitAll();
            }
        }
        ```
    *   **`bootstrap.yml` (配置文件)**:
        ```yaml
        server:
          port: 10681
        spring:
          application:
            name: stock-user
          cloud:
            nacos:
              discovery:
                server-addr: 127.0.0.1:8848
        ```
    *   **`application.yml` (配置文件)**:
        ```yaml
        resource:
          loadBalanced: true
          token-info-uri: http://trade-auth/oauth/check_token
          client:
            client-id: app
            client-secret: app
            scope: server
            access-token-uri: http://trade-auth/oauth/token
            user-authorization-uri: http://trade-auth/oauth/authorize
        mybatis:
          mapper-locations: classpath:/itcast/trade/stock/user/dao/mapper/*.xml
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构展示 (00:00-00:20)**
    *   **描述**: 视频开始时，讲师在 IntelliJ IDEA 中展示了项目的整体结构。项目名为 `bulls-stock-user`，包含 `src/main/java` 和 `src/main/resources` 目录。讲师强调了 `controller`, `dao`, `service` 等包的划分，为后续开发做准备。

*   **场景二：创建 DAO 接口 (00:40-01:00)**
    *   **描述**: 讲师在 `mapper` 包下右键点击，选择“新建” -> “接口”，创建名为 `IStockUserDao` 的接口。在接口中添加 `@Repository` 注解，并定义了 `getUserByUserNo` 方法，用于根据用户编号查询用户对象。

*   **场景三：创建 Service 接口 (01:00-01:20)**
    *   **描述**: 讲师在 `service` 包下创建 `IStockUserService` 接口。在接口中添加 `@Service` 注解，并定义了 `userLogin` 方法，该方法接收用户名和密码作为参数，并抛出 `ComponentException` 异常。

*   **场景四：实现 Controller 层 (01:20-01:40)**
    *   **描述**: 讲师在 `StockUserController` 中定义了 `@RequestMapping("/userLogin")` 的方法。该方法接收 `userNo` 和 `userPwd` 参数，并通过 `@Autowired` 注入 `IStockUserService` 服务对象。

*   **场景五：实现 Service 层 (01:40-02:00)**
    *   **描述**: 讲师在 `StockUserServiceImpl` 中实现了 `userLogin` 方法。方法首先通过 `stockUserDao.getUserByUserNo(userNo)` 获取用户对象，如果用户不存在则抛出 `ComponentException`。接着，方法会验证用户密码，如果密码错误也抛出异常。最后，方法返回用户对象
