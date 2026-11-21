# 06_zk分布式主键_主键生成测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\06_zk分布式主键_主键生成测试【海量资源尽在 666java.com】.mp4
- 时长 7分4秒（音频 424s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去测试一下当前这个封装完之后的组keeper这个生成组件的方式到底行不行那这时候咱们随便去找一个微服务去进行测试啊咱们现在就用当前这个行为当前的微服务去进行测试那测试之前呢首先呢你应当先去加载当前的这个配置叫zkzkconfig所以说呢你在这啊先去加一个东西啊咱们写个类好吧叫什么叫做keeperconfig
[00:33] 这里边其实标定两个就可以了第一个是它是一个什么configuration它是一个配对类然后第二个呢是我们需要去扫描包说的话就是扫描当前那个tokeeper包下边啊叫com.k码然后是common tokeeper好那这样就结束了啊它就会去引导类去加载的时候会自动的去扫描它进行加载好吧那这时候咱们就可以写测试类了啊在这去创建一个类
[01:04] 这个类叫啥呢叫com.kma叫做keeper.test叫什么呢叫cktest好吧有点写啊然后环境的话非常简单啊第一个是sprintboot test然后里边有个classes然后需要去指定当前行为引导类的什么行为引导类的class行为引导类的class啊就是它.class然后第二个是runways
[01:35] shrimp render.class好这时候你可以去注入谁啊注入一个sequence不是client是sequence好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好
[02:13] 最终呢它就是一个浪形然后是直接去打印浪形的值就可以了好就这样啊标识一下别的找不着了行这时候咱们可以在这去加一个test好了啊这时候咱们可以去执行一下看看有没有问题稍等正在编译正在加载这过程还挺慢的是吧好马上结束了啊稍等好这个看看有没有打印啊
[03:07] 结束了这是一个none是吧那为什么是none呢那么咱们一块来看一下然后他去调用这儿这之后他去调了一个circuit然后这块是这会出问题了吗咱们可以把它打断点打断点之后咱们可以再调一下打开当前的这儿然后直接去debug运行看一看效果看看到底是哪出的问题
[03:44] 咱们就看就可以了看当前这个集合里边有没有对应的值就可以了来稍等看看是不是上面初始化的时候出问题了他初始化的时候没报错应该不是初始化的问题好这时候咱们可以看一下这个内幕这个内幕的话其实有当前这个值这个内幕好像有问题是吧应该是调用当前这个内幕是吗往下走往下走看这个ICQ它是个none
[04:19] 那它是个NUM的话咱们最终的如果说它是NUM的话它就反过来就是NUM所以说呢这块你稍微改一改啊不是NUM是谁啊?
[04:38] 点OK这样才行啊行那咱们就可以再来测一下啊好使不好使啊好运行好还到这啊看看看看它是不是NUM就可以稍等第二次还挺快的是吧好来了啊看一下啊嗯看一下当前往下走呗看看当前的ICQ有没有值哎他现在是不是有值了
[05:12] 那有值就没有问题啊咱们可以往下走了啊放行吧放行完之后可以看一下当前到底有没有打印值就可以了啊往下走找一找是不是1啊没问题啊那这样的话咱们这个值就拿到了啊咱们也可以这么测啊怎么测呢你可以去做个循环看看它到底是一个什么样的值比如现在是1那这1还能不能再拿到了呢
[05:33] 如果说再拿到的话那就不是自灯了对吧他应该是从2往后排是吧现在他们呢就可以再去写个循环吧比如说4然后是int a啊int啊a等于0a小于多少第50好吧第50啊然后是给加加让他上乘50个然后把它给放进去我们再打印一下啊好来再执行一遍啊咱们就一八个了直接运行他应该是从二开始啊
[06:10] 然后是一次往下排自增的嘛分布式自增的组件值就是用组keeper去做好上程了来看一下啊你看这块啊咱们从第一个开始看啊找到最上面找到最上面你看是不是没有1是吧没有1啊从2开始的然后1时会延续到打印50个应该是几节结尾啊51节尾没问题吧
[06:48] OK啊那目前的话咱们这个分布是主建这块封装的咱们就做到这以后再去用的话呢直接去你在你的业务上去去注入当前这个Service然后去调用对应表中的一个值就可以了好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中通过 ZooKeeper 实现分布式 ID 生成器（Sequence），并编写单元测试验证其功能。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了项目结构，当前打开的是 `ZkConfig.java` 文件，其中定义了 `@Configuration` 和 `@PropertySource` 注解，用于加载 `ZooKeeper.properties` 配置文件，并创建 `ZookeeperClient` 实例。
画面 2: 在测试包 `com.heima.ZooKeeper.test` 下创建新类 `ZkTest`。
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
@PropertySource("classpath:ZooKeeper.properties")
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

