# 10.RocketMQ研究-Rocket基础-异步消息

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\10.RocketMQ研究-Rocket基础-异步消息【海量资源尽在 666java.com】.mp4
- 时长 4分40秒（音频 280s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面呢我们继续来看后边的内容Rocket MQ的基础知识前面我们已经理解了三种消息发送模式同步 一步和单向那么在入门程序当中我们只是演示了一个同步消息所谓同步消息呢就是各位看就是在发送的时候呀它必须等到结果那么有时候老师那我怎么能判断它是个同步消息呢
[00:27] 那我们说呢它发送的时候必须等到结果呀所以你看它其实是有一个返回值的也就是说呀下边如果我再执行一行代码那么它如果发送不成功这个返回值拿不到我们你第二行代码它能执行吗它执行不了对不对所以这就是同步的效果你可以简单理解为什么这个方法它是有返回值的它一定是一个同步方法对吧也就是说我说这个timeplate它
[00:55] 提供的API方法因为它有好多方法好那么我们再看那么还有一步消息一步消息之前我们也说了也就是它发给Broker对吧然后呢发给Broker呢具体这个成功与否的这个结果呢它是通过回调单独一个线程回调过来的对吧所以现在呢我们也可以来测试一下我们就在这个生产者simple当中来写一个一步的消息
[01:23] 那一步的消息同样还是需要这两个参数的对吧但是关键点就在于他在发消息的时候他用的是哪一个API方法对不对那么这个是rocket.mq的template你注意看啊要发一步了他发一步怎么发呢他有一个async那么这儿他要发的话这里边他怎么个一部分你看他比同部分就多了一个参数叫send callback
[01:51] 也就是个毁掉对吧好所以这些东西都不变只是要变了这里边是不是要有六一个东西六一个啥呀叫send comeback所以第一个方法很显然就是消息发送成功的一个什么一个毁掉而第二个呢很显然它是什么它是消息发送失败的毁掉各位这是不是就咱们刚才说的一步方法
[02:19] 异步调用它是有一个毁掉的对不对所以这里边呢你当然可以去打一个日志来看一下是不是啊好了那现在有时候老师呢怎么咱们去怎么演示一下呢那么演示的结果也是非常简单的啊来我们先把注释写上去注释写上去那这个呢其实就是一个什么对异步消息好那么我们也可以在单元测试这边去测一下吧那么我们考一下吧
[02:49] 然后呢我们前面加一个A就行了Athink是吧好然后呢那么我们是不是就可以准备发了呀那发的时候你要注意这儿你肯定要对吧调方法要调对嘛调不对咋发呀对这就是一个什么第一条异步消息但是异步消息有一点啊我要说一下咱们在跟踪这个日志因为你想你怎么跟踪呀你肯定要跟踪它的毁掉呀对不对
[03:19] 所以我准备再毁掉这你看我打断点了但是有一点要记得这个毁掉是在单独的线程你发送完了之后你注意这个测试程序一旦发送完它就结束了所以你不能让它结束你一结束这个进程就没了进程没了这个毁掉也就毁掉不了了所以这里边你让它干嘛呀有人应该已经知道我要干啥了你让它延时几秒吗行不行你让它延时几秒看到了吗好那现在呢我们就准备准备怎么弄
[03:49] 准备发了准备发了那发的话那我就直接执行就行了好看好走那你看啊看我这个生产者我刚才是不是在那个回调方法当中打断点了对回调方法当中的你看是不是发送成功了他一旦发送成功这是不是就回调了对那消费者是不是也消费了吧对消费者现在正在监听my topic吗是吧好这就是我们说的一步发送
[04:20] 单向发送呢就非常简单了也就是发出去不管结果直接回来大家看一下API自行测试就行了我这就不演示了这就是我们说的三种消息发送方式啊那么这个同步一步需要大家去重点掌握一下单向大家自己测试一下就行了好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面 9: 在 IDE 中展示 `application.yml` 文件，光标位于 `RocketMQ` 配置项，准备配置 RocketMQ。
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
RocketMQ:
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

