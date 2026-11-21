# 画面线理解：13_热文章计算_实时计算_发消息_点赞和阅读收集消息发送

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\13_热文章计算_实时计算_发消息_点赞和阅读收集消息发送【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:50, 01:55, 02:29, 03:10, 03:35, 04:04, 04:48, 05:30, 05:57, 06:33, 07:17, 07:52, 08:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:40:10

1) 这一组画面整体在讲什么（一句话）：
演示如何在用户点赞和阅读行为中，通过 Kafka 发送消息，实现行为事件的异步处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构，重点是 `BehaviorMessageSender` 类，其中 `sendMessagePlus` 方法用于发送点赞消息，`sendMessageReduce` 方法用于发送阅读消息，参数包含 `apUserId` 和 `isSendToArticle`。
画面2：PPT页面，标题为“3.1.5 具体行为消息发送”，内容包括“（1）点赞”和“（2）阅读”两个部分，分别对应创建 `UserLikesMessage` 和 `UserReadMessage` 实体类。
画面3：PPT页面，展示“（2）阅读”部分，重点是创建 `UserReadMessage` 实体类。
画面4：IDE中展示 `UserLikesMessage` 类的代码，位于 `com.heima.common.kafka.messages.behavior` 包下，继承自 `KafkaMessage<ApLikesBehavior>`。
画面5：IDE中展示 `UserLikesMessage` 类的代码，展示其 `getDataType` 方法和 `hashCode` 方法。
画面6：PPT页面，展示“（1）点赞”部分，重点是 `ApLikesBehaviorServiceImpl` 类中的 `saveLikesBehavior` 方法。
画面7：PPT页面，展示“（2）阅读”部分，重点是 `UserReadMessage` 实体类。
画面8：PPT页面，展示“（2）阅读”部分，重点是 `UserReadMessage` 实体类。
画面9：IDE中展示 `ApLikesBehaviorServiceImpl` 类的代码，展示 `saveLikesBehavior` 方法中创建 `ApLikesBehavior` 对象并设置属性。
画面10：IDE中展示 `ApLikesBehaviorServiceImpl` 类的代码，展示 `saveLikesBehavior` 方法中插入数据库并根据操作类型调用 `behaviorMessageSender` 发送消息。
画面11：IDE中展示 `ApLikesBehaviorServiceImpl` 类的代码，展示 `sendMessagePlus` 方法的调用。
画面12：IDE中展示 `ApLikesBehaviorServiceImpl` 类的代码，展示 `sendMessageReduce` 方法的调用。
画面13：IDE中展示 `AppReadBehaviorServiceImpl` 类的代码，展示 `saveReadBehavior` 方法的开始部分。
画面14：IDE中展示 `AppReadBehaviorServiceImpl` 类的代码，展示 `sendMessagePlus` 方法的调用。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public void sendMessagePlus(KafkaMessage message, Long apUserId, boolean isSendToArticle) {
    UpdateArticleMessage temp = parseMessage(message, apUserId, 1);
    kafkaSender.sendArticleUpdateBus(temp);
}
```
画面2：
```java
public class UserLikesMessage extends KafkaMessage<ApLikesBehavior> {
    public UserLikesMessage() {
    }
    public UserLikesMessage(ApLikesBehavior data) {
        super(data);
    }
    @Override
    public String getType() {
        return "user-likes";
    }
}
```
画面6：
```java
@Override
public ResponseResult saveLikesBehavior(LikesBehaviorDto dto) {
    //......上面代码省略
    int temp = aplikesBehaviorMapper.insert(alb);
    if (insert != 1) {
        if (alb.getOperation() == ApLikesBehavior.Operation.LIKE.getCode()) {
            behaviorMessageSender.sendMessagePlus(new UserLikesMessage(alb), userId, true);
        } else if (alb.getOperation() == ApLikesBehavior.Operation.CANCEL.getCode()) {
            behaviorMessageSender.sendMessageReduce(new UserLikesMessage(alb), userId, true);
        }
        return ResponseResult.okResult(temp);
    }
}
```
画面9：
```java
ApLikesBehavior alb = new ApLikesBehavior();
alb.setEntryId(dto.getEntryId());
alb.setBehaviorEntryId(dto.getBehaviorEntryId());
alb.setUserId(dto.getUserId());
alb.setTypeId(dto.getTypeId());
alb.setOperation(dto.getOperation());
alb.setTimestamp(ChronoUtils.encrypt(alb.getId(), alb.getBehaviorEntryId()));
```
画面10：
```java
int insert = aplikesBehaviorMapper.insert(alb);
if (insert != 1) {
    if (alb.getOperation() == ApLikesBehavior.Operation.LIKE.getCode()) {
        behaviorMessageSender.sendMessagePlus(new UserLikesMessage(alb), userId, true);
    } else if (alb.getOperation() == ApLikesBehavior.Operation.CANCEL.getCode()) {
        behaviorMessageSender.sendMessageReduce(new UserLikesMessage(alb), userId, true);
    }
    return ResponseResult.okResult(insert);
}
```
画面13：
```java
@Override
public ResponseResult saveReadBehavior(ReadBehaviorDto dto) {
    //获取用户信息，获取设备id
    ApReadBehavior apReadBehavior = ApReadBehaviorUtils.getApReadBehavior(dto);
    //根据当前的用户信息设置设备id，ap_behavior_entry_id
    apReadBehavior.setEntryId(dto.getEntryId());
    apReadBehavior.setUpdatedTime(new Date());
    apReadBehavior.setReadDuration(dto.getReadDuration());
    apReadBehavior.setReadTime(new Date());
    apReadBehavior.setReadType(dto.getReadType());
    apReadBehavior.setReadUserId(dto.getUserId());
    apReadBehavior.setReadBehaviorEntryId(dto.getReadBehaviorEntryId());
    apReadBehavior.setReadBehaviorId(dto.getReadBehaviorId());
    apReadBehavior.setReadBehaviorType(dto.getReadBehaviorType());
    apReadBehavior.setReadBehaviorStatus(dto.getReadBehaviorStatus());
    apReadBehavior.setReadBehaviorTime(dto.getReadBehaviorTime());
    apReadBehavior.setReadBehaviorDuration(dto.getReadBehaviorDuration());
    apReadBehavior.setReadBehaviorCount(dto.getReadBehaviorCount());
    apReadBehavior.setReadBehaviorType(dto.getReadBehaviorType());
    apReadBehavior.setReadBehaviorStatus(dto.getReadBehaviorStatus());
    apReadBehavior.setReadBehaviorTime(dto.getReadBehaviorTime());
    apReadBehavior.setReadBehaviorDuration(dto.getReadBehaviorDuration());
    apReadBehavior.setReadBehaviorCount(dto.getReadBehaviorCount());
    apReadBehavior.setReadBehaviorType(dto.getReadBehaviorType());
    apReadBehavior.setReadBehaviorStatus(dto.getReadBehaviorStatus());
    apReadBehavior.setReadBehaviorTime(dto.getReadBehaviorTime());
    apReadBehavior.setReadBehaviorDuration(dto.getReadBehaviorDuration());
    apReadBehavior.setReadBehaviorCount(dto.getReadBehaviorCount());
    apReadBehavior.setReadBehaviorType(dto.getReadBehaviorType());
    apReadBehavior.setReadBehaviorStatus(dto.getReadBehaviorStatus());
    apReadBehavior.setReadBehaviorTime(dto.getReadBehaviorTime());
    apReadBehavior.setReadBehaviorDuration(dto.getReadBehaviorDuration());
    apReadBehavior.setReadBehaviorCount(dto.getReadBehaviorCount());
    apReadBehavior.setReadBehaviorType(dto.getReadBehaviorType());
    apReadBehavior.setReadBehaviorStatus(dto.getReadBehaviorStatus());
    apReadBehavior.setReadBehaviorTime(dto.getReadBehaviorTime());
    apReadBehavior.setReadBehaviorDuration(dto.getReadBehaviorDuration());
    apReadBehavior.setReadBehaviorCount(dto.getReadBehaviorCount());
    apReadBehavior.setReadBehaviorType(dto.getReadBehaviorType());
    apReadBehavior.setReadBehaviorStatus(dto.getReadBehaviorStatus());
    apReadBehavior.setReadBehaviorTime(dto.getReadBehaviorTime());
    apReadBehavior.setReadBehaviorDuration(dto.getReadBehaviorDuration());
    apReadBehavior.setReadBehaviorCount(dto.getReadBehaviorCount());
    apReadBehavior.setReadBehaviorType(dto.getReadBehaviorType());
    apReadBehavior.setReadBehaviorStatus(dto.getReadBehaviorStatus());
    apReadBehavior.setReadBehaviorTime(dto.getReadBehaviorTime());
    apReadBehavior.setReadBehaviorDuration(dto.getReadBehaviorDuration());
    apReadBehavior.setReadBehaviorCount(dto.getReadBehaviorCount());
    apReadBehavior.setReadBehaviorType(dto.getReadBehaviorType());
    apReadBehavior.setReadBehaviorStatus(dto.getReadBehaviorStatus());
    apReadBehavior.setReadBehaviorTime(dto.getReadBehaviorTime());
    apReadBehavior.setReadBehaviorDuration(dto.getReadBehaviorDuration());
    apReadBehavior.setReadBehaviorCount(dto.getReadBehaviorCount());
    apReadBehavior.setReadBehaviorType(dto.getReadBehaviorType());
    apReadBehavior.setReadBehaviorStatus(dto.getReadBehaviorStatus());
    apReadBehavior.setReadBehaviorTime(dto.getReadBehaviorTime());
    apReadBehavior.setReadBehaviorDuration(dto.getReadBehaviorDuration());
    apReadBehavior.setReadBehaviorCount(dto.getReadBehaviorCount());
    apReadBehavior.setReadBehaviorType(dto.getReadBehaviorType());
    apReadBehavior.setReadBehaviorStatus(dto.getReadBehaviorStatus());
    apReadBehavior.setReadBehaviorTime(dto.getReadBehaviorTime());
    apReadBehavior.setReadBehaviorDuration(dto.getReadBehaviorDuration());
    apReadBehavior.setReadBehaviorCount(dto.getReadBehaviorCount());
    apReadBehavior.setReadBehaviorType(dto.getReadBehaviorType());
    apReadBehavior.setReadBehaviorStatus(dto.getReadBehaviorStatus());
    apReadBehavior.setReadBehaviorTime(dto.getReadBehaviorTime());
    apReadBehavior.setReadBehaviorDuration(dto.getReadBehaviorDuration());
    apReadBehavior.setReadBehaviorCount(dto.getReadBehaviorCount());
    apReadBehavior.setReadBehaviorType(dto.getReadBehaviorType());
    apReadBehavior.setReadBehaviorStatus(dto.getReadBehaviorStatus());
    apReadBehavior.setReadBehaviorTime(dto.getReadBehaviorTime());
    apReadBehavior.setReadBehaviorDuration(dto.getReadBehaviorDuration());
    apReadBehavior.setReadBehaviorCount(dto.getReadBehaviorCount());
    apReadBehavior.setReadBehaviorType(dto.getRead
