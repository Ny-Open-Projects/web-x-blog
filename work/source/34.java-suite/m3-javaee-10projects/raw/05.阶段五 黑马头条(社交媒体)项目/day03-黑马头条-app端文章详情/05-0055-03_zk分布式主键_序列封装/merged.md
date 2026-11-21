# 03_zk分布式主键_序列封装

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\03_zk分布式主键_序列封装【海量资源尽在 666java.com】.mp4
- 时长 9分30秒（音频 570s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们下面呢就来去把这个当前的分布式组件这个封装代表简单去写一下啊那首先呢咱们要去定义一个这种枚举那这个枚举呢是定义的是这样的一个效果是根据某些表呢然后是去定义那这表是怎么来的呢其实呢是在咱们昨天啊昨天里边呢是有一个这样的一个表这个表呢其实大家都有啊里边呢是定义了某一些
[00:28] 当前的主见生成方式的适用的是什么呢你看ZK sequenceZK sequence看到了吧目前的话呢你看我在笔记上去定义了这么几个分别呢是当前的喜欢喜欢是吧当前的是文章的喜欢类型啊Legs还有什么AP read behavior就是当前的读取文章的行为还有一个收藏还有一个是关注还有一个粉丝就这些表呢目前的话当然是
[00:56] 根据业务需要目前这些表他们需要去使用当前的组keeper去生成主件那你说我们之前用mycat不行吗非得要用它去生成主件吗并且还是自增的mycat不是也能去生成自增的主件吗是的mycat是能生成但是组keeper这块它也能生成它生成的好处就是mycat是有一个不能完成的就是说咱们现在因为这里边都是加入了一个burst
[01:26] 都是加入了一个Boss那这个Boss其实有两部分组成是吧你看第一部分是ID然后第二部分其实是当前某一个表中的某一个字段进行分片确定到底在哪一片那你要是用MyCat的话它不能确定第二个字段所以说咱们用什么呢用ToKeep这种方式叫自以维护当前的字增的组件的方式
[01:54] 所以说这块咱们还是要去用当前的一个这种自动的组件需要去手动维护咱们现在刚才说了就是采用的谁采用的就是主keeper首先咱们就进行封装封装思路就是首先咱们要去创建一些表的枚举因为一个表它都应该会有一个自动的ID是吧咱们根据咱们的业务去创建了那么多的这种枚举那这枚举的话咱们看一下看看在哪去写
[02:23] 就是还是在当前的common中去写啊那也能写一下啊在这呢去定义一个什么呢定义一个包名叫组keeper什么的叫sequencence啊然后呢这个这个类名呢是叫他咱们直接拷过来啊跟笔记包是一致啊好点ok这里边呢他是个numer啊然后这里边啊就是刚才说了就是需要有这几个表第一个是aplex
[02:56] 好那第二个呢就是咱们的一个读取的行为叫readcover好然后第三个呢第三个呢是咱们的一个当前的收藏表然后最后一个还有一个到第二个啊这个是用户的关注表好还有一个就是当前的一个用户的粉丝user
[03:30] 好那这样的话咱们这个枚举啊就算是定义完了这个定义完之后怎么用啊一会咱们再说然后下面咱们就接着写那接着写啥呢写的是往下看啊当前里边的是需要去生成一个主件值那到底用谁去生成主件值呢这里边呢其实有一个分布式的原子自登类这是组keeper客户端里边提供的一个类啊叫就这个类啊他这个类里边呢就有一个叫什么呢叫increment
[03:59] 我先走啊有个increment它呢就能去生成一个当前的自增的并且是分布式的组件保证是只能生成一次是有原子性的行那这个呢咱们就用它啊那这里边还有一个注意事项啊就是说咱们是每500毫秒重视三次后仍然生成失败返回囊咱们是做这么一个处理
[04:25] 但是你要是不这么做的话呢它会有一个默认值默认值的话时间在长所以说咱们是有只让它重视三次并且是只有500毫秒好吧行那咱们就创建这个类啊那这个类呢是也是在当前的包下边啊又一个类出来那这类里边该怎么写呢首先呢咱们刚才说了啊就是有当前某一个这个类吧让它去生成咱们主要把这个类给构建出来就可以了啊构建的方式是这样啊
[04:55] 现在方式就是什么现在的声明一下声明的时候咱们是在这去写个变量这里面保持一致吧用的咱们是用了一个当前的步骤方法用下你去创建的时候它是需要有几个参数的来看一下等于什么等于6一个它参数有点新的你可以点进去看一看这边有三个第一个是客户端
[05:21] 然后第二个呢其实这个客户端呢再说一下啊这个客户端呢其实就是你怎么去连接上当前的组keeper这个呢咱们一会儿再次去封装然后第二个呢就是当前的一个地址而这个地址呢其实就是说的当前的某一个你的那个生成的表的对应表的一个地址那这是你可以这样理解啊就是说我一个表就是一个地址就是区分某些表的字端或者区分表去生成组件
[05:51] 这能理解吧好那这个呢就是刚才咱们说的哪一块呢就是说咱们要去设置一个500毫秒重视三次之后就返回none的一个效果用的是当前的这个类好吧行那咱们就一块来写一下啊好返回过来那这有三个参数说第一个参数是一个client那client还要再看啊client是一个他那他有吗他好像没有是吧那没有怎么办呢那这时候啊咱们可以把它定义出来定义出来啊
[06:20] 可以让他给传过来传过来之后呢咱们就可以把它呢给放上去那这个具体怎么来呢其实呢咱们一会呢会独自再去封装一个客户端好吧行那第二个值呢你看啊第二个值是个pass那这个pass呢其实咱们也可以传过来谁用当前的VK Service就让谁传过来然后第三个值第三个值就不能传了啊第三个值是他那咱们呢可以拗出来可以直接在这去定义当前的方法
[06:51] 给什么呢你有一个啊这是它这个接口啊它这个接口接口的话咱们主要用的是当前的是这个是这个啊这个可以去设置一些时间你看它是有默认值的咱们要去手动付两个值好吧来看一下嗯用的是一次就它第一个参数啊就是500就是你说的是500毫秒同时几次呢三次同时三次之后如果说还是不行咱们就连返回一个none所以说你把它
[07:25] 反过来,第二个参数是pass第三个参数就是当前的这个值这时候呢,咱们就可以去构建当前的一个类这个类可以直接给它好,那构建完之后呢,这个没有参数了啊就只有两个参数那这个构建完之后呢咱们现在呢就可以用它呢去生成咱们的序列那生成序列的话呢就是咱们可以再构建一个方法比如说public返回一个lang的形式,s1,6,5,1,n
[07:59] 这一啊就要的方法啊然后你可以看一下当前这个里边里有没有点什么呢increment他他呢会给你返回一个当前那个automicautomic value啊里边其实这个increment他呢呃稍等啊这报错了是吧报错了之后我先抛先把这一堂给然后咱们再往下看啊最最终是我该怎么去拿到具体的某一个量类型的值因为我现在返回的是不量类型啊
[08:30] 那这个很简单啊咱们可以去判断一下那啥呢其实里边有一个方法increment.它是否成功成功之后呢就可以直接return什么呢increment.有一个叫说的啊post valueok这个返回的其实就是一个浪里形行那这个简单写一下啊生成序列好
[09:04] 然后这还报错是吧咱们可以再去返回一下如果说他不成功的话呢你直接返回什么东西返回弄就可以了啊好那当前的这个ZKSW呢咱们就封装完了好下面呢咱们就来去封装当前的一个叫客户端并且是把客户端跟当前那个pass传过来之后呢咱们再去生成这个序列啊行那咱们先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
创建com.heima.common.ZooKeeper.sequence.ZKSequenceEnum文件，用于定义通过ZK生成自增ID的枚举，
在项目中规范要求与物表关联项目，使用与当前项目阶段的枚举如下：
public enum ZkSequenceEnum {
    AP_LIKES, AP_READ_BEHAVIOR, AP_COLLECTION, AP_USER_FOLLOW, AP_USER_FAN
}

1.4 序列封装
创建com.heima.common.ZooKeeper.sequence.ZKSequence文件，用于封装程序在运行时每个表对应的自增
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
package com.heima.common.ZooKeeper.sequence;

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

