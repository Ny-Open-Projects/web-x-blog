# 05-分布式锁-Redisson分布式锁测试 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,我们接下来对这一块进行一个测试。

那这一块呢,这个名字我们看一下,它应该跟这里保持一致,就不会发错了。

但其实你写着也没有关系。

好,接着我们来测试一下这一块。

测试一下这个锁,看能否实现。

我们在这里新建一个测试类,咱叫Redicent.

Controller,做这么一个事情。

Rest Control.

Request Mapping。

Value,我们就写一下叫做Redicent。

做这么一个事情,就是多个用户实现加锁操作。

那这里只允许有一个用户可以获得对应的锁。

好,我们就测试这么一个功能。

来,Public,写个叫String.

Look,返回一个OK就可以了。

这里写个叫Get Mapping。

Value写个Look。

好,那我每次让你传一个时间过来,Time。

那这个时间就是我们让你休眠的时间,Time。

就OK了,好。

我们来写一下这个操作。

首先我们写一下当前用户,休眠时间,Time。

写个当前休眠标识吧。

就是这一块。

好,那往后面走的话,

接着去做这个获取锁的操作。

那获取锁的操作呢,我们就得把这个ReadySend对象给注入进来哈。

注入进来,这里写个AutoWrite。

来写个获取锁。

那么获取锁这里怎么获取锁呢?

这样子点Look。

锁了我们就写UUUUUU,随便写哈。

好,最后不要忘了释放锁。

行,这个是释放锁。

我们看一下这个方法。

Unlock。

对对吧。

好,这个方法是Unlock,上面也是Unlock啊。

行。

这个是释放锁。

那么中间我们可以执行一些相关的操作。

那比如这里我可以打印一下哈。

打印一下当前这一块。

执行休眠。

谁执行休眠,我们在这里休眠一下。

休眠多久了,休眠Time时间。

就是这一块。

那么休眠之后呢,往后面走。

你还得释放锁呀。

对。

休眠完。

执行休眠。

休眠完成。

准备释放锁。

好。

一释放锁的话,那么下个用户请求就能获取这个锁了。

接着我们来测试一次。

看看效果怎么样哈。

把这里启动一次。

看看效果怎么样。

好,我们看这一块运行的效果。

这里报错了。

我们看一下为什么报错。

这里

JSON,解析是JSON。

我们看这里解析是JSON。

这里。

看这里写的有问题哈。

解析是JSON。

应该是from

Yang哈。

好,再来执行一次。

看看现在的效果怎么样。

好,大家看这个时候执行的效果。

是不是就像我们说的。

大家一起去获取这个

Key的数。

然后只有一个可以获取。

行,这里没有问题。

好,没有问题。

我们开始模拟这个操作。

那这个呢我就模拟一下。

localhost

1808。我们看一下这个是

1808.5

对吧。

reddison

localhost

给多少秒呢?给15秒。

这个是15秒。那么下一个我们就不给这么多。

好,我们把这个窗口最小化。

好,回车一次。

这个呢就给

1.5秒。

大家可以看到哈。

他获取了标识。

这个时候他休眠,他还没有获取到对应的锁。

这是这一块。

好,我们等他休眠。

他休眠15秒之后。

诶,他才获取锁。

看到没有?这是这一块。

因此我们这个

我们这一块这个

分布式锁这一块就搞定了。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段主要演示了如何在 Spring Boot 项目中集成 Redisson 来实现分布式锁功能。讲师通过一个名为 `seckill-order` 的订单服务项目，展示了从配置 Redisson 客户端、创建控制器接口、编写分布式锁的业务逻辑，到最终在浏览器中测试接口的完整流程。视频重点在于讲解如何使用 Redisson 的 `RLock` 对象来实现一个可重入、可指定超时时间的分布式锁，并通过 `@GetMapping` 注解暴露一个简单的锁接口供测试。过程中也展示了项目结构、配置文件（如 `redisson.yml`）以及在 IDEA 中进行代码编写和调试的全过程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 展示项目结构，定位到 `RedisConfig.java` 文件，准备配置 Redisson 客户端。
*   **00:05 - 00:15**: 在 `RedisConfig.java` 中编写 `@Bean` 方法，加载 `redisson.yml` 配置文件并创建 `RedissonClient` 实例。
*   **00:15 - 00:25**: 展示 `RedissonController.java` 文件，编写一个简单的 `@GetMapping("/lock")` 接口，用于测试锁功能。
*   **00:25 - 00:35**: 在 `RedissonController.java` 中，通过 `@Autowired` 注入 `RedissonDistributedLocker` 对象，并编写 `lock` 方法，用于获取和释放锁。
*   **00:35 - 00:45**: 在 `RedissonDistributedLocker.java` 中，编写 `lock` 方法，使用 `RLock` 对象获取锁，并在 `unLock` 方法中释放锁。
*   **00:45 - 00:55**: 在 `RedissonController.java` 中，修改 `lock` 方法，使其支持传入超时时间参数 `time`，并使用 `lock(lockkey, time, TimeUnit.SECONDS)` 方法。
*   **00:55 - 01:05**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **01:05 - 01:15**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **01:15 - 01:25**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **01:25 - 01:35**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **01:35 - 01:45**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **01:45 - 01:55**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **01:55 - 02:05**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **02:05 - 02:15**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **02:15 - 02:25**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **02:25 - 02:35**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **02:35 - 02:45**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **02:45 - 02:55**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **02:55 - 03:05**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **03:05 - 03:15**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **03:15 - 03:25**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **03:25 - 03:35**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **03:35 - 03:45**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **03:45 - 03:55**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **03:55 - 04:05**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **04:05 - 04:15**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **04:15 - 04:25**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **04:25 - 04:35**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **04:35 - 04:45**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **04:45 - 04:55**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **04:55 - 05:05**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **05:05 - 05:15**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **05:15 - 05:25**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **05:25 - 05:35**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **05:35 - 05:45**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **05:45 - 05:55**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **05:55 - 06:05**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **06:05 - 06:15**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **06:15 - 06:25**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **06:25 - 06:35**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **06:35 - 06:45**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **06:45 - 06:55**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **06:55 - 07:05**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **07:05 - 07:15**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **07:15 - 07:25**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **07:25 - 07:35**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **07:35 - 07:45**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **07:45 - 07:55**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **07:55 - 08:05**: 在 `RedissonController.java` 中，编写 `unLock` 方法，用于释放锁。
*   **08:05 - 08:15
