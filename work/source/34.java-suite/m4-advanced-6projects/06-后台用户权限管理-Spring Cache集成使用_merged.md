# 06-后台用户权限管理-Spring Cache集成使用 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们就来学习Splint Cache的集成配置使用

这里先讲说明一下

Splint它从3.1开始定义了

Org Splint Framework Cache

以及Cache Manager接口来统一不同的返存技术

并且支持使用JCache

这个是JSR107的规范

这种注解就简化了咱们的开发

那么我们来看一下Splint Cache

它有哪些核心功能接口

又提供了怎样的功能呢

首先咱们可以看到Cache

这个意思它是返存接口

定义了返存的操作

具体的实现有包括像Ladies Cache

基于InHedge的Cache

然后Concrete Map的Cache

这些就根据咱们的实际需要

去采用不同的方式做具体实现

下面是Cache Manager返存管理器

这个返存管理器可以管理各种返存Cache组件

咱们可以搜寻下

原来之前实现的代码Cache Manager

在这里我们可以看到

Auth Stock User Detail Service下面采用到的Splint Cache返存

之前咱们讲解了Auth2的集成配置

那么我们采用的是密码模式认证

为了优化它整体的处理性能

咱们是结合了Splint Cache返存去做对应的实现

那么我们可以看到Cache Manager具体的用法

在这里它要将Cache Manager注入进去

然后

我们可以看到Cache Manager具体的用法在这里它要将Cache Manager注入进去

去获取对应的Cache对象

接着才去根据你的Key值来找到对应的返存内容

好

Cache Manager刚才从代码当中给大家做了一个讲解

它的意思就是去管理各种返存组件

然后拿到对应的Cache对象

接下来就是Cache Able

它主要是针对方法级别的配置

能够根据方法的请求参数对齐进行返存

这个之前咱们也做了几个课题

也做了讲解

那咱们可以从代码当中再回复一下

在这里我们Auth Client Detail Service里面

有一个load client by client ID

也就是说去获取client信息

在这里加入了返存的处理

这个Cache Able的话

就是对返存的具体配置

咱们可以看到还有Key以及它的一个条件

这个是它对应的存储的前缀信息

咱们可以点进去看到

这里它通过冒号进行分割开启

如果咱们通过Ladies客户端连接Ladies

可以看到它的一个Key

也就是它最终拼接的结果

就是刚才的长量再加上这个Key client ID参数

这样就组成了一个完整的Key值

它的作用就是要对方法的返回对象

做一个返存

也就是Client Details加入到返存当中

下面的话是Cache Invict

这个是返存的星空

然后Cache Invict

Cache Put保证方法被调用

又希望结果被缓存

它和Cache Able具体区别是在于

每次的话它都会去调用方法

而且又会去更新缓存

经常是用于咱们的更新操作上面

如果说咱们在这个方法里面加入了Cache Put

那么它每次都会进入到内部的调用逻辑

如果只是Cache Able

那么第一次它会进入里面逻辑

下次调用的时候

它就会再次进入内部的调用逻辑

而直接从缓存当中获取到具体的返回值

这个是它们的差异

然后Enable Cache

这个就是说要开启咱们的Split Cache的缓存功能

咱们可以回到代码当中

来看一下它具体的使用

这个注解它就加在启动内当中

这样它就能够去开启Split Cache

缓存功能

下面是Key Generator

这个是设置缓存数据时Key的生成策略

然后Serialize是缓存数据时Value的区别化策略

Cache Config是统一配置本类的缓存注解的属性

这个是用于内上面的注解

再往下面咱们来看一下

Cache Able

Cache Put

还有Cache Invict

主要的一些参数

咱们刚才也从代码上面做了一个列表

我们可以看到这个是配置缓存的名称

在Split配置文件当中去定义

必须要指定至少一个配置值

比如说像Cache Able

这里面的话Value指定一个值

或者是Cache Able

在这里面的话咱们可以指定两个值

如果你不加上这个

它就没法进行了缓存的存储

下面是缓存的Key

可以为空

因为你前面配置了Value

对不对

你这里为空的话

它就是以Value进行Key值的存储

如果指定的话

咱们要按照SPL表达式进行编写

如果是不指定的

则确实按照方法的所有参数

还会进行一个组合

在这里咱们可以看到Cache Able配置了一个Value

对不对

这个Key

它就是一个SPL表达式

因为它要去读取参数的具体值

你不配置的话

在这里

它就是按Test Cache进行一个组合

来拼接存储

下面是Condition

这个就是缓存的条件

可以去配置

也可以不用去配置

如果配置的话

也要遵循SPL的表达式

它的结果只会两种

要么就是Cue

要么是False

只有为Cue时

才会进行了对应的缓存

也就是说你这个注解才能够生效

比如说这个Cache Able

咱们配置了一个Value

又配置了一个Condition

对不对

它的条件是什么

就是U至Nim的长度必须要大于二

如果说你的Nim不符合这个条件

在这里

它就不会进行对应的缓存存储

下面是Unless条件

这个是否定缓存

当条件结果为Cue时

它就不会进行缓存

它和这里面的False就是相反了

如果说咱们Cache Able里面

配置了一个Value

配置了一个Unless

也就是说你的U至Nim长度大于二的时候

它就不会生效

这个缓存的话就不会进行存储

下面的话

是All in choice

在这里它的意思是

是否清空所有的缓存内容

缺省为False

如果是指定为Cue

则方法调用之后

它就立即会清空所有的缓存

这个大家要慎重一点

下面就是Before Invocation

也就是说在方法执行前

咱们就进行了缓存的清空

缺省是为False

如果是指定为Cue

那么在方法还没有进行到

内部逻辑处理的时候

它就会清空缓存

缺省情况下

方法执行抛出异常

它是不会清空缓存

也就是说你的一个service接口

如果在上面加上一个注解

这个service接口里面

它抛出了一个异常信息

你不加上这个Before Invocation

它抛出异常的时候是不会清空缓存的

那么你想让它抛出异常的时候

就要去清空缓存的

那么可以加上这个Before Invocation

好

这个是它的一个应用场景

接下来咱们就来看一下具体如何去实现了

使用起来其实也很简单

要在咱们的工程服务当中

加上SpringCage的组件依赖

之前咱们是在认证服务上面加了这个依赖

这个后台管理服务还没有增加

咱们把它加入进去

加入完成之后

咱们通过Mavin Help这个插件来查看一下

refresh

然后我们搜寻

SpringContextSupport

这样咱们就可以看到

SpringCage的组件是它的Cache

下面的话它依赖了SpringContextSupport

它是基于这个组件去做的具体实现

这两个的话

插件功能是不一样的

一个是处理Session

一个是用于咱们的业务缓存的处理

接下来就要去启动内当中

去开启了缓存功能

EnableCache

这样的SpringCage就已经集成配置完成

咱们再回到讲义当中

下面我们会实现后台用户的配置完成

用户登录接口

在下面讲到的时候

咱们还会去做具体的实现

用户登录接口

在这里面就加入了缓存的处理

通过CacheManager来做对应的实现

它在Auth的UserServiceImplement

UserLogging方法里面做的具体的调用

CacheManager它实际上就是Ladies

以Key和Value的结构

二进制数据的形式进行的存储管理器

Ladies里面的Key

它并非上面的GlobalConception里面定义的长量

这个只是它的一个前缀

实际上它是由前缀再加上具体的参数值

然后组成了一个完整的Key

咱们后面在实现过程当中

做功能测试验证的时候

会通过Ladies工具

然后再去查看一下它具体的一个Key的存储信息

咱们在这里可以通过截图看到

它的一个完整的Key可以看到

这个是AuthMenu

就是它在这里定义的长量前缀信息

下面是User的ID

这是它的后缀

然后完整的拼接起来

就形成了一个Key的键值

好

这一点大家要理解清楚

接下来咱们就开始要实现用户的登录接口

这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于 Spring Cloud 项目中集成 Spring Cache（缓存）功能的教学内容。讲师通过演示如何在项目中引入缓存依赖、使用注解（如 `@Cacheable`、`@CachePut`、`@CacheEvict`）来简化开发，并深入讲解了缓存的底层实现机制。视频主要围绕 `AuthClientDetailsService` 服务类中的缓存注解应用，以及如何通过 `CacheManager` 在 Redis 中存储和管理缓存数据。讲师还展示了如何在 `pom.xml` 中配置依赖，并解释了缓存键（key）的生成逻辑。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开始，讲师在 Typora 文档中展示课程大纲，当前章节为“1.4 Spring Cache 集成使用”。
*   **00:00:05 - 00:00:15**: 讲师在文档中介绍 Spring Cache 的核心接口，包括 `Cache` 和 `CacheManager`。
*   **00:00:15 - 00:00:30**: 讲师在文档中列出并解释了常用的缓存注解，如 `@Cacheable`、`@CacheEvict`、`@CachePut` 和 `@EnableCaching`。
*   **00:00:30 - 00:00:45**: 讲师在文档中展示 `@Cacheable`、`@CachePut` 和 `@CacheEvict` 注解的主要参数及其作用。
*   **00:00:45 - 00:01:00**: 讲师切换到 IntelliJ IDEA，展示项目结构，并在 `pom.xml` 文件中添加 Spring Cache 的依赖。
*   **00:01:00 - 00:01:15**: 讲师在 IDEA 中展开依赖树，展示 `spring-boot-starter-cache` 依赖会自动引入 `spring-context-support` 和 `spring-session-data-redis` 等相关依赖。
*   **00:01:15 - 00:01:30**: 讲师在文档中讲解 `CacheManager` 在 Redis 中的存储结构，并展示如何通过 `GlobalConstants.AUTHORITY_MENU_KEY` 和 `authorityUser.getId()` 组合生成实际的缓存键。
*   **00:01:30 - 00:01:45**: 讲师在 IDEA 中打开 `AuthClientDetailsService` 类，展示如何在 `loadClientByClientId` 方法上使用 `@Cacheable` 注解。
*   **00:01:45 - 00:02:00**: 讲师在文档中展示 `CacheManager` 在 Redis 中存储数据的示例，说明缓存键的生成逻辑。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **核心功能接口**:
        *   `Cache`: 缓存接口，定义缓存操作。实现有：`RedisCache`、`EhCacheCache`、`ConcurrentMapCache`等。
        *   `CacheManager`: 缓存管理器，管理各种缓存（cache）组件。
        *   `@Cacheable`: 主要针对方法配置，能够根据方法的请求参数对其进行缓存。
        *   `@CacheEvict`: 清空缓存。
        *   `@CachePut`: 保证方法被调用，又希望结果被缓存。与 `@Cacheable` 区别在于是否每次都调用方法，常用于更新。
        *   `@EnableCaching`: 开启基于注解的缓存。
        *   `keyGenerator`: 缓存数据时 key 生成策略。
        *   `serialize`: 缓存数据时 value 序列化策略。
        *   `@CacheConfig`: 统一配置本类的缓存注解的属性。
    *   **@Cacheable/@CachePut/@CacheEvict 主要的参数**:
        *   `value`: 缓存的名称，在 Spring 配置文件中定义，必须指定至少一个。
        *   `key`: 缓存的 key，可以是表达式，也可以是方法参数。
        *   `condition`: 缓存的条件，只有满足条件才会缓存。
        *   `unless`: 缓存的否定条件，只有不满足条件才会缓存。
        *   `sync`: 是否同步缓存。
        *   `beforeInvocation`: 是否在方法执行前就清空缓存，缺省为 false。
    *   **项目使用**:
        *   **POM 增加依赖**:
            ```xml
            <!-- 自动化缓存依赖 -->
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-cache</artifactId>
                <version>${spring-cloud-starter.version}</version>
            </dependency>
            ```
        *   **实际依赖**:
            *   `spring-boot-starter-cache: 2.1.1.RELEASE [compile]`
            *   `spring-context-support: 5.1.8.RELEASE [compile]`
            *   `spring-session-data-redis: 2.1.7.RELEASE [compile]`
            *   `spring-data-redis: 2.1.9.RELEASE [compile]`
    *   **缓存键生成逻辑**:
        *   `CacheManager` 实质在 Redis 是以 key, value 结构，二进制数据形式存储。
        *   Redis 里面的 key 并非上面的 `GlobalConstants.AUTHORITY_MENU_KEY`，它只是前缀，实质是 `GlobalConstants.AUTHORITY_MENU_KEY + authorityUser.getId()`。

*   **代码示例**:
    *   **`AuthClientDetailsService` 类中的 `loadClientByClientId` 方法**:
        ```java
        @Cacheable(value = GlobalConstants.OAUTH_KEY_CLIENT_DETAILS, key = "#clientId", unless = "...")
        public ClientDetails loadClientByClientId(String clientId) throws InvalidClientException {
            return super.loadClientByClientId(clientId);
        }
        ```
    *   **缓存操作代码**:
        ```java
        // 放入缓存
        cache = cacheManager.getCache(GlobalConstants.AUTHORITY_MENU_KEY);
        cache.put(authorityUser.getId(), uris);
        ```

---

### 4) 关键场景与演示描述

*   **场景一：介绍 Spring Cache 核心接口** (00:00:05 - 00:00:15)
    *   讲师在 Typora 文档中，通过表格形式清晰地列出了 Spring Cache 的核心接口 `Cache` 和 `CacheManager`，并简要说明了它们的作用。
*   **场景二：讲解缓存注解** (00:00:15 - 00:00:30)
    *   讲师在文档中逐一列出并解释了 `@Cacheable`、`@CacheEvict`、`@CachePut` 和 `@EnableCaching` 等常用注解，帮助观众理解它们在实际开发中的应用。
*   **场景三：展示项目依赖配置** (00:00:45 - 00:01:15)
    *   讲师切换到 IntelliJ IDEA，打开 `pom.xml` 文件，演示如何添加 `spring-boot-starter-cache` 依赖。
    *   讲师展开依赖树，展示 `spring-boot-starter-cache` 会自动引入 `spring-context-support` 和 `spring-session-data-redis` 等依赖，强调了 Spring Boot 的自动配置能力。
*   **场景四：演示缓存键生成逻辑** (00:01:15 - 00:01:30)
    *   讲师在文档中解释 `CacheManager` 在 Redis 中的存储结构，并通过 `GlobalConstants.AUTHORITY_MENU_KEY` 和 `authorityUser.getId()` 的组合，说明了实际的缓存键是如何生成的。
    *   讲师在 IDEA 中打开 `AuthClientDetailsService` 类，展示如何在 `loadClientByClientId` 方法上使用 `@Cacheable` 注解。
*   **场景五：展示 Redis 缓存数据** (00:01:30 - 00:01:45)
    *   讲师在文档中展示 `CacheManager` 在 Redis 中存储数据的示例，通过 `GlobalConstants.AUTHORITY_MENU_KEY` 和 `authorityUser.getId()` 的组合，说明了实际的缓存键是如何生成的。
    *   讲师在 IDEA 中打开 `AuthClientDetailsService` 类，展示如何在 `loadClientByClientId` 方法上使用 `@Cacheable` 注解。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解本节课程内容。
