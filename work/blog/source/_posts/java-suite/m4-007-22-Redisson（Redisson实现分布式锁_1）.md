---
title: "Redisson 实现分布式锁与 Lua 脚本在 Redis 中的应用（eval 原子性）"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 品达物流TMS]
tags: [Java, 项目实战, 分布式锁]
---

# Redisson 实现分布式锁与 Lua 脚本在 Redis 中的应用（eval 原子性）

上一篇自研的 Redis 锁留了两个尾巴：非阻塞、无续命。这一篇进入品达物流 TMS 第九章的后半段，直接换成企业里的事实标准 Redisson，从接入、压测到源码走一遍，顺藤摸瓜会发现它的底层是靠 Lua 脚本操作 Redis 的——于是再把 Lua 的三大好处和 EVAL/EVALSHA 用法补齐。第九章最后一块"导入功能代码"也在此一并交代定位。

## 先给结论

- Redisson 的接入成本极低：引一个依赖、写一个配置类创建 `RedissonClient`，业务代码只要三句——`getLock()` 拿锁对象、`lock()` 抢锁、`unlock()` 释放。
- `getLock("mylock")` 只是获得锁对象，并不抢锁；真正抢锁的 `lock(5000, TimeUnit.MILLISECONDS)` 是阻塞方法，抢不到会一直等，第二个参数指的是锁的失效时间（租约），不是阻塞时长——这是课程里纠正过的一个易错点。
- 双实例（8001/8002）+ JMeter 压测，库存扣减 50、49、48……一路递减无重复，超卖问题消失。
- 锁在 Redis 里的真身是一个 hash 类型的 key：field 是「UUID:线程ID」，带 TTL 倒计时，到期自动消失，底层仍是 SET 值那一套。
- 源码走读揭示两件事：没抢到锁的线程通过 Redis 发布订阅（类似 MQ）等释放通知，避免盲目轮询；抢锁动作本身是一段 Lua 脚本，靠 exists/hset/hincrby/pttl 一次执行完成，天然支持可重入。
- Lua 脚本三大好处：减少网络开销、原子操作（整个脚本作为整体执行，不会被其他命令插入）、脚本可在 Redis 服务端缓存复用（SCRIPT LOAD + EVALSHA）。

## 三行代码接入 Redisson 分布式锁

使用 Redisson 首先在 pom 中引入坐标（演示环境加载的是 3.10.1 版本）。接着写一个配置类，负责创建 `RedissonClient`。它底层基于 Redis 实现分布式锁，所以必须指定 Redis 地址和密码；地址不写死，用 `@Value` 把配置文件里 `spring.redis.host/port/password` 读进来：

```java
@Configuration
public class RedissonConfig {

    @Value("${spring.redis.host}")
    private String host;

    @Value("${spring.redis.port}")
    private String port;

    @Value("${spring.redis.password}")
    private String password;

    @Bean
    public RedissonClient redissonClient() {
        Config config = new Config();
        config.useSingleServer()
              .setAddress("redis://" + host + ":" + port)
              .setPassword(password);
        RedissonClient client = Redisson.create(config);
        return client;
    }
}
```

有了 Bean，Controller 里 `@Autowired` 注入即可用。对比上一篇自研版本，业务代码精简成三句：

```java
@Autowired
private RedissonClient redissonClient;

@GetMapping("/stock")
public String stock() {
    // 获得锁对象，并不是去抢锁
    RLock lock = redissonClient.getLock("mylock");
    try {
        // 尝试获取锁，获取不到则阻塞；加锁成功则继续往下执行
        lock.lock(5000, TimeUnit.MILLISECONDS);
        // 拿到了分布式锁，执行库存扣减
        int stock = Integer.parseInt(redisTemplate.opsForValue().get("stock"));
        if (stock > 0) {
            stock--;
            redisTemplate.opsForValue().set("stock", stock + "");
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
    return "OK";
}
```

三个要点：

| 步骤 | 方法 | 说明 |
| :--- | :--- | :--- |
| 拿锁对象 | `getLock("mylock")` | 名字可任意指定，这一步不发生争抢 |
| 抢锁 | `lock(5000, TimeUnit.MILLISECONDS)` | 阻塞方法；抢不到就一直等，期间别的线程释放了锁还能继续抢；5000 是这把锁的**失效时间** |
| 释放 | `unlock()` | 放在 finally 里，保证异常情况下锁也能释放，避免死锁 |

这里有个必须纠正的点：初看容易把 5000 毫秒理解成"最多阻塞 5 秒"，实际上它指的是锁自身的失效时间。自研版本里需要自己 `setIfAbsent` 带过期时间，Redisson 把这件事做进了 `lock()` 的参数里。

## 双实例压测与 Redis 中的锁长什么样

框架封装得好不好，压测说话。把端口改成 8001 启动第一个实例，再改成 8002 启动第二个，Redis 里的库存恢复成 50，然后用 JMeter 并发打 `/stock` 接口。控制台输出依次是 49、48、47、46、45、44、43——数字严格递减、没有重复，说明两个 JVM 实例之间确实互斥了，超卖没有出现。

更值得看的是锁在 Redis 里的真实形态。把失效时间改成 50000 毫秒，以 debug 方式启动（时间够长才来得及观察），浏览器请求一次后打开 Redis Desktop Manager：多出一个名为 `mylock` 的 key——名字正是 `getLock()` 传入的那个。它不是简单的 string，而是 **hash 类型**：

- hash 的 field 是一长串「UUID + 冒号 + 40」，后半段数字就是持有锁线程的 threadId，前半段用于区分不同客户端实例；
- 这个 key 带 TTL，一路倒计时（如从 32 秒往下走），到 0 之后刷新客户端，key 直接消失。

也就是说，Redisson 底层依然是向 Redis 设置值，只是结构比自研版的一个 string 复杂得多——hash 结构正是它支持可重入计数的基础。

## 源码走读：订阅通知 + while 重试 + 一段 Lua

从 `lock()` 进入 `RedissonLock` 源码，主干逻辑在 `lockInterruptibly(long leaseTime, TimeUnit unit)` 里：

```java
public void lockInterruptibly(long leaseTime, TimeUnit unit) throws InterruptedException {
    long threadId = Thread.currentThread().getId();
    Long ttl = tryAcquire(leaseTime, unit, threadId);
    if (ttl == null) {
        return;  // 返回 null 说明抢到了锁，方法不阻塞，程序继续
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
    }
}
```

两个关键设计：

1. **tryAcquire 的返回值语义**：返回 null 表示抢到锁；返回非 null 的 ttl 表示锁被其他线程持有，这个值就是对方那把锁还剩多长时间失效。
2. **订阅而非空转**：没抢到的线程先通过 `subscribe(threadId)` 订阅一个频道——底层是 Redis 的发布订阅模式，作用类似 MQ。持锁线程释放锁时会发通知，等待方收到消息后进入 while 循环再次尝试，避免了纯轮询浪费。

而真正去 Redis 抢锁的代码藏在 `tryLockInnerAsync` 里，核心就是这段 Lua 脚本：

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

三段逻辑对应三种情况：

| 分支 | 条件 | 动作 |
| :--- | :--- | :--- |
| 首次加锁 | key 不存在（exists == 0） | hset 写入「UUID:线程ID → 1」，expire 设置失效时间，返回 nil |
| 可重入 | hash 中已存在本线程的 field（hexists == 1） | hincrby 计数加 1 并重设失效时间——重入次数 +1 |
| 抢锁失败 | 锁被其他线程持有 | 返回 pttl，即剩余失效时间，也就是外层拿到的那个 ttl |

细看这段"脚本"，它并不是一条条独立的 Redis 命令，而是 Lua。Redis 从 2.6 版本起提供 `EVAL` 和 `EVALSHA` 两个命令，可以在服务端执行 Lua 脚本——Redisson 框架操作 Redis 的底层，正是基于 Lua 脚本实现的。要理解这个框架，就得先理解 Lua。

## Lua 脚本：三大好处与 EVAL 用法

Lua 是一种轻量小巧的脚本语言，用标准 C 语言编写、以源代码形式开放，设计目的就是嵌入应用程序中提供灵活的扩展和定制能力，很多产品都在用，Redis 也在 2.6 之后加入了对它的支持。

**为什么在 Redis 里用 Lua？** 三个好处，对照自研代码的痛点看非常直观：

| 好处 | 含义 | 对应痛点 |
| :--- | :--- | :--- |
| 减少网络开销 | 多个命令打包进一个脚本，一次发送、服务端一次执行完 | 不用 Lua 时，exists/hset/expire 每个命令都要单独与 Redis 服务通信，三个命令就是三次网络往返 |
| 原子操作 | Redis 将整个脚本作为一个整体执行，中间不会被其他命令插入 | 不会出现执行完一句就被别的请求插队的情况，编写脚本无需担心竞态条件，也不用再套事务 |
| 复用 | 发送的脚本可以永久存储在 Redis 中，其他客户端复用时直接加载 | 相同逻辑不必每次重复发送完整代码 |

**EVAL 命令**是三者中用得最多的，语法为：

```sql
EVAL script numkeys key [key ...] arg [arg ...]
```

- `script`：Lua 脚本本体；脚本里通过内置的 `redis.call()` 调用 Redis 命令；
- `numkeys`：后面有几个 key，按顺序排在前面的参数算 key，其余算 ARGV；
- 脚本内用 `KEYS[1]`、`KEYS[2]` 取第几个 key，用 `ARGV[1]`、`ARGV[2]` 取其余参数，这些占位写法是固定的。

在 Redis 客户端里几个递进的例子：

```sql
-- 设置 key：KEYS[1]=city，ARGV[1]=beijing
eval "return redis.call('set', KEYS[1], ARGV[1])" 1 city beijing

-- key 和 value 都写死在脚本里，没有 key 时 numkeys 必须写 0
eval "return redis.call('set', 'name', 'xiaoming')" 0

-- 删除：返回 1 表示删除成功
eval "return redis.call('del', KEYS[1])" 1 city

-- 读取：返回 xiaoming
eval "return redis.call('get', KEYS[1])" 1 name

-- 带条件判断：citys 不存在时，设置 city=beijing 且 5000 毫秒后过期，返回 nil
eval "if (redis.call('exists', KEYS[1]) == 0) then redis.call('set', KEYS[2], ARGV[1]); redis.call('expire', KEYS[2], ARGV[2]); return nil; end;" 2 citys city beijing 5000
```

最后一个例子里有 2 个 key（citys、city）和 2 个 ARGV（beijing、5000），执行后 `city` 出现且值为 beijing。日常使用 Lua 时脚本里往往串起多条命令，一次全部执行完——Redisson 那段加锁脚本就是典型。

一个易错细节：即使脚本里没有 key，`numkeys` 这个数字也必须写（写 0），漏掉会直接报 `wrong number of arguments for 'eval' command`。

**脚本缓存**：每次 EVAL 都把完整脚本发给服务端，本身也是网络开销，所以 Redis 提供了缓存机制。`SCRIPT LOAD` 把脚本缓存到服务端，返回一个唯一的 SHA1 编号；之后用 `EVALSHA` 凭编号执行：

```sql
script load "return redis.call('get', KEYS[1]);"
-- 返回编号：0e11c9f252fd7611c38403ce6095872b8c70580

evalsha 0e11c9f252fd7611c38403ce6095872b8c70580 1 name
-- 返回 xiaoming
```

`EVALSHA` 后面同样要跟 numkeys、key 和 arg，Redis 按编号找到缓存的脚本执行即可，完整脚本只需传输一次。

## 附：第九章收尾——导入 pd-web-manager 功能代码

第九章的最后一块内容是"导入功能代码"，与 Redisson/Lua 主题关联不大，属于 TMS 客户端工程化收尾，这里简单交代定位。TMS 分四个端：后台管理端、快递员端、司机端、用户端，都经网关与应用层交互；应用层 `pd-web-manager`（本章要完成的部分）、`pd-web-courier`、`pd-web-driver` 等再通过 Feign 远程调用服务层微服务（pd-oms、pd-base、pd-user、pd-work 等）。这套代码没有新的技术点，直接导入使用即可，值得留意的结构特征是：应用层不直接操作数据库，配置里没有 datasource，也没有 Mapper，全部数据操作都封装成 Feign 接口交给微服务完成；Controller 数量众多（组织管理、员工分页查询、保存机构作业范围等），并配好了 Swagger 方便自测接口。

## 小结

这一篇把分布式锁从"自己写"推进到"用框架"：Redisson 用三行业务代码替代了自研版的判断与删除逻辑，失效时间内建在 `lock()` 参数里；源码层面，等待锁靠发布订阅 + while 重试，抢锁靠一段 Lua 脚本整体执行，hash 结构撑起可重入计数。理解了 Redisson 对 Lua 的依赖，也就理解了 Lua 在 Redis 中的三大价值——省网络、保原子、可复用，以及 EVAL/EVALSHA 的基本用法。至此，品达物流 TMS 第九章的后台管理端内容全部完成。
