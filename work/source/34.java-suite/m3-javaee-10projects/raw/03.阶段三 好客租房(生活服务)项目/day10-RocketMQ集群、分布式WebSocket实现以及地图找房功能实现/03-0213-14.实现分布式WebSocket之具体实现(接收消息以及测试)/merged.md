# 14.实现分布式WebSocket之具体实现（接收消息以及测试）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\14.实现分布式WebSocket之具体实现（接收消息以及测试）【海量资源尽在 ubkz.com】.mp4
- 时长 12分52秒（音频 773s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么下面呢我们来看一下接收消息啊那么接收消息之后应该怎么玩呢那么我们在这个位置来看一下啊那么我们就就拿这个类啊作为我们的一个消费者吧然后呢我们就在这直接去做一个实现实现我们的一个rocket mqrocket mq然后呢listenerlistenerrocket mq listener就他然后呢他所拿的消息呢就是一个字幕创
[00:28] 然后呢我们去实现它的一个方法下面是不是就会拿到一个具体的一个message对象然后呢我们需要给这个类是不是再添加几个注解一个叫做rocket listener这个注解然后呢我们给它添加几个内容那么第一个就是它的一个topic那么topic等于谁呢是不是等于我们去发送消息的这个
[00:54] 这个topic对吧注意没有冒号后面它冒号后面它呢是一个我们那个tag然后呢我们再给它去设置一个选择我选择什么呢我就选择这个tag我就接收这样的一个消息OK然后呢这是第一个这个第二个然后呢我们再来设置它的一个message的一个model那么消息的模式我们来看一下那么它有几种呢第一种是
[01:22] 这个集群第二种是广播那么我们应该用集群呢还是用广播呢大家思考一下其实我们应该用的是广播为什么呢我们前面说过啊就是我们的每一个每一个这个集群的一个节点他都需要去接收到我们这个消息对吧就是他也要接收对吧他也要接收哎他也要接收哎所以呢我们是一个广播啊广播这样的一个模式啊广播这样的模式然后呢我们去设置一下广播
[01:51] 然后呢我们还需要设置的是呃是什么呢我们来看一下这个呃这啊分组那么group组那么这个呢我们就把它设置为是一个这样的组吧im一个group哎ok那我们都把它设置为是这样的一个组那么现在呢我们是不是就应该能够去接收到我们这个topic下面的消息那我们来看一下这个消息内容的具体的一个
[02:20] 业务逻辑的一个编写对吧编写那么应该怎么做呢那么拿到这个Message之后那我们是不是就应该对我们Message做一个解析那么通过一个Mapper.z的什么treeZ的tree去做一个解析那么他拿到了这个JSON Node对吧JSON Node那么他有异常那么异常我们就捕获吧就捕获这个异常吧一旦有异常那我们就自己来捕获就可以了
[02:48] 那么我们需要拿到它里面的什么内容呢是不是点get一个我们需要拿到谁呢因为我们拿到之后我们重点是先要拿到什么拿到我们的这个2ID对吧拿到2ID之后然后呢我们去判断当前的这个JVM里的这个map它是否是存在我们这个sense如果存在就先来发消息如果不存在那就忽略所以说我们也需要去拿到2ID那么2ID怎么拿呢我们来看它的一个具体的一个json
[03:16] 那么json我们需要拿到它的一个to这个下面的id对吧那应该是这样来拿那就是通过一个get to点继续再get一个id然后点long value这样的话是不是我们就拿到它的一个这个叫做to to id这个就是to id
[03:42] 好那么有了这个2ID之后呢这个逻辑是不是跟我们上面这个逻辑是不是就非常的像了对吧非常像了那么如果如果他在我当前的这个这个session中那么也并且是一个open状态的话那么我是不是就向他去发送消息就可以了如果不是的话那么注意如果else的话那么我其实是不需要做任何处理对吧不需要做任何处理的对吧不需要做处理
[04:11] OK这个其实我们这个else不应该写但是呢为了给大家说明一下这个逻辑说不定我们就写这样的空的一个else好那么这个里面应该怎么玩呢就去把这个逻辑把这两个逻辑扣过来首先他应该去发动消息第二呢应该去修改我们这个消息的一个状态好那么我们来看一下那么这个消息消息的内容其实就是我们这个消息对吧就这个message
[04:37] 然后我们来消息的 id那么就通过一个我们 json node.get id.as text它这个是要求要求什么它要求的是一个object id那么这样我们就给它去干嘛去new一个object id那么它通过我们这个字符串
[05:09] 把这个导入进来好导入进来之后呢是不是我们就有了一个传递了一个这个OBJIT给他这样的话呢我们其实就实现了这样的一个业务逻辑了对吧好嘞那么我们在这个位置也打一个断点那么接下来呢我们也去做一个测试看他会发生什么OK走那么把它停掉那么我们现在启动起来了我们来做一个测试
[05:35] 我们依然还是拿刚刚的我们这个例子做一个测试然后向他去发一个消息发一个你好二吧走发消息那么我们来看一下没有去打开这个链接重新打开一下走然后呢这个消息已经来了然后往下面走走走走走你发现他不在线对吧发消息然后走那么显然我们现在注意看现在我们是不是拿到这个消息了那么拿到这个消息往下面走走是不是拿到这个ID对吧
[06:13] 拿了2ID然后呢去拿你发现它是不是也没有啊因为当前JVM里面显然没有这个1003对不对那么接下来我们就开始去做这样的一个测试了对吧那么咱们这么来测啊那么我现在呢我这个1001那么我再来一个这个比如说我这个1002拿1002也来做一个测试啊打开这个连接哎这个也错了这个是81啊打开连接好嘞然后呢我向1002发消息我看能不能能不能发送过去啊1002
[06:44] 然后呢你好你好1002走那么看一下能不能发送过去走走哎你发现是不是走到上面这个逻辑啊可以直接向他发消息推送消息走哎OK然后呢我们发现1002里面是不是已经就收到了我们这个消息对吧好那么接下来我们来看一下如果我们要部署多个Pomcat那么应该怎么去玩或者说我们去启动我们多个这个服务应该怎么搞呢那我们应该这么来玩啊
[07:13] 就是我们去修改一下它的一个配置文件注意我们之前这个启动的标去停止然后呢我们在这个位置呢写一个1018082然后呢再次做一个启动但是呢你要注意是我们现在这个启动它是一个叫单立的一个模式单实力模式那么不能启动多个啊那我们需要给它改一下那么把这个勾给它去掉点个应用那么我们现在就可以去启动多个了走这是我们启动第二个那么它的端口呢是18082
[07:42] 那么我们让1003这个用户在在这个18082这个里面进行连接这样的话呢我们看他能是否跨TVM可以发这样的消息那么如果可以那么我们是不是就已经就实现了我们分布式的这样的一个WebSocket的一个方案的一个解决啊OK那么现在他是不是已经也启动起来了好嘞那么接下来呢我们就
[08:06] 再打开一个我们这个在线的工具啊然后他连接的呢就是我们的180821003然后打个连接好嘞好那么现在呢我们向1003去发消息你好1003在吗然后呢点击发送走来看一下那么往下面走走走发现他不在线对吧不在线干嘛呢就直接发送MQ消息通过走然后呢再去做一个测试看一下
[08:36] 在我们的注意我已经切换到这个里面来了在这个里面我们再去看一下它有没有在线你发现是不是在线对吧发现100你看to id是不是1003那么1003在我们这个gm就是第二个gm在线然后我们继续往下面走发送然后做一个更新通过好那么我们来看一下1003这个里面收到消息了吗是不是同样也收到消息了那我们给1001回个消息
[09:05] 能把消息回回去吗当然是可以的对吧那么给他发一个1001他说你好在吗你说什么呀在的在的有事吗有事吗好那么我给1001是不是发个消息走那么我又进入到是不是我的这个JVM里面来看一下走那么1001他在我们这个JVM吗你发现他显然又不在对不对
[09:37] 那么我还是向我的MQ是不是发消息通过走那么这个里面他找这个里面是不存在的通过那么在我们的这个GVM里面是不是有的消息走通过吧然后呢我们来看一下那么这个是给1008的消息怎么还有消息过来啊那这样通过那么这个断点我们就拿掉吧然后呢我们来看一下1001这个里面拿到消息了吗你发现是不是报消息了你看这个是不是1003
[10:07] 给他发来的消息就说在的有事吗对吧给103发一个就说你说好久不见好久不见还好吗还好吗然后呢走好这样的话呢我们是不是给1013又发了个消息啊这里面断点怎么还有啊把断点拿掉走上面这个断点断点没了哈好嘞那么我们来看一下这里面拿到消息了吗你看好久不见还好吗说不定拿到消息了那么我在1003能不能给1002发消息呢
[10:38] 当然是可以消息内容就是说1002在吗然后发动消息走那么来看1002能不能接收到消息你看是不是1003发来的消息1002在吗对不对你看他的一个from谁的from是不是1003对不对OK那么也就是说1001和1002他们两个是在同一个JVM里面而1003是在另外一个JVM里面我们可以发现
[11:07] 他们三个之间是不是都可以随意的去发送这个消息那么中间起作用的是不是就是我们这个MQ只要一旦你跨一个JVM那么就会把消息发送到我们这个消息系统然后每一个这个节点都会拿到我们的一个这个消息对吧做一个这样的一个处理OK那么这个是不是就是我们所实现的一个这个分布式的一个WebSocket的一个解决方案当然了我们这个解决方案中它也存在一些不完善的一些点
[11:36] 比如说我们的用户下线我们是不是应该对应的把这个里面的这个里面的session给它删除掉对吧这第一个那么第二个呢就是对于同一个这个用户比如说我这个我这个节点发出了一个消息那么我是不是也会接收到这个消息其实对我而言接收到这个消息没什么用
[11:58] 因为肯定不在我这个里面如果在我这个里面的话我也不会去发消息了对不对那么我们是不是就可以去做一个小的逻辑的优化对吧比如说我们在发送消息的时候去携带一个我们当前的一个这个节点的ID比如给它生成一个ID比如这个是1这个是2对吧那这个是3那么我们去携带一个这个1或者2或者3那么当我这个节点拿到这个消息发现这个里面这个值是1的话
[12:26] 那我就不做处理了因为这个消息是我自己发出去的就是这样的一个小优化那么OK那么到目前为止我们是不是基本上也就实现了我们的一个分布式的一个WebSocket这样的一个解决方案对吧我们去借助一段的工具可以做这样一个测试可以在跨JVM的一个情况下面可以任意的去发送个消息那么OK好那么关于我们这个消息的一个接收我们就讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 和 RocketMQ 的分布式 WebSocket 消息推送系统，重点展示消息处理逻辑、会话管理、消息状态更新及 RocketMQ 消息发送。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 MessageHandler.java 中的代码，当用户可能下线时，更新消息状态并发送消息到 RocketMQ 主题 "haoke-im-send-message-topic:SEND_MSG"。
画面 2: 显示 MessageHandler.java 的类定义，包含 @Component、@RocketMQMessageListener 注解，以及 @Autowired 注入的 messageDAO 和 rocketMQTemplate。
画面 3: 显示 @RocketMQMessageListener 注解的配置，指定 topic 为 "haoke-im-send-message-topic"，selectorExpression 为 "SEND_MSG"。
画面 4: 显示 MessageHandler 类的 afterConnectionEstablished 方法，用于将用户 session 存入 SESSIONS 映射表。
画面 5: 显示 RocketMQ 控制台，查询主题 "haoke-im-send-message-topic" 下的消息，显示两条消息记录。
画面 6: 显示 onMessage 方法中，解析消息 JSON，获取 toId，判断用户是否在线，若在线则发送消息，否则更新消息状态并发送到 RocketMQ。
画面 7: 显示 onMessage 方法中，解析消息 JSON，获取 toId，判断用户是否在线，若在线则发送消息，否则更新消息状态并发送到 RocketMQ。
画面 8: 显示调试器断点，正在执行 onMessage 方法，变量 msg 正在被解析。
画面 9: 显示 Simple WebSocket Client 页面，用户发送消息后，消息日志中显示接收方收到消息。
画面 10: 显示 application.properties 文件，其中包含消息保存到 MongoDB 的配置。
画面 11: 显示调试器断点，正在执行 onMessage 方法，变量 msg 正在被解析。
画面 12: 显示 onMessage 方法中，解析消息 JSON，获取 toId，判断用户是否在线，若在线则发送消息，否则更新消息状态并发送到 RocketMQ。
画面 13: 显示 PPT 页面，标题为“4.1、实现方案”，图示了 socket 客户端与 socket 服务端的交互，服务端通过 Map(session) 管理会话，并订阅消息系统。
画面 14: 显示 Simple WebSocket Client 页面，用户发送消息后，消息日志中显示接收方收到消息，验证消息系统已生效。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
this.messageDAO.updateMessageState(message.getId(), status: 2);
}else{
    //该用户可能下线，可能在其他的节点中，发送消息到MQ系统
    //需求：添加tag，便于消费者对消息的筛选
    this.rocketMQTemplate.convertAndSend ( destination: "haoke-im-send-message-topic:SEND_MSG", msg);
```

画面 2:
```java
import cn.itcast.haoke.im.pojo.UserData;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.RocketMQ.spring.annotation.RocketMQMessageListener;
import org.apache.RocketMQ.spring.core.RocketMQTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.socket.TextWebSocketHandler;
import java.util.HashMap;
import java.util.Map;
@Component
@RocketMQMessageListener(
        topic = "haoke-im-send-message-topic",
        selectorExpression = "SEND_MSG",
        messageModel = MessageModel.CLUSTERING
)
public class MessageHandler extends TextWebSocketHandler implements RocketMQListener<String> {
    @Autowired
    private MessageDAO messageDAO;
```

画面 3:
```java
@RocketMQMessageListener(
        topic = "haoke-im-send-message-topic",
        selectorExpression = "SEND_MSG",
        messageModel = MessageModel.CLUSTERING
)
```

画面 4:
```java
@Override
public void afterConnectionEstablished(WebSocketSession session) throws Exception {
    Long uid = (Long) session.getAttributes().get("uid");
    //将当前用户的session就置到map中，后面会使用相应的session通信
    SESSIONS.put(uid, session);
}
```

画面 6:
```java
@Override
public void onMessage(String msg) {
    try {
        JsonNode jsonNode = MAPPER.readTree(msg);
        long toId = jsonNode.get("to").get("id").longValue();
        //判断用户是否在线
        WebSocketSession toSession = SESSIONS.get(toId);
        if (toSession != null && toSession.isOpen()) {
            //TODO 具体格式需要和前端对接
            toSession.sendMessage(new TextMessage(msg));
        }else{
            //该用户可能下线，可能在其他的节点中，发送消息到MQ系统
            //需求：添加tag，便于消费者对消息的筛选
            this.messageDAO.updateMessageState(message.getId(), status: 2);
            this.rocketMQTemplate.convertAndSend ( destination: "haoke-im-send-message-topic:SEND_MSG", msg);
        }
    }catch (Exception e) {
        e.printStackTrace();
    }
}
```

画面 7:
```java
try {
    JsonNode jsonNode = MAPPER.readTree(msg);
    long toId = jsonNode.get("to").get("id").longValue();
    //判断用户是否在线
    WebSocketSession toSession = SESSIONS.get(toId);
    if (toSession != null && toSession.isOpen()) {
        //TODO 具体格式需要和前端对接
        toSession.sendMessage(new TextMessage(msg));
    }else{
        //该用户可能下线，可能在其他的节点中，发送消息到MQ系统
        //需求：添加tag，便于消费者对消息的筛选
        this.messageDAO.updateMessageState(message.getId(), status: 2);
        this.rocketMQTemplate.convertAndSend ( destination: "haoke-im-send-message-topic:SEND_MSG", msg);
    }
} catch (Exception e) {
    e.printStackTrace();
}
```

画面 10:
```properties
#将消息保存到MongoDB
message = this.messageDAO.saveMessage(message);
String mqJson = MAPPER.writeValueAsString(message);
//判断用户是否在线
WebSocketSession toSession = SESSIONS.get(toId);
if (toSession != null && toSession.isOpen()) {
    //TODO 具体格式需要和前端对接
    toSession.sendMessage(new TextMessage(mqJson));
}
```

画面 12:
```java
@Override
public void onMessage(String msg) {
    try {
        JsonNode jsonNode = MAPPER.readTree(msg);
        long toId = jsonNode.get("to").get("id").longValue();
        //判断用户是否在线
        WebSocketSession toSession = SESSIONS.get(toId);
        if (toSession != null && toSession.isOpen()) {
            //TODO 具体格式需要和前端对接
            toSession.sendMessage(new TextMessage(msg));
        }else{
            //该用户可能下线，可能在其他的节点中，发送消息到MQ系统
            //需求：添加tag，便于消费者对消息的筛选
            this.messageDAO.updateMessageState(message.getId(), status: 2);
            this.rocketMQTemplate.convertAndSend ( destination: "haoke-im-send-message-topic:SEND_MSG", msg);
        }
    }catch (Exception e) {
        e.printStackTrace();
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 13:
标题：4.1、实现方案
架构图：
- 左侧：socket 客户端（多个圆形代表客户端）
- 中间：socket 服务端（包含三个 Map(session) 模块）
- 右侧：消息系统
- 箭头：从 socket 客户端指向 socket 服务端，标注“发送消息”；从 socket 服务端指向消息系统，标注“订阅”。

画面 14:
标题：5、地图找房
表格数据：
- 表格标题：消息日志
- 表格内容：
  - 时间：10:34:02
  - 消息内容：{"id":"5c1df024757f73648a5c4b0c","msg":"在吗","status":1,"sendDate":"154546892548","toId":"null","from":"id:1003,username":"wong"}
  - 时间：10:34:02
  - 消息内容：{"id":"5c1df024757f73648a5c4b0c","msg":"在吗","status":1,"sendDate":"154546892548","toId":"null","from":"id:1003,username":"wong"}
  - 时间：10:34:02
  - 消息内容：{"id":"5c1df024757f73648a5c4b0c","msg":"在吗","status":1,"sendDate":"154546892548","toId":"null","from":"id:100

