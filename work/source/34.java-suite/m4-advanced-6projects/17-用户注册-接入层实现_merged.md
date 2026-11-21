# 17-用户注册-接入层实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们呢

接着对接入层的代码

做个具体实现

在stockuser

controller包下面呢

创建一个新的类

名称呢,我们叫stocker

user open controller

我们要提供注册的接口

好

创建完成之后呢

给它加上对应的注解

这个呢,是一个

controller list

然后呢,给它定一个请求路径

request mapping

我们就叫open

通过long block呢,给它一个

日字的注解

好,接着的话呢

我们再来实现呢,它的注册

接口

在这里面呢,定一个通用的

返回对象,API respawn的

request

这个呢,就是提供用户注册的

接口

Valid呢,是做一个校验

那在下面的赵尼的网络呢

咱们还会对自动化校验做一个具体的讲解

在这一讲呢

咱们先来实现了用户注册的接口

接着的话呢

咱们也加上对应的注解

用户注册接口

那我们看一下

怎么去组装返回数据呢

首先咱们要定一个通用的返回对象

API respawn result

这个呢,给一个空置

接着的话呢

咱们要去调用它的service我记者

对不对

那么首先呢

要将这个service注入进来

i stock user service

下面这个

加上了对应的注解

valid

这个呢

就是用户的服务层接口

那我们看一下了

怎么去调用

首先呢

咱们去调用stock user service

user.js的方法

这个呢

还没提供出来

对吧

那我们呢

来看一下它的service层

我们在上一讲了

是对业务层做了一个实现

但是呢

还没有抽把它抽取到接口

层

当中

那我们来将它抽取一下

refact formen bussup

在这里面的话呢

我们选中user.js

然后呢

copy

点击refact

这样呢

它就把我们的抽取到接口层当中

那我们再来看一下

user.js

传递呢

对应的user对象

在这里面呢

还会将它的用户信息呢

进行返回

我们可以看到

确定user

会生成一个新的用户对象

对不对

好

那这里呢

就是对它结果的一个包装返回

这里面api

respond result

就是一个成功的结果

如果能够执行到这里

对不对

确定user

在这里呢

报错

咱们来看一下

它是什么

它说这个呢

vue对象

咱们传递的参数类型呢

是不对的

咱们呢

将它的参数类型呢

改成呢

确定user.vo

咱们再看一下

还是报错

对不对

那是这个错误呢

就跟上一个错误不一样

它是呢

提示我们没有捕获对应的异常

我们将异常呢

做个捕获处理

在这里面的话呢

选择第三的

talent is check edge

那咱们来看一下异常这块呢

咱们该如何处理

log

首先将这个异常日志呢

打印出来

1.getMessage

那同时呢

咱们要将异常做个包装返回

对不对

api

respond result

在这里面呢

啊

叫用allet的方法

getLcode

下面的话呢

是它compound的一个safety

那咱们呢

将这个异常也打印出来

1.getMessage

如果咱们自己要去制定异常的话呢

也可以加一些其他信息

就是便于呢

你的一个排查和使用

然后在这里呢

同样也将这个异常信息呢

包装返回出去

alert

就直接呢

传递错误码就可以了

好

最后呢

咱们再catch一下

在这里只是catch了

咱们

所包装的异常对不对

一个呢

是业务异常

一个是组件异常

那么呢

可能还会出现一些位置异常

比如说数据库连接中断啊

等等对不对

所以呢

咱们在最外层呢

也加一个

最大范围的异常

那lockl.1.

getMessage

result API

在这里面呢

.sysl

就给它一个提示啊

说出现了系统异常

那咱们呢

再将这个success呢

修改下

放在这里面

最后呢

就是返回理造的

结果呢

返回给客户端

这里呢

加上注释

调用

用户的注册接口方法

这样呢

咱们就完成了

用户注册的

controller 层接口的实现

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段是关于一个名为 `bulls-stock-user` 的 Spring Boot 项目中，实现用户注册功能的开发过程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在控制器（Controller）层创建用户注册接口，并在服务层（Service）中实现具体的业务逻辑，包括用户存在性校验、公司信息校验和生成用户信息。整个过程强调了异常处理（`try-catch`）和统一的响应结果封装（`ApiRespResult`），并引入了 `@AutoWired` 注解进行依赖注入。视频内容聚焦于后端开发，特别是 Spring MVC 和 Spring Boot 的实践。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:03:00**: 展示项目结构，定位到 `StockUserController`，并讲解其 `userLogin` 方法的实现，包括调用 `stockUserService.login` 服务和异常处理。
*   **00:03:00 - 00:05:00**: 创建新的控制器类 `StockUserOpenController`，并为其添加 `@RestController` 和 `@RequestMapping("/open")` 注解，为后续的开放接口做准备。
*   **00:05:00 - 00:07:00**: 在 `StockUserOpenController` 中定义 `register` 方法，用于处理用户注册请求，并引入 `@AutoWired` 注解来注入 `IStockUserService` 服务。
*   **00:07:00 - 00:10:00**: 跳转到服务层 `StockUserServiceImpl`，演示 `userRegister` 方法的实现。该方法首先进行用户是否存在性校验，然后校验公司信息，最后生成用户信息并设置密码。
*   **00:10:00 - 00:13:00**: 返回控制器层，为 `register` 方法添加 `try-catch` 块，用于捕获服务层抛出的 `BusinessException` 和 `ComponentException`，并统一返回 `ApiRespResult` 格式的结果。
*   **00:13:00 - 00:15:00**: 完善 `try-catch` 块，将 `ApiRespResult` 的错误码和消息封装到响应中，并最终返回成功结果。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: `3.9 添加自动化校验`。
    *   **核心观点**: “作为一个健壮的后台服务，需要完善的校验机制，但接口繁多，通过自动化校验组件能让我们快速实现。”
    *   **技术选型**: “添加依赖，采用较新的稳定版本 6.0.16.Final。”（指 `hibernate-validator` 或类似校验框架）。

*   **关键代码片段**:

    **控制器层 (`StockUserOpenController.java`)**
    ```java
    @RestController
    @RequestMapping("/open")
    public class StockUserOpenController {
        @AutoWired
        private IStockUserService stockUserService;

        @PostMapping("/register")
        public ApiRespResult register(@Valid TradeUserVo tradeUserVo) {
            ApiRespResult result = null;
            try {
                result = stockUserService.userRegister(tradeUserVo);
            } catch (BusinessException e) {
                log.error(e.getMessage(), e);
                result = ApiRespResult.error(e.getErrorCodeEnum());
            } catch (ComponentException e) {
                log.error(e.getMessage(), e);
                result = ApiRespResult.error(e.getErrorCodeEnum());
            } catch (Exception e) {
                log.error(e.getMessage(), e);
                result = ApiRespResult.sysError(e.getMessage());
            }
            return result;
        }
    }
    ```

    **服务层 (`StockUserServiceImpl.java`)**
    ```java
    @Override
    public TraderUser userRegister(TradeUserVo tradeUserVo) throws BusinessException, ComponentException {
        // 1. 判断用户是否已经注册
        Integer checkResult = stockUserDao.checkRegister(tradeUserVo.getUserNo(), tradeUserVo.getTradePwd());
        if (null != checkResult && checkResult > 0) {
            throw new BusinessException(ApplicationErrorEnum.USER_EXISTS);
        }

        // 2. 对公司信息校验（传递的公司是合法的）
        CompanyVo companyVo = stockUserDao.getCompanyVoById(tradeUserVo.getCompanyId());
        if (null == companyVo) {
            throw new BusinessException(ApplicationErrorEnum.USER_COMPANY_NOT_FOUND);
        }

        // 3. 构造生成用户信息
        BeanUtils.copyProperties(tradeUserVo, newTraderUser);
        newTraderUser.setTradePwd(EncryptUtil.encryptSigned(tradeUserVo.getTradePwd()));
        // ... 其他业务逻辑
    }
    ```

    **响应结果封装类 (`ApiRespResult.java`)**
    ```java
    public class ApiRespResult {
        // ... 其他方法
        public static <T> ApiRespResult success(T data) {
            return new ApiRespResult(data);
        }
        public static ApiRespResult error(String code, String msg) {
            return new ApiRespResult(code, msg);
        }
        public static ApiRespResult sysError(String msg) {
            return new ApiRespResult("SYS_ERROR", msg);
        }
        // ... 其他方法
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：创建开放接口控制器**
    *   讲师在 `StockUserOpenController` 类中，通过 `@RequestMapping("/open")` 注解定义了开放接口的基路径。
    *   通过 `@PostMapping("/register")` 注解定义了具体的注册接口，并使用 `@Valid` 注解对请求参数 `TradeUserVo` 进行校验。

*   **场景二：依赖注入与异常处理**
    *   讲师在控制器中使用 `@AutoWired` 注解将 `IStockUserService` 注入，以便调用其方法。
    *   在 `register` 方法中，通过 `try-catch` 块捕获服务层抛出的 `BusinessException`、`ComponentException` 和 `Exception`，并统一使用 `ApiRespResult` 返回错误信息。

*   **场景三：服务层业务逻辑实现**
    *   讲师跳转到 `StockUserServiceImpl`，演示了 `userRegister` 方法的实现。
    *   方法首先调用 `stockUserDao.checkRegister` 方法检查用户是否已存在，如果存在则抛出 `BusinessException`。
    *   接着调用 `stockUserDao.getCompanyVoById` 方法校验公司信息，如果公司不存在则抛出 `BusinessException`。
    *   最后，使用 `BeanUtils.copyProperties` 方法将请求参数复制到实体对象，并调用 `EncryptUtil.encryptSigned` 方法对密码进行加密。

*   **场景四：统一响应格式**
    *   讲师强调了 `ApiRespResult` 的重要性，它用于统一返回成功或失败的响应格式。
    *   在 `try` 块中，调用 `stockUserService.userRegister` 方法后，直接返回其结果。
    *   在 `catch` 块中，根据异常类型，调用 `ApiRespResult.error` 或 `ApiRespResult.sysError` 方法，将错误码和消息封装到响应中，确保前端能统一处理。
