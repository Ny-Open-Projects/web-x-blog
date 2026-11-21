# 08.圈子推荐之发送消息（下）

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\08.圈子推荐之发送消息（下）_【海量资源尽在 666java.com】.mp4
- 时长 6分8秒（音频 368s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来修改一下我们的Controller来调用我们前面所编写的这个message的一个Service啊那么首先呢我们来找到我们的Controller就是我们这个movins Controller然后呢我们把那个Service呢去注入进来那么我们叫什么呢叫做圈子对吧圈子mq啊Service把它呢注入进来那么注入进来之后呢我们就可以去调用它了那首先呢我们可以看到
[00:27] 第一个呢其实就是我们的这个发布动态啊然后呢我们在发布动态成功之后啊那我们就需要去发送我们的这个消息啊那我们就调用它然后点做一个什么send然后做一个save publish message那么要注意的是呢在这个位置我们是需要传递publish id的但是呢我在我们之前的这个接口中啊那我们并没有去返回我们的一个
[00:56] public id而是直接返回了一次一个布尔类型就是一个标识是否成功那么显然呢这个是不太能够满足我们现在需求的所以说呢我们就需要去修改一下之前的我们这个圈子API的这个接口这个方法那我们来看一下那么C5之后呢我们需要去返回一个谁呢返回我们的这个就是谁呢我们的这个叫什么呢主建ID对吧
[01:23] 好那么接下来呢我们来找一下我们的实现啊在我们的这个double的一个Service中那我们找到啊具体的这个实现那我们来修改一下然后呢再往下面去走呃来看一下这个C5啊那么我们呃返回的是一个支付创呃然后呢在return这个位置是不是就应该拿到我们这个publish点点get什么呢ID啊拿到他的支付创然后呢如果
[01:54] 如果我们去执行失败的话那么就return none这样的话就可以了好那么我们来看一下这样的话就这块也有问题那就return none好这样的话就没问题了然后呢在我们的刚刚所编写control中那么我们可以看到在这个里面然后呢最后它return return到这那么就可以return谁呢直接去把这个stream返回来然后呢在这个位置我们去接收一下就拿到谁呢
[02:23] publish对吧ID然后呢如果判断如果如果这个它为notnot empty如果不为空的话那么我们就执行到这个里面来对吧那就不为空代表的就是发送就是保存成功了那么这样的话呢我们这个是不是就搞定了对吧那么接着继续往下面看那么下面这个呢是查询这个我们不发消息
[02:51] 然后呢这个也不发对吧点赞是不是也需要去发送啊这个消息的对不对那么点赞我们就需要去调用什么呢是不是send我们这个叫做like啊publish啊message呃然后呢我们继续往下面看那么取消点赞是不是同样的也需要去调用那我们来看一下叫send dislike那么传递public id没有问题呃然后呢我们这个喜欢
[03:20] 那么我们也来去修改一下叫什么呢Send什么呢Send什么呢Low对吧Low好那么这个呢是喜欢下面这个是一个取消喜欢那么我们还需要去修改一下那么这个叫什么呢叫Send Dislow那么这个呢就是发送这个取消喜欢的这样的一个消息
[03:46] 那么下面这个是查询对不对那我们就丢到这个里面来是不是我们就去调用这个send什么呢叫宽域啊宽域好那么这样的话是不是就OK了对吧当然还有一个没有做修改就是谁呢我们去评论啊评论我们的这个动态那么在之前呢我们评论是不是写到的是在我们comments这个里面来啊对吧评论我们来看一下啊那么这个查询列表发表评论那么是不是就在这个位置啊
[04:16] 那么我们就需要去写啊这样的一个逻辑了那么下面呢我们还在在我们这个comments Controller中啊那么同样的也是需要把我们这个圈子mq啊Service呢去注入进来那么我们去注一下呃然后呢下面呢我们就可以哎去哪了是不是在这个位置啊去调用它什么呢去啊send什么呢什么啊comment
[04:41] PublishMessage那么这样的话是不是就可以去做一个消息的发送了那么基本上我们这个方法是不是就调用完成了总共呢是有七个啊这样的一个操作哎OK好那么这个呢我们是不是其实就已经完成了我们消息的一个发送对吧一个呢就是我们这个MomentsController中的一个调用当然了我们刚刚呢是不是也修改一下我们的一个Double中的一个接口
[05:08] 那么呃这第一个第二个呢是在我们的那个就是comment啊就是我们这个comment中呢也需要去做一个调用啊这个大家别忘记了那么我们是在评论是在这个里面去做一个完成的啊那我们来写一个啊写一个这个就写到我们这个讲义中吧那么我们写到这个位置来那么另外一个呢是需要在这儿啊好那么这个呢是在哪里是在这儿对吧好那我们来记录一下
[05:38] 这个中呢也需要去做一次这个修改这个别忘记了比如我们写的这个到这个位置然后就把他给忘记了这样是不行的OK好那么到这里呢我们这个发送消息是不是就已经是搞定了对吧那么消息能够发出去了那么接下来我们要做的事情是不是就应该去接收这个消息并且呢我们去做一个处理对不对OK好那么关于这个消息的一个发送那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

