# 画面线理解：10.RocketMQ研究-Rocket基础-异步消息

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\10.RocketMQ研究-Rocket基础-异步消息【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:21, 01:12, 01:36, 01:54, 02:20, 02:37, 03:01, 03:26, 03:39, 03:52, 04:05, 04:18, 04:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 03:09:38

1) 这一组画面整体在讲什么（一句话）：
演示 RocketMQ 中同步消息与异步消息的发送方式及回调处理机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程目录结构，当前章节为“2.5 三种消息发送方式”，并介绍同步、异步、单向消息。
画面 2: 在 IDE 中展示 `ProducerSimple.java` 文件，光标位于同步消息发送方法 `sendSyncMsg` 的定义处。
画面 3: 展示课程目录结构，当前章节为“2.5.2 异步消息”，并介绍异步消息的回调机制。
画面 4: 在 IDE 中展示 `ProducerSimple.java` 文件，光标位于 `rocketMQTemplate` 对象的自动补全建议中，选中 `asyncSend` 方法。
画面 5: 在 IDE 中展示 `ProducerSimple.java` 文件，光标位于 `asyncSend` 方法的调用处，准备编写异步消息发送代码。
画面 6: 在 IDE 中展示 `ProducerSimple.java` 文件，光标位于异步消息回调方法 `onSuccess` 的定义处。
画面 7: 在 IDE 中展示 `ProducerSimple.java` 文件，光标位于异步消息回调方法 `onSuccess` 的定义处，准备编写成功回调代码。
画面 8: 在 IDE 中展示 `ProducerSimpleTest.java` 文件，光标位于测试类中 `testSendSyncMsg` 方法的调用处，准备发送同步消息。
画面 9: 在 IDE 中展示 `application.yml` 文件，光标位于 `rocketmq` 配置项，准备配置 RocketMQ。
画面 10: 在 IDE 中展示 `ProducerSimpleTest.java` 文件，光标位于测试类中 `testSendAsyncMsg` 方法的调用处，准备发送异步消息。
画面 11: 在 IDE 中展示 `ProducerSimpleTest.java` 文件，光标位于异步消息回调方法 `onException` 的定义处。
画面 12: 在 IDE 中展示 `ProducerSimpleTest.java` 文件，光标位于异步消息回调方法 `onException` 的定义处，准备编写异常回调代码。
画面 13: 展示课程目录结构，当前章节为“2.5.2 异步消息”，并展示异步消息回调方法 `onSuccess` 和 `onException` 的完整代码。
画面 14: 展示课程目录结构，当前章节为“2.5.2 异步消息”，并展示异步消息回调方法 `onSuccess` 和 `onException` 的完整代码，光标位于 `onException` 方法的 `e.getMessage()` 调用处。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
2.5 三种消息发送方式
RocketMQ 支持 3 种消息发送方式，即同步消息（sync message）、异步消息（async message）、单向消息（oneway message）。
2.5.1 同步消息
参见快速入门的测试程序。
2.5.2 异步消息
producer向 broker 发送消息时指定消息发送成功及发送异常的回调方法，调用 API 后立即返回，producer发送消息线程不阻塞，消息发送成功或失败的回调任务在一个新的线程中执行。
在ProducerSimple中编写发送异步消息的方法
```

画面 2:
```java
// 发送同步消息
@param topic 主题
@param msg 消息内容
public void sendSyncMsg(String topic,String msg){
    rocketMQTemplate.syncSend(topic, msg);
}
```

画面 3:
```
2.5.2 异步消息
producer向 broker 发送消息时指定消息发送成功及发送异常的回调方法，调用 API 后立即返回，producer发送消息线程不阻塞，消息发送成功或失败的回调任务在一个新的线程中执行。
在ProducerSimple中编写发送异步消息的方法
```

画面 4:
```java
public void sendSyncMsg(String topic, String msg) {
    SendResult sendResult = rocketMQTemplate.syncSend(topic, msg);
    System.out.println("");
}

public void sendAsyncMsg(String topic, String msg) {
    rocketMQTemplate.
```

画面 5:
```java
public void sendSyncMsg(String topic, String msg) {
    SendResult sendResult = rocketMQTemplate.syncSend(topic, msg);
    System.out.println("");
}

public void sendAsyncMsg(String topic, String msg) {
    rocketMQTemplate.asyncSend(topic, msg);
}
```

画面 6:
```java
//消息发送成功的回调
@Override
public void onSuccess(SendResult sendResult) {
}
//消息发送失败的回调
@Override
public void onException(Throwable throwable) {
}
```

画面 7:
```java
//发送异步消息
@param topic 主题
@param msg 消息内容
public void sendAsyncMsg(String topic, String msg){
    rocketMQTemplate.asyncSend(topic,msg,new SendCallback() {
        @Override
        public void onSuccess(SendResult sendResult) {
            //成功回调
            System.out.println(sendResult.getSendStatus());
        }
        @Override
        public void onException(Throwable e) {
            //异常回调
            System.out.println(e.getMessage());
        }
    });
}
```

画面 8:
```java
@SpringBootTest
public class ProducerSimpleTest {

    @Autowired
    ProducerSimple producerSimple;

    @Test
    public void testSendSyncMsg() {
        producerSimple.sendSyncMsg("my-topic", msg: "第2条同步消息");
    }

    @Test
    public void testSendAsyncMsg() {
        producerSimple.sendAsyncMsg("my-topic", msg: "第1条异步消息");
    }
}
```

画面 9:
```yaml
# application.yml
rocketmq:
  name-server: 192.168.1.100:9876
  producer:
    group: test
```

画面 10:
```java
@SpringBootTest
public class ProducerSimpleTest {

    @Autowired
    ProducerSimple producerSimple;

    @Test
    public void testSendSyncMsg() {
        producerSimple.sendSyncMsg("my-topic", msg: "第2条同步消息");
    }

    @Test
    public void testSendAsyncMsg() {
        producerSimple.sendAsyncMsg("my-topic", msg: "第1条异步消息");
        Thread.sleep(1000);
    }
}
```

画面 11:
```java
//消息发送失败的回调
@Override
public void onException(Throwable throwable) {
    System.out.println(throwable.getMessage());
}
```

画面 12:
```java
//消息发送失败的回调
@Override
public void onException(Throwable throwable) {
    System.out.println(throwable.getMessage());
}
```

画面 13:
```java
// 发送异步消息
@param topic 主题
@param msg 消息内容
public void sendAsyncMsg(String topic, String msg){
    rocketMQTemplate.asyncSend(topic,msg,new SendCallback() {
        @Override
        public void onSuccess(SendResult sendResult) {
            //成功回调
            System.out.println(sendResult.getSendStatus());
        }
        @Override
        public void onException(Throwable e) {
            //异常回调
            System.out.println(e.getMessage());
        }
    });
}
```

画面 14:
```java
// 发送异步消息
@param topic 主题
@param msg 消息内容
public void sendAsyncMsg(String topic, String msg){
    rocketMQTemplate.asyncSend(topic,msg,new SendCallback() {
        @Override
        public void onSuccess(SendResult sendResult) {
            //成功回调
            System.out.println(sendResult.getSendStatus());
        }
        @Override
        public void onException(Throwable e) {
            //异常回调
            System.out.println(e.getMessage());
        }
    });
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
