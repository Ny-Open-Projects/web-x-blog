# 画面线理解：19.查询推荐动态（编写dubbo服务）

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\19.查询推荐动态（编写dubbo服务）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:24, 01:41, 02:19, 02:40, 03:32, 03:49, 04:14, 04:26, 04:38, 05:23, 05:40, 06:03, 06:34, 06:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:46:15

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
2019-09-16 17:01:13.122 [pool-1-thread-1] INFO 5824 --- [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet: GET /api/publish/2
2019-09-16 17:01:13.122 [pool-1-thread-1] INFO 5824 --- [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet: GET /api/publish/2
2019-09-16 17:01:13.122 [pool-1-thread-
