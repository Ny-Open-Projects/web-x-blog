# 18-OAUTH2生产实践-认证服务配置讲解 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来咱们接着呢

去实现了web层的接口编写

那之前呢

咱们是实现了设计层的

它的逻辑处理

接着的话呢

我们还去实现认证服务的配置

大家呢

如果暂时跟不上

那我们呢

先来缓一下

咱们呢

回到认证服务

整体的一个工程结构当中

先来捋清楚整个的脉络

那我们可以看到

在整个工程结构当中呢

有数据层

收据层

还有呢

对应的web层

这个web层呢

跟strataf是放在一起了

那还有呢

配置类

整个的话呢

实现起来

相对内容会比较多一点

目前呢

咱们已经将数据层和收据层

已经实现了

对不对

好

那么为什么还去实现web层呢

因为呢

我们要进行认证服务的时候呢

认证服务是不是要提供出一个页面

给咱们去进行登录啊

对不对

这个认证的页面呢

是需要输入用户名

还有用户密码

然后呢

会有一个按钮进行一个登录

那么呢

我们就要在这里呢

提供一个自定义的接口

好

这个呢

就是我们web层接口的一个作用

那

接着的话呢

这个配置类

配置类的话呢

是要去实现OS2的一个集成认证配置

配置下面的话呢

主要有三个配置类

第一个呢

是Organization Server

这个顾名思义呢

就是Sever端的服务配置

它会呢

去实现像我们的OS2的

Circle的一些表印社

它的一些查询配置

然后呢

还有我们Token增强的一些配置

那么Password呢

这个就是密码的一个编码器

如果咱们呢

要自定义密码的一个编码

或者说自定义的密码加密

都可以呢

通过这个类做对应的实现

那么Web Security Config呢

它的主要作用呢

就是Web的一个访问配置

在这里面呢

它可以决定哪些Web接口

然后呢

要通过OS2去认证健全

哪些呢

可以去放行

这个呢

就在这里面去配置的

好

这些作用的话呢

大家一定要明白清楚

整个节奏呢

一定要跟上

好

那咱们呢

就继续回到代码中来做呢

对应的实现

接着的话呢

咱们要将那个Web层的接口呢

做个实现

咱们找到对应的代码

在上面

好

将那个Stock

TokenControler

做一个编写

我们把它放到

Startup下面

New Class

这个接口的话呢

就没有太多技术含量

咱们呢

就直接Copy一下

我们呢

将这里完整的Copy过来

那Copy过来呢

咱们再简要的讲解一下

它提供的哪些接口

它的一些功能和作用是怎样的

先把错误呢

给消灭掉

这个呢

是要Log

所以咱们要装好

LongBlock插件

Log4J2

然后呢

attbhead

Import Class

SpringFrainWalk下面

重新导入一下

就让它

导入那个SpringFrainWalk下面的

因为这个很简单

主要是做一个唯空判断

那这个错误的话呢

解决掉之后

咱们来回顾一下

看一下它整体有哪些接口

前面的话呢

是它的一个Ladies的缓存的操作接口

然后这个TokenStore

是一个增强的Token处理

这个CacheManager是缓存管理器

那么我们可以看到

有制定的什么Login的登录接口

对不对

那么这个制定的登录接口的作用呢

咱们可以去制定自己的交互接口

它的接面

如果是采用默认的OS2的

它的界面来讲呢

比较丑

然后的话呢

交互起来也并不是很好

所以呢

咱们如果是可以呢

去制定自己的一些Logo

或者自己的样式的话呢

就可以呢

去通过这些接口来做一个指向

好

再往下面的话呢

就是它认证的页面

就是成功之后

它要返回到哪里

对不对

或者给它对应的一些提示信息

然后呢

如果说咱们要退出

就这个Token的话呢

咱们想注销

不想用了

咱们也给它提供一个接口

对不对

这样呢

就能够去删除

那这个Token删除的话呢

就要用到Token Store

对不对

咱们要将这个增强Token里面的

所存储的信息呢

将它给清除掉

好

这个呢

就是它的一个处理流程

Logout

好

然后在下面的话呢

就它的另排管理的调用

在这里面的话呢

也可以进行一个另排的一个清除

这个也是一个删除处理

对不对

那这个的话呢

它是一个注销

注销的话呢

它会将所有相关的信息的话呢

全部给清除掉

不同的是呢

Logout

它删除的东西呢

会更多一点

在这里面呢

它只将Token给清除掉

好

这个呢

是Chadstock Token

Ctrl的Web层接口的一个讲解说明

那咱们呢

再来看一下下一个接口

下一个Web层接口呢

是Chaduser

Ctrl了

咱们测试一下

Chaduser

Ctrl接口

它做什么事情呢

我们先

把我们的代码拷贴过来

在这里面呢

它要做的事情呢

其实很简单

就是要获取用户信息

也就是说

它提供的这样一个API接口

对不对

通过这个API接口的话呢

它既可以作为认证服务

也可以作为什么

支援服

咱们要明白它的意思

它就说

想作为一个支援服

到时候通过认证服务

如果是认证成功之后

咱们看一下这个支援服务的接口

能否正常调用成功

好

这个呢

就是这个接口的一个主要功能和作用

那接着的话呢

咱们就来去实现它的一个配置

整个工程的配置内当中呢

讲工程结构的时候呢

也做了大概的一个介绍

会有了三个配置内

那么在这里呢

咱们来逐一实现

new

package

config

接着的话呢

咱们要创建

automation

server config

它要呢

去继承

OS2所提供的一个实现内

这个呢

是automation

然后呢

server config

adapt

然后呢

这个呢

大家可以看到

这个内呢

它实现了

automation

server config

接口

对不对

下面的话呢

都是一些空实现

好

我们呢

先将它的属性加入进来

这个呢

是数据源的配置

autowire

再往下面的话呢

还有用户服务

对不对

user detail

这个接口的话呢

咱们是做了一个实现的

在这里面

将它的名称呢

引入进来

然后呢

autowire

再上对应的注释

用户认证信息健全的

先来

接着话呢

咱们还要去

注注呢

认证管理器

automation manager

这个呢是认证服务管理器

然后呢

autowire

还有呢

缓存服务

缓存服务是基于ladies实现了

ladies

这个呢是ladies的缓存服务

然后呢

咱们呢要去实现了它的一个

osu的

circle信息的一个查询

fios

这个呢

咱们就直接copy过来

在那个讲习当中

将这些语句的话呢

都copy过来

然后呢咱们再做一个讲解

节省一些时间

在这里呢

我们可以看到

它会对于osu client details

这个表呢

进行一个查询

然后这个呢是要查询的字段

下面的话呢

是它查询的拼接语句

可以看到slack

然后呢

它的默认的一个查询语句

它会根据client id做一个排序

在这里呢

它的最主要作用呢

就是查询

它所分配的client id的相关的一个信息

那么呢

如果是咱们不想用这个表呢

通过这种方式

咱们就可以呢

自己去修改

你可以改成其他表

都是可以的

好

那再往下面呢

咱们来回到讲习当中

它的一个缓存配置

内底是缓存配置

加入进来

咱们做个讲解说明

这个呢

是一个key的

烟码类型

它是采用什么

string的

合适

再往下面的话呢

它是

它是key的

烟码类型

也是采用string

这个呢

就是value的

它是一个值

它是采用的

jdk的

这个呢

就是一个续电化

然后再往下面呢

是hash value

值的编码类型

这个呢

也是采用jdk

续电化处理

那这个呢

就是要将

ladies connect fashion

注入进来

设置呢

ladies的

连接公众

好

那接着的话呢

咱们再将这个方法

拷贝进来

这个的话呢

是制定了client查询

就是结合了

这个

这个

这个

这个

这个

这个

这个

这个

这个

就是结合我之前的

所定义的

社科尉区

然后呢

实现的他的一个你的信息的查询

可以看到

家达的设备呢

就继续了

这个呢

时宜尝

抛首的 tapa

这个话呢

咱们再将这个配置呢

cs

我们一顿一顿来看

这个配置是什么意思呢

它是防止申请token

是呢

出现401的认证错误

所以呢

要在这里呢

是允许所有的访问的类型

的好

那个token交易的时候呢

就不会出现这种失灵药的错误

再往下面呢

咱们再来看认证服务的一个具体配置

那认证服务具体配置呢

是怎么做的呢

在这里面我们可以看到他既可以支持呢

先将这个呢

留进来既可以支持get的方法

又可以支持post的方法

对不对

然后在这里呢是token

他的store一个处理配置

这个意思呢就是说你这个token

如何放在那个缓存当中

比如说Ladies当中

你是放在哪key

然后在这里面的话呢

他的一些key的前缀

key的一些格式等等

那么token

inhance这个呢就是token增强的一个处理

咱们

拷贝进来一个是token store

一个呢是token增强的处理

那我们首先来看一下这个token store

token store呢咱们可以看到

他是通过Ladies

去存储他具体的token信息对不对

然后呢给他的一个前缀key

在下面的话呢就是他的一个key的

处理的实现

好

这个呢其实就是说把这个

token信息放在我们的Ladies缓存当中

然后下面的话呢是token的一个增强处理

token增强处理这一块呢比较重要

也是我们整个实现方案的一个核心处理部分

后面呢还有

整个的web安全性的一些配置

以及呢密码

这个编码相关的一些配置

那这一讲呢咱们先讲到这里

下面章节当中呢咱们再做具体讲解

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程是关于在 Spring Cloud 微服务架构中，如何实现一个基于 OAuth2 协议的自定义认证服务（`trade-auth` 服务）。讲师通过演示代码，讲解了如何配置授权服务器（`AuthorizationServerConfig`），自定义客户端详情服务（`AuthClientDetailService`），以及实现核心的令牌（Token）接口（`TradeStockTokenController`）和用户信息接口（`TradeUserController`）。整个过程强调了使用 Redis 作为令牌存储，以减少对数据库的依赖，并展示了如何通过 `@Autowired` 注入 `TokenStore`、`AuthenticationManager` 等核心组件，以及如何自定义 `TokenEnhancer` 来增强令牌信息。课程内容聚焦于代码实现细节，旨在帮助开发者理解 OAuth2 认证服务的底层构建方式。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，讲师介绍本节内容是关于“认证服务”的实现。
*   **00:05 - 00:15**: 讲解 `AuthorizationServerConfig` 类，这是授权服务器的核心配置类，继承自 `AuthorizationServerConfigurerAdapter`。
*   **00:15 - 00:25**: 介绍 `AuthClientDetailService` 类，用于自定义客户端详情的查询逻辑，通过重写 `configure` 方法来设置自定义的 SQL 查询语句。
*   **00:25 - 00:35**: 讲解 `TradeStockTokenController` 类，用于处理获取和注销令牌的 HTTP 请求。
*   **00:35 - 00:45**: 展示 `TradeUserController` 类，用于根据用户名获取用户信息。
*   **00:45 - 00:55**: 讲解 `TokenEnhancer` 的自定义实现，用于在生成令牌时添加额外信息。
*   **00:55 - 01:05**: 总结本节内容，强调了 OAuth2 认证服务的核心组件和配置方法。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **左侧大纲**：显示了课程的结构，包括“目标”、“步骤”、“实现”等部分，以及“第2章 OAuth2生产实践”和“第3章 用户服务”等章节。
*   **文档标题**：`Day7.md - Typora`，表明课程内容可能以 Markdown 文档形式记录。

#### 代码关键内容

*   **`AuthorizationServerConfig.java`** (授权服务器配置)
    *   **类定义**：`public class AuthorizationServerConfig extends AuthorizationServerConfigurerAdapter`
    *   **成员变量**：
        *   `private DataSource dataSource;` // 数据源，用于查询客户端详情。
        *   `private UserDetailsService authStockUserDetailService;` // 用户详情服务。
        *   `private AuthenticationManager authenticationManager;` // 认证管理器。
    *   **配置方法**：
        *   `configure(ClientDetailsServiceConfigurer clients)`：用于自定义客户端详情服务。
            ```java
            String BASE_FIND_STATEMENT = "select " + CLIENT_FIELDS + " from t_oauth_client_details";
            String DEFAULT_FIND_STATEMENT = BASE_FIND_STATEMENT + " order by client_id";
            String DEFAULT_SELECT_STATEMENT = BASE_FIND_STATEMENT + " where client_id = ?";
            ```
            ```java
            AuthClientDetailService clientDetailsService = new AuthClientDetailService(dataSource);
            clientDetailsService.setSelectClientDetailsSql(DEFAULT_SELECT_STATEMENT);
            clientDetailsService.setFindClientDetailsSql(DEFAULT_FIND_STATEMENT);
            clients.withClientDetails(clientDetailsService);
            ```
        *   `configure(AuthorizationServerEndpointsConfigurer endpoints)`：用于配置授权端点。
            ```java
            endpoints
                .allowedTokenEndpointRequestMethods(HttpMethod.GET, HttpMethod.POST)
                .tokenStore(tokenStore())
                .tokenEnhancer(tokenEnhancer())
                .userDetailsService(authStockUserDetailService)
                .authenticationManager(authenticationManager)
                .reuseRefreshTokens(false);
            ```

*   **`TradeStockTokenController.java`** (令牌接口)
    *   **类定义**：
        ```java
        @RestController
        @RequestMapping("/token")
        @Log4j2
        public class TradeStockTokenController {
        ```
    *   **成员变量**：
        *   `private static final String STOCK_OAUTH_ACCESS = GlobalConstants.OAUTH_PREFIX_KEY;`
        *   `@Autowired private RedisTemplate stockRedisTemplate;` // 用于存储令牌。
        *   `@Autowired private TokenStore tokenStore;` // 用于管理令牌。
    *   **方法**：
        *   `@PostMapping("/logout")`：用于注销令牌。
            ```java
            String tokenValue = authHeader.replace(OAuth2AccessToken.BEARER_TYPE, "").trim();
            OAuth2AccessToken accessToken = tokenStore.readAccessToken(tokenValue);
            if (accessToken == null || StringUtils.isEmpty(accessToken.getValue())) {
                return "退出失败, token 无效";
            }
            OAuth2Authentication auth2Authentication = tokenStore.readAuthentication(accessToken);
            tokenStore.removeAccessToken(accessToken);
            return "退出成功, token 已清除";
            ```
        *   `@PostMapping("/token")`：用于获取令牌（代码未完全展示，但逻辑类似）。

*   **`TradeUserController.java`** (用户信息接口)
    *   **方法**：
        ```java
        @RequestMapping("/user")
        @ResponseBody
        public UserDetails getUser(@RequestParam("username") String username) {
            UserDetails userDetails = authStockUserDetailService.loadUserByUsername(username);
            return userDetails;
        }
        ```

*   **`TokenEnhancer.java`** (令牌增强器)
    *   **类定义**：
        ```java
        @Bean
        public TokenEnhancer tokenEnhancer() {
            return (accessToken, authentication) -> {
                try {
                    if (GlobalConstants.OAUTH_CLIENT_CREDENTIALS.equals(authentication.getOAuthRequest().getGrantType())) {
                        return accessToken;
                    }
                    final Map<String, Object> additionalInfo = new HashMap<>(initialCapacity: 16);
                    // 添加额外信息
                    return new DefaultOAuth2AccessToken(accessToken.getValue(), additionalInfo);
                } catch (Exception e) {
                    throw new RuntimeException(e);
                }
            };
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构展示**
    *   讲师在 IDE 中展示了 `bulls-stock` 项目的整体结构，包括 `bulls-stock-common`、`bulls-stock-oauth` 等模块。
    *   重点展示了 `bulls-stock-oauth` 模块下的 `src/main/java/com/itcast/bulls/stock/trade/oauth` 目录，其中包含 `AuthorizationServerConfig`、`AuthClientDetailService`、`TradeStockTokenController` 等核心类。

*   **场景二：自定义客户端详情服务**
    *   讲师在 `AuthorizationServerConfig.java` 中，通过重写 `configure` 方法，自定义了 `AuthClientDetailService`。
    *   他展示了如何通过 `setSelectClientDetailsSql` 和 `setFindClientDetailsSql` 方法，将默认的 SQL 查询语句替换为自定义的查询语句，以支持按 `client_id` 查询。

*   **场景三：令牌接口实现**
    *   讲师在 `TradeStockTokenController.java` 中，演示了如何实现 `/token` 和 `/logout` 接口。
    *   他详细讲解了 `logout` 方法的逻辑：从请求头中提取 `Authorization` 字段，解析出 `access_token`，然后通过 `tokenStore` 读取并删除该令牌，最后返回相应的结果。

*   **场景四：用户信息接口实现**
    *   讲师在 `TradeUserController.java` 中，演示了如何实现 `/user` 接口。
    *   他讲解了如何通过 `@RequestParam` 获取用户名，并调用 `authStockUserDetailService.loadUserByUsername` 方法获取用户详情，然后返回给前端。

*   **场景五：令牌增强器实现**
    *   讲师在 `AuthorizationServerConfig.java` 中，演示了如何自定义 `TokenEnhancer`。
    *   他讲解了 `tokenEnhancer` 方法的逻辑：当认证类型为 `client_credentials` 时，直接返回原始令牌；否则，创建一个包含额外信息的 `DefaultOAuth2AccessToken` 对象并返回。

---

以上是根据视频画面截图整理出的结构化信息，希望能帮助您更好地理解这段技术课程的内容。
