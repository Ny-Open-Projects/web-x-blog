# 画面线理解：04_zk分布式主键_client封装

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\04_zk分布式主键_client封装【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 01:54, 03:02, 04:12, 05:25, 06:43, 07:42, 09:07, 10:04, 11:07, 12:39, 13:47, 15:16, 15:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:07:19

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 中封装 ZooKeeper 客户端，使用 CuratorFramework 初始化连接并管理 ZK 序列化数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 ZooKeeperClient 类的 Java 代码，包含 Logger、host、sequencePath 字段，以及常量如 SLEEP_TIME_MS、MAX_RETRIES、SESSION_TIMEOUT、CONNECTION_TIMEOUT，和 CuratorFramework client 成员变量。
画面 2: 展示了项目结构，目录包含 main/java/com/heima/common/zookeeper/ 和 resources/sequence/，其中 sequence 包下有 ZkSequence.java。
画面 3: 展示了 ZooKeeperClient 构造函数，接收 host 和 sequencePath 参数，并赋值给成员变量。
画面 4: 展示了 init() 方法的开始部分，调用 CuratorFramework.builder().connectString()。
画面 5: 展示了 CuratorFramework.builder() 的方法链，包括 connectionTimeout、sessionTimeout、retryPolicy 等配置。
画面 6: 展示了 CuratorFramework.builder().connectString().sessionTimeout().retryPolicy().build() 的完整调用链。
画面 7: 展示了 initZkSequence() 方法的开始部分，包含注释和 zkSequenceMap 的声明。
画面 8: 展示了 initZkSequence() 方法的 for 循环，用于遍历 ZkSequenceEnum 值并创建 ZkSequence 对象。
画面 9: 展示了 ZkSequenceEnum 枚举类，包含 AP_LIKES, AP_READ_BEHAVIOR, AP_USER_FOLLOW, AP_USER_FAN 等常量。
画面 10: 展示了 initZkSequence() 方法的完整实现，包括创建 ZkSequence 对象并存入 zkSequenceMap。
画面 11: 展示了 sequence(ZkSequenceEnum name) 方法，用于获取序列值。
画面 12: 展示了 Logger 的导入和声明。
画面 13: 展示了 sequence(ZkSequenceEnum name) 方法的 try-catch 块，用于处理异常并记录错误日志。
画面 14: 展示了 init() 方法的完整实现，包括连接配置、重试策略和启动客户端。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@Setter
public class ZookeeperClient {
    private static Logger logger = LoggerFactory.getLogger(ZookeeperClient.class);
    private String host;
    private String sequencePath;

    // 重试间隔时间
    private final int SLEEP_TIME_MS = 1000;
    // 最大重试1000次
    private final int MAX_RETRIES = 1000;
    // 会话超时时间
    private final int SESSION_TIMEOUT = 30 * 1000;
    // 连接超时时间
    private final int CONNECTION_TIMEOUT = 3 * 1000;

    // 创建连接实例
    private CuratorFramework client = null;

    // 序列化集合
    private Map<String, ZkSequence> zkSequence = Maps.newConcurrentMap();
}
```

画面 2:
```
com.heima.common
├── main
│   └── java
│       └── com
│           └── heima
│               └── common
│                   └── zookeeper
│                       └── ZookeeperClient.java
└── resources
    └── sequence
```

画面 3:
```java
import org.apache.curator.framework.CuratorFramework;

public class ZookeeperClient {
    private String host;
    private String sequencePath;
    CuratorFramework client;
    
    public ZookeeperClient(String host, String sequencePath) {
        this.host = host;
        this.sequencePath = sequencePath;
    }
}
```

画面 4:
```java
import org.apache.curator.framework.CuratorFramework;
import org.apache.curator.framework.CuratorFrameworkFactory;

@Setter
public class ZookeeperClient {
    private String host;
    private String sequencePath;
    CuratorFramework client = null;

    public void init() {
        CuratorFrameworkFactory.builder().connectString(String);
    }
}
```

画面 5:
```java
CuratorFramework client = CuratorFrameworkFactory.builder()
    .connectionTimeoutMs(30 * 1000)
    .sessionTimeoutMs(30 * 1000)
    .retryPolicy(new ExponentialBackoffRetry(1000, 3))
    .build();
```

画面 6:
```java
CuratorFramework client = CuratorFrameworkFactory.builder()
    .connectionTimeoutMs(CONNECTION_TIMEOUT)
    .sessionTimeoutMs(SESSION_TIMEOUT)
    .retryPolicy(new ExponentialBackoffRetry(SLEEP_TIME_MS, MAX_RETRIES))
    .build();
```

画面 7:
```java
// 序列化集合
private Map<String, ZkSequence> zkSequence = Maps.newConcurrentMap();

public void initZkSequence() {
    ZkSequenceEnum[] list = ZkSequenceEnum.values();
    for (int i = 0; i < list.length; i++) {
        String name = list[i].name();
        String path = this.sequencePath + name;
        ZkSequence zkSequence = new ZkSequence(this.client, path);
        zkSequenceMap.put(name, zkSequence);
    }
}
```

画面 8:
```java
public void initZkSequence() {
    ZkSequenceEnum[] list = ZkSequenceEnum.values();
    for (int i = 0; i < list.length; i++) {
        String name = list[i].name();
        String path = this.sequencePath + name;
        ZkSequence zkSequence = new ZkSequence(this.client, path);
        zkSequenceMap.put(name, zkSequence);
    }
}
```

画面 9:
```java
package com.heima.common.zookeeper.sequence;

public enum ZkSequenceEnum {
    AP_LIKES,
    AP_READ_BEHAVIOR,
    AP_USER_FOLLOW,
    AP_USER_FAN
}
```

画面 10:
```java
public void initZkSequence() {
    ZkSequenceEnum[] list = ZkSequenceEnum.values();
    for (int i = 0; i < list.length; i++) {
        String name = list[i].name();
        String path = this.sequencePath + name;
        ZkSequence zkSequence = new ZkSequence(this.client, path);
        zkSequenceMap.put(name, zkSequence);
    }
}
```

画面 11:
```java
public long sequence(ZkSequenceEnum name) {
    ZkSequence seq = zkSequenceMap.get(name);
    if (seq == null) {
        return seq;
    }
    try {
        return seq.sequence();
    } catch (Exception e) {
        logger.error("获取[{}]Sequence错误: {}", name, e);
        e.printStackTrace();
        return null;
    }
}
```

画面 12:
```java
import java.util.Map;
import org.apache.curator.framework.CuratorFramework;
import org.apache.curator.framework.CuratorFrameworkFactory;
import org.apache.curator.framework.api.BackgroundCallback;
import org.apache.curator.framework.api.CuratorEvent;
import org.apache.curator.framework.api.CuratorWatcher;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
import org.apache.curator.framework.api.CuratorWatcherListener;
