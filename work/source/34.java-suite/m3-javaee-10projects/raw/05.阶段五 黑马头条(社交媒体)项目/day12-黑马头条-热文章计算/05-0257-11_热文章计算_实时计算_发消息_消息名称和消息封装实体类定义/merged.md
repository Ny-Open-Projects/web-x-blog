# 11_热文章计算_实时计算_发消息_消息名称和消息封装实体类定义

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\11_热文章计算_实时计算_发消息_消息名称和消息封装实体类定义【海量资源尽在 666java.com】.mp4
- 时长 4分55秒（音频 295s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就来去具体定义的消息刚才说了咱们需要去发送消息关于这个新微载采集咱们一会再做首先咱们要先定义当前的消息的名称这个消息名称的就是在当前的maven-test和卡巴卡的publist里边咱们都需要去设置当前的消息这样咱们已经定义完了在这你直接拷贝一下也可以开当前的这个东西好关掉然后是
[00:30] 在当前的common下边找到maven gun test然后呢在下边你再去加一条啊可以加一条那这个呢就是当前的消息的名称这个呢叫啥呢叫article update bus好那这是一个啊然后呢要干嘛呢然后是要在当前的cafka.propos里边再去定义一个好就是这个东西好那定义完之后啊这个名称呢咱们已经读到这了啊
[01:03] 这时候你干嘛要干嘛呢这时候需要到common的卡不卡中找到卡不卡这里边呢是有一个叫做topic config啊这时候呢你需要去在这去读出来读出来啊那读的方式呢比较简单你直接拷贝一下他在这呢定义一个private然后是string的啊这个干了去掉然后是这个是写成大写是吧然后这个呢也是大写那这个就做完了啊
[01:38] 这个消息名称已经定义完之后呢下面看一下下面呢准备是要定义一个消息实时消息封装的实体类实时消息那这时候你可以看一下当前的消息呢其实呢这个类啊已经创建完了给你们资料中已经包含了啊你可以看一下啊那这里边呢其实有啥呢首先第一个是类型就是修改文章的字段类型然后呢是文章的ID还有一个这个比较关键啊
[02:09] 这个你看这说了一句话说什么呢说是优感数据的增量可为正负可为正负啊那什么时候回正什么为负呢就这样你看点赞那就是正如果说取消点赞那就是减一点赞就是加一这个能听明白吧OK啊那这个呢是有一个正负的概念啊然后下面还有什么呢还有一个当前的用户啊还有当前的实体呀OK
[02:36] 那还有当前的这四个什么四个类型类型的话就包含了咱们说的啊收藏是吧评论评论并没有啊然后是点赞和阅读OK啊行那这个实体列啊咱们就说到这儿其实这个呢就是具体包装你的消息的内容的一个实体列好吧然后这里边还有一个列咱们需要去自己创建啊那这个呢叫做update article message那这个呢其实就是这样就是咱们具体要
[03:06] 发送消息的时候使用的这个类啊那这个创建哪啊连到comment卡普卡message下边啊有个app好咱们直接创建一下嗯嗯看message是吧在这呢去右键创建一个类是他这个类呢需要去记上谁啊就等卡普卡message啊卡普卡message这里边有一个范型咱们需要去设置一个范型呢就是update article好
[03:44] 有两个方法咱们需要去实现一下这个呢其实你就是前的消息的名称是吧什么叫update article是吗update articleupdate这里边其实还要去设置一个构造构造的话要设置两个啊第一个是无参的第二个是有参的啊那咱们再去设置一下public然后是updatearticle message第一个呢是无参的
[04:18] 然后第二个呢是有参的啊updatearticle message这个参数是谁啊这个参数就是刚才的update好咱们叫最终的咱们要叫supr中的什么把这个data传到supr中好啊那这样的话咱们就算是设置完了啊那这有问题是吧没有问题啊刚才是没有反应过来好吧行那这个消息的名称啊或者消息的实体列啊
[04:52] 下面已经加完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过 Kafka 消息队列封装文章点赞、收藏等行为的更新事件，并配置相关属性和消息类。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Quartz 定时任务类 AppJobArticleQuartz.java，其中定义了定时任务执行方法和描述触发器，用于触发文章分值计算。
画面 2: 展示项目中 maven-test.properties 配置文件，定义了数据库连接、Eureka 服务地址和 Kafka 消息主题。
画面 3: 展示 Kafka.properties 配置文件，定义了 Kafka 服务地址、消费者组和多个消息主题。
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
mysql.core.Mapper-mappers
mysql.core.alises.package=com.heima.model.**
mysql.core.tx.scan.package-execution(*.com.heima..Service.*.*())

# admin 账户名
admin.username=admin
admin.password=admin

hostname.Eureka.server=localhost
Eureka.client.serviceUrl.defaultZone=http://localhost:8761/Eureka/

#文章提交审核的消息名称
Kafka.topic.submit-article-auth=heima.topic.submit.article.auth.single.test
Kafka.topic.article-audit-success=Kafka.topic.article.audit.success.single.test
```

画面 3:
```properties
Kafka.config
Kafka.hosts=localhost:9092
Kafka.hosts=47.94.7.85:9092
Kafka.group=heima.${profiles.name}
# 单消息通道，需要以Kafka为前缀
Kafka.topic.admin-test=${Kafka.topic.admin-test}
#文章提交审核的消息名称
Kafka.topic.submit-article-auth=${Kafka.topic.submit-article-auth}
Kafka.topic.article-audit-success=${Kafka.topic.article-audit-success}
#app产生的更新文章数据消息
Kafka.topic.article-update-bus=${Kafka.topic.article-update-bus}
```

画面 4:
```java
package com.heima.common.Kafka;

import ...
@Data
@Configuration
@PropertySources({
    @PropertySource(value = "classpath:Kafka.properties")
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
package com.heima.common.Kafka;

import ...
@Data
@Configuration
@PropertySources({
    @PropertySource(value = "classpath:Kafka.properties")
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
Kafka.topic.article-update-bus=${Kafka.topic.article-update-bus}

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
package com.heima.common.Kafka.messages;

public class UpdateArticleMessage extends KafkaMessage<UpdateArticle> {
```

画面 11:
```text
进行消息体的传输封装
com.heima.common.Kafka.UpdateArticleMessage
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
package com.heima.common.Kafka.messages;

import com.heima.common.Kafka.KafkaMessage;
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
内容: 修改 com.heima.common.Kafka.KafkaSender
内容: 发送修改文章数据消息

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

