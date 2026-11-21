# 画面线理解：17.小视频推荐之发送消息

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\17.小视频推荐之发送消息_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:21, 01:02, 01:41, 02:55, 04:10, 05:03, 05:45, 06:27, 07:12, 08:25, 09:15, 10:01, 10:48, 11:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:03:04

1) 这一组画面整体在讲什么（一句话）：
实现视频推荐系统的后端功能，包括视频自增ID、动态计分规则、消息发送、点赞、评论、关注等核心业务逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示视频实体类Video的定义，包含@Document注解、@Data、@AllArgsConstructor、@NoArgsConstructor等注解，以及字段如videoId、userId、title、locationName等。
画面2：展示VideoApiImpl类中的saveVideo方法，用于保存视频对象，调用mongoTemplate.save(video)。
画面3：展示修改后的VideoApiImpl类，添加了视频ID生成、创建时间设置、动态计分规则的逻辑。
画面4：展示VideoMQService类中的likeVideoMsg、disLikeVideoMsg、commentVideoMsg方法，用于处理视频点赞、取消点赞、评论消息。
画面5：展示MongoTemplate的API方法，用于操作MongoDB数据库。
画面6：展示VideoMQService类的包和导入语句，以及类定义。
画面7：展示VideoController类中的saveVideo方法，用于接收前端上传的视频文件并调用videoService.saveVideo方法。
画面8：展示VideoApiImpl类中的saveVideo方法，添加了视频ID生成、创建时间设置、动态计分规则的逻辑。
画面9：展示VideoController类中的likeComment方法，用于处理视频评论点赞。
画面10：展示VideoController类中的likeComment方法，添加了视频点赞成功后发送消息的逻辑。
画面11：展示VideoController类中的queryCommentsList方法，用于查询视频评论列表。
画面12：展示VideoController类中的saveComments方法，用于保存评论。
画面13：展示VideoController类中的saveVideo方法，用于接收前端上传的视频文件并调用videoService.saveVideo方法。
画面14：展示VideoController类中的saveUserFocusComments方法，用于保存用户关注的评论。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
package com.lanhua.dubbo.server.pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.mongodb.core.mapping.Document;
import java.util.List;
@Data
@NoArgsConstructor
@AllArgsConstructor
@Document(collection = "video")
public class Video implements java.io.Serializable {
    private static final long serialVersionUID = -3137323368493387L;
    private ObjectId id; //主键id
    private Long vid;
    private Long userId;
    private String title;
    private String longitude; //经度
    private String latitude; //纬度
    private String locationName; //位置名称
}
```

画面2：
```java
@Service(version = "1.0.0")
public class VideoApiImpl implements VideoApi {
    @Autowired
    private MongoTemplate mongoTemplate;
    @Override
    public Boolean saveVideo(Video video) {
        if (video.getUserId() == null) {
            return false;
        }
        video.setField("videoId", video.getId());
        video.setField("created", System.currentTimeMillis());
        this.mongoTemplate.save(video);
        return true;
    }
}
```

画面3：
```java
@Override
public Boolean saveVideo(Video video) {
    if (video.getUserId() == null) {
        return false;
    }
    video.setId(ObjectId.get());
    video.setCreated(System.currentTimeMillis());
    //生成vid
    video.setVid(this.idService.created("video", video.getId().toString()));
    this.mongoTemplate.save(video);
    return true;
}
```

画面4：
```java
public Boolean likeVideoMsg(String videoId) { return this.sendMsg(videoId, type: 2); }
public Boolean disLikeVideoMsg(String videoId) { return this.sendMsg(videoId, type: 3); }
public Boolean commentVideoMsg(String videoId) { return this.sendMsg(videoId, type: 4); }
```

画面5：
```java
find(Query query, Class<T> entityClass, String collectionName)
save(T objectToSave, String collectionName)
findId(Object id, Class<T> entityClass, String collectionName)
remove(Query query, Class<T> entityClass, String collectionName)
remove(Class<T> domainType)
remove(Object object, String collectionName)
```

画面6：
```java
package com.tanhu.server.service;
import com.alibaba.dubbo.config.annotation.Reference;
import com.tanhu.dubbo.server.api.QuanziApi;
import com.tanhu.dubbo.server.api.Publish;
import com.tanhu.server.pojo.Video;
import com.tanhu.server.utils.UserThreadLocal;
import org.apache.rocketmq.spring.core.RocketMQTemplate;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.HashMap;
import java.util.Map;
@Service
public class VideoMQService {
    private static final Logger LOGGER = LoggerFactory.getLogger(VideoMQService.class);
    @Autowired
    private RocketMQTemplate rocketMQTemplate;
}
```

画面7：
```java
private CommentsController commentsController;
@Autowired
private VideoMQService videoMQService;
@PostMapping("/video")
public ResponseEntity<Void> saveVideo(@RequestParam(value = "videoThumbnail", required = false) MultipartFile picFile,
                                     @RequestParam(value = "videoFile", required = false) MultipartFile videoFile) {
    try {
        Boolean bool = this.videoService.saveVideo(picFile, videoFile);
        if (bool) {
            return ResponseEntity.ok();
        } else {
            throw new RuntimeException("保存失败");
        }
    } catch (Exception e) {
        e.printStackTrace();
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    }
}
```

画面8：
```java
@Override
public String saveVideo(Video video) {
    if (video.getUserId() == null) {
        return null;
    }
    video.setId(ObjectId.get());
    video.setCreated(System.currentTimeMillis());
    video.setVid(this.idService.created("video", video.getId().toString()));
    this.mongoTemplate.save(video);
    return video.getId().toString();
}
```

画面9：
```java
@PostMapping("/{id}/like")
public ResponseEntity<Long> likeComment(@PathVariable("id") String videoId) {
    ResponseEntity<Long> entity = this.movementsController.likeComment(videoId);
    if(entity.getStatusCode().is2xxSuccessful()) {
        this.videoMQService.transmitMsg(videoId);
        return entity;
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面10：
```java
@PostMapping("/{id}/like")
public ResponseEntity<Long> likeComment(@PathVariable("id") String videoId) {
    ResponseEntity<Long> entity = this.movementsController.likeComment(videoId);
    if(entity.getStatusCode().is2xxSuccessful()) {
        this.videoMQService.transmitMsg(videoId);
        return entity;
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面11：
```java
@GetMapping("/{id}/comments")
public ResponseEntity<PageResult> queryCommentsList(@PathVariable("id") String videoId,
                                                   @RequestParam(value = "page", defaultValue = "1") Integer page,
                                                   @RequestParam(value = "pagesize", defaultValue = "10") Integer pagesize) {
    return this.commentsController.queryCommentsList(videoId, page, pagesize);
}
```

画面12：
```java
@PostMapping("/{id}/comments")
public ResponseEntity<Void> saveComments(@RequestBody Map<String, String> param,
                                        @PathVariable("id") String videoId) {
    param.put("movementId", videoId);
    return this.commentsController.saveComments(param);
}
```

画面13：
```java
@PostMapping("/video")
public ResponseEntity<Void> saveVideo(@RequestParam(value = "videoThumbnail", required = false) MultipartFile picFile,
                                     @RequestParam(value = "videoFile", required = false) MultipartFile videoFile) {
    try {
        String id = this.videoService.saveVideo(picFile, videoFile);
        if (StringUtils.isEmpty(id)) {
            return ResponseEntity.ok(null);
        }
        this.videoMQService.commentVideoMsg(videoId);
        return ResponseEntity.ok();
    } catch (Exception e) {
        e.printStackTrace();
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    }
}
```

画面14：
```java
@GetMapping("/{id}/userFocus")
public ResponseEntity<Void> saveUserFocusComments(@PathVariable("id") Long userId) {
    try {
        Boolean bool = this.videoService.followUser(userId);
        if (bool) {
            return ResponseEntity.ok();
        }
    } catch (Exception e) {
        e.printStackTrace();
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
