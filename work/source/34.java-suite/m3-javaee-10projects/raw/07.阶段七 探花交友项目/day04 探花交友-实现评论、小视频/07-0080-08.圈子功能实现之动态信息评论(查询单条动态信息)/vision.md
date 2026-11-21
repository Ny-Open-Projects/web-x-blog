# 画面线理解：08.圈子功能实现之动态信息评论（查询单条动态信息）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\08.圈子功能实现之动态信息评论（查询单条动态信息）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 01:24, 02:15, 03:17, 04:14, 05:18, 05:59, 06:47, 07:12, 08:12, 09:00, 09:40, 10:30, 11:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:53:20

1) 这一组画面整体在讲什么（一句话）：
实现一个社交应用中“动态”功能的后端服务，包括定义 Dubbo 接口、实现接口、服务接口定义以及相关业务逻辑代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Typora 文档，内容为“1.3. 查询单条动态”章节，其中包含“1.3.1. 定义 dubbo接口”和“1.3.2. dubbo接口实现”部分，代码片段为：
```java
// 根据id查询
@Param id
@Return
```
和
```java
@Override
public publish queryPublishById(String id) {
    return this.mongoTemplate.findBysId(new ObjectId(id), Publish.class);
}
```
画面 2: 显示一个空白的网页，页面中央有加载动画，URL 为 https://mock.boxuegu.com/project/164/interface/api/67249。

画面 3: 显示 IntelliJ IDEA 编辑器，打开文件 MovementsController.java，光标位于 @GetMapping 注解处，代码片段为：
```java
@GetMapping("/id/unlove")
public ResponseEntity<Long> unloveComment(@PathVariable("id") String publishId) {
    try {
        NullPointerExce...
    } catch (Exception e) {
        return ResponseEntity.badRequest().body(0L);
    }
}
```
画面 4: 显示 IntelliJ IDEA 编辑器，光标位于 if (nt) 语句处，代码片段为：
```java
if (nt) {
    // 代码被模糊处理
}
```
画面 5: 显示 IntelliJ IDEA 编辑器，打开文件 MovementsService.java，光标位于 public 语句处，代码片段为：
```java
public PageResult queryPublishList(User user, Integer page, Integer pageSize) {
    return this.queryPublishList(user, page, pageSize);
}
```
画面 6: 显示 IntelliJ IDEA 编辑器，打开文件 QuanzApi.java，光标位于方法定义处，代码片段为：
```java
Long queryCommentCount(String publishId, Integer type);
// 根据id查询
@Param publishId
@Return
Publish queryPublishById(String publishId);
```
画面 7: 显示 IntelliJ IDEA 编辑器，打开文件 QuanzApiImpl.java，光标位于方法实现处，代码片段为：
```java
@Override
public Long queryCommentCount(String publishId, Integer type) {
    Criteria criteria = Criteria.where("publishId").is(new ObjectId(publishId))
            .and("commentType").is(type);
    Query query = Query.query(criteria);
    return this.mongoTemplate.count(query, Comment.class);
}

@Override
public Publish queryPublishById(String publishId) {
    return this.mongoTemplate.findById(new ObjectId(publishId), Publish.class);
}
```
画面 8: 显示 IntelliJ IDEA 编辑器，打开文件 MovementsService.java，光标位于代码片段处，代码片段为：
```java
String likeUserCommentKey = "QUANZI_COMMENT_LIKE_USER" + user.getId() + movements.getId();
String value = this.redisTemplate.opsForValue().get(likeUserCommentKey);
if (value != null) {
    movements.setHasLiked(1);
} else {
    movements.setHasLiked(0);
}
```
画面 9: 显示 IntelliJ IDEA 编辑器，打开文件 MovementsService.java，光标位于代码片段处，代码片段为：
```java
pageResult.setCounts(0);
pageResult.setPage(0);
pageResult.setPage(page);
List<Publish> records = pageInfo.getRecords();
if (CollectionUtils.isEmpty(records)) {
    return pageResult;
}
pageResult.setItems(movementList);
return pageResult;
```
画面 10: 显示 IntelliJ IDEA 编辑器，打开文件 MovementsService.java，光标位于代码片段处，代码片段为：
```java
private void fillValueToMovements(List<Publish> records) {
    User user = UserThreadLocal.get();
    List<Movements> movementsList = new ArrayList<>();
    List<Long> userIds = new ArrayList<>();
    for (Publish record : records) {
        Movements movements = new Movements();
        movements.setId(record.getId().toHexString());
        movements.setUserId(record.getUserId());
        if (userIds.contains(record.getUserId())) {
            continue;
        }
        userIds.add(record.getUserId());
        movements.setHasLiked(this.redisTemplate.hasKey(likeUserCommentKey) ? 1 : 0);
        movementsList.add(movements);
    }
    return movementsList;
}
```
画面 11: 显示 IntelliJ IDEA 编辑器，打开文件 MovementsService.java，光标位于代码片段处，代码片段为：
```java
if (CollectionUtils.isEmpty(records)) {
    return pageResult;
}
pageResult.setItems(this.fillValueToMovements(records));
return pageResult;
```
画面 12: 显示 IntelliJ IDEA 编辑器，打开文件 MovementsService.java，光标位于代码片段处，代码片段为：
```java
public Movements queryMovementById(String publishId) {
    Publish publish = this.quanzApi.queryPublishById(publishId);
    if (null == publish) {
        return null;
    }
    // 查询到动态数据，数据的请求
    List<Movements> movementsList = this.fillValueToMovements(Arrays.asList(publish));
    return movementsList.get(0);
}
```
画面 13: 显示 Typora 文档，内容为“1.3.2. dubbo接口实现”和“1.3.3. 定义服务接口”部分，代码片段为：
```java
@Override
public publish queryPublishById(String id) {
    return this.mongoTemplate.findBysId(new ObjectId(id), Publish.class);
}
```
和
```java
@GetMapping("/id")
public ResponseEntity<Movements> queryById(@PathVariable("id") String publishId) {
    Movements movements = this.movementsService.queryById(publishId);
    if (movements == null) {
        return ResponseEntity.notFound().build();
    }
    return ResponseEntity.ok(movements);
}
```
画面 14: 显示 Typora 文档，内容为“1.3.2. dubbo接口实现”和“1.3.3. 定义服务接口”部分，代码片段为：
```java
@GetMapping("/id")
public ResponseEntity<Movements> queryById(@PathVariable("id") String publishId) {
    Movements movements = this.movementsService.queryById(publishId);
    if (movements == null) {
        return ResponseEntity.notFound().build();
    }
    return ResponseEntity.ok(movements);
}
```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
（已在上文第 2 点中完整列出所有代码片段）

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题、架构图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）
