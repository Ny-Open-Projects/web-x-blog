# 12_热文章计算_实时计算_发消息_消息发送方法编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\12_热文章计算_实时计算_发消息_消息发送方法编写【海量资源尽在 666java.com】.mp4
- 时长 7分14秒（音频 434s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好继续啊然后刚才呢咱们是把这些消息的名称啊还有封装的类啊咱们就都已经设置完了然后下面呢咱们还要再去发发消息的方法咱们还去设置一下啊在下面呢再去添加一个方法public然后是 void然后是 sendsend articleticle然后是 update pass参数呢是一样的啊参数跟之前是一样我们也是叫做什么
[00:31] KafkamessagemessageKafkamessage然后呢是message然后最终呢咱们是调用谁呀用this.send当前一个message然后第一个参数呢谁呀这个参数的话其实这样啊就是当前的Kafkaconfig.什么的有一个叫做get这是不是叫叫什么get article update bus是吧然后第二个呢
[01:03] 第二个的话其实就是当前的什么一个值啊UID然后呢是23第三个是真正的消息就是message那这样的话这个方法咱们就说完了啊然后在这咱们可以加加个入室说是发送修改文章等纠消息是一个是吧下面还有哪些呢这个你说咱们刚才说了其实都是在哪啊
[01:35] 在咱们的比如说评论评论没有是吧收藏点赞还有些阅读是吧咱们要去调用这个消息去发送然后是去修改文章的这种分值应该是他的点赞量是吧像那些数据那这样咱们是为了统一一下咱们在当前的behavior当前的行为里边咱们在这呢再去封装一个专门用来发送消息的封装的类好吧在这咱们在这去创建一个叫卡不卡卡
[02:05] 然后呢是叫做什么这个很长时间不写了是吧然后呢是怎么着呢叫messagecinder又去封装列啊他也是用于发送消息的好点ok然后呢让他呢首先是让sprint去管理然后下面呢怎么办呢下面这样啊下面首先呢你要去输入谁啊输入一个叫做kapucacinder
[02:36] 好那这样的话呢我们再去发送消息的时候呢你直接用当前的卡普卡森的就可以了啊这里边啊咱们需要去引入啊还有没有引入啊那没有引入怎么办呢没有引入就就加进来呗好是加一括号啊然后是com.黑马然后怎么着然后是一个叫com好那这样就可以了啊这块内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内内
[03:08] 然后下面咱们要去定义两个方法为什么要定义两个public我先定义出来看一下void然后是一个叫做send message plus然后第二个是void send message然后是reduceu ce这是什么意思这个其实就是刚才说的是什么
[03:42] 发送加一的那个方法这是发送减一的那个方法有可能是负数码所以说呢咱们要去定义两个方法好吧那行那这个咱们设置完之后啊这里边是他呢是是需要去接收一些参数的第一个呢是当前的卡巴卡啊服啊message啊第二个呢这个第二个呢其实就是一样是一个浪类型的呃ap user id然后第三个呢
[04:14] 我们已经设置一个玻璃形的啊嗯is send a t i c l e好吧那这个咱们也是做个标识啊那为什么要这么写我们一会呢去发消息的时候咱们再说好吧下面的猜测是一样的啊下面猜测是一样的好这两话定义出来之后呢那这里一边该怎么办呢这一边其实就是干嘛呢就是去改一个什么有一个叫做send当前的哪个这不是article
[04:48] 对吧这两个都是啊这里边装什么什么参数呢message吗对啊不是message啊这message咱们需要去处理我给这两个咱们都写下啊那到底这个message是谁我给大家下面呢咱们就来去简单说一说啊其实这个message呢其实针对于某一些就一样的话这个message是不一样的比如说点赞跟转发肯定是不一样的是吧
[05:17] 所以说咱们在这先去干嘛先去把这个message给处理一下也就是说你需要去封装成一个什么update article message对呀updateupdate article message好这是message比如叫temp好等于一个什么等于啥你不能拗一个出来你不能拗一个出来这个咱们需要去封装需要去封装pass message
[05:47] 这个参数其实就是当前的一个message第二个就是ap.id第三个是当前的1为什么要是1呢这个啥什么东西发送加1的消息这个呢发送点1的消息大家还不明白没事一会我再去重新去
[06:25] 这个消息发完之后你可能就明白了行这个其实就是temp行这个方法没有咱们可以去创建一下下边好吧下边这方法咱们先留到这咱们一会再做这样现在你看的话估计也看不明白下边这个其实一样是不同的点是这不是1这是-1这是-1它这个装的其实也是temp
[07:00] 好那这样做完之后啊那所有的这种发送消息的股价呢算是做出来了啊那最终那你说这里边到底该怎么去封装咱们那咱们现在啊下面呢就来具体去说一说

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Kafka 发送文章审核成功和文章更新消息，涉及消息实体类、消息发送器类的编写与调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 `UpdateArticleMessage.java` 文件，定义了 `UpdateArticleMessage` 消息类，包含构造函数和 `getTopic` 方法，用于标识消息类型。
画面 2：展示 `KafkaSender.java` 文件，定义了 `sendSubmitArticleAuthMessage` 方法，用于发送文章审核消息。
画面 3：在 `KafkaSender.java` 中，光标位于 `sendArticleAuditSuccessMessage` 方法，该方法用于发送文章审核成功消息。
画面 4：在 `KafkaSender.java` 中，光标位于 `sendArticleUpdateBus` 方法，该方法用于发送文章更新消息。
画面 5：在 `KafkaSender.java` 中，光标位于 `sendArticleUpdateBus` 方法，该方法用于发送文章更新消息。
画面 6：展示项目结构，当前选中的是 `heima-leadnews-common` 模块。
画面 7：展示 `BehaviorMessageSender.java` 文件，该类被 `@Component` 注解标记，用于发送行为相关的消息。
画面 8：在 `BehaviorMessageSender.java` 中，光标位于 `KafkaSender` 类的 `equals` 方法，用于比较两个 KafkaSender 对象。
画面 9：在 `BehaviorMessageSender.java` 中，光标位于 `@Autowired` 注解的 `kafkaSender` 字段，用于注入 Kafka 发送器。
画面 10：在 `BehaviorMessageSender.java` 中，光标位于 `sendArticleUpdateBus` 方法，用于发送文章更新消息。
画面 11：在 `BehaviorMessageSender.java` 中，光标位于 `sendArticleUpdateBus` 方法，用于发送文章更新消息。
画面 12：在 `BehaviorMessageSender.java` 中，光标位于 `sendArticleUpdateBus` 方法，用于发送文章更新消息。
画面 13：在 `BehaviorMessageSender.java` 中，光标位于 `sendArticleUpdateBus` 方法，用于发送文章更新消息。
画面 14：在 `BehaviorMessageSender.java` 中，光标位于 `sendArticleUpdateBus` 方法，用于发送文章更新消息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
package com.heima.common.Kafka.messages;

import com.heima.common.Kafka.KafkaMessage;
import com.heima.model.mess.app.UpdateArticle;

public class UpdateArticleMessage extends KafkaMessage<UpdateArticle> {
    public UpdateArticleMessage() {}

    public UpdateArticleMessage(UpdateArticle data) {
        super(data);
    }

    @Override
    public String getTopic() {
        return "update-article";
    }
}
```

画面 2：
```java
public void sendSubmitArticleAuthMessage(SubmitArticleAuthMessage message) {
    this.sendMessage(kafkaTopicConfig.getSubmitArticleAuth(), UUID.randomUUID().toString(), message);
}

// 发送审核成功消息
public void sendArticleAuditSuccessMessage(ArticleAuditSuccessMessage message) {
    ArticleAuditSuccessMessage temp = new ArticleAuditSuccessMessage();
    temp.setData(message);
    this.sendMessage(kafkaTopicConfig.getArticleAuditSuccess(), UUID.randomUUID().toString(), message);
}
```

画面 3：
```java
public void sendArticleAuditSuccessMessage(ArticleAuditSuccessMessage message) {
    ArticleAuditSuccessMessage temp = new ArticleAuditSuccessMessage();
    temp.setData(message);
    this.sendMessage(kafkaTopicConfig.getArticleAuditSuccess(), UUID.randomUUID().toString(), message);
}

// 发送修改文章请求消息
public void sendArticleUpdateBus(KafkaMessage message) {
    this.sendMessage(kafkaTopicConfig.getArticleUpdateBus(), UUID.randomUUID().toString(), message);
}
```

画面 4：
```java
public void sendArticleAuditSuccessMessage(ArticleAuditSuccessMessage message) {
    ArticleAuditSuccessMessage temp = new ArticleAuditSuccessMessage();
    temp.setData(message);
    this.sendMessage(kafkaTopicConfig.getArticleAuditSuccess(), UUID.randomUUID().toString(), message);
}

// 发送修改文章请求消息
public void sendArticleUpdateBus(KafkaMessage message) {
    this.sendMessage(kafkaTopicConfig.getArticleUpdateBus(), UUID.randomUUID().toString(), message);
}
```

画面 5：
```java
// 发送审核成功消息
public void sendArticleAuditSuccessMessage(ArticleAuditSuccessMessage message) {
    ArticleAuditSuccessMessage temp = new ArticleAuditSuccessMessage();
    temp.setData(message);
    this.sendMessage(kafkaTopicConfig.getArticleAuditSuccess(), UUID.randomUUID().toString(), message);
}

// 发送修改文章请求消息
public void sendArticleUpdateBus(KafkaMessage message) {
    this.sendMessage(kafkaTopicConfig.getArticleUpdateBus(), UUID.randomUUID().toString(), message);
}
```

画面 6：
无代码，仅展示项目结构。

画面 7：
```java
package com.heima.behavior.Kafka;

import org.springframework.stereotype.Component;

@Component
public class BehaviorMessageSender {
```

画面 8：
```java
package com.heima.behavior.Kafka;

import com.heima.common.Kafka.KafkaSender;
import org.springframework.util.Assert;

public class KafkaSender {
    private static final String DEFAULT_TOPIC = "default-topic";

    public KafkaSender() {}

    public KafkaSender(String topic) {
        this.topic = topic;
    }

    public void send(String topic, String key, Object message) {
        // 发送消息逻辑
    }

    public boolean equals(Object obj) {
        return obj instanceof KafkaSender && ((KafkaSender) obj).topic.equals(this.topic);
    }

    public int hashCode() {
        return topic.hashCode();
    }

    public String toString() {
        return "KafkaSender{" + "topic='" + topic + '\'' + '}';
    }
}
```

画面 9：
```java
package com.heima.behavior.Kafka;

import com.heima.common.Kafka.KafkaSender;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class BehaviorMessageSender {
    @Autowired
    private KafkaSender kafkaSender;
```

画面 10：
```java
package com.heima.behavior.Kafka;

import com.heima.common.Kafka.KafkaSender;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class BehaviorMessageSender {
    @Autowired
    private KafkaSender kafkaSender;

    public void sendArticleUpdateBus(KafkaMessage message, Long articleId, boolean isSendToArticle) {
        kafkaSender.sendArticleUpdateBus(message, articleId, isSendToArticle);
    }
}
```

画面 11：
```java
package com.heima.behavior.Kafka;

import com.heima.common.Kafka.KafkaSender;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class BehaviorMessageSender {
    @Autowired
    private KafkaSender kafkaSender;

    public void sendArticleUpdateBus(KafkaMessage message, Long articleId, boolean isSendToArticle) {
        kafkaSender.sendArticleUpdateBus(message, articleId, isSendToArticle);
    }
}
```

画面 12：
```java
package com.heima.behavior.Kafka;

import com.heima.common.Kafka.KafkaSender;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class BehaviorMessageSender {
    @Autowired
    private KafkaSender kafkaSender;

    public void sendArticleUpdateBus(KafkaMessage message, Long articleId, boolean isSendToArticle) {
        kafkaSender.sendArticleUpdateBus(message, articleId, isSendToArticle);
    }
}
```

画面 13：
```java
package com.heima.behavior.Kafka;

import com.heima.common.Kafka.KafkaSender;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class BehaviorMessageSender {
    @Autowired
    private KafkaSender kafkaSender;

    public void sendArticleUpdateBus(KafkaMessage message, Long articleId, boolean isSendToArticle) {
        UpdateArticleMessage temp = parseMessage(message, articleId, isSendToArticle);
        kafkaSender.sendArticleUpdateBus(temp);
    }
}
```

画面 14：
```java
package com.heima.behavior.Kafka;

import com.heima.common.Kafka.KafkaSender;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class BehaviorMessageSender {
    @Autowired
    private KafkaSender kafkaSender;

    public void sendArticleUpdateBus(KafkaMessage message, Long articleId, boolean isSendToArticle) {
        UpdateArticleMessage temp = parseMessage(message, articleId, isSendToArticle);
        kafkaSender.sendArticleUpdateBus(temp);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题、架构图/流程图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

