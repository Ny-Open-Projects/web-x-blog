# 画面线理解：06_zk分布式主键_主键生成测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\06_zk分布式主键_主键生成测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:19, 01:16, 01:41, 02:07, 02:37, 03:00, 03:23, 03:55, 04:24, 05:05, 05:25, 06:08, 06:24, 06:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:08:50

1) 这一组画面整体在讲如何在 Spring Boot 项目中通过 ZooKeeper 实现分布式 ID 生成器（Sequence），并编写单元测试验证其功能。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了项目结构，当前打开的是 `ZkConfig.java` 文件，其中定义了 `@Configuration` 和 `@PropertySource` 注解，用于加载 `zookeeper.properties` 配置文件，并创建 `ZookeeperClient` 实例。
画面 2: 在测试包 `com.heima.zookeeper.test` 下创建新类 `ZkTest`。
画面 3: 在 `ZkTest` 类中导入 Spring Boot 测试相关依赖，并使用 `@SpringBootTest` 注解标注测试类。
画面 4: 为 `ZkTest` 类添加 `@Autowired` 注解，注入 `Sequences` 类的实例。
画面 5: 在 `ZkTest` 类中编写测试方法 `test1()`，调用 `sequences.sequenceReadBehavior()` 方法。
画面 6: 运行测试，控制台输出日志，显示 Spring Boot 应用启动成功。
画面 7: 查看 `ZookeeperClient` 类中的 `sequence` 方法，该方法用于获取序列值。
画面 8: 查看 `ZookeeperClient` 类中的 `initZSequence` 方法，用于初始化序列。
画面 9: 在调试模式下，查看 `ZkTest` 类中 `test1()` 方法的执行过程，变量 `seq` 为 `null`。
画面 10: 在 `ZookeeperClient` 类中，将 `zkSequenceMap.put(name, zkSequence);` 语句设置为断点并调试。
画面 11: 在 `ZkTest` 类中，将 `test1()` 方法中的 `sequenceReadBehavior()` 方法设置为断点并调试。
画面 12: 在 `ZkTest` 类中，将 `test1()` 方法中的 `for` 循环设置为断点并调试。
画面 13: 运行测试，控制台输出日志，显示 `Zookeeper` 客户端连接成功。
画面 14: 运行测试，控制台输出日志，显示 `Zookeeper` 客户端连接成功，并输出了生成的序列号。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面 1:
```java
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
@PropertySource("classpath:zookeeper.properties")
public class ZkConfig {
    String host;
    String sequencePath;

    public ZookeeperClient zookeeperClient() {
        return new ZookeeperClient(this.host, this.sequencePath);
    }
}
```

画面 3:
```java
import com.heima.behavior.BehaviorJarApplication;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest(classes = BehaviorJarApplication.class)
public class ZkTest {
}
```

画面 4:
```java
@Autowired
private Sequences sequences;
```

画面 5:
```java
public void test1() {
    long along = sequences.sequenceReadBehavior();
    System.out.println("Long" + "------------------");
}
```

画面 7:
```java
public Long sequence(ZkSequenceEnum name) {
    try {
        ZkSequence seq = zkSequenceMap.get(name);
        if (seq == null) {
            return seq.sequence();
        }
    } catch (Exception e) {
        logger.error("获取[{}]Sequence错误:{}", name, e);
        e.printStackTrace();
    }
    return null;
}
```

画面 8:
```java
public void initZSequence() {
    zkSequenceMap.put(name, zkSequence);
    for (int i = 0; i < list.length; i++) {
        String name = list[i].name();
        zkSequenceMap.put(name, zkSequence);
    }
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
