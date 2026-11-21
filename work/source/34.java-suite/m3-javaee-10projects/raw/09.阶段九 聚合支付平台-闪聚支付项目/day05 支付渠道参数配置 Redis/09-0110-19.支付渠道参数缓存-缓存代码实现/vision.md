# 画面线理解：19.支付渠道参数缓存-缓存代码实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\19.支付渠道参数缓存-缓存代码实现【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:54, 02:31, 04:17, 05:21, 06:32, 07:13, 08:20, 08:47, 09:17, 10:14, 11:02, 11:28, 11:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:30:20

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
