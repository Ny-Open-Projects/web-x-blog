# 画面线理解：09.圈子功能实现之动态信息评论（查询评论列表-dubbo服务）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\09.圈子功能实现之动态信息评论（查询评论列表-dubbo服务）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:24, 00:48, 01:43, 02:23, 02:47, 03:02, 03:40, 03:56, 04:21, 05:13, 05:26, 05:45, 06:13, 06:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:53:50

1) 这一组画面整体在讲什么（一句话）：
实现单条动态评论的分页查询功能，包括定义 Dubbo 接口和编写服务端实现代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程笔记中“1.4.1. 定义 dubbo 接口”部分，代码为：
```java
/**
 * 查询评论
 * @return
 */
PageInfo<Comment> queryCommentList(String publishId, Integer page, Integer pageSize);
```

画面 2: 展示 Mock 服务的测试界面，用于测试接口 `/comments`，Headers 中包含：
- Content-Type: application/json
- Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

画面 3: 展示项目结构，当前编辑的是 `QuanzApiImpl.java` 文件，其中包含方法：
```java
@Override
public Publish queryPublishById(String publishId) {
    return this.mongoTemplate.findById(new ObjectId(publishId), Publish.class);
}
```

画面 4: 编辑 `queryCommentList` 方法，光标在 `PageInfo<Comment>` 类型上，提示信息显示 `PageInfo` 类型的可用方法。

画面 5: 在 `queryCommentList` 方法中，光标位于 `PageInfo` 类型上，提示信息显示 `PageInfo` 类型的可用方法，包括 `setTotal`、`setPageSize`、`setPageNum` 等。

画面 6: 在 `queryCommentList` 方法中，开始编写代码，`this.mongoTemplate` 后面跟着 `new PageInfo<>()`。

画面 7: 在 `queryCommentList` 方法中，光标位于 `this.mongoTemplate` 后面，提示信息显示 `MongoTemplate` 类型的可用方法，包括 `find`、`query` 等。

画面 8: 在 `queryCommentList` 方法中，编写了查询语句：
```java
Query query = Query.query(Criteria.where("")).is(new ObjectId(publishId));
this.mongoTemplate.find(query, Comment.class);
```

画面 9: 在 `queryCommentList` 方法中，修改查询条件：
```java
Query query = Query.query(Criteria.where("publishId").is(new ObjectId(publishId))
    .and("commentType").is(2));
this.mongoTemplate.find(query, Comment.class);
```

画面 10: 在 `queryCommentList` 方法中，光标位于 `PageRequest` 类型上，提示信息显示 `PageRequest` 类型的可用方法。

画面 11: 在 `queryCommentList` 方法中，编写了 `PageRequest` 对象：
```java
PageRequest pageRequest = PageRequest.of(page - 1, pageSize, Sort.by(Sort.Order.asc("created")));
```

画面 12: 在 `queryCommentList` 方法中，编写了查询语句：
```java
Query query = Query.query(Criteria.where("publishId").is(new ObjectId(publishId))
    .and("commentType").is(2));
this.mongoTemplate.find(query, Comment.class);
```

画面 13: 在 `queryCommentList` 方法中，编写了查询语句：
```java
List<Comment> commentList = this.mongoTemplate.find(query, Comment.class);
PageInfo<Comment> pageInfo = new PageInfo<>();
pageInfo.setTotal(0);
pageInfo.setPageSize(pageSize);
pageInfo.setPageNum(page);
pageInfo.setRecords(commentList);
return pageInfo;
```

画面 14: 展示课程笔记中“1.4.2. 编写实现”部分，代码为：
```java
@Override
public PageInfo<Comment> queryCommentList(String publishId, Integer page, Integer pageSize) {
    PageRequest pageRequest = PageRequest.of(page - 1, pageSize, Sort.by(Sort.Order.asc("created")));
    Query query = Query.query(Criteria.where("publishId").is(new ObjectId(publishId))
        .and("commentType").is(2));
    this.mongoTemplate.find(query, Comment.class);
    PageInfo<Comment> pageInfo = new PageInfo<>();
    pageInfo.setTotal(0);
    pageInfo.setPageSize(pageSize);
    pageInfo.setPageNum(page);
    pageInfo.setRecords(commentList);
    return pageInfo;
}
```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
（已在上文要点中完整抄录）

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
（无 PPT 标题、架构图/流程图或表格数据）

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）
