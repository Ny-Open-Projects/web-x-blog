# 画面线理解：02.我的喜欢之喜欢数统计（dubbo服务实现）

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\02.我的喜欢之喜欢数统计（dubbo服务实现）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 02:46, 04:43, 05:30, 06:45, 07:30, 08:09, 08:49, 09:17, 09:58, 10:25, 11:24, 12:45, 13:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:36:37

1) 这一组画面整体在讲什么（一句话）：
演示如何在“我的喜欢”功能中，通过 MongoDB 实现用户点赞、查询喜欢列表、查询喜欢我的人以及统计喜欢数等核心业务逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示“我的喜欢”功能的 UI 界面截图，用于说明业务场景。
画面 2: 展示 `UserLikeApi.java` 接口定义，包含 `saveUserLike` 和 `isMutualLike` 方法。
画面 3: 展示 `UserLikeApiImpl.java` 中 `deleteTemplate` 方法的实现，用于删除喜欢记录。
画面 4: 展示 `UserLikeApiImpl.java` 中 `queryLikeCount` 方法的实现，用于查询喜欢我的人数量。
画面 5: 展示 `UserLikeApiImpl.java` 中 `queryEachLikeCount` 方法的实现，用于查询喜欢列表。
画面 6: 展示 `UserLikeApiImpl.java` 中 `queryEachLikeCount` 方法中，将喜欢列表中的用户 ID 收集到 `likeUserIds` 列表。
画面 7: 展示 `UserLikeApiImpl.java` 中 `queryEachLikeCount` 方法中，构建查询条件 `query2`，用于查询喜欢我的人。
画面 8: 展示 `UserLikeApiImpl.java` 中 `queryLikeCount` 方法中，调用 `this.mongoTemplate.count` 查询喜欢我的人数量。
画面 9: 展示 `UserLikeApiImpl.java` 中 `queryFanCount` 方法的实现，用于查询喜欢我的人数量。
画面 10: 展示 `day11 讲义.md` 文档中，`1.3. 查询统计数据` 和 `1.3.1. mock接口` 的章节标题。
画面 11: 展示 `TestUserLikeApiImpl.java` 中 `testSave` 和 `testQueryCounts` 测试方法的代码。
画面 12: 展示 MongoDB 数据库中 `user_like` 集合的数据，包含多个点赞记录。
画面 13: 展示 `TestUserLikeApiImpl.java` 中 `testQueryCounts` 方法的执行结果，输出了查询结果。
画面 14: 展示 `UserLikeApiImpl.java` 中 `queryLikeCount` 方法的完整实现，包含 `queryEachLikeCount` 和 `queryFanCount` 的调用。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
package com.tanhua.dubbo.server.api;

public interface UserLikeApi {
    /**
     * 保存喜欢
     * @param userId
     * @param likeUserId
     * @return
     */
    String saveUserLike(Long userId, Long likeUserId);

    /**
     * 判断是否互相关注
     * @param userId
     * @param likeUserId
     * @return
     */
    Boolean isMutualLike(Long userId, Long likeUserId);
}
```

画面 3:
```java
public class UserLikeApiImpl implements UserLikeApi {
    @Override
    public Long queryEachLikeCount(Long userId) {
        // 查询我的喜欢列表
        Query query = Query.query(Criteria.where("userId").is(userId));
        List<UserLike> userLikes = this.mongoTemplate.find(query, UserLike.class);
        // 收集到我的喜欢列表中的用户id（对方）
        List<Long> likeUserIds = new ArrayList<>();
        for (UserLike userLike : userLikes) {
            likeUserIds.add(userLike.getLikeUserId());
        }
        // 在我的喜欢列表范围内，查询喜欢我的人有哪些
        Query query2 = Query.query(Criteria.where("userId").in(likeUserIds));
        return this.mongoTemplate.count(query2, UserLike.class);
    }
}
```

画面 4:
```java
@Override
public Long queryLikeCount(Long userId) {
    return this.mongoTemplate.count(Query.query(Criteria.where("userId").is(userId)), UserLike.class);
}
```

画面 5:
```java
@Override
public Long queryFanCount(Long userId) {
    return this.mongoTemplate.count(Query.query(Criteria.where("likeUserId").is(userId)), UserLike.class);
}
```

画面 11:
```java
@Test
public void testSave() {
    this.userLikeApi.saveUserLike(userId: 1L, likeUserId: 21L);
    this.userLikeApi.saveUserLike(userId: 1L, likeUserId: 3L);
    this.userLikeApi.saveUserLike(userId: 1L, likeUserId: 15L);
    this.userLikeApi.saveUserLike(userId: 1L, likeUserId: 4L);
    this.userLikeApi.saveUserLike(userId: 1L, likeUserId: 11L);
    this.userLikeApi.saveUserLike(userId: 1L, likeUserId: 11L);
}

@Test
public void testQueryCounts() {
    System.out.println(this.userLikeApi.queryEachLikeCount(userId: 1L));
    System.out.println(this.userLikeApi.queryFanCount(userId: 1L));
    System.out.println(this.userLikeApi.queryLikeCount(userId: 1L));
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
