# 画面线理解：18.小视频推荐之接收消息

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\18.小视频推荐之接收消息_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:47, 01:18, 02:04, 02:30, 02:59, 03:24, 04:00, 04:38, 05:05, 05:26, 06:12, 06:37, 07:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:03:52

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 RocketMQ 消息队列接收视频点赞、收藏、评论等行为消息，并将这些消息持久化到 MongoDB 数据库中。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程大纲，当前章节为“4.4 接收消息”，并显示了 `RecommendVideo` 实体类的代码，包含 `id`、`userId`、`videoId`、`score`、`date` 字段。
画面2：展示 `VideoMsgConsumer` 类的代码，定义了 RocketMQ 消息监听器，监听主题为 "tanhua-video"，并导入了相关依赖。
画面3：展示 `VideoMsgConsumer` 类的完整代码，包含 `@Component`、`@RocketMQMessageListener` 注解，以及 `onMessage` 方法中使用 `ObjectMapper` 解析 JSON 消息。
画面4：展示 `onMessage` 方法中解析用户 ID、视频 ID 和类型，并创建 `RecommendVideo` 对象，根据类型设置分数。
画面5：展示 `switch` 语句中不同类型的分数设置逻辑，以及将 `RecommendVideo` 对象保存到 MongoDB 的代码。
画面6：展示调试界面，显示应用正在运行。
画面7：展示 `VideoController` 中的 `@PostMapping("/id/like")` 方法，用于处理点赞请求。
画面8：展示 `VideoController` 中的 `saveVideo` 方法，调用 `videoMQService.videoMsg(id)` 发送消息。
画面9：展示 `VideoMsgConsumer` 的 `onMessage` 方法中解析 JSON 消息并创建 `RecommendVideo` 对象的代码。
画面10：展示 `VideoMsgConsumer` 的 `onMessage` 方法中设置分数和保存到 MongoDB 的代码。
画面11：展示 `VideoController` 中的 `saveVideo` 方法，调用 `videoMQService.videoMsg(id)` 发送消息。
画面12：展示使用 Advanced REST Client 发送 POST 请求，请求地址为 http://127.0.0.1:8080/videos。
画面13：展示 MongoDB 中的 `recommend_video_20191007` 集合，其中包含一条记录，字段包括 `id`、`videoId`、`score`、`date`。
画面14：展示课程大纲，当前章节为“4.5 构造数据”，并显示了 `TestVideoApi` 测试类的代码，用于构造测试数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
package com.tanhua.recommend.pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.bson.types.ObjectId;
@Data
@NoArgsConstructor
@AllArgsConstructor
public class RecommendVideo {
    private ObjectId id;
    private Long userId; // 用户id
    private Long videoId; // 视频id，需要转化为Long类型
    private Double score; // 分数
    private Long date; // 时间戳
}
```

画面2：
```java
package com.tanhua.recommend.msg;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.tanhua.recommend.pojo.Publish;
import com.tanhua.recommend.pojo.RecommendVideo;
import org.apache.commons.lang3.StringUtils;
import org.apache.rocketmq.spring.annotation.RocketMQMessageListener;
import org.apache.rocketmq.spring.core.RocketMQListener;
import org.bson.types.ObjectId;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.stereotype.Component;
@Component
@RocketMQMessageListener(topic = "tanhua-video",
        consumerGroup = "tanhua-video-consumer")
public class VideoMsgConsumer implements RocketMQListener<String> {
```

画面3：
```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.stereotype.Component;
@Component
@RocketMQMessageListener(topic = "tanhua-video",
        consumerGroup = "tanhua-video-consumer")
public class VideoMsgConsumer implements RocketMQListener<String> {
    private static final ObjectMapper MAPPER = new ObjectMapper();
    private static final Logger LOGGER = LoggerFactory.getLogger(VideoMsgConsumer.class);
    @Autowired
    private MongoTemplate mongoTemplate;
    @Override
    public void onMessage(String msg) {
        try {
            JsonNode jsonNode = MAPPER.readTree(msg);
```

画面4：
```java
Long userId = jsonNode.get("userId").asLong();
Long vid = jsonNode.get("vid").asLong();
Integer type = jsonNode.get("type").asInt();
//1-发动态，2-点赞，3-取消点赞，4-评论
RecommendVideo recommendVideo = new RecommendVideo();
recommendVideo.setUserId(userId);
recommendVideo.setVideoId(vid);
recommendVideo.setDate(System.currentTimeMillis());
switch (type) {
    case 1: {
        recommendVideo.setScore(2d);
        break;
    }
    case 2: {
        recommendVideo.setScore(5d);
        break;
    }
```

画面5：
```java
case 3: {
    recommendVideo.setScore(-5d);
    break;
}
case 4: {
    recommendVideo.setScore(10d);
    break;
}
default: {
    recommendVideo.setScore(0d);
    break;
}
}
String collectionName = "recommend_video" + new DateTime().toString("yyyyMMdd");
this.mongoTemplate.save(recommendVideo, collectionName);
```

画面7：
```java
@PostMapping("/id/like")
public ResponseEntity<Long> likeComment(@PathVariable("id") String videoId) {
    ResponseEntity<Long> entity = this.movementsController.likeComment(videoId);
    if (entity.getStatusCode() != HttpStatus.OK) {
        return entity;
    }
    return ResponseEntity.ok(null);
}
```

画面8：
```java
@Autowired
private VideoMQService videoMQService;
@PostMapping(value = "videoThumb")
public ResponseEntity<Void> saveVideo(@RequestParam(value = "videoThumb") MultipartFile picFile,
                                      @RequestParam(value = "videoFile") MultipartFile videoFile) {
    try {
        String id = this.videoService.saveVideo(picFile, videoFile);
        if (StringUtils.isNotEmpty(id)) {
            //发送消息
            this.videoMQService.videoMsg(id);
            return ResponseEntity.ok(null);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面14：
```java
package com.tanhua.server.api;
import com.tanhua.dubbo.server.pojo.Video;
import org.apache.commons.lang3.RandomUtils;
import org.bson.types.ObjectId;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest
public class TestVideoApi {
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
