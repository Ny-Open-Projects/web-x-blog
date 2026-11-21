# 画面线理解：06_热文章计算_定时计算_频道首页数据缓存到redis

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\06_热文章计算_定时计算_频道首页数据缓存到redis【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:19, 01:37, 02:07, 02:38, 03:03, 03:22, 04:07, 04:20, 04:52, 05:18, 05:41, 06:07, 06:24, 06:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:35:12

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
