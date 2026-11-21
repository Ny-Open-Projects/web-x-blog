# 05-Sentinel集成使用-用户服务集成Sentinel — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着实现用户符合申请中的集成

在这一讲,咱们先把Controller的结口

以及工程配置做一个实现

咱们找到StockUser,Controller这个结口

在这里面提供的是用户登录的入口

我们可以看到在这里有个错误

我们修改一下

这个是接收客户端的一个请求

那么会进入我们的UserLogin登录的处理方法

在这里咱们是要确保

对Service层的调用进行了一个异常补货

在这里我们可以进入Service逻辑

看到我们是做了一个降级异常的处理

降级的时候它会进入UserLoginHandle

那么它会抛出对应的错误异常

那这错误异常的话

如果咱们在外层不做补货

这个时候客户端

它是不能接收到对应的错误提示信息

这样的话交互起来就不太友善

所以我们在这里对外层做了一个Catch的补货

Catch了Compat的一个Exception

然后将它的Add Code错误码描述

在这里封装返回给客户端

这样的话客户端就能接收到具体的错误提示

到底是降级产生的异常

还是说限流产生的异常

好

在这一块就是Web

我们就变成了一个修改

那接着的话就是修改工程的一个配置文件

在这工程配置文件当中

咱们要去增加Centino的一个集成配置

那咱们去打开我们的Bluetooth Travel

配置文件

在这里面的话

我们之前并没有去实现Centino的接入

对不对

之前的话只是OS2的一个接入认证

接着的话

我们把Centino的配置加入进来

我们在这里是要接入到NUCOS当中

大家注意我们采用的是Push模式的推送方案

大家这个流程一定要理解清楚

那么在这里我们是通过NUCOS作为配置的一个推送

以及配置的拉取

所以在这里我们用户服务

应该要从NUCOS当中去读取对应的配置

对不对

那我们来看一下这一块该怎么去配呢

我们定义一个Centino

然后呢

Transport

下面的话呢

是它的Dashboard环境后台的地址

这个地址的话呢

是采用默认的端口

8090

我们要注意一下

这个配置的话呢

它是要在Splint Cloud下面

在这里呢

它是买卖地的

所以我们要把这个配置要挪下位置

放到那个上面

跟NUCOS是平级的

因为它在Splint Cloud下面

这个时候的话咱们鼠标conceal上面是会能够出现对应的提示

对不对

那说明了这个配置拼写的是正确的

好

这个是dashboard管理后台的配置

申请的管理后台的连接配置

接着的话咱们还配置nucleus

对不对

好

我们在这里这个格式要对齐

然后是data source

这里面的话

它的数据源就是从nucleus里面去获取的

我们是配置两个处理

一个是我们回答整个服务的设计

一个是降级

一个是限流

对不对

那么对应的话

就是user

这个是用户的降级规则配置

这个名称的话

咱们要保持一致

就是跟咱们后台的配置的名称要保持一致

并没有说要局限于它一个固定的

然后那个nucleus

这里面的话是它的连接地址

要7.0.0.1

我们指向的是本地的nucleus

然后是它的data id

nucleus上面的一个配置名称

userdeploy

然后是group id

dfult

就是采用deploy的group

在下面的话是它的一个名称

这个数据类型

数据类型的话

就采用这个type

然后的话是它的lulu

它的规则是降级

对不对

好

你归类了

这一块就是用户降级的一个配置

接下来咱们还配置一个用户限流的

用户限流的话

跟这个配置也是基本上类似的

咱们也给它一个名称

便于dashboard的一个管理

这个是userflow

然后下面的话是nucles

同样的话是sowodps

咱们将这一块copy过来就可以了

copy过来再做一个调整

这样快一点

那么这个data id的话

我们也改一下

这个就不叫degrade

就叫限流

然后group id保持一致

这个datatype是json

luletype是什么

luletype就是flow

对不对

限流的一个配置处理

好

在这一块的话

我们鼠标concili

可以看到这个配置都是ok的

并没有拼写错误

对不对

在这一块就是对sentinel的一个

集成配置

在这里面咱们采用的是nucles

作为数据源的连接

我们就已经实现了

就是用户服务集成这一块

nucles的一个配置和实现

接着的话

就要去在nucles服务当中

建立了对应的配置规则

具体的话

我们是怎么去配置的

配置的文件名称

配置的具体属性

这个在我们下面章节当中

再做讲解

这一讲咱们先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是“交易平台 - Day 8”课程的一部分，主要讲解如何将 **Sentinel** 限流与降级功能集成到一个基于 **Spring Cloud** 和 **Nacos** 的微服务系统中。课程内容聚焦于 **用户服务** 的改造，具体包括：

*   **修改配置文件**：在 `bootstrap.yml` 中配置 Sentinel 监控台的地址、Nacos 的服务发现地址以及用户降级和限流规则的配置项。
*   **服务端代码改造**：在 `StockUserServiceImpl` 中，为 `userLogin` 方法添加 `@SentinelResource` 注解，以启用 Sentinel 的熔断降级功能，并在方法内模拟异常抛出，以便触发降级。
*   **客户端代码改造**：在 `StockUserController` 中，将服务调用的异常捕获并包装成统一的 `ApiRespResult` 对象，以便前端能统一处理。
*   **规则配置**：通过 Nacos 配置中心，为用户服务配置降级和限流规则，实现动态控制。

整个过程旨在演示如何在实际项目中应用 Sentinel，实现服务的高可用和流量控制。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:15**: **课程目标与大纲介绍**。展示课程目标和学习大纲，明确本节将讲解 Sentinel 集成和用户注册功能的实现。
*   **00:16 - 00:30**: **修改工程配置文件**。在 `bootstrap.yml` 中添加 Sentinel 监控台地址、Nacos 配置中心地址以及用户降级和限流规则的配置项。
*   **00:31 - 00:45**: **服务端代码改造**。在 `StockUserServiceImpl` 中为 `userLogin` 方法添加 `@SentinelResource` 注解，并在方法内模拟异常抛出。
*   **00:46 - 01:00**: **客户端代码改造**。在 `StockUserController` 中，将 `userLogin` 方法的异常捕获并包装成 `ApiRespResult.error` 对象。
*   **01:01 - 01:15**: **规则配置说明**。讲解如何通过 Nacos 配置中心创建和管理降级和限流规则，并强调不同版本的配置差异。
*   **01:16 - 01:30**: **演示与总结**。展示最终的配置和代码结构，并总结本节的核心知识点。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 图表

*   **Sentinel 集成架构图**：展示了 Sentinel Dashboard、远程配置中心（如 Nacos）与多个应用实例（Machine 1, 2, 3）之间的关系，说明了 Sentinel 的“Push 推送模式”。
*   **Nacos 配置管理界面截图**：展示了在 Nacos 中创建 `sentinel-user-degrade` 和 `sentinel-user-flow` 两个配置项的过程。

#### 代码

*   **`bootstrap.yml` 配置文件**：
    ```yaml
    spring:
      application:
        name: stock-user
      cloud:
        nacos:
          discovery:
            server-addr: 127.0.0.1:8848
          config:
            server-addr: 127.0.0.1:8848
        sentinel:
          transport:
            dashboard: 127.0.0.1:8090
          datasource:
            # 用户的降级规则配置
            user-degrade:
              nacos:
                server-addr: 127.0.0.1:8848
                dataId: sentinel-user-degrade
                groupId: DEFAULT_GROUP
                data-type: json
                rule-type: degrade
            # 用户限流的规则配置
            user-flow:
              nacos:
                server-addr: 127.0.0.1:8848
                dataId: sentinel-user-flow
                groupId: DEFAULT_GROUP
                data-type: json
                rule-type: flow
    ```

*   **`StockUserServiceImpl.java` 代码**：
    ```java
    @Override
    @SentinelResource(value = "userLogin", blockHandler = "userLoginHandler")
    public TradeUser userLogin(String userNo, String userPwd) throws ComponentException {
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
            log_error(ApplicationErrorCodeEnum.USER_PWD_ERROR);
            throw new ComponentException(ApplicationErrorCodeEnum.USER_PWD_ERROR);
        }
        return tradeUser;
    }
    ```

*   **`StockUserController.java` 代码**：
    ```java
    @RequestMapping("/userLogin")
    public ApiRespResult userLogin(@RequestParam("userNo") String userNo, @RequestParam("userPwd") String userPwd) {
        ApiRespResult result = null;
        try {
            // 用户登录逻辑处理
            TradeUser tradeUser = stockUserService.userLogin(userNo, userPwd);
            result = ApiRespResult.success(tradeUser);
        } catch (ComponentException e) {
            log.error(e.getMessage(), e);
            result = ApiRespResult.error(e.getErrorCodeEnum());
        } catch (Exception e) {
            log.error(e.getMessage(), e);
            result = ApiRespResult.sysError(e.getMessage());
        }
        return result;
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：配置文件修改演示**。
    *   **描述**：讲师在 IDE 中打开 `bootstrap.yml` 文件，逐行添加 Sentinel 的配置项，包括监控台地址、Nacos 地址以及降级和限流规则的配置。重点演示了 `user-degrade` 和 `user-flow` 两个配置块的结构和参数。
    *   **技术要点**：配置项的命名规范（如 `user-degrade`、`user-flow`）和 Nacos 的 `dataId`、`groupId`、`data-type` 参数的含义。

*   **场景二：服务端代码改造演示**。
    *   **描述**：讲师在 `StockUserServiceImpl.java` 文件中，为 `userLogin` 方法添加 `@SentinelResource` 注解，并在方法内添加了模拟异常的代码，如 `throw new ComponentException(ApplicationErrorCodeEnum.FAILURE);`。
    *   **技术要点**：`@SentinelResource` 注解的 `value` 和 `blockHandler` 属性的使用，以及如何在服务端模拟异常以触发降级。

*   **场景三：客户端代码改造演示**。
    *   **描述**：讲师在 `StockUserController.java` 文件中，将 `userLogin` 方法的 `try-catch` 块中的异常处理逻辑修改为统一的 `ApiRespResult` 对象，并使用 `ApiRespResult.error` 和 `ApiRespResult.sysError` 方法包装异常信息。
    *   **技术要点**：统一异常处理的思路，以及如何将不同类型的异常包装成统一的返回格式。

*   **场景四：Nacos 配置中心演示**。
    *   **描述**：讲师在 Nacos 配置管理界面中，创建了 `sentinel-user-degrade` 和 `sentinel-user-flow` 两个配置项，并展示了其配置内容。
    *   **技术要点**：Nacos 作为配置中心在 Sentinel 中的应用，以及如何通过配置中心动态管理降级和限流规则。

*   **场景五：架构图讲解**。
    *   **描述**：讲师展示了 Sentinel 的“Push 推送模式”架构图，解释了 Sentinel Dashboard、远程配置中心和应用实例之间的关系。
    *   **技术要点**：Sentinel 的分布式部署模式，以及如何通过远程配置中心实现规则的集中管理和动态更新。
