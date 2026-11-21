# 16_热文章计算_实时计算_收消息_消息名称定义及监听类编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\16_热文章计算_实时计算_收消息_消息名称定义及监听类编写【海量资源尽在 666java.com】.mp4
- 时长 9分19秒（音频 560s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好继续啊刚才呢咱们是把这个卡布卡stram的这个配置呢已经加完了啊那加完之后啊下面呢咱们会要去发消息那你说老师不应该发先收消息吗怎么还发消息呢其实呢咱们刚才去说这个流程的时候已经在这啊你看啊我这边呢是收消息没有错但是呢我这边还要去接收消息那接收消息之后呢我还要再发消息给谁啊再不要去更新当前的什么当前的分值
[00:29] 应该这样说应该更新当前的点赞阅读的数量啊所以说呢咱们这块需要去发个消息也就是这块这块啊那这个呢咱们首先呢先把这一块给定义出来然后呢咱们再去接收消息好吧好往下看啊首先呢咱们在这儿还是得去定义当前的一个这种消息的名称消息名称啊咱们直接考一下到哪呢这个是当前的我们下面有一个然后在这去加一个
[00:58] 这个就是article increment handle就是当前的这种增长值这个增长值呢其实就是当前文章里边的某些值比如说还是点赞和阅读啊其实下面现在目前的话就是两块好吧现在这是一个啊然后呢在这加完之后呢你需要去在当前的这种Kafka的public里边啊再去加一个加这个东西啊用这个好然后呢然后需要去读取这个配置对吧
[01:30] 你要去找到哪个类找到当前Kafka里边有一个叫做Kafkatopicconfig在这去加一个属性private然后是string这个怎么加大家都已经很熟了这是i是吧然后这是h那这样的话这个属性就算是读到了读到这个属性之后下面还有一些类这些类咱们还是需要去创建一下
[02:03] 最起码的你要创建两个类首先第一个类呢就是ArticleVest一个StripeDTO这个类啊咱们先去创建一下这个在哪去创建呢来打开当前的这种model啊咱们在model中去创建啊因为这个是封装的消息具体的内容啊App里边呢在这去创建一个类好类呢就是一个date里边封装什么属性呢可以看一下啊
[02:35] 那里边呢其实就是就是五个就是我其实咱们用到的话就三个来看一下啊第一个呢是当前的文章的ID你要修改某条文章的话肯定是要知道当前的文章ID然后第二个呢就是view数量就是阅读的数量是吧你的什么collection就是你的什么收藏的数量你的评论的数量还有你喜欢的数量好吧那这个呢其实要去更新OK啊那这是一个
[03:03] 然后咱们还要再去封装一个消息这个消息叫做ArticleVista.jpMessage这是要传递的一个消息名称里边封装的就是当前的DTO所以说怎么在这需要去创建一个message怎么创建的是不是在当前的Kafka有一个message怎么在这去创建一个包这个包叫啥叫APP好然后在这去创建一个类
[03:35] 这个干嘛呢要继承当前的Kafkamessage是吧然后这个范型刚才说了这范型是怎样就是article然后是vastavistastreamvistastreamvto好了然后呢咱们需要去重写一个方法这个呢就是新的消息的名称是吧articlevista我们的是叫什么叫stream好那这个构造啊
[04:07] 可以提供也可以不提供最好是提供一下啊嗯大布力可一个是无餐另外一个是啥呢有餐是吧好这个是又他对然后呢是super是对的哇那这样的话咱们这两个消息啊就算是呃会消息啊应该是当前的一个封装的类啊和消息都已经做完了啊然后下面咱们就继续啊
[04:46] 这个咱们先留着一会儿再用啊一会儿再用然后下面咱们要去接收留消息那接收留消息需要干嘛呢需要定一个类这个类呢你需要去继承要实现当前的卡普卡StreamListener好吧那这时候咱们一块去写一下啊那这个在哪写呢在当前的微服务端因为你发消息是不是当前的行为啊那你接收消息就是Article所以说咱们在这啊
[05:16] 去创建一个东西在这去创建一个叫什么来着类啊比如说叫Stream包下边然后叫一个当前的HotArticleStreamHandle好那需要干嘛就要去实现当前的KafkaStreamListener好这个范形啊它是有的啊这个范形可以看一下这个范形的话其实就是一个Stream好直接拿过来就可以啊好那这样就可以了啊
[05:48] 然后呢要去control看一下用写下的方法有三个啊一样是让Spring去管理然后呢是log4j2好我刚才说了啊这个呢是接收的监听消息然后这个呢这个是发送的这种消息的名称这个是处理具体的业务对吧那这时候你要去接收消息和发送消息怎么办呢刚才呢咱们已经定义了啊首先呢你要在这儿啊先去把当前的Kafka
[06:16] topic config注进来注进来之后呢这时候呢你就可以去获取消息咋儿咱们要获取的是哪个是不是一个articleupdate bus是吧你要更新呗好你要发送的是哪个呢你要发送的其实就是咱们刚刚定义的这个东西叫什么increment handle好来看一看然后这是cafka config.r有一个叫做get
[06:51] 就是这个东西是要发送的这种消息的名称这时候呢你要想去发送的话你必须这还得去干嘛呢还得去接收那这个接收是接收哪里的呀这个接收是接收的当前的behaviour里边发过来的消息啊那这个呢是咱们处理具体的业务逻辑好那这个业务逻辑啊是比较复杂的咱们一会儿再写好一会儿再写啊那这时候咱们可以再去把这个股价再去伸缩一下啊那这个东西
[07:19] 这个东西是不是要发送啊那发送的话那谁去接收呢其实还是当前的Article去接收还是Article去接收啊那这时候呢咱们就可以干嘛呢就可以在这啊再去加一个什么呢加一个包叫Kafka你也可以加一个ListenerListener啊好KafkaListener吧好吧这样去然后呢你就可以在这去创建一个类这个类叫啥呢咱们可以看一下啊
[07:57] 这个类呢就叫做当前的这东西radical increment handle listener我们在这去创建当前的一个类这个类要干嘛呢这个要去继承呃不要继承啊我们应该是去实现当前的一个叫做Kafka listener咱们都是stri好第一个第二个ctrl i好这个是消息的名称
[08:36] 还是一样啊我现在得让他干嘛呢得让他去去管理加上然后这是啥这就是当前的消息的名称KafkaprivateKafka好注入进来进来之后呢这时候你就可以去拿到当前的消息的名称就是当前哪个哪个不是一个是吧那这样的话咱们这个消息就算是结束了啊
[09:06] 这个业务呢咱们也没有处理咱们一会儿呢咱们再去说现在啊咱们是已经做完的当前的累啊都已经定义完了然后只剩下啥呢只剩下最终的业务的处理

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Kafka 实现文章浏览量实时统计功能，包括定义消息实体类、配置 Kafka 主题、编写监听器和处理方法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 `UpdateArticleMessage` 消息实体类定义，以及 `KafkaSender` 中发送消息的方法。
画面2：展示 `Kafka.properties` 配置文件，定义了多个 Kafka 主题，如 `Kafka.topic.article-submit`、`Kafka.topic.article-audit-success`、`Kafka.topic.article-incr-handle`。
画面3：展示 `KafkaTopicConfig` 配置类，定义了多个 Kafka 主题的字符串常量。
画面4：展示 `ArticleVisitStreamMessage` 消息实体类定义，以及 `ArticleVisitStreamDto` 数据传输对象。
画面5：在项目中右键点击，准备新建一个 Java 类。
画面6：展示 `ArticleVisitStreamMessage` 类的完整定义。
画面7：展示 `ArticleVisitStreamDto` 数据传输对象的定义。
画面8：展示 `HotArticleStreamHandler` 监听器类的开始编写。
画面9：展示 `HotArticleStreamHandler` 类中导入的 `@Component` 注解和 `@Autowired` 注解。
画面10：展示 `HotArticleStreamHandler` 类中定义了 `KafkaTopicConfig` 和 `KafkaStream` 的方法。
画面11：在项目中右键点击，准备新建一个 Java 类。
画面12：展示 `ArticleIncrHandleListener` 监听器类的定义，包含 `@Component`、`@Autowired` 注解和 `onMessage` 方法。
画面13：展示 `ArticleIncrHandleListener` 类中 `onMessage` 方法的实现，用于处理 Kafka 消息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public class UpdateArticleMessage extends KafkaMessage<UpdateArticle> {
    public UpdateArticleMessage() {
    }
    public UpdateArticleMessage(UpdateArticle data) {
        super(data);
    }
    @Override
    public String getType() {
        return "update-article";
    }
}
```
```java
/**
 * 发送修改文章请求消息
 */
public void sendArticleUpdateBus(KafkaMessage message) {
    this.messageBus.send(this.kafkaTopicConfig.getArticleUpdateBus(),
            UUID.randomUUID().toString(), message);
}
```

画面2：
```properties
admin.username=admin
admin.password=admin
hostname.Eureka.server=localhost
Eureka.client.serviceUrl.defaultZone=http://localhost:8701/Eureka/

# 文章提交的消费者名称
Kafka.topic.submit-article-auth=heima.topic.submit.article.auth.sige.test
Kafka.topic.article-audit-success=Kafka.topic.article.audit.success.sige.test
Kafka.topic.article-incr-handle=Kafka.topic.article.incr.handle.sige.test
# app产生的更新文章数据消息
Kafka.topic.article-update-bus=heima.topic.app.article.update.bus.test
```

画面3：
```java
package com.heima.common.Kafka;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.env.PropertySources;
import org.springframework.core.env.PropertySourcesPlaceholderConfigurer;

@Configuration
@PropertySources({
        @PropertySource("classpath:Kafka.properties")
})
public class KafkaTopicConfig {
    private String submitArticleAuth;
    private String articleAuditSuccess;
    private String articleIncrHandle;
    private String articleUpdateBus;
}
```

画面4：
```java
public class ArticleVisitStreamMessage extends KafkaMessage<ArticleVisitStreamDto> {
    @Override
    public String getType() {
        return "article-visit-stream";
    }
}
```
```java
@Data
public class ArticleVisitStreamDto {
    private Integer articleId;
    private Long view;
    private Long collect;
    private Long comment;
    private Long like;
}
```

画面6：
```java
public class ArticleVisitStreamMessage extends KafkaMessage<ArticleVisitStreamDto> {
    @Override
    public String getType() {
        return "article-visit-stream";
    }
}
```

画面7：
```java
@Data
public class ArticleVisitStreamDto {
    private Integer articleId;
    private Long view;
    private Long collect;
    private Long comment;
    private Long like;
}
```

画面8：
```java
package com.heima.article.stream;

import com.heima.common.Kafka.KafkaMessage;
import org.springframework.stereotype.Component;

@Component
public class HotArticleStreamHandler implements KafkaStreamListener<String, String> {
}
```

画面9：
```java
import org.springframework.stereotype.Component;

@Component
public class HotArticleStreamHandler implements KafkaStreamListener<String, String> {
    protected Object clone() { }
    public Package getPackage() { }
    public ProcessBuilder processBuilder() { }
    public Logger getLog() { }
    public boolean equals(Object obj) { }
    public int hashCode() { }
    public String toString() { }
    return null;
}
```

画面10：
```java
public class HotArticleStreamHandler implements KafkaStreamListener<String, String> {
    @Autowired
    private KafkaTopicConfig kafkaTopicConfig;
    @Override
    public String listenerTop() {
        return kafkaTopicConfig.getArticleIncrHandle();
    }
    @Override
    public KStream<String, String> getService(KStream<String, String> stream) {
        return null;
    }
}
```

画面12：
```java
/**
 * 监听类
 */
@Component
public class ArticleIncrHandleListener implements
        com.heima.Kafka.KafkaListener<String, String> {
    @Autowired
    KafkaTopicConfig kafkaTopicConfig;
    @Autowired
    ObjectMapper Mapper;
    @Autowired
    AppArticleService appArticleService;
    @Override
    public String topic() {
        return kafkaTopicConfig.getArticleIncrHandle();
    }
    @Override
    public void onMessage(ConsumerRecord<String, String> consumerRecord, String consumerGroup) {
    }
}
```

画面13：
```java
import lombok.extern.log4j.Log4j2;
import org.apache.Kafka.clients.consumer.Consumer;
import org.springframework.stereotype.Component;
import org.springframework.util.StringUtils;
import org.springframework.util.Assert;

@Component
@Log4j2
public class ArticleIncrHandleListener implements
        com.heima.Kafka.KafkaListener<String, String> {
    @Autowired
    private KafkaTopicConfig kafkaTopicConfig;
    @Override
    public String topic() {
        return kafkaTopicConfig.getArticleIncrHandle();
    }
    @Override
    public void onMessage(ConsumerRecord<String, String> consumerRecord, String consumerGroup) {
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“3.1.3 添加发送消息的方法”。
画面4：PPT标题为“3.2.3 定义消息处理的实体类”和“3.2.4 定义监听类，接收流消息”。
画面6：PPT标题为“3.2.3 定义消息处理的实体类”。
画面7：PPT标题为“3.2.3 定义消息处理的实体类”和“3.2.4 定义监听类，接收流消息”。
画面12：PPT标题为“3.2.5 更新文章浏览量”。
画面13：PPT标题为“3.2.5 更新文章浏览量”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

