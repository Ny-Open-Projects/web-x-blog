# 画面线理解：08_图片缓存_监听消息测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\08_图片缓存_监听消息测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:22, 00:48, 00:59, 01:09, 01:29, 01:55, 02:04, 02:25, 02:47, 03:03, 03:17, 03:37, 04:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:50:55

1) 这一组画面整体在讲如何通过 Kafka 消费热点文章数据，并利用 Spring Boot 和 Quartz 定时任务，结合 Redis 缓存和数据库操作，实现对文章图片的处理与缓存。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Navicat for MySQL 中的 `ap_article` 表，其中 `images` 字段包含文章图片 URL，用于后续处理。
画面2：Navicat 中 `ap_article` 表的另一视角，展示作者、频道等字段，以及部分图片 URL。
画面3：IDEA 中 `HotArticleListener.java` 代码，定义了 Kafka 消费者方法 `onMessage`，用于接收热点文章数据。
画面4：IDEA 中 `AppHotArticleQuartz.java` 代码，定义了定时任务 `executeInternal` 方法，用于触发文章图片处理。
画面5：IDEA 中 `AppHotArticleQuartz.java` 代码，展示定时任务触发器配置 `descTrigger`，设置为“每0天0小时0分5秒执行一次”。
画面6：IDEA 中 `HotArticleListener.java` 代码，调试断点设置在 `onMessage` 方法中，准备接收消息。
画面7：IDEA 中 `HotArticleImageServiceImpl.java` 代码，展示 `handleHotImage` 方法，用于处理热点文章图片。
画面8：IDEA 中 `HotArticleImageServiceImpl.java` 代码，展示使用 `JSOM` 解析文章内容中的图片 URL。
画面9：IDEA 中 `HotArticleImageServiceImpl.java` 代码，展示从数据库查询文章详情，并缓存图片。
画面10：Navicat 中 `ap_article` 表，展示文章数据，用于调试和验证。
画面11：IDEA 中 `HotArticleImageServiceImpl.java` 代码，展示从数据库查询文章详情并赋值给 `apArticle` 对象。
画面12：IDEA 中 `HotArticleImageServiceImpl.java` 代码，展示遍历图片 URL 并缓存到 Redis。
画面13：IDEA 中 `HotArticleListener.java` 代码，展示 `onMessage` 方法中处理消息的逻辑。
画面14：IDEA 中 `AppHotArticleQuartz.java` 代码，展示定时任务触发器配置 `trigger`，设置为“0 0/5 * * * ?”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面3：
```java
@Override
public String topic() {
    return kafkaTopicConfig.getHotArticle();
}

@Override
public void onMessage(ConsumerRecord<String, String> data, Consumer<?, ?> consumer) {
    log.info("接收到热点文章消息为：{}", data);
    try {
        ApotArticleMessage message = mapper.readValue(value, ApotArticleMessage.class);
        hotArticleImageService.handleHotImage(message);
    } catch (IOException e) {
        e.printStackTrace();
    }
    log.error("接收消息失败，错误消息：{}", e);
}
```

画面4：
```java
@Override
protected void executeInternal(JobExecutionContext context) throws JobExecutionException {
    long currentTimeMillis = System.currentTimeMillis();
    log.info("开始定时计算分值");
    apHotArticleService.computeHotArticle();
    log.info("计算分值完成，耗时：{}毫秒", System.currentTimeMillis() - currentTimeMillis);
}
```

画面5：
```java
@Override
public String descTrigger() {
    return new String[]{"0 0/5 * * * ?"};
}
```

画面7：
```java
@Override
public void handleHotImage(ApotArticleMessage message) {
    log.info("处理热点文章图片开始articleId: {}, message: {}", message.getArticleId(), message);
    AparticleContent aparticleContent = aparticleContentMapper.selectByArticleId(message.getArticleId());
    if (aparticleContent != null && aparticleContent.getImages() != null) {
        String[] articleImages = aparticleContent.getImages().split(",");
        for (String im : articleImages) {
            log.info("处理图片：{}", im);
            cacheImageService.cacheRedisUrl(im, true);
        }
    }
    log.info("处理热点文章图片结束：{}", message);
}
```

画面8：
```java
String content = JSOMUtils.parseJsonArray(content, content);
for (int i = 0; i < array.size(); i++) {
    JSONObject obj = array.get(i);
    if (!"image".equals(obj.getString("type"))) {
        continue;
    }
}
```

画面9：
```java
ApArticle apArticle = apArticleMapper.selectById(Long.valueOf(message.getArticleId()));
if (apArticle != null && StringUtils.isNotEmpty(apArticle.getImages())) {
    String[] articleImages = apArticle.getImages().split(",");
    for (String im : articleImages) {
        log.info("非热门图片不进行缓存articleId: {}, message: {}", message.getArticleId(), message);
        continue;
    }
    cacheImageService.cacheRedisUrl(im, true);
}
```

画面11：
```java
ApArticle apArticle = apArticleMapper.selectById(Long.valueOf(message.getArticleId()));
```

画面12：
```java
for (String im : articleImages) {
    log.info("非热门图片不进行缓存articleId: {}, message: {}", message.getArticleId(), message);
    continue;
}
cacheImageService.cacheRedisUrl(im, true);
```

画面14：
```java
@Component
@Scheduled(cron = "0 0/5 * * * ?")
public class AppHotArticleQuartz extends AbstractJob {
    @Override
    public String trigger() {
        return new String[]{"0 0/5 * * * ?"};
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
