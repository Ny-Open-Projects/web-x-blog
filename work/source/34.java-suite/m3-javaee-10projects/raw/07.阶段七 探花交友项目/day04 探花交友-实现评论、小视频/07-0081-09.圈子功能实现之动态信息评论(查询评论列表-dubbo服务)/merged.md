# 09.圈子功能实现之动态信息评论（查询评论列表-dubbo服务）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\09.圈子功能实现之动态信息评论（查询评论列表-dubbo服务）_【海量资源尽在 666java.com】.mp4
- 时长 6分39秒（音频 399s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来查询我们的这个动态中的评论的列表那么前面我们说过在我们去展现我们一个单条动态的时候呢除了我们要查询动态的信息以外呢我们还需要去查询它的这个评论的列表才能够正常的去显示出来所以说呢我们还需要把这个接口呢来提供一下那么这个接口呢其实就是在我们的这个位置啊有一个
[00:28] 叫做什么呢叫做评论的列表来刷新一下那么就是评论的列表那么评论列表呢我们最后返回的是这样的一些这个数据啊那么参数呢是有三个参数一个是moment id还有是page还有一个page size然后呢我们来看一下上面的是comments啊所以说呢我们还需要去编写这样的一个Controller啊去做一个评论的一个这个编写
[00:59] 那么下面我们就来看一下那么首先我们先来提供我们Double的接口那么这个是怎么查询我们的评论那么名字方法名叫做query comment list然后传递是public id,pager还有page size那么我们把接口的定义我们来拷贝过来那么去添加到我们Double工程中的interface中
[01:25] 那么我们就还是写到这个圈子这个里面来吧那么我们写到这写到这好嘞好那么我们这样的话就定义好了那么把这个comment这个类呢我们去导入进来那么这个呢就是查询啊那么下面呢我们去找到这个double的Service那么在double Service中呢我们去生成我们的一些这个方法
[01:50] 那么就是刚刚我们所写的这个查询这个comment list这样的一个方法那我们来看一下这个方法应该怎么样去写那么最终呢我们需要返回的是我们的呃配置info啊当然了在配置info中呢肯定是需要去呃那我们就直接来定义吧肯定是需要一个我们呃集合的对吧就是我们的这个list集合的那我们就直接来给他去呃定义一个配置info
[02:18] 有点卡顿啊稍微等待一下好那么我们在这个位置呢去定一个这是一个什么呢comment好那么定一个叫page info等于new一个page info然后呢最后把它return这样就可以了然后呢我们需要去给它做数据的一些填充那么recode呢我们一会儿来写这个recode嘛total呢就设置为0那么先不提供它然后呢我们去继续点set谁呢
[02:47] Pager Size那就是上面传入的Pager Size然后呢还有什么呢Pager Info.set什么的还有Pager Number那就是Pager好那么接下来我们只要处理那个集合是不是就可以了好那么这个集合怎么拿呢肯定是通过我们的Mongo Template然后呢去做一个Find去做一个查询啊对吧那么显然呢我们可以看到呢是这个Query呢我们先设置为呢然后呢我们还需要设置的是一个就是我们的一个类
[03:16] 那么就是comment然后点class这样的一个类那么comment class那么我们来看一下这个里面的查询那么我们要查询的是它的评论那就是type为2的这样的一个这样的一个数据然后呢以及这个publish id那么接下来呢我们来看一下怎么样去做一个构建的query呢那么显然呢我们是需要去给它设置一个query对象然后呢
[03:45] query设置一个criteria.avail首先肯定是会有一个publish id我们给它来设置一下然后它点new object id然后publish id去设置它然后我们回测一下点
[04:12] 然后我们再设置一个按的条件谁呢还有一个就是我们的这个comment type类型那么这个类型呢就是在这设置它呢一一是谁呢我们这个叫做配置不是配置叫什么呢就是我们的二类型为二然后呢这是我们的一个这个条件对吧那么大家可以想一下我们要查询的是一个评论的一个列表那么显然呢它肯定是需要
[04:43] 按照时间去排序的那么就是我们需要按照用户的一个回复的一个时间按照一个顺序排序啊也就是正序排序不是倒序啊是正序那么这个应该怎么去做呢所以呢我们在上面这个位置啊那我们既要去做排序那么又需要去设置分页那么我们就需要设置一个什么呢叫PagerPager什么呢PagerRequest是不是这个对象那么可以设置它
[05:12] 等于去new一个不能去new对吧通过一个page request.off那么是不是可以使用这个下面的这个第二个这个方法那么首先呢是page-1然后呢设置一个page size那么第三个呢是不是设置一个排序然后呢order然后呢我们要用的是.asc那么根据哪个字段去做排序呢我们来看一下那么在我们这个comment中呢它其实有一个created字段
[05:41] 那我们需要按照这个字段的去做一个什么呢正序的一个排序了好那我们好那么我们就得到一个这个page request然后呢我们下面的通过一个位置把这个传递过去那么这个querydition是不是就构建好了哎呦这一丢好那么这样的话呢就实现了我们去查询我们这个comment list然后拿到之后呢我们就需要放到info
[06:09] 然后点set一个recode把它丢进去好这样的话呢做return是不是就搞定了那么到这里呢我们是不是就已经啊完成了它的一个这个double接口服务的一个啊这样的一个编写那么我们来看一下讲义啊有没有问题那么这个是接口的一个定义那么下面这个是接口的一个实现啊应该是没有问题的好那么关于这个查询我们评论列表的这样的一个double服务的一个编写呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

