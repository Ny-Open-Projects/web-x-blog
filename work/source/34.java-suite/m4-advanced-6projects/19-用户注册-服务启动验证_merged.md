# 19-用户注册-服务启动验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着的话咱们开始启动服务

并且对整个功能进行测试和验证

首先咱们要启动必要的依赖服务

那咱们来看一下

在这里我们要启动用户服务

认证服务可以不用启动

为什么呢

因为注册功能它是开放出来的

用户注册成功之后

他才拥有账号对不对

拥有账号之后进行登录认证

我们才需要进行健全处理

这也就是说新增的用户注册接口

前缀路径

为什么是以-open开头的原因

目的是便于我们区分管理

那接着的话呢

我们要检查认证配置

Resource Security Config

它是否配置正确

不要把包含open前缀的请求

加入到验证当中

那咱们看一下代码

找到Resource Security Config

看一下Config方法里面

它怎么配置的

下面的话

add matches

这个呢是-user开头的

它后面呢是要进行什么

进行认证

接着的话呢

咱们可以看到就没有其他的请求

需要进行认证处理

对不对

也就是说其他的这种请求的话呢

就不需要经过咱们的认证服务

做健全处理

那我们呢可以看到

stock user open controller

它是以-open开头的

跟在这里配置的-user开头的前缀路径呢

是不一致的

接下来咱们呢

就可以进行功能上的测试核心称

首先呢

我们要启动用户服务

找到startup启动内

将必要的主件呢

启动成功

ladies

nacos

好

那咱们呢

右键启动用户服务

启动完成之后呢

我们就来访问它的注册接口

通过postman

我们做一个模拟调用

看一下注册成功呢

能否正常返回用户信息

好

那我们看一下启动控制台

用户服务呢

是否启动成功

好

在这里呢

它发现我们的company we all

这个路径呢

是编写错误的

对不对

那我们呢

将它做个修正

所以咱们在写那个map文件的时候呢

不要麻木的去copy

一定呢

要检查它的路径是否正确的

让他们来检查一下其他的

其他的呢

就没有问题

我们呢

再重新启动下

好

咱们访问了用户注册接口

在这里呢

我们通过postman做个模拟请求调用

看一下注册成功之后呢

能否正常返回用户信息

好

在这里呢

报出了一个错误

说没有找到chadglobeconfig.dao数据层接口

那是什么原因呢

我们可以看到

这个chadglobeconfig接口呢

它是在system模块下面

而我们这个启动内呢

咱们可以看一下

stock user application呢

上面的map scan

只是扫描什么

它当前工程的dao并没有扫描system模块下面的dao

所以呢

会出现对应错误

那我们怎么去调整呢

再加上对应的包的扫描

在这里可以支持多个

通过逗号分割

那咱们呢

去指定ichadglobeconfig的扫描路径

在这里呢

咱们就配置完成

我们重新启动服务

大家注意

在编写代码的时候

一定要确保了路径是填写正确

并且呢

circle成数据的包路径一定要配置正确

好

用户服务呢

它就启动完成

端口呢是10681

那咱们呢

可以去访问用户的注册接口

在这里呢

我们通过postman工具进行一个模拟请求调用

然后看一下注册成功之后

能否正常返回用户的信息

好

我们再来看看

通过postman

将这个接口呢

拷贝过来

然后呢

去配置对应的参数formdate

这里请求类型的改成post

接着话呢

咱们去传递对应的参数

首先呢

是phone

这个呢

是手机号

在这里呢

我们给他随便填写一个139.01

接着的话呢

是usepassword

用户的密码

在这里呢

我们给他123456

在下面呢

是commonid

这个ID的话

我们就填写为1

然后的话呢

是name

给他test

好

对了

这个是formdata形式

然后呢

采用post方式进行提交

我们点击send发送

这时候呢

他提示我们什么

openlyjson了

这个接口没找到

让我们看一下呢

是什么原因

那么回到代码当中

检查stockuser opencontent这个接口

看一下下面呢

有没有加上对应的注册

在这里呢

并没有加上他的路径

对不对

所以呢

咱们在编解时候要注意

把他的路径呢

也要加入进去

这个值呢

是给他一个路径叫request

然后method的类型的话呢

我们让他支持post类型就可以了

这个呢

改成post

那咱们呢

就重启用户服

重启用户服呢

再次调用用户注册的接口

看一下了他的结果能否注册成功

接着话呢

咱们再访问post们的注册接口

发送请求

这时候可以看到返回结果呢

提示是注册成功的

他将用户的完整质量呢

返回出来了

在这里我们可以看到

他生成的用户编号

对不对

然后呢

他的密码也是一个加密的形式

手机号呢

跟我们在这里传递的手机号是一致的

对不对

接下来呢

我们再看一下数据库

我们找到了的确的user这个表

在这里呢

咱们刷信一下

可以看到生成了一个新的用户数据

我们看一下

交易账户有没有生成了

因为咱们在这里呢

全局配置呢

是注册即开户

这个值呢是yes

然后的话

我们看一下交易账号

是否能够生成了新的数据

刷新的时候

可以看到已经生成了一个新的账号

在这里呢

他关联的是user id

对应的是teacher的表的user id33

那么我们通过这个注册接口呢

验证整个流程呢

是ok的

没问题

好

接下来呢

咱们再

去对校验功能做一个验证

这个验证呢

就包括逻辑教验

以及呢

自动化教验

逻辑教验呢

就是咱们手动添加的业务逻辑的判断处理

这个呢

是重复注册请求的一个判断

那咱们呢

先来看一下

我们现在呢

已经生成了一个test1的手机号

是1390013900的用户

那咱们再次访问一下

看一下这个注册接口呢

还能否注册成功呢

我们先来看一下

这个时候呢

可以看到返回的结果呢

是用户已存在了

对不对

说明了我们的逻辑教验判断呢

也是正常生效的

好

接着的话呢

咱们再看一下密码围空的时候

去发出一个请求

看一下自动化教验呢

能否去检测识别出来

那咱们呢

将UZI password改为空

再次发送请求

验证一下

好

可以看到呢

它提示出来

密码长度

必须为1到30X

也就是自动化教验呢

它正常生效了

对不对

接下来呢

我们再来看一下

用户名和密码都围空

然后发出请求

看它呢

能否将所有错误提示都返回出来

刚才呢

是验证了一个错误请求

对不对

因为咱们之前讲过

这个自动化教验呢

它会教验所有属性呢

是否都符合我们的教验规则

如果说都不符合呢

它会将所有的提示性计划呢

全部抛出来

这样呢

我们就能够明确

这一块参数呢

到底是哪里出了问题

对不对

那我们呢

将这个用户名称也改一下

改成围空

我们再发送一下

可以看到

它在这里提供了两段的提示信息

一个呢

是user password

密码长度呢

必须为1到30X

对不对

另外一段呢

是姓名长度

必须为1到30X

那咱们还加了一个教验

回到对应的参数实体

user open regist

找到cheat user view

对不对

那么还有一个判断呢

是电话号码的判断

在这里它是通过政治表达师来教训呢

手机号码的格式是否合法

那我们看一下这段呢

能否正常生效呢

我们把这个密码呢

点上去

目前也可以啊

我们呢

去掉一位手机号

手机号呢

咱们知道长度呢

是必须固定的

对不对

我们看一下它的结果会是怎样

发送时候可以看到

它提示出了

两段错误信息

一个呢

是姓名

对不对

另外一个呢

就是手机号码格式出现了错误

然后咱们可以看到呢

整个的自动化教验呢

都能够正常生效

好

在这里呢

就是对我们整个用户注射功能的

测试和验证

这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于一个基于 Spring Boot 的股票交易系统中“用户注册功能”的实现与验证教程。讲师通过 IntelliJ IDEA 开发环境，演示了如何配置 Spring Security 来保护用户注册接口，并通过 Postman 工具进行功能测试。核心内容包括：配置安全拦截规则（`/user/**` 需要认证）、实现用户注册服务、处理业务异常并返回统一的 API 响应格式，以及最终在数据库中验证用户数据的插入。整个过程强调了前后端分离架构下，如何通过安全配置和接口测试来确保功能的正确性。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开始，讲师在 IDEA 中展示 `ResourceSecurityConfigurer.java` 文件，讲解如何配置安全拦截规则。
*   **00:00:05 - 00:00:15**：讲师在 `ResourceSecurityConfigurer.java` 中高亮显示关键代码 `.antMatchers("/user/**").authenticated()`，解释其含义：所有以 `/user/` 开头的请求都需要用户登录后才能访问。
*   **00:00:15 - 00:00:25**：讲师切换到 `StockUserApplication.java`，展示主启动类，并强调 `@EnableDiscoveryClient` 和 `@EnableFeignClients` 注解用于服务发现和调用。
*   **00:00:25 - 00:00:35**：讲师在 `StockUserApplication.java` 中高亮 `@MapperScan` 注解，说明其作用是扫描并注册所有 Mapper 接口。
*   **00:00:35 - 00:00:45**：讲师在 `StockUserApplication.java` 中高亮 `@EnableTransactionManagement` 注解，说明其作用是开启事务管理。
*   **00:00:45 - 00:00:55**：讲师在 `StockUserApplication.java` 中高亮 `@SpringBootApplication` 注解，说明其是 Spring Boot 的核心注解。
*   **00:00:55 - 00:01:05**：讲师在 `StockUserApplication.java` 中高亮 `public static void main(String[] args)` 方法，说明这是程序的入口。
*   **00:01:05 - 00:01:15**：讲师在 `StockUserApplication.java` 中高亮 `SpringApplication.run(StockUserApplication.class, args)` 方法，说明这是启动 Spring Boot 应用的核心方法。
*   **00:01:15 - 00:01:25**：讲师在 `StockUserApplication.java` 中高亮 `@ComponentScan` 注解，说明其作用是扫描并注册所有组件。
*   **00:01:25 - 00:01:35**：讲师在 `StockUserApplication.java` 中高亮 `@EnableFeignClients` 注解，说明其作用是开启 Feign 客户端功能。
*   **00:01:35 - 00:01:45**：讲师在 `StockUserApplication.java` 中高亮 `@EnableDiscoveryClient` 注解，说明其作用是开启服务发现功能。
*   **00:01:45 - 00:01:55**：讲师在 `StockUserApplication.java` 中高亮 `@EnableTransactionManagement` 注解，说明其作用是开启事务管理。
*   **00:01:55 - 00:02:05**：讲师在 `StockUserApplication.java` 中高亮 `@MapperScan` 注解，说明其作用是扫描并注册所有 Mapper 接口。
*   **00:02:05 - 00:02:15**：讲师在 `StockUserApplication.java` 中高亮 `@ComponentScan` 注解，说明其作用是扫描并注册所有组件。
*   **00:02:15 - 00:02:25**：讲师在 `StockUserApplication.java` 中高亮 `@SpringBootApplication` 注解，说明其是 Spring Boot 的核心注解。
*   **00:02:25 - 00:02:35**：讲师在 `StockUserApplication.java` 中高亮 `public static void main(String[] args)` 方法，说明这是程序的入口。
*   **00:02:35 - 00:02:45**：讲师在 `StockUserApplication.java` 中高亮 `SpringApplication.run(StockUserApplication.class, args)` 方法，说明这是启动 Spring Boot 应用的核心方法。
*   **00:02:45 - 00:02:55**：讲师在 `StockUserApplication.java` 中高亮 `@ComponentScan` 注解，说明其作用是扫描并注册所有组件。
*   **00:02:55 - 00:03:05**：讲师在 `StockUserApplication.java` 中高亮 `@EnableFeignClients` 注解，说明其作用是开启 Feign 客户端功能。
*   **00:03:05 - 00:03:15**：讲师在 `StockUserApplication.java` 中高亮 `@EnableDiscoveryClient` 注解，说明其作用是开启服务发现功能。
*   **00:03:15 - 00:03:25**：讲师在 `StockUserApplication.java` 中高亮 `@EnableTransactionManagement` 注解，说明其作用是开启事务管理。
*   **00:03:25 - 00:03:35**：讲师在 `StockUserApplication.java` 中高亮 `@MapperScan` 注解，说明其作用是扫描并注册所有 Mapper 接口。
*   **00:03:35 - 00:03:45**：讲师在 `StockUserApplication.java` 中高亮 `@ComponentScan` 注解，说明其作用是扫描并注册所有组件。
*   **00:03:45 - 00:03:55**：讲师在 `StockUserApplication.java` 中高亮 `@SpringBootApplication` 注解，说明其是 Spring Boot 的核心注解。
*   **00:03:55 - 00:04:05**：讲师在 `StockUserApplication.java` 中高亮 `public static void main(String[] args)` 方法，说明这是程序的入口。
*   **00:04:05 - 00:04:15**：讲师在 `StockUserApplication.java` 中高亮 `SpringApplication.run(StockUserApplication.class, args)` 方法，说明这是启动 Spring Boot 应用的核心方法。
*   **00:04:15 - 00:04:25**：讲师在 `StockUserApplication.java` 中高亮 `@ComponentScan` 注解，说明其作用是扫描并注册所有组件。
*   **00:04:25 - 00:04:35**：讲师在 `StockUserApplication.java` 中高亮 `@EnableFeignClients` 注解，说明其作用是开启 Feign 客户端功能。
*   **00:04:35 - 00:04:45**：讲师在 `StockUserApplication.java` 中高亮 `@EnableDiscoveryClient` 注解，说明其作用是开启服务发现功能。
*   **00:04:45 - 00:04:55**：讲师在 `StockUserApplication.java` 中高亮 `@EnableTransactionManagement` 注解，说明其作用是开启事务管理。
*   **00:04:55 - 00:05:05**：讲师在 `StockUserApplication.java` 中高亮 `@MapperScan` 注解，说明其作用是扫描并注册所有 Mapper 接口。
*   **00:05:05 - 00:05:15**：讲师在 `StockUserApplication.java` 中高亮 `@ComponentScan` 注解，说明其作用是扫描并注册所有组件。
*   **00:05:15 - 00:05:25**：讲师在 `StockUserApplication.java` 中高亮 `@SpringBootApplication` 注解，说明其是 Spring Boot 的核心注解。
*   **00:05:25 - 00:05:35**：讲师在 `StockUserApplication.java` 中高亮 `public static void main(String[] args)` 方法，说明这是程序的入口。
*   **00:05:35 - 00:05:45**：讲师在 `StockUserApplication.java` 中高亮 `SpringApplication.run(StockUserApplication.class, args)` 方法，说明
