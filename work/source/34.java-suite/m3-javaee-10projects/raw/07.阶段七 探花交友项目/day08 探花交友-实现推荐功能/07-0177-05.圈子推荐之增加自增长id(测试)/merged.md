# 05.圈子推荐之增加自增长id（测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\05.圈子推荐之增加自增长id（测试）_【海量资源尽在 666java.com】.mp4
- 时长 3分0秒（音频 180s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来测试一下我们的这个新增这个publish动态啊那我们来看一下这个刚刚我们编写的这个逻辑是否是ok的好那么我们在这个方法中啊就是刚刚我们所编写的我们这个叫做c5啊publish这个方法中我们去打一个断点然后呢我们去看一下测试用力这个呢之前我们写过的测试用力啊那我们就直接来执行一个debug
[00:28] 好那我们来等待它的一个执行好那么断点呢就进来了我们来执行一下走走走走往下面走呃然后呢我们去进入这个方法啊那我们来看一下然后呢往下面去走然后呢再进入一下哎走呃那么我们就继续往下面走走走走呃然后呢我们是应该去进入到这个方法呢我们就呃
[00:56] 来找一下啊那么我们就在这个里面吧直接来打个断点好通过一下啊这样比较快一点然后呢呃走转成大写我们去判断是否存在呃他显然肯定是不存在的对吧那么肯定返回是fos那么就执行到下面来然后呢走走去做一个自增长那我们来看一下他的一个自增长之后的值是多少呢这个自增长之后的值呢是1呃然后呢我们做一个pool的操作
[01:25] 然后呢报错了我们来看一下什么错误啊那么这个异常呢是在这个位置他说我们不能把这个浪啊去转成string那么这个是什么意思呢是我们刚刚在存入我们这个ID的时候啊那我们直接存入的是这个ID那这个值呢它本身是一个浪类型啊那我们需要把它
[01:49] 做一个to stream这样的一个处理然后呢我们再次去做一个测试看它OK不OK好那么我们再次启动好那么端点呢又进来了然后呢我们走直接通过吧走走到这个位置来走走走依然是不存在的对吧那么原因是我们刚刚没有存进去它继续做一个支撑着走然后呢
[02:11] 这回就重进去了对吧然后走我们来看一下publish它的ID是几这个是不是2对吧然后走通过好我们来看一下我们的mongodbmongodb中我们来刷新一下我们来找到publish那么可以看到只有一条数据其中pid为2就是我们刚刚自增长的ID我们可以再次去做一个执行我们来看一下它的一个结果
[02:39] 好,那么我们就直接通过看最后的结果就可以了那么我们在这个位置来刷新一下然后可以看到第二条数据的这个ID是不是变成3了那么它就会做一个自增长了也OK好,那么关于我们这个自增长ID的一个测试呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
2019-10-08 14:56:16.774 INFO 752 --- [Thread-4] org.apache.ZooKeeper.ClientCnxn : Session establishment complete
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

