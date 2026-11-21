# 16-限价委托下单-挂单队列并发锁自测验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接着咱们对挂单对列并发所做一个致测和验证

在这里我们采用了Sympathize的

来实现不同的对象所控制

需要去验证是否能够有效控制并生效

通过客户端联条

不能够有效模拟并发的场景

因为你要开启很多客户端

同时发送的这些挂单数据

还必须要和实时行情的报价信息相匹配

所以在这里咱们可以自设而进行功能的验证

咱们首先将以下的测试代码拖比到工程当中

咱们就放在Core的Consume的实现类里面

这里为了简化咱们就通过MainFile网进行测试

实际开发当中

大家还是要去采用JUnit去做对应的测试

咱们来看一下整个测试处理流程

先将对应的包导入进来

首先在这里咱们构造了10个实时行情的对象数据

为了便于区分

咱们在这里设置了不同的StockID

从0开始0到9总共有10个对象

接下来咱们会去开启10个线程

去处理1000次任务的调用

也就是每个线程它会去处理1000次的调用

外层是开启了10个线程

内部的话是对计算逻辑做处理

那在这里是如何去计算和验证呢

它在这里

是做了一个普通方式的累加

接着的话是采用线程安全的方式进行累加

这个GetCount咱们可以点进去看一下

它其实是一个AtomicInteger

也就是一个原子的操作对象

那么原子的操作对象是能够保障线程安全的

所以咱们在这里就可以做一个结果的对比

去检查普通方式的累加和线程安全方式的累加

是否能够匹配正确的

外层是加入了咱们在挂单服务里面所采用的锁处理机制

可以看到它调用的是GetLog方法

这里面的话是一个静态的Map对象

好

咱们再回到刚才的测试逻辑

那首先咱们采用不加上Synchronize关键字的方法进行测试

看一下整个的运行结果

先将它注视掉

然后右键Run运行

大家注意一下

在这里我们会有一个新的方法

就是让整个主线程去休眠5秒

目的的话是为了让这10个线程将这些任务处理完成

最后我们会将整个结果再打印输出

咱们可以检查运行结果是否正确

右键Run运行

咱们将窗口放大一点

在这里我们可以看到它已经打印出了运行结果

我们可以看到这些数据

Total在这里是采用普通方式的累加

Active就是采用普通方式的累加

我们可以看到它是采用现成安全方式的累加

也就是它实际的累加次数

不加上Synchronize的同步锁处理

它们的运行结果是不一致的

这样就产生了现成安全的问题

接着的话咱们再加上Synchronize的关键字

这里面的锁处理逻辑和挂单对垫里面的锁处理逻辑是一致的

咱们再去校训一下它的运行结果

看能否真正的有效控制

右键Run运行

在这里咱们可以看到

经过了10个运行结果

10个现成

每个现成1000次任务的操作之后

它们的普通方式累加结果和现成安全方式的累加结果都是一致的

说明这个并发现成操作是安全性的

为什么Total跟Active有些是900多

有些又是1000多呢

因为在这里咱们是采用一个随机的方式

去选取不同的对象进行操作

所以有的对象会比较多一点

有的对象操作次数会相对少一点

最主要

咱们是要关注采用现成安全的方式

原子性操作

它的结果和普通方式累加的结果是否一致

通过外层锁处理机制

是可以保障整个现成处理安全的

好

那咱们回到讲义当中

这里咱们是通过自测去验证了挂单对列的并发锁控制

从运行结果来看

是能够正常生效的

好

那这一讲内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“挂单队列并发处理”功能的单元测试与验证。讲师通过在 `PendingQuoteConsumer` 类中编写并运行一个测试程序，来验证 `synchronized` 关键字能否有效控制并发访问，确保在多线程环境下对共享对象（`TradeStockQuoteLast`）的修改是线程安全的。测试通过创建10个线程，每个线程执行1000次操作，分别使用普通方式和线程安全方式（加锁）来修改对象的 `volume` 和 `count` 字段，并最终对比两个字段的最终值是否一致，以此来验证锁机制的有效性。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开始，讲师在 Typora 文档中展示课程大纲，当前章节为“5. 挂单队列并发的验证”。
*   **00:05 - 00:15**: 讲师切换到 IntelliJ IDEA，展示 `PendingQuoteConsumer.java` 文件，并解释测试目标：验证 `synchronized` 是否能有效控制并发。
*   **00:15 - 00:30**: 讲师在代码中添加测试逻辑，包括创建一个包含10个 `TradeStockQuoteLast` 对象的列表，并为每个对象设置不同的 `stockId`。
*   **00:30 - 00:45**: 讲师编写核心测试逻辑，创建10个线程，每个线程循环1000次，每次从列表中随机选取一个对象，并对其进行操作。
*   **00:45 - 01:00**: 讲师演示了两种操作方式：一种是普通方式（`setVolume`），另一种是线程安全方式（`synchronized` + `incrementAndGet`）。
*   **01:00 - 01:15**: 讲师在代码中添加了 `Thread.sleep(5000);` 以观察测试结果，并在终端中查看输出。
*   **01:15 - 01:30**: 讲师运行测试程序，终端输出显示了每个 `stockId` 对应的 `total`（预期值）和 `actual`（实际值），用于验证线程安全。
*   **01:30 - 01:45**: 讲师在 Typora 文档中展示如何通过 `forEach` 方法来检查两个数量是否一致，并解释了测试的最终目的。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：`5. 挂单队列并发的验证`。
    *   关键点：`我们采用了 synchronized 来实现不同的对象锁控制，需要验证是否能够有效控制并发生效`。
    *   测试目标：`验证加锁与不加对象锁，两个数量是否一致`。

*   **代码关键内容**:
    *   **锁管理方法**:
        ```java
        private static Long getLock(Long stockId) {
            if (null == lockKeys.get(stockId)) {
                lockKeys.put(stockId, stockId);
            }
            return lockKeys.get(stockId);
        }
        ```
    *   **测试主方法**:
        ```java
        public static void main(String[] args) throws Exception {
            // 测试对象锁能否生效
            List<TradeStockQuoteLast> quotelastList = new ArrayList<TradeStockQuoteLast>();
            // 构造十个对象
            for(int i=0; i<10; i++) {
                TradeStockQuoteLast quotelast = new TradeStockQuoteLast();
                quotelast.setStockId(Long.valueOf(60000 + i));
                quotelast.setVolume(0);
                quotelast.setLastPrice(0);
                quotelastList.add(quotelast);
            }
            // 开启十个线程同时处理1000次任务
            for(int i=0; i<10; i++) {
                new Thread(() -> {
                    for(int j=0; j<1000; j++) {
                        TradeStockQuoteLast quotelast = quotelastList.get(RandomUtils.nextInt(0, 10));
                        synchronized (getLock(quotelast.getStockId())) {
                            // 普通方式累加
                            quotelast.setVolume(quotelast.getVolume() + 1);
                            // 线程安全方式累加
                            quotelast.getCount().incrementAndGet();
                            quotelast.setStockId(quotelast.getStockId());
                        }
                    }
                }).start();
            }
            // 检查两个数量是否一致
            quotelastList.forEach(p -> {
                System.out.println(p.getStockId() + ", total :" + p.getCount() + ", actual :" + p.getVolume());
            });
        }
        ```
    *   **测试结果输出示例**:
        ```
        60000, total :1000, actual :1000
        60001, total :1000, actual :1000
        ...
        ```

---

### 4) 关键场景与演示描述

*   **场景一：测试环境搭建**
    *   讲师在 IntelliJ IDEA 中打开 `PendingQuoteConsumer.java` 文件，展示了其结构和 `getLock` 方法。
    *   讲师在 `main` 方法中初始化一个 `ArrayList`，并创建了10个 `TradeStockQuoteLast` 对象，每个对象的 `stockId` 从60000到60009。

*   **场景二：并发测试逻辑编写**
    *   讲师编写了一个 `for` 循环，创建10个线程。
    *   每个线程内部再循环1000次，每次从列表中随机选取一个对象。
    *   使用 `synchronized` 块对选中的对象进行操作，包括普通方式的 `setVolume` 和线程安全方式的 `incrementAndGet`。

*   **场景三：测试结果验证**
    *   讲师在 `main` 方法末尾添加了 `forEach` 循环，用于打印每个对象的 `stockId`、预期值 `total` 和实际值 `actual`。
    *   运行程序后，终端输出显示了每个 `stockId` 对应的 `total` 和 `actual` 值。
    *   通过对比 `total` 和 `actual` 的值，讲师验证了 `synchronized` 机制的有效性，确保了在并发环境下数据的一致性。

*   **场景四：测试结果分析**
    *   讲师在 Typora 文档中展示了如何通过 `forEach` 方法来检查两个数量是否一致。
    *   讲师解释了测试的最终目的：验证加锁与不加对象锁，两个数量是否一致，从而证明锁机制的有效性。
