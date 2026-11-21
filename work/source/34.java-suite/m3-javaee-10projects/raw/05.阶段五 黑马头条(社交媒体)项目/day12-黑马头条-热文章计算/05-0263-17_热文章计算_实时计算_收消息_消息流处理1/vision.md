# 画面线理解：17_热文章计算_实时计算_收消息_消息流处理1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\17_热文章计算_实时计算_收消息_消息流处理1【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:37, 01:21, 02:30, 03:46, 04:13, 05:14, 05:56, 06:24, 07:16, 08:15, 09:02, 10:02, 11:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:43:06

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Kafka Stream 处理文章行为事件，并通过自定义的 `BehaviorMessageSender` 发送消息，同时展示相关代码结构和调试过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 项目结构：`heima-leadnews-article` 模块下的 `stream` 包中包含 `HotArticleStreamHandler.java`。
- 代码：`HotArticleStreamHandler` 类中定义了 `listenTopic()` 和 `sendTopic()` 方法，返回 Kafka Topic 名称。
- 代码：`getService()` 方法返回 `null`。

画面 2：
- 项目结构：`heima-leadnews-article` 模块下的 `stream` 包中包含 `HotArticleStreamHandler.java`。
- 代码：`HotArticleStreamHandler` 类中 `sendTopic()` 方法返回 `kafkaTopicConfig.getArticleIncHandle()`。

画面 3：
- 代码：`getService()` 方法中 `stream.map(...)` 的 `value` 变量被赋值后，`return new KeyValue<>("","")`。
- 代码：`return null;`。

画面 4：
- 项目结构：`heima-leadnews-article` 模块下的 `stream` 包中包含 `HotArticleStreamHandler.java`。
- 代码：`HotArticleStreamHandler` 类中 `getService()` 方法返回 `stream.map(...)` 的结果。

画面 5：
- 项目结构：`heima-leadnews-behavior` 模块下的 `src/main/java/com/heima/behavior` 包中包含 `BehaviorMessageSender.java`。
- 代码：`BehaviorMessageSender` 类中 `sendArticlePlus()` 方法接收 `UpdateArticleMessage` 和用户 ID，调用 `kafkaSender.sendArticlePlus(...)`。

画面 6：
- 代码：`BehaviorMessageSender` 类中 `sendArticlePlus()` 方法中 `UpdateArticleMessage temp = parseMessage(...)`。
- 代码：`kafkaSender.sendArticlePlus(temp);`。

画面 7：
- 代码：`HotArticleStreamHandler` 类中 `getService()` 方法中 `stream.map(...)` 的 `value` 变量被赋值后，`return new KeyValue<>("","")`。
- 代码：`return null;`。

画面 8：
- 代码：`IntConfig.java` 文件中 `@ComponentScan` 注解的 `value` 属性包含 `com.heima.common.quartz`, `com.heima.common.kafka`, `com.heima.common.kafkastream`。

画面 9：
- 代码：`BehaviorMessageSender` 类中 `sendArticlePlus()` 方法中 `UpdateArticleMessage temp = parseMessage(...)`。
- 代码：`kafkaSender.sendArticlePlus(temp);`。

画面 10：
- 代码：`BehaviorTest` 类中 `testLikesSave()` 方法中 `AppUser user = new AppUser();`。
- 代码：`user.setId(1L);`。
- 代码：`LikesBehaviorDTO dto = new LikesBehaviorDTO();`。
- 代码：`dto.setArticleId(10120);`。
- 代码：`dto.setOperation((short) 1);`。
- 代码：`dto.setType((short) 1);`。
- 代码：`applikesBehaviorService.saveLikesBehavior(dto);`。

画面 11：
- 代码：`HotArticleStreamHandler` 类中 `getService()` 方法中 `stream.map(...)` 的 `value` 变量被赋值后，`return new KeyValue<>("","")`。
- 代码：`return null;`。

画面 12：
- 代码：`HotArticleStreamHandler` 类中 `getService()` 方法中 `stream.map(...)` 的 `value` 变量被赋值后，`return new KeyValue<>("","")`。
- 代码：`return null;`。

画面 13：
- 代码：`HotArticleStreamHandler` 类中 `getService()` 方法中 `stream.map(...)` 的 `value` 变量被赋值后，`return new KeyValue<>("","")`。
- 代码：`return null;`。

画面 14：
- 代码：`HotArticleStreamHandler` 类中 `getService()` 方法中 `stream.map(...)` 的 `value` 变量被赋值后，`return new KeyValue<>("","")`。
- 代码：`return null;`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1：
```java
@Autowired
private KafkaTopicConfig kafkaTopicConfig;

@Override
public String listenTopic() {
    return kafkaTopicConfig.getArticleUpdateBus();
}

@Override
public String sendTopic() {
    return kafkaTopicConfig.getArticleIncHandle();
}

@Override
public KStream<?, String> getService(KStream<?, String> stream) {
    return null;
}
```

画面 2：
```java
public class HotArticleStreamHandler implements KafkaStreamListener<KStream<?, String>> {
    @Autowired
    private KafkaTopicConfig kafkaTopicConfig;

    @Override
    public String listenTopic() {
        return kafkaTopicConfig.getArticleUpdateBus();
    }

    @Override
    public String sendTopic() {
        return kafkaTopicConfig.getArticleIncHandle();
    }

    @Override
    public KStream<?, String> getService(KStream<?, String> stream) {
        return null;
    }
}
```

画面 3：
```java
public KStream<?, String> getService(KStream<?, String> stream) {
    return stream.map((key, val) -> {
        UpdateArticleMessage value = format(val);
        return new KeyValue<>("", "");
    });
}
```

画面 4：
```java
public KStream<?, String> getService(KStream<?, String> stream) {
    return stream.map((key, val) -> {
        UpdateArticleMessage value = format(val);
        return new KeyValue<>("", "");
    });
}
```

画面 5：
```java
public class BehaviorMessageSender {
    @Autowired
    private KafkaTopicConfig kafkaTopicConfig;

    public void sendArticlePlus(UpdateArticleMessage message, Long userId, boolean isSendArticle) {
        UpdateArticleMessage temp = parseMessage(message, userId, isSendArticle);
        kafkaSender.sendArticlePlus(temp);
    }
}
```

画面 6：
```java
public void sendArticlePlus(UpdateArticleMessage message, Long userId, boolean isSendArticle) {
    UpdateArticleMessage temp = parseMessage(message, userId, isSendArticle);
    kafkaSender.sendArticlePlus(temp);
}
```

画面 7：
```java
public KStream<?, String> getService(KStream<?, String> stream) {
    return stream.map((key, val) -> {
        UpdateArticleMessage value = format(val);
        System.out.println(value);
        return new KeyValue<>("", "");
    });
}
```

画面 8：
```java
@ComponentScan(value = {
    "com.heima.common.quartz",
    "com.heima.common.kafka",
    "com.heima.common.kafkastream"
})
```

画面 9：
```java
public void sendArticlePlus(UpdateArticleMessage message, Long userId, boolean isSendArticle) {
    UpdateArticleMessage temp = parseMessage(message, userId, isSendArticle);
    kafkaSender.sendArticlePlus(temp);
}
```

画面 10：
```java
@Test
public void testLikesSave() {
    AppUser user = new AppUser();
    user.setId(1L);
    LikesBehaviorDTO dto = new LikesBehaviorDTO();
    dto.setArticleId(10120);
    dto.setOperation((short) 1);
    dto.setType((short) 1);
    applikesBehaviorService.saveLikesBehavior(dto);
}
```

画面 11：
```java
public KStream<?, String> getService(KStream<?, String> stream) {
    return stream.map((key, val) -> {
        UpdateArticleMessage value = format(val);
        System.out.println(value);
        return new KeyValue<>("", "");
    });
}
```

画面 12：
```java
public KStream<?, String> getService(KStream<?, String> stream) {
    return stream.map((key, val) -> {
        UpdateArticleMessage value = format(val);
        System.out.println(value);
        return new KeyValue<>("", "");
    });
}
```

画面 13：
```java
public KStream<?, String> getService(KStream<?, String> stream) {
    return stream.map((key, val) -> {
        UpdateArticleMessage value = format(val);
        System.out.println(value);
        return new KeyValue<>("", "");
    });
}
```

画面 14：
```java
public KStream<?, String> getService(KStream<?, String> stream) {
    return stream.map((key, val) -> {
        UpdateArticleMessage value = format(val);
        System.out.println(value);
        return new KeyValue<>("", "");
    });
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
