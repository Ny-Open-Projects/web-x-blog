# 04-Sentinel集成使用-功能设计流程 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着的话呢

咱们就开始学习呢

用户服务去集成Sentinel的使用

那咱们来看一下

首先我们要加入Sentinel的组件依赖

那么将以下组件呢

加入到咱们的用户服务当中

咱们来copy下

放到呢

FastTalk User服务工程下面

找到POM文件

那咱们呢

把它放在最下面

这些依赖呢

之前咱们讲Sentinel使用的时候呢

也做过的介绍

对不对

那么现在的话呢

咱们是要集成在项目当中

那么项目当中的话呢

一咱们要有一个Sentinel

Narcos的一个数据源依赖

因为咱们呢

刚才也讲了

是采用了Push的模式进行的一个实现

所以在这里呢

会依赖于Narcos数据中心

作为我们的数据源

接着的话呢

是Sentinel Data Source

这个呢

是Splint Cloud Alibaba呢

帮我们做了一个封装

然后的话呢

是Splint Cloud Alibaba的话呢

对Sentinel做了一个封装实现

大家呢

把这三个组件

加入到咱们的工程服务当中

就可以了

那接着的话呢

咱们再看一下

加完这个依赖之后呢

我们呢

就开始修改用户登录接口

对不对

这个的话呢

怎么去改呢

这个Sentinel集成起来

能不能快速去实现呢

要做哪些配置

咱们呢

先来看一下它的官方文档说明

在这里面呢

Sentinel的接入来讲

非常简单

官方的话呢

也是本着简单易用的原则

做的设计和实现

那么咱们可以看到

在这里呢

咱们只需要加上Sentinel Resource的注解

就可以了

通过这个注解呢

我们就可以控制它的

熔断降级的处理策略

那在这里呢

它有哪些参数呢

可以看到它有资源名称

Entry的类型

Block handle

在这里面的话呢

Block handle

它对应处理的类型呢

Block exception的函数名称

Fallback函数名称呢

顾名思义

是做一个回调

也就是说抛出一行长的时候呢

要做一个Fallback回调的处理

Fallback函数呢

它可以针对所有类型的一长

而Block handle呢

它针对的是Block exception

再往下面的话呢

是Default Fallback

这个呢

是一个默认的Fallback函数名称

可选项

一般呢

咱们配置Fallback就可以了

如果是通用性比较强呢

咱们可以配置一个Default Fallback

再往下面的话呢

是一个Exception to Enogy

也就是说有哪些异常呢

咱们不想去触发它的垄断或降级

那么呢

我们就要去做一个指定的排除

在这里可以看到

非常的简单

对不对

咱们呢

只需要加上这个注解

这里是一个示例

然后的Block handle

是一个Exception的一个Handle

Fallback呢

它会到Hello Fallback里面函数

去做对应的处理

好

在这里呢

咱们给大家呢

简单的讲解了一下

Sentinel的一个

集成使用

那接下来呢

咱们就

从实际代码工程当中

来对Sentinel的集成呢

做到实现

咱们呢

回到代码当中

在这里呢

我们找到用户登录的方法

那我们呢

加上Sentinel Resource

S E N

E I N U Resource

在这里面怎么配置呢

首先咱们要给它配置一个Value

这个Value的话呢

我们给它一个名称

这个呢

是一个支援名称的

表示

我们配置任何降级

熔断降级

撤离的时候呢

一定要把这个名称配置上去

否则的话呢

你通过申请的监控管理后台呢

如果没有这个标识

它是没法进行一个对应和关联匹配的

那么我们再定义什么

Block handle

Block handle的话呢

对应的就是熔断降级时候的方法处理

在这里呢

它就会记录到我们所定义的这个方法

我们这个方法名称呢

就叫UseLockingHandle

在这里面的话呢

我们看一下还有

刚才所讲的BlockingHandle

这个Fallback参数

这个Fallback跟这个Block handle

它们有什么样的区别呢

那咱们来扩展一下

咱们可以看到官方文档上面的它的参数说明

对不对

Fallback函数呢

它是用于抛出异常词提供的Fallback处理逻辑

那么Block handle呢

它对应的是什么

BlockException的函数名称

那这个意思的话呢

也就是说你抛出了BlockException

那么呢

它就会记录Block handle

对不对

如果说你没有配置这个

配置了Fallback

那么只要它抛出异常

就会进入Fallback处理逻辑

那么咱们呢

再来看一下

在这里呢

如果是又配置了Block handle

和也配置了Fallback

对不对

我们俩都配置了

那咱们在这里可以看到

在这两个参数都配置的情况下面

它在这里呢

如果是触发了限流和降级

抛出了BlockException时

它只会进入Block handle

那么

Fallback呢

它的优先级就次一级

不会进入Fallback的处理

这一点呢

大家要注意

如果没有抛出BlockException

是其他的一个异常

那么呢

它就进入Fallback的一个处理

也就是说这两者同时配置的话呢

如果是触发了BlockException优先的话呢

会进入Block handle的一个处理

这一点呢

咱们明确之后

那么呢

咱们在这里配置一个Block handle的方法就可以了

对不对

那么配置完这个方法之后呢

咱们再做一个这个方法的具体实现

在这里的话呢

这个方法该怎么去实现呢

如何去定义

我们来编写一下

Ubricate

ShadeUser

在这里面呢

同样也返回一个User对象

然后的话呢

Handle

在这里面呢

要跟这个方法保持一致

然后它的参数呢

我们也保持一致

让它呢copy过来

咱们还要加上一个User对象呢

加上一个参数是BlockException

因为的话呢

刚才也讲了

对不对

它会抛出BlockException的时候呢

就会记录这个方法

所以呢

它就能够拿到BlockException这个参数

在这里呢

咱们还可以再去抛出对应的一长

比如咱们是封装的Compat的一长

这个是咱们制定封装的一长

那么加上一个注释

它的意思呢

是用户登录限流

处理逻辑

好

那我们看一下方法的具体实现

该怎么去做呢

首先咱们加上一个日志

这边的话呢

就是user

打一个提示

Block

用户登录方法呢

做了一个限流处理

对不对

然后呢

第二用了咱们的userLoginHandle

在这里呢

咱们也将它的一长细节呢

反映一下

这样呢

便于我们的调试

对不对

接着的话呢

咱们来看要做什么事情呢

第一

咱们要获取了熔断线流的条件

的规则

第二步呢

咱们可以根据不同的规则进行

不同逻辑的处理

那最后一步呢

就是如果在默认情况下面

它没有符合对应的一长

不符合配置的规则

就进入了系统一长

这呢

是这里面所谓的方法述述逻辑

那咱们一步一步来做一个实现

apps check

然后在这里呢

是LULU

给它创建一个对象

给它获取

可以从blocking一个setup里面

获取它的一个

熔断线流的规则

那拿到这个规则之后呢

咱们就要做一个判断

if apps check the LULU

因为呢

这是一个通用的接口

对不对

咱们可以看一下

是一个抽象类

它下面的话呢

有很多的实现

我们可以看一下

对不对呢

对不对

有限流的

有那个降级的

很多的一些实现

那咱们要做一个判断

如果说你是一个降级的

degrade

degrade

举ID

LULU

那如果是你是降级的话呢

我们就抛出一个一长

compendant exception

那这一长的话呢

我们就叫做

assist

assist

就是系统谈判

这个呢

就是符合

咱们的整个功能的设计

咱们可以再回过头来看一下

如果是大家没有印象

我记不清楚的话

咱们来看一下

在这功能设计的时候

降级的话呢

我们会触发一个系统反盲

对不对

限流的话呢

会触发一个稍后重视

那我们呢

怎么去实现

就是根据这个异常来做呢

不同的处理

好

接着的话呢

我们再做一个LGE

然后呢

apps check LULU

extends of

然后是flow

LULU

在这里面呢

咱们也抛出一个异常

compound exception

它错误码呢

就是限流

system flow

就是请稍后再重视

好

最后呢

也就是说

在这里面

它都不符合熔断

或者是限流呢

咱们就抛出一个系统的异常

就超出咱们的预期了

对不对

compound exception

application

在这里面的话呢

就fill

就返回错误

一般情况下呢

只要咱们是配置正确的

能够正常进入到这个方法

它呢

就可以进入到这里面的两个流程分支

去做对应的处理

除非是出现配置方面的一些异常

或是位置的情况

才会进入下面的逻辑

好

在这一块呢

就是对整个熔断和限流的一个处理

咱们呢

再回到讲义当中

去回顾一下刚才的代码实现

在这里面咱们加入一个熔断

降级的一个选项

这个是一个降级的一个处理方法

那么再往下面呢

咱们要注意一下

采用Sentinel的source的这个注解

定义资源

名称与降级方法

这个呢是它的作用

咱们要注意1.6.0以下的版本

也就是Sentinel1.6.0以下版本呢

降级它只支持degrade一个exception一场

也就是说你只有呢

抛出degrade一个exception呢

它才会触发降级的处理

而在这里呢

咱们可以看到它会抛出什么block一个exception

对不对

好

这个呢是它的版本上面的一些差异

但是功能呢

都是一样的

都是要实现了它的一个熔断降级的处理

用户登录方法呢

如果是符合降级规则

它就会进入uselogin fallback的方法

里面呢

会返回一个not对象

咱们可以看到

uselogin

为了方便做这个验证的话呢

咱们呢

在代码里面模拟了一个一场

抛出了application

addcode animal

这个fuel

这个错误嘛

使用compend的一个exception呢

不要抛出degrade的exception

否则只要出现了该一场呢

它就会进入什么

降级的处理

在这里呢

咱们可以看到

我们模拟的降级一场呢

抛出的都是compend的exception

对不对

所以呢

为了能够让它触发降级

也能够触发限流呢

咱们呢

就抛出compend的exception

千万不要抛出degrade的exception

这个呢是指定只会触发降级的

配置的

它就会呢

根据你的降级规则条件

来触发

对应的

一个熔断

好

最后呢

咱们再注意一下

如果是在同一个方法方面

我们同时呢

是配置的降级和限流的处理规则

那么它还怎么去做呢

它会优先进入block handle里面

所定义的方法

也就是咱们在这里面定义的block handle

对不对

如果没有定义block handle

或者fallback等任何呢

熔断限流的处理属性

那么呢

它就会抛出block exception

也就是说在这里面的话

咱们这个也没有定义

fallback也没有定义

那么呢

它就会将这个异常呢

抛入出去

block exception

在这里呢

咱们那个

还要加上一个模拟异常

对不对

否则的话呢

如果是按正常逻辑处理完成之后

它呢

是不会触发任何的熔断和限流的

那么在这里呢

我们把这个异常增加进去

好

那在这里呢

就是对用户服务和Sentinel

做了一个集成配置

这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频是关于在 Spring Cloud 微服务架构中集成阿里巴巴开源的流量控制与熔断降级框架 **Sentinel** 的实战教程。课程聚焦于如何将 Sentinel 的限流和降级功能应用到一个用户登录服务中。讲师通过修改 Maven 依赖、编写注解、处理异常和配置规则，演示了如何在服务出现异常或流量过大时，自动触发降级或限流，从而保护系统稳定。整个过程结合了代码编写、官方文档查阅和架构图理解，旨在帮助开发者掌握 Sentinel 在生产环境中的落地应用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，展示课程大纲，明确本节目标是“修改用户服务，集成 Sentinel 的降级与限流功能”。
*   **00:06 - 00:15**: 展示并讲解 `pom.xml` 文件，添加 Sentinel 的核心依赖和数据源依赖，为后续功能实现做准备。
*   **00:16 - 00:25**: 讲解 Sentinel 的注解支持，重点介绍 `@SentinelResource` 注解的用法，包括 `value`、`blockHandler` 等关键属性。
*   **00:26 - 00:35**: 在 `StockUserServiceImpl` 服务类中，为 `userLogin` 方法添加 `@SentinelResource` 注解，并编写 `blockHandler` 方法来处理被拦截的异常。
*   **00:36 - 00:45**: 详细讲解 `blockHandler` 方法的实现逻辑，包括如何根据异常类型（如降级或限流）抛出不同的业务异常。
*   **00:46 - 00:55**: 在 `userLogin` 方法中，模拟异常并调用 `blockHandler`，演示 Sentinel 如何拦截并处理异常。
*   **00:56 - 01:05**: 代码编写完成，展示最终的 `userLogin` 方法，包含用户登录逻辑、异常模拟和 Sentinel 注解的完整配置。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **课程大纲**: 明确了本节的学习目标，包括“修改用户服务”、“集成 Sentinel”、“实现降级与限流”。
    *   **架构图**: 展示了服务注册、Sentinel 控制台、Nacos 配置中心的协作关系，以及降级和限流的触发点。
    *   **官方文档**: 引用 Sentinel 官方文档，解释 `@SentinelResource` 注解的属性和 `blockHandler` 的工作原理。

*   **关键代码**:
    *   **Maven 依赖**:
        ```xml
        <!-- Sentinel 限流组件 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
        </dependency>
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-alibaba-sentinel-datasource</artifactId>
        </dependency>
        <dependency>
            <groupId>com.alibaba.csp</groupId>
            <artifactId>sentinel-datasource-nacos</artifactId>
        </dependency>
        ```
    *   **服务方法注解**:
        ```java
        @SentinelResource(value = "userLogin", blockHandler = "userLoginHandler")
        public TradeUser userLogin(String userNo, String userPwd) throws Exception {
            // 业务逻辑
        }
        ```
    *   **降级/限流处理方法**:
        ```java
        public TradeUser userLoginHandler(String userNo, String userPwd, BlockException ex) {
            AbstractRule abstractRule = ex.getRule();
            if (abstractRule instanceof DegradeRule) {
                throw new ComponentException(ApplicationErrorCodeEnum.SYS_BUSY);
            } else if (abstractRule instanceof FlowRule) {
                throw new ComponentException(ApplicationErrorCodeEnum.SYS_FLOW);
            }
            // 默认处理
            throw new ComponentException(ApplicationErrorCodeEnum.SYS_ERROR);
        }
        ```
    *   **业务逻辑**:
        ```java
        // 模拟降级异常
        if ("error".equals(userNo)) {
            throw new ComponentException(ApplicationErrorCodeEnum.FAILURE);
        }
        // 获取用户对象
        TradeUser tradeUser = stockUserDao.getByUserNo(userNo);
        if (null == tradeUser) {
            throw new ComponentException(ApplicationErrorCodeEnum.USER_NOT_FOUND);
        }
        // 用户密码加密判断
        String encryptPassword = EncryptUtil.encryptSigned(userPwd);
        boolean pwdMatch = tradeUser.getUserPwd().equals(encryptPassword);
        if (!pwdMatch) {
            log.error(ApplicationErrorCodeEnum.USER_PWD_ERROR);
            throw new ComponentException(ApplicationErrorCodeEnum.USER_PWD_ERROR);
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：环境准备与依赖配置** (00:06-00:15)
    *   讲师在 IDE 中打开 `pom.xml` 文件，通过鼠标点击和高亮，演示如何添加 Sentinel 的核心依赖和 Nacos 数据源依赖。他强调了这些依赖是后续功能实现的基础。

*   **场景二：注解配置与异常处理** (00:26-00:45)
    *   讲师在 `StockUserServiceImpl` 类中，为 `userLogin` 方法添加 `@SentinelResource` 注解，并编写 `userLoginHandler` 方法。他通过鼠标悬停和高亮，解释了 `value` 和 `blockHandler` 的作用。
    *   在 `userLoginHandler` 方法中，他演示了如何通过 `ex.getRule()` 获取触发异常的规则，并根据规则类型（`DegradeRule` 或 `FlowRule`）抛出不同的业务异常，从而实现降级或限流的逻辑。

*   **场景三：业务逻辑与异常模拟** (00:46-01:05)
    *   讲师在 `userLogin` 方法中，编写了完整的用户登录业务逻辑，包括用户对象查询、密码比对等。
    *   他通过注释 `// 模拟降级异常`，在方法中添加了模拟异常的代码，以演示 Sentinel 如何拦截并处理异常。
    *   最后，他展示了完整的代码，强调了 Sentinel 注解如何与业务逻辑无缝集成，实现流量控制和熔断降级。

---

以上是根据视频画面进行的详细技术分析，希望能帮助您更好地理解 Sentinel 在微服务中的集成与应用。
