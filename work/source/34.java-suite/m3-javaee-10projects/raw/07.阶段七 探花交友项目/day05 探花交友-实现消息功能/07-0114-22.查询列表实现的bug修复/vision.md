# 画面线理解：22.查询列表实现的bug修复

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\22.查询列表实现的bug修复_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:45, 01:22, 02:06, 02:24, 02:46, 03:19, 03:50, 04:04, 04:12, 05:00, 05:15, 05:29, 06:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:16:16

1) 这一组画面整体在讲如何在评论功能中实现评论的保存与关联逻辑，包括设置评论的父节点、用户ID、发布时间，并根据评论所属的发布内容（如视频、文章）动态设置发布者ID，同时展示分页查询评论列表的实现。

2) 按时间顺序列出每张画面的要点：
画面1：展示 `saveComment` 方法的代码，其中创建 Comment 对象并设置其属性，最后调用 `this.mongoTemplate.save(comment)` 保存评论。代码中包含异常捕获和返回布尔值。
画面2：代码与画面1相同，但高亮了 `comment.setIsParent(true)` 行，强调设置评论为父节点。
画面3：展示 `Comment` 类的定义，包含 `@Document(collection = "guanzi_comment")` 注解、`ObjectId id`、`String content`、`Long userId` 等字段，以及 `Boolean isParent` 字段。
画面4：在 `saveComment` 方法中，高亮了 `comment.setCreated(System.currentTimeMillis());` 行，显示设置评论创建时间。
画面5：高亮了 `this.mongoTemplate.find` 方法的调用，用于查询评论。
画面6：在 `saveComment` 方法中，高亮了 `Publish publish = this.mongoTemplate.findById(comment.getPublishId(), Publish.class);` 行，用于根据评论的发布ID查询发布内容。
画面7：高亮了 `if (null != publish)` 条件判断，用于检查发布内容是否存在。
画面8：在 `saveComment` 方法中，高亮了 `comment.setPublishUserId(publish.getUserId());` 行，用于设置评论的发布者ID。
画面9：高亮了 `Video video = this.mongoTemplate.findById(comment.getPublishId(), Video.class);` 行，用于查询视频对象。
画面10：在 `saveComment` 方法中，高亮了 `comment.setPublishUserId(video.getUserId());` 行，用于设置评论的发布者ID。
画面11：展示 `queryCommentListByUser` 方法的代码，用于分页查询用户评论列表。
画面12：高亮了 `pageInfo.setTotal(0);` 行，用于设置分页信息中的总记录数。
画面13：展示 Typora 文档中“8.3. 解决bug”部分，内容为“第一步：修改 Comment 对象，增加 publishUserId 字段”，并显示了 `Comment` 类的代码片段。
画面14：展示 Typora 文档中“9. 公告列表”部分，内容为“第三步：修改查询条件”，并显示了 `queryCommentListByUser` 方法的代码片段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public boolean saveComment(Long userId, String publishId, Integer type, String content) {
    try {
        Comment comment = new Comment();
        comment.setContent(content);
        comment.setIsParent(true);
        comment.setCommentType(type);
        comment.setPublishId(new ObjectId(publishId));
        comment.setUserId(userId);
        comment.setId(ObjectId.get());
        comment.setCreated(System.currentTimeMillis());
        this.mongoTemplate.save(comment);
        return true;
    } catch (Exception e) {
        e.printStackTrace();
    }
    return false;
}
```

画面2：
```java
public boolean saveComment(Long userId, String publishId, Integer type, String content) {
    try {
        Comment comment = new Comment();
        comment.setContent(content);
        comment.setIsParent(true);
        comment.setCommentType(type);
        comment.setPublishId(new ObjectId(publishId));
        comment.setUserId(userId);
        comment.setId(ObjectId.get());
        comment.setCreated(System.currentTimeMillis());
        this.mongoTemplate.save(comment);
        return true;
    } catch (Exception e) {
        e.printStackTrace();
    }
    return false;
}
```

画面3：
```java
@org.springframework.data.mongodb.core.mapping.Document(collection = "guanzi_comment")
public class Comment implements java.io.Serializable{
    private static final long serialVersionUID = -291788238125767614L;
    private ObjectId id;
    private ObjectId publishId; //发布id
    private Integer commentType; //评论类型，1-点赞，2-评论
    private String content; //评论内容
    private Long userId; //评论人
    private Boolean isParent = false; //是否为父节点，默认为子评论
    private ObjectId parentId; //父节点id
    private Long created; //发表时间
}
```

画面4：
```java
comment.setCreated(System.currentTimeMillis());
```

画面5：
```java
this.mongoTemplate.find
```

画面6：
```java
Publish publish = this.mongoTemplate.findById(comment.getPublishId(), Publish.class);
```

画面7：
```java
if (null != publish)
```

画面8：
```java
comment.setPublishUserId(publish.getUserId());
```

画面9：
```java
Video video = this.mongoTemplate.findById(comment.getPublishId(), Video.class);
```

画面10：
```java
comment.setPublishUserId(video.getUserId());
```

画面11：
```java
public List<Publish> queryPublishByPids(List<Long> pids) {
    Query query = Query.query(Criteria.where("pid").in(pids));
    return this.mongoTemplate.find(query, Publish.class);
}

@Override
public PageInfo<Comment> queryCommentListByUser(Long userId, Integer type, Integer page, Integer pageSize) {
    PageRequest pageRequest = PageRequest.of(page - 1, pageSize, Sort.by(Sort.Order.desc("created")));
    Query query = new Query(Criteria.where("publishUserId").is(userId)
            .and("commentType").is(type)).with(pageRequest);
    List<Comment> commentList = this.mongoTemplate.find(query, Comment.class);
    PageInfo<Comment> pageInfo = new PageInfo<>();
    pageInfo.setPageNum(page);
    pageInfo.setPageSize(pageSize);
    pageInfo.setRecords(commentList);
    pageInfo.setTotal(0); //提供总数
    return pageInfo;
}
```

画面12：
```java
pageInfo.setTotal(0); //提供总数
```

画面13：
```markdown
8.3. 解决bug
点赞、评论、喜欢列表应该显示该人对别人发布的消息做了操作之后显示的数据，所以查询条件是发布人的id作为查询条件。
第一步：修改 Comment 对象，增加 publishUserId 字段。
```

```java
package com.tanhua.dubbo.server.pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.mongodb.core.mapping.Document;
import java.util.Date;
// 评论表
@Data
@AllArgsConstructor
@NoArgsConstructor
@Document(collection = "guanzi_comment")
public class Comment implements java.io.Serializable{
    private static final long serialVersionUID = -291788238125767614L;
```

画面14：
```markdown
9. 公告列表
第三步：修改查询条件
```

```java
@Override
public PageInfo<Comment> queryCommentListByUser(Long userId, Integer type, Integer page, Integer pageSize) {
    PageRequest pageRequest = PageRequest.of(page - 1, pageSize, Sort.by(Sort.Order.desc("created")));
    Query query = new Query(Criteria.where("publishUserId").is(userId)
            .and("commentType").is(type)).with(pageRequest);
    List<Comment> commentList = this.mongoTemplate.find(query, Comment.class);
    PageInfo<Comment> pageInfo = new PageInfo<>();
    pageInfo.setPageNum(page);
    pageInfo.setPageSize(pageSize);
    pageInfo.setRecords(commentList);
    pageInfo.setTotal(0); //提供总数
    return pageInfo;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面13：PPT标题为“8.3. 解决bug”，内容为“点赞、评论、喜欢列表应该显示该人对别人发布的消息做了操作之后显示的数据，所以查询条件是发布人的id作为查询条件”，并列出“第一步：修改 Comment 对象，增加 publishUserId 字段”。
画面14：PPT标题为“9. 公告列表”，内容为“第三步：修改查询条件”。

5) 不要评价画面美观，不要输出与课程无关的内容。
