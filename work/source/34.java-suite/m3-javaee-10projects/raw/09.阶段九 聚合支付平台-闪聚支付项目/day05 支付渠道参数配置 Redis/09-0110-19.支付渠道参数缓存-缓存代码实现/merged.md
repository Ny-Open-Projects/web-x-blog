# 19.支付渠道参数缓存-缓存代码实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\19.支付渠道参数缓存-缓存代码实现【海量资源尽在 666java.com】.mp4
- 时长 11分55秒（音频 715s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,下面我们就来实现支付渠道参数缓存的具体的方法刚才我们已经分析了具体的缓存策略是在保存支付渠道参数的时候向Redis来保存支付渠道参数那么在查询支付渠道参数的时候我们先从Redis查如果有我们就返回没有我们也将从数据库查询到的东西同时保存到Redis
[00:28] 这是两个地方都要向Redis来保存好那下面呢我们就来实现这个代码首先呢我们先做在保存支付渠道参数的时候呢向Redis呢来写数据这里我们思考一件事啊就是说你在保存的时候呢需要向Redis写你在查询的时候呢也需要向Redis写对不对所以这里边呢我们就在想那干脆我们写一个私有方法行不行
[00:55] 而这个sale方法呢就是向什么向redis来写数据对吧好了那么这个sale方法我们要根据要传入哪些数据然后呢根据什么来写入redis呢注意我说一下啊这里边呀我们要将啊支付渠道看好啊支付渠道参数写入redis对吧那具体支付渠道你是要根据什么
[01:23] 来查询支付渠道你这查询一个支付渠道列表呀还是查询一个支付渠道的参数注意我这边定规则了啊我们要将什么呀我们要根据啊应用的ID和服务类型的code查询什么支付渠道列表然后呢将它就是这个支付渠道参数列表写入redis我说的够清楚了吧对
[01:54] 所以这里边呢我们准备将应用和服务类型他们所有的支付渠道参数都要写到redis举个例子这里边这个应用和支付应用和服务类型它的绑定ID是不是它它的支付渠道可能有多个是不是在这个表可能是多条记录所以我们就准备把这多条记录呢写到我们的redis好那既然根据应用和服务类型
[02:23] 来把他们的支付渠道参数呢写到reddit所以这里边肯定得有一个什么应用ID对吧那么还得有一个什么服务类型的code对吧plateform然后呢channelcode这样可以吧好这样的话我把这个私有方法说一下这就是根据应用和服务类型将他们的支付
[02:54] 将查询到的支付渠道参数配置列表写入redis所以这样的话你就知道了它这个参数这就是应用的ID对不对好那么这个呢就是什么服务类型的code没错吧好了那现在呢我们需求明确了那下面我们就要怎么弄啊你要根据应用ID和服务类型code干嘛我们先要查询支付
[03:25] 渠道参数行不行你不查你咋存呢对不对那这个查询是不是在这我们直接调用这个方法appid然后呢plataform channel code我是不是就拿到了这个对吧但是我们再定一个逻辑你这是更新缓存吗你更新缓存的时候我建议你这么做如果有的情况下你先把它删掉然后再添加
[03:56] 为什么这么做呢因为你要知道根据应用和服务类型在这个表当中可能是一条记录也可能如同一条我们的目的是我们把应用和服务类型相关的支付渠道参数都存到redis对不对那如果说已经有了一个微信了那么我建议你你把原来的微信这个支付渠道参数删掉然后呢我们再次把
[04:18] 比较完整的一个支付渠道参数列表插出来存到redis以免我们说的这个缓存到redis里面的数据不完整懂我意思吧所以这里边呢我们要先根据key看好啊来查询redis而这个key注意这个key就是将来存redis里面的这个key懂吧那么这个key呢注意我们要得到redis当中对
[04:47] 你准备是不是要根据应用和服务类型查询到支付渠道参数传到Redis呀所以这里边呢我们要得到Redis当中的什么key而这个key呢就是支付渠道参数列表的key懂吧这个key是有一定规律的啊那这个key怎么构造出来呢我们原来是不是考了一个工具类呀这里边它有一个叫
[05:14] 构建一个key的方法这个key呢注意点开看一下那它呢是以一定的前缀命名看见吗有个闪具配下环线param然后呢中间可以冒号分割可以包括几个元素那么我们准备这么做我们把这个什么呀APP ID还有这个服务类型code我们把它拿过去这个就是redis的什么key那你说老师这个key的格式是啥呢
[05:41] 这个格式我刚才说了一个是这个前缀还有一个冒号这后边就是应用ID然后再冒号后边就是我们说的服务类型的code懂吧你们用一举个例子这个例子假如说我们生成了一个key就是这个应用ID比如说这个应用ID是他你看是不是他那么我们生成了一个key那么前缀不要变懂吧然后后边呢它是一个应用ID然后加一个服务类型code
[06:12] 那服务类型呢我们也可以找一个比如说服务类型那个好这是不是就是我们的服务类型这就是一个例子吧最终我们会把这个应用的服务类型是C扫币的它的支付渠道参数呢存到redis看懂这个key的一个构造方法要记着好了那么来看一下这个工具类呢我们之前不是我们写的但是你也能大概看得懂啊你看有一个什么潜序这里边你看分别是以
[06:41] 冒号分隔符来累加一个字符串对不对拼装一个字符串好了拿到了这个key呢我们现在呢就要从redis里边来查那怎么查我们可以先看看这个key存在不存在懂吧对如果说我刚才说了嘛如果它存在我就建议你干嘛把它删掉为啥为了保证数据的完整性因为我们的目的是要拿这个应用服务类型所有的支付渠道参数
[07:10] 对吧你把假如说里边原来有一个了你把一个删掉然后呢查一个完整的把它存进去所以我们先删后查好吧好那下面呢如果存在我们就删掉对吧那现在redis里面是不是就没有这个可以对应的值了那下面我们是不是就查到了一个完整的置步渠道参数列表所以这呢我们就准备将这个什么将这个置步渠道参数列表存入redis
[07:38] 是这个意思吧好那当然这里边当然我建议你也判断一下如果说它不等于空你在存你别存进去一个空是不是啊不等于空在存的话怎么存里面catch里面是不是有一个set看见吧set的话你把key拿到这对吧然后呢那个value呢value是不是准备这是个例子的我们准备把它转成json来存行不行转成json那转成json的话那你就把它填进去
[08:08] 转成支付串这是不是就相当于我们说的将这个list然后呢我们把它转成json串存入redis这个sale方法我是不是就写好了这个sale方法一旦写好我跟你说特别好用你拿了这个sale方法看好在这我们不是说保存支付区到参数的时候来保存redis吗那你就在这来叫做保存到redis直接调这个sale方法就行了
[08:38] 掉的时候呢你看他要啥你给他啥对吧他要啥他要一个APP ID还要一个什么服务类型code这是不是就是换存呀这是保存的时候我们要换存那么后边呢我们说了吗查询的时候也要先从Redis查如果有则返回对不对好那刚才说了嘛你首先是不是要拿到key对不对
[09:07] 你拿到key了之后呢看好啊我们把这个先补充完整拿到key之后咋弄拿到key之后你得判断它在不在嘛是不是啊你得看看它存在不存在如果存在的话那么你这儿呢就要把它给得到get到我是不是拿到了一个什么这是一个啥这个是不是就是我们从这个redis里边拿到的这个支付渠道
[09:38] 参数的什么呀哎字符串懂吗那我拿到这个字符串了它是个jason串了你得转嗯你得转怎么转pass啊它是一个什么呀它是个最终你原来放进去是不是一个list呀list要转的话你得用这个方法你看见吗你用这个方法然后呢你把它放进去啊里边呢你再写一个将来你转成list的list里边的这个对象它的类型然后这就
[10:09] 成了我们就把这个返回就可以了看懂啥意思了吗对这里边我们说这时候呢就从redis来获取支付渠道参数列表而你拿到这个列表是不是一个json串啊那这个json串我们是不是要做一件事啊对就是要将什么呀将json串转成转成谁转成这个类型最后返回
[10:41] 懂了吧那如果有你只要返回那如果没有没有这是不是就从数据库查从数据库查完根据我们说的缓存策略从数据库查完了之后你是不是还要把它保存到redis所以这里边注意看这里边我们这么做我们先这是不是就是从数据库查到的对吧那么从数据库查到的你在返回之前你得做一件事啥事
[11:10] 保存redis懂吧那这时候呢你再给我apvid然后再给我服务类型代码我呢就再次给你保存对所以其实各位你会发现我们在写代码的时候呢这个方法抽取非常重要所以这个方法你抽取好了之后你写代码特别快保存支付渠道参数的时候呢我们同时保存的redis调一下这方法就行了对不对然后呢
[11:37] 查询的时候呢如果Redis有我们就直接返回如果没有我们这儿呢再次调用刚才的自由方法来保存这就是我们整个的什么Redis缓存支付渠道参数的一个实现逻辑稍后呢我们进行测试好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何在支付渠道参数保存时，将参数同时缓存到 Redis 中，涉及代码实现和 Redis 配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程大纲，当前章节为 5.6.3 保存缓存，说明保存参数成功的同时将参数保存在 Redis 中，需要修改 PayChannelServiceImpl 中的 savePayChannelParam 方法。
画面 2: 展示 PayChannelServiceImpl.java 文件，光标位于 private void updateCache(...) 方法的定义处，显示了方法的参数和注释。
画面 3: 展示 updateCache 方法的实现，光标位于方法体内部，显示了方法的注释和部分代码。
画面 4: 展示 updateCache 方法的实现，光标位于方法体内部，显示了方法的注释和部分代码。
画面 5: 展示 RedisUtil.java 文件，光标位于 KEY_SPLIT_CHAR 字段的定义处，显示了常量的值。
画面 6: 展示 RedisUtil.java 文件，光标位于 keyBuilder 方法的定义处，显示了方法的注释和部分代码。
画面 7: 展示 updateCache 方法的实现，光标位于 cache.del(redisKey) 语句处，显示了删除 Redis 中的 key。
画面 8: 展示 updateCache 方法的实现，光标位于 cache.set(redisKey, ...) 语句处，显示了将参数序列化后存入 Redis。
画面 9: 展示 updateCache 方法的实现，光标位于 updateCache(...) 语句处，显示了调用 updateCache 方法。
画面 10: 展示 updateCache 方法的实现，光标位于 cache.set(redisKey, ...) 语句处，显示了将参数序列化后存入 Redis。
画面 11: 展示 queryPayChannelParamByAppPlatform 方法的实现，光标位于 return payChannelParamDTOs 语句处，显示了返回查询到的参数列表。
画面 12: 展示 queryPayChannelParamByAppPlatform 方法的实现，光标位于 payChannelParamMapper.select(...) 语句处，显示了查询数据库。
画面 13: 展示 updateCache 方法的实现，光标位于 updateCache(...) 语句处，显示了调用 updateCache 方法。
画面 14: 展示课程大纲，当前章节为 5.6.1 需求分析，说明渠道参数查询频繁，为提高性能将参数缓存到 Redis 中，以及 5.6.2 搭建 redis 环境，需要安装 redis 并在 Nacos 中添加 spring-boot-redis.yaml 配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
5.6.3 保存缓存
保存渠道参数成功，同时将渠道参数保存在Redis中。
修改交易服务保存支付渠道参数接口，修改PayChannelServiceImpl中的savePayChannelParam方法：
```

画面 2:
```
private void updateCache(String appid, String platformChannelCode) {
    //根据应用和业务类型查询支付渠道参数列表写入redis
    String redisKey = RedisUtil.keyBuilder(appid, platformChannelCode);
    Boolean exists = cache.exists(redisKey);
    if (exists) {
        cache.del(redisKey);
    }
    //根据应用和业务类型查询支付渠道参数列表写入redis
    List<PayChannelParamDTO> payChannelParamDTOs = queryPayChannelParamByAppPlatform(appid, platformChannelCode);
    if (payChannelParamDTOs != null) {
        //将payChannelParamDTOs转换成json存入redis
        cache.set(redisKey, JSON.toJSONString(payChannelParamDTOs));
    }
}
```

画面 3:
```
private void updateCache(String appid, String platformChannelCode) {
    //根据应用和业务类型查询支付渠道参数列表写入redis
    String redisKey = RedisUtil.keyBuilder(appid, platformChannelCode);
    Boolean exists = cache.exists(redisKey);
    if (exists) {
        cache.del(redisKey);
    }
    //根据应用和业务类型查询支付渠道参数列表写入redis
    List<PayChannelParamDTO> payChannelParamDTOs = queryPayChannelParamByAppPlatform(appid, platformChannelCode);
    if (payChannelParamDTOs != null) {
        //将payChannelParamDTOs转换成json存入redis
        cache.set(redisKey, JSON.toJSONString(payChannelParamDTOs));
    }
}
```

画面 4:
```
private void updateCache(String appid, String platformChannelCode) {
    //根据应用和业务类型查询支付渠道参数列表写入redis
    String redisKey = RedisUtil.keyBuilder(appid, platformChannelCode);
    Boolean exists = cache.exists(redisKey);
    if (exists) {
        cache.del(redisKey);
    }
    //根据应用和业务类型查询支付渠道参数列表写入redis
    List<PayChannelParamDTO> payChannelParamDTOs = queryPayChannelParamByAppPlatform(appid, platformChannelCode);
    if (payChannelParamDTOs != null) {
        //将payChannelParamDTOs转换成json存入redis
        cache.set(redisKey, JSON.toJSONString(payChannelParamDTOs));
    }
}
```

画面 5:
```
package com.shanju.pay.common.util;

public class RedisUtil {

    //主键前缀标识
    public static final String KEY_PREFIX = "SJ_PAY_PARAM";

    //分隔字符，默认[.]，使用，可用于redis分组查询
    private static final String KEY_SPLIT_CHAR = ".";
```

画面 6:
```
public static String keyBuilder(String module, String func, String... args) {
    return keyBuilder(prefix, module, func, args);
}

public static String keyBuilder(String prefix, String module, String func, String objStr) {
    return keyBuilder(prefix, module, func, new String[]{objStr});
}
```

画面 7:
```
private void updateCache(String appid, String platformChannelCode) {
    //根据应用和业务类型查询支付渠道参数列表写入redis
    String redisKey = RedisUtil.keyBuilder(appid, platformChannelCode);
    Boolean exists = cache.exists(redisKey);
    if (exists) {
        cache.del(redisKey);
    }
    //根据应用和业务类型查询支付渠道参数列表写入redis
    List<PayChannelParamDTO> payChannelParamDTOs = queryPayChannelParamByAppPlatform(appid, platformChannelCode);
    if (payChannelParamDTOs != null) {
        //将payChannelParamDTOs转换成json存入redis
        cache.set(redisKey, JSON.toJSONString(payChannelParamDTOs));
    }
}
```

画面 8:
```
private void updateCache(String appid, String platformChannelCode) {
    //根据应用和业务类型查询支付渠道参数列表写入redis
    String redisKey = RedisUtil.keyBuilder(appid, platformChannelCode);
    Boolean exists = cache.exists(redisKey);
    if (exists) {
        cache.del(redisKey);
    }
    //根据应用和业务类型查询支付渠道参数列表写入redis
    List<PayChannelParamDTO> payChannelParamDTOs = queryPayChannelParamByAppPlatform(appid, platformChannelCode);
    if (payChannelParamDTOs != null) {
        //将payChannelParamDTOs转换成json存入redis
        cache.set(redisKey, JSON.toJSONString(payChannelParamDTOs));
    }
}
```

画面 9:
```
//根据应用和业务类型查询支付渠道参数列表写入redis
String redisKey = RedisUtil.keyBuilder(appid, platformChannelCode);
Boolean exists = cache.exists(redisKey);
if (exists) {
    cache.del(redisKey);
}
//根据应用和业务类型查询支付渠道参数列表写入redis
List<PayChannelParamDTO> payChannelParamDTOs = queryPayChannelParamByAppPlatform(appid, platformChannelCode);
if (payChannelParamDTOs != null) {
    //将payChannelParamDTOs转换成json存入redis
    cache.set(redisKey, JSON.toJSONString(payChannelParamDTOs));
}
```

画面 10:
```
//根据应用和业务类型查询支付渠道参数列表写入redis
String redisKey = RedisUtil.keyBuilder(appid, platformChannelCode);
Boolean exists = cache.exists(redisKey);
if (exists) {
    cache.del(redisKey);
}
//根据应用和业务类型查询支付渠道参数列表写入redis
List<PayChannelParamDTO> payChannelParamDTOs = queryPayChannelParamByAppPlatform(appid, platformChannelCode);
if (payChannelParamDTOs != null) {
    //将payChannelParamDTOs转换成json存入redis
    cache.set(redisKey, JSON.toJSONString(payChannelParamDTOs));
}
```

画面 11:
```
public List<PayChannelParamDTO> queryPayChannelParamByAppPlatform(String appid, String platformChannelCode) {
    //先从redis查询，如果存在则返回渠道参数
    String redisKey = RedisUtil.keyBuilder(appid, platformChannelCode);
    Boolean exists = cache.exists(redisKey);
    if (exists) {
        String payChannelParamDTOsString = cache.get(redisKey);

