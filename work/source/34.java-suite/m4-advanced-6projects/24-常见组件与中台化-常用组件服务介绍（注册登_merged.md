# 24-常见组件与中台化-常用组件服务介绍（注册登 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们来看一下我们注册登录服务它的使用说明。

当然在使用之前呢,我们需要做什么事呢?

先把我们这个网关服务还有注册登录服务,对吧,先把它跑起来。

咱们来看一下我们是具体如何把它运行起来的。

刚才我们也提到了,它是不是依赖我们这个MySQL还有Redis,然后还有什么呢,还有这个Nexus。

首先呢,我们先来看MySQL数据库。

MySQL数据库呢,我这用的是本地的数据库。

咱们可以来看一下。

然后呢,我们在这儿呢,来创建了这么一个数据库,对吧,叫做Customer-Auth。

然后这个数据库里面这些表是怎么来的呢?

就是我执行的这个地方,Docs,然后呢,Circle,对吧,执行的这个Circle脚本,把这些表创建出来的。

所以说呢,我们第一步呢,是先把数据库环境搞定,对吧。

然后呢,你也可以自己在本地呢,创建这么一个数据库,然后呢,把这个表通过那个Circle脚本的方式。

把它一执行,这样的话,表就创建出来了。

然后呢,就是Redis,对吧。

Redis的话呢,你就使用本地的也行,或者是远程的都可以。

这个呢,你根据自己的情况来启动Redis。

然后呢,就是我们这个Nexus,对吧。

Nexus的话呢,我这儿也已经启动完成了。

这是我们这个Nexus,对吧。

然后呢,这里边有这么三个配置文件。

而这三个配置文件是怎么来的呢?

就是我在这个地方,是不是这个压缩文件呢,你直接一导入就可以了。

对应的就是这么一样。

这么三个文件。

这三个文件我们可以来看一下。

一个是Customer-auth-dev。

这个呢,是不是就是我们这个auth它所使用的。

因为它这个应用名就叫Customer-auth。

咱们可以来看一下。

你看,它这个应用名是不是叫做Customer-auth。

所以说呢,它在启动的时候呢,会读取这个配置文件。

当然了,它也会读取这个文件,因为这个文件呢,是一个公共文件。

咱们可以来看一下。

你看,这个文件,对吧。

是我们这个公共文件,叫Customer-auth-comment。

这个是公共的文件。

所以它在启动的时候呢,会读取这两个文件。

而这个呢,这是咱们这个网关的,对吧。

它所读取的文件。

而网关呢,也会读取这个。

因为在网关服务的配置文件里边呢,也是这么配置的。

也就是把它配置成一个shared data IDs。

相当于是一个什么公共的,共享的这么一个文件。

这是我们这个配置文件,是不是也就搞定了。

然后搞定之后啊,我们就可以来正常启动了。

当然这些相应的地方呢,你需要把它都改对了,对吧。

能够连上你这个NUCOS。

然后呢,我们就可以正常来启动咱们这两个服务了。

起来之后呢,它会注册到我们这个服务列表里面来。

我这个是已经过期了,重新登录一下。

在这个服务列表里面,你看啊,就是这个,叫做Customer-auth。

Customer-auth-comment。

Customer-auth-comment。

Customer-auth-comment。

Customer-auth-comment。

Customer-auth-comment。

Customer-auth-comment。

因为现在呢,我这个服务还没有启动完。

所以说呢,在这个服务列表里面呢,还看不到。

好,现在这个Customer-auth已经起来了。

再来。

网关呢,正在启动。

好,网关也起来了。

然后呢,我们从这儿来查询。

你看,这两个微服务呢,就都跑起来了。

这是我们真正在使用之前,对吧。

需要来做个什么事呢?

就是先把我们这两个微服务把它跑起来。

能够成功地运行起来,就可以了。

这是第一步。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段主要演示了一个基于 Spring Cloud 的微服务认证授权系统（`cust-auth`）的开发与部署过程。讲师通过 IntelliJ IDEA 开发环境，逐步展示了如何实现微信登录功能、配置 Nacos 服务注册与发现、以及如何通过网关进行路由和 JWT 校验。视频内容涵盖了后端代码逻辑、数据库表结构设计、配置文件编写以及服务启动后的状态监控，旨在为学习者提供一个完整的微服务认证系统搭建实例。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:02**: 展示 `AuthServiceImpl.java` 文件中的微信登录核心逻辑，包括构造授权 URL、调用 HTTP 请求获取 `access_token` 和 `openid`，并进行空值校验。
*   **00:02 - 00:04**: 继续展示代码，将获取到的 `token` 保存到 Redis 中，设置过期时间为 3 天（`3 * 24 * 60 * 60` 秒），并返回登录成功结果。
*   **00:04 - 00:06**: 切换到数据库设计界面，展示 `customer_auth.sql` 文件中的 `tb_qq` 表结构，用于存储用户信息。
*   **00:06 - 00:08**: 展示数据库设计界面，显示 `tb_weixin` 表结构，用于存储微信用户信息。
*   **00:08 - 00:10**: 展示 `bootstrap.yml` 配置文件，用于配置 Spring Cloud 服务的 Nacos 注册中心信息。
*   **00:10 - 00:12**: 展示 `bootstrap-dev.yml` 配置文件，用于配置开发环境下的 Nacos 服务信息。
*   **00:12 - 00:14**: 在 IDEA 中运行 `AuthApplication` 和 `GatewayApplication`，并查看控制台日志。
*   **00:14 - 00:16**: 展示 Nacos 平台的登录界面，用于管理服务注册与配置。
*   **00:16 - 00:18**: 展示服务在 Nacos 平台上的注册状态，确认服务已成功启动。
*   **00:18 - 00:20**: 展示网关服务的路由配置页面，用于配置路由规则。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “2.2.3. 使用说明”
    *   **步骤说明**:
        1.  部署网关服务和注册登录服务并成功启动。
        2.  开发自己的业务应用。
        3.  在网关服务配置文件中配置路由规则，由网关服务进行 JWT 校验。

*   **代码关键内容**:
    *   **`AuthServiceImpl.java` 中的微信登录方法**:
        ```java
        @Transactional
        @LoginRec(status = LoginStatus.IN, type = AuthType.WEIXIN, note = "微信登录/注册")
        public Result loginWx(LoginDto loginDto, String authId) {
            // 构造微信授权URL
            String apiUrl = wxAccessTokenUrl + "?code=" + loginDto.getCode() + "&appid=" + wxAppid + "&secret=" + wxSecret + "&grant_type=authorization_code";
            // 发起HTTP请求获取access_token和openid
            Map<String, Object> atMap = HttpUtil.sendGet(apiUrl);
            Object access_token = atMap.get("access_token");
            Object openid = atMap.get("openid");

            // 判断access_token和openid是否为空
            if (access_token == null || openid == null) {
                return Result.error("微信扫码失败");
            }

            // 将token保存到Redis中，用于后续登录功能
            redisUtil.set(RedisKey.getWrtToken(auth.gettId()), token, time: 3 * 24 * 60 * 60);

            // 返回登录成功结果
            return Result.ok(msg: "登录成功", token);
        }
        ```

    *   **`customer_auth.sql` 中的 `tb_qq` 表结构**:
        ```sql
        CREATE TABLE `tb_qq` (
          `auth_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '认证信息ID',
          `openid` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '微信openid',
          `nickname` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户昵称',
          `gender` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '性别',
          `province` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '省份',
          `city` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '城市',
          `avatar_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '头像地址',
          `mobile_bind_date` datetime NULL DEFAULT NULL COMMENT '绑定手机时间',
          `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
          `user_date` datetime(0) NULL DEFAULT NULL COMMENT '用户登录时间',
          PRIMARY KEY (`id`) USING BTREE,
          INDEX `user_date` (`user_date`) USING BTREE
        ) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '登陆记录表' ROW_FORMAT = COMPACT;
        ```

    *   **`bootstrap-dev.yml` 配置文件**:
        ```yaml
        spring:
          cloud:
            nacos:
              username: custauth
              password: itheima123
              server-addr: nacos.itcast.cn:8848
              discovery:
                server-addr: nacos.itcast.cn:8848
                namespace: 16a44c82-7a92-4ff8-a431-239e93498245
              config:
                server-addr: nacos.itcast.cn:8848
                file-extension: yaml
                sharedDataIds: cust-auth-common.yml
                refreshable-dataIds: cust-auth-common.yml
                namespace: 16a44c82-7a92-4ff8-a431-239e93498245
                group: AUTH_GROUP
                server:
                  port: 8783
        ```

---

### 4) 关键场景与演示描述

*   **场景一：微信登录逻辑实现**
    *   **描述**: 讲师在 IDEA 中打开 `AuthServiceImpl.java` 文件，逐行讲解微信登录的核心代码。他首先构造了微信的授权 URL，然后通过 `HttpUtil.sendGet` 方法发送请求，获取 `access_token` 和 `openid`。接着，代码对这两个值进行空值校验，如果为空则返回错误信息。最后，将 `token` 保存到 Redis 中，并返回登录成功结果。

*   **场景二：数据库表结构设计**
    *   **描述**: 讲师切换到数据库设计界面，展示了 `tb_qq` 和 `tb_weixin` 两个表的结构。`tb_qq` 表用于存储 QQ 用户信息，包含 `auth_id`、`openid`、`nickname`、`gender`、`province`、`city`、`avatar_url`、`mobile_bind_date`、`create_date` 和 `user_date` 等字段。`tb_weixin` 表用于存储微信用户信息，包含 `auth_id`、`openid`、`nickname`、`sex`、`province`、`city`、`avatar_url`、`mobile_bind_date`、`create_date` 和 `user_date` 等字段。

*   **场景三：Nacos 服务注册与配置**
    *   **描述**: 讲师在 IDEA 中打开 `bootstrap-dev.yml` 文件，配置了 Nacos 服务的注册信息。他设置了 Nacos 的用户名、密码、服务器地址、命名空间和配置文件的共享 ID。然后，他运行 `AuthApplication` 和 `GatewayApplication`，并查看控制台日志，确认服务已成功注册到 Nacos 平台。

*   **场景四：网关路由配置**
    *   **描述**: 讲师展示了网关服务的路由配置页面，用于配置路由规则。他说明了网关服务的作用是将请求路由到后端服务，并进行 JWT 校验，以确保请求的安全性。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解该技术课程的内容。
