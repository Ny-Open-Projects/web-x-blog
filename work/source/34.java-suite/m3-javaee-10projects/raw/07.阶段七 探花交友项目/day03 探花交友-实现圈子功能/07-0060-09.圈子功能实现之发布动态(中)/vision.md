# 画面线理解：09.圈子功能实现之发布动态（中）

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\09.圈子功能实现之发布动态（中）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:16, 00:38, 01:23, 01:56, 02:14, 03:06, 03:28, 04:13, 04:28, 04:54, 05:10, 05:26, 06:02, 06:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:38:44

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 MongoTemplate 实现发布动态功能，包括定义接口、编写测试用例、保存动态、专辑和时间线数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Typora 文档中定义的 QuanzApi 接口，包含 savePublish 方法。
画面 2: 显示 TestUsers 测试类，使用 @SpringBootTest 和 @Autowired 注解，包含 saveUsers 和 testQueryList 方法。
画面 3: 显示 TestUsers 测试类运行结果，日志显示测试通过。
画面 4: 显示 MongoDB 数据库界面，展示 Users 集合中的数据。
画面 5: 显示 TestUsers 测试类运行日志，显示测试执行过程。
画面 6: 显示 QuanzApiImpl 类中 savePublish 方法的实现，包含保存动态、专辑和查询好友数据的逻辑。
画面 7: 显示 QuanzApiImpl 类中查询用户数据的代码，使用 Query 和 Criteria。
画面 8: 显示 QuanzApiImpl 类中查询用户数据的代码，使用 Query 和 Criteria。
画面 9: 显示 QuanzApiImpl 类中查询用户数据的代码，使用 Query 和 Criteria。
画面 10: 显示 QuanzApiImpl 类中查询用户数据的代码，使用 Query 和 Criteria。
画面 11: 显示 QuanzApiImpl 类中查询用户数据的代码，使用 Query 和 Criteria。
画面 12: 显示 QuanzApiImpl 类中查询用户数据的代码，使用 Query 和 Criteria。
画面 13: 显示 QuanzApiImpl 类中查询用户数据的代码，使用 Query 和 Criteria。
画面 14: 显示 QuanzApiImpl 类中 savePublish 方法的实现，包含保存动态、专辑和时间线数据的逻辑。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.tanhua.dubbo.server.api;
import com.tanhua.dubbo.server.pojo.Publish;
public interface QuanzApi {
    /*
     * 发布动态
     * @param publish
     * @return
     */
    boolean savePublish(Publish publish);
}
```

画面 2:
```java
package com.tanhua.dubbo.server.api;
import ...
@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest
public class TestUsers {
    @Autowired
    private MongoTemplate mongoTemplate;

    @Test
    public void saveUsers() {
        this.mongoTemplate.save(new Users(ObjectId.get(), userId: 1L, friendId: 2L, new Date()));
        this.mongoTemplate.save(new Users(ObjectId.get(), userId: 1L, friendId: 3L, new Date()));
        this.mongoTemplate.save(new Users(ObjectId.get(), userId: 1L, friendId: 4L, new Date()));
        this.mongoTemplate.save(new Users(ObjectId.get(), userId: 1L, friendId: 5L, new Date()));
    }

    @Test
    public void testQueryList() {
        Criteria criteria = Criteria.where("userId").is(1L);
    }
}
```

画面 3:
```
2019-09-14 20:46:26.688 INFO 10284 --- [168.31.81.2181] org.apache.zookeeper.ClientCnxn: EventThread: 
2019-09-14 20:46:26.902 INFO 10284 --- [pool-1-thread-1] d.c.e.AwaitingNonAppBe
2019-09-14 20:46:26.914 INFO 10284 --- [pool-1-thread-1] d.c.e.AwaitingNonAppBe
2019-09-14 20:46:27.573 INFO 10284 --- [Thread-4] org.mongodb.driver.conn
2019-09-14 20:46:27.603 INFO 10284 --- [booShutdownHook] org.apache.zookeeper.Cli
2019-09-14 20:46:27.603 INFO 10284 --- [tor-EventThread] org.apache.zookeeper.Cli
Process finished with exit code 0
```

画面 4:
```
Key          Value                          Type
_class        com.tanhua.dubbo.server.pojo.Users    String
_id           ObjectId("5d7fa4b4e3b172a8524204")    Object
userId        1                                Int32
friendId      2                                Int32
date          2019-06-04 08:24:11.313          Date
_class        com.tanhua.dubbo.server.pojo.Users    String
_id           ObjectId("5d7fa124a8c3d282c7d6099")    Object
userId        1                                Int32
friendId      3                                Int32
date          2019-06-04 12:46:57.283          Date
_class        com.tanhua.dubbo.server.pojo.Users    String
_id           ObjectId("5d7fa124a8c3d282c7d6099")    Object
userId        1                                Int32
friendId      4                                Int32
date          2019-06-04 12:46:57.495          Date
```

画面 6:
```java
publish.setSeeType(1); // 查看权限
// 保存动态信息
this.mongoTemplate.save(publish);
// 写入到自己的相册表中
Album album = new Album();
album.setId(ObjectId.get()); // 动态id
album.setPublishId(publish.getId());
album.setCreated(System.currentTimeMillis());
// 将相册对象写入到MongoDB中
this.mongoTemplate.save(album, collectionName: "quanzi_album" + publish.getUserId());
// 查询当前用户的好友数据，将动态数据写入到好友的时间线表中
this.mongoTemplate.find();
return false;
```

画面 7:
```java
Query query = Query.query(Criteria.where("userId").is(publish.getUserId()));
List<Users> users = this.mongoTemplate.find(query, Users.class);
```

画面 8:
```java
Query query = Query.query(Criteria.where("userId").is(publish.getUserId()));
List<Users> users = this.mongoTemplate.find(query, Users.class);
for (Users user : users) {
    Timeline timeline = new Timeline();
    timeline.setId(ObjectId.get());
    timeline.setUserId(publish.getUserId());
    timeline.setPublishId(publish.getId());
    timeline.setDate(System.currentTimeMillis());
}
```

画面 9:
```java
Timeline timeline = new Timeline();
timeline.setId(ObjectId.get());
timeline.setUserId(publish.getUserId());
timeline.setPublishId(publish.getId());
timeline.setDate(System.currentTimeMillis());
```

画面 10:
```java
Timeline timeline = new Timeline();
timeline.setId(ObjectId.get());
timeline.setUserId(publish.getUserId());
timeline.setPublishId(publish.getId());
timeline.setDate(System.currentTimeMillis());
```

画面 11:
```java
Timeline timeline = new Timeline();
timeline.setId(ObjectId.get());
timeline.setUserId(publish.getUserId());
timeline.setPublishId(publish.getId());
timeline.setDate(System.currentTimeMillis());
```

画面 12:
```java
Timeline timeline = new Timeline();
timeline.setId(ObjectId.get());
timeline.setUserId(publish.getUserId());
timeline.setPublishId(publish.getId());
timeline.setDate(System.currentTimeMillis());
```

画面 13:
```java
this.mongoTemplate.save(timeline, collectionName: "quanzi_time_line" + user.getUserId());
```

画面 14:
```java
@Override
public boolean savePublish(Publish publish) {
    if (publish.getBeerId() == null) {
        return false;
    }
    // 填充数据
    publish.setUserId(ObjectId.get());
    publish.setCreated(System.currentTimeMillis());
    publish.setSeeType(1);
    this.mongoTemplate.save(publish);
    Album album = new Album();
    album.setId(ObjectId.get());
    album.setPublishId(publish.getId());
    album.setCreated(System.currentTimeMillis());
    this.mongoTemplate.save(album);
    return false;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
