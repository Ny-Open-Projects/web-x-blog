# 06-j2cache多级缓存（入门案例_4） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,继续来看咱们这个Rumor案例啊,刚才呢,我们已经把这个GetCatchData这个方法呢,是不是进行了一个测试,那接下来呢,我们再来看下一个啊,下一个呢,我们来测试一下什么呢,一个小点,就是关于我们配置的这个地方,叫做Serialization,其实是序列化,对吧,序列化,现在呢,我们配置的是这种叫做FST这种序列化的方式,对吧,其实除了这个方式之外呢,它另外还有这么两个啊,一个是Java的,还有一个是这个的,好,

那么不同的序列化方式它会影响什么呢,它会影响我们这个数据的存储,以及它的存储的这个形式,以及什么呢,这个字节的大小,比如说我们现在啊,现在咱们是FST这种方式,对吧,那么我们当前这个数据呢,它存储的这个字节数呢,大家可以看到这个地方是31,对吧,是31字节,好,那么接下来呢,我们可以来这个修改一下,咱们把这个FST呢,改成什么呢,比如说我改成Java,好,

改成Java,好,然后呢,我们需要重新启动一下,重新启动一下,重新启动之后呢,我们再来测试一下,看看什么呢,就是相同的数据,我们用不同的这种序列化方式,对吧,把它存储起来,来看一下最终我们这个数据的字节数啊,它这个大小其实还是有差别的,而且差别还是比较大的,刚才我们看到这个是31,对吧,31,那接下来呢,我们可以把这个数据把它清理掉,然后呢,重新比较,

把它再存进来,这是,这次呢,使用的是这种啊,Java这种序列化方式,好,那么现在呢,这个服务已经启动完了,启动完之后呢,咱们现在把原先存储的这个数据呢,给它清理掉,直接delete,OK,好,把它删掉,删掉之后呢,我们重新reload一下,大家来看,现在这里面是不是有没有数据了,然后呢,我们重新再来请求一下这个方法,对吧,重新请求这个方法,刷新,好,它又过来了,对吧,过来之后呢,我们来看,好,第一次的话呢,我们可以看到这个数据呢,我们可以看到这个数据呢,我们可以看到这个数据呢,我们可以看到这个数据呢,我们可以看到这个数据呢,

它肯定是获取不到数据的啊,因为我刚才是不是已经清理掉了,你看,是不是现在是NOW,对吧,没有获取到,然后呢,我们直接进来,它会定义这个set的方法,把相同的一份数据是不是载入缓存,对吧,好,set,又进来了,进来之后呢,重新到这边来看,好,你看,数据是不是又存进来,刚才我们看到相同的数据呢,它那个是31,对吧,而现在呢,大家来看,它是不是变成了什么了,89,好,基本上相差三十一,对吧,好,现在呢,大家来看,它是不是变成了什么了,八十九,好,基本上相差三十一,对吧,

三倍,这个字节大小,然后呢,你可以看到这边的话,其实从这儿也能看到,它这个形式还是不太一样的啊,所以说呢,我们不同的这种什么呢,不同的这种虚拟化方式会导致我们最终啊,这个字节数呢,存储的数据的字节数呢,还是有非常大的区别的,这是这个,那么正常我们一般使用的时候呢,建议使用的就是这种FST这种方式就可以了,FST,好,我还要重新把它改回来,

好,这是关于我们这个,

另外这个呢,大家如果感兴趣呢,也可以自己去测试一下,那么我们后边呢,就统一都使用这种FST这种虚拟化方式,好,这是关于这个小点呢,一个简单的测试,我们先说到这儿,

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频演示了一个基于 Spring Boot 的 Java 项目，使用 JCache 规范结合 Caffeine 缓存库和 Redis 数据库实现缓存功能。核心内容包括：
- **项目结构与配置**：展示了 `application.yml` 中如何配置 JCache 的缓存提供者（`provider_class`）为 Caffeine，并指定其底层存储为 Redis。
- **缓存逻辑实现**：在 `JCacheController.java` 中，通过 `cacheChannel.get()` 方法尝试从缓存中获取数据。若缓存中无数据（`cacheObject.getValue() == null`），则从数据库（此处模拟为内存列表）中查询数据（如“北京”、“上海”），并将数据写入缓存。
- **调试与验证**：通过 IntelliJ IDEA 的调试器（Debugger）逐步执行代码，观察变量值的变化，并使用 Redis Desktop Manager 查看 Redis 中实际存储的缓存数据，以验证缓存机制的有效性。

整个演示旨在说明如何在 Spring Boot 应用中集成 JCache，并利用 Caffeine 作为缓存中间件，同时将数据持久化到 Redis 中。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频中的时间戳，以下章节基于画面内容和逻辑顺序进行划分：

- **00:00 - 00:05**: **项目初始化与环境介绍**。画面显示 IntelliJ IDEA 中的项目结构，包括 `pom.xml`、`application.yml` 和 `JCacheController.java` 文件，为后续操作做准备。
- **00:05 - 00:15**: **配置文件详解**。聚焦于 `application.yml`，详细讲解 `L1` 和 `L2` 缓存层的配置，包括 `provider_class`、`config_section`、`serialization` 等关键属性。
- **00:15 - 00:25**: **缓存逻辑代码演示**。在 `JCacheController.java` 中，讲解 `@GetMapping("/getCacheData")` 方法的实现逻辑，重点是 `cacheChannel.get()` 的调用和 `if (cacheObject.getValue() == null)` 的条件判断。
- **00:25 - 00:35**: **调试与数据写入**。启动调试器，设置断点，逐步执行代码，观察 `data` 列表的构建过程，并在 `cacheChannel.set()` 中将数据写入缓存。
- **00:35 - 00:45**: **缓存数据验证**。切换到 Redis Desktop Manager，查看 Redis 中 `rx:city` 键对应的值，确认缓存数据已成功写入。
- **00:45 - 00:55**: **缓存读取与返回**。继续调试，观察 `cacheChannel.get()` 返回的缓存数据，并最终返回给客户端。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### 代码关键内容

- **控制器方法 (`JCacheController.java`)**
  ```java
  @GetMapping("/getCacheData")
  public List<String> getCacheData() {
      CacheObject cacheObject = cacheChannel.get(region: "rx", key: "city");
      if (cacheObject.getValue() == null) {
          // 没有获取到缓存数据，需要从数据库中查询数据
          List<String> data = new ArrayList<>();
          data.add("beijing");
          data.add("nanjing");
          data.add("shanghai");
          // 将从数据库中获取的数据载入缓存
          cacheChannel.set(region: "rx", key: "city", data);
          return data;
      }
      return (List<String>) cacheObject.getValue();
  }
  ```

- **配置文件 (`application.yml`)**
  ```yaml
  # L1 缓存配置
  broadcast: net.oschina.jcache.cache.support.redis.SpringRedisPubSubPolicy
  L1:
    provider_class: caffeine
    config_section: lettuce
    sync_ttl_to_redis: true
    default_cache_null_object: false
    serialization: java # 序列化方式：fst, kyro, Java

  # L2 缓存配置
  L2:
    provider_class: net.oschina.jcache.cache.support.redis.SpringRedisProvider
    config_section: lettuce
    sync_ttl_to_redis: true
    default_cache_null_object: false
    serialization: java # 序列化方式：fst, kyro, Java

  # Caffeine 配置
  caffeine:
    properties: /caffeine.properties # 这个配置文件需要放在项目中

  # Redis 配置
  lettuce:
    mode: single
    namespace: generic
    channel: jcache
    scheme: redis
    hosts: ${pinda.redis.ip}:${pinda.redis.port}
    password: ${pinda.redis.password}
    database: ${pinda.redis.database}
    sentinelMasterId: 100
  ```

#### 图表/演示内容

- **Redis Desktop Manager 界面**：用于查看 Redis 中的缓存数据。画面显示了 `rx:city` 键的值为一个包含“北京”、“上海”等城市的字符串数组，验证了缓存写入成功。

---

### 4) 关键场景与演示描述

- **场景一：缓存读取失败，触发数据加载**
  - **描述**：在调试器中，当执行 `cacheChannel.get(region: "rx", key: "city")` 时，`cacheObject.getValue()` 返回 `null`，表示缓存中没有数据。
  - **演示**：代码进入 `if` 分支，创建一个 `ArrayList`，并添加“北京”、“上海”等城市数据，随后调用 `cacheChannel.set()` 将数据写入缓存。

- **场景二：缓存数据写入与验证**
  - **描述**：在 `cacheChannel.set()` 方法执行后，数据被写入 Redis。
  - **演示**：切换到 Redis Desktop Manager，查看 `rx:city` 键，确认其值已更新为包含城市数据的数组，证明缓存机制有效。

- **场景三：缓存读取成功，直接返回**
  - **描述**：当再次调用 `getCacheData()` 方法时，`cacheChannel.get()` 直接从缓存中获取数据，无需再次查询数据库。
  - **演示**：调试器中 `cacheObject.getValue()` 返回非空值，代码直接返回该值，提高了数据访问效率。

- **场景四：调试器变量观察**
  - **描述**：通过调试器观察变量 `cacheObject`、`data` 和 `cacheChannel` 的值，帮助理解程序执行流程。
  - **演示**：在断点处，`cacheObject` 的值为 `null`，`data` 列表为空，随后在 `cacheChannel.set()` 后，`data` 列表被填充，`cacheObject` 的值变为非空。

---

以上是根据视频画面进行的结构化技术分析报告。
