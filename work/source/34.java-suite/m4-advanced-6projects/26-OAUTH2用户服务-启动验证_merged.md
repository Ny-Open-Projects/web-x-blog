# 26-OAUTH2用户服务-启动验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接着的话咱们开始对用户服务做个启动和验证

在启动验证之前

我们要确保中间键都已经启动完成

将Nagos Ladies以及ChadOS认证服务都启动下

这Ladies Nagos我这边已经启动完成

我们将认证服务启动下

认证服务找到它的启动路口

在这个ChadOS Application当中

我们右键让运行

运行完认证服务之后

咱们还要开始启动咱们的用户服务

用户服务咱们同样找到它的启动内

右键让运行

启动过程当中确保不要出现任何错误

那么认证服务已经启动完成

接着的话我们看一下用户服务

用户服务它也已经启动完成

没有报任何错误

接着的话咱们就可以进行一个验证

首先的话咱们去访问用户服务

在没有认证不传递token的情况下面

咱们看一下

它返回的结果是一个什么样子的

能不能正常获取到这个接口的数据

那么打开Postman工具

在上面的话

我们将链接地址拷贝进来

这里传递的参数

一个是账户名称

一个是账户密码

咱们访问一下

在这里可以看到返回结果是什么

onOS说明没有经过认证

对不对

不具备了资源的访问权限

所以咱们要怎么办呢

接着的话咱们就要去申请对应的token

那么拿到token之后

咱们再接着访问一下

看它能否正常访问成功

那么找到认证服务

在这里面的话

之前我们做过测试了

对不对

我们确保采用的是密码模式

然后基础认证信息都已经填写完成

接着的话咱们去申请个token

好

token已经申请成功了

申请完token之后该怎么去用呢

好

回到刚才的用户访问的接口

在这里面的话

我们要选择一个类型

这个类型是Value Token

在这里面将token的值copy进来

好

这个选项千万不要选错了

一定要选择Value Token

然后玻璃在这里面都不变

咱们再访问一下

在这里面的话

它没有刚才的错误了

对不对

说明了它已经能够正常访问

我们受保护的资源

在这里出现了一个系统异常

是吧

这个系统异常咱们可以看一下

它说什么

说这个的话

没有找到这个数据层接口的实现

咱们可以看一下用户后台服务

用户后台服务找到它对应的错误异常

它说什么

没有绑定对应的Circle

出现这个问题的原因是什么呢

大家还记不记得

就在咱们之前做工程配置的时候呢

我们就做买Battis的配置

对不对

它会去指定咱们的Map Circle的路径

咱们再重新检查下

comidcast的这个报名是不一样的

对吧

我们来先把它补一下

确定

Boss stock user

下面画了DAO

然后就是对应的Map

这个路径一定要写正确

这也就是说

为什么要在这里配置买Battis的一个路径扫描的原因

咱们再启动一下

买Battis呢

它在这里面要去扫描它的收口文件

这样呢

才能跟它的DAO数据层的接口呢

形成对应的网络关系

好

启动完成之后呢

咱们再次去访问一下这个接口

在这里面的OS服务没有重新启动

对不对

那咱们的OS这一块认证是基于Ladies

所以呢

咱们不需要再次申请Token

那咱们再访问一下

哎

这个时候可以看到什么啊?好

访问的话呢

已经成功了

对不对

能够呢

获取到用户的完整的信息

咱们看一下是不是在那个controller省当中

咱们呢

是不是将用户的信息了

放到我们的包装返回对象里面

对不对

那么在Data里面显示的就是咱们用户的完整资料

那么通过这个测试呢

咱们就验证了这个用户服务呢

他已经成功加入到我们的OS2统计认证当中

在这一块呢

咱们就完成了用户服务的搭建和配置

然后在这里面的话呢

咱们要注意的一些地方

刚才的话呢

在实际测试当中

也已经给大家做了一些讲解

那些路径的话呢

一定要配置正确

千万不能搞错了

好

那这一块呢

就是对用户服务的启动和验证

这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程为一个关于“用户服务”模块的实战教学，重点讲解了如何在 Spring Boot 项目中集成 Spring Security 进行用户认证与授权，并通过 Postman 工具进行接口测试。课程内容围绕“启动与验证”展开，演示了如何启动 Nacos、Redis 和自定义的 `trade-auth` 认证服务，如何通过 `POST` 请求获取用户登录凭证（access_token），以及如何使用该凭证通过 `GET` 请求获取用户详细数据。同时，课程也展示了在未认证或未携带有效 token 的情况下，服务端如何返回 401 Unauthorized 错误，以及在代码层面如何通过 MyBatis 的 Mapper 接口定义和实现来完成数据查询。整个过程旨在帮助学习者掌握微服务架构下用户认证的完整流程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，展示课程大纲，当前章节为“3.5 启动与验证”。
*   **00:05 - 00:15**: 讲师介绍本节目标，即启动用户服务并进行验证。
*   **00:15 - 00:30**: 展示项目结构，重点介绍 `TradeAuthApplication` 和 `StockUserApplication` 两个 Spring Boot 启动类。
*   **00:30 - 00:45**: 在 IntelliJ IDEA 中，演示如何启动 `TradeAuthApplication` 和 `StockUserApplication`，并查看控制台日志确认服务已成功启动。
*   **00:45 - 01:00**: 切换到 Postman，演示如何向 `http://127.0.0.1:10681/user/userLogin?userNo=admin&userPwd=admin` 发起 `POST` 请求以获取登录凭证。
*   **01:00 - 01:15**: 在 Postman 中，演示如何在 `Authorization` 标签页中选择 `Bearer Token`，并粘贴上一步获取的 `access_token`。
*   **01:15 - 01:30**: 再次发起 `GET` 请求，验证携带 `access_token` 后可以成功获取用户数据。
*   **01:30 - 01:45**: 展示在未携带 `access_token` 的情况下，请求返回的 401 Unauthorized 错误信息。
*   **01:45 - 02:00**: 讲师总结本节内容，强调了认证服务的启动、接口的测试方法以及 Spring Security 的集成。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “3.5 启动与验证”。
    *   **关键步骤**:
        1.  启动 Nacos、Redis 和 `trade-auth` 认证服务。
        2.  启动用户服务，端口为 10681，访问登录接口：`http://127.0.0.1:10681/user/userLogin?userNo=admin&userPwd=admin`。
        3.  在没有认证、不传递 token 的情况下，返回错误信息。
        4.  在 `Authorization` 下选择 `Bearer Token`，加入 `access_token` 信息，再次请求，能够成功获取用户数据。
    *   **总结**: 完成用户服务的配置改进以及 Spring Security 的集成，核心类的处理实现；在整个项目中，存在公用的地方，要做统一处理，比如统一异常和统一接口数据返回，复用。

*   **代码内容**:
    *   **`TradeAuthApplication.java`**:
        ```java
        @SpringBootApplication
        @EnableDiscoveryClient
        @ComponentScan(basePackages = "com.itcast")
        @EntityScan(basePackages = "com.itcast")
        @EnableJpaRepositories(basePackages = "com.itcast")
        @EnableCaching
        public class TradeAuthApplication {
            public static void main(String[] args) {
                SpringApplication.run(TradeAuthApplication.class, args);
            }
        }
        ```
    *   **`StockUserApplication.java`**:
        ```java
        @SpringBootApplication
        @EnableTransactionManagement
        @EnableDiscoveryClient
        @ComponentScan(basePackages = "com.itcast")
        @EntityScan(basePackages = "com.itcast")
        @EnableJpaRepositories(basePackages = "com.itcast")
        @EnableCaching
        public class StockUserApplication {
            public static void main(String[] args) {
                SpringApplication.run(StockUserApplication.class, args);
            }
        }
        ```
    *   **`iStockUserDao.java`**:
        ```java
        TraderUser getByUserNo(String userNo);
        ```
    *   **配置文件内容**:
        ```yaml
        scope: server
        access-token-uri: http://trade-auth/oauth/token
        user-authorization-uri: http://trade-auth/oauth/authorize

        # mybatis 配置
        mybatis:
          mapper-locations:
            classpath:/com/itcast/trade/stock/user/dao/mapper/*.xml
        ```

---

### 4) 关键场景与演示描述

*   **场景一：服务启动与日志验证 (00:15 - 00:45)**
    *   **描述**: 讲师在 IntelliJ IDEA 中，通过点击 `Run` 按钮启动 `TradeAuthApplication` 和 `StockUserApplication`。随后，讲师在控制台中查看日志，确认两个服务均已成功启动，端口分别为 10681 和 10681（或其它端口，根据实际配置）。日志中显示了 Spring Boot 的初始化信息，如 `Tomcat initialized` 和 `Root WebApplicationContext`。

*   **场景二：Postman 无认证请求测试 (00:45 - 01:00)**
    *   **描述**: 讲师在 Postman 中创建一个 `POST` 请求，目标地址为 `http://127.0.0.1:10681/user/userLogin?userNo=admin&userPwd=admin`。请求体为空，`Authorization` 头部未设置。点击 `Send` 后，返回状态码为 401，响应体为 `{"error": "unauthorized", "error_description": "Full authentication is required to access this resource"}`，表明未认证的请求被拒绝。

*   **场景三：Postman 带认证请求测试 (01:00 - 01:30)**
    *   **描述**: 讲师在 Postman 中，将 `Authorization` 头部的类型改为 `Bearer Token`，并在值中粘贴上一步获取的 `access_token`。再次点击 `Send`，返回状态码为 200，响应体为包含用户信息的 JSON 数据，如 `{"code": "SYS_200", "msg": "成功", "data": {"id": null, "userNo": "admin", ...}}`，表明认证成功，可以获取用户数据。

*   **场景四：MyBatis Mapper 接口定义 (01:45 - 02:00)**
    *   **描述**: 讲师在 IntelliJ IDEA 中打开 `iStockUserDao.java` 文件，展示其中定义的 `TraderUser getByUserNo(String userNo);` 方法。该方法用于根据用户编号查询用户对象，是实现用户数据查询的核心接口。

*   **场景五：错误信息演示 (01:15 - 01:30)**
    *   **描述**: 在 Postman 中，讲师演示了在未携带 `access_token` 的情况下，请求返回的 401 Unauthorized 错误信息，强调了认证机制的重要性。
