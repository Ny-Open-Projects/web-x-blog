# 05-分布式锁-资金服务集成分布式锁 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们就在资金服务里面去实现分布式锁的集成运用

首先咱们思考一下资金服务的枷锁处理逻辑

在使用分布式锁之前

我们需要考虑以下的问题

第一锁的力度是到什么级别

如果没有拿到锁

我们又该如何进行处理

第一个问题锁的力度在这里我们控制在账户的级别

也就是根据账户的ID进行枷锁处理

确保同一时刻每一个账户只有一个请求在进行处理

那如果不能立刻拿到锁

咱们会先进行等待

达到指定时间之后

如果还不能拿到锁

这个时候我们就要封装一个异常

返回给客户端

好那接下来咱们就对分布式锁组件做进一步的封装处理

咱们回到代码工程当中

在公用的Boss Stock Common Service工程下面

我们找到Ladies

Lock Service

这个代码咱们之前已经引用进来

我们来看一下代码的具体实现

首先是进行促使化

这里传递了两个参数

一个是Ladies Lock Registry

这个是锁的注册管理器

另外一个是Wait Time

枷锁等待的超时时间

接下来我们提供了两个封装方法

一个是Try Lock尝试枷锁的处理

另外一个是解锁的处理Unlock

那咱们来看一下

枷锁这一块的处理逻辑

注意这里枷锁的类型是采用持续类型

不能传递其他的类型

否则会爆出异常

这一点大家要注意一下

下面就是尝试进行枷锁

这里会传递一个等待时间

这个也就在初始化的时候所传递的Wait Time

如果一直不能获取到锁

超过指定等待时间之后

它就会抛出一个异常

枷锁成功的话呢

它的结果就会返回为Q

这个呢就是Try Lock方法的处理逻辑

接着咱们再看一下Unlock的处理

Unlock处理呢就比较简单

首先是通过LegitLockRegister

获取一个Lock的锁对象

同样咱们要传递锁的Key值

这个Key值要和上面Try Lock里面的Key保持一致

接着再调用Unlock方法进行锁的释放

这个呢就是解锁的处理逻辑

好

那接下来我们再去看一下

资金服务如何去集成分布式锁的配置

咱们回到工程当中

定位到资金服务的Ladies Configuration

这里咱们去加上分布式锁的配置

首先要定义Ladies Lock

Register

Ladies Lock

传递Ladies Connection Factory

接下来我们就去初始化分布式锁的管理器

并且设置超时时间

Ladies Lock Register

创建锁的对象管理器

传递Ladies Connection Factory

再传递注册管理器的Key值

这个呢是资金服务的注册管理器

然后设置默认的超时时间

Distribute

Lock Key Is Here

我们可以看一下

这里面的超时时间默认了是30秒

接下来咱们要返回Ladies Lock Register的对象

在方法上面增加并注解

然后添加对应注释

这个呢是分布式锁的配置

接下来咱们就将刚才所封装的

Ladies Lock Service注入进来

Public Ladies Lock Service

Ladies Lock Register

将上面定义的Ladies Lock Register

作为参数传递进来

Ladies Lock Service

New Ladies Lock Service

传递分布式锁的注册管理器

传递加锁等待时间

Wait Time这里呢是等于5秒

Return Lady Lock Service

Return Lady Lock Service

这里呢是等于5秒

Return Lady Lock Service

Return Lady Lock Service

Return Lady Lock Service

Return Lady Lock Service

这里是配置分布式锁的实现类

咱们是基于Ladies实现的分布式锁

我们要去检查工程配置

Ladies的连接是否配置正确

检查Ladies的缓存配置

好

这里已经加上了Ladies的缓存配置

那资金服务的Ladies分布式锁

咱们就已经集成配置完成

接下来

咱们就要在额度调整接口里面

加入分布式锁的控制

咱们回到工程当中

定位到资金服务的GRBC接口

GRBC Stock Finance Service

找到更新账户余额的接口

这里我们要在更新账户资金处理之前

调用分布式锁加锁处理

Ladies

Lock Registry

加入分布式锁

Lock Registry

控制处理

增加两个步骤就可以

这个呢

是第一步

第二步要在Foundry里面

对锁进行释放处理

解锁处理

好

那咱们将Ladies Lock Service

引入进来

Clarify

Ladies

Lock Service

AutoWire的注写

这个是分布式锁的实现内

回到刚才

更新账户资金余额的接口

第一步

咱们通过Ladies Lock Service

进行加锁的处理

Try Lock

这里面的参数

传递的是账户ID

然后下面是解锁处理

Ladies Lock Service

Unlock

Request Get Account ID

好

更新账户资金余额的接口

就已经加入了

分布式锁的控制处理

咱们回到讲义当中

这一讲咱们就完成了

资金服务对分布式锁的

集成配置和运用

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个分布式系统中“资金服务”如何集成使用 Redis 实现分布式锁的实战教学。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何封装一个 `RedisLockService` 组件，并将其配置到 Spring Boot 项目中，最终在 GPRC 服务的业务方法中调用该锁服务，以确保对账户余额的修改操作是线程安全的。整个过程涵盖了分布式锁的业务逻辑设计、代码封装、Spring 配置以及在业务代码中的实际应用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，讲师展示课程大纲，定位到“3.3 资金服务集成分布式锁”章节。
*   **00:05 - 00:15**: 讲解分布式锁的业务逻辑，强调锁的粒度应控制在“账户级别”，并根据账户 ID 进行加锁，确保同一时刻只有一个请求在处理。
*   **00:15 - 00:25**: 讲解锁的处理策略：如果无法立即拿到锁，应等待指定时间；如果等待后仍无法拿到锁，则封装异常并返回给客户端。
*   **00:25 - 00:35**: 展示 `stock-common-service` 工程中的 `RedisLockService` 类，讲解其 `tryLock` 方法的实现，该方法尝试加锁，失败则抛出 `ComponentException`。
*   **00:35 - 00:45**: 讲解 `RedisLockService` 的封装，包括初始化 `redisLockRegistry` 注入参数和 `waitTime`，以及对 `tryLock` 方法的封装。
*   **00:45 - 00:55**: 展示 `bulls-stock-finance` 项目中的 `RedisConfiguration` 类，讲解如何配置 `RedisLockRegistry`。
*   **00:55 - 01:05**: 讲解 `RedisLockRegistry` 的初始化，传入 `RedisConnectionFactory` 和锁的超时时间（24小时）。
*   **01:05 - 01:15**: 讲解如何在 `RedisConfiguration` 中通过 `@Bean` 注解创建并返回 `RedisLockService` 实例。
*   **01:15 - 01:25**: 展示 `GrpcStockFinanceService` 服务类，讲解其 `updateAccountBalance` 方法的业务逻辑。
*   **01:25 - 01:35**: 讲解在 `updateAccountBalance` 方法中如何调用 `redisLockService.tryLock(Object key)` 来获取分布式锁。
*   **01:35 - 01:45**: 讲解在获取锁后，调用 `stockFinanceService.updateBalance` 更新账户余额，并在 `finally` 块中释放锁（虽然视频未展示释放锁的代码，但这是标准做法）。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “3.3 资金服务集成分布式锁”。
    *   **子章节**: “3.3.1 资金服务的加锁处理逻辑”、“3.3.2 分布式锁组件进一步封装”、“3.3.3 资金服务集成分布式锁配置”。
    *   **核心概念**: 锁的粒度应控制在“账户级别”，根据账户 ID 进行加锁。
    *   **处理策略**: 如果无法立即拿到锁，应等待指定时间；如果等待后仍无法拿到锁，则封装异常并返回给客户端。

*   **代码关键内容**:

    *   **`RedisLockService` 类 (位于 `stock-common-service` 工程)**:
        ```java
        public RedisLockService(RedisLockRegistry redisLockRegistry, int waitTime) {
            this.redisLockRegistry = redisLockRegistry;
            this.waitTime = waitTime;
        }

        public boolean tryLock(Object key) throws ComponentException {
            try {
                Lock lock = redisLockRegistry.obtain(String.valueOf(key));
                boolean isLock = lock.tryLock(waitTime, TimeUnit.SECONDS);
                if (!isLock) {
                    throw new ComponentException(ApplicationErrorCodeEnum.WAITING_UNLOCK);
                }
                return isLock;
            }
        }
        ```

    *   **`RedisConfiguration` 类 (位于 `bulls-stock-finance` 工程)**:
        ```java
        @Bean
        public RedisLockService redisLockService(RedisLockRegistry redisLockRegistry) {
            return redisLockRegistry;
        }

        @Bean
        public RedisLockRegistry redisLockRegistry(RedisConnectionFactory redisConnectionFactory) {
            Duration expiration = Duration.ofSeconds(3600 * 24);
            return RedisLockRegistry
                .builder(redisConnectionFactory)
                .cacheDefaults(RedisCacheConfiguration.defaultCacheConfig().entryTtl(expiration))
                .build();
        }
        ```

    *   **`GlobalConstants` 类 (位于 `bulls-stock-common-utils` 工程)**:
        ```java
        GlobalConstants.DISTRIBUTE_LOCK_FOR_FINANCE, GlobalConstants.DISTRIBUTE_LOCK_KEY_EXPIRED
        ```

    *   **`GrpcStockFinanceService` 类 (位于 `bulls-stock-finance` 工程)**:
        ```java
        @Override
        public void updateAccountBalance(UpdateBalanceRequest request, StreamObserver<UpdateBalanceResponse> responseObserver) {
            // STEP1: 加入分布式锁的控制处理
            redisLockService.tryLock(request.getAccountID());
            long balance = stockFinanceService.updateBalance(request.getAccountID());
            response = UpdateBalanceResponse.newBuilder()
                .setStatus(GlobalConstants.STATUS_OK)
                .setBalance(balance)
                .build();
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：业务逻辑设计与封装**
    *   讲师首先在 PPT 上阐述了分布式锁的业务逻辑，即锁的粒度应控制在“账户级别”，并根据账户 ID 进行加锁。
    *   接着，讲师在 `stock-common-service` 工程中展示了 `RedisLockService` 类的代码，演示了如何封装 `tryLock` 方法，该方法尝试获取锁，失败则抛出异常。

*   **场景二：Spring 配置与注入**
    *   讲师切换到 `bulls-stock-finance` 项目，展示了 `RedisConfiguration` 类。
    *   讲师演示了如何通过 `@Bean` 注解创建 `RedisLockRegistry` 实例，并将其注入到 `RedisLockService` 中。
    *   讲师还演示了如何配置锁的超时时间（24小时）。

*   **场景三：业务方法集成**
    *   讲师展示了 `GrpcStockFinanceService` 服务类。
    *   讲师在 `updateAccountBalance` 方法中，演示了如何调用 `redisLockService.tryLock(request.getAccountID())` 来获取分布式锁。
    *   讲师强调，获取锁后，才能执行后续的业务操作（如更新账户余额）。

*   **场景四：开发环境操作**
    *   整个视频中，讲师都在 IntelliJ IDEA 开发环境中进行操作，展示了项目结构、代码编辑、配置文件修改和方法调用。
    *   讲师使用了代码高亮、光标定位和方法调用提示等功能，以清晰地展示代码逻辑。

---
