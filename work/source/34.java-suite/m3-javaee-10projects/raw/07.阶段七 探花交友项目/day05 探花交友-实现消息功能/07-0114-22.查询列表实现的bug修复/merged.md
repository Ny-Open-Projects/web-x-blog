# 22.查询列表实现的bug修复

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\22.查询列表实现的bug修复_【海量资源尽在 666java.com】.mp4
- 时长 6分38秒（音频 399s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢,我们来说一个问题啊就是前面我们所实现的这个列表啊就是点赞啊,或者说我们这个评论列表啊其实我们这个实现的是稍微有点问题的就是逻辑会有点问题啊就是说我们其实在这个位置所要实现的一个这个是什么呢,是我自己所发布的一些动态被别人点赞了之后给我发送的一个消息
[00:27] 那么我在这块能够看到别人的一个操作而我们刚刚这个实现的是刚好反过来是查询我自己的那个操作所以说这块是有点问题的那我们来把这个一起来调一下这个逻辑就可以了那么这个还是比较简单的可以去解决掉的那么首先我们先来回顾一下之前我们的一个comment就是我们这个评论这张表那么在这个表里面其实我们只记录一个评论人
[00:57] 我们并没有去记录这个就是发布人那么如果说那么我们在这个位置那么我们要去查询的时候一定是查询的是发布的发布人的作为一个条件去做查询这个动态那么才能够去把它查询出来不能去
[01:17] 查询的是评论人啊所以说这块是有问题的就说那么我们这块是缺少一个我们的一个publish一个user id啊那我们来去补一个这个id啊那我们去写一个叫做publish user id啊那么我们去写给他这个叫什么呢就是发布人的用户啊
[01:40] 用户ID那么这个要注意要发布人的用户ID那么有了它之后我们就需要在我们前面去圈子中有一个save comment因为无论是点赞还是喜欢那么都是去使用了save comment的方法所以说我们核心逻辑在这个里面编写就可以了那么下面我们就可以通过我们的当然目的是需要去set一个
[02:08] publish your id去做一个设置但是这个id呢我们现在根本不知道啊我们只能去通过一个publish id去做查询那么这个时候呢我们怎么查呢我们通过一个mongo template叫fenderfender by id啊那么我们把这个id呢传递过去那么就是通过这个commentcomment然后呢点get那应该是by id啊来一个comment点
[02:36] get a publish id作为一个这个条件对吧然后呢还有一个是publish.class然后去做一个查询那么要注意这个时候呢我们的查询呢也是有问题的那么我们这样查询仅仅是针对于什么呢我们圈子中的一些这个动态可能可以查询对吧但是呢要注意的是我们点赞呢喜欢的这个逻辑啊对于我们的小视频同样的也是有效的所以说呢
[03:05] 我们也就说我们这个小视频跟我们的圈子他就使用的这个点赞啊喜欢的逻辑呢是同一套逻辑对吧所以说呢在这块我们不能只是去查询他我们还需要做一个判断啊那么如果空如果他如果空不等于这个publish的话OK那我们就直接去使用他就做一个保存就可以了那么设置一个他
[03:33] get什么呢url这样的话就ok那么我们再做一个else if那么如果如果是当然我们还应该这样去写那么如果是它不等它等于空的话那我们就需要去查询谁呢查询我们的这个小视频了然后呢我们去查询我们的这个小视频的这张表然后呢我们再去做一个判断
[04:00] 如果空不等于我们的一个这个video的话那我们就把他的这个发布的人呢给他丢进去然后呢就video.get什么呢url id这个大家能够理解吧那么如果说依然为空的话就代表着我们这个就理论上就目前我们来看的话他不应该出现这种情况那么如果真的出现这种情况那就意味着什么呢这个publish这个这个id啊
[04:29] 它呢是非法传入的一个ID或者说我们新增了一些其他逻辑之后啊产生了这个ID那么我们就给它设置为none就可以了那么当然我们这块你不设置它本身也是一个none啊OK好那么这样的话呢我们是不是就实现了一个保存它的一个发布人的一个ID啊这个就是我们的设置啊发布人的ID啊发布人的ID然后呢接下来呢我们来看一下
[04:56] 那么在我们刚刚所实现的这个查询列表中啊那么我们的这个查询的这个条件啊要注意那么查询的这个条件呢就不能使用这个UraID了那么就要使用谁呢使用我们刚刚所写这个PublisUraID那么要使用它啊才能够去做一个查询了好那么接下来呢我们把我们这个double呢我们服务呢重启一下啊好那么下面呢我们把我们的这个
[05:23] 讲义啊那我们来调整一下好那么来看一下这个讲义啊那么在讲义中呢我们也写了一个这个叫做解决bug啊那么我们的这个点赞啊评论喜欢这个列表呢是应该是别人对我发布的信息做了操作之后的显示的数据啊并不是说我对别人的操作所以说我们之前这个的逻辑是有点问题的
[05:46] 那么所以说我们这个查询条件呢应该是发布人的ID作为一个条件去做查询而并不是我操作人作为一个查询条件啊这一点要注意那我们修改这个bug呢需要三步操作第一步呢就是我们给这个comment这个对象啊去增加一个publish your ID这个字段啊我们去做这样的一个增加那第二步呢就是在我们保存comment的这个逻辑中啊去增加一个设置发布人的ID的这样的一个逻辑啊
[06:16] 然后呢我们就可以去第三步啊去修改它的一个查询条件啊这样的话呢我们就搞定了啊OK好那么接下来呢我们就可以针对于我们刚刚的一个这个修改呢我们做一下这个测试啊OK好那么关于我们这个bug的一个这个修复呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

