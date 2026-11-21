# 画面线理解：15_app文章详情_文章关系接口_service代码编写(2)

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\15_app文章详情_文章关系接口_service代码编写(2)【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:09, 02:32, 03:26, 05:25, 06:46, 07:47, 08:55, 09:35, 11:23, 12:35, 13:57, 14:50, 15:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:15:43

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 服务层中实现文章点赞、收藏、关注等行为的逻辑，包括数据库操作和状态判断。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 `ApplikeInfoServiceImp.java` 中的点赞逻辑，通过 `apBehaviorEntryMapper` 查询行为记录，初始化点赞、收藏、关注状态。
画面 2: 鼠标悬停在 `apBehaviorEntryMapper.selectById` 方法上，显示方法签名和注释。
画面 3: 代码中调用 `apCollectionMapper.selectForEntryId` 查询收藏状态，设置 `isCollection`。
画面 4: 代码中调用 `apLikesBehaviorMapper.selectLastLike` 查询点赞状态，设置 `islike`。
画面 5: 代码中调用 `apLikesBehaviorMapper.selectLastUnLike` 查询取消点赞状态，设置 `isunlike`。
画面 6: 展示 `ApplikeInfoServiceImp.java` 中的 `loadArticleBehavior` 方法，定义了 `apBehaviorEntryMapper`、`apCollectionMapper`、`apLikesBehaviorMapper` 等字段。
画面 7: 代码中调用 `apLikesBehaviorMapper.selectLastLike` 查询点赞状态，设置 `islike`。
画面 8: 代码中调用 `apAuthorMapper.selectById` 查询作者信息，设置 `authorId`。
画面 9: 代码中调用 `apAuthorMapper.selectById` 查询作者信息，设置 `authorId`。
画面 10: 展示 `ApplikeInfoServiceImp.java` 中的 `loadArticleBehavior` 方法，定义了 `apBehaviorEntryMapper`、`apCollectionMapper`、`apLikesBehaviorMapper` 等字段。
画面 11: 代码中调用 `apUserFollowMapper.selectByFollowId` 查询关注状态，设置 `isFollow`。
画面 12: 代码中调用 `apUserFollowMapper.selectByFollowId` 查询关注状态，设置 `isFollow`。
画面 13: 代码中创建 `Map<String, Object> data`，并放入 `isFollow`、`islike`、`isunlike`、`isCollection` 等状态。
画面 14: 代码中返回 `ResponseResult.okResult(data)`，将状态数据封装返回。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
long userId = null;
if(user!=null){
    userId = user.getlD();
}
ApBehaviorEntry apBehaviorEntry = apBehaviorEntryMapper.selectByUserlDOrEquipmentlD(userId, dto.getEquipmentId());
boolean islike = false, islike = false, isCollection = false, isFollow=false;
String burst = BurstUtils.groundId(apBehaviorEntry.getlD());
//2. 通过entry和articleId去查看点赞表，看看是否有数据，有数据就说明已经点赞，否则就是没有点赞
//3. 通过entry和articleId去查看点赞表，看看是否有数据，有数据就说明已经点赞，否则就是没有点赞
//4. 通过entry和articleId去查看不喜欢表，看看是否有数据，有数据就说明不喜欢，否则就是喜欢
//5. 通过authorId去app的id userlD(app账号信息id)
//查看关注表，根据当前登录人的userlD与作者的app账号id去查询，如果有数据，就说明已经关注，没有则说明没有关注
return null.
```

画面 2:
```java
ApBehaviorEntry apBehaviorEntry = apBehaviorEntryMapper.selectByUserlDOrEquipmentlD(userId, dto.getEquipmentId());
boolean islike = false, islike = false, isCollection = false, isFollow=false;
String burst = BurstUtils.groundId(apBehaviorEntry.getlD());
//2. 通过entry和articleId去查看点赞表，看看是否有数据，有数据就说明已经点赞，否则就是没有点赞
//3. 通过entry和articleId去查看点赞表，看看是否有数据，有数据就说明已经点赞，否则就是没有点赞
//4. 通过entry和articleId去查看不喜欢表，看看是否有数据，有数据就说明不喜欢，否则就是喜欢
//5. 通过authorId去app的id userlD(app账号信息id)
//查看关注表，根据当前登录人的userlD与作者的app账号id去查询，如果有数据，就说明已经关注，没有则说明没有关注
return null.
```

画面 3:
```java
ApCollection apCollection = apCollectionMapper.selectForEntryId(burst, apBehaviorEntry.getlD(), dto.getArticleId(), ApCollection.Type.ARTICLE.getlD());
if(apCollection!=null){
    isCollection=true;
}
```

画面 4:
```java
apLikesBehaviorMapper.selectLastLike(burst, apBehaviorEntry.getlD(), dto.getArticleId());
```

画面 5:
```java
if(apLikesBehavior!=null && apLikesBehavior.getOperation() == ApLikesBehavior.Type.LIKE.getCode()){
    islike = true;
}
if(apLikesBehavior!=null && apLikesBehavior.getOperation() == ApLikesBehavior.Type.UNLIKE.getCode()){
    islike = false;
}
```

画面 6:
```java
@Autowried
private ApBehaviorEntryMapper apBehaviorEntryMapper;
@Autowried
private ApCollectionMapper apCollectionMapper;
@Autowried
private ApLikesBehaviorMapper apLikesBehaviorMapper;
@Autowried
private ApUnlikesBehaviorMapper apUnlikesBehaviorMapper;
@Override
public ResponseResult loadArticleBehavior(ArticleInfoDto dto) {
    ApUser user = ApoThreadLocalUtils.getUser();
    //用户与设备不能同时为空
    if(user==null && dto.getEquipmentId()!=null){
        return ResponseResult.errorResult(AppErrorCodeEnum.PARAM_REQUIRER);
    }
```

画面 7:
```java
if(apLikesBehavior!=null && apLikesBehavior.getOperation() == ApLikesBehavior.Type.UNLIKE.getCode()){
    islike = false;
}
```

画面 8:
```java
ApAuthor apauthor = apAuthorMapper.selectById(dto.getAuthorId());
```

画面 9:
```java
ApAuthor apauthor = apAuthorMapper.selectById(dto.getAuthorId());
```

画面 10:
```java
@Autowried
private ApBehaviorEntryMapper apBehaviorEntryMapper;
@Autowried
private ApCollectionMapper apCollectionMapper;
@Autowried
private ApLikesBehaviorMapper apLikesBehaviorMapper;
@Autowried
private ApUnlikesBehaviorMapper apUnlikesBehaviorMapper;
@Override
public ResponseResult loadArticleBehavior(ArticleInfoDto dto) {
    ApUser user = ApoThreadLocalUtils.getUser();
    //用户与设备不能同时为空
    if(user==null && dto.getEquipmentId()!=null){
        return ResponseResult.errorResult(AppErrorCodeEnum.PARAM_REQUIRER);
    }
```

画面 11:
```java
if(apUserFollow!=null && apUserFollow.getFollowId()!=null){
    isFollow=true;
}
```

画面 12:
```java
if(apUserFollow!=null && apUserFollow.getFollowId()!=null){
    isFollow=true;
}
```

画面 13:
```java
Map<String, Object> data = new HashMap<>();
data.put("isFollow", isFollow);
data.put("islike", islike);
data.put("isunlike", isunlike);
data.put("isCollection", isCollection);
```

画面 14:
```java
return ResponseResult.okResult(data);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
