# 画面线理解：14_热文章计算_实时计算_发消息_类型消息转换

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\14_热文章计算_实时计算_发消息_类型消息转换【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 01:09, 01:52, 02:18, 03:13, 03:35, 04:11, 04:42, 05:50, 06:18, 06:35, 06:57, 07:21, 07:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:40:42

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
