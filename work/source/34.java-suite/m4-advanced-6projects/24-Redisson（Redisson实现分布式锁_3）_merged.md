# 24-Redisson（Redisson实现分布式锁_3） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢,咱们是对于我们redition这种方式实现的分布式锁这个代码进行了一个测试,对吧

那么这个代码是没有问题的,是能够满足我们的要求的

那接下来呢,我们可以结合着原码,咱们来看一下

它这个框架,它到底是怎么实现分布式锁的主要的一个实现思路

那么我们可以从哪儿跟呢,就是这个lock方法

咱们前面也解释了,这个方法呢,就是用来尝试获取锁,对吧

如果获取不到呢,它就阻塞

那接下来呢,我们就来进入它的一个原码呢,来看一下

好,直接点进来,好,你看这个lock方法

然后在这里边呢,它是不是又调了这个方法

因为作为框架,它其实封装还是比较深的

然后呢,它就调用这个方法

然后呢,它在这儿是不是获得了一个什么呢

当前这个现成,它的ID,对吧,thread ID

然后呢,又调了这个方法

这个方法呢,其实就是干什么呢

尝试去获取锁

试试去获取锁

那么,我们怎么知道,就是这个方法

它的返回值,通过返回值怎么来判断它获得到了呢

这个地方呢,就看它是否为空

如果它等于空,你看它这个方法是不是就return了

return的话呢,相当于我们这个方法是不是就不阻塞

然后程序继续往下走

这是它获取锁了,对吧

那么如果没有获取锁,那就是这个TTL呢

这就说明什么呢,有其他的现成

有其他的现成

已经持有了这把锁

而这个TTL指的就是什么呢

指的就是那个现成所持有的那个锁

还有多长时间失效

它返回的这个值代表的是那个锁

还有多长时间失效

那就是说它没有获得锁,对吧

那么没有获得锁,它会做什么事呢

注意,你看,它会去订阅

它会去订阅一个消息

subcry吧,对吧

这个底层呢,其实是基于redis

它的一个发布订阅模式

发布订阅模式

其实就这个发布订阅呢

就类似于什么呢,mq

就是消息堆裂

为什么要订阅它呢,就是因为别人现在持有锁呢

而我现在是不是想获得锁

所以说呢,我要去订阅它

然后呢,你看,就是订阅这个现成的ID

对吧,因为刚才我们也看到了

它其实存起来的那个值呢

是跟其中有一部分是ID

也就是它去订阅

这个频道,然后呢,一旦那边

释放的时候呢,它这边就能收到通知

好,收到通知之后呢

它是不是就可以继续来干什么

继续来这个

尝试获取锁

所以你看,它在这个地方呢,是不是就有一个

well 循环,对吧

有个well 死循环,然后在这个地方呢

是不是去尝试,去尝试

然后呢,我们回到这边来

这个方法呢,其实就是来

真正去获取锁

如果返回值是空,表示获取到了

然后呢,我们可以点进去再来看

然后在这儿呢,它是不是就

掉了个get方法,get方法呢

这儿其实就是返回这个值,对吧

然后呢,在这里边它又掉了这个方法

重点看的是里边这个方法

好

好

好

好

点进来

然后在这里边呢,这个嵌套比较深啊

然后呢,它是不是又

调用了这个方法

这么一个方法

try lock

然后这个是一步的来获得锁的

这个当然也是尝试来获得,对吧

然后点进来

那么主要的代码其实就在这一块

主要的代码在这儿

那么它具体操作redis,刚才我们也看到了

它是不是去设置了一个值

那个值的类型是什么呢,是hc类型,对吧

它是怎么操作的呢

其实值形

就是这一段代码

但是这一段的话呢

你看if什么redis.call

调用什么exist

然后这个是动态的

其实类似于站位符,对吧

它其实就是传进了一个key

如果等于0,说明什么呢

说明我们指定的那个key不存在,对吧

因为它等于0嘛,也就是不存在

不存在的话呢,它就会执行下边这个

hset

是不是来设置值

然后设置完值之后呢,又调用了一个

pexpair,其实就是设置什么呢

设置这个key

它的这个有效期

指的就是我们那个失效时间,对吧

就是有效期

然后它如果已经存在了,对吧

它如果已经存在了呢

就执行这个,curve by,对吧

就是给它加1,然后呢

是不是又重新设置这个时间

然后呢,又设置,这个就返回什么呢

返回这个key还有多长时间失效

大概这个代码呢

我们其实是这个含义,对吧

大概读一下,但是你仔细看的话

好像它并不是真正的这个redis命令

对吧

那么这一段是什么呢

这一段其实叫做lua

它其实是一段脚本

而在我们这个redis2.6版本之后呢

它是支持这个

它提供了这么两个命令

它提供了这么两个命令

叫uvl,还有一个uvl,sha,对吧

那么通过这两个命令呢

我们就可以在redis当中来执行什么呢

lua脚本

所以说呢

我们这个原码当中啊

也就是我们redition这个框架

它底层是怎么操作的redis呢

它其实是基于lua这个脚本来操作的redis

所以一会儿呢

我们就重点来讲一下咱们这个lua脚本

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频课程聚焦于使用 **Redisson** 库在 Java 应用中实现 **分布式锁** 的技术细节。讲师通过一个“库存扣减”的业务场景，演示了如何在高并发环境下保证数据一致性。视频内容从应用层的控制器代码开始，逐步深入到 Redisson 库的底层源码，特别是其核心的 `tryLock` 和 `tryLockInterruptibly` 方法，最终揭示了其底层使用 **Lua 脚本** 来实现锁的原子性操作。整个过程旨在帮助开发者理解分布式锁的实现原理，而不仅仅是使用它。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的实际时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:30**: 课程引入与业务场景。讲师展示了一个简单的 Java Web 应用，其 `StockController` 中的 `stock()` 方法用于扣减库存。该方法直接从 Redis 中读取库存值并减一，但未加锁，存在并发问题。
*   **00:30 - 00:50**: 引入分布式锁解决方案。讲师在 `stock()` 方法中添加了 `redissonClient.getLock("mylock")`，并使用 `try` 块来尝试获取锁。
*   **00:50 - 01:20**: 展示应用层代码逻辑。讲师高亮了 `lock.lock(leaseTime: 5000, TimeUnit.MILLISECONDS)` 这行代码，解释了锁的获取和释放逻辑。
*   **01:20 - 01:50**: 进入 Redisson 源码分析。讲师切换到 `RedissonLock.java` 文件，开始分析 `lockInterruptibly` 方法。
*   **01:50 - 02:20**: 分析 `tryAcquire` 方法。讲师展示了 `tryAcquire` 方法的实现，其中包含了 `subscribe` 和 `syncSubscription` 等操作，用于监听锁的释放事件。
*   **02:20 - 02:50**: 深入 `tryLockInnerAsync` 方法。讲师展示了 `tryLockInnerAsync` 方法，该方法最终会调用 `evalWriteAsync` 来执行 Lua 脚本。
*   **02:50 - 03:20**: 重点讲解 Lua 脚本。讲师高亮并解释了 `tryLockInnerAsync` 方法中构建的 Lua 脚本，该脚本包含了 `hset`、`expire`、`hincrby` 等 Redis 命令，用于实现锁的原子性操作。
*   **03:20 - 03:50**: 总结与回顾。讲师回到 PPT，总结了 Redisson 实现分布式锁的核心思想：通过 Lua 脚本保证原子性，避免了传统锁的复杂性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “3.3 Lua脚本”。
    *   **3.3.1 Lua简介**: 描述了 Lua 是一种轻量级脚本语言，用于嵌入应用程序中。
    *   **3.3.2 Redis中使用Lua的好处**:
        *   减少网络开销。
        *   原子操作：Redis 会将整个脚本作为一个整体执行。
        *   复用：客户端发送的脚本会永久存在 Redis 中。

*   **代码关键内容**:

    *   **应用层代码 (`StockController.java`)**:
        ```java
        @GetMapping("/stock")
        public String stock() {
            RLock lock = redissonClient.getLock(name: "mylock");
            try {
                // 尝试获取锁，如果获取不到则阻塞，如果加锁成功则后续程序继续执行
                lock.lock(leaseTime: 5000, TimeUnit.MILLISECONDS);
                // 获取到了分布式锁
                int stock = Integer.parseInt(redisTemplate.opsForValue().get("stock"));
                if (stock > 0) {
                    stock--;
                    redisTemplate.opsForValue().set("stock", stock+"");
                    System.out.println("库存扣减成功，剩余库存：" + stock);
                } else {
                    System.out.println("库存不足！！！");
                }
            } catch (Exception ex) {
                System.out.println("争抢异常...");
            } finally {
                // 释放锁
                lock.unlock();
            }
            return "ok";
        }
        ```

    *   **Redisson 源码 (`RedissonLock.java`)**:
        ```java
        @Override
        public void lockInterruptibly() throws InterruptedException {
            lockInterruptibly(-1, null);
        }

        @Override
        public void lockInterruptibly(long leaseTime, TimeUnit unit) throws InterruptedException {
            long threadId = Thread.currentThread().getId();
            Long ttl = tryAcquire(leaseTime, unit, threadId);
            if (ttl == null) {
                return;
            }
            RFuture<RedissonLockEntry> future = subscribe(threadId);
            commandExecutor.syncSubscription(future);
            try {
                while (true) {
                    ttl = tryAcquire(leaseTime, unit, threadId);
                    if (ttl == null) {
                        break;
                    }
                }
            } finally {
                unsubscribe(future, threadId);
                get(lockAsync(leaseTime, unit));
            }
        }

        private Long tryAcquire(long leaseTime, TimeUnit unit, long threadId) {
            return get(tryAcquireAsync(leaseTime, unit, threadId));
        }

        private RFuture<Boolean> tryLockInnerAsync(long leaseTime, TimeUnit unit, final long threadId) {
            if (leaseTime != -1) {
                return tryLockInnerAsync(leaseTime, unit, threadId, RedisCommands.EVAL_NULL_BOOLEAN);
            }
            return tryLockInnerAsync(leaseTime, unit, threadId, RedisCommands.EVAL);
        }

        @Override
        public void operationComplete(Future<Boolean> future) throws Exception {
            if (!future.isSuccess()) {
                return;
            }
        }
        ```

    *   **Lua 脚本 (`tryLockInnerAsync` 方法中)**:
        ```lua
        if (redis.call('exists', KEYS[1]) == 0) then
            redis.call('hset', KEYS[1], ARGV[2], 1);
            redis.call('expire', KEYS[1], ARGV[1]);
            return nil;
        end;
        if (redis.call('hexists', KEYS[1], ARGV[2]) == 1) then
            redis.call('hincrby', KEYS[1], ARGV[2], 1);
            redis.call('expire', KEYS[1], ARGV[1]);
            return nil;
        end;
        return redis.call('pttl', KEYS[1]);
        ```

---

### 4) 关键场景与演示描述

*   **场景一：应用层演示 (00:00 - 00:50)**:
    *   讲师在 IntelliJ IDEA 中打开 `StockController.java` 文件。
    *   他高亮并解释了 `@GetMapping("/stock")` 注解和 `lock.lock(leaseTime: 5000, TimeUnit.MILLISECONDS)` 语句。
    *   他演示了在 `try` 块中获取锁、执行业务逻辑、在 `finally` 块中释放锁的完整流程。

*   **场景二：源码分析 (01:20 - 03:20)**:
    *   讲师切换到 `RedissonLock.java` 文件，开始分析 `lockInterruptibly` 方法。
    *   他逐步深入到 `tryAcquire` 方法，解释了 `subscribe` 和 `syncSubscription` 的作用。
    *   他重点讲解了 `tryLockInnerAsync` 方法，并展示了其内部调用的 `evalWriteAsync` 方法。
    *   最后，他高亮并逐行解释了 Lua 脚本，说明了其如何通过 `hset`、`expire`、`hincrby` 等命令实现锁的原子性操作。

*   **场景三：PPT 总结 (03:20 - 03:50)**:
    *   讲师切换到 PPT，总结了 Redisson 实现分布式锁的核心思想。
    *   他强调了 Lua 脚本在保证原子性、减少网络开销和复用方面的优势。
    *   他指出，通过这种方式，Redisson 能够在高并发环境下安全地实现分布式锁。
