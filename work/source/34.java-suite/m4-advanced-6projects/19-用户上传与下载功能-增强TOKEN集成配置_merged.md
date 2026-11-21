# 19-用户上传与下载功能-增强TOKEN集成配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们就在项目当中去集成和使用增强token

这里我们需要通过增强token来获取用户的ID信息

并于咱们在接入层去进行使用

商业账件咱们在用户上传的时候

也需要用到用户ID

那么咱们来看一下具体如何去封装和使用

咱们回到用户服务工程

在下面创建一个base controller

这base controller就封装统一的解口方法

那么首先我们要定义一个成员变量

token store

让它注入进来

加上注释

这个是token的存取管理解口

接着我们就来封装对应的方法

第一个方法就是获取当前的token

get

token

第一步要获取request对象

attp

so let request

好

我们就通过上下文来获取request对象

咱们来看一下

request

获取request hbuse

这里我们要做一个转换

转换成servlet request hbuse

然后再去获取request对象

好

这个就是从它的request上下文当中

获取hbuse对象

然后把它转换为servlet

在这里我们就来做一个转换

这里就可以通过servlet request hbuse

去获取get request

获取request对象

第二步咱们来看一下

第二步就是获取token信息

然后怎么获取

就可以从request当中去取得它的token

是从head当中获取

它的属性名称叫authored position

咱们要加个判断

如果是不等于空

那么这个token呢

我们要做一个分析啊

我们做一个替换

replace access token

然后呢

value type在这里面呢

我们要把这个value呢

把它给去除

这个意思呢

就是要把前面的value这个名称呢

给它去掉

我们呢

只要获取完整的token值就可以

好

那么呢

就将token呢返回

接下来呢

咱们就要实现了获取token的项目

我们先来看看我们获取用户ID的方法

我tag

用户ID呢是一个长整形

get user ID

sruce

compound exception

第一步呢要获取

access token信息

这个是从token store当中获取

读取access token

那从哪里读取呢

就是从刚才咱们碰到的方法

获取当前token

从这个token值呢

然后去读取token store当中呢

具体的token信息

那么咱们也要做唯空判断

os2

如果唯空呢

咱们抛出对应一场compound exception

给它一个错误码

就是说系统的token呢

未能获取到有效的token信息

好了

第二步呢

咱们就要获取

token的增强信息

那么怎么获取呢

我们来看一下

首先呢我们去创建一个门口

我们的门口对象

从os2 access token当中呢

去获取它的附加信息

如果是唯空呢

咱们同样也创出对应一场

这样的话呢

我们可以看到有很多的唯空判断对不对

目的的话呢是要为了保证咱们代码的建状性

当一些可能想到异常了

我们先事先处理好

然后呢下面就会专注于具体的业务逻辑的处理

是意思

就是说未能获取到

有效的用户信息

第三步呢

我们要获取

用户的

ID信息

用户的ID

通过呢

additional

inforce

去获取到

他们的用户ID

这个从常量当中

os2

然后呢

定义的常量

usid

好从这里获取

那么如果是唯空呢

同样咱们也创出一个异常

因为你拿不到usid

之后的逻辑化呢

都不好处理

所以呢

我们要将他异常

直接呢抛出来

这个并非是一些辅助信息对不对

usid呢是一个比较重要的数据

所以呢咱们要抛出异常

由

外层呢去决定是否接受处理

是意思

not access user

好最后呢咱们就可以返回usid

接着呢咱们在这种讲习当中

回顾一下刚才的实现处理流程

首先呢咱们要去获取透明的usid

拿到了当前用户的token

每个接口请求呢

他都会在头部附带value token信息

由getclient token呢

去负责具体的处理

根据token呢

通过token store呢

从缓存当中获取到信息

唯空呢就

抛出异常

拿到缓存信息之后呢

从map stream object当中呢

去获取

具体的用户ID

同时呢我们也可以做相应的异常判断

这里啊

刚才也给大家做了讲解对不对

由外层去决定

出现异常时候呢

还要不要去处理呢

接下来的业务逻辑

那么咱们呢来看一下

token store是从哪里来的

这里呢我们要做一个配置

我们看一下

在global system configuration当中呢

我们要实现了

他token store的一个具体配置

之前呢咱们是实现了分布式ID的配置

接着话呢

我们看一下如何去实现token store配置呢

首先我们要去定义一个

ladies connection factory

ladies connection factory呢

这里还没有引路进来

那么咱们呢要将他的

主件呢加入进去

在pum文件当中

加入呢ladies的依赖主线

然后呢从讲义当中让他copy进来

这个呢是ladies的缓冲依赖主线

我们呢加入到最下面

导入生效

加入完成之后呢咱们再来实现具体的代码

ladies connection factory

然后呢将他注入进来

autowide

下面呢咱们再给他定义呢

token store的配置

public

token store

基于ladies就实现了token存储

给他创建一个新的

token

store对象

将ladies connection factory呢注入进去

然后呢token store

在这里面我们给他一个

key的保存前缀

这个呢在global

constance下面呢定义的长量

叫auth

place fix

设置完token的前缀key之后呢

咱们就可以返回token store

其他的话呢咱们就不用做调整了

然后呢

给他一个注解

纳入视频笼子当中

加上注释

这个呢是token

store的

配置

好接着的话呢咱们再看一下

还有哪些配置呢

这里呢咱们是实现了他的代码配置

然后呢

我们来看一下

这里要和认证服务的token store要保持一致

否则呢你不能正常拿到对应的token缓存数据

所以呢

我们可以看到token store呢

他的前缀

我们在这里呢都是采用了authplace fix

key作为他的统一前缀

我们搜寻一下

在auth下面呢

他的token store的配置也是采用这个前缀对不对好

其他的就没做额外的调整

这一块呢他没有做实际的改动

仍然是按照他默认的配置来

那么呢

我们在这里就不用再重复实现

好

再往下面我们来看一下

这个依赖已经添加商区了

我们最后呢要在工程当中去增加呢

Ladies的连接配置信息对不对

这个呢我们将拿copy进去

在咱们的

stock user

配置文件当中

他是放在哪里

放在spring的

属性下面

然后呢

他在放在哪里

他是放在spring的属性下面

我们呢把它copy进来

这个可以把它去掉

下面的就是Ladies的缓存配置咱们conclude的话呢移到上面去

在这里呢

这些属性的话都配置正确

指向的是本机的Ladies缓存服

好

这样呢

启动工程之后就可以直接从base control当中

去

获取到用户的ID通过get user ID方法

那咱们呢回过头来

再去修改呢

我们刚才实现了

用户上传接口

这个呢就是

可以从get user ID方法当中去获取对不对

首先呢我们要去继承

base control了

在这里呢咱们就可以

通过get user ID来获取到用户的实际ID

这样呢咱们就实现了增强token的

集成配置和运用

这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程讲解了在 Spring Boot 项目中，如何通过增强的 OAuth2 Token（Bearer Token）来高效获取用户 ID，从而避免在每个接口中都调用认证服务。核心思想是将用户信息（如用户 ID）缓存到 Redis 中，通过 Token 从 Redis 中直接读取，以减少网络请求和计算成本。课程主要演示了如何在 `BaseController` 中封装 `getUserId()` 方法，并配置 Redis 缓存，最终实现一个可复用的用户身份获取方案。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，展示课程大纲，当前章节为“2.5 利用增强Token高效获取信息”。
*   **00:00:05 - 00:00:15**：讲师介绍本节目标：通过 Token 直接从 Redis 获取用户 ID，减少对认证服务的调用。
*   **00:00:15 - 00:00:30**：讲师讲解方案优势：减少交互次数、降低加密成本、减少数据传输。同时指出其缺点：需要暴露外网，安全性风险。
*   **00:00:30 - 00:00:45**：讲师开始演示代码，进入 `BaseController` 类。
*   **00:00:45 - 00:01:00**：演示如何从 HTTP 请求头中获取 Bearer Token，并移除前缀 `Bearer `。
*   **00:01:00 - 00:01:15**：演示如何使用 `tokenStore.readAccessToken()` 方法解析 Token。
*   **00:01:15 - 00:01:30**：演示如何从解析后的 `OAuth2AccessToken` 对象中获取附加信息（`additionalInformation`）。
*   **00:01:30 - 00:01:45**：演示如何从附加信息中提取用户 ID（`user_id`），并抛出异常处理。
*   **00:01:45 - 00:02:00**：讲师切换到 PPT，讲解如何在工程中配置 Redis 依赖和连接信息。
*   **00:02:00 - 00:02:15**：展示 `application.yml` 中的 Redis 配置示例。
*   **00:02:15 - 00:02:30**：展示 `GlobalSystemConfiguration` 类中创建 `RedisTokenStore` 的代码。
*   **00:02:30 - 00:02:45**：讲师总结，说明配置完成后，`BaseController` 中的 `getUserId()` 方法即可正常使用。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT 内容

*   **章节标题**：`2.5 利用增强Token高效获取信息`
*   **核心思想**：通过 Token 直接从 Redis 获取用户 ID，减少对认证服务的调用。
*   **方案优缺点**：
    *   优点：减少交互次数、降低加密成本、减少数据传输。
    *   缺点：需要暴露外网，安全性风险。
*   **依赖配置**：
    ```xml
    <!-- Redis 缓存依赖 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-redis</artifactId>
        <version>${spring-cloud-starter.version}</version>
    </dependency>
    ```
*   **Redis 配置示例**：
    ```yaml
    spring:
      # Redis 缓存配置
      redis:
        host: 127.0.0.1
        port: 6379
    ```

#### 代码关键内容

*   **`BaseController.java` 中的 `getUserId()` 方法**：
    ```java
    protected Long getUserId() throws ComponentException {
        // 1. 获取Token信息
        String token = request.getHeader("Authorization");
        if (null != token) {
            token = token.replace(OAuth2AccessToken.BEARER_TYPE, replacement);
        }
        // 2. 获取Token的增强信息
        OAuth2AccessToken authAccessToken = tokenStore.readAccessToken(getCurrentToken());
        if (null == authAccessToken) {
            throw new ComponentException(ApplicationErrorCodeEnum.SYS_NOT_VALID_TOKEN);
        }
        // 3. 获取用户的增强信息
        Map<String, Object> additionalInfos = authAccessToken.getAdditionalInformation();
        if (null == additionalInfos) {
            throw new ComponentException(ApplicationErrorCodeEnum.SYS_NOT_ACCESS_USER);
        }
        Long userId = (Long) additionalInfos.get(GlobalConstants.OAUTH_DETAILS_USER_ID);
        if (null == userId) {
            throw new ComponentException(ApplicationErrorCodeEnum.SYS_NOT_ACCESS_USER);
        }
        return userId;
    }
    ```

*   **`GlobalSystemConfiguration.java` 中的 `tokenStore` 配置**：
    ```java
    public TokenStore tokenStore() {
        RedisTokenStore tokenStore = new RedisTokenStore(redisConnectionFactory);
        tokenStore.setPrefix(GlobalConstants.OAUTH_PREFIX_KEY);
        return tokenStore;
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：方案介绍与优势分析**（00:00:05 - 00:00:30）
    *   讲师在 PPT 上展示方案的核心思想：通过 Token 直接从 Redis 获取用户 ID。
    *   讲师用文字描述了该方案的优势：减少交互次数、降低加密成本、减少数据传输。
    *   讲师也指出了该方案的缺点：需要暴露外网，安全性风险。

*   **场景二：代码实现演示**（00:00:30 - 00:01:45）
    *   讲师在 IntelliJ IDEA 中打开 `BaseController.java` 文件。
    *   讲师演示如何从 HTTP 请求头中获取 `Authorization` 头，并移除 `Bearer ` 前缀。
    *   讲师演示如何使用 `tokenStore.readAccessToken()` 方法解析 Token。
    *   讲师演示如何从解析后的 `OAuth2AccessToken` 对象中获取附加信息。
    *   讲师演示如何从附加信息中提取用户 ID，并抛出异常处理。

*   **场景三：配置 Redis**（00:01:45 - 00:02:30）
    *   讲师切换到 PPT，讲解如何在工程中配置 Redis 依赖。
    *   讲师展示 `application.yml` 中的 Redis 配置示例。
    *   讲师展示 `GlobalSystemConfiguration.java` 中创建 `RedisTokenStore` 的代码。

*   **场景四：总结与应用**（00:02:30 - 00:02:45）
    *   讲师总结，说明配置完成后，`BaseController` 中的 `getUserId()` 方法即可正常使用。
    *   讲师强调该方案的可复用性，可以在其他 Controller 中直接调用。
