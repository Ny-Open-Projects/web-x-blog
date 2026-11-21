# 18.支付渠道参数缓存-缓存逻辑和redis配置

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\18.支付渠道参数缓存-缓存逻辑和redis配置【海量资源尽在 666java.com】.mp4
- 时长 9分34秒（音频 575s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来实现支付渠道参数缓存那么这是什么意思呢来看一下需求因为我们知道啊我们这个支付渠道参数配置成功了之后呢是不是就插入到我们数据库的这个支付渠道参数表了那么大家知道那么这个表当中呢应该说操作是比较频繁的因为每一次支付动作呢都会从这个表来查询我们说的这个参数那么好我们
[00:25] 可以想象一下那么每次都查数据库那这个性能就不是很好对吧所以呢我们建议然后我们把支付渠道参数呢把它缓存到redis因为大家知道redis呢是基于内存存储的所以这个查询的速度呢就会比从这个数据库磁盘上面去查速度要快对吧所以这里边呢我们就准备把支付渠道参数呢缓存到redis那我们来看怎么缓存呢缓存的策略是什么呢
[00:53] 也就是说这个数据现在在数据库我们怎么样把这个数据保存到redis呢那么这个时候大家要思考前边啊我们是不是完成了支付渠道参数配置也就是像这个支付渠道参数表来保存数据啊那其实我们就可以想象一下我们在保存参数的时候呢其实我们就可以同时向redis保存一份对吧但有人说老师那你保存的时候如果没有保存成功呢
[01:19] 如果没有保存成功那么我们查询的时候呢我们先从redis查如果能查到就从redis查到数据返回给调用方如果说从redis查不到那么我们呢先从数据库查查到了之后呢我们在查询的时候呢也向redis保存数据啥意思呢就是我们前面呢我们写的这个交易服务的这个接口当中啊我们来看
[01:48] 当初我们写的一个是保存支付渠道参数对吧这是保存吗那么也就是说在保存这儿我们要向Redis来缓存我们的支付渠道参数这个就是保存渠道参数的时候呢我们同时向Redis也保存一份而查询的时候呢我们刚才说如果是查询我们准备怎么做呀我们是让你
[02:18] 先从Redis来查如果说你查询到了那么则直接返回懂吗否则呢我们从数据库查那么这个时候下边是不是都是从数据库查呀那么从数据库查的话那么从数据库查询完毕然后呢再将数据保存到Redis也就是在
[02:47] 保存配置的时候呢我们向Redis保存在查询的时候呢我们先从Redis查如果有呢就返回来如果没有我们从数据库查完了然后呢再把它保存到Redis就是两个地方呢我们都要向Redis来缓存大家理解了吧好了那下面呢我们知道了这个缓存的逻辑之后呢我们就可以来搭建Redis环境来实现整个我们刚才说的这些缓存的方法
[03:17] 好那Redis在前面呢我们已经安装成功了在搭建验证码服务的时候我们就做过了那下边呢只是需要我们在哪里呀对在我们的Necros上边我们单独再添一个Redis的配置文件好我们呢打开Necros好那么这个时候呢我们来登录一下在我们的配置文件这里边呢我们新添一个Redis的配置
[03:47] 好那这个Redis的配置呢应该是一个什么呀公共的组对吧所以这里边呢我们给它起一个公共的组那么它的内容呢其实就是Redis的一个相关的信息那里有啥呀有这个你的Redis的主机端口Redis的一个认证的密码后边呢都是它的一些连接连接池的参数啊所以这里边呢我们按照讲义上我们把它拷进去
[04:16] 但这里边有几个点就是你这个Redis我建议你在开发的时候就把这个Redis的密码就配上因为生产环境肯定要配Redis的密码对吧然后包括你这个主机名和端口这些你都要去看一下是否正确好那么发布这是不是就搞定然后接下来我们还要做什么是不是就是要把这个刚才Redis的这个文件我们要在我们的什么
[04:46] 交易服务上面我们让交易服务来读取这个Redis的配置文件好那么各位看我们交易服务这里边是不是有罗列了很多的这种子配置文件呀下面呢我们再加一个这就是刚才我们配的Redis的一个配置文件好那接下来我们继续我们呢现在要做的事呢还有你要访问Redis你在交易服务上面是不是还要把Redis的什么哎他的依赖呢也加进来
[05:16] 可以吧好然后接下来我们继续因为我们要访问redis所以呢我们就需要一些redis的工具类那么这个工具类呢在给大家的代码当中呀我都给大家提供好了在资料当资料当中我们把这两个工具类按照我讲演唱指示啊把它拷贝到我们的common工程拷贝到common工程我们可以先看一下这工具类啊打开你看那包是不是就是common youtube对吧这是工具类
[05:47] 我们把它考到COM工程对于工具类因为在企业当中任何一个项目都有很多的这个工具类或者说封装的一些代码那么有一些工具类和封装代码我在课堂上是不讲的那么如果大家有兴趣的可以去翻看一下我们这个原代码好这就考上去了考上去之后呢我们继续看啊还需要我们考一个叫redis catch然后到我们交易服务的这个工程下边
[06:16] 好打开以后呢我只是给你讲这些工具类怎么用啊具体的封装的逻辑呢我们课堂上不讲大家呢可以私下呢去看一下好这里边呢在这儿我们要新建一个包叫common youtube然后呢你把这个靠进去好注意看大家看到这个接口吗在我们的平台上面呢我们有一个非常抽象的一个缓存的一个接口
[06:42] 那么你要知道缓存不光有Redis还有其他的是吧所以那Redis呢只是实现了这个接口如何拿到key然后呢如何根据key得到我们说的缓存的数据并且如何判断这个key是否存在包括删除这个key所对应的数据等等等等这些都是一些抽象的方法而Redis缓存只是一个具体的其中的一个实现你看通过Redis Template我来访问我们的Redis好吧
[07:10] 好那么这些东西呢我们把它考进去之后呢那么我们来看接下来那么你要访问Redis啊你就需要刚才我们说到的那个Redis的cache的一个实例定义一个bin对吧所以这里边呢我们在说Spring Boot工程定义bin的时候呢和参谋方式就不太一样了参谋方式呢是在参谋里边配置一个是吧而Spring Boot呢就需要我们加注解configuration对吧
[07:40] 好然后在这个里边呢我们定义bin之前我们是不是定义过rest的template是吧new一个就行了而现在呢我们基本上也是这种方式啊new一个好那下面我们来看一下首先呢这里边有一个bin的注解对吧好然后呢你最终要返回这么一个catch的一个实例好那redis的话咱们需要用到redis的一个什么呀redis的一个模板类对
[08:09] 这个redis的模板类呢有些同学应该接触过没有接触过的也不要着急因为现在我们说嘛整个的这个工程代码已经封装到我们说的这个catch当中了大家只要调用catch呢就可以来啊他的方法就可以来访问redis好new一个new一个我们刚才看到我们是不是考了一个叫redis cache然后我们把它放进去这样我们这个redis cache呀我们就实力化成功了
[08:36] 这样我在我们的Service里边我们就可以注入这个什么这个cache就可以去使用了好那么到这儿呢基本上我们这个redis的环境啊咱们就配置好了你看我注入cache因为我说了嘛cache是一个抽象的接口我们针对它是不是有一个什么呀是不是实现类呀而这个实现类是不是就是我们说的redis cache对通过redis template的模板方法来访问redis里边的数据
[09:06] 好了那么到这呢我们说我们准备将支付渠道参数呢缓存到Redis在保存参数的时候呢要向Redis里面保存在查询渠道参数的时候呢我们也要向Redis里面查询报存对吧先查询Redis如果有返回如果没有的话就向Redis保存这是它的缓存策略以及刚才Redis环境好我们呢先到这稍后呢我们再实现整个缓存的逻辑

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现支付渠道参数缓存功能，通过 Redis 缓存提升查询性能，并展示如何在 Spring Boot 项目中配置和使用 Redis。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档“5.6 支付渠道参数缓存”章节，重点是“5.6.1 需求分析”，说明将渠道参数缓存到 Redis 以提升查询性能。
画面2：在 IntelliJ IDEA 中查看 `PlatformParamController.java` 代码，展示查询支付渠道参数的接口方法。
画面3：在 IntelliJ IDEA 中查看 `PayChannelService.java` 代码，展示查询支付渠道参数的业务逻辑。
画面4：在 Postman 中测试支付渠道参数查询接口，参数包括 appid、payChannel、platformChannel。
画面5：在 Typora 中查看 Nacos 中的 Redis 配置文件 `spring-boot-redis.yaml`，配置了 Redis 的连接信息和连接池参数。
画面6：在 Typora 中展示如何在 `shanjupay-transaction-Service` 工程的 `bootstrap.yml` 中引入 Redis 配置。
画面7：在 Typora 中展示如何在 `shanjupay-transaction-Service` 工程的 `pom.xml` 中添加 Redis 依赖。
画面8：在 IntelliJ IDEA 中查看 `RedisEnum.java` 代码，定义了 Redis 缓存的键前缀、模块、方法名、描述等。
画面9：在 IntelliJ IDEA 中查看 `RedisEnum.java` 代码，展示其构造函数和 getPrefix 方法。
画面10：在 IntelliJ IDEA 中查看 `RedisCache.java` 代码，展示其 `set` 和 `get` 方法。
画面11：在 IntelliJ IDEA 中查看 `RedisCache.java` 代码，展示其构造函数和 `getKeys` 方法。
画面12：在 IntelliJ IDEA 中查看 `RedisConfig.java` 代码，展示其 `@Configuration` 注解和 `Cache cache()` 方法。
画面13：在 IntelliJ IDEA 中查看 `PayChannelService.java` 代码，展示其 `queryPayChannelParamsByAppIdAndPlatformChannel` 方法。
画面14：再次展示课程文档“5.6 支付渠道参数缓存”章节，重点是“5.6.1 需求分析”，说明将渠道参数缓存到 Redis 以提升查询性能。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
```yaml
spring:
  redis:
    # Redis数据库索引（默认为0）
    database: 0
    host: 127.0.0.1
    port: 6379
    # 连接超时时间（毫秒）
    timeout: 1000ms
    password: 123456
  lettuce:
    pool:
      # 连接池中的最大空闲连接
      max-idle: 8
      # 连接池中的最小空闲连接
      min-idle: 0
      # 连接池最大连接数（使用负值表示没有限制）
      max-active: 8
      # 连接池最大阻塞等待时间（使用负值表示没有限制）
      max-wait: 1000ms
      shutdown-timeout: 1000ms
```

画面6：
```yaml
refresh: true
data-id: spring-boot-redis.yaml # redis配置
group: COMMON_GROUP # 通用配置组
```

画面7：
```xml
<!-- Redis启动器 -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```

画面8：
```java
package com.shanju.pay.common.util;

/**
 * @author Administrator
 * @version 1.0
 */
public class RedisEnum {
    /**
     * 缓存键前缀
     */
    private String keyPrefix;
    /**
     * 模块名称
     */
    private String module;
    /**
     * 方法名称
     */
    private String func;
    /**
     * 描述
     */
    private String remark;

    RedisEnum(String keyPrefix, String module, String func, String remark) {
        this.keyPrefix = keyPrefix;
        this.module = module;
        this.func = func;
        this.remark = remark;
    }

    public String getKeyPrefix() {
        return keyPrefix;
    }
}
```

画面10：
```java
/**
 * 简单的字符串设置
 * @param key
 * @param value
 */
void set(String key, String value);
```

画面11：
```java
package com.shanju.pay.transaction.common.util;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Component;

@Component
public class RedisCache implements Cache {
    private RedisTemplate<String, Object> redisTemplate;

    public RedisCache(RedisTemplate<String, Object> redisTemplate) {
        this.redisTemplate = redisTemplate;
    }

    @Override
    public Set<String> getKeys(String pattern) {
        return redisTemplate.keys(pattern);
    }
}
```

画面12：
```java
import com.shanju.pay.common.cache.Cache;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.StringRedisTemplate;

@Configuration
public class RedisConfig {
    @Bean
    public Cache cache(RedisTemplate<String, Object> redisTemplate) {
        return new RedisCache(redisTemplate);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1、14：PPT 标题为“5.6 支付渠道参数缓存”，子标题“5.6.1 需求分析”和“5.6.2 搭建redis环境”。
画面5：PPT 标题为“5.6.2 搭建redis环境”，子标题“2. 在Nacos中添加Redis配置：spring-boot-redis.yaml, Group: COMMON_GROUP”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

