# 27.Nacos-配置管理-扩展配置

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\27.Nacos-配置管理-扩展配置【海量资源尽在 666java.com】.mp4
- 时长 8分7秒（音频 487s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们学习一下自定义扩展配置因为我们知道啊一个项目呢它不仅有一个组配置文件嗯它还有很多配置文件那么这时候我们怎么样来扩展我们的配置呢比如举个例子啊比如我们这个项目呢它有一个组配置文件但是多个项目呢它可能公用一些配置文件这时候怎么做这时候我们就需要扩展我们的这个配置
[00:27] 扩展配置的方法呢我们用这个EXT-configure素组的这种方式来进行扩展比如我给大家举个例子就知道了那下边呢我们想扩展配置我们怎么扩展呢我们在下边的这个什么配置configure这个标签下我们定义一个叫做EXT-configure
[00:51] 注意它是素组形式它的下标从0开始下标从0开始所以这里边我们想配置一个什么具体的配置文件比如我们要首先指定Data ID对吧指定Data ID那么指定完Data ID那你是不是就要指定具体的配置文件的名称好我们根据这个讲义来现在我们准备在哪里准备在还是这个public这个命名空间我们定义一个看好
[01:20] 好那么这个是一个我们把它定义为一个公用的配置是吧所以呢我们给它起一个独立的组名叫group叫common group好吧然后呢它的这个配置文件的内容呢我们按照讲义上来叫看好啊叫什么呢叫common name看好啊叫commonyml嘛name张三然后呢它的地址我们叫北京行吧
[01:53] 好这个配置文件有时候老师那你这个配置文件的意义是啥最后我们会读取这个配置文件的内容啊我们一会测一下现在我们先配可以吧然后呢我们再按照讲义上来我们再配一个配置文件因为我们说扩展嘛我们可能扩展多个配置文件对不对所以这里面我们再讲好那这个还是我们叫common行吗好那么他的这个内容呢和刚才内容差不多但是呢我们给他换个名看好啊我们给他换个名
[02:23] 我们叫刚才是不是叫common name刚才张三是吧现在李四ADDR然后呢刚才是北京是吧现在郑州看好我现在这两个配置文件是不是都配上了并且这个组是不是就是common group我定了两个配置文件那么我们现在需要我们的应用程序去引用这两个配置文件那么怎么引用是不是就在这里我们写上它对不对然后呢
[03:02] data id是不是指定配置文件的名称下面是不是应该还有一个叫什么是不是有一个叫group对不对group那这个group是不是就是我们刚才定义的叫common group对不对然后还有一点当配置文件更新的时候我们是否立即刷新呢对我们如果把这个refresh把它写成一个true那就表示当配置文件更新就立即刷新按照同样的规则看好
[03:31] 然后我们再继续配置另外一个那这个是不是就是我们说的02啊跟刚才的配置文件的名称要对上啊你看是不是就是它看到了吗现在这个扩展呢我就扩展完了那扩展完了之后呢各位我们发布也发布成功了现在我是不是要获取配置了看我怎么获取啊看好啊我这里面要获取嗯比如这里面呢我们准备呃这么弄行吧这样写可以吧然后呢再来一个
[04:06] 那么这样的话我们准备获取哪个呢一个内幕还有一个地址ADDR行吧最后呢我们把这个内幕加ADDR行不行我们把它返回OK现在呢我们把它重启一下大家需要观察的是看看我能不能把这个扩展配置文件里面的信息获取到对不对来看一下好那现在呢我们仍然是访问这个链接刷新大家看到有吗
[04:37] 有了但是好像好像有点乱对吧跟我们的预期好像不太一样啥意思看好啊我们把它我们把它加一个隔离好前面是不是获取的内幕属性下后面是不是ADDR属性啊那其实通过这个测试你会发现前边一部分获取到这个内幕属性其实这个信息来源于哪里啊是不是来源于我们组配置文件它里边的这个application1convector大家能看懂吧
[05:07] 而后边这个郑州这个词语它是不是获取的地址啊那它来源于谁啊它是不是来源于common02这个配置文件里边的这个什么这个属性值啊各位我们获取内幕它为什么没有把这个李四对吧没有把张三获取到反而是把主配置文件里边的这个什么这个内幕的值获取到了大家猜一下什么原因啊什么原因
[05:34] 对这就是我们说的你使用了扩展配置这里边就有一个什么优先级的问题那么优先级这里边我要跟大家说一下就是为什么最后扩展配置我有两个扩展配置文件为什么获取郑州因为它的优先级是以什么呀是以这个宿主的下标越大这个优先级又越高
[05:59] 也就是说现在我们这两个配置文件你会发现一个是01一个是0202在我们的配置当中它的下标各位是不是就是ext-configure1这个下标是不是要大于0它对应的是不是0202里边的配置信息要干嘛要优先于什么01里边换句话说也就是01和02里边有相同的配置02会覆盖01理解吗
[06:26] 因为01和02是不是都有这个都有这个ADDR的这个属性所以由于02的优先级比01高所以呢02就覆盖了01所以你这里边看到的是郑州对吧那有时候老师那为啥会这个取到的是主配置文件里边的这个内幕值这个这个扩展配置文件的内幕没有取到呢那其实同理嘛那当主配置文件和扩展配置文件都存在的时候主配置文件的优先级最高也就是说什么意思啊
[06:56] 也就是说当组配置文件和扩展配置文件里边有相同的属性那么组配置文件会干嘛会覆盖扩展配置文件里边的这些属性值所以它会把组配置文件里边的内部属性值取到而扩展里边的内部值取不到大家理解了吗对这就是我们说的什么自定义扩展配置所以大家一定要注意它的一个优先级的问题优先级的问题好那到这儿
[07:26] 自定义扩展配置的演示呢就完成了大家知道具体的具体的整个的这个配置的方法其实就是采用eit-configure输组配置方式从零开始从零开始你千万不要这里边写一个1这写一个2懂吧这要从零开始啊好另外刚才我们也说了优先级的问题对吧下标越大的这个配置文件的优先级比下标小的配置文件优先级高那么这个
[07:53] 组配置文件也就是通过application name加扩展名所拿到的这个配置文件它的优先级最高好那到这这个扩展配置的演示呢我们就演示完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Nacos 中配置和使用多数据源（ext-config）来管理不同服务的配置文件，并在 Spring Cloud 应用中读取这些配置。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了项目结构，重点在 `bootstrap.yml` 文件中配置了 Nacos 服务发现和负载均衡，以及 `ext-config` 配置项。
画面2: PPT 页面，讲解了通过 `spring.cloud.Nacos.config.ext-config[n].data-id` 和 `group` 属性来管理多个配置文件。
画面3: Nacos 界面，新建配置，Data ID 为 `ext-config-common01.yaml`，Group 为 `COMMON_GROUP`。
画面4: Nacos 界面，配置 `ext-config-common01.yaml`，内容为 `name: zhangsan` 和 `addr: beijing`。
画面5: 项目中 `bootstrap.yml` 文件，配置了 `ext-config[0]` 使用 `ext-config-common01.yaml`。
画面6: 项目中 `bootstrap.yml` 文件，配置了 `ext-config[1]` 使用 `ext-config-common02.yaml`。
画面7: 代码中 `RestConsumerController`，使用 `@Value("${common.name}")` 注入配置值。
画面8: 控制台输出，显示服务已启动并注册到 Nacos。
画面9: Nacos 界面，显示了已配置的多个配置文件，包括 `ext-config-common01.yaml` 和 `ext-config-common02.yaml`。
画面10: PPT 页面，讲解了 `ext-config` 配置不支持多个 `data-id` 的情况。
画面11: 控制台输出，显示服务已启动并注册到 Nacos。
画面12: PPT 页面，再次强调 `ext-config` 配置不支持多个 `data-id`，但可以通过 `group` 属性自定义组。
画面13: Nacos 界面，配置 `ext-config-common02.yaml`，内容为 `name: zhangsan` 和 `addr: beijing`。
画面14: 项目中 `bootstrap.yml` 文件，配置了 `ext-config[0]` 和 `ext-config[1]` 分别指向 `ext-config-common01.yaml` 和 `ext-config-common02.yaml`。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1:
```yaml
name: Nacos-RESTful-consumer
#服务名
cloud:
  Nacos:
    discovery:
      server-addr: 127.0.0.1:8848 #服务发现中心地址
      namespace: 1f5ec8a1-1f05-10cd-961a-8414f312a204 #指定命名空间的id
    config:
      server-addr: 127.0.0.1:8848 #配置中心地址
      file-extension: yaml #指定配置文件的扩展名，配置文件名称根据application.name的名称拼接，为Nacos-RESTful-consumer.yaml
      ext-config[0]:
        data-id: ext-config-common01.yaml
        group: COMMON_GROUP
        refresh: true
      ext-config[1]:
        data-id: ext-config-common02.yaml
        group: COMMON_GROUP
        refresh: true
```

画面2:
```yaml
cloud:
  config:
    server-addr: 127.0.0.1:8848 # 配置中心地址
    file-extension: yaml
    # namespace: 1f5ec8a1-1f05-10cd-961a-8414f312a204 # 开发环境
    # config external configuration
    # 1. Data Id group: 组名,refresh: 动态刷新
    ext-config[0]:
      data-id: ext-config-common01.yaml
      group: COMMON_GROUP
      refresh: true
    ext-config[1]:
      data-id: ext-config-common02.yaml
      group: COMMON_GROUP
      refresh: true
```

画面3:
Data ID: ext-config-common01.yaml
Group: COMMON_GROUP

画面4:
配置ext-config-common01.yaml :
Data ID: ext-config-common01.yaml
Group: COMMON_GROUP
配置格式: YAML
配置内容:
```yaml
common:
  name: zhangsan
  addr: beijing
```

画面5:
```yaml
name: Nacos-RESTful-consumer
#服务名
cloud:
  Nacos:
    discovery:
      server-addr: 127.0.0.1:8848 #服务发现中心地址
      namespace: 1f5ec8a1-1f05-10cd-961a-8414f312a204 #指定命名空间的id
    config:
      server-addr: 127.0.0.1:8848 #配置中心地址
      file-extension: yaml #指定配置文件的扩展名，配置文件名称根据application.name的名称拼接，为Nacos-RESTful-consumer.yaml
      ext-config[0]:
        data-id: ext-config-common01.yaml
        group: COMMON_GROUP
        refresh: true
```

画面6:
```yaml
name: Nacos-RESTful-consumer
#服务名
cloud:
  Nacos:
    discovery:
      server-addr: 127.0.0.1:8848 #服务发现中心地址
      namespace: 1f5ec8a1-1f05-10cd-961a-8414f312a204 #指定命名空间的id
    config:
      server-addr: 127.0.0.1:8848 #配置中心地址
      file-extension: yaml #指定配置文件的扩展名，配置文件名称根据application.name的名称拼接，为Nacos-RESTful-consumer.yaml
      ext-config[0]:
        data-id: ext-config-common01.yaml
        group: COMMON_GROUP
        refresh: true
      ext-config[1]:
        data-id: ext-config-common02.yaml
        group: COMMON_GROUP
        refresh: true
```

画面7:
```java
@Value("${common.name}")
private String common_name;

@Autowired
ConfigurableApplicationContext applicationContext;

@GetMapping(value = "/configs")
public String getValue() {
    String name = applicationContext.getEnvironment().getProperty("common.name");
    String addr = applicationContext.getEnvironment().getProperty("common.addr");
    return name+addr;
}
```

画面8:
```text
2019-11-28 20:54:35.195 INFO 7392 --- [TaskScheduler-1] a.r.c.n.NacosServiceMetadataRepository : Current application will subscribe all services(size: 0)
2019-11-28 20:54:35.212 INFO 7392 --- [TaskScheduler-1] a.r.c.n.NacosServiceMetadataRepository : Current application will subscribe all services(size: 0)
ServiceBootstrap: 0 classes reloaded
SpringRestConsumerBootstrap: 0 classes reloaded
SpringRestConsumerBootstrap: 0 classes reloaded
SpringRestConsumerBootstrap: 0 classes reloaded
```

画面9:
Data ID: Nacos-RESTful-consumer.yaml
Group: DEFAULT_GROUP
Data ID: ext-config-common01.yaml
Group: COMMON_GROUP
Data ID: ext-config-common02.yaml
Group: COMMON_GROUP

画面10:
```yaml
application:
  name: service2
cloud:
  Nacos:
    config:
      server-addr: 127.0.0.1:8848 # 配置中心地址
      file-extension: yaml
      namespace: 1f5ec8a1-1f05-10cd-961a-8414f312a204 # 开发环境
      # config external configuration
      # 1. Data Id group: 组名,refresh: 动态刷新
      ext-config[0]:
        data-id: ext-config-common01.yaml
        group: COMMON_GROUP
        refresh: true
      ext-config[1]:
        data-id: ext-config-common02.yaml
        group: COMMON_GROUP
        refresh: true
```

画面11:
```text
2019-11-28 20:55:35.203 WARN 7392 --- [TaskScheduler-1] a.r.c.n.NacosServiceMetadataRepository : Current application will subscribe all services(size: 0)
2019-11-28 20:55:35.212 WARN 7392 --- [TaskScheduler-1] a.r.c.n.NacosServiceMetadataRepository : Current application will subscribe all services(size: 0)
ServiceBootstrap: 0 classes reloaded
SpringRestConsumerBootstrap: 0 classes reloaded
SpringRestConsumerBootstrap: 0 classes reloaded
SpringRestConsumerBootstrap: 0 classes reloaded
```

画面12

