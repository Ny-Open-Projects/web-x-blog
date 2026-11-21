# 画面线理解：12_热文章计算_实时计算_发消息_消息发送方法编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\12_热文章计算_实时计算_发消息_消息发送方法编写【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:18, 00:44, 01:05, 01:32, 01:59, 02:26, 03:14, 03:57, 04:45, 05:33, 06:01, 06:34, 07:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:39:19

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
package com.heima.common.kafka.messages;

import com.heima.common.kafka.KafkaMessage;
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
package com.heima.behavior.kafka;

import org.springframework.stereotype.Component;

@Component
public class BehaviorMessageSender {
```

画面 8：
```java
package com.heima.behavior.kafka;

import com.heima.common.kafka.KafkaSender;
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
package com.heima.behavior.kafka;

import com.heima.common.kafka.KafkaSender;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class BehaviorMessageSender {
    @Autowired
    private KafkaSender kafkaSender;
```

画面 10：
```java
package com.heima.behavior.kafka;

import com.heima.common.kafka.KafkaSender;
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
package com.heima.behavior.kafka;

import com.heima.common.kafka.KafkaSender;
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
package com.heima.behavior.kafka;

import com.heima.common.kafka.KafkaSender;
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
package com.heima.behavior.kafka;

import com.heima.common.kafka.KafkaSender;
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
package com.heima.behavior.kafka;

import com.heima.common.kafka.KafkaSender;
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
