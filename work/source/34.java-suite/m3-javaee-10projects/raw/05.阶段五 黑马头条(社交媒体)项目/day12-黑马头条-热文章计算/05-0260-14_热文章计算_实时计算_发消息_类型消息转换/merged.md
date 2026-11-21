# 14_热文章计算_实时计算_发消息_类型消息转换

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\14_热文章计算_实时计算_发消息_类型消息转换【海量资源尽在 666java.com】.mp4
- 时长 7分59秒（音频 479s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就来去把当前解析的方法给去设置一下这个方法其实已经很明显了刚才咱们是把当前的什么比如说点赞然后阅读的消息已经发送了其实消息发送完之后其实就是发送这条消息
[00:16] 那这个内容啊那这个内容呢里边呢其实就是个message呢就是它根据不同的业务去设置的比如说你在里边有什么点赞也有阅读是吧你最终呢要把这个message呢去转换成一个叫做update article message就可以了好吧这个呢其实就是它转换的一个方法啊内容那里边其实还有个材数啊就是当前那个is sent to article到底是否需要去发送到文章是吧在目前的话呢其实都是文章啊
[00:45] 咱们为了后期的扩展方面所以说加了这么个参数啊目前的话呢你可以这么去轰转一下啊如果说他是出来默认现在给的都是出啊然后呢你再让他去处理这个消息就可以了啊上面这个是一样啊if is sent to article然后呢就可以去处理这个消息了那重点呢咱们还是要去说一下前这个消息啊
[01:14] 他说了就是通过当前这个message要转换为谁呢转换为update article message但这个呢只是一个消息的包装类啊他最终消息的存储存到了当前的update article这里边是有这么多啊第一个是当前的type到底是什么收藏的还是评论的还是当前的点赞还是你的阅读是吧还有什么文章ID还有你的征服值刚才也说了啊还有你的
[01:43] 用户ID还有你的行为实体ID是吧那好那咱们下面就来去设置一下刚才说了其实就是updateArticle其实它最终要去封装一些消息是吧那就先去new出来然后呢咱们就可以去设置ua.setUserID这个userID其实就是它我们可以直接装进去就可以了然而你最好呢是在这去判断一下点interval怎么判断呢
[02:14] 不说呀AP user ID不等于None这时候呢咱们再去往里边去设置然后下面呢咱们就可以去换换啥呢message换成他其实呢就是从这里边去拿数据啊最终是往里边去设置数据就可以了好判断一下呗message啊然后是instance然后是谁呢如果说他是当前的AP likeuser吗
[02:48] 我看 user like message如果说是当前这个message的话呢我们就可以去强转一下啊user like我们叫like message吧好吧等于等于message好这时候强转一下强转完之后呢你这时候呢你就可以干嘛呢你就可以去设置值了啊设置值之前呢就是uadrset一个叫做type这个type是谁呢
[03:17] type的话就是当前的update article.at然后里边是有一个叫做likelikes就是当前的赞的类型ua.set一个叫什么来着这个add其实就是stype就是你刚才传过来这个尼或者是富尼是吧好 接着往下看ua.set一个叫什么来着article id
[03:46] 这个ID是有点问题的点get date里面呢你看里面有没有get article ID呢没有谁呢这个intro ID其实就是这样就是当前的文章ID这个要注意一下这个点赞这块这个资料说的有点问题所以说咱们这块是intro ID是当前的article ID好这是一个ua.set一个叫做cover ID这个其实就是这样lags message
[04:16] at, get, r, 当前的 behavior, actually其实这个呢是行为实体, 这不是set, 是get那这样的话咱们就设置完了啊设置完之后啊这里边就还有一些需要注意的事项吗?
[04:36] 就是咱们在这需要去做一个判断当时啊咱们这个点赞呢有很多种方式比如说你的是文章的点赞
[04:45] 还是转发的点赞还是说其他类型的点赞所以说咱们在这需要去加一个判断咱们现在只处理文章的点赞只处理文章数据的点赞那这个怎么办呢其实就是用前的一个叫做谁呢back message.cat type然后是等于谁等于当前的AP
[05:18] 里边有一个叫lagslags.type.article必须是article的code那这时候呢它呢是啥呢就是当前的什么当前的这种文章类的信息文章类的信息那这块有问题吗我看看啊这不是这个啊这应该是少写点东西啊get date.get date然后是再点
[05:49] 那这个咱们就设置完了啊那这个是点赞的这一块那下面这个就容易了啊如果说呀message instance of等于谁呀等于当前的user read message这时候呢你可以再次去强转user read message好等于new一个不是new啊是message你需要去强转
[06:22] 参照完之后呢你还是往UA里面去设置比如set一个叫做type这个呢其实还是update article.r然后是有一个类型然后是有一个viewviews其实呢就是当前的阅读然后是UA.set一个叫做type这就是还是当前的step然后下面还有什么呢UA.set article.id那这个呢要注意啊这个里面呢其实它是有
[06:51] 当前的article id的加2get article id你看它是有的是吧好然后下面还有一个啊是当前的行为实体idset然后是有一个recover id然后还是user readmessage.get date加2一个叫做entry id这个就是行为实体好吧最终呢这两个消息啊咱们就算是弄的完了最终呢你要去返回啊返回之前呢你最好是做一个判断啊
[07:20] 那上的 ua.getArticle 它不能等于none如果说等于none的话呢那咱们就直接干嘛呢给更多的none就可以了不让它发消息如果它不等于none那时候咱们就可以去new一个当前的combo.datArticleMessage然后里边装的谁呀装的就是ua那这样的话呢我们就算是说完了
[07:50] 这个方法咱们也解析完了那关于行为这一块其实呢咱们已经都做完了下面该去接收消息了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 IDEA 中编写并调试一个用于处理用户行为消息（点赞、阅读）并发送到 Kafka 的 Java 服务端代码，核心是解析消息并构造 UpdateArticleMessage 对象。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 BehaviorMessageSender.java 文件中 sendMessageReduce 方法的开头部分，定义了参数 message、apUserId、isSendToArticle，并调用 parseMessage 方法。
画面 2: 代码光标在 sendMessageReduce 方法中，显示了 if (isSendToArticle) 判断语句和后续的 parseMessage 调用。
画面 3: 光标在 parseMessage 方法内部，IDE 显示了 UpdateArticleMessage 类的自动补全建议列表。
画面 4: 光标在 parseMessage 方法中，创建了 UpdateArticle 对象 ua，并调用 ua.setUserId 方法设置用户 ID。
画面 5: 光标在 ua.setUserId 语句后，IDE 显示了可用的 set 方法补全建议，包括 setArticleId、setType 等。
画面 6: 光标在 ua.setUserId 语句后，IDE 显示了可用的 set 方法补全建议，包括 setArticleId、setType 等。
画面 7: 光标在 ua.setUserId 语句后，IDE 显示了可用的 set 方法补全建议，包括 setArticleId、setType 等。
画面 8: 光标在 parseMessage 方法中，添加了对 UserLikeMessage 的判断语句。
画面 9: 光标在 parseMessage 方法中，添加了对 UserLikeMessage 的判断语句，并设置了 ua.setType(UpdateArticleType.LIKES)。
画面 10: 光标在 parseMessage 方法中，添加了对 UserReadMessage 的判断语句。
画面 11: 光标在 parseMessage 方法中，为 UserReadMessage 设置了 ua.setType(UpdateArticleType.VIEWS)。
画面 12: 光标在 parseMessage 方法中，为 UserReadMessage 设置了 ua.setArticleId 方法。
画面 13: 光标在 parseMessage 方法中，IDE 显示了 UpdateArticleMessage 类的自动补全建议列表。
画面 14: 光标在 parseMessage 方法中，显示了对 UserLikeMessage 的判断语句和设置 ua.setType(UpdateArticleType.LIKES) 的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public void sendMessageReduce(KafkaMessage message, Long apUserId, boolean isSendToArticle) {
    UpdateArticleMessage temp = parseMessage(message, apUserId, step - 1);
    kafkaSender.sendArticleUpdateBus(temp);
}
```

画面 4:
```java
private UpdateArticleMessage parseMessage(KafkaMessage message, Long apUserId, int step) {
    UpdateArticle ua = new UpdateArticle();
    if (apUserId != null) {
        ua.setUserId(apUserId.intValue());
    }
}
```

画面 8:
```java
private UpdateArticleMessage parseMessage(KafkaMessage message, Long apUserId, int step) {
    UpdateArticle ua = new UpdateArticle();
    if (apUserId != null) {
        ua.setUserId(apUserId.intValue());
    }
    if (message instanceof UserLikeMessage) {
        UserLikeMessage likedMessage = (UserLikeMessage) message;
        if (likedMessage.getData().getButtonType() == AppliedBehavior.Type.ARTICLE.getCode()) {
            ua.setType(UpdateArticleType.LIKES);
            ua.setArticleId(likedMessage.getData().getEntryId());
            ua.setBehaviorId(likedMessage.getData().getBehaviorEntryId());
        }
    }
}
```

画面 10:
```java
private UpdateArticleMessage parseMessage(KafkaMessage message, Long apUserId, int step) {
    UpdateArticle ua = new UpdateArticle();
    if (apUserId != null) {
        ua.setUserId(apUserId.intValue());
    }
    if (message instanceof UserLikeMessage) {
        UserLikeMessage likedMessage = (UserLikeMessage) message;
        if (likedMessage.getData().getButtonType() == AppliedBehavior.Type.ARTICLE.getCode()) {
            ua.setType(UpdateArticleType.LIKES);
            ua.setArticleId(likedMessage.getData().getEntryId());
            ua.setBehaviorId(likedMessage.getData().getBehaviorEntryId());
        }
    } else if (message instanceof UserReadMessage) {
        UserReadMessage userReadMessage = (UserReadMessage) message;
        ua.setType(UpdateArticleType.VIEWS);
        ua.setArticleId(userReadMessage.getData().getArticleId());
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

