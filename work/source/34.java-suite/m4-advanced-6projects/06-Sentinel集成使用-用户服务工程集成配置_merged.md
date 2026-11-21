# 06-Sentinel集成使用-用户服务工程集成配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来那接着呢咱们就来实现Nacos上面的熔断和限流规则的配置

那咱们呢首先要启动Nacos服务

然后呢咱们在Nacos的控制后台当中

配置列表的菜单里面去创建两项配置

一项呢是它的降级一项呢是限流

好那Nacos服务呢在这里我已经将它启动完成

启动完成之后呢咱们就来访问Nacos服务

本机端口8848

接着的话呢咱们打开配置列表

在这里呢之前测试的时候有一项配置对不对

那接着的话呢咱们来创建两个新的配置

点击新增

Data ID的话呢我们给它一个名称

要申请了

这个呢是跟咱们的配置当中的名称呢是一致的

这个是降级咱们可以看一下在那个配置文件当中

是有一项那个名称对不对

申请了UserDeclared

咱们要检索一下

确保了名称是完全匹配

好

那接着换了它的格式是json

json格式咱们来看一下它具体规则是什么呢

我们先把它拷贝进去

然后呢

创建点击发布

这样呢就发布完成咱们再点击配置列表

可以看到了

申请了UserDeclared

就已经创建成功

咱们看下它的详情

在这里面的话呢

我们是配置了它的一个Resource

资源名称对不对

资源名称的话呢是UserLogin

这个呢

大家还有没有印象

UserLogin对应的就是咱们service里面的申请了Resource

注解当中的Value的值

UserLogin

那么这个Count是它的一个降级的这个比例

咱们可以看到这里呢

0到1

是从0到100%

那如果是0.2呢

就代表20%

Glued呢

是它的降级策略

0呢

是代表响应时间

根据响应时间来做

1呢

是代表异常比例

那咱们这里设置的是1

就是异常比例

对不对

当然了

还可以根据代表的异常数量

这里呢

根据自己的业务需要

选择了不同的配置策略

TimeWindow呢

是它的一个时间长

在这里呢

配置为4秒

也就是经过4秒之后呢

它会尝试进行恢复

那整体的这个意思呢

就是说

咱们呢

如果是业务方法处理的时候

这个异常比例呢

超过了20%

也就是说你发起两次请求

有一次呢

就是造成失败

那么呢

就是50%

对不对

已经超过了20%的

它的比例要求

那么呢

就会触发它的一个降级的策略

接下来呢

咱们再看一下

Synion Userflow的

先流配置策略

先流配置策略

那咱们呢

在NUC上面

去创建一下

点击新增

这台ID呢

咱们去输入

Synion Userflow

这个配置格子呢

仍然是采用JSON

那咱们呢

将它的配置值呢

拷贝过来

接着的话呢

点击发布

咱们呢

返回配置列表

好

咱们看一下呢

这个配置的具体说明

在这里

Resource是支援名称

跟我们上面的这个名称呢

都是一样的

对不对

最主要呢

它是要匹配

我们User Service里面

定义的User Logging

好

这个呢

要匹配正确

然后的话呢

咱们可以看到

这个先流配置策略

具体是怎样控制呢

定义了一个ControlBehaviour

在这里呢

它的值是0

在这里

这个属性值是什么意思呢

它是流量整形的一个控制效果

它目前支持呢

快速失败

以及呢

匀速排队两种模式

默认呢

是0

也就是说快速失败

只要说你超过了我的先流

那么呢

就立马触发失败

如果是作为匀速排队呢

那它就会把你的流量呢

作为一个整合

然后的话呢

按照那个排队的顺序呢

有序的进行一个触发调用

下面的话呢

是Count

这个呢

是现成的数量

也就是说咱们在这里呢

先流的时候

它的现成控制数量呢

是为12个

那Grade呢

是先流的配置策略

0呢

是代表现成数量

对不对

1呢

就是代表QPS的引发数

对不对

那么LimitApp呢

它是现流针对的来源

在这里呢

填写Depot就可以了

Storage是基于调用关系的流量控制策略

在这里面呢

具体有三种

咱们来看一下

分别代表什么意思呢

第一种呢

0StorageDelete

这个是根据调用方进行现流

结合呢

LimitApp去做使用

如果这调用方呢

在这里面

比如说是第三方的一个来源

那么呢

它在这里就会根据你的调用方

进行一个配合的现流处理

在这里呢

1

1的意思呢

它是一个Relate

对不对

根据关联的流量进行现流

也就是说

当多个资源之间呢

具有资源的增强和关联关系的时候

比如说

同一个数据表当中的读和写请求

对不对

如果是写操作比较频繁了

那么读数据的请求呢

它就会被现流处理

比如说我要去修改一个订单

先要查出这个订单

然后再做对应的修改

那么如果是你写操作

就修改起来比较频繁了

它的读取是不是也会

同样受到现流的处理呢

对不对

因为呢

它们是一个关联的操作

那么咱们再看一下

值为R的时候呢

它是一个Chain

这个Chain的话呢

就是一个调用链

它是根据调用链的路口来进行现流

这个具体是什么意思呢

比如说在这里有两个请求

对不对

一个请求呢

是Request1

那么的话呢

还有一个请求的话呢

是Request2

咱们在这里标记一下

那么呢

Request1呢

是一个

是作为你的第一个调用环节

调用完Request1之后呢

接着它又去调用Request2

那么呢

每个请求呢

它肯定是落在不同的服务上面

比如说这个呢

是它的订单服务

这个呢

是它的直进服务

对不对

这两个的话呢

就组成了一个什么

调用链

这个时候呢

它就会配合咱们设置的LiveResource

配合这个属性值呢

它如果是指定Request1

它就会配合咱们设置的LiveResource

那么它对应的话呢

Request1就会受到限流的控制

因为呢

它是根据调用链的入口

对不对

而Request1呢

正好是它的入口

那么Request2呢

就可以进行一个方形

这个呢

是它的一个欠的控制策略

在这里面咱们要注意

配置的内容呢

是采用阶层的格式

我们一定要符合它的要求

如果是填写错误了

在这里面的话呢

不是按照阶层格式去填写的

它可能呢

就会报错

比如说你多了一个逗号啊

或者它的格式

不是按照阶层这样拼装的

那么呢

就会有对应的错误

虽然在这里呢

不会提示出来

但在使用的时候呢

就不会生效

这一点呢

大家要注意一下

好

那这一块呢

就是基于NACOS的一个

熔断限流规则的配置处理

以及呢

对降级和限流配置

我们做的具体的讲解

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是关于在 Spring Cloud 微服务架构中集成阿里巴巴开源的流量控制组件 **Sentinel** 的技术教程。课程主要演示了如何配置 **熔断降级** 和 **流量限流** 两种核心策略，并通过 **Nacos** 作为配置中心进行动态管理。视频内容聚焦于用户登录服务的实现，通过在 `StockUserServiceImpl` 中编写 `@SentinelResource` 注解来定义规则，并在 `Nacos` 中配置对应的 JSON 格式规则。讲师强调了在处理降级和限流异常时，应使用 `ComponentException` 而非 `DegradeException`，以避免不必要的服务降级。整个过程展示了从代码编写、配置中心配置到最终生效的完整流程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：课程开场，展示课程大纲，介绍本节将讲解 Sentinel 的集成与使用。
*   **00:00:05 - 00:00:15**：讲解熔断降级配置，展示 `sentinel-user-degrade` 的 JSON 配置内容。
*   **00:00:15 - 00:00:25**：讲解流量限流配置，展示 `sentinel-user-flow` 的 JSON 配置内容。
*   **00:00:25 - 00:00:35**：在 Nacos 配置中心创建并发布熔断降级规则。
*   **00:00:35 - 00:00:45**：在 Nacos 配置中心创建并发布流量限流规则。
*   **00:00:45 - 00:00:55**：在 `StockUserServiceImpl` 中编写 `@SentinelResource` 注解，定义降级和限流处理逻辑。
*   **00:00:55 - 00:01:05**：讲解 `BlockHandler` 和 `fallback` 的区别，强调应使用 `ComponentException`。
*   **00:01:05 - 00:01:15**：总结本节内容，强调配置的正确性和异常处理的重要性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### **PPT / 文档内容**

*   **熔断降级配置 (sentinel-user-degrade)**：
    ```json
    [
      {
        "resource": "userLogin",
        "count": 0.2,
        "grade": 1,
        "timeWindow": 4
      }
    ]
    ```
    *   `resource`: 资源名称。
    *   `count`: 降级阈值，为百分比 [0-1]，这里表示 20%。
    *   `grade`: 降级策略，0 代表响应时间，1 代表异常比例，2 代表异常数量，这里采用的是异常比例。
    *   `timeWindow`: 降级时间窗，单位为秒。

*   **流量限流配置 (sentinel-user-flow)**：
    ```json
    [
      {
        "resource": "userLogin",
        "controlBehavior": 0,
        "count": 12,
        "grade": 1,
        "limitApp": "default",
        "strategy": 0
      }
    ]
    ```
    *   `resource`: 资源名称。
    *   `controlBehavior`: 流量整形的控制效果，目前支持快速失败和匀速排队两种模式，默认是 0，快速失败。
    *   `count`: 线程数量。
    *   `grade`: 限流配置策略，0 代表线程数量，1 代表 QPS 并发数。
    *   `limitApp`: 限流针对的来源，填写 `default` 即可。
    *   `strategy`: 基于调用关系的流量控制策略，有三种：
        1.  `0-STRATEGY_DIRECT`：根据调用方进行限流，结合 `limitApp` 使用。
        2.  `1-STRATEGY_RELATE`：根据关联流量限流，当多个资源间具有资源竞争和关联关系的时候，比如同一个数据库的读与写操作比较频繁，那么多个数据的请求就会被限流处理。
        3.  `2-STRATEGY_CHAIN`：根据调用链的入口流限流，比如两个请求 Req1 和 Req2，同时再配合设置 `FlowRule.releResource` 指定 Req1 为入口请求，那么 Req1 就会受到限流控制，Req2 则可放行。

#### **代码关键内容**

*   **`StockUserServiceImpl.java` 中的 `@SentinelResource` 注解**：
    ```java
    @SentinelResource(value = "userLogin", blockHandler = "userLoginHandler")
    public TradeUser userLogin(String userNo, String userPwd) throws ComponentException {
        // 业务逻辑
        if ("error".equals(userNo)) {
            throw new ComponentException(ApplicationErrorCodeEnum.FAILURE);
        }
        // 获取用户对象
        return userLoginHandler(userNo, userPwd);
    }
    ```

*   **`userLoginHandler` 方法**：
    ```java
    public TradeUser userLoginHandler(String userNo, String userPwd, BlockException ex) throws ComponentException {
        Log.error("userLogin flow limit, call userLoginHandler: " + ex.getMessage());
        AbstractRule abstractRule = ex.getRule();
        if (abstractRule instanceof DegradeRule) {
            throw new ComponentException(ApplicationErrorCodeEnum.SFS_DES);
        } else if (abstractRule instanceof FlowRule) {
            throw new ComponentException(ApplicationErrorCodeEnum.SFS_FLOW);
        }
        // 默认情况，抛出系统异常
        throw new ComponentException(ApplicationErrorCodeEnum.FAILURE);
    }
    ```

---

### 4) 关键场景与演示描述

1.  **场景一：配置中心创建熔断规则**
    *   **描述**：讲师在 Nacos 配置中心的 `DEFAULT_GROUP` 组中，创建名为 `sentinel-user-degrade` 的配置项，并将 JSON 格式的熔断规则粘贴进去，然后点击“确定”按钮发布配置。

2.  **场景二：配置中心创建限流规则**
    *   **描述**：讲师在 Nacos 配置中心的 `DEFAULT_GROUP` 组中，创建名为 `sentinel-user-flow` 的配置项，并将 JSON 格式的限流规则粘贴进去，然后点击“确定”按钮发布配置。

3.  **场景三：代码实现降级与限流逻辑**
    *   **描述**：讲师在 IntelliJ IDEA 中打开 `StockUserServiceImpl.java` 文件，为 `userLogin` 方法添加 `@SentinelResource` 注解，并指定 `blockHandler` 为 `userLoginHandler` 方法。然后在 `userLoginHandler` 方法中，根据捕获到的异常类型（`DegradeRule` 或 `FlowRule`）抛出不同的 `ComponentException`，以实现降级和限流的逻辑。

4.  **场景四：异常处理策略说明**
    *   **描述**：讲师在 PPT 上强调，为了防止服务降级，应使用 `ComponentException` 而非 `DegradeException`。只有当出现 `DegradeException` 时，才会触发降级。同时，如果在同一个方法上同时配置了降级和限流规则，系统会优先执行 `BlockHandler` 定义的方法。

5.  **场景五：配置文件内容展示**
    *   **描述**：讲师在 Typora 中展示 `sentinel-user-degrade` 和 `sentinel-user-flow` 的 JSON 配置内容，并逐项解释各个字段的含义，如 `resource`、`count`、`grade`、`timeWindow`、`controlBehavior`、`limitApp` 和 `strategy` 等。

---

以上是根据视频画面进行的详细技术分析，希望能帮助您更好地理解 Sentinel 的集成与使用。
