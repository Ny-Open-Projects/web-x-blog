# 画面线理解：22.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\22.课程总结【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:13, 00:24, 00:56, 01:17, 01:31, 01:43, 02:01, 02:08, 02:36, 02:40, 02:50, 02:56, 03:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:24:35

1) 这一组画面整体在讲什么（一句话）：
本课程系统讲解了 RocketMQ 的重试策略、集群部署、SpringBoot 整合 RocketMQ、分布式 WebSocket 实现以及基于 MongoDB 的地理信息索引与查询功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：课程介绍，包含 RocketMQ 的重试消息策略、集群搭建、SpringBoot 整合 RocketMQ、实现分布式 WebSocket 功能等模块。
画面 2：展示了一个名为 SyncProducer 的 Java 类，用于演示 RocketMQ 生产者端的重试机制，其中设置了发送失败时的重试次数为 3。
画面 3：讲解 RocketMQ 的集群模式，包括单个 Master、多 Master 模式、多 Master 多 Slave 模式及其优缺点。
画面 4：展示 SpringBoot 项目中引入 RocketMQ 依赖的 pom.xml 文件片段，使用了 Spring Boot 2.1.0.RELEASE 版本。
画面 5：展示了一个名为 TransactionListenerImpl 的 Java 类，用于实现 RocketMQ 的本地事务监听器，包含 executeLocalTransaction 方法。
画面 6：展示了一个名为 MessageHandler 的 Java 类，用于实现 WebSocket 消息监听器，包含 @Component 注解和 RocketMQMessageListener 注解。
画面 7：展示了一个 WebSocket 客户端界面，用于测试消息发送和接收，包含 URI、Request、Message Log 等部分。
画面 8：展示了一个地图找房的界面，包含多个红色标记点和一个绿色圆形区域。
画面 9：讲解 MongoDB 的地理索引，展示创建地理索引的命令和百度地图 API 的 URL。
画面 10：展示 MongoDB 中存储的房屋数据，包含 _id、hid、title、loc 等字段。
画面 11：展示 MongoDB 查询语句，用于查找距离指定坐标一定范围内的房屋。
画面 12：展示一个名为 MongoHouse 的 Java 类，用于表示房屋数据，包含 id、hid、title、loc 字段。
画面 13：展示一个名为 MongoHouseService 的 Java 类，包含一个查询房屋数据的方法，使用了 MongoTemplate。
画面 14：展示一个地图找房的界面，包含多个红色标记点和一个绿色圆形区域。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```java
package cn.itcast.rocketmq;
import org.apache.rocketmq.client.producer.DefaultMQProducer;
import org.apache.rocketmq.client.producer.SendResult;
import org.apache.rocketmq.common.Message;
import org.apache.rocketmq.remoting.common.RemotingHelper;
public class SyncProducer {
    public static void main(String[] args) throws Exception {
        DefaultMQProducer producer = new DefaultMQProducer("HAOME_IT");
        producer.setNamesrvAddr("172.16.55.185:9876");
        //消息发送头次数，重试3次
        producer.setRetryTimesWhenSendFailed(3);
        producer.start();
        String msgStr = "用户发送消息给用户";
        Message msg = new Message("haoke_in_topic", "SEND_MSG",
                msgStr.getBytes(RemotingHelper.DEFAULT_CHARSET));
        //发送消息，并且指定超时时间
        SendResult sendResult = producer.send(msg, 1000);
        System.out.println("消息状态：" + sendResult.getSendStatus());
        System.out.println("消息queue：" + sendResult.getMessageQueue());
        System.out.println("消息offset：" + sendResult.getQueueOffset());
    }
}
```

画面 4：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
        http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.0.RELEASE</version>
    </parent>
```

画面 5：
```java
import org.apache.rocketmq.spring.core.RocketMQTransactionListener;
import org.apache.rocketmq.spring.core.RocketMQTransactionState;
import org.apache.rocketmq.spring.support.RocketMQHeaders;
import org.springframework.messaging.Message;
import java.util.HashMap;
@RocketMQTransactionListener(txProducerGroup = "myTransactionGroup")
public class TransactionListenerImpl implements RocketMQTransactionListener {
    private static Map<String, RocketMQLocalTransactionState> STATE_MAP = new HashMap<>();
    @Override
    public RocketMQLocalTransactionState executeLocalTransaction(Message message, Object o) {
        String transId = (String) message.getHeaders().get(RocketMQHeaders.TRANSACTION_ID);
        try {
            System.out.println("执行操作1");
            Thread.sleep(500);
            System.out.println("执行操作2");
            Thread.sleep(500);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return RocketMQLocalTransactionState.COMMIT;
    }
}
```

画面 6：
```java
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.rocketmq.spring.annotation.MessageModel;
import org.apache.rocketmq.spring.core.RocketMQTransactionListener;
import org.apache.rocketmq.spring.core.RocketMQTransactionState;
import org.apache.rocketmq.spring.support.RocketMQHeaders;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.socket.TextMessage;
import org.springframework.web.socket.WebSocketSession;
import java.util.HashMap;
import java.util.Map;
@Component
@RocketMQMessageListener(topic = "haoke-in-send-message-topic",
        consumerGroup = "haoke-in-consumer",
        messageModel = MessageModel.BROADCASTING,
        selectorExpression = "SEND_MSG")
public class MessageHandler extends TextWebSocketHandler implements RocketMQMessageListener {
    @Autowired
    private RocketMQTemplate rocketMQTemplate;
    @Override
    public void afterConnectionEstablished(WebSocketSession session) throws Exception {
        super.afterConnectionEstablished(session);
    }
    @Override
    public void handleMessage(WebSocketSession session, TextMessage message) throws Exception {
        super.handleMessage(session, message);
    }
    @Override
    public void afterConnectionClosed(WebSocketSession session, CloseStatus status) throws Exception {
        super.afterConnectionClosed(session, status);
    }
}
```

画面 9：
```bash
#进入容器
docker exec -it mongodb /bin/bash
use testdb
db.house.createIndex({loc: "2d"}) #为house表的loc字段创建地理2d索引
{
  "createdIndexesBefore" : 1,
  "numIndexesAfter" : 2,
  "ok" : 1
}
db.house.createIndex({hid:1}, {unique:true}) #为house表的hid字段创建唯一索引
```

画面 10：
```json
{
  "_id": ObjectId("5c1c99c4d729d1aaabdbbf3"),
  "hid": 6,
  "title": "祥瑞新村",
  "loc": [121.48377804633, 31.231386755927]
}
{
  "_id": ObjectId("5c1c99c4d729d1aaabdbbf4"),
  "hid": 7,
  "title": "杨家板块",
  "loc": [121.5180613891443, 31.2388780213505]
}
```

画面 11：
```javascript
db.house.find({loc:{$near: [121.4261657004589, 31.2291141023585], $maxDistance:2/111.12}})
```

画面 12：
```java
@Builder
public class MongoHouse {
    @Id
    @JsonSerialize(using = ToStringSerializer.class)
    private ObjectId id;
    private Long hid;
    private String title;
    private Float[] loc;
}
```

画面 13：
```java
public MapHouseDataResult queryHouseData(Float lng, Float lat, Integer zoom) {
    double distance = BAI_DU_ZOOM.get(zoom) * 1.5 / 111.12; //1.5倍距离范围，根据实际
    Query query = Query.query(Criteria.where("loc").near(new Point(lng, lat)).maxDistance(distance));
    List<MongoHouse> mongohouses = this.mongoTemplate.find(query, MongoHouse.class);
    return new MapHouseDataResult(mongohouses);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 3：
标题：2、RocketMQ的集群
子标题：2.1、集群模式
内容：
- 单个Master
  - 这种方式风险较大，一旦broker重启或者
