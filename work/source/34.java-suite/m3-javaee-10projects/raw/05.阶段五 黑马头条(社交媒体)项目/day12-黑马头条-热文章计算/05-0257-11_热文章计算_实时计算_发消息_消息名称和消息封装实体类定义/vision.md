# 画面线理解：11_热文章计算_实时计算_发消息_消息名称和消息封装实体类定义

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\11_热文章计算_实时计算_发消息_消息名称和消息封装实体类定义【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:25, 00:35, 01:09, 01:24, 01:52, 02:06, 02:39, 02:55, 03:20, 03:33, 03:52, 04:12, 04:33, 04:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:38:30

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过 Kafka 消息队列封装文章点赞、收藏等行为的更新事件，并配置相关属性和消息类。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Quartz 定时任务类 AppJobArticleQuartz.java，其中定义了定时任务执行方法和描述触发器，用于触发文章分值计算。
画面 2: 展示项目中 maven-test.properties 配置文件，定义了数据库连接、Eureka 服务地址和 Kafka 消息主题。
画面 3: 展示 kafka.properties 配置文件，定义了 Kafka 服务地址、消费者组和多个消息主题。
画面 4: 展示 KafkaTopicConfig.java 文件，正在定义类的属性，用于配置 Kafka 消息主题。
画面 5: 展示 KafkaTopicConfig.java 文件，已定义了三个私有字符串属性：submitArticleAuth、articleAuditSuccess 和 articleUpdateBus。
画面 6: 展示 UpdateArticle.java 文件，定义了文章更新实体类，包含 articleId、add、applierId、behaviorId 等字段和 UpdateArticleType 枚举。
画面 7: 展示 UpdateArticle.java 文件，对 UpdateArticleType 枚举的定义进行编辑。
画面 8: 展示文档内容，说明了如何在 KafkaTopicConfig 类中新增属性并添加消息名称。
画面 9: 展示 UpdateArticle.java 文件，对 UpdateArticleType 枚举的定义进行编辑。
画面 10: 展示 UpdateArticleMessage.java 文件，正在编写类的继承结构，准备继承 KafkaMessage 和 UpdateArticle。
画面 11: 展示文档内容，说明了如何添加发送消息的方法。
画面 12: 展示 UpdateArticleMessage.java 文件，正在编写类的构造方法。
画面 13: 展示 UpdateArticleMessage.java 文件，正在编写类的构造方法，调用父类构造方法。
画面 14: 展示 UpdateArticleMessage.java 文件，正在编写 gettype() 方法，返回 "update-article"。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
private ApolloArticleService apolloArticleService;

@Override
protected void executeInternal(JobExecutionContext jobExecutionContext) throws JobExecutionException {
    long currentTimeMillis = System.currentTimeMillis();
    log.info("开始定时计算分值");
    apolloArticleService.computallArticle();
    log.info("计算分值完成，耗时: {} ", System.currentTimeMillis()-currentTimeMillis);
}

@Override
public String descTrigger() {
    return "每天00:05执行一次";
}
```

画面 2:
```properties
mysql.core.mapper-mappers
mysql.core.alises.package=com.heima.model.**
mysql.core.tx.scan.package-execution(*.com.heima..service.*.*())

# admin 账户名
admin.username=admin
admin.password=admin

hostname.eureka.server=localhost
eureka.client.serviceUrl.defaultZone=http://localhost:8761/eureka/

#文章提交审核的消息名称
kafka.topic.submit-article-auth=heima.topic.submit.article.auth.single.test
kafka.topic.article-audit-success=kafka.topic.article.audit.success.single.test
```

画面 3:
```properties
kafka.config
kafka.hosts=localhost:9092
kafka.hosts=47.94.7.85:9092
kafka.group=heima.${profiles.name}
# 单消息通道，需要以kafka为前缀
kafka.topic.admin-test=${kafka.topic.admin-test}
#文章提交审核的消息名称
kafka.topic.submit-article-auth=${kafka.topic.submit-article-auth}
kafka.topic.article-audit-success=${kafka.topic.article-audit-success}
#app产生的更新文章数据消息
kafka.topic.article-update-bus=${kafka.topic.article-update-bus}
```

画面 4:
```java
package com.heima.common.kafka;

import ...
@Data
@Configuration
@PropertySources({
    @PropertySource(value = "classpath:kafka.properties")
})
public class KafkaTopicConfig {
    // String adminTest;
    private String submitArticleAuth;
    private String articleAuditSuccess;
    private String articleUpdateBus;
}
```

画面 5:
```java
package com.heima.common.kafka;

import ...
@Data
@Configuration
@PropertySources({
    @PropertySource(value = "classpath:kafka.properties")
})
public class KafkaTopicConfig {
    private String submitArticleAuth;
    private String articleAuditSuccess;
    private String articleUpdateBus;
}
```

画面 6:
```java
package com.heima.model.mess.app;

import lombok.Data;

public class UpdateArticle {
    // 修改文章的字段类型
    private UpdateArticleType type;
    // 文章id
    private Integer articleId;
    // 修改数据的增量，可为正数
    private Integer add;
    private Integer applierId;
    private Integer behaviorId;

    public enum UpdateArticleType {
        COLLECTION, COMMENT, LIKES, VIEWS
    }
}
```

画面 7:
```java
public enum UpdateArticleType {
    COLLECTION, COMMENT, LIKES, VIEWS
}
```

画面 8:
```text
// app产生的更新文章数据消息
kafka.topic.article-update-bus=${kafka.topic.article-update-bus}

// 更新文章数据的消息topic
String articleUpdateBus;
```

画面 9:
```java
package com.heima.model.mess.app;

import lombok.Data;

public class UpdateArticle {
    // 修改文章的字段类型
    private UpdateArticleType type;
    // 文章id
    private Integer articleId;
    // 修改数据的增量，可为正数
    private Integer add;
    private Integer applierId;
    private Integer behaviorId;

    public enum UpdateArticleType {
        COLLECTION, COMMENT, LIKES, VIEWS
    }
}
```

画面 10:
```java
package com.heima.common.kafka.messages;

public class UpdateArticleMessage extends KafkaMessage<UpdateArticle> {
```

画面 11:
```text
进行消息体的传输封装
com.heima.common.kafka.UpdateArticleMessage
public class UpdateArticleMessage extends KafkaMessage<UpdateArticle> {
    public UpdateArticleMessage() {
        super(data);
    }

    @Override
    public String gettype() {
        return "update-article";
    }
}
```

画面 12:
```java
package com.heima.common.kafka.messages;

import com.heima.common.kafka.KafkaMessage;
import com.heima.model.mess.app.UpdateArticle;

public class UpdateArticleMessage extends KafkaMessage<UpdateArticle> {
    public UpdateArticleMessage() {
    }
}
```

画面 13:
```java
public UpdateArticleMessage(UpdateArticle data) {
    super(data);
}
```

画面 14:
```java
@Override
public String gettype() {
    return "update-article";
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 8:
标题: 3.1.2 定时消息封装的实体类
内容: 针对文章点赞、收藏等行为的实体类 com.heima.model.mess.app.UpdateArticle
内容: public class UpdateArticle implements Serializable {
内容: private static final long serialVersionUID = 392496820765182165L;
内容: // 修改文章的字段类型
内容: private UpdateArticleType type;
内容: // 文章id
内容: private Integer articleId;
内容: // 修改数据的增量，可为正数
内容: private Integer add;
内容: private Integer applierId;
内容: private Integer behaviorId;

画面 11:
标题: 3.1.3 添加发送消息的方法
内容: 修改 com.heima.common.kafka.KafkaSender
内容: 发送修改文章数据消息

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
