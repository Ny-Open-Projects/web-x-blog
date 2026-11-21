# 画面线理解：day15-12-定时还款任务-配置类

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-6 实现定时还款任务
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-6 实现定时还款任务\day15-12-定时还款任务-配置类_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 01:02, 01:28, 02:04, 02:44, 03:48, 04:15, 04:51, 05:36, 06:17, 08:25, 09:06, 09:38, 09:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:37:27

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

    //zookeeper服务地址
    @Value("${pzp.zookeeper.comString}")
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
