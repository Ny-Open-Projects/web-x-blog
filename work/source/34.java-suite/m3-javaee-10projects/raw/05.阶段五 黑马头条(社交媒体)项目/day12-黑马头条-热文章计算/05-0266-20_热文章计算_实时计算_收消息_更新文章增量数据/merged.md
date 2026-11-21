# 20_热文章计算_实时计算_收消息_更新文章增量数据

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\20_热文章计算_实时计算_收消息_更新文章增量数据【海量资源尽在 666java.com】.mp4
- 时长 8分41秒（音频 522s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就继续往下讲啊刚才呢咱们是已经把当前那个监听啊这个流的监听啊咱们已经设置完了那设置完之后的效果呢其实就是咱们要去还要再去发一条消息这个消息呢其实就是谁啊其实就是这个是吧他就会发到这发到这之后呢我要去更新数据那这个数据是谁呢这个数据就是AP article这里边咱们要去更新哪个呢你可以看一下啊打开
[00:28] 其实就是更新某一条文章的什么呢当前的什么like,collection,command,viewOK就是更新这四项那行那咱们下面就来去设置一下那首先咱们还是要从mypl开始还是要在这在这个当前ap article mypl中去添加一个方法就是更新的方法我们可以考过来考到当前哪个呀ap article myplOK就它啊
[00:57] 好现在去把这个方法加上方法你可以看一下啊就是根据当前的article id去更新这四项当然这有多个参数咱们需要去用一个什么一个解去区分一下是吧这是什么article id好这个拷贝一下好都拷贝一下啊这一共是四项啊一共是五个啊好替换一下这个也替换还有最后一个
[01:34] 那这样替换完了啊替换完之后呢这时候呢你需要去写它的Map文件啊这时候呢咱们直接从当前的笔记中考一下之后呢这东西啊咱们就来看一下首先呢咱们这个更新的时候呢是更新的AP article并且呢根据主件去更新那这些是什么意思呢来看一下啊先看这里边的啊先看这里边的这什么意思啊说如果说搭呢
[02:02] v4是none的话呢就把它转换成0然后呢是加上你的参数加上你的参数啊然后这个还有一个函数叫grist那这是什么意思呢你看这里边是有两个值一个哎两个它呢是取出一个最大值比如说啊你加完之后是10那这个值呢是11那它呢就会取当前这个11这个值呢去哎给它复值好吧就取出一个最大值啊下面这个套路都是一样的
[02:31] 好吧那行那这个咱们就说完了说完之后下面咱们还要再去定义什么呢定义当的Service这Service就是还是AP article Service好吧来咱们下面就来去设置一下在哪呢在当前的AP article找一找在这去创建不是创建应该是之前是有的叫APP article Service在这去加一个方法
[03:05] 这个方法呢就是什么呢叫response without咱们还是返回这个东西然后呢咱们叫一个方法叫appleticreview咱们可以随便设置一个啊然后这里边呢咱们可以去找一个参数articlemasterstrivedto因为这里边包括了刚才咱们说的那五项啊第一个呢咱们就在这更新
[03:38] 阅读书其实呢这个叫啥都无所谓啊咱们这个其实最终更新的呢其实不仅仅是阅读是吧那阅读啊还有什么点赞主要是设置两项吧好吧那行那这个设置完之后啊那咱们下面呢就来去写它的实现类这时候他会需要去重写当前这个方法方法该怎么去写呢那这个方法就比较比较容易了啊咱们可以直接去设置值比如说AP article
[04:09] myport.uploaditmew那第一个是呢就是dto的get article id那第二个呢是dto的get那个mew可以看一下啊当前这个不行这个不是view是吧就是view啊第三个呢第三个是收藏是吧写一下收藏和
[04:39] 评论最后是点赞收藏写DTO.getLex好DTO.getBond最后一个DTO.get一个叫做Lex好吧那这样的话咱们就算是设置完了啊那设置完之后那这东西最终是不是他需要一个response你怎么办呢这样咱们可以在这去返回一个什么呢
[05:11] 返回一个intruth返回一个这种影响的函数然后最终你在这去response withoutr e s p o s eresult假如有一个og result然后是把当前的ruth放进去就可以了当然这里边还去加了一个日志咱们可以去加上这个日志不加也行是吧我看看行吗那就不加了好吧行这样的话咱们就算是设置完了设置完之后是不是还没有完呢
[05:43] 你要干嘛呢你是不是得需要去在当前的这一块去接收当前这个消息好那去接收的话在这时候咱们需要去把这个Service给注入进来然后是app article Service后到你接收的消息咱们还需要去转换一下所以说咱们需要再去这个json这个adjson这去转换去拿到怎么拿就是private objectobject map
[06:19] 好把他也给注入进来好那这个拿到之后呢这时候呢你就可以去往里边去设置了啊我们也可以去接收消息了消息的话是怎样我们可以在这去加一个东西loginfo是接收到的接收到的消息为这个呢其实就是当前的这个data其实没有啊错了啊这个data呢其实就是他那的话咱们就把这个值给拿到了然后呢然后怎么办呢
[06:58] 然后咱们要去读当前这个值来没有mypro点有一个叫做read value然后呢你把当前那个data放进去然后第二个呢咱们是有一个articlerestartmessage他啊下面的好吧pass啊点万没有返回是吗我看看啊应该返回的是谁啊返回的就是当前那个article
[07:36] 好这是就是message这个是有问题吗我看看啊哦对错了啊那这个呢咱们这样啊date.有一个value这个value呢其实咱们在最终是拿到的一个值是一个值啊行这个value呢你直接去放到这就可以了啊不是date好这样的话咱们需要去try cache一下拿到之后呢这时候你再去干嘛呢再去拿到
[08:09] message中的什么dat有一个date这个dat呢其实就是一个目前的dto拿到这个dto之后呢你再去调用Service里边的方法就可以了呗点有一个update把dto装进去那这样的话就算是结束了在这儿你也可以去打印句话是吧你说有什么错误啊咱们就不打印了啊行那这个咱们就算是做完了啊
[08:38] 一会儿咱们再来去综合测试一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Kafka 消息驱动，结合 Spring Boot 和 MyBatis，实现文章浏览量、点赞数等数据的实时增量更新。

2) 按时间顺序列出每张画面的要点：
画面1：展示 ArticleIncrHandleListener 类，其中注入了 KafkaTopicConfig，并定义了 onMessage 方法，用于处理 Kafka 消息。
画面2：展示 HotArticleStreamHandler 类，其中定义了 sendTopic 和 getStream 方法，用于处理流式数据。
画面3：在 IDEA 中使用全局搜索功能，查找与 ArticleIncrHandleListener 相关的类和文件。
画面4：在 Typora 中查看文档，内容为“3.2.5 更新文章增量数据”，并展示 ApArticleMapper.xml 中的 updateArticleView SQL 语句。
画面5：在 Typora 中查看文档，内容为“3.2.5 更新文章增量数据”，并展示 AppArticleService 接口和实现类中的 updateArticleView 方法。
画面6：在 IDEA 中查看项目结构，定位到 AppArticleService 接口。
画面7：在 IDEA 中查看 AppArticleServiceImpl 类，展示其构造函数和成员变量。
画面8：在 IDEA 中查看 AppArticleServiceImpl 类，展示 updateArticleView 方法的实现。
画面9：在 IDEA 中查看 AppArticleServiceImpl 类，展示 updateArticleView 方法的实现，其中调用 aparticleMapper.updateArticleView。
画面10：在 IDEA 中查看 ArticleIncrHandleListener 类，展示其构造函数和成员变量。
画面11：在 IDEA 中查看 ArticleIncrHandleListener 类，展示其构造函数和成员变量。
画面12：在 IDEA 中查看 ArticleIncrHandleListener 类，展示其构造函数和成员变量。
画面13：在 IDEA 中查看 ArticleIncrHandleListener 类，展示其构造函数和成员变量。
画面14：在 IDEA 中查看 ArticleIncrHandleListener 类，展示其 onMessage 方法的完整实现，包括日志记录、消息解析和调用服务层方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Component
@Slf4j
public class ArticleIncrHandleListener implements KafkaListener<String, String> {
    @Autowired
    private KafkaTopicConfig kafkaTopicConfig;

    @Override
    public String topic() {
        return kafkaTopicConfig.getArticleIncrHandle();
    }

    @Override
    public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {

    }
}
```

画面2：
```java
@Mutated
private KafkaTopicConfig kafkaTopicConfig;
private ObjectMapper Mapper;

@Override
public String listenerTopic() {
    return kafkaTopicConfig.getArticleIncrHandle();
}

@Override
public String sendTopic() {
    return kafkaTopicConfig.getArticleIncrHandle();
}

@Override
public Stream<String> getStream(String stream) {
    return stream.map((key, val) -> {
        UpdatedArticleMessage value = Format(val);
        System.out.println(value);
        return value;
    });
}
```

画面4：
```xml
<update id="updateArticleView">
    UPDATE ap_article SET
    views = GREATEST(IFNULL(views,0) + #{viewCount}, #{viewCount}),
    collection = GREATEST(IFNULL(collection,0) + #{collectCount}, #{collectCount}),
    comment = GREATEST(IFNULL(comment,0) + #{commentCount}, #{commentCount}),
    likes = GREATEST(IFNULL(likes,0) + #{likeCount}, #{likeCount})
    WHERE id = #{articleId}
</update>
```

画面5：
```java
ResponseResult updateArticleView(ArticleVisitStreamDto dto);
```

画面6：
```java
package com.heima.article.Service;

import com.heima.article.dto.ArticleVisitStreamDto;
import com.heima.article.dto.ArticleVisitStreamDto;
import com.heima.article.dto.ArticleVisitStreamDto;

public interface AppArticleService {
    ResponseResult load(ArticleVisitStreamDto dto, Short type);
}
```

画面7：
```java
@Autowired
private ApArticleMapper aparticleMapper;
```

画面8：
```java
@Override
public ResponseResult updateArticleView(ArticleVisitStreamDto dto) {
    aparticleMapper.updateArticleView(dto.getArticleId(), dto.getView(), dto.getCollect(), dto.getComment(), dto.getLike());
    return null;
}
```

画面9：
```java
@Override
public ResponseResult updateArticleView(ArticleVisitStreamDto dto) {
    int rows = aparticleMapper.updateArticleView(dto.getArticleId(), dto.getView(), dto.getCollect(), dto.getComment(), dto.getLike());
    return ResponseResult.okResult(rows);
}
```

画面10：
```java
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
```

画面11：
```java
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
```

画面12：
```java
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
```

画面13：
```java
@Autowired
private KafkaTopicConfig kafkaTopicConfig;
```

画面14：
```java
@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    log.info("接收到的消息为：{}", data);
    ArticleVisitStreamMessage message = Mapper.readValue(data, ArticleVisitStreamMessage.class);
    ArticleVisitStreamDto dto = message.getData();
    appArticleService.updateArticleView(dto);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4：PPT标题为“3.2.5 更新文章增量数据”，内容包括“（1）Mapper定义”和“（2）Service定义”。
画面5：PPT标题为“3.2.5 更新文章增量数据”，内容包括“（2）Service定义”。
画面6：无PPT内容。
画面7：无PPT内容。
画面8：无PPT内容。
画面9：无PPT内容。
画面10：无PPT内容。
画面11：无PPT内容。
画面12：无PPT内容。
画面13：无PPT内容。
画面14：无PPT内容。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。

