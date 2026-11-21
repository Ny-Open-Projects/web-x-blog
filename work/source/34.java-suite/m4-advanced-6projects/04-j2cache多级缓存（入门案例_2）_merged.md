# 04-j2cache多级缓存（入门案例_2） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

继续来看咱们J2Cache入门案例

刚才我们是把配置文件两个

一个是application.yml

还有一个是cafony.properties

这两个配置文件已经写完了

接下来我们就可以来编写一个controller

在controller当中来编写一些缓存操作的方法来进行测试

咱们先在这来创建一个包结构

com.it黑码

然后controller

把这个包结构创建一下

然后接下来我们在这来创建一个controller

咱们就叫J2Cache controller

然后我们在这加个注释

这个是测试我们J2Cache缓存相关操作

为了便于访问他

我们可以给他加一个rest controller注解

再加一个request mapping

咱们这个

路径就是-cache

接下来我们来看

在这里边要编写方法

具体我们应该如何来操作我们J2Cache的缓存

那么在这个地方

J2Cache给我们提供了非常核心的一个类

这个类叫做cache channel

那么我们在这个地方

直接把这个cache channel

把它注入一下就可以

把它注进来

通过outware的就可以注进来

那么有的同学可能就有疑问了

那么

我们在这里

在这个地方好像也并没有配置什么东西

对吧

为什么直接加一个outware的就能够注入这个对象

这是因为什么呢

这是因为在咱们这个POM文件当中

我们其实已经导入了他这个stutter

对不对

J2Cache这个stutter

而这个stutter当中

咱们来找一下

他其实已经跟我们注册了相关的这个什么配置类

来找一下

这里面稍微有一点点乱

在这

J2Cache supreme boot starter

对吧

好

在这里边呢

有个meta info

然后呢

这里边是不是有个叫sprint.factories

那么熟悉sprint boot的同学应该都了解

我们项目在启动的时候呢

就会加载到我们这个文件

而在这个文件里边呢

他是不是注册了很多这种

以这种叫做什么呢

auto configuration结尾的这些类

这些这些呢

叫做自动配置类

对不对

他其实本质上起的作用就相当于配置文件

对吧

就相当于我们配置文件

而在这个自动配置类里边

大家可以看到啊

你看他是不是都加了这个注解

configuration注解

那这样的话呢

我们这个类就会被加载到

那么在这个类里边呢

他就已经给我们这个通过bin

是不是注册了这么一个叫做cache channel的对象

这样的话呢

在我们项目启动的时候呢

其实这个cache channel就已经被创建出来了

并且载入了sprint的容器

那么这样的话呢

我们在这个controller这个地方呢

就可以通过autoware的把这个对象是不是直接注入了

这是为什么我们并没有自己去做这些事

对吧

直接加一个autoware的

就能够注入成功

就是因为框架其实已经帮我们做了这些事了

对吧

所以说呢

我们直接把它注入一下就可以

那接下来呢

我们可以简单来了解一下这个类啊

因为呢

我们后边操作主要就是操作它的一些方法啊

这里边呢

都有一些什么方法呢

其实都是关于一些什么呢

关于一些这个缓存操作的方法

当然大家可以看到这个地方的是一个抽象类

对吧

实际上我们真正注入的是它的子类啊

那么我们引用的时候呢

就引用副类就可以通过副类来引用啊

然后回到这个catch channel

我们来看一下

它这里边都有什么样的方法呢

来看

这个是get

get的方法是不是就是获取缓存数据

那么获取的时候呢

需要我们传过来什么呢

region

这个region我们刚才解释了

它代表的是区域对不对

比如说我们在这定义的default

默认区域还有rx

这是我们自定义的区域

就指定啊

从哪个区域是不是来获取数据

然后呢

仅仅是指定区域还不够

还要指定一个key

还要指定一个key

对不对

因为我们这个缓存数据呢

是以这种key value形式存储的

所以说呢

你要获取某个数据需要指定key

但是后边呢是可变长度的

这个暂时先不考虑

最重要的就是前面这两个

一个是区域对吧

从哪个区域

然后呢

获取哪个key所对应的value

这是get的方法

获取缓存数据

但是get的方法呢

有好几个重载的

你看都叫get

它就是参数啊

或者是返回值类型不一样

那么都是啊

这些都是

获得

这个缓存数据的对吧

然后呢

这个exist呢

这个是不是判断缓存数据是否存在

对吧

那么你需要传给我

哪个区域的哪个key

缓存数据

对应的缓存数据是否存在

如果返回true的话呢

那就表示存在啊

它是返回一个boot类型

然后呢

接下来这个方法呢

叫做check对吧

check字面翻译呢

是不是应该叫做检查对吧

这个指的就是什么呢

检查某个缓存数据啊

它是存在于第一级缓存

也就是level1还是level2当中

如果说在第一级缓存

当中呢

它就会返回一个1

你看它是不是返回int类型啊

如果是在一级缓存当中

它就会返回1

否则的话呢

它就会返回2

这个是检查

下面是set

set的话

这是我们用的也是非常多的

是不是就是将数据载入缓存

对不对

放到缓存中

那么放入进去之后呢

放入进去的时候呢

需要来指定什么呢

region

区域

还有key

还有value

set的方法呢

也有多个啊

重载的方法

好

这都是set的方法

这些都是set的方法

对吧

然后再往下呢

我们来看

这个呢叫做evaked

evaked呢

其实是缓存清理的方法

对不对

缓存清理

然后下一个呢是clear

也是清理缓存

那么它们之间有什么区别呢

这个evaked呢

它是清理指定缓存

你看是不是需要指定key啊

需要指定region

而这个clear呢

只需要指定region

不需要指定key

那就意味着什么呢

它会把这个region

区域下边

所有的缓存数据

全给清理掉

好

这是clear

然后呢

这个是evaked

那么这么两个缓存清理的方法

好

这是咱们大概过一下

这是catch channel

这个类里边呢

给我们提供了一些

缓存操作的方法

对吧

所以说我们在这个地方呢

要操作缓存数据

主要呢

用的最多的

就是这个对象

叫做catch channel对象

好

简单了解一下它就可以

好

那接下来呢

我们就需要来编写一个方法

这个方法呢

我们就来测试一下什么呢

咱们

先从这个缓存里面来get

对吧

获得一些数据

那么如果获取不到

我们就干什么呢

就模拟啊

从数据库里面查数据

然后呢

查出来数据之后呢

再把这个数据重新载入缓存

大概是这么一个操作

好

那接下来呢

我们来看一下

咱们返回值呢

返回个例子的

好

这个地方有点问题

返回一个例子的

然后这个方法呢

方法名就叫做get

什么呢

catch data

可以吧

获得缓存数据

先retain一个now

好

好

然后呢

下面呢

来加一个什么呢

get mapping

咱们这个路径呢

就跟这个方法名呢

保持一致就可以了

这样

这个方法呢

我们也给它加一个注释吧

加一个注释

这个呢

就是从我们的这个

J2 catch

中来获取什么呢

缓存数据

获取缓存数据

好

那在这儿的话呢

咱们是不是就可以

直接来调我们这个方法了

刚才我们看到

catch channel对象里边

是不是有一个叫做

get的方法呢

就是获得缓存数据的方法

get

你看

第一个参数呢

是region

区域

第二个参数呢

就是keys

我们可以指定什么样

根据某个key来获得

对吧

这个region呢

我们就叫Rx吧

Rx

你看

咱们在这儿是不是

已经定义了这么一个region

好

然后呢

第二个参数是什么呢

是key

这个key的话呢

比如就叫city

city

好

然后它的返回值

是一个什么呢

叫做catch object

catch object

catch object的对象

当然了

我们如果第一次调用这个方法

对吧

那么它肯定是获取不到的

因为我们现在还没有给它去载入缓存

所以你直接获取缓存

它肯定是没有数据的

那么没有数据怎么办呢

所以我们在这儿来判断一下

catch object.get value

这就是获得缓存数据

然后呢

如果等于

now

也就是说

我们获得那个缓存数据

它是封装到这个value里边

并不是这个catch object的对象里边

它是在这个value里边

所以我们可以说是

所以说我们get value

如果value等于空

那就说明什么呢

说明没有获取到缓存数据

这个地方呢

没有获取到缓存数据

那么这个时候呢

我们需要什么呢

从我们的数据库中来查询数据

对不对

从数据库里面来查询数据

这是我们一般的做法

先从缓存里面来获取

没有的话再查数据库

大概是这么一个过程

当然了我们这个地方呢

其实重点呢

是讲解缓存的操作

所以数据库

这块呢

我们就简单模拟一下就可以了

就不再真的去操作数据库了

那怎么办呢

我们可以在这儿

自己来造一个假数据

对吧

假设就是从数据库里面

这个查出来了

这个假设就是从数据库里面

查出来这么一个数据

封装成了一个粒子的集合

比如就叫data吧

release的

用出来

然后呢

我们data.add

好

.add

这个呢

比如说是北京

好

打这个

你先要知道

几个字都可以啊

这都没有关系啊

add

这个是南京

好

data.add

咱们再add一个就可以了

上海

是吧

好

那么把这个数据呢

把它造好

假设这就是从数据库里面查出来的数据

封装好了

对吧

那接下来呢

我们就可以干什么呢

将我们从这个数据库中获取的数据

是不是载入什么呢

我们的缓存

对吧

载入缓存

刚才我们也看了

在这个j2

在这个catchchannel里边呢

是不是给我们提供了各种各样的set方法

对吧

就是用来将这个数据啊

把它载入缓存的

所以我们在这儿呢

就可以直接还是使用这个catchchannel对象

它的一个什么呢

set方法

你看咱们直接调第一个方法就可以啊

这是最简单的

传出什么呢

region

区域

然后key

还有value

好

这个region的话呢

就是rx呗

然后key的话呢

是不是就是city了

value呢

就是我们这个data

其实就是这个粒子的集合

对不对

好

这样的话就表示我们把数据呢

载入缓存

载入缓存之后呢

咱们是不是就可以啊

就可以把这个什么呢

return

就可以把我们这个data呢

返回了

把这个data返回了

你看因为我们最终这个方法是不是需要返回这个数据

这个数据呢

不管你是从数据库里面查出来的

还是从缓存里面查出来的

对吧

最终的需要给到我们的这个调用端

对吧

一般就是前端会调我们的方法

这个呢

我们写的是if这个分支

对不对

写的是if这个分支

那么if它这个get value啊

它等于

no

就是没有缓存数据的时候

是不是走这个分支

那么如果获取到了呢

获取到之后呢

我们是不是直接给它返回就可以了

所以我们这个地方呢

就可以直接什么呢

catch object

还是点get value

get value

这是我们的缓存数据

给它强转一下就可以

好

就是这么一个逻辑啊

整个这个方法呢

其实思路还是非常清晰的啊

无非就是先get对吧

get不到呢

然后呢

再查

查完之后呢

再set

最后呢

把数据不管是哪个分支

那么把数据给我返回到前端就可以了

好

这是关于我们这个control的方法呢

我们先写到这儿

一会儿呢

我们来编写一下什么呢

咱们这个服务的启动类

对吧

我们启动起来之后呢

来访问一下这个方法

咱们来测试一下这个效果

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程旨在演示如何在 Spring Boot 项目中集成和使用 `jCache`（具体为 `Caffeine`）缓存框架。讲师通过 IntelliJ IDEA 开发环境，逐步展示了项目的初始化、依赖配置、核心配置文件（`application.properties`）的编写、以及如何在控制器（Controller）中注入并使用 `CacheChannel` 接口来实现缓存的读取与写入操作。课程重点在于实践操作，通过代码演示了如何将数据库查询结果缓存到内存中，以提升应用性能。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:10**: 课程开场，展示项目结构和 `application.properties` 配置文件，介绍 `jCache` 的基本概念。
*   **00:10 - 00:25**: 展示 `jCache` 的 Maven 依赖配置，包括 `org.springframework.boot:spring-boot-starter-cache` 和 `net.oschina:jCache`。
*   **00:25 - 00:40**: 详细讲解 `application.properties` 文件中的配置项，如 `caffeine` 和 `lettuce` 的设置。
*   **00:40 - 01:00**: 在 `jCacheController.java` 中，通过 `@Autowired` 注入 `CacheChannel` 接口，并开始编写缓存读取方法。
*   **01:00 - 01:20**: 编写 `getCacheData` 方法，演示如何通过 `cacheChannel.get(region, key)` 获取缓存数据。
*   **01:20 - 01:40**: 在 `getCacheData` 方法中，如果缓存不存在，则从数据库查询数据（此处为模拟），并将数据存入缓存。
*   **01:40 - 02:00**: 完成 `getCacheData` 方法，返回缓存对象的值。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    *   **配置文件 (`application.properties`)**:
        ```properties
        # Caffeine 配置
        caffeine:
          properties: /caffeine.properties # 这个配置文件需要放在项目中
        # Lettuce 配置
        lettuce:
          mode: single
          namespace: 
          storage: generic
          channel: jcache
          scheme: redis
          hosts: ${pinda.redis.ip}:${pinda.redis.port}
          password: ${pinda.redis.password}
          database: ${pinda.redis.database}
          sentinelMasterId: 
          maxTotal: 100
          maxIdle: 10
          minIdle: 10
          timeout: 10000
        ```
    *   **控制器代码 (`jCacheController.java`)**:
        ```java
        @RestController
        @RequestMapping("/cache")
        public class J2cacheController {
            @Autowired
            private CacheChannel cacheChannel;

            @GetMapping("/getCacheData")
            public List<String> getCacheData() {
                CacheObject cacheObject = cacheChannel.get("rx", "city");
                if (cacheObject.getValue() == null) {
                    // 没有获取到缓存数据，需要从数据库中查询数据
                    List<String> data = new ArrayList<>();
                    data.add("beijing");
                    data.add("nanjing");
                    data.add("shanghai");
                    // 将从数据库中获取的数据载入缓存
                    cacheChannel.set("rx", "city", data);
                    return data;
                }
                return (List<String>) cacheObject.getValue();
            }
        }
        ```
    *   **核心类 (`CacheChannel.java`)**:
        ```java
        public abstract class CacheChannel implements Closeable, AutoCloseable {
            private static final Map<String, Object> _g_keyLocks = new ConcurrentHashMap<>();
            private J2CacheConfig config;
            private CacheProviderHolder holder;
            private boolean defaultCacheNullObject;
            private boolean closed;

            public CacheChannel(J2CacheConfig config, CacheProviderHolder holder) {
                this.config = config;
                this.holder = holder;
                this.defaultCacheNullObject = config.isDefaultCacheNullObject();
                this.closed = false;
            }

            public CacheObject get(String region, String key) {
                // ... 实现省略
            }

            public void evict(String region, String... keys) {
                // ... 实现省略
            }

            public void clear(String region) {
                // ... 实现省略
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖配置**
    *   讲师首先展示了项目结构，包括 `src/main/java`、`src/main/resources` 等目录。
    *   在 `pom.xml` 中，讲师添加了 `spring-boot-starter-cache` 和 `jCache` 的依赖，并配置了 `spring.factories` 文件，以启用 `jCache` 的自动配置。

*   **场景二：配置文件编写**
    *   讲师在 `application.properties` 文件中配置了 `caffeine` 和 `lettuce` 的参数，如缓存模式、Redis 连接信息等。

*   **场景三：控制器开发**
    *   讲师在 `jCacheController.java` 中创建了一个 `@RestController`，并使用 `@Autowired` 注入 `CacheChannel`。
    *   讲师编写了 `getCacheData` 方法，该方法首先尝试从缓存中获取数据。
    *   如果缓存中没有数据，讲师会创建一个 `ArrayList`，添加模拟数据（如“beijing”、“nanjing”、“shanghai”），然后调用 `cacheChannel.set(region, key, data)` 将数据存入缓存，并返回数据。

*   **场景四：代码调试与交互**
    *   讲师在编写代码时，IDEA 提供了智能提示，如 `CacheObject` 的 `getValue()` 方法。
    *   讲师通过 `@GetMapping` 注解定义了 REST API 接口，用于测试缓存功能。

---

以上是根据视频画面截图整理出的结构化信息，希望能帮助您更好地理解该技术课程的内容。
