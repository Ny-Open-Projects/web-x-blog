# 19.查询推荐动态（编写dubbo服务）

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\19.查询推荐动态（编写dubbo服务）_【海量资源尽在 666java.com】.mp4
- 时长 7分2秒（音频 423s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们将要实现的是我们查询我们推荐的这个动态那么这个推荐的动态呢是由我们在后面的去通过我们的推荐系统所计算出来的一些结果那我们将要去推荐一些比较热门或者说比较优质的一些这种动态来推荐给我们的用户去做一个查看
[00:25] 那么这个具体的推荐的逻辑呢我们在后面的去做一个实现那么目前呢我们将要实现的就是根据我们所推荐的这个结果呢我们做一个查询然后呢在我们的这个APP里面能够去显示出来就可以了那么其实我们这个推荐动态啊
[00:45] 它和我们这个好友动态的这个数据结构呢它是一样的大家可以想一下对吧它是一样的结构只是呢我们查询的时候呢需要去
[00:56] 通过我们的推荐动态一张表去做查询就可以了那么其实呢我们是需要有一张叫做推荐的时间线表就可以了因为呢我们去查询这个时间线表就可以去查询这个相关的动态的信息了所以说呢我们只需要去修改一下我们之前的逻辑那么这个业务呢就可以实现了
[01:18] 好那么接下来呢首先呢我们来修改我们double的一个这个实现的一个逻辑啊那么这个逻辑怎么样去做一个修改我们来看一下那么我们找到我们之前的一个这个Service的一个实现啊那我们找到这个API这个实现然后呢在这个里面啊在这个里面呢我们来看一下就是在这个方法就是我们这个query啊publicist那么大家可以想一下就是那么我们查询
[01:47] 好友的这个推荐和查询我们的这个查询好友动态和查询推荐动态有什么区别呢其实区别就在于有没有ID那么如果是我们查询推荐的这个动态那么所有的这个用户查询的是不是都是这些数据啊对不对查询都是这些数据那么是没有ID的所以说呢我们是不是可以在这个位置啊在这个位置呢我们去做一个
[02:17] 判断如果空等于UIDUID那么这个呢就说明我们现在查询的是什么呢查询的是推荐动态那么else那就说明是什么呢这个是查询什么呢这个查询好友的一个动态那么这么去玩的话我们是不是就可以定义一个什么呢定义我们的一个这个table
[02:45] 内幕等于啊表明等于什么呢我们来看一下那我们就把这个这个拿过来对吧然后呢一个是他对吧那么如果如果是我们这个推荐啊推荐这个那么我们应该这么写啊如果是查询推荐的话那我们是不是应该后面去跟一个什么Zickmon对吧那么这样的话就是个推荐那么如果说是查询好友的话
[03:15] 那我们就去跟一个谁呢跟一个用户ID啊就可以了哎这个大家能不能够理解啊那么我们把这个table name啊那么我们就放到这来这个我们就不能写死了对不对那么我们把它去掉啊这是我们查询这个表明好嘞好那么这样的话呢我们其实就已经完成了我们这个推荐的啊这样的一个查询啊那么接下来呢我们就来把我们的这个呃先把这个服务呢先停掉
[03:45] 然后我们把这个double这个服务做一个什么呢重启好那我们来等待它的一个重新启动好那么这个启动呢我们一会儿再启动为什么呢原因是呢我们需要去插入一些测试的数据因为我们现在呢还并没有去实现我们的一个推荐系统那我们只能去插入一些这个测试数据用于我们当做是我们的这个
[04:10] 这个推荐的这个数据那么我们就把下面这个就拷贝过来吧那我们去写到我们的一个测试用力中那我们来看一下这个它是怎么样去实现的呢我们来找到我们的一个这个test trend这个方法中那我们来看一下那么在这个中的实现呢我们还需要把这个mongo注入进来那就是mongo的一个template去注进来好那么把它注进来
[04:40] 那么注入进来之后啊我们来看一下啊那么注入进来之后呢我们就可以去使用它了那么我们首先呢去通过我们之前的这个这个方法去查询用户ID为2的啊这个他用户的一些这个动态啊用户查询他的动态那么查询到之后呢查询到之后呢我们去做一个便利然后呢把这个用户ID为2的这个用户动态呢
[05:10] 作为我们的一个这个数据啊那么其实我们应该查询的是用户ID我们来看一下我们的数据啊那么我们当前这个数据啊这个应该是我们查询这个啊因为我们是这个查询我们的是时间线表对吧哎没错那么是查询的用户ID为二的它就可以查询到我们用户ID为一的一些动态了是这样的一个逻辑啊然后呢拿到它之后呢我们去拿到了records
[05:39] 然后呢我们拿到他的这个就是时间线啊就是这个timeline啊这个数据然后呢我们给他丢到我们这张表里面叫就是这个圈子啊timeline然后呢就come on的这张表里面去然后呢我们一会儿是不是就可以做一个这个测试了好那我们来先执行一下这个测试用力好那我们来等待他的一个执行好那么现在呢我们这个呢就执行成功了啊那我们来刷新一下看一下我们这个表里面的一些情况啊
[06:07] 那么可以看到有一张表叫Rickmonger的一张表那么打开来看一下那么我们是不是就把用户ID用户ID为2的这个用户他的timeline中的一些这个动态就插入到这个里面来了就假设这个是我们的一些推荐的这个结果做了这样的一个数据的构造那么接下来我们就把我们的这个就是我们的这个double这个服务我们跑起来找一下我们这个double这个服务走把它跑起来
[06:36] 那么跑起来之后呢我们接下来呢就可以去编写我们的server的一些逻辑了去实现我们这样的一些这个逻辑啊好那么我们来等待它的一个启动好那么现在呢我们这个服务呢就已经跑起来了那么我们现在是不是已经完成了double服务的一个提供那么接下来我们是不是就编写它了对吧哎OK好那么我们关于这个double服务的一个编写或者说修改呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中编写测试用例，以验证推荐动态功能的正确性，涉及 MongoDB 数据操作和 Dubbo 服务调用。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 `RelativeDateFormat` 类的源码，定义了时间单位常量和格式化方法。
画面 2: 展示了 `QuanziApiImpl` 类中 `queryPublishList` 方法的代码，用于查询动态列表。
画面 3: 在 `queryPublishList` 方法中，光标位于 `if (null` 处，弹出的自动补全建议列表显示了多种异常类型。
画面 4: 在 `queryPublishList` 方法中，添加了 `if (null == userId)` 的条件判断语句，用于区分查询自己的动态还是好友的动态。
画面 5: 在 `queryPublishList` 方法中，根据 `userId` 是否为 null，动态设置 `tableName` 为 `"quanzi_time_line"` 或 `"quanzi_time_line_" + userId`。
画面 6: 展示了 `DubboApplication` 启动日志，确认服务已成功启动并连接到 ZooKeeper。
画面 7: 展示了 PPT 页面，标题为“2.5.2. 编写测试用例”，内容是关于如何编写测试用例以插入推荐数据。
画面 8: 展示了 `TestQuanzi.java` 文件中的 `testRecommendPublish` 方法，用于测试推荐动态功能。
画面 9: 展示了 `TestQuanzi.java` 文件中的 `testSavePublish` 方法，用于测试保存动态功能。
画面 10: 展示了 Robo 3T 数据库客户端界面，选中了 `quanzi_time_line_2` 集合。
画面 11: 展示了 `TestQuanzi.java` 文件中的 `testRecommendPublish` 方法，其中 `timeline.setPublishId(record.getPublishId());` 语句被高亮。
画面 12: 展示了 Robo 3T 数据库客户端界面，显示了 `quanzi_time_line_2` 集合中的数据记录。
画面 13: 展示了 `TestQuanzi.java` 文件中的 `testRecommendPublish` 方法，其中 `timeline.setPublishId(record.getPublishId());` 语句被高亮。
画面 14: 展示了 `TestQuanzi.java` 文件中的 `testRecommendPublish` 方法，其中 `timeline.setPublishId(record.getPublishId());` 语句被高亮。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.tanhua.server.utils;

import ...

public class RelativeDateFormat {
    private static final long ONE_SECOND = 1000L;
    private static final long ONE_MINUTE = 60000L;
    private static final long ONE_HOUR = 3600000L;
    private static final long ONE_DAY = 86400000L;
    private static final long ONE_WEEK = 604800000L;

    private static final String ONE_SECOND_AGO = "秒前";
    private static final String ONE_MINUTE_AGO = "分钟前";
    private static final String ONE_HOUR_AGO = "小时前";
    private static final String ONE_DAY_AGO = "天前";
    private static final String ONE_MONTH_AGO = "月前";
    private static final String ONE_YEAR_AGO = "年前";

    public static void main(String[] args) throws ParseException {
        SimpleDateFormat format = new SimpleDateFormat(pattern: "yyyy-MM-dd HH:mm:ss");
        Date date = format.parse("2013-11-11 18:35:35");
        System.out.println(format.format(date));
    }
}
```

画面 2:
```java
@Override
public PageInfo<Publish> queryPublishList(Long userId, Integer page, Integer pageSize) {
    Pageable pageable = PageRequest.of(page - 1, pageSize, Sort.by(Sort.Order.desc("date")));
    Query query = new Query().with(pageable);
    // 查询自己的时间表
    List<Timeline> timelines = this.mongoTemplate.find(query, Timeline.class, collectionName: "quanzi");
    List<ObjectId> ids = new ArrayList<>();
    for (Timeline timeline : timelines) {
        ids.add(timeline.getPublishId());
    }
}
```

画面 3:
```java
if (null
    NullPointerException (java.lang)
    NumberFormatException (java.lang)
    NoUniqueBeanDefinitionException (org.springframework.beans.factory)
    Null (org.apache.commons.lang3.ObjectUtils)
    Nullable (org.springframework.data.util)
    Nullabe (org.springframework.data.repository.util)
    NullabeWrapper (com.sun.org.apache.xerces.internal)
    NullabeWrapper (org.springframework.data.repository.util)
```

画面 4:
```java
if (null == userId) {
    // 查询推荐动态
} else {
    // 查询好友动态
}
```

画面 5:
```java
String tableName = "quanzi_time_line";
if (null == userId) {
    // 查询推荐动态
} else {
    // 查询好友动态
    tableName += userId;
}
// 查询自己的时间表
List<Timeline> timelines = this.mongoTemplate.find(query, Timeline.class, tableName);
List<ObjectId> ids = new ArrayList<>();
for (Timeline timeline : timelines) {
    ids.add(timeline.getPublishId());
}
```

画面 6:
```text
Client environment: [192.168.31.81:2181] (ZooKeeper)
Client connection established to server 192.168.31.81:2181, initiating session
Session establishment complete on server 192.168.31.81:2181, session timeout=30000
DubboApplication
ApplicationListener
Connection
```

画面 7:
```java
@Test
public void testRecommendPublish() {
    // 宣告用户id为2的动态作为推荐动态的数据
    PageInfo<Publish> pageInfo = this.quanziApi.queryPublishList(2L, 1, 10);
    for (Publish record : pageInfo.getRecords()) {
        Timeline timeline = new Timeline();
        timeline.setId(ObjectId.get());
        timeline.setPublishId(record.getPublishId());
        timeline.setUserId(record.getUserId());
        timeline.setDate(System.currentTimeMillis());
        this.mongoTemplate.save(timeline, "quanzi_time_line_recommend");
    }
}
```

画面 8:
```java
@Test
public void testRecommendPublish() {
    // 宣告用户id为2的动态作为推荐动态的数据
    PageInfo<Publish> pageInfo = this.quanziApi.queryPublishList(2L, 1, 10);
    for (Publish record : pageInfo.getRecords()) {
        Timeline timeline = new Timeline();
        timeline.setId(ObjectId.get());
        timeline.setPublishId(record.getPublishId());
        timeline.setUserId(record.getUserId());
        timeline.setDate(System.currentTimeMillis());
        this.mongoTemplate.save(timeline, "quanzi_time_line_recommend");
    }
}
```

画面 9:
```java
@Test
public void testSavePublish() {
    Publish publish = new Publish();
    publish.setUserId(1L);
    publish.setUserName("上海市");
    publish.setSeeType(1);
    publish.setText("今天天气不错~");
    publish.setMedias(Arrays.asList("https://itcast-tanhua.oss-cn-shanghai.aliyuncs.com/images/quan"));
    boolean result = this.quanziApi.savePublish(publish);
    System.out.println(result);
}
```

画面 10:
```text
db.getCollection("quanzi_time_line_2").find({})
```

画面 11:
```java
@Test
public void testRecommendPublish() {
    // 宣告用户id为2的动态作为推荐动态的数据
    PageInfo<Publish> pageInfo = this.quanziApi.queryPublishList(userId: 2L, page: 1, pageSize: 10);
    for (Publish record : pageInfo.getRecords()) {
        Timeline timeline = new Timeline();
        timeline.setId(ObjectId.get());
        timeline.setPublishId(record.getPublishId());
        timeline.setUserId(record.getUserId());
        timeline.setDate(System.currentTimeMillis());
        this.mongoTemplate.save(timeline, collectionName: "quanzi_time_line_recommend");
    }
}
```

画面 12:
```text
Key: ObjectId("5d7e19d46a9d14503b03a0")
Value: (5 fields)
Type: Object
```

画面 13:
```text
2019-09-16 17:01:13.122 [pool-1-Thread-1] INFO 5824 --- [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet: GET /api/publish/2
2019-09-16 17:01:13.122 [pool-1-Thread-1] INFO 5824 --- [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet: GET /api/publish/2
2019-09-16 17:01:13.122 [pool-1-Thread-

