# 画面线理解：19.小视频推荐之构造数据

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\19.小视频推荐之构造数据_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:29, 00:43, 00:52, 01:24, 01:38, 01:47, 01:56, 02:03, 02:10, 02:19, 02:35, 02:46, 02:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:04:50

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Dubbo 服务中使用 Spring Boot 和 MongoDB 实现视频推荐数据的生成、存储与查询功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 MongoDB 数据库界面，查看名为 “recommend_video_20191007” 的集合，其中包含多个视频推荐对象，显示了 id、userId、videoId、score、date、class 等字段。
画面 2：展示 IntelliJ IDEA 中 VideoMsgConsumer.java 文件，其中定义了 @Autowired MongoTemplate，并在 onMessage 方法中从消息中解析 userId，用于后续处理。
画面 3：展示 TestVideoApi.java 文件中的 testSaveRecommend 方法，用于生成并保存 1000 条推荐视频数据，设置视频的 locationName、seeType、picUrl、videoUrl、created 等属性。
画面 4：展示 TestVideoApi.java 文件中的 testSaveRecommend 方法，其中设置视频的 score 为随机值（0-15），并保存到 MongoDB。
画面 5：展示 VideoApiImpl.java 文件中的 saveVideo 方法，用于保存视频对象，设置 videoId、created、setVid 等属性，并调用 mongoTemplate.save。
画面 6：展示 TestVideoApi.java 文件中的 testSaveVideo 方法，用于生成并保存视频对象，设置 videoId、userId、locationName、seeType、picUrl、videoUrl、created 等属性。
画面 7：展示测试运行结果，显示 Spring Boot 启动日志，以及测试失败（Tests passed: 0 of 1）。
画面 8：展示测试运行时的控制台输出，显示 SLF4J 多绑定警告信息。
画面 9：展示 MongoDB 数据库界面，查看 “recommend_video_20191007” 集合中的数据，显示了多个视频对象的详细信息。
画面 10：展示测试运行结果，显示测试通过（Tests passed: 1 of 1），并输出了生成的视频 ID。
画面 11：展示 TestVideoApi.java 文件中的 testSaveRecommend 方法，用于生成并保存推荐视频数据。
画面 12：展示 TestVideoApi.java 文件中的 testSaveRecommend 方法，其中设置视频的 score 为随机值（0-15），并保存到 MongoDB。
画面 13：展示 Typora 编辑器中的 day08 推荐.md 文件，其中包含 TestVideoApi 类的代码，用于测试视频保存功能。
画面 14：展示 MongoDB 数据库界面，查看 “recommend_video_20191007” 集合中的数据，显示了多个视频对象的详细信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```java
private static final Logger LOGGER = LoggerFactory.getLogger(VideoMsgConsumer.class);
@Autowired
private MongoTemplate mongoTemplate;
@Override
public void onMessage(String msg) {
    try {
        JsonNode jsonNode = MAPPER.readTree(msg);
        Long userId = jsonNode.get("userId").asLong();
    } catch (Exception e) {
        LOGGER.error("解析消息失败", e);
    }
}
```

画面 3：
```java
@Test
public void testSaveRecommend() {
    for (int i = 0; i < 1000; i++) {
        RecommendVideo recommendQuanzi = new RecommendVideo();
        recommendQuanzi.setDate(System.currentTimeMillis());
        recommendQuanzi.setUserId(ObjectId.get());
        recommendQuanzi.setScore(Double.valueOf(RandomUtils.nextInt(0, 15)));
        recommendQuanzi.setVideoId(RandomUtils.nextLong(1000, 1099));
        this.mongoTemplate.save(recommendQuanzi, collectionName: "recommend_video_20191007");
    }
}
```

画面 5：
```java
@Override
public String saveVideo(Video video) {
    if (video.getUserId() == null) {
        return null;
    }
    video.setId(ObjectId.get());
    video.setCreated(System.currentTimeMillis());
    video.setVid(this.idService.createId(type "video", video.getId()).toString());
    this.mongoTemplate.save(video);
    return video.getId().toHexString();
}
```

画面 6：
```java
@Test
public void testSaveVideo() {
    for (int i = 0; i < 100; i++) {
        Video video = new Video();
        video.setId(ObjectId.get());
        video.setUserId(RandomUtils.nextLong(1, 10));
        video.setVid(Long.valueOf(1000 + i));
        video.setLocationName("上海市");
        video.setSeeType(1);
        video.setPicUrl("http://itcast-tanhua.oss-cn-shanghai.aliyuncs.com/images/2019/10/07/157043");
        video.setVideoUrl("http://192.168.31.81:8888/group1/M00/00/2/");
        video.setCreated(System.currentTimeMillis());
        String videoId = this.videoApi.saveVideo(video);
        System.out.println(videoId);
    }
}
```

画面 13：
```java
package com.tanhua.dubbo.server.api;
import com.tanhua.dubbo.server.pojo.Video;
import org.apache.commons.lang3.RandomUtils;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit
