# 06_热文章计算_定时计算_频道首页数据缓存到redis

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\06_热文章计算_定时计算_频道首页数据缓存到redis【海量资源尽在 666java.com】.mp4
- 时长 6分59秒（音频 419s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就继续往下看啊然后下面是一个什么呢是缓存文章中的频道啊这个其实说的有问题啊干啥呢这叫缓存频道首页叫readies什么意思呢你可以看啊比如说我在这去画个图比如说这个啊这个就是咱们的app那app里边是不是会有一些标签哎这是标签啊标签栏一个一个的比如说这是第一个是jar第二个是pason
[00:33] 好吧第三个什么vix其他的无所谓比如说我去点了一下jar是不是他应该会有这种列表出来我讲这个列表其实咱们最终是要缓存它怎么样缓存它它的key谁key就是当前的jar然后这个列表就是咱们要缓存的value所以说咱们要缓存的是当前的一个根据频道去缓存一些数据好
[01:03] 那该怎么去办该怎么办呢这个咱们在这去封装一个方法叫pitch然后是to write this这个里边参数就是当前的critical list这个没有是吧方法没有怎么就创建一下缓存频道首页数据到write this首先咱们这会肯定会用到write this
[01:38] 你会用到啊那这个redis怎么去拿呢那个redis该怎么去做呢该怎么去集成呢那非常简单啊那咱们在之前的课上啊其实已经把这个redis已经集成到了当前的common中所以说啊你在这啊你在当前的article当前这个微服务中在这去加一个redisconfig啊我这已经加完了看到了吗我看这就是你直接去扫描当前那个common redis就可以了啊非常简单啊
[02:08] 现在这个加完之后这里边我要去强调一个问题比如说你这个你这讲说你那个你那个realist环境没有设置密码的话你需要把这一行给除掉或者你删了也可以因为这个默认是有密码的有密码的话如果说你的环境没有密码他就会报错所以说你要去设置一下但是真实环境肯定会有密码
[02:33] 怎么现在测试环境都没有密码啊所以说你把这一行给住掉就可以啊那行那咱们就接着往下写啊那这会该该怎么去写呢刚才说了就是根据频道去缓存他的首页的数据是吧首先呢你要拿到所有的频道拿到啊拿到所有频道怎么拿呀等在这先去注入一个private叫adchinovipo啊不是诸然后还要再注入一个什么东西
[03:09] 一个redis是吧revit有一个redis好注入进来该注入进来的都注入进来了这时候咱们就可以去写了首先呢你要去发寻所有的频道啊2没有一个slack的这个呢其实就是当前的inose就是所有的频道信息最重要你要去缓存的谁呀缓存是他是吧比如说咱们去在这先去创建一个东西叫temp等于呢
[03:45] 这个数据怎么来呢意思呢咱们要首先要去循环的是它点有一个叫做循环的时候呢咱们要去过滤当前这个里边是不是包含了当前的Tino那怎么办呢咱们可以这么找点咱们有一个叫做Stream点有一个Field随便找啊这个杠找谁呢
[04:17] 好记得Tino什么呢Tino ID假如Ecos谁呢Ecos当前的Tino的Get ID他的ID是一样的话呢这时候我们就让他去到一个集合中这个集合呢其实就是谁啊这个集合就是咱们上面定义的当前这个fam好那这样的话咱们就算是跑着了到着之后啊其实还没有完还没有完啊然后接着往下看
[04:55] 如果说temp.size大于30咱们就是什么意思为什么要这么判断呢判断的意思就是大于30的话咱们就截到30因为太多的话其实也没有必要这个数据显示的时候所以说咱们在这temp.sublist然后是0-30如果不超过30的话那就无所谓了是吧下面咱们就可以进行
[05:26] 换存了换存之前咱们还要在这去做个判断说什么temp.size等于0的话咱们设置为空这个该怎么去设置咱们可以videos.r咱们有一个叫做ops.forvalue.rset第一个是key第二个是value是吧那这个key是谁
[05:56] 跟当前的Channel ID是相关的这样咱们呢在前面再加一个前对这前对呢叫做AarticleConstance点里边有一个叫做OutArticleFirstPage首页是吧然后呢是加上前的Channel的GetID然后呢这个值就作为空就可以了它是0嘛OK啊如果说它不是0不是0的话那就简单了啊
[06:28] 你可以直接去加什么呢直接加数据就可以了直接把temp装进去就可以了但是这么装进去之后呢这个不太方便啊咱们可以干嘛呢咱们可以去把它呢转成之前的json好然后你把当前的temp装进去就可以了好吧最终的话我们就把当前的这个频道首页的数据啊就给缓存了起来好那这个缓存这块咱们就说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过 Redis 缓存热点文章分页数据，并根据频道 ID 和文章数量进行分页存储。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 `ApiHotArticleServiceImp.java` 中的 `computeHotArticle` 方法，用于计算热点文章列表，调用 `apArticleMapper` 查询数据，并将结果缓存到 Redis。
画面 2: 展示 `ApiHotArticleServiceImp.java` 中的 `cacheTagRedis` 方法，用于将文章列表按频道缓存到 Redis。
画面 3: 展示 `RedisConfig.java` 文件，用于配置 Redis 相关的 Bean。
画面 4: 展示 PPT 页面，内容为“2.5 定时任务”，并提及集成 Quartz 和 MySQL。
画面 5: 展示 `ApiHotArticleServiceImp.java` 中的 `@Autowired` 注解，用于注入 `AdChannelMapper` 和 `RedisTemplate`。
画面 6: 展示 `ApiHotArticleServiceImp.java` 中的 `cacheTagRedis` 方法，定义了 `AdChannelMapper` 和 `RedisTemplate` 的注入。
画面 7: 展示 `ApiHotArticleServiceImp.java` 中的 `cacheTagRedis` 方法，使用 `Stream` API 对文章列表进行分组处理。
画面 8: 展示 `ApiHotArticleServiceImp.java` 中的 `cacheTagRedis` 方法，使用 `filter` 方法根据频道 ID 过滤文章。
画面 9: 展示 `ApiHotArticleServiceImp.java` 中的 `cacheTagRedis` 方法，使用 `collect(Collectors.toList())` 收集过滤后的文章列表。
画面 10: 展示 `ApiHotArticleServiceImp.java` 中的 `cacheTagRedis` 方法，使用 `temp.size()` 判断文章数量。
画面 11: 展示 `ApiHotArticleServiceImp.java` 中的 `cacheTagRedis` 方法，使用 `redisTemplate.opsForValue().set(...)` 将文章分页信息存入 Redis。
画面 12: 展示 `ApiHotArticleServiceImp.java` 中的 `cacheTagRedis` 方法，使用 `redisTemplate.opsForValue().set(...)` 将文章分页信息存入 Redis，并设置键值。
画面 13: 展示 `ApiHotArticleServiceImp.java` 中的 `cacheTagRedis` 方法，使用 `redisTemplate.opsForValue().set(...)` 将文章分页信息存入 Redis，并设置键值。
画面 14: 展示 `ApiHotArticleServiceImp.java` 中的 `cacheTagRedis` 方法，使用 `redisTemplate.opsForValue().set(...)` 将文章分页信息存入 Redis，并设置键值。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@Override
public void computeHotArticle() {
    String lastDay = DateTime.now().minusDays(1).toString("yyyy-MM-dd 00:00:00");
    List<Article> articleList = apArticleMapper.loadLastArticleForHot(lastDay);
    List<ApHotArticles> hotArticlesList = computeHotArticle(articleList);
    cacheTagRedis(hotArticlesList);
    //缓存文章中的图片（暂时不做）
}
```

画面 2:
```java
private void cacheTagRedis(List<Article> articleList) {
```

画面 3:
```java
package com.heima.article.config;

import ...

@Configuration
@ComponentScan("com.heima.common.redis")
public class RedisConfig {
}
```

画面 4:
```java
redis config
spring.redis.host=127.0.0.1
spring.redis.port=6379
spring.redis.password=123456
spring.redis.timeout=90000
```

画面 5:
```java
@Autowired
private AdChannelMapper adChannelMapper;

@Autowired
private RedisTemplate redisTemplate;
```

画面 6:
```java
@Autowired
private AdChannelMapper adChannelMapper;

@Autowired
private RedisTemplate redisTemplate;
```

画面 7:
```java
private void cacheTagRedis(List<Article> articleList) {
    List<AdChannel> channels = adChannelMapper.selectAll();
    List<Article> temp = null;
    for (AdChannel channel : channels) {
        temp = articleList.stream().filter(p -> p.getChannelId().equals(channel.getChannelId())).collect(Collectors.toList());
    }
}
```

画面 8:
```java
private void cacheTagRedis(List<Article> articleList) {
    List<AdChannel> channels = adChannelMapper.selectAll();
    List<Article> temp = null;
    for (AdChannel channel : channels) {
        temp = articleList.stream().filter(p -> p.getChannelId().equals(channel.getChannelId())).collect(Collectors.toList());
    }
}
```

画面 9:
```java
private void cacheTagRedis(List<Article> articleList) {
    List<AdChannel> channels = adChannelMapper.selectAll();
    List<Article> temp = null;
    for (AdChannel channel : channels) {
        temp = articleList.stream().filter(p -> p.getChannelId().equals(channel.getChannelId())).collect(Collectors.toList());
    }
}
```

画面 10:
```java
private void cacheTagRedis(List<Article> articleList) {
    List<AdChannel> channels = adChannelMapper.selectAll();
    List<Article> temp = null;
    for (AdChannel channel : channels) {
        temp = articleList.stream().filter(p -> p.getChannelId().equals(channel.getChannelId())).collect(Collectors.toList());
    }
}
```

画面 11:
```java
private void cacheTagRedis(List<Article> articleList) {
    List<AdChannel> channels = adChannelMapper.selectAll();
    List<Article> temp = null;
    for (AdChannel channel : channels) {
        temp = articleList.stream().filter(p -> p.getChannelId().equals(channel.getChannelId())).collect(Collectors.toList());
    }
}
```

画面 12:
```java
private void cacheTagRedis(List<Article> articleList) {
    List<AdChannel> channels = adChannelMapper.selectAll();
    List<Article> temp = null;
    for (AdChannel channel : channels) {
        temp = articleList.stream().filter(p -> p.getChannelId().equals(channel.getChannelId())).collect(Collectors.toList());
    }
}
```

画面 13:
```java
private void cacheTagRedis(List<Article> articleList) {
    List<AdChannel> channels = adChannelMapper.selectAll();
    List<Article> temp = null;
    for (AdChannel channel : channels) {
        temp = articleList.stream().filter(p -> p.getChannelId().equals(channel.getChannelId())).collect(Collectors.toList());
    }
}
```

画面 14:
```java
private void cacheTagRedis(List<Article> articleList) {
    List<AdChannel> channels = adChannelMapper.selectAll();
    List<Article> temp = null;
    for (AdChannel channel : channels) {
        temp = articleList.stream().filter(p -> p.getChannelId().equals(channel.getChannelId())).collect(Collectors.toList());
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 4:
PPT 标题: “2.5 定时任务”
内容: “集成quartz,把之前的mysql也集成到一个配置类中,并放到quartz之前”

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

