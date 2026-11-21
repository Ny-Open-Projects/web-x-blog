# day15-12-定时还款任务-配置类

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-6 实现定时还款任务
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-6 实现定时还款任务\day15-12-定时还款任务-配置类_【海量资源尽在 666java.com】.mp4
- 时长 10分11秒（音频 612s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把这个任务类编写好了由任务类是不是调上右层去触发这个功能执行那任务类有谁触发对不对就是这个isq的方案谁去执行呢那这里边的话我们就需要增加两块配置啊两块配置类一块就是ZooKeeper的一块就是elastic job的这两大块配置好之后呢将来这个方案就由什么elastic job他去执行就行了
[00:25] 那这两块代码呢其实跟咱前面elastic job入门案例里边那个代码基本上是一模一样的咱看一看讲义首先呢是ZooKeeper的一个配置类吧大家知道啊ZooKeeper是一个独立的服务我们需要什么呀得到他的服务器地址以及什么呀名称空间啊然后在这个出手化方法里边呢去最终创建出来这个什么呀对注册中心这个对象就行了啊
[00:53] 这个代码呢我就不再从头给大家编写了呃这因为呢这个咱刚写过第二个呢是这个代码基本上是不定不变的呃那咱就在哪写呢在configure里边我们也放到job里边了好吧跟定时任务相关的都放到job里边那这呢我需要新定义一个类讲义保持一致然后呢在这呢加上一个configuration的这样的一个注解
[01:24] 然后在这里边我们是不是需要注入两个值吗我们刚才看讲也说了一个是做keeper服务的地址对不对一个是名称空间这两个值我们都已经配置在什么地方了对Apollo上了其实就这两个值是吧所以我们接下来需要把这两个值呢给他注进来做一个准备工作啊这个名字我们跟讲义保持一日吧我先声明俩属性这个名字叫job namespace然后呢我们
[02:07] 注入的话是还是通过什么呀Value注解这里面是写表达是对吧直直你要看看你的Apollo里边的这个配置比如说这个服务地址应该就是拷贝这个纸给他拿过来你错了然后名称空间名称空间的纸拿过来给他放到这
[02:40] 这两个值咱现在是不是就拿了手拿了手之后呢我们接下来主要就是编写一个出手话的一个方法对不对在这个方案里面我们是不是回过一下啊咱是不是先创建了这个什么配置对象对不对拿着这个配置对象封装了谁啊对服务的地址和名称空间然后把这个配置对象再扔给谁啊扔给这个注册中心从而创建出来这个什么呀注册中心啊所以这个方法比较简单啊咱前面刚写过就不再给大家写了我们直接拿过来用一下
[03:15] 然后呢还有一部分在这我把这个格式稍微调整一下呃大家看一下这是一个方法吗啊init 出手化方法啊加了bin 诸也就证明这个方案的反位值是不是交给sprint进行管理了那它的反位值呢其实就是一个什么呀ZooKeeper注册中心对不对这个代码我就不再说了啊那这是哪个配置类咱就搞定了对这个ZooKeeper的这个配置类我们就搞定搞定完之后呢我们需要再增加一块配置
[03:59] 这个配置会稍微麻烦一下是不是elastic job的这个配置类是不是咱看一看讲义往下走elastic job配置这里边呢咱当时在入门案例里边把这个代码基本上一行一行都给大家写了一遍啊这次我就不再从头给你写啊我们一会呢大概回顾一下那咱先把这个类给它创建出来啊还是放到这个job包里边然后呢我们在这加上configuration的这个注解
[04:38] 加上这个注解之后呢我们回顾一下我们之前说过在这个elastic job的配置当中呢我们是不是需要需要干什么呀需要注入好多东西对吧比如注入那个任务类就这个recommend job因为他需要知道任务类是谁从而去down is killed的方法是不是就触发这个功能的这个执行了对不对所以我们需要注入这个谁啊对需要注入这个任务类还需要注入啥
[05:07] 还需要注入注册中心啊组keeper注册中心这不用说然后呢就是还有两个值对吧一个是分片总数啊一个是那个谁啊chrome表达是一共有四个值我们需要注入哇这块就拿过来了放到这儿好我们把这个给他导一下包啊导完包之后呢我们接下来是不是还是要编写方法咱回顾一下就行了啊呃他是这么一回事就是
[05:50] 他一开始是要执行了是不是这个初始化方法对不对这个方法最终创建出来一个对象就是这个对象我们说这个对象叫任务调度器是非常非常重要的一个对象这个对象啊就是由他来具体去干什么呀去找到这个谁啊任务类啊找到这个任务类然后去执行isq的方法从而触发整个定时任务的一个什么呀对一个运行
[06:18] 所以说我们最终的目的就是把这个对象给创建出来这个对象怎么创建呢你看这儿是不是直接Nu出来了直接NuNu的时候你看它要三个参数第一个参数就是任务类第二个参数就是组Keeper注册中心第三个参数有点复杂是一个配置对象这个配置对象咱当时在入门案例的时候说过创建起来有点麻烦是不是所以咱在上面是不是单独封装了一个方法叫Create Job Configuration是不是你看
[06:47] 就这个方法就这个方法最终呢我们就是要得到这么一个叫light job configuration这么一个配置对象这个配置对象里边我们要封装的比如说就有这个什么呀crumb辩答式啊那个那个什么呀分片总说啊对吧这也指我们就要封装到这个配置对象里啊那这个对象怎么创建呢就有点麻烦了他的API是一层靠一层是不是我们首先要创建出来一个builder对象就是构造器对象他不是new了对不对通过这个
[07:19] 静态方法new builder创建出来一个构造器对象这里边有什么呀任务类的名字科研表辑还有分片总算你看这儿其实都已经进行封装然后再通过这个builder对象的build方法是不是创建出来一个配置对象但是这个配置对象呢是一个基础的配置对象那这个基础配置对象创建出来之后呢我们再拿上它还有这个什么呀
[07:45] 任何类的名字扔给这个什么呀simple job configuration最终呢就把这个simple job configuration这个对象给创新出来但这个呢仍然不是我们最终想要但是基本上已经差不多了你看接下来把这个又扔给谁啊扔给light job configuration的new builder方法然后呢最终调build方法是不是把这个谁啊我们最终想要的light job configuration这么一个配置对象就创新了
[08:17] 创业出来之后呢我们是不是一调用这个方法当然是在这调用了一调用这个方法最终是不是就得到这么一个配置对象嘛是不是这就是第三个参数然后最终呢就把这个什么呀任务调度器这个对象给创业出来它只要一存在那么它就会看着那个什么呀定时策略比如说每个五秒钟哎它就去干什么呀找到这个谁呀
[08:41] 对找到这个任务对象或者任务类对不对去执行这个什么呀is cute方法哎他们之间是大概这么一个联系啊那接下来的话我这块代码我就不再给大家编写了呃入门案里边刚写过这个代码基本上是没有啥变化的都是固定写法虽然多啊但是都是固定写法在这儿对吧一块全给他粘过来了我们稍微调整一下格式
[09:28] 这个代码的话我建议你在入门案例当中你要是有时间可以敲一敲然后到这儿的话你只要知道这其实就是ElasticJob的一堆什么呀对一堆API你只要知道这些代码是干啥的就可以了这是目前吧这还有个错对不对多个大我号这是目前吧咱们把ElasticJob的这个配置类也搞定了那
[09:55] 它再加上这个组KPRO的这个配置类就完全可以去触发什么呀对我们定时还款这个什么呀那咱一会儿是不是就可以进行什么呀对进行功能测试

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何配置和使用分布式任务调度框架（如 ElasticJob）结合 Zookeeper 和 Apollo 实现分片任务的注册与执行。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 RepaymentJob 类的源码，其中重写了 execute 方法，用于执行还款业务逻辑，调用 repaymentService 的 executeRepayment 方法。
画面 2: 同画面 1，鼠标光标移动到 execute 方法的注释“//使用业务层执行任务”。
画面 3: 展示了 ZKRegistryCenterConfig 类的源码，用于配置 Zookeeper 注册中心，包含 ZOOKEEPER_CONNECTION_STRING 和 JOB_NAMESPACE 两个属性。
画面 4: 展示了多个服务窗口的切换，包括 adminservice、ApolloPortal、configservice 等，用于说明服务注册与配置管理。
画面 5: 同画面 3，继续展示 ZKRegistryCenterConfig 类的源码。
画面 6: 展示了 ZKRegistryCenterConfig 类中创建 ZookeeperConfiguration 实例的代码。
画面 7: 展示了 PPT 页面，标题为“7.3 功能测试”，内容说明由于分片总数设置为 2，需要启动两个还款服务，端口号分别为 53081 和 53082。
画面 8: 展示了 RepaymentJob 类的源码，与画面 1 相同。
画面 9: 展示了 ElasticJobConfig 类的源码，其中导入了 org.springframework.context.annotation.Configuration 和 org.springframework.beans.factory.annotation.Autowired 注解，并定义了 JobCoreConfigurationBuilder。
画面 10: 同画面 7，展示 PPT 页面“7.3 功能测试”。
画面 11: 展示了 PPT 页面“7.3 功能测试”的内容，说明需要启动两个还款服务。
画面 12: 展示了 ElasticJobConfig 类中创建 LiteJobConfiguration 的代码。
画面 13: 展示了 ElasticJobConfig 类中创建 LiteJobConfiguration 的代码，其中包含 JobCoreConfigurationBuilder 的构建过程。
画面 14: 展示了 ZKRegistryCenterConfig 类的源码，与画面 3 和 5 相同。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

@Component
public class RepaymentJob implements SingleJob {

    @Autowired
    private RepaymentService repaymentService;

    @Override
    public void execute(ShardingContext shardingContext) {
        //使用业务层执行任务
        repaymentService.executeRepayment(LocalDate.now().format(DateTimeFormatter.ISO_LOCAL_DATE), shardingContext.getShardingItem());
    }
}
```

画面 3:
```java
@Configuration
public class ZKRegistryCenterConfig {

    //ZooKeeper服务地址
    @Value("${pzp.ZooKeeper.comString}")
    private String ZOOKEEPER_CONNECTION_STRING ;

    //定时任务命名空间
    @Value("${pzp.job.namespace}")
    private String JOB_NAMESPACE;

    //创建注册中心
    @Bean(initMethod = "init")
    public ZookeeperRegistryCenter setUpRegistryCenter(){
        ZookeeperConfiguration zookeeperConfiguration = new
                ZookeeperConfiguration(ZOOKEEPER_CONNECTION_STRING, JOB_NAMESPACE);
        ZookeeperRegistryCenter zookeeperRegistryCenter = new
                ZookeeperRegistryCenter(zookeeperConfiguration);
        return zookeeperRegistryCenter;
    }
}
```

画面 6:
```java
//创建注册中心
@Bean(initMethod = "init")
public ZookeeperRegistryCenter setUpRegistryCenter(){
    ZookeeperConfiguration zookeeperConfiguration = new
            ZookeeperConfiguration(ZOOKEEPER_CONNECTION_STRING, JOB_NAMESPACE);
    ZookeeperRegistryCenter zookeeperRegistryCenter = new
            ZookeeperRegistryCenter(zookeeperConfiguration);
    return zookeeperRegistryCenter;
}
```

画面 9:
```java
@Configuration
public class ElasticJobConfig {

    @Autowired
    RepaymentJob repaymentJob;

    @Autowired
    ZookeeperRegistryCenter registryCenter;

    @Value("${pzp.job.count}")
    private int jobCount;
}
```

画面 12:
```java
//创建SimpleJobConfiguration
SimpleJobConfiguration simpleJobConfiguration = new
        SimpleJobConfiguration(jobClass.getCanonicalName(), jobClass.getCanonicalName());
//创建LiteJobConfiguration
LiteJobConfiguration liteJobConfiguration = LiteJobConfiguration.
        newBuilder(simpleJobConfiguration).overwrite(true).build();
return liteJobConfiguration;
```

画面 13:
```java
private LiteJobConfiguration createJobConfiguration(final Class<? extends SimpleJob> jobClass,
                                                       final String cron,
                                                       final int shardingTotalCount) {
    //创建JobCoreConfigurationBuilder
    JobCoreConfiguration.Builder jobCoreConfigurationBuilder =
            JobCoreConfiguration.newBuilder(jobClass.getCanonicalName(), cron, shardingTotalCount);
    //创建JobCoreConfiguration
    JobCoreConfiguration jobCoreConfiguration = jobCoreConfigurationBuilder.build();
    //创建SimpleJobConfiguration
    SimpleJobConfiguration simpleJobConfiguration = new
            SimpleJobConfiguration(jobCoreConfiguration, jobClass.getCanonicalName());
    //创建LiteJobConfiguration
    LiteJobConfiguration liteJobConfiguration = LiteJobConfiguration.
            newBuilder(simpleJobConfiguration).overwrite(true).build();
    return liteJobConfiguration;
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 7:
标题：7.3 功能测试
内容：由于分片总数设置为2，所以这里需要再配置一个还款服务，端口号是53081，最终一共要启动两个还款服务。

5) 无。

