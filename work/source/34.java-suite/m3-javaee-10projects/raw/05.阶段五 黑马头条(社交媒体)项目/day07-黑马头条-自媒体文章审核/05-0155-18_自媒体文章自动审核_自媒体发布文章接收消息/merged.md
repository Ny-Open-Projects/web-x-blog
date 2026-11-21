# 18_自媒体文章自动审核_自媒体发布文章接收消息

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\18_自媒体文章自动审核_自媒体发布文章接收消息【海量资源尽在 666java.com】.mp4
- 时长 8分3秒（音频 483s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好刚才呢咱们是把这个发送文章的消息发送啊给设置了一下咱们主要呢是在当前的media端去发布文章的时候同时去发送一条消息啊让他去审核那这个消息发送了那我得去审核吧那审核怎么审核呢审核的话是不是得去接收当前的那条消息啊所以说咱们在admin端啊因为admin端呢需要去审核文章
[00:26] 所以说你需要在额德命端去接收到当前的这个消息那这个怎么接收呢其实呢就跟咱们之前是差不多的啊做测试的时候就是来去创建一个监听就可以监听啊这话咱们可以创建一个类啊这个类就叫啥类呢就就在当前的额德命端打开在Kafka这包下边去创建一个类类就来负责负责去接收消息而这个类干嘛呢要去实现一个Kafka
[00:58] 然后给一个范形吧好吧行那这样的话就设置完了啊那这个呢就是要去设置消息的名称这个呢这个就是来接收具体的消息来处理当前的消息到底该怎么去怎么做是吧行那首先呢这个列啊你得让Spring去管理好然后下面咱们要去设立一步啊首先呢这是有一个消息的名称那消息的名称大家都知道咱们在这可以去写死那也可以干嘛呢
[01:28] 也可以去注入一个类类里边其实已经读了当前的配置的名称应该是消息的名称打开它是不是这个类里边其实已经在这去读了一次了所以说咱们在这就可以干嘛呢就可以直接去注入好注入完进来之后咱们可以直接去调用就可以了这个就完了Rat Double Meet Article Author完了那这样的话其实这个就是消息的名称
[02:04] 下面咱们就可以接收具体的消息具体的消息是这样这个其实就是具体的消息咱们可以干嘛呢也可以在这去打印打印的话咱们在这用目前的log4j2吧是去加一个log.info咱们可以去设置一换说接收到消息为
[02:40] 然后咱们可以去加个这东西好像不对感觉找引号然后是加谁呢加上value完事了好吧这样的话就在空台上去打印了当前的信息然后下面咱们该怎么去设置下面咱们要去首先要去转换一下转换啥呢这个value是这样这个value它去传过来之后其实是一个json字母串这个有印象吗你要是不知道的话你可以打开当前的卡布卡森
[03:09] 咱们是不是都要用了这个方法去去发送消息对吧没问题啊最终呢他是掉了一个send message其实呢就是把当前这个send message往上走啊他最终是掉了当前的这个方法掉了当前这个方法那这个方法里边是不是加了一个myper right value是不是把这个当前对象转成了一个json字母串没问题吧所以说啊你在这去接收的时候你首先要去转换过来转换过来啊那转换的话咱们还是需要去注入一个啊什么
[03:40] private object mypro行 注进来然后呢咱们就可以直接去read value然后是谁呀就是当前掌value然后转换过来的是谁呢这转换过来就是submit my article author message就是他这应该是加个class啊好那这样的话就是一个message
[04:11] 这个需要去try cache一下那设置完之后下面咱们就可以去通过当下的message去获取到当前具体的内容比如说咱们在这去设置一下比如说要去随好时做个判断message不等于什么呢不等于none的时候下面就可以去拿到消息了message rgetgetdat rarticle这样的话就能拿到文章信息
[04:42] 是大家要注意啊你直接拿到文章信息的话你不能确定到底是自媒体或者是爬虫的文章所以说咱们在这啊要去重新设置一下重新设置一下怎么设置呢你在这啊去设置一个什么东西啊message.get.get.r先去拿到当前这个type那这个type呢其实就是怎样不是具体的你是自媒体呀或者是说你的爬虫啊就是咱们在这啊再去做一个
[05:11] 好,type等于谁呀?
[05:14] 等于submit.get.article.type.remedial等于当前的自媒体的时候咱们再去重新设置好吧这时候呢,可以拿到当前的.get.article.idOK,那这样就能拿到ID了ID之后要干嘛呢?
[05:40] ID之后,那你要去审核
[05:42] 审核文章啊就说咱们在这去审核文章就可以了啊说article id不等于难然后呢就可以去审核文章信息那审核文章是不是在干嘛呢是不是得去再去入一个类呀类是不是就咱们审核文章那个类呀刚才咱们写那个哪个就是当前的review media article Service对吧ok啊咱们来说说这一下
[06:13] review media article Service 收藏好注进来注进来之后呢咱们就可以干嘛呢就可以在这在这啊点里边只有一个方法把当前的 article 设置进去这样的话呢我们就算是设置完了啊最终呢咱们在这也可以去打印一些加上 log.error好吧然后咱们去写一下说复理
[06:45] 自动审核文框错误好吧直接去设置一个错误但你也可以把错误给打印出来是吧打印错误怎么打印呢我们加一个冒号好吧然后呢咱们再去加这东西然后呢下面第一个就是value第二个就是e就是上前的异常信息好那这样咱们就说这完了啊当然你也可以在这去直接去抛一个异常抛一个srmrun time
[07:23] run time exception里边咱们可以去设置一下说ws消息处理错误然后咱们也可以把这个eek打印一下这样的话我们就算是设置完了这个do号有问题有问题吗我看看srow ws 冒号 new少一括号哪一小括号呢这还是有问题是吧那这样就可以了
[07:56] 那这个代码咱们就写完了写完之后咱们一会就可以进行来测试一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中使用 Kafka 消费者监听器处理文章自动审核消息，并通过对象映射器解析消息体并调用服务处理。

2) 按时间顺序列出每张画面的要点：
画面1: 展示项目结构，选中 `heima-leadnews-admin` 模块，准备进入代码编辑。
画面2: 打开 `AutoReviewArticleListener.java` 文件，显示类定义和导入语句。
画面3: 在 `AutoReviewArticleListener` 类中添加 `@Component` 注解，并定义 `topic()` 和 `onMessage()` 方法的骨架。
画面4: 在 `@Component` 注解下方，使用 `@Autowired` 注解注入 `KafkaTopicConfig`。
画面5: 定义 `topic()` 方法，返回 `kafkaTopicConfig.getSubmitArticleAuth()`。
画面6: 在 `onMessage()` 方法中，使用 `kafkaTemplate` 发送消息，但画面焦点在 `KafkaSender.java` 文件。
画面7: 在 `onMessage()` 方法中，使用 `ObjectMapper` 解析消息体。
画面8: 使用 `ObjectMapper` 将字符串解析为 `SubmitArticleAuthMessage` 对象。
画面9: 在 `onMessage()` 方法中，对解析出的对象进行非空判断。
画面10: 在 `onMessage()` 方法中，根据消息类型进行判断，使用 `SubmitArticleAuto.ArticleType` 枚举。
画面11: 在 `onMessage()` 方法中，根据消息类型判断是否为 `MEDIA` 类型。
画面12: 在 `onMessage()` 方法中，调用 `reviewMediaArticleService` 服务处理媒体文章。
画面13: 在 `onMessage()` 方法中，添加 `catch` 块处理异常。
画面14: 完成 `onMessage()` 方法，显示最终代码结构。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2:
```java
package com.heima.admin.Kafka;
import com.heima.common.Kafka.KafkaListener;
public class AutoReviewArticleListener implements KafkaListener<String, String> {
```

画面3:
```java
import com.heima.common.Kafka.KafkaListener;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Override
public String topic() {
    return null
}
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {

}
```

画面4:
```java
import com.heima.common.Kafka.KafkaListener;
import com.heima.common.Kafka.KafkaTopicConfig;
import org.apache.Kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
@Override
public String topic() {
    return kafkaTopicConfig.getSubmitArticleAuth();
}
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {

}
```

画面5:
```java
import com.heima.common.Kafka.KafkaListener;
import com.heima.common.Kafka.KafkaTopicConfig;
import org.apache.Kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
@Override
public String topic() {
    return kafkaTopicConfig.getSubmitArticleAuth();
}
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    String value = consumerRecord.value();
    log.info("接收到的消息为：{}", value);
}
```

画面6:
```java
public class KafkaSender {
    private KafkaTemplate<String, String> kafkaTemplate;
    private KafkaTopicConfig kafkaTopicConfig;
    public void sendMessage(String topic, String key, String message) {
        try {
            this.kafkaTemplate.send(topic, key, message);
        } catch (Exception e) {
            logger.error("send message to {} error: {}", topic, e);
        }
    }
    public void sendSubmitArticleAuthMessage(SubmitArticleAuthMessage message) {
        this.kafkaTemplate.send(kafkaTopicConfig.getSubmitArticleAuth(), UUID.randomUUID().toString(), message);
    }
}
```

画面7:
```java
import com.heima.common.Kafka.KafkaListener;
import com.heima.common.Kafka.KafkaTopicConfig;
import org.apache.Kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
private ObjectMapper Mapper;
@Override
public String topic() {
    return kafkaTopicConfig.getSubmitArticleAuth();
}
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    String value = consumerRecord.value();
    log.info("接收到的消息为：{}", value);
}
```

画面8:
```java
import com.heima.common.Kafka.KafkaListener;
import com.heima.common.Kafka.KafkaTopicConfig;
import org.apache.Kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
private ObjectMapper Mapper;
@Override
public String topic() {
    return kafkaTopicConfig.getSubmitArticleAuth();
}
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    String value = consumerRecord.value();
    log.info("接收到的消息为：{}", value);
    SubmitArticleAuthMessage message = Mapper.readValue(value, SubmitArticleAuthMessage.class);
}
```

画面9:
```java
import com.heima.common.Kafka.KafkaListener;
import com.heima.common.Kafka.KafkaTopicConfig;
import org.apache.Kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
private ObjectMapper Mapper;
@Override
public String topic() {
    return kafkaTopicConfig.getSubmitArticleAuth();
}
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    String value = consumerRecord.value();
    log.info("接收到的消息为：{}", value);
    SubmitArticleAuthMessage message = Mapper.readValue(value, SubmitArticleAuthMessage.class);
    if (message == null) {
        message.getData().getArticleId();
    }
}
```

画面10:
```java
import com.heima.common.Kafka.KafkaListener;
import com.heima.common.Kafka.KafkaTopicConfig;
import org.apache.Kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
private ObjectMapper Mapper;
@Override
public String topic() {
    return kafkaTopicConfig.getSubmitArticleAuth();
}
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    String value = consumerRecord.value();
    log.info("接收到的消息为：{}", value);
    SubmitArticleAuthMessage message = Mapper.readValue(value, SubmitArticleAuthMessage.class);
    if (message == null) {
        message.getData().getArticleId();
    }
    if (message.getData().getArticleType() == 0) {
        message.getData().getArticleId();
    }
}
```

画面11:
```java
import com.heima.common.Kafka.KafkaListener;
import com.heima.common.Kafka.KafkaTopicConfig;
import org.apache.Kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
private ObjectMapper Mapper;
@Override
public String topic() {
    return kafkaTopicConfig.getSubmitArticleAuth();
}
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    String value = consumerRecord.value();
    log.info("接收到的消息为：{}", value);
    SubmitArticleAuthMessage message = Mapper.readValue(value, SubmitArticleAuthMessage.class);
    if (message == null) {
        message.getData().getArticleId();
    }
    if (message.getData().getArticleType() == 0) {
        message.getData().getArticleId();
    }
}
```

画面12:
```java
import com.heima.common.Kafka.KafkaListener;
import com.heima.common.Kafka.KafkaTopicConfig;
import org.apache.Kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
private ObjectMapper Mapper;
private ReviewMediaArticleService reviewMediaArticleService;
@Override
public String topic() {
    return kafkaTopicConfig.getSubmitArticleAuth();
}
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    String value = consumerRecord.value();
    log.info("接收到的消息为：{}", value);
    SubmitArticleAuthMessage message = Mapper.readValue(value, SubmitArticleAuthMessage.class);
    if (message == null) {
        message.getData().getArticleId();
    }
    if (message.getData().getArticleType() == 0) {
        message.getData().getArticleId();
    }
}
```

画面13:
```java
import com.heima.common.Kafka.KafkaListener;
import com.heima.common.Kafka.KafkaTopicConfig;
import org.apache.Kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
@Component
public class AutoReviewArticleListener implements KafkaListener<String, String> {
@Autowired
private KafkaTopicConfig kafkaTopicConfig

