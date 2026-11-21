# 27-OAUTH2用户服务-总结 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们就对第三章内容做一个回顾和总结

首先咱们来明确一下第三章的主要学习目标

这一章的学习目标咱们是要去完善用户服务工程

实现了OS2的集成配置

并且要增加用户的登录接口

对OS2的建立权功能做一个测试和验证

这个是我们本章所要学习和掌握的目标

那么咱们回顾一下本章所讲的具体内容有哪些

首先咱们对工程结构做了一个讲解

先要预先读咱们用户服务

它整体的一个实现实录是怎样的

在这里面的话有它的一个配置实现

也有controller层接口的提供

然后数据层的实现

业务层的实现

最后就是其中的还有我们的配置

接着的话咱们是讲解了统一异常的处理

因为在这一块

我们需要先把周边的这些组件

必须要完善好

我们才能更好地去实现它的核心业务功能

那么统一异常处理

这一块我们是如何封装的

在这里面咱们是通过美举的形式

定义了统一的筹码

那么在这里面的话

我们会提供了两个两大类的异常

第一类就是compendant exception

称作为组成异常

第二类就是business exception

称作为业务异常

那么在这里面的话

筹码的美举我们是怎么去定义的

它有哪些属性

这些大家要了解清楚

那么再往下面

就是对统一借口数据返回的一个包装和定义

咱们是使用API

responder的照的

对统一返回整个的借口数据

这样的话

如果是其他的第三方平台

或者中端和前端跟我们做对接的时候

整个格式来讲就会更加清晰不规范

也能够便于我们的统一维护

最后咱们是实现了核心类

这个核心

业务逻辑

我们怎么去做的实现

在这里面的话

其实也很简单

主要的就实现了用户的登录接口

在登录接口

会涉及到数据层的DLO的操作查询

那么在这一块Map的配置

大家要对接包的路径

千万不要搞错了

然后的话

业务类这一块咱们是先获取用户对象

然后对密码做了一个判断

这样就完成了用户登录交易逻辑的一个处理

最后会将用户机器返回给交易房

那么通过可修了层接口进行交互

再往下面的就是OS2的一个配置

这个认证配置里面的话

咱们最主要要掌握资源服务的一个安全配置

比如说哪些接口

咱们要暴露访问

哪些接口

不需要暴露访问

在这里面都是可以支持的

还有制定一些登录验并

登录错误

登录成功等等的跳转

在这里面都可以根据自己的需要去制定

指定相应的路径

然后再往下面就是rest template的一个配置

因为咱们会涉及到远程的一些调用

比如说要去访问认证服务的接口

做一个token的权限交易

这里就是它的整体的认证服务的具体配置

那在我们实现完这些配置之后

要注意加上它这里的注解

Enable resource server的注解

以及Enable global domestic security的方法系列安全控制的注解

以及Enable global domestic security的方法系列安全控制的注解

然后咱们要把工程配置也给它做一个实现

在这里面的话

有数学员的配置

基本的服务信息配置

然后还有string security的OS2的认证配置

在这里面的话

之前讲认证服务的时候

也讲解过对不对

整体都是基本上类似的

那么最后就是mybattist的一个配置

一定要注意

这个class pass这个路径要少了正确

如果说扫描配置错误的时候呢

刚才做测试的时候

是启动验证的时候

也给大家做了一个演示

对不对

会出现了找不到数据层接口的一个错误提示

这样的话

就不能正常去操作数据层的接口

最后咱们再来总结一下

在这里面咱们最主要的目的是要完成应用服务的配置

以及它的改进

最主要还要掌握string security的OS2集成

核心类的处理实现

在整个项目当中

会存在一些公用的地方

咱们要做统一的处理

比如说统一异常

对不对

统一接口返回数据这些

通过统一的封装

雇用起来会更加方便

而且呢

值番清晰

便于将来呢

咱们的维护与扩展

好

这些呢

就是对第三章内容的回顾与总结

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，进行的结构化中文技术课程分析。

---

### 1) 视频摘要

本视频课程为一个技术实战项目的一部分，主要讲解如何在微服务架构中实现用户认证服务，并集成 Spring Security OAuth2。课程内容围绕“第4章 网关服务与Druid监控数据源”展开，但核心是“第3章 用户服务”的实现细节。讲师通过展示项目代码结构、配置文件和核心类的实现，系统性地讲解了如何统一处理异常、统一接口数据返回、实现核心业务逻辑、配置 Spring Security 资源服务器，并最终完成服务的启动与验证。课程强调了代码的可维护性和扩展性，通过引入 MyBatis、Druid 和 Spring Security 等技术，将一个基础的用户服务升级为一个具备完整认证和监控能力的生产级服务。

---

### 2) 按时间顺序的章节（带时间点）

由于无法从截图中获取精确的时间戳，以下章节划分是基于画面内容的逻辑顺序推断的：

*   **00:00 - 00:15**: **课程总览与目标介绍**
    *   展示了课程大纲，明确指出本章目标是“完成网关服务认证转发配置与功能验证”和“实现监控数据源Druid的集成配置”。
    *   介绍了项目整体结构，包括 `stock-user` 服务和 `stock-common-utils` 工具库。

*   **00:15 - 00:30**: **统一异常处理说明 (3.2节)**
    *   讲解了如何通过 `ApplicationErrorCodeEnum` 枚举类来统一定义和管理错误码。
    *   展示了 `ApplicationErrorCodeEnum` 的代码实现，其中定义了如 `SUCCESS`、`FAILURE`、`USER_NOT_FOUND` 等常量。

*   **00:30 - 00:45**: **统一接口数据返回说明 (3.3节)**
    *   介绍了 `ApiRespResult<T>` 这个泛型类，用于统一所有 API 的返回格式。
    *   展示了该类的代码结构，其中包含 `code` 字段用于返回状态码。

*   **00:45 - 01:00**: **核心类实现说明 (3.4节)**
    *   展示了服务层 `StockUserServiceImpl` 的代码，其中包含了用户登录方法 `userLogin`。
    *   讲解了如何通过 `@Autowired` 注入 DAO 层，并抛出 `ComponentException` 异常。

*   **01:00 - 01:15**: **认证配置类 (3.4节)**
    *   展示了 `ResourceSecurityConfigurer` 配置类的代码。
    *   重点讲解了 `@EnableResourceServer` 注解和 `@EnableGlobalMethodSecurity` 注解的作用。

*   **01:15 - 01:30**: **RestTemplate 配置与异常处理**
    *   展示了 `lbRestTemplate` 的配置代码。
    *   讲解了如何为 `RestTemplate` 设置 `DefaultResponseErrorHandler` 来处理 HTTP 错误响应。

*   **01:30 - 01:45**: **工程配置与启动**
    *   展示了 `bootstrap.yml` 配置文件，其中包含了 `server` 和 `security` 配置。
    *   详细讲解了 `security.oauth2.resource` 和 `security.oauth2.client` 的配置项，如 `token-info-uri`、`client-id`、`client-secret` 等。

*   **01:45 - 02:00**: **总结与展望**
    *   回顾了本章的核心内容，强调了统一异常处理、统一接口返回、核心业务实现和 Spring Security 集成的重要性。
    *   提到项目中存在公用模块，应统一处理，以提高代码的复用性和可维护性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：清晰列出了“第3章 用户服务”和“第4章 网关服务与Druid监控数据源”的章节结构。
    *   **关键概念**:
        *   **统一异常处理**: 使用 `ApplicationErrorCodeEnum` 枚举类定义错误码。
        *   **统一接口返回**: 使用 `ApiRespResult<T>` 类规范返回格式。
        *   **核心实现**: `StockUserServiceImpl` 服务类和 `ResourceSecurityConfigurer` 配置类。
        *   **技术栈**: Spring Cloud、Spring Security OAuth2、MyBatis、Druid。

*   **代码关键内容**:

    *   **统一异常枚举类 `ApplicationErrorCodeEnum`**:
        ```java
        public enum ApplicationErrorCodeEnum implements IErrorCodeEnum {
            SUCCESS("200", "成功"),
            FAILURE("300", "系统异常"),
            COMPONENT_LOAD_PROPERTIES_OBJ_HAD_EXIST("000001", "配置文件加载类已经存在"),
            SYS_ERROR_ENCRYPT_SINGED(IErrorCodeEnum.MODULE_SYSTEM, "000002", "签名加密错误"),
            USER_NOT_FOUND(IErrorCodeEnum.MODULE_USER, "000003", "用户不存在！"),
            USER_PWD_ERROR(IErrorCodeEnum.MODULE_USER, "000004", "用户密码错误！");
        }
        ```

    *   **统一返回结果类 `ApiRespResult<T>`**:
        ```java
        public class ApiRespResult<T> implements Serializable {
            private static final long serialVersionUID = -1L;
            private String code = ApplicationErrorCodeEnum.SUCCESS.getcode();
            // ... 其他字段和方法
        }
        ```

    *   **认证配置类 `ResourceSecurityConfigurer`**:
        ```java
        @Configuration
        @EnableResourceServer
        @EnableGlobalMethodSecurity(prePostEnabled = true)
        public class ResourceSecurityConfigurer implements ResourceServerConfigurer {
            // ... 配置方法
        }
        ```

    *   **RestTemplate 配置类**:
        ```java
        @Bean
        @Primary
        @LoadBalanced
        public RestTemplate lbRestTemplate() {
            RestTemplate restTemplate = new RestTemplate();
            restTemplate.setErrorHandler(new DefaultResponseErrorHandler() {
                @Override
                public void handleError(ClientHttpResponse response) throws IOException {
                    if (response.getRawStatusCode() != HttpStatus.BAD_REQUEST.value()) {
                        super.handleError(response);
                    }
                }
            });
            return restTemplate;
        }
        ```

    *   **配置文件 `bootstrap.yml`**:
        ```yaml
        server:
          # ... 服务器配置

        security:
          oauth2:
            resource:
              loadBalanced: true
              token-info-uri: http://trade-auth/oauth/check_token
            client:
              client-id: app
              client-secret: app
              scope: server
              access-token-uri: http://trade-auth/oauth/token
              user-authorization-uri: http://trade-auth/oauth/authorize
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构展示**
    *   **描述**: 讲师首先展示了项目在 IDE 中的目录结构，包括 `src/main/java` 下的 `controller`、`dao`、`service` 等包，以及 `resources` 下的配置文件。通过对比，指出当前项目与初始版本的不同，强调了 MyBatis、Druid 和 Spring Security 的集成。

*   **场景二：统一异常处理演示**
    *   **描述**: 讲师切换到 `stock-common-utils` 项目，展示了 `ApplicationErrorCodeEnum` 的代码。通过鼠标悬停和代码高亮，详细解释了每个错误码的含义和用途，强调了统一错误码管理的重要性。

*   **场景三：统一接口返回演示**
    *   **描述**: 讲师展示了 `ApiRespResult<T>` 类的代码。通过注释和代码结构，说明了该类如何封装返回数据，包括状态码 `code` 和泛型 `T`，从而实现所有接口的统一返回格式。

*   **场景四：核心业务实现演示**
    *   **描述**: 讲师展示了 `StockUserServiceImpl` 的代码。通过 `@Service` 和 `@Log4j2` 注解，以及 `userLogin` 方法的实现，演示了如何在服务层处理用户登录逻辑，并抛出自定义异常。

*   **场景五：认证配置演示**
    *   **描述**: 讲师展示了 `ResourceSecurityConfigurer` 配置类。通过 `@EnableResourceServer` 和 `@EnableGlobalMethodSecurity` 注解，演示了如何将服务配置为资源服务器，并启用方法级别的安全控制。

*   **场景六：RestTemplate 配置演示**
    *   **描述**: 讲师展示了 `lbRestTemplate` 的配置代码。通过 `@LoadBalanced` 注解和 `DefaultResponseErrorHandler` 的实现，演示了如何配置一个支持负载均衡和自定义错误处理的 `RestTemplate`，用于调用其他微服务。

*   **场景七：配置文件配置演示**
    *   **描述
