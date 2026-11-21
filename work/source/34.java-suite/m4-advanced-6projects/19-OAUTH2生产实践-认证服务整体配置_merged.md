# 19-OAUTH2生产实践-认证服务整体配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来咱们接着呢

去实现认证服务的

它整体的集成配置

那上一讲呢

咱们是实现了

Authentication Server Config的

它的一些基本的配置

那在这里呢

咱们重点是要掌握呢

Token增强的一个处理

这一块呢

它怎么去配置的呢

咱们可以看一下

在这里呢

它是去通过Token Inertial

这个对象呢

然后去做了一个实现

在这里它怎么去实现的呢

我们可以看到

首先呢

它会去判断

是否呢

要经过那个Client的认证

对不对

如果说你的那个Client Type

就是认证类型的

是Client呢

在这里它就直接会

返回对应的Access Token

咱们可以看一下

就是客户端的认证模式

对不对

咱们之前应该还有印象

对吧

是种模式的时候

如果是客户端认证模式

会直接将Token返回出去

好

在这里呢

有个错误

咱们呢

先把它处理一下

加上大括号

接着的话呢

它是做什么处理呢

它是会通过

咱们将注释呢

写一下

通过呢

Map存储附加的信息

咱们可以看到

这个附加的信息呢

它的格式是一个Map

对不对

然后呢

它会附加些什么信息呢

会针对于User的信息

我们可以看到

会存储它的User的ID

Name Email等等

对不对

为什么叫做Token的增强呢

正是因为它有这样的一个扩展能力

所以呢

它可以将用户更多的信息呢

存储进来

就实现了Token的增强

如果说咱们不通过这种方式呢

它只能附带用户的基本信息

比如说用户的ID呀

它不能存储过多的信息

所以呢

咱们要明白

为什么会采用Token增强

以及呢

Token增强的它的一个作用

再往下面的话呢

在这里就是它的一个增加的附件信息

咱们来加上一个注释

需要

扩充增加的用户附带信息

再往下面呢

它是要将附加的信息呢

保存进去

将附加的信息

记录保存

然后呢

形成一个增强的Token

可以看到在这里面的话呢

它在XS Token当中呢

做了一个转换

对不对

然后呢

将这个附带信息放置在附带的

Admin information当中

好

这个呢

就是整个增强Token的一个处理流程

那么咱们再来看一下

接下来的配置

接着的话呢

咱们要去实现了Web的一个安全性配置

咱们呢

也创建对应的配置类

在这里面

New Java Class

OK

我们给它呢

加上对应的注解

Configuration

是作为一个配置类

然后呢

我们让它的优先级调高一点

怎么去调呢

通过那个Primary注解

下面呢

再给它的一个顺序

如果说大家在实现工程的时候呢

有些配置

它的顺序需要额外处理

大家就按照这种方式来做

比如说你其他的

那个有存在必要的依赖关系

要先加在哪个后加在哪个

那么呢

就直接进入对应的order就可以了

这里加完注解之后呢

不要忘了

Orderization 收货Configure呢

它还加上对应的注解

首先呢是Configuration

然后呢Enable

Oscillation 收货

这个注解的意思呢

是让它开启认证服务

如果说你这个不开启了

下面这些配置是无法生效的

好

这里面呢要继承一个类

Web Security

Configuration

Adapt

好

那这里呢

还要配置哪些东西呢

咱们呢

让它copy一下

这个呢是

用户服务介绍

这个呢是我们自定义实现的

对不对

然后呢是它的密码编码器

密码编码器

这个可以支持加密

处理

比如说咱们要考虑它的安全性

可以加入一些AES DS等等的

辗迷方式

这个Stalker password encode呢

咱们接下来再做实现

然后呢这个是Web服务的认证配置

咱们把它加入进来

这个Web服务认证配置

它主要作用是干嘛呢

在这里它会去指定你的登录页面

然后呢是你的登录的表单

这个呢是登录成功之后的地址

比如说你要

登录成功之后你要去请求哪个接口

比如通过这个接口

然后这边的话呢

登录成功之后要返回的地址信息

下面的话呢

就是它的一个认证请求

我们可以看到它是Permit All

是进行了一个放权

对不对

然后除此之外的其他请求呢

它是都需要进行一个认证

也就是它经过这个token的

还有accuter

以及呢

DLUID的前缀的请求呢

都会进行一个放行处理

这一块呢是它的一个Web服务的认证配置

再往下面我们可以看一下

还有它的一个静态资源的拦截配置

我们注意拷贝一下

这个意思是什么呢

它是不拦截静态资源

咱们知道一个服务当中呢

特别是一些存在交互的页面

对不对

会有些CSS的样式

在这里呢

一些图片了

或者是CSS啊

咱们就不需要进行拦截

然后再往下面呢

是它的CSS Manage Bin

这个是什么作用呢

这个是认证的管理器

认证管理器

就按照它默认的方式

做一个调用处理就可以

接着的话呢

是它的Config

这个Config呢

咱们可以看到

它的主要作用呢

是什么

会注入我们的用户服务接口

对不对

以及呢

我们的密码编码器

好

这个呢

就是Web Security Config的

它的一个主要配置

那接着的话呢

咱们就要把这个编码器呢

做个实现

New

Double Class

Store

Double Class

Store

是吧

编码器在这里呢

是要实现一个接口

这个接口呢

是它输入的

引扣的

那么同样呢

我们将对应的代码呢

扣一下

这个呢

是编码的处理器

这个呢

因为我们并不需要特殊编码

所以在这里呢

选择它默认方式

直接转换为自讯就可以了

然后咱们来看一下

它在这一块还有一个密码的校园判断

密码校园判断呢

咱们来看一下

它怎么处理的呢

在这里呢

它会传入它的一个

原始密码里面呢

你编录就是进行编码之后的一个密码支付串

在这里

咱们先把那个

logpc2加入进去

它会做一个判断

首先呢

去判断你的law password

在这里面呢

它是否围空

也对原始密码进行一个判断

判断完围空之后呢

如果是围空

它就没法进行下面的逻辑处理

它在这里呢

还会进行一个编码加密

这个加密呢

是

用我们自己的实现的加密方式

它其实呢

就是

先通过md5加密

然后呢

外层再通过b64进行编码

在这里

它就会进行一个判断

因为我们这个密码的话呢

都是密文进行一个传输处理

对不对

然后呢

编码判断

如果说是匹配的话呢

那么就返回q

如果是不匹配呢

就返回一个警告信息

好

这样呢

它就认证就无法通过

md5的加密距离实验逻辑呢

在这个工具上呢

工具当中

Inclined side

在这里面呢

是一只通用的md5的加密处理

好

返回

那么这个编码的配置呢

就已经实现完成

接着的话呢

咱们就要去实现了工程的一个配置

工程配置文件

我们要创建一下

是在resource下面

在这里呢

咱们就先将它copy过来

然后再做详细讲解

咱们来看一下

最上面的话呢

是服务的基本配置

相当多

搜寻口啊

服务的名称

在这里啊

就不做过的追溯

然后呢

是数据员的一些连接配置

在这里面是采用了得鲁伊的监控数据员

那这个数据员呢

他有一些连接词的配置信息

对不对

好

如果说咱们是要去开启了他的后台

就是监控的一个访问的

咱们需要将他的urlpattern要指定一下

要允许哪些能够访问

然后哪些的禁止访问

在这里呢

如果没有特殊要求

咱们就留空就可以了

然后这个呢

这是他登录的用户名和登录密码

下面就是Fluidmark的一个模板引擎配置

为什么会采用Fluidmark

因为咱们的那个登录页面

制定的登录页面

就通过Fluidmark的模板引擎去实现了

好这一块就是Fluidmark的通用配置

再往下面的话是他的一些排除类

像这种的话

一些MVC的这种错误的配置的话

咱们是不需要

所以可以做一个排除

然后这个是JPA的一个功能配置

这个JPA的话

并没有一个特殊的处理

最主要咱们是要

实现这样的一个配置

也就是说这个

命名我们的对象命名

我们找到对应的Nt

这个Chad User里面的对象命名

跟我们数据固表里面

是保持一致的

都是采用脱封命名方法

并没有采用下滑线

所以不需要进行转换

大家要明白清楚

如果说你在

这里面的话不做这个配置

他的映射的时候

就不能实现这种

自动化映射

好

下面就是内底子的配置

最重要的话

就下面的SplitSecurity

跟OS2的一个集成配置

我们来看一下他怎么去做的

在这里是作为一个资源服务

资源服务的话

他的一个token

获取的地址是什么

是就是我们本身的认证服务

对不对

也就是说这个认证服务

因为我们是加了一个用户的接口

所以他既能作为

资源服务又能作为什么认证服务

那么作为资源服务

他要去交易他的token

对不对

那么怎么去交易

就要去访问他的认证服务地址

好

这个就是Check Token

他的一个接口

下面就是client

要给你分配一个client信息

那么client信息的话

我们会预制好

在这里的话都是要保持一致

像这个app

然后这个meer

跟我们数据库里面的话

一定要匹配正确

否则的话是无法验证通过

也就没法去申请到对应的token

这个scope作用预计也要保持一致

如果这里是收罗

我们后台里面的

数据库的信息也要是设定为收罗

下面的话就是要放行的url

这块的话

比如说有些模块

咱们是需要放行处理

这里的话就可以把它加入进去

因为这些swork的话

咱们目前还没有用到

对不对

先可以不用去关注这一块

后面咱们还会对于这一块的

os2的一个功能

就是这个组件再做进一步的封装

便用我们其他的一个服务的

揭露和使用

在这里就主要的一些配置信息

其实作为认证服务来讲的话

咱们并不需要去配置这些

因为咱们既作为资源服务

又作为认证服务

对不对

所以咱们还配置一些信息

好

在这里就是os2

它的认证服务的一个整体的配置

下面也有具体的讲解和说明

那么的话咱们要明白

什么是security的一个认证配置

那么的话咱们要明白什么是security的一个认证配置

好

再往下面就是它的一个静态服务资源

因为我们是实现了自定义的登录页面

对不对

这里也是教大家如何去实现

自定义的这种页面的处理

那么为了方便起见

我已经将这些静态资源直接copy进来了

接着的话咱们就可以对整个服务

做一个启动和验证

在这里就已经实现完了认证服务的一个发现

以及它整体的配置

这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对这段技术课程进行的结构化中文输出：

---

### 1) 视频摘要

本视频课程是关于一个名为 `bulls-stock-trade-oauth` 的 Spring Boot 项目，重点讲解如何实现一个基于 OAuth2 协议的认证授权服务。课程内容涵盖了从项目结构、配置文件、自定义密码编码器，到 Spring Security 安全配置、令牌增强器（Token Enhancer）的开发，以及如何集成 Redis 作为令牌存储。讲师通过 IntelliJ IDEA 编辑器进行代码演示，并结合 `application.yml` 配置文件和 Markdown 文档进行讲解，旨在帮助学习者掌握构建一个可扩展、高可用的认证服务的完整流程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，展示项目结构，介绍 `bulls-stock-trade-oauth` 项目。
*   **00:05 - 00:15**: 讲解 `AuthorizationServerConfig` 配置类，演示如何自定义 `TokenEnhancer` 来增强访问令牌，添加用户信息。
*   **00:15 - 00:25**: 介绍 `WebSecurityConfigurer` 类，展示如何配置 Spring Security 的安全策略，包括登录页面、权限控制和 CSRF 保护。
*   **00:25 - 00:35**: 创建并实现 `StockPasswordEncoder` 类，演示如何自定义密码编码器，使用 MD5 和 Base64 进行密码加密。
*   **00:35 - 00:45**: 讲解 `application.yml` 配置文件，配置数据库（Druid）、Redis、以及 Spring Security 的 OAuth2 相关参数。
*   **00:45 - 00:55**: 展示如何配置静态资源（CSS、模板文件），并说明如何通过 HTML 页面的“Reset All”功能重置配置。
*   **00:55 - 01:05**: 总结本章内容，强调项目中各组件的协作关系，为后续的用户服务和 Postman 测试做准备。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **大纲**: 包含“目标”、“步骤”、“实现”等章节，具体到“3.4 认证服务 (trade-auth)”、“3.5 认证服务启动与验证”、“3.6 认证服务与 PostMan 使用”。
    *   **配置说明**: 详细说明了 Redis 配置用于 OAuth TokenStore 缓存，以及 Spring Security 认证配置采用支持负载均衡的方式。
    *   **静态资源配置**: 指导用户将自定义的静态资源（如 `static.css` 和 `templates.ftl`）复制到 `resources` 目录下。

*   **代码关键内容**:

    *   **`AuthorizationServerConfig.java`**:
        ```java
        @Bean
        public TokenEnhancer tokenEnhancer() {
            return (accessToken, authentication) -> {
                try {
                    if (GlobalConstants.OAUTH_CLIENT_CREDENTIALS
                            .equals(authentication.getOAuth2Request().getGrantType())) {
                        return accessToken;
                    }
                    final Map<String, Object> additionalInfo = new HashMap<>(initialCapacity: 16);
                    if (null != authUser) {
                        TraderUser traderUser = authUser.getUser();
                        additionalInfo.put(GlobalConstants.OAUTH_DETAILS_USER_ID, traderUser.getId());
                        additionalInfo.put(GlobalConstants.OAUTH_DETAILS_USERNAME, traderUser.getName());
                    }
                    return new DefaultOAuth2AccessToken(accessToken.getValue(), additionalInfo);
                } catch (Exception e) {
                    log.error(e.getMessage(), e);
                    return accessToken;
                }
            };
        }
        ```

    *   **`WebSecurityConfigurer.java`**:
        ```java
        @Configuration
        @EnableWebSecurity
        public class WebSecurityConfigurer extends WebSecurityConfigurerAdapter {
            @Override
            protected void configure(HttpSecurity http) throws Exception {
                http
                    .formLogin()
                        .loginPage("/token/login")
                        .loginProcessingUrl("/token/form")
                        .defaultSuccessUrl("/token/success")
                        .and()
                    .authorizeRequests()
                        .antMatchers("/token/**", "/actuator/**").permitAll()
                        .anyRequest().authenticated()
                        .and()
                    .csrf().disable();
            }
        }
        ```

    *   **`StockPasswordEncoder.java`**:
        ```java
        @Component
        public class StockPasswordEncoder implements PasswordEncoder {
            @Override
            public boolean matches(CharSequence rawPassword, String encodedPassword) {
                try {
                    String password = EncryptUtil.encryptSigned(rawPassword.toString());
                    boolean isMatch = encodedPassword.equals(password);
                    return isMatch;
                } catch (Exception e) {
                    log.error(e.getMessage(), e);
                    return false;
                }
            }
        }
        ```

    *   **`application.yml`**:
        ```yaml
        # Redis 配置
        redis:
          host: 127.0.0.1
          password: 123456
          port: 6379

        # Spring Security 配置
        security:
          oauth2:
            resource:
              loadBalanced: true
              token-info-uri: http://trade-auth/oauth/check_token
            client:
              client-id: app
              client-secret: app
              scope: server
              ignore-urls: # 如果子模块重写这里的配置就会被覆盖
        ```

---

### 4) 关键场景与演示描述

*   **场景一：自定义令牌增强器** (00:05-00:15)
    *   讲师在 `AuthorizationServerConfig` 类中，演示如何通过 `@Bean` 注解定义一个 `TokenEnhancer`。
    *   代码逻辑判断客户端是否使用了 `client_credentials` 授权模式，如果是，则直接返回原始令牌；否则，通过 `OAuth2Authentication` 获取用户信息，并将其存入 `additionalInfo` Map 中，最终返回一个包含用户信息的增强型令牌。

*   **场景二：安全配置** (00:15-00:25)
    *   讲师创建并配置 `WebSecurityConfigurer` 类，继承 `WebSecurityConfigurerAdapter`。
    *   通过 `configure(HttpSecurity http)` 方法，配置了表单登录、权限控制和关闭 CSRF 保护。
    *   特别强调了 `antMatchers` 中的 `/token/**` 和 `/actuator/**` 路径允许所有用户访问，这是为了方便 OAuth2 令牌的获取和健康检查。

*   **场景三：自定义密码编码器** (00:25-00:35)
    *   讲师创建 `StockPasswordEncoder` 类，实现 `PasswordEncoder` 接口。
    *   在 `matches` 方法中，使用 `EncryptUtil.encryptSigned()` 方法对原始密码进行 MD5 和 Base64 加密，然后与数据库中存储的加密密码进行比对。
    *   演示时，弹出一个“新建文件”的对话框，提示用户“一致！”，表明密码匹配成功。

*   **场景四：配置文件详解** (00:35-00:55)
    *   讲师打开 `application.yml` 文件，详细讲解了数据库（Druid）、Redis、以及 Spring Security 的 OAuth2 配置。
    *   特别指出 `ignore-urls` 配置项，说明其作用是避免子模块重写配置时导致的冲突。
    *   展示了如何配置静态资源，将 `static.css` 和 `templates.ftl` 文件复制到 `resources` 目录下，以便在前端页面中使用。

*   **场景五：项目结构与资源管理** (00:55-01:05)
    *   讲师在 PPT 中展示了项目的目录结构，强调了 `resources` 目录下 `static.css` 和 `templates.ftl` 文件的重要性。
    *   通过“Reset All”功能，演示了如何重置配置，以便在不同环境下进行测试。

---
