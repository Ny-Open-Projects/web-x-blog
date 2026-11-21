# 03_图片缓存_article端发送消息

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\03_图片缓存_article端发送消息【海量资源尽在 666java.com】.mp4
- 时长 5分55秒（音频 356s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就来去在Article的微服务端去发送消息去处理当前这个图片的信息应该是热文章的图片信息这个思路刚才其实咱们已经说过了首先咱们在Article的微服务端去发送消息然后咱们一会会在这再去创建一个关于处理图片的微服务去处理当前图片进行缓存好吧当然图片的微服务咱们还没有创建
[00:28] 咱们现在当前的article端的先去发消息好吧那这个发消息是这样啊发消息的话首先呢你还得去定义当前的名称是吧然后呢要去定义一个消息的包装类最终的是定义发送在当前的这种计算热文章的这个方法里边呢去发一个消息就可以了好吧那这个咱们从头开始说首先呢还是要去定义当前的消息名称开前的common
[00:56] 然后在这test里边呢再去加一个消息的名称消息名称叫做out article然后呢你在当前的这种resource这有一个kavka的properties然后呢在这呢再去加一个加这个东西啊好那考过来之后啊下面呢你就要在当前的这种kavka这里边有个topicconfig中去读取当前这个消息名称读啊private然后呢你最好是能够在这啊
[01:26] 考一下我们这是子针就行的然后把这个杠去掉一变成大写这样的话就可以了这个消息名称拿到之后下面咱们就可以去封装一个消息叫什么AP hot messageAP hot article message这时候咱们在当前的message私中这里边是有一个APP你在这去创建一个消息的接触类
[01:58] 让他呢去继承当前的Kafkamessage好这里边装的呢是谁呀就是ap hot hot my myarticles好这时候重写一个方法方法呢咱们叫啥呢嗯叫hot article呃加s也行啊我看有没有加s啊不用加s是吧没有事啊这时候呢你就可以再去写两个方法第一个是无参的构造ap hot message好吧
[02:30] 然后这是无参然后再去写一个有参的AP hot message这个就是AP hotarticles那是date然后是调用复利的一个方法好吧那行那这样的话咱们就算是设置完了那设置完之后下面咱们要去发送消息首先咱们还是在当前的Kafkasender中去定义一个方法public void
[03:03] 怎么叫看叫啥我是保持一致Send hot message好这里边也是一个Kafka对啊我们这个里边的方法跟这个稍微有点区别咱一路再说这个方法叫啥处理热文章热文章数据消息这里边的这个东西你看
[03:36] 它是一个AP HOT ARTICLES也就是说你直接去传那个AP HOT ARTICLES就回了AP HOT ARTICLES当前是MESSAGE最终你就可以去调用THIS.SENDMESSAGE一个就是当前的什么Kafka消息名称是吧Kafkaconfig.getHOTARTICLE然后第二个
[04:09] 就是你要去设立一个UID点Random.toString然后第三个呢第三个的话其实就是这样那第三个其实你不应该传message传谁呢传的是当前的tphotArticleMessage是吧所以说你在这直接去叫temp直接去new出来给他tphot好然后最终的你就可以把当前的message装进去这样就可以了好吧然后你把这个
[04:40] pump呢放到这儿这样的话消息就算是发出去了这时候你接收的当前的也是一个APHOT articles好吧这个都没完之后呢下面呢咱们就可以干嘛呢就可以在当前的article类中去处理当前的热文章数据的方法上的去发送消息打开这个Service好在上面你先去注入一个谁呀注入一个当前的这种
[05:13] 这个啊叫Kafka森的啊就他啊那我写过啊所以说在这儿去留下了一个啊我可以你需要去把它给注入进来啊然后呢你就在这儿去写一个叫什么阿夫卡森的点森的有一个叫做奥特阿提扣买提示接收的就是一个当前的号的这样的话就可以了暂时不做咱们就可以给他删了啊现在是缓存文章的
[05:43] 图片信息主要是图片信息好吧那这时候这个消息已经发送了下面咱们就来去创建一个当前的图片的微服务去处理当前的这种消息

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现文章热度计算后，通过 Kafka 发送热点文章消息到指定主题。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档“1.1 功能需求”，说明要实现热点文章缓存图片功能，以及“1.2 article微服务发送消息”章节，列出 Kafka 主题名称 `Kafka.topic.hot-article`。
画面2：展示代码 `sendHotArticleMessage` 方法，用于发送热点文章消息，参数为 `ApiHotArticleMessage` 对象。
画面3：展示项目目录结构，重点是 `maven.test.properties` 文件，其中定义了 Kafka 主题名称，如 `Kafka.topic.hot-article`。
画面4：展示 `Kafka.properties` 文件内容，定义了 Kafka 配置，包括 `Kafka.group` 和多个主题名称，如 `Kafka.topic.hot-article`。
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
Kafka.topic.hot-article
```
画面3：
```
mysql.core.tx.scan.package-execution(* com.heima.Service.*.*(..))
# admin 账户名
admin.username=admin
admin.password=admin
host.name=localhost
Eureka.client.serviceUrl.defaultZone=http://localhost:8761/Eureka/
#文章提交相关的消息名称
Kafka.topic.submit-article-auth=heima.topic.article.auth.sige.test
Kafka.topic.article-audit-success=heima.topic.article.audit.success.sige.test
Kafka.topic.article-incr-handle=heima.topic.article.incr.handle.sige.test
Kafka.topic.hot-article=heima.topic.hot.article.sige.test
# app产生的定时文章消息
Kafka.topic.article-update-bus=heima.topic.app.article.update.bus.test
```
画面4：
```
Kafka config
Kafka.hosts=192.168.1.100:9092
Kafka.hosts=47.94.7.85:9092
Kafka.group=heima.${profiles.name}.${spring.application.name}
# 单例发消息，需要以sige结尾
#文章提交相关的消息名称
Kafka.topic.admin-test=${Kafka.topic.admin-test}
Kafka.topic.submit-article-auth=${Kafka.topic.submit-article-auth}
Kafka.topic.article-audit-success=${Kafka.topic.article-audit-success}
Kafka.topic.article-incr-handle=${Kafka.topic.article-incr-handle}
Kafka.topic.hot-article=${Kafka.topic.hot-article}
Kafka.topic.article-update-bus=${Kafka.topic.article-update-bus}
```
画面5：
```
package com.heima.common.Kafka;
import ...
@Data
@ConfigurationProperties(prefix = "Kafka.topic")
@PropertySource("classpath:Kafka.properties")
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
package com.heima.common.Kafka.messages.app;
import com.heima.common.Kafka.KafkaMessage;
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

