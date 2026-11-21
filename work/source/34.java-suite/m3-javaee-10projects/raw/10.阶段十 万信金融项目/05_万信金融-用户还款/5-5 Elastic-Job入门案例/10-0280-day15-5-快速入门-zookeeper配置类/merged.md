# day15-5-快速入门-zookeeper配置类

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-5 Elastic-Job入门案例
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-5 Elastic-Job入门案例\day15-5-快速入门-zookeeper配置类_【海量资源尽在 666java.com】.mp4
- 时长 7分35秒（音频 456s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把elastic-job的任务类给搞定了在这个任务类当中我们是不是具体实现了分片查询数据的这个什么呀任务对吧但是这个任务怎么去触发执行我们是还需需要干什么呀需要两大块配置第一大块配置就是咱接下来要搞租keeper什么呀注册中心哎前面我们说过啊
[00:24] Zookeeper呢它是类似于什么呀Eureka是一个微服务注册与管理中心那你将来启动的所有的这个微服务全部都要注册到这个什么呀对Zookeeper这个注册中心里边那现在这个注册中心存在吗还不存在呢对不对还不存在呢所以说我们需要搞一个配置类把这个注册中心呢给它创建出来那有了这个Zookeeper这个注册中心之后我将来我们这个例子当中是不是我要启动几个服务器
[00:56] 我学说了老师我哪知道你起几个呀哎你别忘了啊我们刚才搞了一个配置啊这个分片总算是几啊三三就意味着我要起几台服务器啊三台服务器那我启动这个三台服务器将来都要往哪注册呀对Zookeeper这个注册中心进行注册注册完之后呢哎我们利用Zookeeper内部的选举机制对不对会选出来一个leader由他负责进行什么呀分片就行
[01:22] 那咱们先来把这个配置类给整一整吧我们需要新建一个类叫ZK Reductor Center Configure这个名字比较长但这个名字是可以随便起来我们放到Configure这个包里边新建一个类名字就叫这名然后呢这是一个配置类对吧加上注解CONFI Configuration好咱们先来看看讲义这个配置稍微有点多啊
[01:52] 那这个注册中心呢其实说白了我们在下边大家看一下是不是直接NU出来NU是吧Zookeeper Register Center这不注册中心吗直接NU但是你要造一个注册中心的话你得告诉他你这个Zookeeper的这个服的这个什么地址啊对吧还有你要用哪个什么呀名称空间啊是不是这是最基本的信息对不对那这些值在哪放着呢大家应该有印象这些值我是不是就放到这个配置文件里边是不是他俩
[02:22] 对不对你要造一个注册中心哎这个你得知道啊ZooKeeper他这个服务的IP地址端口号还有这个名称空间那因此我是不是需要把这两个值先注入到这个什么呀对配置类当中啊一个一个来吧第一个我要注入的就是ZooKeeper的这个什么呀对服务器地址那我先声明一个属性吧private其个名字叫tree这个名字咱跟你讲一保持一致吧他应该是
[02:56] 全大写然后呢我们通过哪个注解进行注注对add value里边是不是要写一个表达是dollar什么呀大股号然后大股号里边写啥大股号这个值你可不能随便乱写是不是应该写配种件里边等号前的这个什么呀件对不对写件取的就是他的这个什么呀值等号后面的值大家看是这么写的吧然后我们再取一个再取的就是那个什么呀
[03:32] 对这个定时任务的名称空间名称空间我也要声明一个属性来存储名字呢跟讲义保持一致叫叫宝Name Space然后呢它的值呢也要通过Add Value注解给它拿到那里边的这个我们要从这儿是不是粘一下是不是我们为了创建这个注册中心呢我们需要
[04:10] 拿到这两个值现在这两个值已经有了接下来的话咱就开始去创建这个什么样注册中心怎么创建呢大家看我们单独写了一个方法那咱看看这个方法吧反位值是不是就是那个那个注册中心那个类啊那个类的一个对象嘛然后发二名无所谓的然后没有参数那这里边特别特别大家要注意的是这个发什么加了这么一个注解at b at b 啥意思at b 是吧你看这个发最终是不是要返回这个类型的一个对象是不是
[04:41] 那么这个对象呢我们将来是不是交给sprint进行管理了啊然后呢他还是一个什么呀初始化的一个什么样方法这个注解非常非常重要里边代码其实就是两个new就是造两个对象咱把这块呢先拿过来然后里边代码咱一会编写一下我这里边你一定要特别注意上面的这个注解啊并这个注解那这里边咱最终是不是要造这个类的一个对象这个类不就是注册中心吗
[05:10] 那具体咋造呢咱看看讲义他首先是创建一个配置对象你看ZooKeeper什么呀configuration对不对那这个配置对象就是用来封装这个什么呀一个是服务的地址一个是那个什么呀名称空间然后呢我再去new这个什么呀注册中心new注册中心的时候把这个配置对象是不是扔进去完事了就是两个new然后第一个呢其实就是zk的配置是吧zk
[05:39] 配置它有一个类我们直接new直接new我们看它这个类的名字是叫名字都可长ZookeeperConfiguration是它等于newZookeeperConfiguration我们说了要把上面这两个值给它封装进去就行了一个是服务的地址一个是这个名称空间
[06:09] 我们需要把这个两个信息封装到这个什么样配置里这是不是第一个new吗对不对然后接下来我们该进行第二个new了第二个new直接就是创建注册中心了创建注册中心那这个类的名字不就是这个名吗好也是直接new啊new然后呢把谁扔进去对把上面这个配置对一下扔到这里因为他要
[06:49] 通过配置对象里边的这两个值是不是来创建这个什么呀对注册中心这不是创建完了吗创建完你你最后不就是返回业下大家看搞定了没有搞定了所以说呢这个租K帕的这个配置类其实这里边的这个东西不是很多啊不是很多关键的就是这块代码先造一个什么样配置对象啊把这两个数据封装进去然后呢再把这个配置对象扔给这个什么呀这个类最终呢把这个注册中心就
[07:20] 创建出来然后作为反而之返回交给谁啊对spirit进行管理就行了另外一定要注意这个方式一个出入化的一个方法那么到目前为止咱们租keeper相关的这个配置就搞定

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中配置和使用 ElasticJob 分布式任务框架，重点讲解 ZK 注册中心的配置与初始化。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 MyJob 作业类的代码，实现 SimpleJob 接口，用于执行分片任务。
- 代码中包含获取分片总数和当前分片的逻辑。
- 代码中包含查询数据库并打印结果的逻辑。

画面 2：
- 展示了 application.properties 配置文件，包含数据库连接、MyBatis 配置、ZooKeeper 服务地址、作业命名空间、分片总数和调度 Cron 表达式。
- 配置内容：
  spring.datasource.url=jdbc:mysql://localhost:3306/mp?useUnicode=true&characterEncoding=utf8&autoReconnect=true
  spring.datasource.username=root
  spring.datasource.password=123
  mybatis-plus.Mapper-locations = classpath*:dao/*.xml
  mybatis-plus.type-aliases-package = com.ithema.elasticjob.pojo
  ZooKeeper.comString = localhost:2181
  myjob.namespace = elastic-job-example
  myjob.count = 3
  myjob.cron = 0/5 * * * * ?

画面 3：
- 画面内容与画面 2 相同，仅鼠标位置不同。

画面 4：
- 展示了 ZKRegistryCenterConfig 配置类的代码，用于配置和初始化 ZooKeeper 注册中心。
- 代码中包含注解 @Configuration、@Value 注入配置、@Bean 初始化方法。

画面 5：
- 展示了 application.properties 配置文件，内容与画面 2 相同，仅鼠标位置不同。

画面 6：
- 展示了 ZKRegistryCenterConfig 配置类的代码，显示了 Spring 注解的自动补全建议。

画面 7：
- 展示了 ZKRegistryCenterConfig 配置类的代码，显示了 @Value 注解的使用。

画面 8：
- 展示了 application.properties 配置文件，内容与画面 2 相同，仅鼠标位置不同。

画面 9：
- 展示了 ZKRegistryCenterConfig 配置类的代码，内容与画面 4 相同，仅鼠标位置不同。

画面 10：
- 展示了 ZKRegistryCenterConfig 配置类的代码，显示了 Spring 注解的自动补全建议。

画面 11：
- 展示了 ZKRegistryCenterConfig 配置类的代码，显示了 ZookeeperConfiguration 的创建。

画面 12：
- 展示了 ZKRegistryCenterConfig 配置类的代码，显示了 ZookeeperRegistryCenter 的创建。

画面 13：
- 展示了 ZKRegistryCenterConfig 配置类的代码，显示了 ZookeeperRegistryCenter 的创建。

画面 14：
- 展示了 ZKRegistryCenterConfig 配置类的代码，显示了 ZookeeperRegistryCenter 的创建。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1：
```java
@Component
public class MyJob implements SimpleJob {
    @Autowired
    private UserMapper userMapper;

    //执行定时任务
    @Override
    public void execute(ShardingContext shardingContext) {
        //得到分片总数
        int count = shardingContext.getShardingTotalCount();
        //得到分片项
        int item = shardingContext.getShardingItem();
        //查询数据
        List<User> userList = userMapper.queryUserById(count,item);
        //输出结果
        userList.forEach(user -> {
            System.out.println("作业分片:"+item+"--->"+user);
        });
    }
}
```

画面 2：
```properties
spring.datasource.url=jdbc:mysql://localhost:3306/mp?useUnicode=true&characterEncoding=utf8&autoReconnect=true
spring.datasource.username=root
spring.datasource.password=123
mybatis-plus.Mapper-locations = classpath*:dao/*.xml
mybatis-plus.type-aliases-package = com.ithema.elasticjob.pojo
ZooKeeper.comString = localhost:2181
myjob.namespace = elastic-job-example
myjob.count = 3
myjob.cron = 0/5 * * * * ?
```

画面 4：
```java
@Configuration
public class ZKRegistryCenterConfig {
    //ZooKeeper服务地址
    @Value("${ZooKeeper.connString}")
    private String ZOOKEEPER_CONNECTION_STRING;

    //定时任务命名空间
    @Value("${myjob.namespace}")
    private String JOB_NAMESPACE;

    //zk的配置及创建注册中心
    @Bean(initMethod = "init")
    public ZookeeperRegistryCenter setupRegistryCenter(){
        //zk的配置
        ZookeeperConfiguration zookeeperConfiguration = new
                ZookeeperConfiguration(ZOOKEEPER_CONNECTION_STRING,
                JOB_NAMESPACE);
        //创建注册中心
        ZookeeperRegistryCenter zookeeperRegistryCenter = new
                ZookeeperRegistryCenter(zookeeperConfiguration);
        return zookeeperRegistryCenter;
    }
}
```

画面 6：
```java
@Configuration
public class ZKRegistryCenterConfig {
    //ZooKeeper服务地址
    @Value("${ZooKeeper.connString}")
    private String ZOOKEEPER_CONNECTION_STRING;

    //定时任务命名空间
    @Value("${myjob.namespace}")
    private String JOB_NAMESPACE;

    //zk的配置及创建注册中心
    @Bean(initMethod = "init")
    public ZookeeperRegistryCenter setupRegistryCenter(){
        //zk的配置
        ZookeeperConfiguration zookeeperConfiguration = new
                ZookeeperConfiguration(ZOOKEEPER_CONNECTION_STRING,
                JOB_NAMESPACE);
        //创建注册中心
        ZookeeperRegistryCenter zookeeperRegistryCenter = new
                ZookeeperRegistryCenter(zookeeperConfiguration);
        return zookeeperRegistryCenter;
    }
}
```

画面 10：
```java
@Configuration
public class ZKRegistryCenterConfig {
    //ZooKeeper服务地址
    @Value("${ZooKeeper.connString}")
    private String ZOOKEEPER_CONNECTION_STRING;

    //定时任务命名空间
    @Value("${myjob.namespace}")
    private String JOB_NAMESPACE;

    //zk的配置及创建注册中心
    @Bean(initMethod = "init")
    public ZookeeperRegistryCenter setupRegistryCenter(){
        //zk的配置
        ZookeeperConfiguration zookeeperConfiguration = new
                ZookeeperConfiguration(ZOOKEEPER_CONNECTION_STRING,
                JOB_NAMESPACE);
        //创建注册中心
        ZookeeperRegistryCenter zookeeperRegistryCenter = new
                ZookeeperRegistryCenter(zookeeperConfiguration);
        return zookeeperRegistryCenter;
    }
}
```

画面 11：
```java
@Configuration
public class ZKRegistryCenterConfig {
    //ZooKeeper服务地址
    @Value("${ZooKeeper.connString}")
    private String ZOOKEEPER_CONNECTION_STRING;

    //定时任务命名空间
    @Value("${myjob.namespace}")
    private String JOB_NAMESPACE;

    //zk的配置及创建注册中心
    @Bean(initMethod = "init")
    public ZookeeperRegistryCenter setupRegistryCenter(){
        //zk的配置
        ZookeeperConfiguration zookeeperConfiguration = new
                ZookeeperConfiguration(ZOOKEEPER_CONNECTION_STRING,
                JOB_NAMESPACE);
        //创建注册中心
        ZookeeperRegistryCenter zookeeperRegistryCenter = new
                ZookeeperRegistryCenter(zookeeperConfiguration);
        return zookeeperRegistryCenter;
    }
}
```

画面 12：
```java
@Configuration
public class ZKRegistryCenterConfig {
    //ZooKeeper服务地址
    @Value("${ZooKeeper.connString}")
    private String ZOOKEEPER_CONNECTION_STRING;

    //定时任务命名空间
    @Value("${myjob.namespace}")
    private String JOB_NAMESPACE;

    //zk的配置及创建注册中心
    @Bean(initMethod = "init")
    public ZookeeperRegistryCenter setupRegistryCenter(){
        //zk的配置
        ZookeeperConfiguration zookeeperConfiguration = new
                ZookeeperConfiguration(ZOOKEEPER_CONNECTION_STRING,
                JOB_NAMESPACE);
        //创建注册中心
        ZookeeperRegistryCenter zookeeperRegistryCenter = new
                ZookeeperRegistryCenter(zookeeperConfiguration);
        return zookeeperRegistryCenter;
    }
}
```

画面 13：
```java
@Configuration
public class ZKRegistryCenterConfig {
    //ZooKeeper服务地址
    @Value("${ZooKeeper.connString}")
    private String ZOOKEEPER_CONNECTION_STRING;

    //定时任务命名空间
    @Value("${myjob.namespace}")
    private String JOB_NAMESPACE;

    //zk的配置及创建注册中心
    @Bean(initMethod = "init")
    public ZookeeperRegistryCenter setupRegistryCenter(){
        //zk的配置
        ZookeeperConfiguration zookeeperConfiguration = new
                ZookeeperConfiguration(ZOOKEEPER_CONNECTION_STRING,
                JOB_NAMESPACE);
        //创建注册中心
        ZookeeperRegistryCenter zookeeperRegistryCenter = new
                ZookeeperRegistryCenter(zookeeperConfiguration);
        return zookeeperRegistryCenter;
    }
}
```

画面 14：
```java
@Configuration
public class ZKRegistryCenterConfig {
    //ZooKeeper服务地址
    @Value("${ZooKeeper.connString}")
    private String ZOOKEEPER_CONNECTION_STRING;

    //定时任务命名空间
    @Value("${myjob.namespace}")
    private String JOB_NAMESPACE;

