# 画面线理解：05.圈子推荐之增加自增长id（测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\05.圈子推荐之增加自增长id（测试）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:16, 00:32, 00:42, 00:51, 01:01, 01:13, 01:28, 01:38, 01:49, 02:03, 02:11, 02:22, 02:39, 02:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:53:58

1) 这一组画面整体在讲如何在 Dubbo 服务中，通过 Redis 生成全局唯一的 ID 并保存到 MongoDB 中，同时展示相关测试用例的执行过程。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 QuanzApiImpl.java 中保存发布内容的代码，调用 idService.createId() 生成 ID 并保存到 MongoDB。
画面2: 展示 TestQuanz.testSavePublish 测试用例执行，其中对 publish 对象进行校验，若 userId 为空则返回 false。
画面3: 展示 Publish.java 类的定义，包含 id、userId、text、medias 等字段，以及 @AllArgsConstructor 和 @Document 注解。
画面4: 展示 ObjectId.java 中 toHexString() 方法的实现，用于将 ObjectId 转换为十六进制字符串。
画面5: 展示 IdService.java 中 createId 方法的实现，通过 Redis 的 hash 结构生成并存储 ID。
画面6: 展示 IdService.java 中 Redis 操作的细节，将生成的 ID 通过 opsForHash().put() 写入 Redis。
画面7: 展示测试用例执行日志，包含 MongoDB 连接、Zookeeper 会话建立等信息。
画面8: 展示测试用例执行日志，包含 Spring Boot 启动、Redis 序列化器配置等信息。
画面9: 展示 IdService.java 中 Long 类型的 toString() 方法，用于调试或日志输出。
画面10: 展示 IdService.java 中 createId 方法的执行过程，其中 hashKey 为 "TANHUA_ID_PUBLISH"。
画面11: 展示 IdService.java 中 createId 方法的执行过程，其中 key 为 "TANHUA_ID_PUBLISH"，并执行 opsForHash().put()。
画面12: 展示 MongoDB Compass 中的 quanzi_publish 集合，显示了多个 ObjectId 的文档。
画面13: 展示 QuanzApiImpl.java 中保存发布内容的代码，以及测试日志中 ProfileValueUtils 和日志初始化警告。
画面14: 展示 IdService.java 中 createId 方法的执行过程，其中 hashKey 为 "TANHUA_ID_PUBLISH"。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1:
```java
publish.setId(ObjectId.get());
publish.setCreated(System.currentTimeMillis()); //发布时时间戳
publish.setSeeType(1); //查看权限
publish.setPid(this.idService.createId(type: "publish", p
this.mongoTemplate.save(publish);
```

画面2:
```java
if (publish.getUserId() == null) {
    return false;
}
```

画面3:
```java
@AllArgsConstructor
@Document(collection = "quanzi_publish")
public class Publish implements java.io.Serializable {
    private static final long serialVersionUID = -8732308321082804771L;
    private ObjectId id; //主键id，用于存储系统的模型
    private Long pid; //用于存储系统的模型
    private Long userId; //用户id
    private String text; //文字：今天天气不错
    private List<String> medias; //媒体数据，图片或小视频 url
}
```

画面4:
```java
public String toHexString() {
    char[] chars = new char[24]; chars = {5, d, 6, 7, 8, 9, A, B, C, D, E, F};
    int i = 0;
    for (byte b : toByteArray()) { b = -100
    chars[i++] = HEX_CHARS[b & 0xF];
    }
    return new String(chars);
}
```

画面5:
```java
public Long createId(String type, String objectId) {
    Type = StringUtils.upperCase(type);
    String hashKey = "TANHUA_HASH_ID_" + type;
    if(this.redisTemplate.opsForHash().hasKey(hashKey, objectId))
        return Long.valueOf(this.redisTemplate.opsForHash().get(hashKey, objectId));
    return 0L;
}
```

画面6:
```java
String key = "TANHUA_ID_" + type;
Long id = this.redisTemplate.opsForValue().increment(key);
this.redisTemplate.opsForHash().put(hashKey, objectId, id);
return id;
```

画面7:
```java
//日志信息
2019-10-08 14:56:16.764 INFO 752 --- [Thread-5] d.c.e.AwaitingNonWebApplicationListener : Started TestQuanzi in 30.641 seconds
2019-10-08 14:56:16.774 INFO 752 --- [Thread-4] org.apache.zookeeper.ClientCnxn : Session establishment complete
```

画面8:
```java
//日志信息
14:58:05.115 [main] DEBUG org.springframework.test.annotation.ProfileValueUtils - ...
14:58:05.125 [main] DEBUG org.springframework.test.context.support.DependencyInjection...
14:58:05.161 [main] DEBUG org.springframework.test.context.support.TestPropertySource...
log4j:WARN No appenders could be found for logger (com.alibaba.dubbo.common.logger.log4j)
log4j:WARN Please initialize the log4j system properly.
```

画面9:
```java
//Long 类型的 toString 方法
public String toString() {
    return String.valueOf(value);
}
```

画面10:
```java
public Long createId(String type, String objectId) {
    type = StringUtils.upperCase(type);
    String hashKey = "TANHUA_HASH_ID_" + type;
    if(this.redisTemplate.opsForHash().hasKey(hashKey, objectId))
        return Long.valueOf(this.redisTemplate.opsForHash().get(hashKey, objectId));
    return 0L;
}
```

画面11:
```java
String key = "TANHUA_ID_" + type;
Long id = this.redisTemplate.opsForValue().increment(key);
this.redisTemplate.opsForHash().put(hashKey, objectId, id);
return id;
```

画面12:
```json
{
  "key": "quanzi_publish",
  "value": [
    {
      "id": "ObjectId('5d84c32b04d3040d02f0bfb6')",
      "fields": 9
    }
  ]
}
```

画面13:
```java
publish.setCreated(System.currentTimeMillis()); //发布时时间戳
publish.setSeeType(1); //查看权限
publish.setPid(this.idService.createId(type: "publish", p
this.mongoTemplate.save(publish);
```

画面14:
```java
public Long createId(String type, String objectId) {
    type = StringUtils.upperCase(type);
    String hashKey = "TANHUA_HASH_ID_" + type;
    if(this.redisTemplate.opsForHash().hasKey(hashKey, objectId))
        return Long.valueOf(this.redisTemplate.opsForHash().get(hashKey, objectId));
    return 0L;
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不评价画面美观，不输出与课程无关的内容。
