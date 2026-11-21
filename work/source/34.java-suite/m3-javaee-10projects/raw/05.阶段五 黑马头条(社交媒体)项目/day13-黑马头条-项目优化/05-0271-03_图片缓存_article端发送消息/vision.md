# 画面线理解：03_图片缓存_article端发送消息

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\03_图片缓存_article端发送消息【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:40, 01:06, 01:26, 01:53, 02:20, 02:37, 03:00, 03:31, 03:59, 04:22, 05:06, 05:21, 05:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:47:21

1) 这一组画面整体在讲什么（一句话）：
实现文章热度计算后，通过 Kafka 发送热点文章消息到指定主题。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档“1.1 功能需求”，说明要实现热点文章缓存图片功能，以及“1.2 article微服务发送消息”章节，列出 Kafka 主题名称 `kafka.topic.hot-article`。
画面2：展示代码 `sendHotArticleMessage` 方法，用于发送热点文章消息，参数为 `ApiHotArticleMessage` 对象。
画面3：展示项目目录结构，重点是 `maven.test.properties` 文件，其中定义了 Kafka 主题名称，如 `kafka.topic.hot-article`。
画面4：展示 `kafka.properties` 文件内容，定义了 Kafka 配置，包括 `kafka.group` 和多个主题名称，如 `kafka.topic.hot-article`。
画面5：展示 `KafkaTopicConfig` 类，定义了多个 Kafka 主题的属性，如 `submitArticleAuth`、`articleAuditSuccess`、`articleIncrHandle` 和 `hot-article`。
画面6：展示文档“1.2.2 定义封装类”，说明要创建 `ApiHotArticleMessage` 类，继承自 `KafkaMessage`。
画面7：展示 `ApiHotArticleMessage` 类的代码，定义了构造函数和 `getType()` 方法。
画面8：展示 `KafkaSender` 类的代码，包含 `sendArticleAuditSuccessMessage` 方法，用于发送文章审核成功消息。
画面9：展示 `KafkaSender` 类的代码，包含 `sendArticleUpdateBus` 方法，用于发送文章更新消息。
画面10：展示 `KafkaSender` 类的代码，包含 `sendHotArticleMessage` 方法，用于发送热点文章消息。
画面11：展示 `ApiHotArticleMessage` 类的代码，定义了 `getType()` 方法，返回 `"hot-article"`。
画面12：展示 `ApiHotArticleService` 类的代码，包含 `computeHotArticle` 方法，用于计算热点文章。
画面13：展示 `ApiHotArticleService` 类的代码，`computeHotArticle` 方法中调用 `kafkaSender.sendHotArticleMessage` 发送热点文章消息。
画面14：展示 `ApiHotArticleService` 类的代码，`computeHotArticle` 方法中调用 `kafkaSender.sendHotArticleMessage` 发送热点文章消息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
kafka.topic.hot-article
```
画面3：
```
mysql.core.tx.scan.package-execution(* com.heima.service.*.*(..))
# admin 账户名
admin.username=admin
admin.password=admin
host.name=localhost
eureka.client.serviceUrl.defaultZone=http://localhost:8761/eureka/
#文章提交相关的消息名称
kafka.topic.submit-article-auth=heima.topic.article.auth.sige.test
kafka.topic.article-audit-success=heima.topic.article.audit.success.sige.test
kafka.topic.article-incr-handle=heima.topic.article.incr.handle.sige.test
kafka.topic.hot-article=heima.topic.hot.article.sige.test
# app产生的定时文章消息
kafka.topic.article-update-bus=heima.topic.app.article.update.bus.test
```
画面4：
```
Kafka config
kafka.hosts=192.168.1.100:9092
kafka.hosts=47.94.7.85:9092
kafka.group=heima.${profiles.name}.${spring.application.name}
# 单例发消息，需要以sige结尾
#文章提交相关的消息名称
kafka.topic.admin-test=${kafka.topic.admin-test}
kafka.topic.submit-article-auth=${kafka.topic.submit-article-auth}
kafka.topic.article-audit-success=${kafka.topic.article-audit-success}
kafka.topic.article-incr-handle=${kafka.topic.article-incr-handle}
kafka.topic.hot-article=${kafka.topic.hot-article}
kafka.topic.article-update-bus=${kafka.topic.article-update-bus}
```
画面5：
```
package com.heima.common.kafka;
import ...
@Data
@ConfigurationProperties(prefix = "kafka.topic")
@PropertySource("classpath:kafka.properties")
public class KafkaTopicConfig {
    String adminTest;
    private String submitArticleAuth;
    private String articleAuditSuccess;
    private String articleIncrHandle;
    private String hotArticle;
}
```
画面6：
```
String hotArticle;
```
画面7：
```
package com.heima.common.kafka.messages.app;
import com.heima.common.kafka.KafkaMessage;
import com.heima.model.article.pojos.ApiHotArticles;
public class ApiHotArticleMessage extends KafkaMessage<ApiHotArticles> {
    public ApiHotArticleMessage() {}
    public ApiHotArticleMessage(ApiHotArticles data) {
        super(data);
    }
    @Override
    public String getType() {
        return "hot-article";
    }
}
```
画面8：
```
public void sendArticleAuditSuccessMessage(ArticleAuditSuccess message) {
    ArticleAuditSuccess temp = new ArticleAuditSuccess();
    temp.setData(message);
    this.sendMessage(kafkaTopicConfig.getArticleAuditSuccess(), UUID.randomUUID().toString(), temp);
}
```
画面9：
```
public void sendArticleUpdateBus(KafkaMessage message) {
    this.sendMessage(kafkaTopicConfig.getArticleUpdateBus(), UUID.randomUUID().toString(), message);
}
```
画面10：
```
public void sendHotArticleMessage(ApiHotArticleMessage message) {
    this.sendMessage(kafkaTopicConfig.getHotArticle(), UUID.randomUUID().toString(), message);
}
```
画面11：
```
@Override
public String getType() {
    return "hot-article";
}
```
画面12：
```
public void computeHotArticle() {
    //获取前一天的新发布的文章列表
    String lastDay = DateTime.now().minusDays(1).toString("yyyy-MM-dd 00:00:00");
    //计算文章热度（浏览量、评论、点赞）
    List<Article> articleList = apArticleMapper.loadLastArticleForHot(lastDay);
    //缓存热点文章到redis
    cacheTagZoRedis(articleList);
    //给每一个用户存一份热点文章
    List<ApBehaviorEntry> entryList = apBehaviorEntryMapper.selectAllEntry();
    for (ApiHotArticles hot : hotArticleList) {
        //保存热点文章
        apHotArticlesMapper.insert(hot);
        //给每一个用户存一份热点文章
        saveHotArticleForEntry(hot, entryList);
    }
}
```
画面13：
```
private ApiHotArticlesMapper apHotArticlesMapper;
private KafkaSender kafkaSender;
@Override
public void computeHotArticle() {
    //获取前一天的新发布的文章列表
    String lastDay = DateTime.now().minusDays(1).toString("yyyy-MM-dd 00:00:00");
    //计算文章热度（浏览量、评论、点赞）
    List<Article> articleList = apArticleMapper.loadLastArticleForHot(lastDay);
    //缓存热点文章到redis
    cacheTagZoRedis(articleList);
    //给每一个用户存一份热点文章
    List<ApBehaviorEntry> entryList = apBehaviorEntryMapper.selectAllEntry();
    for (ApiHotArticles hot : hotArticleList) {
        //保存热点文章
        apHotArticlesMapper.insert(hot);
        //给每一个用户存一份热点文章
        saveHotArticleForEntry(hot, entryList);
    }
}
```
画面14：
```
kafkaSender.sendHotArticleMessage(hot);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
