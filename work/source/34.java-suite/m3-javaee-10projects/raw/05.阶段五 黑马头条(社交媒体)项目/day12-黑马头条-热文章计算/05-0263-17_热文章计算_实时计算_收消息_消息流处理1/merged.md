# 17_热文章计算_实时计算_收消息_消息流处理1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\17_热文章计算_实时计算_收消息_消息流处理1【海量资源尽在 666java.com】.mp4
- 时长 11分41秒（音频 701s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就继续往下讲啊刚才呢咱们是写了当前的接收消息的方法同时呢咱们在这儿也去定义了一个监听的类咱们可以再重新捋一遍啊你看现在的咱们要去接收流的消息是吧咱们去继承实现了一个卡布卡斯这样的listing然后这里面呢有量有有几个三个方法是吧第一个呢是这个第二个是这个这个量啊
[00:27] 这个呢是要接收消息的名称然后这个呢是要发送消息的名称这个是具体处理消息的一个方法当然这个我这边是意思就是我这边是要接收并且呢我要发送我要发送啊那发送的发送的消息呢是我用的当前的这个类去接收当然这个类咱们还没有写啊咱们只是定义了大概的一个框架好吧那你说这里边啊这里边那这是去接收啊这是去发送
[00:57] 哎没问题是吧那这时候那这个消息该怎么去拿那这样啊咱们先写一段先写一段啊然后呢咱们可以打了段点先去测试一下先去看一眼这个数据到底是什么样的然后咱们再去往下写好吧那这个该怎么去写呢就这样啊咱们就直接去return一个什么它呢是需要一个svamp这种呢咱们就可以用它的一个子类啊new一个什么不对啊stream
[01:27] 点map然后呢咱们可以在这里边去拿到值然后值之后呢咱们再去new当前的key value这个呢当前的key呢是他key然后是这是vl有问题这个return删了我看看啊这少少个花啊行那这样的话就可以了啊那拿到这之后啊你这时候是不是他这还报错是吧没错没有事啊因为你没有return啊咱们再去return一个return哪个呢return当前一个
[02:02] 又一个key value这里边你再去设置值就可以设置什么值比如说我要去设置一个两个参数一般是两个参数这两个参数人们先不给先给一个空先给一个空重点咱们要去看一下里边怎么去拿到咱们之前发的消息这消息发送在哪发送还知道吧在哪发的这不是在当前的行为这一段可以再打开
[02:33] 打开当前的卡不卡这里有一个behaviour message center这里边其实就是发两个一个是reduce一个是plus是吧一个是加一个是减OK他最终消息的封装就是update article message最终其实就是让这个类去接收到当前那个就是update article message就可以这样咱们在这可以去接收一下我可以告诉你
[03:01] 里边的真正的消息呢其实就是个VL就是个VL这个VL呢其实就是一个String的字符串那它呢其实呢就是一个什么当前当前这个对象的一个String的JSON字符串那你说该怎么办假如说我要我就想获得到它那你该怎么办呢是吧咱们可以先去干嘛呢先去设置一个东西比如说咱们叫Value就等于好吗
[03:29] 就是把当前的vr转传进去这个呢就好写啊这怎么好写呢其实就是干嘛呢就是通过json去把把这个字幕啊转成什么转成一个对象就可以啊那这时候咱们就可以去转一下之前呢咱们可以在这先去注入一个哪个入一个private是object mypro这是他的一个这种工具包好拿到之后呢咱们在这啊可以直接去
[04:02] 当前的有一个ride value然后你把当前的vr传进去然后你你返回的类型拿过来updateradical message这样就可以了啊这加一个class好这样就可以了啊这时候呢咱们需要去package一下那这个呢其实就是咱们最终要要返回的这个底下啊比如说怎么叫msg啊等于一个当好吧然后呢最终呢把这个东西呢复一下值
[04:34] 换成之后你这时候你再去return像MSD可以了看的话对象拿到了好那之后验证一下好吧验证一下咱们把这个value打印一下打印一下先打印一下他们先看一下这个效果咱们把这个在这打个断点你说我该怎么去测试的测试起来其实很方便因为我这块只要是CM1启动我是不是就自动监听了是吧
[05:04] 所以说呢你现在是首要任务先把当前这个Article这个项目启动稍等启动完之后呢你需要在Behaver这一块呢去发一个消息去发一个消息啊咱们先看一下启动有没有报错啊当启动的时候呢你需要嗯稍等啊稍等这会儿我要去再去说一个事啊因为这会儿啊咱们需要用到Kabooka Stream这个理由是吧所以说呢你要在当前的Article中
[05:34] 要去干嘛呢引入当前的配置这配置刚才我加了啊我加了啊所以说这块他没有报错啊也就是说你不仅要引入卡不卡还要引入卡不卡因为这个是新的封装好吧这东西一定要加进来啊然后这时候呢你再去启动就可以了好吧启动一下啊好那这个启动着啊咱们再回过头来去说比如说啊那我这一块呢已经哎我这边已经启动了已经在监听了
[06:04] 那我的消息该怎么拿呢那这时候呢你需要在Behaver这一端去干嘛呢去发送消息看有没有报错啊应该是没有报错的啊稍等应该是启动完了啊没有报错这时候呢你要在Behaver这一端呢去发送消息那发送消息的话呢其实就是调用这两个方法就可以是吧这样啊那咱们呢目前的话呢其实就两块内容第一个是阅读第二个呢是当前的点赞
[06:33] 这时候呢你只要是保存一点点赞的信息就干嘛呢哎就可以去自动的去发送消息因为我的EU代码里边其实已经包用了当前的消息啊所以说呢咱们在这啊直接去创建一个测试类来打开在这里边啊咱们再去创建一个啊你看我这边是写了一个啊咱们直接拷过来就可以啊那什么意思可以看一下啊我现在我去注入了一个AAP like behavior Service然后呢这里边去调了一个当前的保存
[07:09] 点赞的信息的行为点赞信息的行为啊这里边传达参数你看一下啊第一个呢就是当前的用户啊你要用户你要去设置一下必须要设置啊然后第二个呢就是你要去给这个DTO中去设置值啊其实最主要的设置一个120啊10120这是啊当前能够查看的一个文章的信息ID啊还有这个两个零的都是操作的文章所以说呢你最终测试的时候就可以这么去测试啊只要我一
[07:38] 点保存在保存的时候呢它就会自动的去发送消息你可以看一下当前的一块内容这块内容是不是咱们在这去设置了消息发送的你看这你只要是保存成功我就会自动的去发送消息好吧那这时候呢咱们就可以在这啊打到点啊看看啊把这些没用的关掉这也关掉好在这已经打到点了啊这时候呢你就可以直接在这块去发送就可以了啊
[08:09] 比如说我去执行Dbug然后他就会去保存保存的时候他就会发消息发消息的时候我这块就能断点就能到这好咱们先看一下当前的消息的结构是什么样的看看是不是当前的Value是不是你发送的消息稍等快结束了正常的话应该断点能够到这我看看写的有没有问题好没有问题你看这个断点也到这了看到了吗当前这个Value其实就是消息的
[08:54] 内容你看咱们可以往下执行一步最终它是解析了当前这个数据你看这个value里边就是封装什么东西第一个就是咱们直接看Data就可以了Data里边是不是当前Archive ID是10120然后Add咱们是加1是吧然后是AdUser用户ID是1然后是当前的操作是2当前行为ID是2但是这里边最主要的一个东西就是当前的Type
[09:23] 这个type的话其实是like看到了吗是likes也就是说咱们的点赞然后并且是加一并且是加一好那这个数据拿到之后下面咱们就继续往下做咱们可以把断点把这个服务先停了停了之后下面咱们就继续往下看你说我这一块该怎么去返回其实这块咱们要需要去把这个参数直接放到这里边就可以
[09:49] 直接放到这里边那我该怎么去封装这个参数呢你看我现在就这么写那第一个参数咱们就可以从value中get.article.to3这是第一个咱们把这个当前的article id是传过去然后第二个呢第二个的话就是当前的咱们要去设置成这样的一个类型比如说lex冒号咱们有可能是-1
[10:18] 咱们先设置先这样保存保存完之后咱们后续还会再次去处理那这个拼成这么一个串好拼吗好拼可以看一下首先这时候还是从value中拿指点get有一个什么咱们应该是拿这个data有一个type名其实就是like如果你要想拼的话前面加个引号加个冒号再去加什么
[10:48] 你加那个就可以了啊而是y6.getDate.getDD好那这样的话呢就是新成了这样的一个效果好吧那行啊那其实咱们之前呢也分析过啊如果说你这么写的话呢其实是可以的但是你要是去解析的话就不太好解析并且呢你说我每发一次呢我都要去处理一次这样不太好其实呢咱们要去做一个时间窗口去
[11:17] 聚合当前的这种数据那时间转口是怎么设置的咱们下面呢就来去设置一个呃这种时间转口就是每10秒呢我去聚合一次数据然后呢再去发送消息发送谁呀发送给他再去更新当前的这种什么这种什么点赞的评论的或者说阅读的信息好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Kafka Stream 处理文章行为事件，并通过自定义的 `BehaviorMessageSender` 发送消息，同时展示相关代码结构和调试过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 项目结构：`heima-leadnews-article` 模块下的 `stream` 包中包含 `HotArticleStreamHandler.java`。
- 代码：`HotArticleStreamHandler` 类中定义了 `listenTopic()` 和 `sendTopic()` 方法，返回 Kafka Topic 名称。
- 代码：`getService()` 方法返回 `null`。

画面 2：
- 项目结构：`heima-leadnews-article` 模块下的 `stream` 包中包含 `HotArticleStreamHandler.java`。
- 代码：`HotArticleStreamHandler` 类中 `sendTopic()` 方法返回 `kafkaTopicConfig.getArticleIncHandle()`。

画面 3：
- 代码：`getService()` 方法中 `stream.map(...)` 的 `value` 变量被赋值后，`return new KeyValue<>("","")`。
- 代码：`return null;`。

画面 4：
- 项目结构：`heima-leadnews-article` 模块下的 `stream` 包中包含 `HotArticleStreamHandler.java`。
- 代码：`HotArticleStreamHandler` 类中 `getService()` 方法返回 `stream.map(...)` 的结果。

画面 5：
- 项目结构：`heima-leadnews-behavior` 模块下的 `src/main/java/com/heima/behavior` 包中包含 `BehaviorMessageSender.java`。
- 代码：`BehaviorMessageSender` 类中 `sendArticlePlus()` 方法接收 `UpdateArticleMessage` 和用户 ID，调用 `kafkaSender.sendArticlePlus(...)`。

画面 6：
- 代码：`BehaviorMessageSender` 类中 `sendArticlePlus()` 方法中 `UpdateArticleMessage temp = parseMessage(...)`。
- 代码：`kafkaSender.sendArticlePlus(temp);`。

画面 7：
- 代码：`HotArticleStreamHandler` 类中 `getService()` 方法中 `stream.map(...)` 的 `value` 变量被赋值后，`return new KeyValue<>("","")`。
- 代码：`return null;`。

画面 8：
- 代码：`IntConfig.java` 文件中 `@ComponentScan` 注解的 `value` 属性包含 `com.heima.common.quartz`, `com.heima.common.Kafka`, `com.heima.common.kafkastream`。

画面 9：
- 代码：`BehaviorMessageSender` 类中 `sendArticlePlus()` 方法中 `UpdateArticleMessage temp = parseMessage(...)`。
- 代码：`kafkaSender.sendArticlePlus(temp);`。

画面 10：
- 代码：`BehaviorTest` 类中 `testLikesSave()` 方法中 `AppUser user = new AppUser();`。
- 代码：`user.setId(1L);`。
- 代码：`LikesBehaviorDTO dto = new LikesBehaviorDTO();`。
- 代码：`dto.setArticleId(10120);`。
- 代码：`dto.setOperation((short) 1);`。
- 代码：`dto.setType((short) 1);`。
- 代码：`applikesBehaviorService.saveLikesBehavior(dto);`。

画面 11：
- 代码：`HotArticleStreamHandler` 类中 `getService()` 方法中 `stream.map(...)` 的 `value` 变量被赋值后，`return new KeyValue<>("","")`。
- 代码：`return null;`。

画面 12：
- 代码：`HotArticleStreamHandler` 类中 `getService()` 方法中 `stream.map(...)` 的 `value` 变量被赋值后，`return new KeyValue<>("","")`。
- 代码：`return null;`。

画面 13：
- 代码：`HotArticleStreamHandler` 类中 `getService()` 方法中 `stream.map(...)` 的 `value` 变量被赋值后，`return new KeyValue<>("","")`。
- 代码：`return null;`。

画面 14：
- 代码：`HotArticleStreamHandler` 类中 `getService()` 方法中 `stream.map(...)` 的 `value` 变量被赋值后，`return new KeyValue<>("","")`。
- 代码：`return null;`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1：
```java
@Autowired
private KafkaTopicConfig kafkaTopicConfig;

@Override
public String listenTopic() {
    return kafkaTopicConfig.getArticleUpdateBus();
}

@Override
public String sendTopic() {
    return kafkaTopicConfig.getArticleIncHandle();
}

@Override
public KStream<?, String> getService(KStream<?, String> stream) {
    return null;
}
```

画面 2：
```java
public class HotArticleStreamHandler implements KafkaStreamListener<KStream<?, String>> {
    @Autowired
    private KafkaTopicConfig kafkaTopicConfig;

    @Override
    public String listenTopic() {
        return kafkaTopicConfig.getArticleUpdateBus();
    }

    @Override
    public String sendTopic() {
        return kafkaTopicConfig.getArticleIncHandle();
    }

    @Override
    public KStream<?, String> getService(KStream<?, String> stream) {
        return null;
    }
}
```

画面 3：
```java
public KStream<?, String> getService(KStream<?, String> stream) {
    return stream.map((key, val) -> {
        UpdateArticleMessage value = format(val);
        return new KeyValue<>("", "");
    });
}
```

画面 4：
```java
public KStream<?, String> getService(KStream<?, String> stream) {
    return stream.map((key, val) -> {
        UpdateArticleMessage value = format(val);
        return new KeyValue<>("", "");
    });
}
```

画面 5：
```java
public class BehaviorMessageSender {
    @Autowired
    private KafkaTopicConfig kafkaTopicConfig;

    public void sendArticlePlus(UpdateArticleMessage message, Long userId, boolean isSendArticle) {
        UpdateArticleMessage temp = parseMessage(message, userId, isSendArticle);
        kafkaSender.sendArticlePlus(temp);
    }
}
```

画面 6：
```java
public void sendArticlePlus(UpdateArticleMessage message, Long userId, boolean isSendArticle) {
    UpdateArticleMessage temp = parseMessage(message, userId, isSendArticle);
    kafkaSender.sendArticlePlus(temp);
}
```

画面 7：
```java
public KStream<?, String> getService(KStream<?, String> stream) {
    return stream.map((key, val) -> {
        UpdateArticleMessage value = format(val);
        System.out.println(value);
        return new KeyValue<>("", "");
    });
}
```

画面 8：
```java
@ComponentScan(value = {
    "com.heima.common.quartz",
    "com.heima.common.Kafka",
    "com.heima.common.kafkastream"
})
```

画面 9：
```java
public void sendArticlePlus(UpdateArticleMessage message, Long userId, boolean isSendArticle) {
    UpdateArticleMessage temp = parseMessage(message, userId, isSendArticle);
    kafkaSender.sendArticlePlus(temp);
}
```

画面 10：
```java
@Test
public void testLikesSave() {
    AppUser user = new AppUser();
    user.setId(1L);
    LikesBehaviorDTO dto = new LikesBehaviorDTO();
    dto.setArticleId(10120);
    dto.setOperation((short) 1);
    dto.setType((short) 1);
    applikesBehaviorService.saveLikesBehavior(dto);
}
```

画面 11：
```java
public KStream<?, String> getService(KStream<?, String> stream) {
    return stream.map((key, val) -> {
        UpdateArticleMessage value = format(val);
        System.out.println(value);
        return new KeyValue<>("", "");
    });
}
```

画面 12：
```java
public KStream<?, String> getService(KStream<?, String> stream) {
    return stream.map((key, val) -> {
        UpdateArticleMessage value = format(val);
        System.out.println(value);
        return new KeyValue<>("", "");
    });
}
```

画面 13：
```java
public KStream<?, String> getService(KStream<?, String> stream) {
    return stream.map((key, val) -> {
        UpdateArticleMessage value = format(val);
        System.out.println(value);
        return new KeyValue<>("", "");
    });
}
```

画面 14：
```java
public KStream<?, String> getService(KStream<?, String> stream) {
    return stream.map((key, val) -> {
        UpdateArticleMessage value = format(val);
        System.out.println(value);
        return new KeyValue<>("", "");
    });
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

