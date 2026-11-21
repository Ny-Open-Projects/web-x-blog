# 画面线理解：04.我的喜欢之喜欢数列表（dubbo服务实现）

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\04.我的喜欢之喜欢数列表（dubbo服务实现）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 01:32, 02:46, 04:02, 04:57, 06:06, 07:07, 08:01, 09:09, 10:15, 10:58, 12:09, 13:21, 14:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:38:31

1) 这一组画面整体在讲：演示如何在 Dubbo 服务中实现用户点赞列表、粉丝列表和访客列表的分页查询功能，涉及 MongoDB 的查询操作和 PageInfo 分页封装。

2) 按时间顺序列出每张画面的要点：
画面1：显示 Chrome 浏览器的下载页面，包含三个下载文件：DdHm...mp4（2019年10月30日）、apowermirror-setup-bd.exe（2019年10月30日）、DesktopDemo.3.6.0.win.setup.zip（2019年10月28日）。
画面2：桌面背景为黑马程序员/博学谷的水印，显示一个手机应用界面，其中包含“ApowerMirror”字样，暗示即将安装或演示该软件。
画面3：IDE 中显示项目结构，当前选中 `UserLikeApi.java` 文件，其中定义了 `queryEachLikeList` 和 `queryFanList` 方法。
画面4：IDE 中显示 `UserLikeApiImpl.java` 文件，代码中包含 `queryLikeCount`、`queryFanCount` 和 `queryEachLikeList` 方法的实现，使用了 `MongoTemplate`。
画面5：IDE 中显示 `UserLikeApiImpl.java` 文件，代码中包含 `queryEachLikeList` 方法的实现，使用了 `MongoTemplate` 和 `PageInfo`。
画面6：IDE 中显示 `UserLikeApiImpl.java` 文件，代码中包含 `queryEachLikeList` 方法的实现，使用了 `PageRequest` 和 `Sort`。
画面7：IDE 中显示 `UserLikeApiImpl.java` 文件，代码中光标位于 `PageInfo` 类的定义处，下方有自动补全提示。
画面8：IDE 中显示 `UserLikeApiImpl.java` 文件，代码中 `queryEachLikeList` 方法的实现，使用了 `PageRequest` 和 `Sort`。
画面9：IDE 中显示 `UserLikeApiImpl.java` 文件，代码中 `queryLikeList` 方法的实现，使用了 `PageRequest` 和 `Sort`。
画面10：IDE 中显示 `TestUserLikeApiImpl.java` 文件，代码中包含 `testQueryCounts` 和 `testQueryList` 方法，用于测试 `UserLikeApi`。
画面11：Typora 编辑器中显示 `day11 详义.md` 文件，内容为“1.4.3. UserLikeApiImpl”部分，包含 `queryLikeList` 方法的伪代码。
画面12：IDE 中显示 `VisitorsApiImpl.java` 文件，代码中包含 `topVisitor` 方法的实现，使用了 `MongoTemplate`。
画面13：IDE 中显示 `VisitorsApiImpl.java` 文件，代码中 `topVisitor` 方法的实现，使用了 `PageInfo`。
画面14：Typora 编辑器中显示 `day11 详义.md` 文件，内容为“1.4.4. VisitorsApi”部分，包含 `topVisitor` 方法的伪代码。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面3：
```java
nfo<UserLike> queryEachLikeList(Long userId, Integer page, Integer pageSize);
nfo<UserLike> queryFanList(Long userId, Integer page, Integer pageSize);
```

画面4：
```java
@Override
public Long queryLikeCount(Long userId) {
    return this.mongoTemplate.count(Query.query(Criteria.where("userId").is(userId)), UserLike.class);
}

@Override
public long queryFanCount(Long userId) {
    return this.mongoTemplate.count(Query.query(Criteria.where("likeUserId").is(userId)), UserLike.class);
}

@Override
public PageInfo<UserLike> queryEachLikeList(Long userId, Integer page, Integer pageSize) {
```

画面5：
```java
@Override
public PageInfo<UserLike> queryEachLikeList(Long userId, Integer page, Integer pageSize) {
    // 查询我的喜欢列表
    Query query = Query.query(Criteria.where("userId").is(userId));
    List<UserLike> userLikes = this.mongoTemplate.find(query, UserLike.class);

    // 收集到我的喜欢列表中的 userId（对方）
    List<Long> likeUserIds = new ArrayList<>();
    for (UserLike userLike : userLikes) {
        likeUserIds.add(userLike.getLikeUserId());
    }

    // 在我的喜欢列表范围内，查询喜欢我的人有哪些
    Query query2 = Query.query(Criteria.where("userId").in(likeUserIds).and("likeUserId").is(userId);
    List<UserLike> userLikeList = this.mongoTemplate.find(query2, UserLike.class);

    PageInfo<UserLike> pageInfo = new PageInfo<>();
    pageInfo.setPageNum(page);
    pageInfo.setPageSize(pageSize);
    pageInfo.setTotal(0); // 暂时不提供
    pageInfo.setRecords(userLikeList);

    return pageInfo;
}
```

画面6：
```java
@Override
public PageInfo<UserLike> queryEachLikeList(Long userId, Integer page, Integer pageSize) {
    // 查询我的喜欢列表
    Query query = Query.query(Criteria.where("userId").is(userId));
    List<UserLike> userLikes = this.mongoTemplate.find(query, UserLike.class);

    // 收集到我的喜欢列表中的 userId（对方）
    List<Long> likeUserIds = new ArrayList<>();
    for (UserLike userLike : userLikes) {
        likeUserIds.add(userLike.getLikeUserId());
    }

    // 在我的喜欢列表范围内，查询喜欢我的人有哪些
    Query query2 = Query.query(Criteria.where("userId").in(likeUserIds).and("likeUserId").is(userId);
    List<UserLike> userLikeList = this.mongoTemplate.find(query2, UserLike.class);

    PageInfo<UserLike> pageInfo = new PageInfo<>();
    pageInfo.setPageNum(page);
    pageInfo.setPageSize(pageSize);
    pageInfo.setTotal(0); // 暂时不提供
    pageInfo.setRecords(userLikeList);

    return pageInfo;
}
```

画面7：
```java
private PageInfo<UserLike> queryList(Query query, Integer page, Integer pageSize) {
    PageRequest pageRequest = PageRequest.of(page - 1, pageSize, Sort.by(Sort.Order.desc("created")));
    query.with(pageRequest);
    List<UserLike> userLikeList = this.mongoTemplate.find(query, UserLike.class);

    PageInfo<UserLike> pageInfo = new PageInfo<>();
    pageInfo.setRecords(userLikeList);
    pageInfo.setTotal(0); // 暂时不提供
    pageInfo.setPageNum(page);
    pageInfo.setPageSize(pageSize);

    return pageInfo;
}
```

画面8：
```java
@Override
public PageInfo<UserLike> queryEachLikeList(Long userId, Integer page, Integer pageSize) {
    // 查询我的喜欢列表
    Query query = Query.query(Criteria.where("userId").is(userId));
    List<UserLike> userLikes = this.mongoTemplate.find(query, UserLike.class);

    // 收集到我的喜欢列表中的 userId（对方）
    List<Long> likeUserIds = new ArrayList<>();
    for (UserLike userLike : userLikes) {
        likeUserIds.add(userLike.getLikeUserId());
    }

    // 在我的喜欢列表范围内，查询喜欢我的人有哪些
    Query query2 = Query.query(Criteria.where("userId").in(likeUserIds).and("likeUserId").is(userId);
    List<UserLike> userLikeList = this.mongoTemplate.find(query2, UserLike.class);

    PageInfo<UserLike> pageInfo = new PageInfo<>();
    pageInfo.setPageNum(page);
    pageInfo.setPageSize(pageSize);
    pageInfo.setTotal(0); // 暂时不提供
    pageInfo.setRecords(userLikeList);

    return pageInfo;
}
```

画面9：
```java
@Override
public PageInfo<UserLike> queryLikeList(Query query, Integer page, Integer pageSize) {
    PageRequest pageRequest = PageRequest.of(page - 1, pageSize, Sort.by(Sort.Order.desc("created")));
    query.with(pageRequest);
    List<UserLike> userLikeList = this.mongoTemplate.find(query, UserLike.class);

    PageInfo<UserLike> pageInfo = new PageInfo<>();
    pageInfo.setRecords(userLikeList);
    pageInfo.setTotal(0); // 暂时不提供
    pageInfo.setPageNum(page);
    pageInfo.setPageSize(pageSize);

    return pageInfo;
}
```

画面10：
```java
@Test
void testQueryCounts() {
    this.userLikeApi.saveUserLike(userid: 51, likeUserId: 11);
    this.userLikeApi.saveUserLike(userid: 61, likeUserId: 11);
    System.out.println(this.userLikeApi.queryEachLikeCount(userid: 11));
    System.out.println(this.userLikeApi.queryFanCount(userid: 11));
}

@Test
void testQueryList() {
    PageInfo<UserLike> pageinfo = this.userLikeApi.queryEachLikeList(11, 1, 10);
}
```

画面11：
```markdown
1.4.3. UserLikeApiImpl
    public PageInfo<UserLike> queryLikeList(Long userId, Integer page, Integer pageSize) {
        Query query = Query.query(Criteria.where("userId").is(userId));
        return this.queryList(query, page, pageSize);
    }

    private PageInfo<UserLike> queryList(Query query, Integer page, Integer pageSize) {
        PageRequest pageRequest = PageRequest.of(page - 1, pageSize, Sort.by(Sort.Order.desc("created")));
        query.with(pageRequest);
        List<UserLike> userLikeList = this.mongoTemplate.find(query, UserLike.class);
