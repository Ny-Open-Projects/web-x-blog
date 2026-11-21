# 06-分布式锁-解决超卖现象 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

前面那一块我们已经强调过

在我们秒杀这里是存在一个超卖现象的

那么我们可以对这个超卖现象这里进行一个处理

这里怎么处理呢

我们就使用分布式锁来实现一下就可以了

做这么一个事情

在这里我就去获取一个key的锁

获取一个key的锁之后呢

紧接着让这个中间流程全部执行完了

再释放这个锁

这样就可以保障一个用户在执行这个操作的时候

其他的用户不能执行

这样子就不会存在一个超卖现象了

数据判断就会是很精准的了

好我们来实现一下

那这里我们首先注入下我们的reddition对象

注入之后呢

我们接着开始去实现这个锁的控制

那锁的控制我们从这里开始

从这里开始

不过我要先给它一个锁

给它一个锁呢

我写一下

lock key

这个key呢

我就是只针对当前这个商品的

好lock key

这里开始进行锁定

我们选

我们选这个吧

好我们接着看

还缺一个超时时间

无法解锁的时候

最终锁这一块会释放的

我们选择分钟

这里是获取锁

那如果获取锁了之后

我们就选择分钟

我们才会执行这些操作

好我们开始写一个判断

B O

才会执行下面这些操作

获取到的锁

最终不要忘记了释放锁

点unlock

可以了

这块就搞定了

那么用户下次来请求操作的时候呢

这里就不会说有多个人进入这个环节了

这里只会有一个人能参与进来

但是注意哈

这里的我写的这个锁定的key是什么key呢

注意不要去锁这个商品的key

很多人会选择这个key

不要锁它

因为你下面要操作它的

你锁谁呢

你锁一个当前商品对应的锁定的key

所以我这里写了个lock

那么所有用户抢购

只要是抢购该商品的所有用户

只能一个一个一个一个一个来操作

而不能说多个人一起来操作

那样子就会乱套了

好

这是我们这一块解决这个秒杀这一块超卖现象

主要是用的是分布之锁

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段聚焦于一个高并发电商系统中“秒杀”订单的分布式锁实现。讲师通过在 `OrderServiceImpl` 类中编写代码，演示了如何利用 Redisson 库来实现一个可重入、带超时的分布式锁，以确保同一商品在高并发场景下只能被一个用户成功下单。核心逻辑包括：首先尝试获取锁，如果获取失败则直接返回；如果成功获取锁，则检查商品库存，库存不足则释放锁并返回；库存充足则创建订单、扣减库存，并将用户信息和订单信息写入 Redis，最后释放锁。整个过程旨在解决分布式环境下的“超卖”问题。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 展示 `OrderServiceImpl` 类中 `hotAdd` 方法的初始代码，用于处理秒杀下单逻辑。
*   **00:04 - 00:07**: 讲师在 `hotAdd` 方法中添加了 Redis 分布式锁的逻辑，使用 `redissonDistributedLocker.tryLock(lockkey, timeout, leaseTime, unit)` 方法。
*   **00:08 - 00:11**: 讲师在 `tryLock` 方法中设置锁的超时时间和租约时间，例如 `timeout: 10, leaseTime: 10, unit: MINUTES`。
*   **00:12 - 00:15**: 讲师在 `hotAdd` 方法中添加了 `if (redisTemplate.hasKey(key))` 条件，用于检查商品库存。
*   **00:16 - 00:19**: 讲师在 `hotAdd` 方法中添加了 `Integer num = Integer.parseInt(redisTemplate.boundHashOps(key).get("num").toString());` 用于获取库存数量。
*   **00:20 - 00:23**: 讲师在 `hotAdd` 方法中添加了 `if (num <= 0) { return; }` 条件，用于判断库存是否为零。
*   **00:24 - 00:27**: 讲师在 `hotAdd` 方法中添加了 `Result<Sku> skuResult = skuFeign.findById(id);` 用于获取商品信息。
*   **00:28 - 00:31**: 讲师在 `hotAdd` 方法中添加了 `Sku sku = skuResult.getData();` 用于获取商品对象。
*   **00:32 - 00:35**: 讲师在 `hotAdd` 方法中添加了 `Order order = new Order();` 用于创建订单对象。
*   **00:36 - 00:39**: 讲师在 `hotAdd` 方法中添加了 `order.setTotalNum(1);` 用于设置订单数量。
*   **00:40 - 00:43**: 讲师在 `hotAdd` 方法中添加了 `order.setCreateTime(new Date());` 用于设置订单创建时间。
*   **00:44 - 00:47**: 讲师在 `hotAdd` 方法中添加了 `order.setUpdateTime(order.getCreateTime());` 用于设置订单更新时间。
*   **00:48 - 00:51**: 讲师在 `hotAdd` 方法中添加了 `order.setOrderId("No" + idWorker.nextId());` 用于设置订单ID。
*   **00:52 - 00:55**: 讲师在 `hotAdd` 方法中添加了 `order.setOrderStatus("0");` 用于设置订单状态。
*   **00:56 - 00:59**: 讲师在 `hotAdd` 方法中添加了 `order.setPayStatus("0");` 用于设置支付状态。
*   **01:00 - 01:03**: 讲师在 `hotAdd` 方法中添加了 `order.setConsignStatus("0");` 用于设置发货状态。
*   **01:04 - 01:07**: 讲师在 `hotAdd` 方法中添加了 `order.setSkuId(id);` 用于设置商品ID。
*   **01:08 - 01:11**: 讲师在 `hotAdd` 方法中添加了 `order.setName(sku.getName());` 用于设置商品名称。
*   **01:12 - 01:15**: 讲师在 `hotAdd` 方法中添加了 `order.setPrice(sku.getSeckillPrice() * order.getTotalNum());` 用于设置商品价格。
*   **01:16 - 01:19**: 讲师在 `hotAdd` 方法中添加了 `orderMapper.insertSelective(order);` 用于将订单插入数据库。
*   **01:20 - 01:23**: 讲师在 `hotAdd` 方法中添加了 `redisTemplate.boundValueOps(userKey).set("1");` 用于记录用户已下单。
*   **01:24 - 01:27**: 讲师在 `hotAdd` 方法中添加了 `redisTemplate.boundValueOps(userKey).expire(timeout, unit);` 用于设置用户下单记录的过期时间。
*   **01:28 - 01:31**: 讲师在 `hotAdd` 方法中添加了 `redissonDistributedLocker.unlock(lockkey);` 用于释放锁。
*   **01:32 - 01:35**: 讲师在 `hotAdd` 方法中添加了 `return StatusCode.ORDER_OK;` 用于返回成功状态码。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码片段 1 (核心逻辑)**:
    ```java
    public void hotAdd(Map<String, String> orderMap) {
        String username = orderMap.get("username");
        String id = orderMap.get("id");

        // Redis中对应的key
        String key = "SKU_" + id;
        String lockkey = "LOCKSku_" + id;
        String userKey = "USER_" + username + "_ID" + id;

        // 如果key在redis缓存, 则表示商品信息在Redis中进行操作
        boolean bo = redissonDistributedLocker.tryLock(lockkey, timeout, leaseTime, unit);
        if (bo) {
            // 获取商品数量
            Integer num = Integer.parseInt(redisTemplate.boundHashOps(key).get("num").toString());
            if (num <= 0) {
                return;
            }
            Result<Sku> skuResult = skuFeign.findById(id);
            Sku sku = skuResult.getData();

            // 1. 创建Order
            Order order = new Order();
            order.setTotalNum(1);
            order.setCreateTime(new Date());
            order.setUpdateTime(order.getCreateTime());
            order.setOrderId("No" + idWorker.nextId());
            order.setOrderStatus("0");
            order.setPayStatus("0");
            order.setConsignStatus("0");
            order.setSkuId(id);
            order.setName(sku.getName());
            order.setPrice(sku.getSeckillPrice() * order.getTotalNum());
            orderMapper.insertSelective(order);

            // 2. 记录当前用户抢单的时间点, 24小时内不能抢购该商品
            redisTemplate.boundValueOps(userKey).set("1");
            redisTemplate.boundValueOps(userKey).expire(timeout, unit);

            // 3. 释放锁
            redissonDistributedLocker.unlock(lockkey);

            return StatusCode.ORDER_OK;
        }
    }
    ```

*   **代码片段 2 (Redisson 锁方法)**:
    ```java
    public boolean tryLock(String lockkey, long timeout, long leaseTime, TimeUnit unit) {
        // 实现逻辑
    }

    public void unlock(String lockkey) {
        RLock lock = redissonClient.getLock(lockkey);
        lock.unlock();
    }
    ```

*   **代码片段 3 (Redis 操作)**:
    ```java
    // 获取商品数量
    Integer num = Integer.parseInt(redisTemplate.boundHashOps(key).get("num").toString());

    // 记录用户抢单信息
    redisTemplate.boundValueOps(userKey).set("1");
    redisTemplate.boundValueOps(userKey).expire(timeout, unit);
    ```

---

### 4) 关键场景与演示描述

*   **场景 1**: 讲师在 `OrderServiceImpl` 类中编写 `hotAdd` 方法，用于处理秒杀下单。
*   **场景 2**: 讲师在 `hotAdd` 方法中添加了 `redissonDistributedLocker.tryLock(lockkey, timeout, leaseTime, unit)` 方法，用于获取分布式锁。
*   **场景 3**: 讲师在 `hotAdd` 方法中添加了 `if (redisTemplate.hasKey(key))` 条件，用于检查商品库存。
*   **场景 4**: 讲师在 `hotAdd` 方法中添加了 `Integer num = Integer.parseInt(redis
