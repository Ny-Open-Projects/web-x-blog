# 画面线理解：08.圈子推荐之发送消息（下）

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\08.圈子推荐之发送消息（下）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:41, 01:18, 01:44, 02:13, 02:46, 03:10, 03:36, 03:59, 04:23, 04:44, 05:09, 05:27, 06:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:55:48

1) 这一组画面整体在讲一个社交应用中“发布动态”功能的前后端实现，包括控制器、服务层、MQ消息发送以及相关接口定义。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 `MovementsController` 中的 `@PostMapping` 方法，用于接收用户发布的动态，参数包括文本内容、位置经纬度和图片文件。
画面2: 展示了 `MovementsController` 中 `@PostMapping` 方法的 try-catch 块，调用 `movementsService.saveMovements` 后，若成功则调用 `quanziMQService.sendPublishMsg` 发送消息。
画面3: 展示了 `QuanZiApi` 接口，定义了 `savePublish` 和 `queryPublishList` 两个方法，用于发布和查询动态。
画面4: 展示了 `QuanZiApiImpl` 中的 `savePublish` 方法实现，包含将图片存入 MongoDB、查询好友并写入时间线的逻辑。
画面5: 展示了 `MovementsService` 中的 `saveMovements` 方法，用于创建 `Publish` 对象、上传图片并设置媒体信息。
画面6: 展示了 `MovementsController` 中 `@PostMapping` 方法的完整逻辑，包括调用服务层和发送 MQ 消息。
画面7: 展示了 `MovementsController` 中 `@GetMapping("/id/dislike")` 方法，用于取消点赞，调用服务层并发送 MQ 消息。
画面8: 展示了 `MovementsController` 中 `@GetMapping("/id/unlove")` 方法，用于取消收藏，调用服务层并发送 MQ 消息。
画面9: 展示了 `MovementsController` 中 `@GetMapping("/id")` 方法，用于查询动态详情，调用服务层并发送 MQ 查询消息。
画面10: 展示了 `CommentsController` 的类定义，包含 `@Autowired` 注入的 `commentsService` 和 `movementsService`。
画面11: 展示了 `CommentsController` 中 `@PostMapping` 方法，用于保存评论，调用服务层并发送 MQ 消息。
画面12: 展示了 Typora 文档中 `day08` 的内容，包含 `dislikeComment` 和 `loveComment` 方法的伪代码和注释。
画面13: 展示了 Typora 文档中 `day08` 的内容，包含 `itcast-tanhua-recommend` 工程的 `pom.xml` 配置片段。
画面14: 展示了 Typora 文档中 `day08` 的内容，包含 `QuanziMQService` 类的定义，包含 `@Autowired` 注入的 `rocketMQTemplate` 和 `quanziApi`。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1:
```java
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
@RequestMapping("movements")
public class MovementsController {

    @Autowired
    private MovementsService movementsService;

    /**
     * 发布动态
     * @param textContent
     * @param location
     * @param longitude
     * @param latitude
     * @param multipartFile
     * @return
     */
    @PostMapping
    public ResponseEntity<Void> saveMovements(@RequestParam("textContent") String textContent,
                                             @RequestParam("location") String location,
                                             @RequestParam("longitude") String longitude,
                                             @RequestParam("latitude") String latitude,
                                             @RequestParam("multipartFile") MultipartFile[] multipartFile) {
```

画面2:
```java
try {
    Boolean bool = this.movementsService.saveMovements(textContent, location, longitude, latitude, multipartFile);
    if (bool) {
        // 发送消息
        this.quanziMQService.sendPublishMsg(publishId);
        return ResponseEntity.ok(null);
    }
} catch (Exception e) {
    e.printStackTrace();
}
return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
```

画面3:
```java
package com.tanhua.dubbo.server.api;

import ...

public interface QuanZiApi {

    /**
     * 发布动态
     * @param publish
     * @return
     */
    String savePublish(Publish publish);

    /**
     * 查询好友动态
     * @param userId
     * @param page
     * @param pageSize
     * @return
     */
    PageInfo<Publish> queryPublishList(Long userId, Integer page, Integer pageSize);
```

画面4:
```java
// 将相册对象写入到MongoDB中
this.mongoTemplate.save(album, collectionName: "quanzi_album" + publish.getUserId());
// 查询当前用户的好友数据，将动态数据写入到好友的时间线表中
Query query = Query.query(Criteria.where("userId").is(publish.getUserId()));
List<User> users = this.mongoTemplate.find(query, Users.class);
for (User user : users) {
    Timeline timeline = new Timeline();
    timeline.setId(ObjectId.get());
    timeline.setUserId(publish.getUserId());
    timeline.setPublishId(publish.getId());
    timeline.setPublishTime(System.currentTimeMillis());
    this.mongoTemplate.save(timeline, collectionName: "quanzi_time_line_" + user.getFriendId());
}
return true;
```

画面5:
```java
User user = UserThreadLocal.get();
Publish publish = new Publish();
publish.setUserId(user.getId());
publish.setText(textContent);
publish.setLocationName(location);
publish.setLatitude(latitude);
publish.setLongitude(longitude);

// 图片上传
List<String> imageUrls = new ArrayList<>();
for (MultipartFile file : multipartFile) {
    PicUploadResult uploadResult = this.picUploadService.upload(file);
    imageUrls.add(uploadResult.getName());
}
publish.setMedias(imageUrls);
```

画面6:
```java
try {
    String publishId = this.movementsService.saveMovements(textContent, location, longitude, latitude, multipartFile);
    if (StringUtils.isNotEmpty(publishId)) {
        // 发送消息
        this.quanziMQService.sendPublishMsg(publishId);
        return ResponseEntity.ok(null);
    }
} catch (Exception e) {
    e.printStackTrace();
}
return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
```

画面7:
```java
@GetMapping("/id/dislike")
public ResponseEntity<Long> dislikeComment(@PathVariable("id") String publishId) {
    try {
        Long count = this.movementsService.dislikeComment(publishId);
        if (null != count) {
            // 发送消息
            this.quanziMQService.sendSavePublishMsg(publishId);
            return ResponseEntity.ok(count);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面8:
```java
@GetMapping("/id/unlove")
public ResponseEntity<Long> unloveComment(@PathVariable("id") String publishId) {
    try {
        Long count = this.movementsService.unloveComment(publishId);
        if (null != count) {
            return ResponseEntity.ok(count);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面9:
```java
@GetMapping("/id")
public ResponseEntity<Movements> queryMovementsById(@PathVariable("id") String publishId) {
    try {
        Movements movements = this.movementsService.queryMovementsById(publishId);
        if (null != movements) {
            // 发送消息
            this.quanziMQService.sendQueryPublishMsg(publishId);
            return ResponseEntity.ok(movements);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面10:
```java
@RestController
@RequestMapping("comments")
public class CommentsController {

    @Autowired
    private CommentsService commentsService;

    @Autowired
    private MovementsService movementsService;
```

画面11:
```java
@PostMapping
public ResponseEntity<Void> saveComments(@RequestBody Map<String, String> param) {
    try {
        String publishId = param.get("movementId");
        String content = param.get("comment");
        Boolean bool = this.commentsService.saveComments(publishId, content);
        if (bool) {
            // 发送消息
            this.quanziMQService.sendCommentPublishMsg(publishId);
            return ResponseEntity.ok(null);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面12:
```java
{
    try {
        Long likeCount = this.movementsService.cancelLikeComment(publishId);
        if (null != likeCount) {
            // 发送取消点赞消息
            this.quanziMQService.dislikePublishMsg(publishId);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}

/**
 * 取消收藏
 * @param publishId
 * @return
 */
@GetMapping("/id/unlove")
public ResponseEntity<Long> unloveComment(@PathVariable("id") String publishId) {
    try {
        Long loveCount = this.movementsService.unloveComment(publishId);
        if (null != loveCount) {
            return ResponseEntity.ok(loveCount);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面
