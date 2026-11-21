# 07-分布式锁-总结 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们对本章内容做一个回顾和总结

首先咱们回顾下本章的学习目标

在这里咱们要掌握两点

第一点要正确使用分布式锁

掌握Spring Integration Ladies的使用

第二点我们要在资金服务里面去集成分布式锁

保障账户资金处理的正确性

那咱们来回顾一下本章所讲解的具体内容

首先咱们讲解介绍了Ladies分布式锁的正确用法

注意通过Ladies分布式锁的操作

咱们要确保它的原子性

这样才能保障分布式锁真正生效

接下来咱们讲解了分布式锁的实现方案

我们采用的是Spring Integration Ladies

去实现了分布式锁处理

之所以采用Spring Integration这个组件

因为它是出自Spring

而且从整体设计上可以支持

接入众多的存储组件

作为咱们分布式锁的实现方案

如果将来要做升级和替换

咱们只需要更改配置就可以

故需要再侵入原有的代码

接下来咱们对资金服务做了改造

让它能够支持和集成分布式锁

咱们要明白整体的枷锁处理逻辑

锁的力度是到什么级别

这里咱们的锁力度是控制在账户的级别上

根据账户ID进行枷锁

锁的力度一般根据业务的需要

在这里我们的锁力度是控制在账户的级别上

另外一个处理逻辑

在没有拿到锁的情况下面

我们该怎么去做

这里最好要给它一个超时时间

不能一直等待下去

这样会造成大量的现成开销

那在这里咱们对分布式组件做了进一步的封装

便于咱们服务的接入使用

然后再来看看我们的分布式锁

我们的分布式锁是什么样的

我们的分布式锁是一个

我们的分布式锁是一个

我们在资金服务里面集成了分布式锁的配置

整个集成实现也比较简单

接着我们就修改了额度调整的接口

加入了分布式锁的控制

整个实现只需要两步

第一步是枷锁的处理

第二个步骤就是对解锁的处理

这样就完成了分布式锁的控制

可以看到通过Split Integration Ladies的分布式锁方案

使用起来也是比较简单

咱们可以将更多的精力

侧重于业务逻辑的实现上

最后咱们对整体功能进行了测试和验证

这里需要对客户端进行改造

让它能够支持并发的调用处理

然后在测试过程当中

如果是出现了超时的异常

最好将分布式事务功能关闭掉

因为单机处理来讲性能有限

咱们在这里侧重的是分布式锁的运用

在对整个功能进行调用验证时

咱们只需要把整个功能进行调用验证时

咱们结合了两种场景

一种是不加锁的验证

另外一种就是加锁的验证处理

经过这两种场景的验证

咱们可以知道

如果是不加帐分布式锁

不能保证数据的一致性

会造成现成安全的问题

通过分布式加锁的处理

能够保障咱们资金服务

对资金处理的正确性

最后咱们再来总结一下

分布式锁的使用

要保障护士性以及

其他员工的原子性

不能出现错误的加锁方式

这个咱们在上面章节也做了讲解

通过SpringIntegrationLadies组件

能够帮助咱们快速实现分布式锁的功能

同时具有较强的扩展性

无论说你将来想扩展其他的存储组件

比如说GymFi

比如说JK数据库等等

通过该组件能够快速实现

不需要再去修改原有的代码

如果我们想要使用这个方式

如果大量接口都需要运用到分布式锁

大家可以考虑采用反射

或者进行拦截的方式

去做对应的处理

以注解的形式做进一步的封装

如果在项目当中

较少的接口去做使用

可以直接通过咱们封装的接口

进行相应的操作

能够减少一些不必要的开销

这个就要结合项目当中具体的场景

做不同程度的封装使用

好,这一讲就是对本章内容的回顾与总结

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对技术课程内容进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程主要讲解了在微服务架构下，如何使用分布式锁来解决高并发场景下的“超卖”问题，特别是针对“资金服务”的余额更新操作。课程内容分为两大部分：

*   **第一部分：分布式锁的实现与集成**
    *   **核心内容**：详细对比了两种分布式锁的实现方案：**Redis 原生实现**（强调其原子性）和 **Spring Integration Redis**（强调其高扩展性）。
    *   **实践应用**：将分布式锁集成到“资金服务”中，通过封装 `RedisLockService` 组件，为 `updateAccountBalance` 接口添加锁，确保同一时刻只有一个线程能更新某个账户的余额。
    *   **测试验证**：通过模拟并发下单，验证了加锁后的正确性。在不加锁的情况下，系统会出现“Global lock wait timeout”异常，导致事务阻塞；而加锁后，最终余额正确，验证了方案的有效性。

*   **第二部分：用户预警通知**
    *   **核心内容**：课程的后半部分开始介绍“用户预警通知”的设置与生成功能，目标是实现“止盈止损”和“账户预警”的模板设置功能。这部分内容在视频中仅做了简要介绍，未深入展开。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的实际时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:15**：课程开场，介绍本章目标：分布式锁集成运用。
*   **00:16 - 00:35**：**3.1 Redis分布式锁正确用法**。讲解Redis原生锁的实现方式，展示正确的 `jedis.set(lockkey, clientId, "NX", "PX", expireTime)` 代码，并对比错误的两步操作方式。
*   **00:36 - 01:00**：**3.2 分布式锁方案 (Spring Integration Redis)**。介绍Spring Integration Redis方案的优势，展示其使用方法 `lock.tryLock(5, TimeUnit.SECONDS)`。
*   **01:01 - 01:30**：**3.3 资金服务集成分布式锁**。
    *   **3.3.1 资金服务的加锁处理逻辑**：讲解锁的粒度（账户级）和超时等待策略。
    *   **3.3.2 分布式锁组件进一步封装**：展示 `RedisLockService` 的代码实现，包括初始化和 `tryLock` 方法。
    *   **3.3.3 资金服务集成分布式锁配置**：（画面中未展示具体配置，但提到了需要修改配置文件）。
    *   **3.3.4 额度调整接口加入分布式锁**：展示如何在 `updateAccountBalance` 方法中使用 `RedisLockService`。
*   **01:31 - 02:00**：**3.4 功能测试验证**。展示测试代码 `NettyClientTest`，模拟并发下单。讲解测试环境的配置（关闭SEATA分布式事务）。
*   **02:01 - 02:30**：**4. 总结**。总结分布式锁的核心要点：互斥性、原子性、扩展性，并给出使用建议。
*   **02:31 - 02:45**：**第2章 用户预警通知的设置与生成**。介绍本章目标：实现止盈止损和账户预警模板设置功能。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文本内容**：
    *   **章节标题**：`第1章 分布式锁集成运用`，`3.1 Redis分布式锁正确用法`，`3.2 分布式锁方案 (Spring Integration Redis)`，`3.3 资金服务集成分布式锁`，`3.4 功能测试验证`，`4. 总结`，`第2章 用户预警通知的设置与生成`。
    *   **关键概念**：互斥性、原子性、锁粒度（账户级）、超时等待、事务阻塞、SEATA分布式事务。
    *   **FAQ**：当服务调用超时，会提示 `Global transaction[192.168.19.1:8091:2020713605] is timeout and will be rolled back.`

*   **代码关键内容**：

    *   **Redis 原生锁（正确方式）**：
        ```java
        String result = jedis.set(lockkey, clientId, "NX", "PX", expireTime);
        if ("OK".equals(result)) {
            return true;
        }
        ```

    *   **Redis 原生锁（错误方式）**：
        ```java
        Long result = jedis.setnx(lockkey, clientId);
        if (result == 1) {
            // 如果程序崩溃，无法设置过期时间，资源将一直无法释放
            jedis.expire(lockkey, expireTime);
        }
        ```

    *   **Spring Integration Redis 锁（使用方法）**：
        ```java
        // 根据账户ID进行加锁
        Lock lock = redisLockRegistry.obtain("accountId");
        boolean isLock = lock.tryLock(5, TimeUnit.SECONDS);
        // 处理业务逻辑
        ...
        // 解锁
        lock.unlock();
        ```

    *   **`RedisLockService` 封装类**：
        ```java
        public RedisLockService(RedisLockRegistry redisLockRegistry, int waitTime) {
            this.redisLockRegistry = redisLockRegistry;
            this.waitTime = waitTime;
        }

        public boolean tryLock(Object key) throws ComponentException {
            try {
                Lock lock = redisLockRegistry.obtain(String.valueOf(key));
                // ... 业务逻辑 ...
                return true;
            } catch (Exception e) {
                // ... 异常处理 ...
            }
        }
        ```

    *   **`updateAccountBalance` 方法（集成锁）**：
        ```java
        public void updateAccountBalance(UpdateBalanceRequest request, StreamObserver<UpdateBalanceResponse> responseObserver) {
            try {
                // STEP1: 分布式锁
                redisLockService.tryLock(request.getAccountId());
                // 更新账户资金
                long balance = ...;
                // ... 业务逻辑 ...
            } catch (ComponentException e) {
                // 业务异常返回
                log_error(e.getMessage(), e);
                response = UpdateBalanceResponse.newBuilder().setStatus(e.getErrorCodeEnum().getCode()).setMessage(e.getErrorCodeEnum().getMessage()).build();
            } catch (Exception e) {
                // 系统异常返回
                log_error(e.getMessage(), e);
                response = UpdateBalanceResponse.newBuilder().setStatus(GlobalConstants.STATUS_ERROR).setMessage(e.getMessage()).build();
            } finally {
                // STEP2: 解锁处理
                redisLockService.unlock(request.getAccountId());
            }
            responseObserver.onNext(response);
        }
        ```

    *   **测试代码 `NettyClientTest`**：
        ```java
        public static void main(String[] args) throws Exception {
            int clientNums = 10;
            for(int i=0; i<clientNums; i++) {
                new Thread(() -> {
                    try {
                        ClientBoundHandler client = startClient();
                        // 用户登录
                        client.getBusinessHandler().userLogin();
                        Thread.sleep(3000L);
                        // 模拟发送十次下单请求
                        for(int j=0; j<10; j++) {
                            client.getBusinessHandler().placeOrder();
                        }
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }).start();
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：Redis 原生锁的正确与错误对比**
    *   **演示**：讲师在屏幕上展示正确的 `jedis.set(...)` 代码，并解释其原子性。随后，展示错误的 `setnx` + `expire` 两步操作，并指出其在程序崩溃时会导致锁无法释放的问题。
    *   **目的**：强调分布式锁实现中“原子性”的重要性，避免死锁和资源泄露。

*   **场景二：Spring Integration Redis 锁的集成**
    *   **演示**：讲师展示如何通过 `redisLockRegistry.obtain("accountId")` 获取锁，并使用 `tryLock` 方法进行尝试加锁。随后，展示如何在业务逻辑前后调用 `unlock()` 方法。
    *   **目的**：说明Spring Integration Redis方案的易用性和扩展性，为后续的业务集成做铺垫。

*   **场景三：资金服务加锁逻辑的实现**
    *   **演示**：讲师在 `RedisLockService` 类中展示 `tryLock` 方法的实现，包括异常处理和最终的解锁操作。然后，在 `updateAccountBalance` 方法中，将 `tryLock` 调用插入到业务逻辑之前，并在 `finally` 块中调用 `unlock`。
    *
