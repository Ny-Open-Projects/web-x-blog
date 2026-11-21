# 05_zk分布式主键_config封装

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\05_zk分布式主键_config封装【海量资源尽在 666java.com】.mp4
- 时长 6分24秒（音频 384s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们继续往下讲刚才咱刚才呢咱们是把当前的客户端给封装了一下那为了后期呢能够更方便的让这个其他模块去调用啊所以说呢咱们再去进行有一个统一的这种封装啊这封装呢主要呢就是调去当前客户端创建当前组keeper客户端的一个实力就完事了啊那这个怎么写呢其实这个东西比较简单啊这个跟咱们之前封装买伺服是差不多的
[00:26] 咱们主要的是有一个这样的并哎让他住到死不认的容器中哎这时候谁想用直接去拿这个当前这个值就可以了好吧那这个咱们去写一下啊那这个呢是在当前组gaybar下面有一个zk config好ctrl c一下啊然后是创建一个类这类里边呢其实呢他是一个配置类啊所以说咱们首先加一个config然后呢然后咱们需要去解一个方法是吧public
[00:56] 然后返回的就是toKeeperClient然后是我们叫toKeeperClient最终咱们需要去return一个new一个什么呢return new一个toKeeperClient它需要两个参数第一个是host二个是当前的一个地址是吧那这时候咱们就可以去从当前的配置文件中去读那读的话怎么读呢咱们之前讲过吧在这去怎么写
[01:26] 首先你得去加一个助理叫configuration properties是吧你可以去设置一个前置然后咱们的前置是啥呢等一下前置是不是好VK啊比如说在这去写啊就是Z好那这个加完之后咱们还要去把这个文件给加载进来这文件加载进来那你来用哪个什么Property是吧你可以去设置一下class pass下边的哪个呢就是当前的这个路径是吧
[01:56] 做keeper的properties放进来之后咱们还需要去出取这两个里边的文件里边两个属性是吧主要文件叫属性一个叫host一个叫sequence pathOK那咱们怎么写写一下一个是str的型的host好这个是private写法叫什么sequence path要去掉了吧p什么p改成大小好
[02:25] 好这样就完了写错了吗这是个spin好那写完之后我看看seqencpass没问题这时候你要在这去加上比如说有一个host这样最好是给他最好你应该去在这去加上什么setter和setter方法然后你再去拿
[02:57] list.host然后是list.那个地址好那这样的话就算是封装结束了好吧行那这个结束完之后啊咱们为了能够更方便啊你看这里边其实还有东西咱们又做了一次封装就是sirkins的封装其实呢你在项目中直接注入它能不能行呢可以
[03:22] 可以的话呢你还要去拿到具体的你看这里边啊你创建这个Soccer Client之后呢你看啊当前这儿你是不是还得去调用当前的Sequence然后还要拿到当前的某一个表的名称最终是拿到具体的值啊那这一步咱们能不能封装呢能不能封装呢也可以那怎么封装呢好来看啊这里边呢其实就是在这儿又去创建了Sequence然后把当前的Soccer Client给封装进去之后呢
[03:51] 对针对于某一些表所需要的当前ZK生成的主件的表通一都去进行了封装这时候呢你再去某个地儿去需要去用到主件的时候比如说当前那个APLX它需要的话你只需要去注入当前的Sequence就可以了然后注入它之后呢调用那个方法是不是就能自动返回当前的一个浪内型的自动的IT啊所以说啊咱们再去封装一个啊在这儿再去加一个叫什么叫Sequence
[04:21] 然后呢是去加一个compound让他什么意思让sprint去管理是吧所以说咱们在这private然后是zokeeperclient然后注入进来然后下面呢就写的时候呢其实就比较简单了有的时候你直接去某一个表去写就可以了比如说public这个有问题吗zokeeperclient
[04:54] 怎么爆红了呢我看这啊啊不对啊不是足给了可烂的啊啊是足给我看的没没问题啊但这应该是少个东西当前封装的时候啊这应该是少了一个爱他别好吧一般他应该不会报错啊嗯好你看现在好了是吧好那返回的是一个浪类型啊然后呢说针对于s e u u c e说ap likes好基于
[05:32] cplex 咱们同期那很简单了直接 return this.走k一盘client 打什么呢打一个sequence 传的是谁呢传的就是前的某一个表是吧是咱们的numer里边的cplex这样的话其实就可以了行这个其实就是咱们的
[05:56] 根据于当前的名称去拿到某一个序列这个其实有很多都一样直接考过来就可以了它是针对于当前咱们定义的某一个美举类型所以不去定义了当前的东西都一样client这叫client是吧讲名吧好吧叫client它也叫client这样讲问题了这个封装完之后咱们下面就来去测一下看看到底好使不好使

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spring Boot 配置类和注解方式，结合 Zookeeper 客户端，实现分布式序列号功能。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 ZookeeperClient.java 中的 init() 方法，用于初始化 CuratorFramework 客户端并启动，以及 initSequence() 方法用于创建序列节点。
画面2: 展示 ZkConfig.java 文件，定义了 @Configuration 注解的类，用于配置 Zookeeper 客户端。
画面3: 展示 ZkConfig.java 中的 @ConfigurationProperties 注解，用于绑定配置属性。
画面4: 展示 ZooKeeper.properties 文件，定义了 zk.host 和 zk.sequence-path 的配置。
画面5: 展示 ZkConfig.java 中使用 @ConfigurationProperties(prefix = "zk") 和 @PropertySource("classpath:ZooKeeper.properties") 注解绑定配置。
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
package com.heima.common.ZooKeeper;

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
@PropertySource("classpath:ZooKeeper.properties")
public class ZkConfig {
```

画面6:
```java
@ConfigurationProperties(prefix = "zk")
@PropertySource("classpath:ZooKeeper.properties")
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
@PropertySource("classpath:ZooKeeper.properties")
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
@PropertySource("classpath:ZooKeeper.properties")
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
package com.heima.ZooKeeper.sequence;

import org.springframework.stereotype.Component;

@Component
public class Sequences {
```

画面11:
```java
package com.heima.common.ZooKeeper;
import com.heima.common.ZooKeeper.sequence.ZkSequenceEnum;
import com.heima.common.ZooKeeper.sequence.ZkSequence;
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

