# 18.小视频推荐之接收消息

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\18.小视频推荐之接收消息_【海量资源尽在 666java.com】.mp4
- 时长 7分35秒（音频 455s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下接收消息那么前面呢我们已经完成了我们这个小视频的一些相关的消息的发送那么下面我们来看一下接收那么首先呢我们需要定义一个对象叫做RecommendVideo这样的一个对象那么同样呢它也是有这么几个字段第一个呢是用户ID
[00:21] 第二个呢是视频ID第三个呢是score得分第四个呢是我们的一个这个时间戳然后呢我们把它来拷贝一下然后呢找到我们的Rickmonger这个工程啊那么来找到Rickmonger的工程然后呢找到这个下面会有一个podio把它丢过来
[00:41] 好那么就是这样的一个对象然后呢我们来编写它的consumer那么consumer呢我们就直接拷贝过来了跟我们之前写的非常类似啊那我们拷过来看一下啊那么首先呢我们可以看到哎这块会有些问题啊这个是我们是这个不需要它对吧这个圈子这个也不需要啊把这个
[01:03] 处理一下好嘞好那么来看一下啊在我们的这个consumer中呢呃然后呢首先指定他的topic呢是叫做碳花然后呢video然后呢consumer的group呢是碳花video consumer呃然后呢下面这个的实现啊那么这个all message呃然后呢我们是通过谁呢通过我们的这个消息然后呢通过这个Mapper呢去呃反序列化得到一个json node
[01:31] 然后呢去拿到一些值其中呢有的UID啊VID还有VID还有这个type啊那么呃其实我们这个VID是不是没有用到啊没有用到呢我们就不需要它了那我们就把它去掉就好了那么呃然后呢下面我们定义这个recommend video啊这样的一个呃对象然后呢去设置这个用户ID还有呃它的
[01:53] 自身的这个ID还有这个我们当前的时间戳然后还有video的ID就是VID然后呢下面呢我们对这个type呢我们去做一个处理然后呢这个如果是唯一的话那就走到这来二走到这然后呢三走到这那么按照我们的一个积分规则那么我们来看一下这个积分规则那么如果是发布的话那么是计两分
[02:21] 那么如果是点赞的话我们是记五分啊如果是取消点赞那就是负五分然后呢评论啊就十分默认的是零分呃然后呢我们最后呢去把数据呢保存起来啊保存到这个Rickmong的video呃这个就是这个库里面来哎呀OK好那么就是这样的一些这个逻辑啊那么接下来呢我们就可以去做测试了好那我们把这个呃我们的这个工程呢都来重启一下包括我们这个
[02:51] 就是double的这个服务这个SSO不需要重启然后呢还有就是我们这个serverserver也需要重启一下那么把这个先关掉然后呢就come on也需要重启一下好那么我们来等待一下它启动好那么现在呢我们就都跑起来了然后呢我们去发送一个小视频我们来看一下这个效果那么我们找到我们这个server的工程我们先来看一下我们这个小视频
[03:18] 就是我们去发布一个小视频的参数然后呢上面这个呢就是往上面走这个呢有两个参数都是文件一个是我们的图片一个是我们的视频文件那我们来添加一下一个是它一个呢是这个video这个fail好那么这个是我们的一个图片然后呢下面是我们的一个这个视频好那我们在桌面呢会有一个这个视频
[03:48] 就是它然后呢我们点击send发送那么这样我们就还是在我们这个里面去打一个断点然后呢在我们这个Service中啊那么同样的我们也打一个断点找到这个recmond然后呢在我们recmond中呢我们也去打一个断点就是我们消息消费的这个位置也打个断点那我们来看一下啊走提交好那么断点呢是不是就进入了对吧
[04:17] 然后呢我们直接往下面走做一个say我一个video然后呢我们去看它是否执行成功了那么拿到这个ID呢来说明我们执行成功了往下面走做一个消息的一个发送好那么OK那么可以看到呢前面的这个已经有了这个消息的接收这一块了对吧然后呢走走拿到消息拿到消息内容走走走走走来看一下这个对象啊那我们再下一步
[04:46] 好那么这个对象的内容是不是是符合我们这个预期的对吧哎OK好然后呢我们继续往下面去走然后呢是第一个啊这个操作就是type为1然后呢设置score呢为2走然后呢这个呢就是我们的video对象了看一下啊video对象那么这个是不是得分就是2.0啊这样的一个分分数然后呢走
[05:15] 做一个保存好通过然后再回到我们这个server这个里面来同样也通过好那么我们但断点就去掉了当然我们也可以去做点赞以及操作我们先来看一下我们这个数据来刷新一下那么这个是在这个然后数据就是这样的一条数据了我们可以再来测试一下我们的一个点赞这个操作
[05:41] 那么我们点赞的是在这个位置那么我们需要后面加一个like发起的是一个post请求那么当然我们首先是需要我们的ID对吧需要这个ID那么我们把两个文件就去掉然后后面跟一个我们小视频的ID那么小视频的一个ID是在我们找到这个里面来这个ID因为这个里面数据还是比较多的
[06:11] 那么我们得找一下看一下啊是在是在最后一条吧那么这个vid我们可能没没找到我们的这个数据啊这个刚刚呢可能也没记录那个就是我们视频的一个id啊那么这样的话呢我们来看一下能不能找到啊这个哦那就是102了那就是他啊对的那就是最后的那那条数据啊
[06:40] 那么往后面走就是最后的这个102102这个啊那就它那么我们来查看一下这个就是我们的视频ID然后呢我们去在这个位置啊加一个like操作然后呢走好那么消息是不是又来了那我们就直接通过吧把这个断点也去掉了那么再回到刚才的我们这个表中再查看一下是不是又多了一条这个数据啊对吧那么这个呢就是还是对我们这条数据做
[07:08] 这个视频数据呢做一个操作那么做一个点赞的这个操作啊OK那么可以看到跟我们前面的这个实现的是是不是非常一致的啊非常一致的好那么这样的话呢我们就最后实现了我们这个数据了对吧那么我们基于这里面的数据呢其实就可以做推荐了对吧OK好那么关于这个小视频的这个消息的一个接收处理啊那么就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import org.apache.RocketMQ.spring.annotation.RocketMQMessageListener;
import org.apache.RocketMQ.spring.core.RocketMQListener;
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

