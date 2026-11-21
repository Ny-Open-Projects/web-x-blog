# 画面线理解：20.查询推荐动态（编写接口服务以及测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\20.查询推荐动态（编写接口服务以及测试）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:34, 01:37, 02:34, 03:02, 03:39, 04:44, 05:10, 05:40, 06:02, 06:33, 07:11, 07:52, 08:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:46:49

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Mock 服务测试推荐动态接口，并展示后端 Java 代码实现、数据库数据及前端测试结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Mock 服务界面，接口路径为 /movements/recommend，请求头包含 Authorization 和 Content-Type。
画面 2: 展示 MovementsController.java 中 queryPublishList 方法的代码，用于查询用户发布的动态列表。
画面 3: 展示 MovementsService.java 中处理用户信息与动态关联的代码，设置动态的标签、昵称、性别等属性。
画面 4: 展示 MovementsService.java 中 queryPublishList 方法的代码，处理用户 ID 为 null 的情况并调用 quanZiApi 查询。
画面 5: 展示 MovementsController.java 中 queryRecommendPublishList 方法的代码，用于查询推荐动态列表。
画面 6: 展示 MovementsService.java 中 savePublish 方法的代码，处理上传图片并保存动态。
画面 7: 展示 Mock 服务界面，接口路径为 /movements/recommend，请求头包含 Authorization 和 Content-Type。
画面 8: 展示 Advanced REST Client 中设置请求头 Authorization 和 Content-Type，并发送 POST 请求。
画面 9: 展示 MovementsController.java 中 queryPublishList 方法的代码，用于查询用户发布的动态列表。
画面 10: 展示 Advanced REST Client 中发送 GET 请求，请求头包含 Authorization，返回状态码 200。
画面 11: 展示 Advanced REST Client 中发送 GET 请求，请求头包含 Authorization，返回状态码 200。
画面 12: 展示 Genymotion 模拟器启动界面。
画面 13: 展示 Navicat Premium 中 tb_user 表的数据，包含用户 ID、密码、创建时间等字段。
画面 14: 展示 Typora 中的文档，内容为 queryRecommendPublishList 方法的代码和测试结果截图。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
@GetMapping
public ResponseEntity<PageResult> queryPublishList(@RequestParam(value = "page", defaultValue = "1") Integer page,
                                                   @RequestParam(value = "pagesize", defaultValue = "10") Integer pageSize) {
    try {
        PageResult pageResult = this.movementsService.queryPublishList(page, pageSize);
        return ResponseEntity.ok(pageResult);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 3:
```java
for (Movements movements : movementsList) {
    for (UserInfo userInfo : userInfoList) {
        if (movements.getUserId().longValue() == userInfo.getUserId().longValue()) {
            movements.setTags(StringUtils.split(userInfo.getTags(), ','));
            movements.setNickname(userInfo.getNickName());
            movements.setGender(userInfo.getName().toLowerCase());
            movements.setAvatar(userInfo.getLogo());
            break;
        }
    }
}
pageResult.setItems(movementsList);
return pageResult;
```

画面 4:
```java
public PageResult queryPublishList(User user, Integer page, Integer pageSize) {
    PageResult pageResult = new PageResult();
    Long userId = null;
    if (user != null) {
        userId = user.getId();
    }
    PageInfo<Publish> pageInfo = this.quanZiApi.queryPublishList(userId, page, pageSize);
    pageResult.setCounts(0);
    pageResult.setPages(0);
    pageResult.setPageSize(pageSize);
    pageResult.setPage(page);
    List<Publish> records = pageInfo.getRecords();
    if (CollectionUtils.isEmpty(records)) {
        // 没有查询到动态数据
    }
    return pageResult;
}
```

画面 5:
```java
@GetMapping("/recommend")
public ResponseEntity<PageResult> queryRecommendPublishList(@RequestParam(value = "page", defaultValue = "1") Integer page,
                                                          @RequestParam(value = "pagesize", defaultValue = "10") Integer pageSize) {
    try {
        PageResult pageResult = this.movementsService.queryRecommendPublishList(page, pageSize);
        return ResponseEntity.ok(pageResult);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 6:
```java
private static final ProcessBuilder processBuilder = new ProcessBuilder();
private static final PageResult pageResult = new PageResult();
private static final List<Publish> records = pageInfo.getRecords();
```

画面 9:
```java
@GetMapping("/recommend")
public ResponseEntity<PageResult> queryPublishList(@RequestParam(value = "page", defaultValue = "1") Integer page,
                                                   @RequestParam(value = "pagesize", defaultValue = "10") Integer pageSize) {
    try {
        PageResult pageResult = this.movementsService.queryPublishList(page, pageSize);
        return ResponseEntity.ok(pageResult);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 13:
```sql
SELECT * FROM tb_user LIMIT 1,1000;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
