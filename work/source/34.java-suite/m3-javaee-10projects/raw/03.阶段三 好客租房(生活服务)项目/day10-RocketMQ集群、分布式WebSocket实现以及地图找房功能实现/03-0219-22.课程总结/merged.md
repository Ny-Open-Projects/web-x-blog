# 22.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\22.课程总结【海量资源尽在 ubkz.com】.mp4
- 时长 3分21秒（音频 201s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来我们对今天的课程做一个总结那么今天我们首先学了RockMQ的从事的机制那么去了解了它的生产者和消费者的一个从事但重点要落在哪里呢?
[00:14] 消费者上面因为生产者其实我们比较简单只要设置从事次数以及一个操作时间就可以了
[00:22] 然后后面我们学习了ROCK的MQ的集群那么集群它有单个master有多个master以及多master多sleeve的一个模式但多master多sleeve又分为异步复制和同步双写那么我们其实比较建议大家使用的是后面这两个对吧在我们当然是生产环境如果说我们本地做开发的话其实第一个就够了那么这两个如何选择异步如何选择同步双写
[00:51] 那么就需要根据具体的业务场景去做出一个选择了OK好那么在后面我们去学习了如何通过spin boot去整合我们rockmq去做一个开发去了解了它的基本的一些生产者和消费者的一些代码的编写以及后面我们去学习了它的一些事物的消息的一些操作跟我们使用原生的API的操作基本上差不多只是做了一些简化的工作
[01:20] 然后后面我们基于log的MQ实现了一个WebSocket的一个分布式WebSocket的一个解决方案的一个具体的一个实现那么OK那么这个就不重复了我们也花了一些时间是不是做了一个讲解的实现那么希望大家能够动手去把这个功能去做一下去理解一下
[01:40] 那么在测试的时候需要大家注意的是我们需要去启动多个你的JVM然后才能够测试出这样的一个效果OK好那么在最后我们实现了一个功能就是地图找房的功能当然在这个里面我们在实现的过程中会涉及到一些前端的内容OK那么会有一些百度API百度地图API的一些操作大家对它有些基本的一些了解就可以了
[02:03] 但是这个里面其实需要我们重点需要掌握的一个内容呢就是这个mongoDB它的一个地理位置的一个索引这个是一个非常优秀也是非常好的一个功能那么通过它就可以去实现我们很多的一些我们现在非常使用比较平凡的这样的一些功能包括找附近的人附近的一些餐馆附近的什么什么什么就是给他一个位置然后找他周边的什么什么这是一个非常非常好的这样的一个东西OK
[02:31] 然后呢我们来看一下后面那么我们后面呢基于这个mongodb啊这个地理位置的这样的一个索引的一个特性那么我们就去可以实现我们的一个地图找房的这样的功能哎OK好那么我们就后面基于这种啊他的这个地理位置所以呢去做了一个具体的一个实现那么呃当然他会结合我们百度地图一些业务啊这个结合了这个业务的哎OK
[02:58] 好那么最后呢我们就实现了这样的一个效果那么其实我们已经把这个整个架构已经打好了对吧那我们后面只需要往里面去灌数据那么就可以实现这样的一个效果了OK这个呢就是我们今天的一些内容还是希望大家能够去跟着这个节奏去动手去敲里面的一些这个代码OK好那么今天内容我们就这么多讲到这里了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
本课程系统讲解了 RocketMQ 的重试策略、集群部署、Spring Boot 整合 RocketMQ、分布式 WebSocket 实现以及基于 MongoDB 的地理信息索引与查询功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：课程介绍，包含 RocketMQ 的重试消息策略、集群搭建、Spring Boot 整合 RocketMQ、实现分布式 WebSocket 功能等模块。
画面 2：展示了一个名为 SyncProducer 的 Java 类，用于演示 RocketMQ 生产者端的重试机制，其中设置了发送失败时的重试次数为 3。
画面 3：讲解 RocketMQ 的集群模式，包括单个 Master、多 Master 模式、多 Master 多 Slave 模式及其优缺点。
画面 4：展示 Spring Boot 项目中引入 RocketMQ 依赖的 pom.xml 文件片段，使用了 Spring Boot 2.1.0.RELEASE 版本。
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
package cn.itcast.RocketMQ;
import org.apache.RocketMQ.client.producer.DefaultMQProducer;
import org.apache.RocketMQ.client.producer.SendResult;
import org.apache.RocketMQ.common.Message;
import org.apache.RocketMQ.remoting.common.RemotingHelper;
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
import org.apache.RocketMQ.spring.core.RocketMQTransactionListener;
import org.apache.RocketMQ.spring.core.RocketMQTransactionState;
import org.apache.RocketMQ.spring.support.RocketMQHeaders;
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
import org.apache.RocketMQ.spring.annotation.MessageModel;
import org.apache.RocketMQ.spring.core.RocketMQTransactionListener;
import org.apache.RocketMQ.spring.core.RocketMQTransactionState;
import org.apache.RocketMQ.spring.support.RocketMQHeaders;
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
Docker exec -it mongodb /bin/bash
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

