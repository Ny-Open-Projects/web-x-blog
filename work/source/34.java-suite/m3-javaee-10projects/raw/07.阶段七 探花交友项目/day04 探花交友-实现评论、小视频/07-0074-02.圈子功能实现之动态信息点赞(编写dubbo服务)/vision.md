# 画面线理解：02.圈子功能实现之动态信息点赞（编写dubbo服务）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\02.圈子功能实现之动态信息点赞（编写dubbo服务）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:16, 02:04, 04:19, 05:22, 06:23, 06:49, 07:49, 08:52, 10:34, 11:25, 12:56, 13:40, 14:48, 16:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:48:45

1) 这一组画面整体在讲什么（一句话）：
在 Dubbo 服务接口中定义评论相关的操作，包括点赞、取消点赞、保存评论、删除评论等方法，并在实现类中编写具体的业务逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了评论模块的接口定义，包括点赞、取消点赞、保存评论、删除评论等方法。
画面 2: 展示了接口中定义的查询评论列表方法和保存点赞方法。
画面 3: 展示了接口中定义的删除评论和保存喜欢方法。
画面 4: 展示了实现类中对删除评论和保存喜欢方法的初步实现（返回 false）。
画面 5: 展示了实现类中对保存评论方法的初步实现（创建 Comment 对象并设置属性）。
画面 6: 展示了实现类中对保存评论方法的继续实现（设置评论类型、父节点等属性）。
画面 7: 展示了实现类中对保存评论方法的继续实现（设置评论内容、创建时间等属性）。
画面 8: 展示了实现类中对保存评论方法的继续实现（调用 saveComment 方法保存评论）。
画面 9: 展示了实现类中对保存评论方法的继续实现（设置评论类型、父节点等属性）。
画面 10: 展示了 Comment 实体类的定义，包括字段和注解。
画面 11: 展示了实现类中对保存点赞方法的实现（查询数据库判断是否已点赞）。
画面 12: 展示了实现类中对保存点赞方法的继续实现（查询数据库判断是否已点赞）。
画面 13: 展示了实现类中对保存点赞方法的继续实现（保存评论到数据库）。
画面 14: 展示了实现类中对保存评论方法的完整实现（设置评论属性、保存到数据库、异常处理）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.tanhua.dubbo.server.api;

import com.tanhua.dubbo.server.pojo.Publish;
import com.tanhua.dubbo.server.vo.PageInfo;

public interface QuanziApi {
    /**
     * 左右动态
     * @param publish
     * @return
     */
    boolean savePublish(Publish publish);

    /**
     * 查询动态
     * @param userId
     * @param page
     * @param pageSize
     * @return
     */
    PageInfo<Publish> queryPublishList(Long userId, Integer page, Integer pageSize);

    /**
     * 点赞
     * @param userId
     * @param publishId
     * @return
     */
    boolean saveLikeComment(Long userId, String publishId);

    /**
     * 取消点赞、喜欢等
     * @param userId
     * @param publishId
     * @param commentType
     * @return
     */
    boolean removeComment(Long userId, String publishId, Integer commentType);

    /**
     * 喜欢
     * @param userId
     * @param publishId
     * @return
     */
    boolean saveLoveComment(Long userId, String publishId);

    /**
     * 保存评论
     * @param userId
     * @param publishId
     * @param type
     * @param content
     * @return
     */
    boolean saveComment(Long userId, String publishId, Integer type, String content);

    /**
     * 查询评论数
     * @param publishId
     * @param type
     * @return
     */
    Long queryCommentCount(String publishId, Integer type);
}
```

画面 2:
```java
/**
 * 查询好友动态
 * @param userId
 * @param page
 * @param pageSize
 * @return
 */
PageInfo<Publish> queryPublishList(Long userId, Integer page, Integer pageSize);

/**
 * 点赞
 * @param userId
 * @param publishId
 * @return
 */
boolean saveLikeComment(Long userId, String publishId);
```

画面 3:
```java
/**
 * 取消点赞、喜欢等
 * @param userId
 * @param publishId
 * @param commentType
 * @return
 */
boolean removeComment(Long userId, String publishId, Integer commentType);

/**
 * 喜欢
 * @param userId
 * @param publishId
 * @return
 */
boolean saveLoveComment(Long userId, String publishId);

/**
 * 保存评论
 * @param userId
 * @param publishId
 * @param type
 * @param content
 * @return
 */
boolean saveComment(Long userId, String publishId, Integer type, String content);
```

画面 4:
```java
@Override
public boolean removeComment(Long userId, String publishId, Integer commentType) {
    return false;
}

@Override
public boolean saveLoveComment(Long userId, String publishId) {
    return false;
}

@Override
public boolean saveComment(Long userId, String publishId, Integer type, String content) {
    Comment comment = new Comment();
    comment.setContent(content);
    comment.setPublishId(new ObjectId(publishId));
    comment.setCommentType(type);
    comment.setCreated(System.currentTimeMillis());
    comment.setParent(true);
    comment.setUserId(userId);
    return false;
}
```

画面 5:
```java
@Override
public boolean saveLoveComment(Long userId, String publishId) {
    return false;
}

@Override
public boolean removeComment(Long userId, String publishId, Integer commentType) {
    return false;
}

@Override
public boolean saveComment(Long userId, String publishId, Integer type, String content) {
    try {
        Comment comment = new Comment();
        comment.setContent(content);
        comment.setPublishId(new ObjectId(publishId));
        comment.setCommentType(type);
        comment.setCreated(System.currentTimeMillis());
        comment.setParent(true);
        comment.setUserId(userId);
        return false;
    } catch (Exception e) {
        e.printStackTrace();
    }
    return false;
}
```

画面 6:
```java
@Override
public boolean saveLoveComment(Long userId, String publishId) {
    return false;
}

@Override
public boolean removeComment(Long userId, String publishId, Integer commentType) {
    return false;
}

@Override
public boolean saveComment(Long userId, String publishId, Integer type, String content) {
    try {
        Comment comment = new Comment();
        comment.setContent(content);
        comment.setPublishId(new ObjectId(publishId));
        comment.setCommentType(type);
        comment.setCreated(System.currentTimeMillis());
        comment.setParent(true);
        comment.setUserId(userId);
        return false;
    } catch (Exception e) {
        e.printStackTrace();
    }
    return false;
}
```

画面 7:
```java
@Override
public boolean saveLikeComment(Long userId, String publishId) {
    return false;
}

@Override
public boolean removeComment(Long userId, String publishId, Integer commentType) {
    return false;
}

@Override
public boolean saveComment(Long userId, String publishId, Integer type, String content) {
    try {
        Comment comment = new Comment();
        comment.setContent(content);
        comment.setPublishId(new ObjectId(publishId));
        comment.setCommentType(type);
        comment.setCreated(System.currentTimeMillis());
        comment.setParent(true);
        comment.setUserId(userId);
        return false;
    } catch (Exception e) {
        e.printStackTrace();
    }
    return false;
}
```

画面 8:
```java
@Override
public boolean saveLikeComment(Long userId, String publishId) {
    return false;
}

@Override
public boolean removeComment(Long userId, String publishId, Integer commentType) {
    return false;
}

@Override
public boolean saveComment(Long userId, String publishId, Integer type, String content) {
    try {
        Comment comment = new Comment();
        comment.setContent(content);
        comment.setPublishId(new ObjectId(publishId));
        comment.setCommentType(type);
        comment.setCreated(System.currentTimeMillis());
        comment.setParent(true);
        comment.setUserId(userId);
        return false;
    } catch (Exception e) {
        e.printStackTrace();
    }
    return false;
}
```

画面 9:
```java
@Override
public boolean saveLikeComment(Long userId, String publishId) {
    //判断是否已经点赞，如果已经点赞就返回
    Criteria criteria = Criteria.where("userId").is(userId)
            .and("publishId").is(new ObjectId(publishId))
            .and("commentType").is(1);
    Query query = Query.query(criteria);
    long count = this.mongoTemplate.count(query, Comment.class);
    if (count > 0) {
        return false;
    }
    return this.saveComment(userId, publishId, type, content);
}
```

画面 10:
```java
/**
 * 评论表
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Document(collection = "quanzi_comment")
public class Comment implements java.io.Serializable{
    private static final long serialVersionUID = -291788258125767614L;

    private ObjectId id;
    private ObjectId publishId; //发布id
    private Integer commentType; //评论类型，1-点赞，2-评论，3-喜欢
    private String content; //评论内容
    private Long userId; //评论人
    private Boolean isParent = false; //是否为父节点，转(默认为否)
    private ObjectId parentId; //父
