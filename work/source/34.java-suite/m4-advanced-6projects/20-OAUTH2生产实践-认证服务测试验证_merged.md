# 20-OAUTH2生产实践-认证服务测试验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着的话呢

咱们就对认证服务呢

做个启动和验证

首先呢

咱们要进行了数据库的初始化

因为呢

认证服务

它需要去预制呢

对应的client信息

对不对

好

那我们来看一下

在这里面的话呢

会去创建一个

tosclientdetails这个表

然后呢

会给它初始化两条数据

新增tosclientdetails表

初始化两条client信息

名称呢

是app

密码呢

也是app

这个名称跟密码呢

都是一致的

然后呢

我们还初始化了一个

t-chatter

U字表的

它的一个数据信息

因为呢

我们要提供了一个

资源服务接口

对不对

根据这个U字

去获取它对应的

用户详情

那么这个呢

也可以

也是为了

便于我们呢

去验证

这个密码模式的揭露

是否呢

能够成功

好

那么我们来看一下

在

打开我们的数据库

虚拟机当中

t-chatter

这个业务数据库

在这里面的话呢

创建对应的表

在这里我已经提前装件好了

t-os client detail

然后呢

要插入两条数据

大家呢

按照这个circle

去执行就可以

这里面的话呢

大家可以看到

它的一个密钥呢

是经过加密的

对不对

并非明文的这个方式

进行了显示

它也是为了保证整个

密码信息的一个安全可靠性

接着的话呢

咱们要启动相关的一个服务

要启动什么服务呢

第一个是Nacos

这个是Nacos

这个Nacos呢

要检查好

咱们呢

已经将它启动好了

对不对

然后呢

是Ladies

Ladies服务呢

要确保启动正常

这个数据库呢

也要将它启动好

咱们呢

都已经启动完成

接着的话呢

咱们就要启动认证服务

好

咱们呢

来看一下

认证服务呢

找到启动内

那么我们呢

之前已经是将整个工程的

实现了

以及配置了

都已经完成

这时候的话呢

大家在持续过程当中呢

要检查一下

是否有包错

对不对

最近的这些

注解呢

一定要加入进去

像stock password

这个呢

也要加入一下

我们把它那个service

加入进去

注入到Split容器当中

好

其他的话呢

这一块都没什么问题

那我们呢

再启动一下启动内

右键

好

注意观察它的一个输出日志

好

等待它的启动

咱们注意观察一下

它的端口

好

对

对

对

这个端口呢

9999已经是启动完成

整个过程当中呢

也没有包错

对不对

那接着的话呢

咱们就可以去验证和访问一下

看能否呢

获取到我们的用户信息

咱们可以看到

在这个初始化数据的时候呢

T-Shared user里面是内置一个用户数据

对不对

admin

那我们来传递对应的参数

看能否呢

把这样user name改成admin

看能否呢

获取到用户的详细信息

那我们呢

去访问一下

在这里面的话呢

是404的错误

为什么会404呢

咱们看一下后台日志

也没有输出错误

对不对

那这个时候呢

咱们就要去检查一下

我们的web

conclude的层

在这里面呢

咱们可以看到

没有加上对应的诸解

对吧

所以呢

大家自己在实现的过程当中呢

一定要注意这些细节

不要呢

出现了偏差

有些地方呢

产生了遗漏

那这样呢

就容易出现

各种各样的问题

然后呢

我们把user的这个诸解呢

在这里呢

它已经加上去了

对吧

这块呢

是没问题

因为呢

咱们可以从这个错误当中就知道了

在这里呢

它访问的时候呢

它是报这个地址呢

找不到

对不对

所以呢

我们第一反应

应该就是查到

conclude的这个诸解呢

它是否配置是正常的

那么重新启动一下服务

好

整个服务呢

已经启动完成

咱们呢

再次访问一下

好

copy一下这个讲习当中的地址

然后呢

我们再做一个访问

好

这个时候呢

是否能够成功找到了

对不对

support by adkas

这个呢

就是我们返回到自定义的登录页面

那么呢

就可以输入对的那个用户认证信息

因为我们呢

初次发的时候是额得命

对不对

密码呢

也是额得命

那我们来看一下

能否呢

找到用户的完整信息呢

好

这个时候呢

可以看到

它已经呢

将用户的完整信息呢

返回出来了

对不对

将用户的

密码呢

用户的名称啊

然后在这里面的话

它的common id啊

它的这个email啊

我们可以看一下

检查一下

在这里面email

对不对

和坤一

然后呢

adkas.cn

在这里面的话

和坤一

对吧

这个呢

是ok的

那在这里呢

就是实现了认证服务的一个

启动和验证

接下来呢

咱们再通过postman

来做一个

token的申请和认证

从中的话呢

咱们呢

我们呢

去进一步

认识整个token的一个

申请处理流程

咱们呢

就来打开postman工具

在这里呢

就按照我们的要求

进行一个测试和验证

咱们来看一下

整个的配置流程

是怎样的

咱们要新建一个请求

然后呢

输入这个地址

好

那咱们呢

就新建一个请求

好吧

然后呢

去输入它的一个地址

注意啊

这个呢

千万要注意

你哪怕错了一个字符呢

这个访问起来

都是会有问题的

就是说呢

最后的时候呢

不要加斜杠

千万不要手抖

加上一个斜杠

那最后的话呢

就会把自己给坑了

那咱们呢

将这个地址

copy进来

然后的话呢

咱们看一下

接着的话呢

它要去配置

它对应的

那个认证信息

那我们来看一下

首先的话呢

你要去配置

它基本的认证信息

对不对

basic auth

然后呢

这里要配置什么

要配置

就是client的信息

因为client

我们预制的是

A

对不对

然后名称

跟那个用户密码呢

都设置为app

配置完这个之后呢

咱们再来看一下

完成的第一步

基本的认证配置

也就是client的信息的

填写之后

接着的话呢

咱们就要去

填入

光路type

也就是说

密码的认证模式的配置

那咱们呢

就来看一下

在body里面

咱们呢

要去选择

它的类型为form data

以form表单的形式

进行提交

然后呢

要填入对应的参数

form的type

type呢

它的值为password

我们采用的是

密码认证模式

接着的话呢

是它的username

用户名称信息

这个的话呢

就填写admin

注意了

这个用户名称呢

就是chad user里面的

这个账户名和密码

然后下面这个password

这个呢

也是改成admin

还有一个scope

scope呢

我们要跟服务单的

保持一致

叫做sewer

这里呢

就完成了body的一个配置

然后呢

咱们就来测试

验证一下

大家一定要注意

这里有两部分配置

一个呢

是基础的认证配置

如果说你这部分不填呢

就是登录进去呢

它就会弹出一个黄

让你去输入账号和密码信息

这一块呢

是密码模式认证了

它所需要的信息

好

两个步骤填写完成之后

咱们呢

就来请求一下

这个时候呢

可以看到

它的结果呢

就已经返回出来了

在这里呢

它返回了一个value token

然后呢

还有refetch token的一个信息

已经在token的超时时间

对不对

因为我们采用的是什么

增强的token

所以在这里面的话呢

它将我们增强的一些信息呢

也给附带出来了

咱们还记不记得

回到我们的代码时间当中

在那个增强token的处理的时候

咱们是不是附带了三个信息

ID,NAME,EMAIL

那么咱们来看一下

拿到的结果是不是有ID,NAME

还有你对应的这个EMAIL信息

好

那么咱们来看一下

是不是

好

这个呢

就是针对于那个Postman的

它的token获取的一个测试和验证

我们采用post跟get方式的请求都可以

返回结果呢

可以看到两部分

一部分呢

是内置的token信息

另一部分呢

就是我们自定义增强的token扩展信息

这样呢

就比较方便

对不对

就不用呢

我再去交互一次

去获取完整的用户信息

你需要哪些呢

你就那个把它的标记

传递到这个附加信息中

这个附加信息

在这个附加的token上面就可以了

那我们看一下post的方式呢

post的方式也是可以

对不对

都是一样的

好

接着的话呢

咱们来看一下

怎么去刷新token

刷新token呢

它是比较简单

那咱们呢

继续来做一个测试验证

咱们呢

再创建一个请求

地址呢

还是保持不变

那这里呢

我们选中多地

同样的表单方式进行提交

那这里呢

关到type

这里呢

我们选中多地

也是要选择密码

这个关到type呢

就不叫密码模式

因为你是要刷新token嘛

对不对

你要告诉我具体的动作

refresh

然后token

下面的话呢

就是refresh

token的具体值

好

我们将值呢

在这里请求到这个值呢

传递进去

将它copy过来

粘贴一下

我们呢

就来发送一下

在这里呢

它告诉我们是错误了

对不对

提示呢

401认证错误

为什么呢

因为咱们在这里呢

忘记填写一个base

基本认证了

所以在这里呢

要把它加入进去

这就是说

为什么要加入这个基础认证

否则呢

它不能识别你这个客户端呢

是我合法的

咱们呢

再来发送一下

这个时候呢

是不是就是ok了

跟我们之前的这个token呢

获取的信息都是一样的

对不对

因为你做了一个刷新

所以呢

它将token信息呢

重新获取了一遍

这个token呢

跟之前的token就不一样了

看到没有

好

这一块呢

就是通过postman

进行了一个测试和验证

好

这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程是关于“用户服务”模块中“认证服务”的实战部署与调用。讲师通过演示如何在 Spring Boot 项目中配置并启动一个基于 OAuth2 的认证服务，然后使用 Postman 工具来模拟客户端获取和刷新访问令牌（Token）的过程。整个过程涵盖了数据库初始化、服务启动、配置文件编写、以及通过 HTTP 接口进行认证的完整流程，旨在让学习者掌握如何在实际项目中集成和使用认证服务。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，讲师介绍本节内容为“认证服务启动与验证”，并展示当前正在编辑的文档大纲。
*   **00:05 - 00:15**: 讲师切换到项目文件夹，展示 `resources` 目录下的 `static.css` 和 `templates.ftl` 文件，说明前端资源的存放位置。
*   **00:15 - 00:30**: 讲师在文档中定位到“3.5 认证服务启动与验证”章节，开始讲解数据库初始化。
*   **00:30 - 00:45**: 讲师展示并解释用于初始化 `t_oauth_client_details` 表的 SQL 语句，包括 `DROP TABLE IF EXISTS` 和 `CREATE TABLE` 语句（虽然图中未完全展示 `CREATE` 语句，但根据上下文可知其存在）。
*   **00:45 - 01:00**: 讲师展示用于初始化 `t_trade_user` 表的 SQL `INSERT` 语句，插入一个用户名为 `admin`、密码为 `admin` 的用户。
*   **01:00 - 01:15**: 讲师切换到 Navicat Premium，演示数据库连接和表结构，确认初始化操作已成功。
*   **01:15 - 01:30**: 讲师在文档中列出启动服务的步骤，包括启动 Nacos、Redis、数据库和认证服务。
*   **01:30 - 01:45**: 讲师在 IntelliJ IDEA 中展示 `WebSecurityConfigurer` 类的配置代码，重点是 `configure` 方法中对 `auth` 的配置，包括 `userDetailsService` 和 `passwordEncoder`。
*   **01:45 - 02:00**: 讲师展示 `TradeAuthApplication` 类的主方法，并在终端中执行 `SpringApplication.run(...)` 启动服务，终端输出显示服务启动成功。
*   **02:00 - 02:15**: 讲师展示 `TradeStockTokenController` 类的代码，其中定义了 `STOCK_OAUTH_ACCESS` 常量和 `stockRedisTemplate` 字段。
*   **02:15 - 02:30**: 讲师切换到浏览器，访问 `http://127.0.0.1:9999/trade/user?rname=admin` 接口，演示用户信息接口的访问和拦截。
*   **02:30 - 02:45**: 讲师在 Postman 中新建一个 GET 请求，地址为 `http://127.0.1.9999/oauth/token`，并设置 `Basic Auth` 认证方式，准备申请 Token。
*   **02:45 - 03:00**: 讲师在 Postman 中设置请求参数，包括 `grant_type=password`、`username=admin`、`password=admin`、`scope=server`，并发送请求。
*   **03:00 - 03:15**: 讲师展示 Postman 返回的 JSON 响应，其中包含 `access_token`、`refresh_token` 等关键信息。
*   **03:15 - 03:30**: 讲师在文档中讲解如何刷新 Token，需要将 `grant_type` 设置为 `refresh_token`，并传递 `refresh_token`。
*   **03:30 - 03:45**: 讲师在 Postman 中设置刷新 Token 的请求参数，并发送请求，成功获取新的 `access_token`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 文档内容**:
    *   **章节标题**: “3.5 认证服务启动与验证”、“3.6 认证服务与 PostMan 使用”。
    *   **数据库初始化**: `DROP TABLE IF EXISTS t_oauth_client_details;` (用于删除表)。
    *   **用户数据初始化**: `INSERT INTO trade_stock.t_trade_user (...) VALUES (...)`。
    *   **服务启动步骤**: 启动 Nacos、Redis、数据库、认证服务。
    *   **Postman 操作指南**: 申请 Token 的地址、参数设置、刷新 Token 的方法。

*   **代码关键内容**:
    *   **`WebSecurityConfigurer.java`**:
        ```java
        @Override
        protected void configure(AuthenticationManagerBuilder auth) throws Exception {
            auth.userDetailsService(authStockUserDetailService).passwordEncoder(stockPasswordEncoder);
        }
        ```
    *   **`TradeAuthApplication.java`**:
        ```java
        public static void main(String[] args) {
            SpringApplication.run(TradeAuthApplication.class, args);
        }
        ```
    *   **`TradeStockTokenController.java`**:
        ```java
        private static final String STOCK_OAUTH_ACCESS = GlobalConstants.OAUTH_PREFIX_KEY;
        @Autowired
        private RedisTemplate stockRedisTemplate;
        ```
    *   **SQL 语句**:
        ```sql
        DROP TABLE IF EXISTS t_oauth_client_details;
        INSERT INTO trade_stock.t_trade_user (...) VALUES (1, 'admin', 'ISMVKKXp...AFw==', '123', 1, NULL, NULL, NULL, 0, NULL);
        ```

---

### 4) 关键场景与演示描述

*   **场景一：数据库初始化与服务启动**
    *   **描述**: 讲师首先在 Typora 文档中规划了数据库初始化和服务启动的步骤。随后，通过在 IDEA 中编写并执行 SQL 语句，成功创建了 `t_oauth_client_details` 和 `t_trade_user` 表，并插入了初始数据。接着，讲师在终端中执行 `SpringApplication.run(...)`，成功启动了认证服务，终端日志显示了服务启动的详细信息。

*   **场景二：Postman 申请 Token**
    *   **描述**: 讲师在 Postman 中创建了一个 GET 请求，地址为 `http://127.0.1.9999/oauth/token`。他设置了 `Basic Auth` 认证方式，并在 `Params` 中填入了 `grant_type=password`、`username=admin`、`password=admin`、`scope=server` 等参数。发送请求后，Postman 成功返回了包含 `access_token` 和 `refresh_token` 的 JSON 响应。

*   **场景三：Postman 刷新 Token**
    *   **描述**: 讲师在 Postman 中创建了一个新的 POST 请求，地址与申请 Token 的地址相同。他将 `grant_type` 设置为 `refresh_token`，并将 `refresh_token` 值填入 `Params`。发送请求后，Postman 成功返回了新的 `access_token`，证明 Token 刷新功能正常工作。

*   **场景四：用户信息接口访问**
    *   **描述**: 讲师在浏览器中访问了 `http://127.0.0.1:9999/trade/user?rname=admin` 接口。该接口被认证服务拦截，页面跳转到一个登录页面，要求用户输入用户名和密码，验证了认证服务的拦截和认证功能。

---
