# 18-用户注册-自动化校验 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接着的话咱们开始实现了自动化校验的功能

作为一个现状的后台服务

必须要有一个完善的校验机制

对不对

但是一个服务往往会提供很多的接口

如果一两个接口这个还好

咱们去手动做校验实现都没有问题

但是接口如果比较多

每个接口的参数都不一样

这个时候有没有比较快捷的方法

帮助咱们去快速实现接口的校验

这个就是本章节所要学习的自动化校验组件

咱们来看一下具体是该如何去实现

首先咱们先把它的依赖添加进来

把它拷贝到Store.U者POM依赖文件当中

咱们放到最下面

依赖添加完成之后咱们来看一下

从代码层当中该怎么去实现

在Control了当中

我们要在需要校验的参数当中

增加校验的注解Valid

也是上个章节咱们实现的

用户注册的接入层接口

在这里面添加了一个Valid注解

先把这个注解加进去

好

这个只是第一步

也就是说告诉咱们哪个参数是需要做自动化校验

好

这个参数下面的话咱们可以看到它是一个对象

对不对

它下面有很多属性

那么这些属性该怎么去校验

每个属性的校验规则是不一样的

对不对

比如说电话号码有电话号码的校验规则

那么邮箱有邮箱的校验规则

这个时候该怎么去实现了

咱们接着往下看

在参数当中去增加具体的校验规则

咱们在这里来举例做个实现

在咱们的shared user view当中

我们name给它一个校验

那这个具体规则呢

我们可以限制下它的长度

该怎么去实现呢

在这里面要设置它的一个参数

你有长度的话呢

可以设定它最小的一个长度

以及最大的一个长度

这个呢就是它的提示信息

如果是超长的

你要给它一个明确的错误提示

那么在这里咱们给它制定一下姓名长度

必须为1到32

这个size呢

注解呢

咱们要改成大小

这个时候可以看到就没包错了

它在哪个包下面呢

我们鼠标conclude

可以看到它在那个validation API下面

对不对

habitator

validator所依赖的包

再往下面呢

咱们就来对它的密码

也做一个长度的限制

这个密码呢

同样的方法

比如说咱们也限定

它的一个

最大的长度不能超过32

message

密码长度

必须为1到32

这些呢

是基本的格式教验

那如果咱们想做一些比较复杂的教验

比如说手机号

这个时候呢

该怎么去做呢

能不能支持一些高级的匹配规则呢

这个也是可以的

那咱们来看一下

比如说咱们要教验手机号

因为手机号来讲呢

它的规则

会相对比较复杂一点

它就不是单纯的一个长度

或者这样的一个判断就能够去实现了

在这里呢

它是要根据了对应的一个规则

然后呢

进行一个匹配教验

那么我们可以看到

它是可以支持什么正轴的匹配规则

通过这种方式呢

咱们就可以更加灵活的去实现了不同属性的必要条件的教验

好

那除了这些的话呢

还能不能实现呢

其他的一些教验功能呢

这个都是可以的

咱们来看一下

它还提供的哪些教验呢

咱们往下面去看

在这里呢

它还提供了比较多的教验方式

比如说

not null

限制呢

必须不为 null

然后呢

它的一个decibel max

限制呢

它不大于指定的一个数字

这个degeast是限制为呢

必须为一个小数

可以看到

它的这种注解功能呢

也是比较好

可以呢

实现咱们不同场景下面的不同教验的需要

好

在这里呢

咱们就实现了它的比较参数的教验

只是做了对应的力学

大家呢

还可以去根据自己的需要

再去扩充其他的属性教验

那咱们看一下

在这里定义完成之后

是不是就能够呢

去实现了整个自动化教验呢

这个还没有完成

那咱们来看一下

还要做哪些配置呢

接着的话呢

我们还要去制定教验的错误信息

那么我们虽然能够做到它的一个教验

对不对

你是不是要将这个教验提示信息呢

通过统一的接口数据格式

然后返回给终端

所以呢

需要咱们去对自动化教验错误呢

去做一个封装

否则的话呢

它的接口提示信息呢

会比较繁杂

不符合咱们统一接口的规范和要求

那么咱们来看一下

如何去拦截

并且将这个信息组装成为统一接口的数据格式

咱们要增加一个Handle

这个Handle呢

就是针对于自动化教验异常的拦截器的实现

在咱们的用户服工程下面

很非可目录下

创建一个Handle

这个Handle呢

就是Pyramid Validate Exception Handle

专门用于自动化教验异常的拦截处理

咱们看一下它具体该如何去实现了

首先要加上它的注解

Controller

Otherwise

这个意思呢

就说明了它是一个什么

Controller层的拦截器

好

这的话呢

咱们再加上它的

Log的注解

下面呢

我们就要去做异常具体的拦截和包装处理

因为咱们是统一的返回对象

所以呢

它的返回对象呢

就是API Result

然后呢

来一个方法

叫Handle Reception

去拦截对应的异常

那么呢

自动化教验异常

它会抛出一个Band Exception

咱们呢

做一个拦截处理

这个参数呢

是Band Exception

别搞错了啊

它在哪里

在Validation这个

加保里面

首先呢

咱们给它打出一个提示

这支

说明了你已经进入到咱们拦截器当中

便于咱们的排查

下面呢

我们看一下

整个的实现步骤是怎样的

首先是要获取

所有的教验错误提示

因为呢

我们会定义很多种教验规范

对不对

刚才呢

也给大家做了演示

咱们可以看到

Chad UseValue

它的教验是怎么处理的

它会将这些东西全部教验出来

然后呢

做统一的返回

也就是说

它不会因为第一个教验错误了

下面就不进行教验了

它会将这里面定义的所有的教验错误呢

都做一遍检查

然后呢

将这些信息

全部返回抛出来

咱们再写下第二个步骤

第二个步骤呢

我们要

便利

它的属性教验结果

因为它会是多个对不对

最后呢

咱们就要去

封装返回

这就是呢

三个复利步骤

Stream Buffer

通过Stream Buffer呢

帮助我们做一个拼接

那么我们来看一下

怎么去获取它所有的异常提示呢

Build

Field

Ellis

通过

这个一个Savage里面

会有一个GetBund

Result

绑定了

回错误结果

获取了所有的属性教验错误

好

拿到这个属性教验错误呢

咱们就来做一个便利处理

Build

Ellis

然后呢

我们要做一个拼接

通过Stream Buffer

做异常的拼接处理

Field

Ellis

获取它的属性

然后呢

去拼接我们的错误提示

通过冒号

然后分割

Field

获取了默认的错误提示消息

这个默认的错误提示消息呢

就在Chad User Viewer里面

逆了Message

拼接完成之后呢

我们就将这个

异常错误呢

包装返回家

Add WebResult

VPI Respond Result

在这里面呢

去教演它的错误

Buffer

最后呢

我们就将包装结果呢

返回出去

好

这一块呢就是对

自动化交易异常的拦截包装处理

在这里呢

我们可以看到它整体的一个处理流程

对不对

下面呢

我们还要去实现一个方法

这个方法又是干什么用呢

这个是拦截呢

约束性的异常处理

比如说Node Blank

非空的必要性约束等等

那在这里呢

它是拦截什么

教验的异常信息

那咱们来看一下

教验异常和约束性异常

有什么区别呢

像Node NotNode

这个呢

就是约束性异常

因为呢

在这个对应的注解下面呢

它没有呢

再去定义具体的教验规则

而这种呢

Min和Max呢

下面还可以定义更具体的教验规则

比如说你的长度

最小呢

是一个长度

或是五个长度

最大呢

是十个长度

或是二十个长度

可以根据自己的需要去定义

这种呢

就是教验性异常

而这种呢

直接去限制了一个结果

这个就是约束性的异常

不能够呢

去定义呢

自己所需要的规则

所以呢

这种就是约束性异常

好

那咱们呢

再将约束性异常呢

也做一个拦截处理

在这一块呢

跟整个逻辑比较类似

咱们呢

就copy过来

将它呢

同样放在这个handle下面

那咱们来看一下

它整体是如何处理的呢

既然呢

它是一个什么

它是一个约束性异常

那么except handle呢

要给它做一个注解

去配置你所要拦截的异常类型

它是在java x validation的包下面

好

配置完你所需要拦截的异常之后呢

你还要再增加

一个拦截约束

这个约束呢

我们可以看一下是400

也就是说

出现了400的响应状态码

并且呢

你的返回抛出异常是concentrate的

validation exception呢

它就会进入下面的拦截方法处理之内

它才会进入下面的拦截处理方法

那它的整个处理流程呢

跟我们上面也是一样的

首先呢

要去获取所有的教研错误提示

对不对

第二呢

就是要封装教研异常的红信息

好

不同的是它的拦截配置约束

在上面呢

是一个教研性异常

同样的

它也要配置对应的拦截约束

这上面呢

它配置的是fandexception

也就是说绑定的异常

根据呢

我们自己定义的教研规则

去触发了拦截处理

这个响应状态码呢

同样也是在这个拦截处理的

这个拦截处理的

这个拦截处理的

这个拦截处理的

同样也是出现

失败的错误请求

rsponsebody呢

是将这个结果呢

做一个返回

封装成为接手对象

这个呢

你加和不加呢

关系都不大

我们呢

也把它加上去

将这个注释呢

也加入进来

好

在这呢

就是对自动化教研异常的

拦截处理

咱们可以看到

主要呢

是两块处理步骤

第一个呢

是拦截所有的教研性异常

对不对

第二呢

是阅述性异常

下面呢

还有很多的教研规则

咱们有时间呢

可以再去研究和学习一下

那这个FAQ要补充说明一下

如果是使用阅述性异常

比如说not blank

非空

对不对

它不生效的情况

那么你要检查呢

我们这个使用类上面

有没有增加它对应的

validate注解

也就是说

要把这个注解呢

加入进来

这个呢

就是一个补充说明

那这一讲呢

对自动化教研实现呢

我们就讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程是关于在 Spring Boot 项目中实现用户注册功能的“自动化校验”部分。讲师通过 IntelliJ IDEA 开发环境，演示了如何利用 Hibernate Validator 框架，结合 `@Valid` 注解和 `@Size`、`@Pattern` 等约束注解，对前端传入的用户注册参数（如用户名、密码、手机号）进行校验。同时，讲师还演示了如何自定义一个异常处理器 `ParamValidExceptionHandler`，用于捕获校验失败时抛出的 `BindException`，并将其转换为统一的 JSON 格式错误响应，以提升用户体验和系统健壮性。最后，讲师补充了关于 `@NotBlank` 注解的使用细节，并预告了后续将启动服务和进行功能验证。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程引言，介绍本节目标是“添加自动化校验”。
*   **00:05 - 00:15**: 在 `pom.xml` 中添加 Hibernate Validator 依赖。
*   **00:15 - 00:30**: 在 `StockUserOpenController` 的 `register` 方法中添加 `@Valid` 注解。
*   **00:30 - 00:45**: 在 `TradeUserVo` 实体类中为各个字段添加校验注解（`@Size`、`@Pattern`）。
*   **00:45 - 01:00**: 创建并编写 `ParamValidExceptionHandler` 类，用于处理校验异常。
*   **01:00 - 01:15**: 在 `ParamValidExceptionHandler` 中编写 `handlerException` 方法，解析 `BindException` 并封装错误信息。
*   **01:15 - 01:30**: 为 `handlerException` 方法添加 `@ExceptionHandler` 和 `@ResponseBody` 注解。
*   **01:30 - 01:45**: 为 `handlerException` 方法添加 `@ResponseStatus(HttpStatus.BAD_REQUEST)` 注解。
*   **01:45 - 02:00**: 为 `handlerConstraintException` 方法添加 `@ExceptionHandler(ConstraintViolationException.class)` 注解。
*   **02:00 - 02:15**: 补充说明 `@NotBlank` 注解的使用，并演示如何在 Controller 中使用 `@Validated` 注解。
*   **02:15 - 02:30**: 预告下一节内容“启动服务”和“功能验证”。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **章节标题**: “3.9 添加自动化校验”。
*   **核心思想**: “通过自动化校验组件，让我们快速实现”。
*   **依赖信息**: `groupId: org.hibernate`, `artifactId: hibernate-validator`, `version: 6.0.16.Final`。
*   **FAQ补充**: “如果使用约束性异常`@NotBlank`不生效的情况，要注意在使用的类上加上`@Validated`”。

#### 代码关键内容

*   **Maven 依赖 (pom.xml)**:
    ```xml
    <dependency>
        <groupId>org.hibernate</groupId>
        <artifactId>hibernate-validator</artifactId>
        <version>6.0.16.Final</version>
    </dependency>
    ```

*   **Controller 层代码 (`StockUserOpenController.java`)**:
    ```java
    @PostMapping("/register")
    public ApiRespResult register(@Valid TradeUser tradeUser) {
        // ...
    }
    ```

*   **实体类校验注解 (`TradeUserVo.java`)**:
    ```java
    @Size(min = 1, max = 32, message = "姓名长度必须为1到32")
    private String name;

    @Size(min = 1, max = 32, message = "密码长度必须为1到32")
    private String userPwd;

    @Pattern(regexp="^(13[0-9]|15[4,\\d]|18[0,5-9])\\d{8}$", message="手机号格式错误")
    private String phone;
    ```

*   **异常处理器代码 (`ParamValidExceptionHandler.java`)**:
    ```java
    @ExceptionHandler(BindException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    @ResponseBody
    public ApiRespResult handlerException(BindException ex) {
        StringBuffer stringBuffer = new StringBuffer();
        List<FieldError> errors = ex.getFieldErrors();
        for (FieldError fieldError : errors) {
            stringBuffer.append(fieldError.getField()).append(":").append(fieldError.getDefaultMessage());
        }
        ApiRespResult errorWebResult = ApiRespResult.validError(stringBuffer.toString());
        return errorWebResult;
    }

    @ExceptionHandler(ConstraintViolationException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    @ResponseBody
    public ApiRespResult handlerConstraintException(ConstraintViolationException ex) {
        // ...
    }
    ```

---

### 4) 关键场景与演示描述

1.  **场景一：添加依赖** (00:05-00:15)
    *   讲师在 `pom.xml` 文件中定位到 `<dependencies>` 区域。
    *   他手动添加了 Hibernate Validator 的 Maven 依赖，并指定了版本号 `6.0.16.Final`。
    *   他强调了这个依赖是实现自动化校验的基础。

2.  **场景二：Controller 层注解** (00:15-00:30)
    *   讲师切换到 `StockUserOpenController.java` 文件。
    *   他在 `register` 方法的参数 `TradeUser tradeUser` 前面添加了 `@Valid` 注解。
    *   他解释了 `@Valid` 注解的作用是触发对 `TradeUser` 对象中所有校验注解的检查。

3.  **场景三：实体类校验** (00:30-00:45)
    *   讲师切换到 `TradeUserVo.java` 文件。
    *   他在 `name` 字段上添加了 `@Size(min=1, max=32, message="姓名长度必须为1到32")` 注解。
    *   他在 `userPwd` 字段上添加了相同的 `@Size` 注解。
    *   他在 `phone` 字段上添加了 `@Pattern` 注解，并配置了正则表达式 `^(13[0-9]|15[4,\\d]|18[0,5-9])\\d{8}$` 来校验手机号格式。

4.  **场景四：自定义异常处理器** (00:45-01:00)
    *   讲师在项目中创建了一个新的 Java 类 `ParamValidExceptionHandler`。
    *   他为这个类添加了 `@ControllerAdvice` 注解，使其成为一个全局异常处理器。
    *   他声明了 `handlerException` 方法，用于处理 `BindException`。

5.  **场景五：封装错误信息** (01:00-01:15)
    *   讲师在 `handlerException` 方法中，使用 `ex.getFieldErrors()` 获取所有校验失败的字段信息。
    *   他使用 `StringBuffer` 拼接错误信息，格式为 `字段名: 错误信息`。
    *   他将拼接好的字符串传递给 `ApiRespResult.validError()` 方法，生成一个标准的错误响应对象。

6.  **场景六：处理约束性异常** (01:15-01:30)
    *   讲师在 `ParamValidExceptionHandler` 类中添加了 `handlerConstraintException` 方法。
    *   他为该方法添加了 `@ExceptionHandler(ConstraintViolationException.class)` 注解，使其能够捕获 `@NotBlank` 等约束性注解抛出的异常。
    *   他指出，`ConstraintViolationException` 是 `@NotBlank` 等注解抛出的异常类型。

7.  **场景七：FAQ 补充** (02:00-02:15)
    *   讲师在 PPT 上展示了关于 `@NotBlank` 注解的 FAQ。
    *   他解释了如果 `@NotBlank` 注解不生效，需要在使用它的 Controller 类上添加 `@Validated` 注解。
    *   他演示了如何在 `StockUserController` 类上添加 `@Validated` 注解。

8.  **场景八：启动服务预告** (02:15-02:30)
    *   讲师在 PPT 上展示了下一节的标题“3.10 启动服务”。
    *   他预告了接下来将启动项目中的服务，并进行功能验证。
    *   他强调了自动化校验的实现是后续功能验证的基础。
