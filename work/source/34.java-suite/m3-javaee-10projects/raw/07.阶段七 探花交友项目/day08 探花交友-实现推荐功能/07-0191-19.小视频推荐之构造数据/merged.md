# 19.小视频推荐之构造数据

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\19.小视频推荐之构造数据_【海量资源尽在 666java.com】.mp4
- 时长 3分11秒（音频 189s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就应该来做它的推荐了对吧但是呢我们首先呢还是需要去构造数据啊那我们把这个数据构造出来那么需要构造两个数据那么一个呢就是我们这个video这个数据啊那我们把这个表就给它删除掉吧我重新去做一个生成啊就可以了把这个表呢也删除掉好嘞好那么这样的话呢我们就可以来构造数据了把它来拷贝一下同样的还是拷贝到我们的这个
[00:30] 就是我们这个SS这个double这个里面来Service找到下面有一个test我们把它丢到这个里面来这个里面呢它会缺少缺少这个Rickmong的video对象那么我们把这个对象呢来拷贝一下就是这个对象然后呢我们拷贝到这个里面来这样的话保证它不报错然后呢我们来看一下那么其实同理呢也是我们去生成100条我们这个
[00:59] 数据啊然后呢我们呢也是呢去给他去设置我们的一个vid呢是一个1000啊加爱的这样的一个id用户id呢同样的也是1到10这样的一个用户id其他的数据呢那就是一些常规的一些这个数据了然后呢我们来看一下做一个这个c5操作那么c5操作呢我们到这个里面来找到这个video
[01:25] API这个C5操作那么这个里面呢我们先把这个增长这个ID呢先VID的设置值呢先去掉然后呢我们再去做一个测试用力的一个执行好那我们到这个位置吧来执行一下然后呢走去做一个执行那么执行完成之后啊那我们再把它呢再还原回来当然了我们先得停一下为什么呢原因是我们先把之前这个double停掉要不然它会端口有冲突跑不起来好那我们再次执行一下
[01:55] OK好那么我们程序呢执行结束了啊那么下面我们来看一下我们的这个表找一下video然后呢可以看到数据呢是不是已经就生成了啊对吧OK好嘞好那么我们千万要记着呢把之前这个代码呢要这个还原一下啊要不然的话这个ID就没了对吧好那么然后呢我们再回到这个测试用力中啊我们再去插入1000条这个Rekmon的这个数据啊
[02:24] 然后呢同样的他也是这个score得分的是0到15分之间然后呢UID呢是1到10然后呢video ID呢是1000到1099然后呢我们X5的这个是改成什么呢10吧这个我们可以随便去写啊然后呢我们去做一个这个sale走那我们来等待他的一个执行好那么现在呢又执行结束了那我们再回到我们的这个
[02:51] Connection 中去做一个刷新那么数据是不是就来了那么我们构造了有1000条这样的一个数据好那么下面我们就会基于这个数据来做一个我们MLlib的一个推荐的一个实现OK好那么关于我们这个数据的一个构造那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

