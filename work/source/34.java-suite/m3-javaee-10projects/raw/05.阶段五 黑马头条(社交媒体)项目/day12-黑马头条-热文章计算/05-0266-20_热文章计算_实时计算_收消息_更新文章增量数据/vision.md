# 画面线理解：20_热文章计算_实时计算_收消息_更新文章增量数据

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\20_热文章计算_实时计算_收消息_更新文章增量数据【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:17, 00:53, 01:41, 02:41, 03:08, 04:08, 04:41, 05:22, 05:54, 06:31, 07:12, 07:54, 08:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:44:52

1) 这一组画面整体在讲如何通过 Kafka 消息驱动，结合 Spring Boot 和 MyBatis，实现文章浏览量、点赞数等数据的实时增量更新。

2) 按时间顺序列出每张画面的要点：
画面1：展示 ArticleIncrHandleListener 类，其中注入了 KafkaTopicConfig，并定义了 onMessage 方法，用于处理 Kafka 消息。
画面2：展示 HotArticleStreamHandler 类，其中定义了 sendTopic 和 getStream 方法，用于处理流式数据。
画面3：在 IDEA 中使用全局搜索功能，查找与 ArticleIncrHandleListener 相关的类和文件。
画面4：在 Typora 中查看文档，内容为“3.2.5 更新文章增量数据”，并展示 ApArticleMapper.xml 中的 updateArticleView SQL 语句。
画面5：在 Typora 中查看文档，内容为“3.2.5 更新文章增量数据”，并展示 AppArticleService 接口和实现类中的 updateArticleView 方法。
画面6：在 IDEA 中查看项目结构，定位到 AppArticleService 接口。
画面7：在 IDEA 中查看 AppArticleServiceImpl 类，展示其构造函数和成员变量。
画面8：在 IDEA 中查看 AppArticleServiceImpl 类，展示 updateArticleView 方法的实现。
画面9：在 IDEA 中查看 AppArticleServiceImpl 类，展示 updateArticleView 方法的实现，其中调用 aparticleMapper.updateArticleView。
画面10：在 IDEA 中查看 ArticleIncrHandleListener 类，展示其构造函数和成员变量。
画面11：在 IDEA 中查看 ArticleIncrHandleListener 类，展示其构造函数和成员变量。
画面12：在 IDEA 中查看 ArticleIncrHandleListener 类，展示其构造函数和成员变量。
画面13：在 IDEA 中查看 ArticleIncrHandleListener 类，展示其构造函数和成员变量。
画面14：在 IDEA 中查看 ArticleIncrHandleListener 类，展示其 onMessage 方法的完整实现，包括日志记录、消息解析和调用服务层方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Component
@Slf4j
public class ArticleIncrHandleListener implements KafkaListener<String, String> {
    @Autowired
    private KafkaTopicConfig kafkaTopicConfig;

    @Override
    public String topic() {
        return kafkaTopicConfig.getArticleIncrHandle();
    }

    @Override
    public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {

    }
}
```

画面2：
```java
@Mutated
private KafkaTopicConfig kafkaTopicConfig;
private ObjectMapper mapper;

@Override
public String listenerTopic() {
    return kafkaTopicConfig.getArticleIncrHandle();
}

@Override
public String sendTopic() {
    return kafkaTopicConfig.getArticleIncrHandle();
}

@Override
public Stream<String> getStream(String stream) {
    return stream.map((key, val) -> {
        UpdatedArticleMessage value = Format(val);
        System.out.println(value);
        return value;
    });
}
```

画面4：
```xml
<update id="updateArticleView">
    UPDATE ap_article SET
    views = GREATEST(IFNULL(views,0) + #{viewCount}, #{viewCount}),
    collection = GREATEST(IFNULL(collection,0) + #{collectCount}, #{collectCount}),
    comment = GREATEST(IFNULL(comment,0) + #{commentCount}, #{commentCount}),
    likes = GREATEST(IFNULL(likes,0) + #{likeCount}, #{likeCount})
    WHERE id = #{articleId}
</update>
```

画面5：
```java
ResponseResult updateArticleView(ArticleVisitStreamDto dto);
```

画面6：
```java
package com.heima.article.service;

import com.heima.article.dto.ArticleVisitStreamDto;
import com.heima.article.dto.ArticleVisitStreamDto;
import com.heima.article.dto.ArticleVisitStreamDto;

public interface AppArticleService {
    ResponseResult load(ArticleVisitStreamDto dto, Short type);
}
```

画面7：
```java
@Autowired
private ApArticleMapper aparticleMapper;
```

画面8：
```java
@Override
public ResponseResult updateArticleView(ArticleVisitStreamDto dto) {
    aparticleMapper.updateArticleView(dto.getArticleId(), dto.getView(), dto.getCollect(), dto.getComment(), dto.getLike());
    return null;
}
```

画面9：
```java
@Override
public ResponseResult updateArticleView(ArticleVisitStreamDto dto) {
    int rows = aparticleMapper.updateArticleView(dto.getArticleId(), dto.getView(), dto.getCollect(), dto.getComment(), dto.getLike());
    return ResponseResult.okResult(rows);
}
```

画面10：
```java
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
```

画面11：
```java
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
```

画面12：
```java
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
```

画面13：
```java
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
```

画面14：
```java
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    log.info("接收到的消息为：{}", data);
    ArticleVisitStreamMessage message = mapper.readValue(data, ArticleVisitStreamMessage.class);
    ArticleVisitStreamDto dto = message.getData();
    appArticleService.updateArticleView(dto);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4：PPT标题为“3.2.5 更新文章增量数据”，内容包括“（1）mapper定义”和“（2）service定义”。
画面5：PPT标题为“3.2.5 更新文章增量数据”，内容包括“（2）service定义”。
画面6：无PPT内容。
画面7：无PPT内容。
画面8：无PPT内容。
画面9：无PPT内容。
画面10：无PPT内容。
画面11：无PPT内容。
画面12：无PPT内容。
画面13：无PPT内容。
画面14：无PPT内容。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。
