# 02.圈子功能实现之动态信息点赞（编写dubbo服务）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\02.圈子功能实现之动态信息点赞（编写dubbo服务）_【海量资源尽在 666java.com】.mp4
- 时长 16分38秒（音频 999s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下我们圈子中的评论啊这个功能那么这个评论功能呢我们可以分为有这三个功能啊那么第一个呢是点赞啊第二个呢是喜欢然后第三个呢是评论那么其实呢我们可以把这三种这个操作啊都可以去理解为这是用户对我们这个动态信息的一个评论当然这个评论是一个
[00:29] 广义的这样的一个评论了那么点赞啊它其实也是属于评论只是说它换了一种形式它没有去输入这个文字啊那么喜欢呢其实也是一样那么评论呢是我可以去写一些我的一些这个想法我的一些观点啊写进去那么这个呢是评论所以说呢我们可以把它理解成的是一个啊这样的功能那么这样的话呢我们这个
[00:53] 就容易去做实现了那么所以说我们把它做这样的一个理解是我们去实现这个功能的一个前提那么下面我们分别来看一下这三个功能的实现那么首先第一个呢是点赞这个功能那么点赞呢就是我们对一个这个比如说我们的朋友圈呀或者圈子呀这种圈子中的一些
[01:19] 动态信息呢我们去可以去点赞一下就是代表着你比较喜欢这个动态啊好那么下面我们就来看一下这个功能的实现那么首先呢我们来看一下我们定义这个double这个接口那么我们需要定义这么几个接口啊那么我们就把这个来拷贝一下那么我们来一起来看一下我们需要去实现的这么几个需要实现这么几个这个接口
[01:46] 然后我们找到我们这个double的这个interface然后我们去找到这个里面的API然后找到它然后我们就把它丢到下面来来看一下这么几个方法那么首先第一个是可以看到这个是什么点赞对吧叫做什么呢sale like comment然后有两个参数一个就是usual ID哪个用户给哪个动态做一个点赞
[02:15] 然后呢下面这个呢是做取消点赞啊或者说取消这个喜欢那么有参数呢有这个什么UID然后呢public ID还有什么呢comment IDcomment type那么这个是用户啊这个是我们的动态的ID然后呢这个是我们的这comment type就是类型
[02:38] 那么在前面呢我们其实知道啊我们这个comment呢它呢是有三个类型的对吧那么这个id为一呢是点赞那么id为二呢是评论id为三呢是喜欢所以说呢我们要去跟这个comment type去做一个这样的一个完成那么我们还找到前面这个圈子这个API然后呢传递这个type那么就可以去实现你是在
[03:02] 取消这个点赞呢还是在取消这个喜欢啊根据他的来做一个区分那么下面我们来看一下这个喜欢那么喜欢的同样也是呢传递一个用户id和传递一个动态这个id那么就可以去喜欢这个动态信息了然后呢下面的这个方法呢是用于什么呢去保存我们这个评论信息啊保存这个评论信息那么有这么几个参数那么第一个呢是用户id
[03:31] 还有什么呢是叫public ID还有type还有我们的这contact的内容那么就是我们这个用户啊给这个动态去发表一个这个评论啊这个传递一个type然后呢它的一个内容是什么所以说呢有这么几个参数然后呢下面呢最后一个这个方法呢是做一个查询评论的一个数量那么我们去可以去查询一下比如说某一个这个动态信息的
[04:00] 它的一个类型的啊这样的一些这个数量比如说点赞数呢还是一些这个喜欢数呢或者说评论数啊那么最后返回呢是一个楞形的啊这样的一个数值那么我们是不是在接口中已经就完成了这个接口的一个定义那么接下来呢我们将
[04:20] 一个一个来实现这几个服务那么首先我们先来找到我们API的一个template然后IMPL然后在这个里面我们去做一个实现那么我们去实现这个方法那么这总共要实现有五个方法好那么我们点击实现好那么我们接下来将一个一个来实现这些方法这个是我们去实现的什么就是
[04:47] 我们保存我们的这个like那就是我们这个点赞然后呢love呢是喜欢那么下面这个是我们保存评论那么首先我们应该实现是这个方法因为其实这个点赞和评论呢只是这个type不同对吧所以说呢我们先应该实现的是这个方法好那我们来看一下怎么样去做一个实现那么首先呢我们其实应该去定义一个这个comment这样的一个对象
[05:17] 然后呢我们去new一个这个对象好那我们来给他设置一些相关的值比如说我们设置contact内容那就是contact值然后呢我们继续设置什么呢这个is parent那么is parent呢就是说回复呢是不是要回去要去做一个这个比如说
[05:38] 一楼的可以回复二楼回复一楼三楼回复二楼这样的回复那我们暂时呢不实现这样的功能所以我们设置为easyparent都设置为true那就是都是这个复杰点那么还有什么呢我们继续往下面看那么还有是这个就是comment type那么就是我们所传入这个type了然后呢我们再去添加一个比如说这个叫
[06:04] 什么呢publish id那么我们这个呢需要去new一个object id然后呢把这个publishpublish id传递过去因为我们传递这个publish id呢它是一个字幕创我们所需要的是一个object id这样的一种类型所以呢需要去new一个对象去转换一下然后呢我们下面来看一下还有这个叫什么呢就是url id那就是我们传入这个url id了
[06:32] 然后呢我们再来写一个叫做ID那么我们就使用object id.get来获取到一个新的一个ID然后呢继续往下面看然后呢还有谁呢还有是这个就是叫created就是创建时间那我们就使用我们系统的当前的时间时间戳就可以了然后呢去set去设置一个还有谁呢叫就是pilot id
[06:59] 那么parent id呢我们现在呢它就没有啊这个parent id那我们就不做一个设置了啊就空了就好了呃然后呢我们需要把它去我们去做一个呃try cat处理吧然后呢是如果出现了异常的话那我们就return false那么如果啊如果正常执行的话那么就return true啊当然了我们还没有去做保存对吧
[07:25] 我们需要通过this.mongo.template.做一个save这个操作那么save呢我们直接去保存这个对象就可以了因为所有用户的评论呢都会写到这张表里面来所以我们只需要只需要去写一张表啊就可以了不需要去指定这个表明了那么这个就是我们保存我们的一个
[07:48] 这个评论那么接下来呢我们来看一下我们这个点赞啊它呢是该如何去做一个实现那么我们其实直接去调用我们下面这个方法就可以了对不对调用race.salecomment然后呢传递这么几个参数那么第一个呢就是这个user id那么第二个这个参数我们来看一下啊第二个参数呢是叫什么呢public idtype
[08:13] 那么我们来看一下那publish id那么把这个publish id呢也传递过去还有呢type注意来看一下啊那么我们这个comment这个type那么点赞呢id是1啊所以说在这个位置啊那我们就传递这个1啊就可以了然后呢第四个参数呢是这个contact就是内容那么我们点赞呢是没有内容的
[08:37] 所以呢把它设置为none就可以了那么这个是不是就非常的简单了然后呢我们再来看一下那么下面的这个保存我们这个喜欢那么这个就变得更简单了对吧直接把它改成几呢改成3就可以了那么为什么是3呢我们来看一下那么comment它的这个类型呢二次评论3呢是喜欢所以呢在这个位置啊我们需要把它设置为呢是一个这个3
[09:04] 好那我们来看一下那么但是大家可以去思考一下就是说那么其实我们在这个位置还是缺少一点逻辑的就是说用户在点赞之后能不能够再次点赞就是说比如说我一个用户对一个这个动态我点赞了那么我再次点赞的时候应该是取消并不是点赞那么如果说我们的一些在我们的APP中那么如果说出现一些出现一些这种比如说网络
[09:34] 或者一些这种bug呀它可能会导致我们重复点赞那么所以在这个位置我们最好去做一个判断就是我们需要去判判断是否是是否已经是否已经点赞那么如果已经已经点赞那么就返回OK好这个大家应该能够去理解吧那么怎么样去去得知它已经
[10:04] 点赞呢那就做查询就可以了那么怎么查询呢还是通过这个mongo啊template然后做一个这个fund的操作呃然后呢我们来看一下啊需要一个这个query对象然后呢去查询谁呢comment啊就可以了那么接下来我们去定义一个这个query对象那么queryquery等于啊query那么我们想要呢肯定是需要去给他去设置查询条件的对不对啊
[10:33] 我们来看条件怎么去做一个设置,然后去设置条件那么首先,第一个我们来看一下他的UID是不是就应该是我当前的人对吧那么UID然后点依日依日这个UID然后我们继续设置是不是应该是按的按的谁呢是不是我们comment中会有一个
[11:02] public id他呢应该是一日谁呢哎这个点啊一日谁呢要注意要去new一个object id啊给他传递过去这是第二个这个条件啊来看一下啊这是第二个条件那么第三个啊这个条件啊它是什么呢就是我们应该再去更一个条件就是谁就是我们这个叫做什么呢comment type就是就是他啊
[11:27] 就是说我们这个已经点赞了对吧它的一个值1应该是谁呢那就应该是1啊对吧那么这个呢就是我们的一个条件那么我们来给它去生成一下啊这个呢得到的一个creative那么我们把这个creative呢放到这儿来那么就构造了一个query把query丢到这儿那么这个就是我们的一个查询条件那么如果啊那我们就不需要去拿到它了呢我们应该这样查吧我们来一个什么呢叫做count
[11:56] 对吧我们去查看它的一个数量就可以了那么如果如果这个数量呢然后大于0那就代表着已经这个用户对于这个动态已经点赞了那我们就应该return false就代表着这一次点赞它是失败了它失败了那么这样的话我们是不是就实现了这样的一个判断就判断它是否已经点赞了如果已经点赞了就返回OK
[12:25] 好那么下面的这个是否喜欢那个这个位置逻辑是不是也就一样了那我们来看一下那么是否已经这个喜欢喜欢如果已经喜欢那么就返回了那么这个条件一样一样那么只要改变的是在这个位置三这样的话是不是就OK了对吧好那么这个是那我们目前是不是已经就实现了有三个方法了对吧一个点赞
[12:56] 一个是喜欢那么还有什么呢就是保存这个评论那么接下来呢我们来继续来实现啊其他的两个方法那么下面这个呢是叫remote contact那么就是我们的所说的这个怎么的取消点赞或者说取消这个喜欢那么这个怎么去实现呢其实跟我们上面这个差不多了对吧那我们就通过这个this.mongo template然后呢做一个remote这个操作
[13:24] 那么我们肯定是需要根据一个条件是不是去做一个这个remote删除那么条件是先设置文档那第二个就是我们这个comment.class指定它那么接下来我们来写一个query那么query其实跟我们这个就非常的类似了那我们就直接拷贝过来那么首先UID是它然后public ID是它然后comment type我是写到这来就不能写死了
[13:52] 那么去做一个这个remote三除那么它的返回值呢是一个叫做delete result那我们就拿到一个delete result然后呢return一个值来布尔值来表明我们是三除成功还是失败我们通过它的一个get一个delete count如果它大于0
[14:13] 大于0那就是返回错那就代表着我们删除成功了如果说它要等于0的话那代表着我们这个肯定不成立对吧那就返回这个False啊代表着删除失败了OK好那么这个呢是不是我们的一个取消的这个操作啊那么接下来呢我们来看一下下面还有这个是查询什么呢查询这个Count对不对那么这个Count怎么查询呢是不是我们就可以啊调用谁呢
[14:39] 通过这个mongo这个template做一个什么count这个操作就可以了那么我们还是设置为num然后呢还是需要设置一个comment.class那么这个query怎么来呢其实跟前面是不是又是非常的类似了那我们把这个呢也拷贝过来哎丢的账然后呢要注意的是那我们查询count呢我们就没有必要根据用户来了对吧和用户没有关系那我们就去查询这一个
[15:08] 动态它的类型但是它和type是有关系的所以说呢我们应该是这么来玩一下那么应该是把它吧一直到这一直到这里这样改一下就是will这个public id一直它然后呢common type呢是这个type这个就不能写死了那么写个type那么query呢丢到这来那这样的话呢我们就完成了一个这个
[15:35] 就是我们数量的一个查询就是点赞数还是我们的一些喜欢数啊等等的这样的去做一个实现啊好那么接下来呢我们来看一下我们的讲义的这个实现啊应该跟我们实现的也差不多对吧那么这个呢是哎上面这个是点赞啊点赞数那么是不是也设置了一个条件啊然后呢去做一次数量的查询如果大于0呢就返回fos然后呢是如果
[16:01] 不大于0呢那就代表着还没有进行操作那么就可以做一个save这个操作了然后呢这个呢是取消这个点赞那么通过构造这个条件呢去做一个remote最后呢返回他的delete count大于0这个布尔值然后呢下面这个动作呢是一个喜欢的动作下面这个呢是保存评论啊都是一样的
[16:21] 然后呢来看一下下面这个呢也是一样的去查询我们这个条件对吧根据条件去做一个counter查询最后返回的是一个这个数量也OK好那么关于我们这个接口double接口的一个实现呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

