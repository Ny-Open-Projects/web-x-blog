# 画面线理解：06.谁看过我实现之dubbo接口服务

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\06.谁看过我实现之dubbo接口服务_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:13, 02:40, 04:49, 05:53, 07:11, 08:10, 10:18, 12:52, 13:54, 15:07, 16:04, 17:28, 18:40, 19:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:12:29

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 MongoDB 的 MongoTemplate 实现访客记录的保存与按用户和时间维度查询的推荐服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示一个名为“桃花传情”的社交应用界面，包含“今日达人”和“推荐”板块，用于演示业务场景。
画面 2：展示 `VisitorsApi.java` 接口定义，包含 `saveVisitor` 和 `topVisitor` 两个方法，用于定义服务契约。
画面 3：展示 `VisitorsApiImpl.java` 实现类，包含对 `saveVisitor` 和 `topVisitor` 方法的空实现。
画面 4：在 `saveVisitor` 方法中，注入 `MongoTemplate`，并开始编写保存逻辑，使用 `save` 方法。
画面 5：完成 `saveVisitor` 方法，设置 ID 和日期，调用 `save` 保存对象，并返回 ID 的十六进制字符串。
画面 6：在 `topVisitor(Long userId, Integer num)` 方法中，使用 `Pageable` 和 `Sort` 构建分页和排序查询。
画面 7：在 `topVisitor(Long userId, Long date)` 方法中，构建查询条件，按日期降序排序。
画面 8：在 `queryVisitorsList` 方法中，遍历访客列表，并为每个访客查询推荐用户。
画面 9：在 `queryVisitorsList` 方法中，使用 `Criteria` 构建推荐用户查询，并设置访客的分数。
画面 10：在 `queryVisitorsList` 方法中，使用 `MongoTemplate` 的 `findOne` 方法查询推荐用户，并设置访客分数。
画面 11：展示项目目录结构，包含 `api`、`service`、`test` 等模块，以及 `VisitorsApiImpl` 的完整代码。
画面 12：展示 MongoDB 数据库中的 `visitors` 集合，包含多个访客记录，用于验证数据持久化。
画面 13：展示测试类 `TestVisitors` 的运行结果，显示测试通过，日志中包含访客数据和推荐用户信息。
画面 14：展示测试文档 `day09 试写.md`，其中包含测试相关的代码和注释，用于记录和说明测试过程。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```java
String saveVisitor(Visitors visitors);
/**
 * 按照时间倒序排序，查询最近的访客信息
 * @param userId
 * @param num
 * @return
 */
List<Visitors> topVisitor(Long userId, Integer num);

/**
 * 按照时间倒序排序，查询最近的访客信息
 * @param userId
 * @param date
 * @return
 */
List<Visitors> topVisitor(Long userId, Long date);
```

画面 3：
```java
@Service(version = "1.0.0")
public class VisitorsApiImpl implements VisitorsApi {

    @Override
    public String saveVisitor(Visitors visitors) {
        return null;
    }

    @Override
    public List<Visitors> topVisitor(Long userId, Integer num) {
        return null;
    }

    @Override
    public List<Visitors> topVisitor(Long userId, Long date) {
        return null;
    }
}
```

画面 4：
```java
@Autowired
private MongoTemplate mongoTemplate;

@Override
public String saveVisitor(Visitors visitors) {
    visitors.setId(ObjectId.get());
    visitors.setDate(System.currentTimeMillis());
    this.mongoTemplate.
        save(T objectToSave, String collectionName)
        scriptOps()
        setApplicationContext(ApplicationContext applicationContext)
        setReadPreference(ReadPreference readPreference)
        setSessionSynchronization(SessionSynchronization sessionSynchronization)
        setWriteConcern(WriteConcern writeConcern)
        setWriteResultChecker(WriteResultChecking writeResultChecking)
        stream(Query query, Class<T> entityType, String collectionNam, CloseableIterator<T> closeableIterator)
        ...
```

画面 5：
```java
@Override
public String saveVisitor(Visitors visitors) {
    visitors.setId(ObjectId.get());
    visitors.setDate(System.currentTimeMillis());
    this.mongoTemplate.save(visitors);
    return visitors.getId().toHexString();
}
```

画面 6：
```java
@Override
public List<Visitors> topVisitor(Long userId, Integer num) {
    Pageable pageable = PageRequest.of(page: 0, num, Sort.by(Sort.Order.desc("")));
    Query query = Query.query(Criteria.where("userId").is(userId)).with(pageable);
    return this.mongoTemplate.find(query, Visitors.class);
}
```

画面 7：
```java
@Override
public List<Visitors> topVisitor(Long userId, Long date) {
    Query query = Query.query(Criteria
        .where("userId").is(userId)
        .and("date").lt(date)
        .with(Sort.by(Sort.Order.desc("date")));
    return this.mongoTemplate.find(query, Visitors.class);
}
```

画面 8：
```java
@Override
public List<Visitors> queryVisitorsList(Query query) {
    List<Visitors> visitorsList = this.mongoTemplate.find(query, Visitors.class);
    for (Visitors visitors : visitorsList) {
        Query recommendQuery = Query.query(Criteria.where("userId").is(visitors.getUserId()));
        this.mongoTemplate.findOne(query, RecommendUser.class);
    }
    return visitorsList;
}
```

画面 9：
```java
@Override
public List<Visitors> queryVisitorsList(Query query) {
    List<Visitors> visitorsList = this.mongoTemplate.find(query, Visitors.class);
    for (Visitors visitors : visitorsList) {
        Query recommendQuery = Query.query(Criteria.where("userId").is(visitors.getUserId())
            .and("toUserId").is(visitors.getUserId()));
        RecommendUser recommendUser = this.mongoTemplate.findOne(recommendQuery, RecommendUser.class);
        if (null != recommendUser) {
            visitors.setScore(recommendUser.getScore());
        } else {
            visitors.setScore(300);
        }
    }
    return visitorsList;
}
```

画面 10：
```java
@Override
public List<Visitors> queryVisitorsList(Query query) {
    List<Visitors> visitorsList = this.mongoTemplate.find(query, Visitors.class);
    for (Visitors visitors : visitorsList) {
        Query recommendQuery = Query.query(Criteria.where("userId").is(visitors.getUserId())
            .and("toUserId").is(visitors.getUserId()));
        RecommendUser recommendUser = this.mongoTemplate.findOne(recommendQuery, RecommendUser.class);
        if (null != recommendUser) {
            visitors.setScore(recommendUser.getScore());
        } else {
            visitors.setScore(300);
        }
    }
    return visitorsList;
}
```

画面 11：
```java
@Service(version = "1.0.0")
public class VisitorsApiImpl implements VisitorsApi {

    @Autowired
    private MongoTemplate mongoTemplate;

    @Override
    public String saveVisitor(Visitors visitors) {
        visitors.setId(ObjectId.get());
        visitors.setDate(System.currentTimeMillis());
        this.mongoTemplate.save(visitors);
        return visitors.getId().toHexString();
    }

    @Override
    public List<Visitors> topVisitor(Long userId, Integer num) {
        Pageable pageable = PageRequest.of(page: 0, num, Sort.by(Sort.Order.desc("")));
        Query query = Query.query(Criteria.where("userId").is(userId)).with(pageable);
        return this.mongoTemplate.find(query, Visitors.class);
    }

    @Override
    public List<Visitors> topVisitor(Long userId, Long date) {
        Query query = Query.query(Criteria
            .where("userId").is(userId)
            .and("date").lt(date)
            .with(Sort.by(Sort.Order.desc("date")));
        return this.mongoTemplate.find(query, Visitors.class);
    }
}
```

画面 12：
```json
{
  "id": "5daf10177da931a6c4d8593",
  "userId": 32,
  "from": "首页",
  "date": 1571724010111,
  "score": 300
}
```

画面 13：
```java
Query recommendQuery = Query.query(Criteria.where("userId").is(visitors.getUserId())
    .and("toUserId").is(visitors.getUserId()));
RecommendUser recommendUser = this.mongoTemplate.findOne(recommendQuery, RecommendUser.class);
if (null != recommendUser) {
    visitors.setScore(recommendUser.getScore());
} else {
    visitors.setScore(300);
}
```

画面 14：
```markdown
2.4. 测试

package com.tanhua.dubbo.server.api;
import org.apache.commons.lang3.RandomUtils;
import org.bson.types.ObjectId;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest
public class TestVisitors {

    @Autowired
    private VisitorsApi visitorsApi;

    @Test
    public void testSaveVisitor() {
        Visitors visitor = new Visitors();
        visitor.setUserId(32);
        visitor.setFrom("首页");
        visitor
