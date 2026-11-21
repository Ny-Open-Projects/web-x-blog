# 02.我的喜欢之喜欢数统计（dubbo服务实现）

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\02.我的喜欢之喜欢数统计（dubbo服务实现）_【海量资源尽在 666java.com】.mp4
- 时长 13分21秒（音频 802s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下我的喜欢啊这个功能那么在我的这个模块中呢那么我们会展现一些相关我们喜欢啊相关的一些这种数据啊你比如说呢那么我们进入到我这个我的模块中啊那么在这个位置呢我们会展现一些这个相互关注的一些这个数量还有喜欢的数量还有些粉丝的这样的一些这个数量
[00:24] 并且呢我们点击这个相互关注啊或者说喜欢或者是粉丝呢那我们就会进入到我们这个详情这个页面那么在这个里面呢去做一些这个展现啊有这个相互关注啊这个关注啊粉丝啊等等那么我们会把他的详情呢去展现出来并且呢我们在这个里面可以做一些操作啊你比如说呢我们可以做这个取消关注啊或者说我们去关注啊或者说喜欢呢这样的一些操作啊好那么接下来呢我们对
[00:53] 这个这三个概念呢我们来做一个说明那么这个喜欢呢就是指什么呢我喜欢别人啊比如说呢这个张三啊喜欢这个李四那么我们需要展现的就是什么这个喜欢这个数据啊就说张三喜欢李四那么我们如果去查看我的喜欢的时候那么在张三这个角度去看的话那么这个就会展现李四的这个数据
[01:18] 但是要注意的是那么张三喜欢李四并不代表着李四也喜欢张三这个要注意一下那么粉丝呢就是说对于李四而言是不是张三就是他的粉丝因为张三喜欢李四对吧那么张三呢就是李四的一个粉丝那么如果说李四也喜欢张三的话那么这个张三和李四他们之间
[01:43] 就是相互喜欢所以这个就是相互关注啊或者说相互喜欢啊这样的关系这三个概念呢一定要搞清楚那么如果你搞不清楚呢在后面我们再去做开发的过程中呢就可能做错了好那么接下来呢我们就来做一个具体的一个实现那么接下来呢我们就先把我们这个double这个服务呢我们来做一个这个编写那么我们来给它定义这么几个方法啊就是在我们的原有的这个
[02:12] 接口的基础之上啊那我们来添加这么几个啊方法那三个这个方法那么就是我们去查看他的相互喜欢的一个数量啊返回是一个浪类型然后呢喜欢数呢也返回是一个浪类型然后呢粉丝数呢也是去做一个啊这个返回然后呢我们把这个三个方法呢我们拷贝一下那么我们来把它拷贝到我们的这个double的这个接口中啊那么找到这个里面呢我们去啊找到他有个
[02:42] 我们的一个uselike API然后呢之前呢是不是我们有三个啊这个方法那我们再来添加啊三个方法那么这个呢是相互喜欢啊喜欢以及粉丝那么接下来呢我们就来找到它的一个Service就是具体的一个接口的一个实现类然后呢我们来做一个具体的一个实现好那么我们去找到上面啊然后呢去实现啊这三个这个方法
[03:09] 好那么这个三个方法是不是就拿出来了对吧那么接下来呢我们就来做具体的实现那么首先呢我们先来看一下我们这个查询我们相互喜欢的啊这个方法那么这个实现的一个思路啊那我们先来写一下我们的一个思路啊那我们是这样的一个思路那么我们是不是应该是去查询什么呢就是我喜欢对方那么同样的
[03:34] 对方呢也是喜欢我啊这样的一个思路啊去做一个实现那么我们是不是应该去首先查询什么呢我的这个喜欢的一个列表就是我喜欢谁啊我喜欢谁然后呢查询到之后啊那么然后呢我们再去查询什么呢就是所有喜欢我的用户的这个列表就是说在我的这个我喜欢别人的这个范围内那么再去查找
[04:02] 这么多人中哪些人喜欢我那么查询到的这个就是跟我相互喜欢的这样的关系这个大家能不能够理解啊就是说我们然后呢去在在这个的在我的这个我的喜欢的这个喜欢的人范围内对吧范围内然后呢去查询喜欢我的人那么这个就是什么呢相互喜欢
[04:31] 对吧那么首先呢我们就来查询什么呢下面我们就先来查询我的喜欢的一个列表那么这个怎么做呢我们就通过我们的这个this.mongo.template做一个份的这个查询然后呢我们需要给它构造一个条件那么就通过这个query.query然后呢设置creator然后呢view那么我的喜欢是谁呢是不是就是我们去查询啊这个
[05:00] UraIDUraID然后呢点一之谁呢是不是就这个UraID传递过来那么这个呢是我自己的这个用户ID这个是我们的一个条件那么我们这个就是一个这个query然后呢我们把这个query呢就给它丢到这个里面来然后呢这第一个参数那第二个参数呢就是我们这个UraLike然后呢一个class那么这个拿到的就是什么呢
[05:29] 叫做我的喜欢的一个列表然后呢我们就需要去收集到收集到我的喜欢列表中的这个什么呢用户ID这个用户ID指的是谁那是对方对吧是对方那我们就定一个list然后呢写一个log叫做什么呢like吧like
[05:57] Uraids然后呢我们去new一个arrivalist然后呢我们去做一个便利便利谁呢就是上面我们的这个UraLikes然后呢我们就拿到谁呢拿到这个里面的and去添加一个叫UraLike.get谁呢注意get什么like UraID就是我喜欢的谁这个列表然后呢接下来呢我们是不是就查询是不是在我的
[06:27] 喜欢列表范围内是不是去查询什么呢去查询喜欢我的人有哪些那么是不是就这样的话就可以得到这样的一个列表了对吧那我们又要构造一个查询条件了那么就是通过query.query.cat然后呢will设计一个什么呢叫做usid点一日谁呢注意那么这个不能是一日了
[06:56] 应谁呢就是我们上面收集到的这个用户ID应他然后呢我们再去做一个and一个操作按着谁呢按着我们这个like your ID就喜欢我的喜欢我的这个用户呢等于等于我这个那么所以说我们要找到我们的这个对象他里面有个叫做like your IDand这个like your ID点一日谁呢
[07:24] 就是我啊以我就他喜欢我这样的一个条件啊然后呢我们这样的话呢就查询到我们的这个这样的一个这个列表了对吧然后呢我们就设置一个这个叫query啊就query2吧啊query2然后呢下面我们是不是就可以去做一个啊这个查询了对吧因为我们需要返回的呢是一个不是列表是一个这个数量所以我们直接就可以
[07:53] this.template然后呢做一个count一个查询啊就可以了然后呢把这个query2传递进去然后呢再拿到一个uselike.class那么这样的话呢我们就拿到一个这个数量了啊拿到一个数量了那么这个是不是就是我们的啊第一个啊这个的一个实现啊这个大家能不能够理解啊就是先查询出我的喜欢列表拿到我喜欢的这个人的一个ID
[08:20] 然后通过这个ID中再去查询什么呢再去查询这个喜欢我的人有哪些两个条件一个就是这个他的ID等于这个我喜欢的那个ID的人然后再去看喜欢我那个人这个是我的话那么就会拿到这个数据了这就是一个数量那么这个第一个我们是不是就搞定了那么接下来我们来看我们的第二个那么这个是主要是查询我喜欢谁
[08:46] 所以说这个就比较简单了我们直接可以写就this.mongo.template然后countquery其实就是我们上面的它是不是就是我们这个query条件对吧那就是我喜欢的人肯定用户ID是我然后逗号来一个yourlike.class好嘞那么这样的话是不是我们这个就搞定了这个查询我喜欢那么下面我们来看一下我们要查询我们这个
[09:14] 粉丝的这个列表那这个这个count啊那我们还是去来一个count这个操作那么这个query呢就是谁呢就是粉丝嘛就是喜欢喜欢的喜欢我的人啊有哪些所以说呢我们就把这个这样吧我们就把这个拷贝过来条件改一下就可以了来看一下啊那么这个条件呢就不能用这个UID了应该用谁呢用这个like UID啊like UID是等于我的这个
[09:44] 那么就是这样的一个条件啊这就是查到这个粉丝了好那么接下来呢我们就来做一下这个单元测试啊那么单元测试呢就是在我们的讲义中呢有这个单元测试那么接下来呢我们把这个呢来考虑一下那么首先我们来看一下之前呢我们有没有这个单元测试啊那我们来看一下那么之前呢我们是叫Uderlike油对吧然后呢我们就把这个来改造一下那么我就把它吧
[10:12] 把这个我们就直接拷贝过来吧然后呢我们去做一个测试了好那么这个呢就是哎这个是包错之前我们是不是已经有一个test c5我们改成这个2吧改成2然后呢我们像我们的这个uselike这个表里面插入一堆数据就是我们可以来看一下这个数据啊就是1喜欢2然后呢1喜欢32喜欢1啊这个就是一个相互喜欢了1喜欢4
[10:40] 然后呢4喜欢1这个是不是也是一个相互喜欢5喜欢16喜欢1那么这两个就是两个粉丝对不对好那么接下来呢我们就来执行一下那么当然了首先呢我们先把我之前的一些这个数据呢我先把它清理掉啊然后呢我们再来去做一个测试然后呢找到这个碳花connections然后呢找到下面有一个叫做uselike我直接把它做不定
[11:07] 好嘞那么接下来呢我们就来执行一下这个C5这个操作好那我们来等待它的一个执行好那么现在呢我们就执行结束了那我们来看一下这个数据那么下面呢这个U2Like表那么有这么几条数据啊那么这个跟我们的期望是一样的就是把数据呢插入进来了那么接下来呢我们就来执行一下下面的这个查询那我们去查询这个用户
[11:33] ID唯一的这个用户他的一个相互喜欢的数量有多少那么以及呢他的这个粉丝啊有多少以及他的所喜欢的这样的一个数量是有多少那么接下来呢我们就来执行一下看他的一个效果好那么接下来呢我们来看一下他输出的一个结果那么首先我们可以看到他的这个就是相互喜欢数呢是二那我们来检查一下对不对啊就是那么一喜欢我们来这样来画一下啊就是一喜欢二
[12:03] 那么二喜欢一这个是不是属于一对那么就是一对吧这个数量是一然后呢一喜欢四和四喜欢一那么这个显然是不是就是二对吧然后呢这个我的这个粉丝数有几个呢我们来数一下还有几个那么喜欢我的是一的这个就可以了只要找到这个like有来自于一的是吧有一个两个三个四个是不是有四个这个数量
[12:29] 然后呢这个喜欢这个粉这个我的喜欢呢是三个人就是UID啊等于这个1的这个有几个可以看到是不是有三个OK那么这个结果啊是不是就是对的呀所以说呢我们刚刚所写的这个方法是OK的没有问题那么下面呢我们来看一下我们的一个这个讲义啊
[12:51] 那么讲义的这个实现呢跟我们应该也差不多就是我们可以看到这个位置是不是有三个这个接口然后呢在我们下面这个位置呢就做具体的一个实现那么这个呢也是先去查询我的这个喜欢列表然后拿到喜欢列表中的用户ID然后呢去做这样的一个查询然后下面这个呢就和这个呢就比较简单了去设置一个条件啊去查询就OK了好那么关于我们的这个double服务的一个实现呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

