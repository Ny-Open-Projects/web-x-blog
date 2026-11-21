# 画面线理解：09.圈子推荐之接收消息并且处理

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\09.圈子推荐之接收消息并且处理_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:22, 01:45, 04:47, 06:47, 08:31, 10:13, 11:53, 13:31, 14:51, 16:26, 18:01, 20:10, 21:32, 23:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:56:35

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现 RocketMQ 消息消费，处理动态推荐相关的业务逻辑，包括消息接收、数据解析、MongoDB 操作和评分逻辑。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示课程目录结构，当前章节为“1.6.2 配置文件”，并预览了后续开发步骤的多张截图。
画面 2: 显示 `application.properties` 配置文件内容，包含 RocketMQ 和 Redis 的配置。
画面 3: 显示 `RecommendQuanZi` POJO 类的定义，包含 `id`, `publishId`, `score`, `date` 等字段。
画面 4: 显示 `QuanZiMsgConsumer` 类的初始结构，使用 `@RocketMQMessageListener` 注解监听 `tanhua-quanzi` 主题。
画面 5: 在 `QuanZiMsgConsumer` 类中，定义了 `private static final Logger` 字段，并导入了多个日志框架。
画面 6: 在 `onMessage` 方法中，使用 `ObjectMapper` 解析 JSON 消息，提取 `type`, `publishId`, `date`, `userId`, `pid` 字段。
画面 7: 继续在 `onMessage` 方法中，创建 `RecommendQuanZi` 对象并设置其属性。
画面 8: 在 `switch` 语句中，为 `case 6` 添加了 `break;`。
画面 9: 在 `switch` 语句中，为 `case 1` 和 `case 3` 添加了 `break;`，并为 `case 2` 和 `case 3` 设置了评分逻辑。
画面 10: 在 `switch` 语句中，为 `case 1` 添加了 `Publish publish = this.mongoTemplate.findById(...)` 代码。
画面 11: 在 `switch` 语句中，为 `case 1` 完成 `Publish publish = this.mongoTemplate.findById(...)` 代码。
画面 12: 在 `switch` 语句中，为 `case 1` 添加了根据 `publish.getText()` 长度计算 `score` 的逻辑。
画面 13: 在 `switch` 语句中，为 `case 1` 添加了 `try-catch` 块，并在 `catch` 块中记录错误日志。
画面 14: 在 `switch` 语句中，为 `default` 分支添加了 `recommendQuanZi.setScore(0d);` 代码，并在 `catch` 块中记录错误日志。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面 2:
```properties
spring.application.name=itcast-rocketmq
server.port=10082
# rocketmq相关配置
spring.rocketmq.nameServer=192.168.31.1:9876
spring.rocketmq.producer.group=tanhua
# Redis相关配置
spring.redis.jedis.pool.max-wait = 5000ms
spring.redis.jedis.pool.maxIdle = 10
spring.redis.jedis.pool.minIdle = 10
spring.redis.cluster.nodes=192.168.31.1:6379,192.168.31.1:6380,192.168.31.1:6381,192.168.31.1:6382
spring.redis.cluster.maxRedirects=5
# mongodb相关配置
spring.data.mongodb.uri=mongodb://192.168.31.81:27017/tanhua
```

画面 3:
```java
package com.tanhua.recommend.pojo;

import ...
@Data
@NoArgsConstructor
@AllArgsConstructor
public class RecommendQuanZi {
    private ObjectId id;
    private Long publishId; // 动态id，需要转化为Long类型
    private Double score; // 待分
    private Long date; // 时间戳
}
```

画面 4:
```java
package com.tanhua.recommend.msg;

import org.apache.rocketmq.spring.annotation.RocketMQMessageListener;
import org.apache.rocketmq.spring.core.RocketMQListener;
import org.springframework.stereotype.Component;

@Component
@RocketMQMessageListener(topic = "tanhua-quanzi",
        consumerGroup = "tanhua-quanzi-consumer")
public class QuanZiMsgConsumer implements RocketMQListener<String> {
    @Override
    public void onMessage(String s) {
    }
}
```

画面 5:
```java
private static final Logger LOGGER = LoggerFactory.getLogger(QuanZiMsgConsumer.class);
```

画面 6:
```java
private static final ObjectMapper MAPPER = new ObjectMapper();

@Override
public void onMessage(String msg) {
    try {
        msg.put("Type", type);
        msg.put("publishId", publishId);
        msg.put("date", System.currentTimeMillis());
        msg.put("userId", userId);
        msg.put("pid", publish.getPid());
        JsonNode jsonNode = MAPPER.readTree(msg);
        int type = jsonNode.get("type").asInt();
        String publishId = jsonNode.get("publishId").asText();
        Long date = jsonNode.get("date").asLong();
        Long pid = jsonNode.get("pid").asLong();
    } catch (Exception e) {
        LOGGER.error("消息处理失败！msg = " + msg);
    }
}
```

画面 7:
```java
RecommendQuanZi recommendQuanZi = new RecommendQuanZi();
recommendQuanZi.setDate(date);
recommendQuanZi.setPublishId(pid);
recommendQuanZi.setUserId(userId);
```

画面 9:
```java
switch (type) {
    case 1:
        break;
    case 2:
        recommendQuanZi.setScore(1d);
        break;
    case 3:
        recommendQuanZi.setScore(5d);
        break;
}
```

画面 10:
```java
Publish publish = this.mongoTemplate.findById(new ObjectId(publishId), Publish.class);
```

画面 12:
```java
int score = 0;
Publish publish = this.mongoTemplate.findById(new ObjectId(publishId), Publish.class);
if (length > 0 && length <= 50) {
    score = 1;
} else if (length > 50 && length <= 100) {
    score = 2;
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 1: PPT 标题为“1.6.2 配置文件”，左侧目录显示“1.6.2 配置文件”。
画面 14: PPT 标题为“1.7.1、发布动态”，下方显示 HTTP 请求的“Headers”和“Authorization”字段。

5) 无。
