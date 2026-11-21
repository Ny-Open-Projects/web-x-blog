# 画面线理解：03_zk分布式主键_序列封装

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\03_zk分布式主键_序列封装【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:21, 02:29, 03:41, 04:38, 04:54, 05:17, 06:09, 06:56, 07:08, 07:38, 08:07, 08:40, 08:51, 09:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:06:17

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 ZooKeeper 和 Curator 库实现分布式序列生成器，包括枚举定义、序列类实现、重试策略配置及异常处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示一个 Excel 表格，列出了多个表的主键生成方式（如 auto_increment、zk_sequence），并标注了分表字段和分表数，用于说明需要分布式序列的表。
画面 2：IDE 中显示项目结构，当前选中的是 `heima-leadnews-common` 模块下的 `src/main/java/com/heima/common/` 目录，准备编写序列相关代码。
画面 3：打开文档，显示了技术文档中关于“枚举封装”和“序列封装”的说明，指出需要创建 `ZkSequenceEnum` 枚举和 `ZkSequence` 类。
画面 4：在 IDE 中，`ZkSequenceEnum` 枚举类被高亮显示，内容为定义了多个常量，如 `AP_LIKES`, `AP_READ_BEHAVIOR` 等。
画面 5：IDE 中，`ZkSequence` 类文件被选中，准备编写序列生成逻辑。
画面 6：在 `ZkSequence` 类中，导入了 `org.apache.curator.framework.recipes.atomic.DistributedAtomicLong`，并开始编写构造函数。
画面 7：查看 `DistributedAtomicLong` 类的源码，了解其内部实现，包括构造函数和 `increment()` 方法。
画面 8：在 `ZkSequence` 类中，为 `retryPolicy` 成员变量赋值，选择 `ExponentialBackoffRetry` 类型。
画面 9：查看 `ExponentialBackoffRetry` 类的源码，了解其构造函数参数和内部逻辑。
画面 10：在 `ZkSequence` 类中，完成 `retryPolicy` 的初始化，使用 `new ExponentialBackoffRetry(500, 3)`。
画面 11：在 `ZkSequence` 类中，编写 `sequence()` 方法，调用 `distAtomicLong.increment()`。
画面 12：在 `ZkSequence` 类中，为 `sequence()` 方法添加返回值，选择 `return increment.postValue()`。
画面 13：在 `ZkSequence` 类中，完善 `sequence()` 方法，添加 `if (increment.succeeded()) return increment.postValue(); else return null;` 逻辑。
画面 14：在 `ZkSequence` 类中，完成 `sequence()` 方法，最终代码为 `if (increment.succeeded()) return increment.postValue(); else return null;`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3 中的文档内容：
```
1.3 枚举封装
创建com.heima.common.zookeeper.sequence.ZKSequenceEnum文件，用于定义通过ZK生成自增ID的枚举，
在项目中规范要求与物表关联项目，使用与当前项目阶段的枚举如下：
public enum ZkSequenceEnum {
    AP_LIKES, AP_READ_BEHAVIOR, AP_COLLECTION, AP_USER_FOLLOW, AP_USER_FAN
}

1.4 序列封装
创建com.heima.common.zookeeper.sequence.ZKSequence文件，用于封装程序在运行时每个表对应的自增
器，这些主要通过分布式原子自增（DistributedAtomicLong）实现，注意每500毫秒重试3次以后生成失败
代码如下：
public class ZkSequence {
    RetryPolicy retryPolicy = new ExponentialBackoffRetry(500, 3);
    DistributedAtomicLong distAtomicLong;
    public ZkSequence(String sequencename, CuratorFramework client) {
        distAtomicLong = new DistributedAtomicLong(client, sequencename, retryPolicy);
    }
}
```

画面 4 中的代码：
```
package com.heima.common.zookeeper.sequence;

public enum ZkSequenceEnum {
    AP_LIKES, AP_READ_BEHAVIOR, AP_COLLECTION, AP_USER_FOLLOW, AP_USER_FAN
}
```

画面 6 中的代码：
```
import org.apache.curator.framework.recipes.atomic.DistributedAtomicLong;

public class ZkSequence {
    DistributedAtomicLong distAtomicLong;
    public ZkSequence(CuratorFramework client, String counterPath) {
        this.distAtomicLong = new DistributedAtomicLong(client, counterPath, retryPolicy);
    }
}
```

画面 7 中的代码：
```
public class DistributedAtomicLong implements DistributedAtomicNumber<Long> {
    private final AtomicValue<Long> value;
    public DistributedAtomicLong(CuratorFramework client, String counterPath, RetryPolicy retryPolicy) {
        this(client, counterPath, retryPolicy, PromotedClock.NULL);
    }
    public DistributedAtomicLong(CuratorFramework client, String counterPath, RetryPolicy retryPolicy, PromotedClock promotedClock) {
        this.value = new AtomicValue<Long>(client, counterPath, retryPolicy, promotedClock);
    }
    public AtomicValue<Long> get() throws Exception {
        return new DistributedAtomicLong(client, counterPath, retryPolicy, promotedClock);
    }
    public void forceSet(Long newValue) throws Exception {
        this.value.forceSet(this.valueToBytes(newValue));
    }
}
```

画面 8 中的代码：
```
RetryPolicy retryPolicy = new ExponentialBackoffRetry(500, 3);
```

画面 9 中的代码：
```
public class ExponentialBackoffRetry extends SleepingRetry {
    private static final int MAX_RETRIES_LIMIT = 20;
    private static final int DEFAULT_MAX_SLEEP_MS = 2147483647;
    private final Random random;
    private final int maxSleepMs;
    public ExponentialBackoffRetry(int baseSleepTimeMs, int maxRetries, int maxSleepMs) {
        this(baseSleepTimeMs, maxRetries, maxSleepMs, DEFAULT_MAX_SLEEP_MS);
    }
    public ExponentialBackoffRetry(int baseSleepTimeMs, int maxRetries, int maxSleepMs, int maxSleepMs) {
        super(baseSleepTimeMs, maxRetries, maxSleepMs);
        this.random = new Random();
        this.baseSleepTimeMs = baseSleepTimeMs;
        this.maxSleepMs = maxSleepMs;
    }
}
```

画面 11 中的代码：
```
public class ZkSequence {
    RetryPolicy retryPolicy = new ExponentialBackoffRetry(500, 3);
    DistributedAtomicLong distAtomicLong;
    public ZkSequence(CuratorFramework client, String counterPath) {
        this.distAtomicLong = new DistributedAtomicLong(client, counterPath, retryPolicy);
    }
    public long sequence() {
        distAtomicLong.increment();
    }
}
```

画面 12 中的代码：
```
public class ZkSequence {
    RetryPolicy retryPolicy = new ExponentialBackoffRetry(500, 3);
    DistributedAtomicLong distAtomicLong;
    public ZkSequence(CuratorFramework client, String counterPath) {
        this.distAtomicLong = new DistributedAtomicLong(client, counterPath, retryPolicy);
    }
    public long sequence() {
        AtomicValue<Long> increment = distAtomicLong.increment();
        if (increment.succeeded()) {
            return increment.postValue();
        }
    }
}
```

画面 13 中的代码：
```
public class ZkSequence {
    RetryPolicy retryPolicy = new ExponentialBackoffRetry(500, 3);
    DistributedAtomicLong distAtomicLong;
    public ZkSequence(CuratorFramework client, String counterPath) {
        this.distAtomicLong = new DistributedAtomicLong(client, counterPath, retryPolicy);
    }
    public long sequence() throws Exception {
        AtomicValue<Long> increment = distAtomicLong.increment();
        if (increment.succeeded()) {
            return increment.postValue();
        } else {
            return null;
        }
    }
}
```

画面 14 中的代码：
```
public class ZkSequence {
    RetryPolicy retryPolicy = new ExponentialBackoffRetry(500, 3);
    DistributedAtomicLong distAtomicLong;
    public ZkSequence(CuratorFramework client, String counterPath) {
        this.distAtomicLong = new DistributedAtomicLong(client, counterPath, retryPolicy);
    }
    public long sequence() throws Exception {
        AtomicValue<Long> increment = distAtomicLong.increment();
        if (increment.succeeded()) {
            return increment.postValue();
        } else {
            return null;
        }
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题或架构图/流程图。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
