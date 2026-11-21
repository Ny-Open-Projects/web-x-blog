# 画面线理解：05_zk分布式主键_config封装

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\05_zk分布式主键_config封装【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:41, 00:59, 01:32, 02:04, 02:23, 02:46, 03:00, 03:23, 04:00, 04:36, 04:59, 05:24, 05:48, 06:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:08:18

1) 这一组画面整体在讲如何使用 Spring Boot 配置类和注解方式，结合 Zookeeper 客户端，实现分布式序列号功能。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 ZookeeperClient.java 中的 init() 方法，用于初始化 CuratorFramework 客户端并启动，以及 initSequence() 方法用于创建序列节点。
画面2: 展示 ZkConfig.java 文件，定义了 @Configuration 注解的类，用于配置 Zookeeper 客户端。
画面3: 展示 ZkConfig.java 中的 @ConfigurationProperties 注解，用于绑定配置属性。
画面4: 展示 zookeeper.properties 文件，定义了 zk.host 和 zk.sequence-path 的配置。
画面5: 展示 ZkConfig.java 中使用 @ConfigurationProperties(prefix = "zk") 和 @PropertySource("classpath:zookeeper.properties") 注解绑定配置。
画面6: 展示 ZkConfig.java 中的构造方法，用于创建并返回 ZookeeperClient 实例。
画面7: 展示 ZkConfig.java 中为 host 和 sequencePath 添加了 Getter 和 Setter 方法。
画面8: 展示 Typora 文档中关于 ZkConfig 配置类的说明，包括注解和代码。
画面9: 展示 Sequences.java 文件中定义了多个序列方法，如 sequenceApLikes、sequenceApReadBehavior 等。
画面10: 展示 Sequences.java 文件中定义了 @Component 注解。
画面11: 展示 ZookeeperClient.java 文件，定义了类的包名、导入的依赖和类的结构。
画面12: 展示 Sequences.java 文件中定义了 @Autowired 注解的 private ZookeeperClient client 字段。
画面13: 展示 Sequences.java 文件中定义了 sequenceApLikes 方法，调用 client.sequence 方法。
画面14: 展示 Sequences.java 文件中定义了 sequenceApReadBehavior、sequenceApCollection、sequenceApUserFollow、sequenceApUserFan 方法，分别调用 client.sequence 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```java
public void init() {
    this.client = CuratorFrameworkFactory.builder().connectString(this.getHost())
            .connectionTimeoutMs(CONNECTION_TIMEOUT)
            .sessionTimeoutMs(SESSION_TIMEOUT)
            .retryPolicy(new ExponentialBackoffRetry(SLEEP_TIME_MS, MAX_RETRIES)).build();
    this.client.start();
    this.initSequence();
}

public void initSequence() {
    ZkSequenceEnum[] list = ZkSequenceEnum.values();
    for (int i = 0; i < list.length; i++) {
        String name = list[i].name();
        ZkSequence zkSequence = new ZkSequence(this.client, path);
        zkSequenceMap.put(name, zkSequence);
    }
}

public Long sequence(ZkSequenceEnum name) {
    try {
```

画面2:
```java
package com.heima.common.zookeeper;

import org.springframework.context.annotation.Configuration;

@Configuration
public class ZkConfig {

}
```

画面3:
```java
@ConfigurationProperties
public class ZkConfig {
    @ConfigurationProperties(prefix = "zk")
    public ZookeeperClient return new
```

画面4:
```properties
zk.host=192.168.220.145:2181
zk自增序列节点
zk.sequence-path=/heima-leadnews/sequence/
```

画面5:
```java
@ConfigurationProperties(prefix = "zk")
@PropertySource("classpath:zookeeper.properties")
public class ZkConfig {
```

画面6:
```java
@ConfigurationProperties(prefix = "zk")
@PropertySource("classpath:zookeeper.properties")
public class ZkConfig {
    String host;
    String sequencePath;
    public ZookeeperClient zookeeperClient() {
        return new ZookeeperClient();
    }
}
```

画面7:
```java
@ConfigurationProperties(prefix = "zk")
@PropertySource("classpath:zookeeper.properties")
public class ZkConfig {
    String host;
    String sequencePath;
    public ZookeeperClient zookeeperClient() {
        return new ZookeeperClient(this);
    }
}
```

画面8:
```java
// 自动配置核心线程池的生命周期
@Setter
@Getter
@Configuration
@ConfigurationProperties(prefix = "zk")
@PropertySource("classpath:zookeeper.properties")
public class ZkConfig {
    String host;
    String sequencePath;
    @Bean
    public ZookeeperClient zookeeperClient() {
        return new ZookeeperClient(this.host, this.sequencePath);
    }
}
```

画面9:
```java
@Component
public class Sequences {

    @Autowired
    private ZookeeperClient client;

    public Long sequenceApLikes() {
        return this.client.sequence(ZkSequenceEnum.AP_LIKES);
    }

    public Long sequenceApReadBehavior() {
        return this.client.sequence(ZkSequenceEnum.AP_READ_BEHAVIOR);
    }

    public Long sequenceApCollection() {
        return this.client.sequence(ZkSequenceEnum.AP_COLLECTION);
    }

    public Long sequenceApUserFollow() {
        return this.client.sequence(ZkSequenceEnum.AP_USER_FOLLOW);
    }

    public Long sequenceApUserFan() {
        return this.client.sequence(ZkSequenceEnum.AP_USER_FAN);
    }
}
```

画面10:
```java
package com.heima.zookeeper.sequence;

import org.springframework.stereotype.Component;

@Component
public class Sequences {
```

画面11:
```java
package com.heima.common.zookeeper;
import com.heima.common.zookeeper.sequence.ZkSequenceEnum;
import com.heima.common.zookeeper.sequence.ZkSequence;
import lombok.Getter;
import lombok.Setter;
import org.apache.curator.framework.CuratorFramework;
import org.apache.curator.framework.CuratorFrameworkFactory;
import org.apache.curator.retry.ExponentialBackoffRetry;
import org.apache.curator.retry.RetryPolicy;
import org.apache.curator.retry.RetryOneTime;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryPolicy;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryOneTime;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org.apache.curator.retry.RetryNTimes;
import org
