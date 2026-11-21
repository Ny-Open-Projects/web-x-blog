# 08_图片缓存_监听消息测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\08_图片缓存_监听消息测试【海量资源尽在 666java.com】.mp4
- 时长 4分17秒（音频 257s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去测试一下啊那测试的方式呢其实就要干嘛呢你需要去设置一些数据这数据是这样啊你看我这里边有三条数据并且这个时间的发布时间呢我都是大于当前的时间啊所以说呢大于昨天应该大于昨天啊这样的话呢就能去找到这三条数据进行缓存同时呢我在这呢去设置了一个这种这种
[00:24] 是本地的图片因为大部分数据都是从爬中来的所以说我是改了一张图片这个图片就能进行缓存好吧你要想去测试的话非常简单你在这打断连然后你就可以去启动当前的image右键debug然后你再次去启动当前的article就可以了这样的话它就会自动的去发送消息用它
[00:57] 这啊咱们在这儿去定做了个定时他没两分钟啊没两分钟的就会去发送一次然后计算分值并且是处理当前图片啊右键咱们也右键去debug一下走啊稍等一下啊这个可能时间稍微再耗点时间稍等一下好马上跑完了啊那跑完之后看看啊啊这数据其实已经拿到了看到了吗这数据啊其实已经拿到了啊咱们可以往下去走了啊往下走走
[01:32] 嗯咱们可以看一下这个数据是啥这个是不是有一个10120看到了吧当前的10120嗯这其他也看不着是吧咱们可以这样啊我们可以在这打断点让他过来过来之后呢咱们可以去获取到这个消息你看当前的这个热点文章是这些是吧没问题吧就是10120是吧然后呢咱们下面就可以去获取他的内容好获取内容看看能不能拿到内容啊
[02:02] 内容是已经拿到了是吧然后呢是去解析内容里面的图片进行干嘛呢进行换存但是这个内容的图片应该都是干都是啥呢应该都是目前啊目前应该都是当前的这种爬虫者的数据啊所以说他应该不会不会进行换存那这样吧咱们直接到这儿好吧直接到这儿啊看看当前article中有没有本地的图片啊好直接放行过来然后往下走这时候你可以看一下article呦走
[02:37] 看不着是吗我看这在这看吧但是这个图片好像也不行是吧也不行那这样咱们直接放行直接放行因为刚才我是准备了三点数据他总有一条会去能拿到的好咱们直接放行了就放行他是不是又来了好往下走还是到封面怎么可以往下走一步你可以看一下这个数据这数据这条数据是不是就是当前包含了当前的这个潜坠
[03:09] 那这时候那这个图片肯定会干嘛呢肯定会进行缓存好往下走然后咱们看一下能不能缓存成功啊走走走看看他是不是以这个前缀啊很显然嗯不是那这时候呢咱们就要干嘛呢就要去进行缓存了啊好往下走好就已经缓存成功了啊这时候已经缓存成功了啊在咱们的redis中其实已经有了这么一套数据好可以直接放行了啊好那这数据啊其实已经做完了
[03:39] 其实我这里边有三条数据那么还有呢还有的方式还有的原因呢其实就是啥呢就是当前我每两分钟执行一次所以说呢他那时间点又到了又去审核了一次所以说这个数据啊一直在重复啊当然这个咱们可以关掉啊因为咱们在正常的这种逻辑中应该是什么时候去执行一次啊应该是在这去试了个0.05分是吧也就是说每天凌晨的0.05分才会去执行一次
[04:07] 好那行那这个啊这个当前的这种收发数据并显得是审核不是审核应该是处理当前图片的缓存咱们就做到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
        ApotArticleMessage message = Mapper.readValue(value, ApotArticleMessage.class);
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

