# 09.圈子功能实现之发布动态（中）

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\09.圈子功能实现之发布动态（中）_【海量资源尽在 666java.com】.mp4
- 时长 6分56秒（音频 417s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前面呢我们讲到我们需要呢把我们的这个动态数据啊写到我们的时间线表中那么写到这个时间线呢其实就是写入到
[00:08] 好友的这个对方的这个表里面去啊所以说我们现在应该先有的是我们好友所以接下来呢我们先来去照一下我们的数据啊因为我们现在还没有去设计到一个好友的这个数据的操作啊所以说呢我们先去把这个数据呢先来照出来那我们就把这个测试用力啊我们做一个拷贝那么直接就拷贝到我们的这个这个Service下面有一个test啊这个下面那就直接哎靠到这吧
[00:36] 那么这个呢其实就非常简单了就是我们去插入这么几个用户的这个数据就是好友的数据那么这个UID呢是1就是我们第一个这个用户然后他的这个Fade ID呢就是2 3 4 5这个是我们多了一个给他来个6吧来个6那么也就是说我这个用户ID唯一的这个用户他呢有这个是不是有五个好友对吧有五个好友
[01:06] 好那么下面我们来看一下这个呢是做查询啊那我们先来去做一个sale这个操作那么下面呢我们就来执行一下啊这个操作然后呢我们去run一下走好那我们来等待它的一个执行好那么我们现在呢就执行成功了啊那么接下来呢我们来看一下呃我们呢有没有去生成啊我们的这个
[01:29] 就是我们的一个这个us那么其实可以看到是不是已经就生成了对吧那么这个us我们来看一下它的一些这个字段那么这个是我们用户ID唯一的这个用户然后这个是为2这个是1这个是22345是不是都有ok好那么这个是5
[01:54] 这个我们是不是执行了两遍呢对吧数据重复了对吧好那么我们重新来做一个执行我们把它呢就直接drop掉然后呢我们再来执行一下可能是跟之前的这个数据呢重复了那我再来执行一下走好那我们来等待一下好那么我们再次执行完成之后啊那么这个数据呢就正常了那么总共呢有五条数据啊就对了
[02:20] OK好那么接下来呢我们就编写我们的业务逻辑啊那么在前面呢我们这个位置啊那么首先呢我们肯定是需要去干嘛呢是不是我们去啊查询这个当前用户的这个好友的数据然后呢将数据就是这个动态的这个数据呢写入到哪里呢写入到这个好友的时间啊线表中啊
[02:49] 那么我们主要是在做这个逻辑那么我们首先需要去做一个查询那就通过this.mongo db template然后做一个find这个操作那么我们来看一下这个find这个操作那么我们就直接去这样去写那么需要两个参数一个是query那么一个就是我们对象我们在这个位置给它写做us.class
[03:15] 那我们来看这query对象怎么去定义啊那么写一个这个query这个对象然后呢query那么query对象是不是可以通过一个query点query去得到然后呢我们去传一个creator这样的一个对象然后呢点设置一个条件will那我们来看一下那么我们这个对象是谁呢其实这个条件是不是叫user id对吧我们去查询我这个用户的这个好友
[03:41] 那么就是这个什么呢Ura ID然后呢他呢一只啊就是谁呢就是我们上面所拿到的这个public点这个getUra ID那么就是他这个就是我们的一个条件啊那么通过这个query是不是就可以去查询到我们的这个叫做Uras那么接下来呢我们是不是就需要去对我们这个Uras做一个便利然后呢去写入这个数据啊
[04:10] 对吧那么每一个这个用户都需要给他去做一个写入所以说呢在这个位置我们要定义一个什么呢timeline这样的一个对象等于new一个timeline然后呢我们去给他设置一些属性那么首先第一个呢是ID同样的通过object id.get去拿到然后呢我们在set设置一个谁呢设置一个user id那么这个user id是谁呢我们来看一下对吧
[04:39] 那么这个UID其实是好友的这个UID也就是谁呢也就是当前的我的这个ID对吧就是我自己对吧我自己发的这个动态那么就是我然后呢我再设置谁呢设置我们这个public ID那么public ID是谁呢就是我们上面所得到的一个public.getID这样的一个对象然后呢我们再set设置谁呢set date
[05:09] 就是当前的一个时间戳当前的一个时间戳然后呢下面的注意我们做保存了是不是就this.mongodbtemplate做一个save这个操作那么save谁呢save就是我这个timeline对象第二个参数我要给他设置谁设置我们的表明设置表明设置表明那么这个表明怎么设置呢我们来看一下要把它copy过来然后呢
[05:39] 要注意啊然后呢我们要给他设置谁呢设置什么下滑线去加一个我的好友我自己的这个用户ID啊那么我就是通过谁呢就通过我这个Ura刚刚我拿到的这个Ura对象点get谁getUragetUraID那么这个呢就对了对吧这个他的用户ID就是他对吧
[06:05] 那我们来看这个不是UID这个应该错了应该是getfader朋友ID对吧你要对方的这个表中去写入数据这个大家能不能够理解那么我当前是这个用户他需要往好友中去写是不是就应该拿到好友的这个ID对象对吧OK
[06:27] 好那么这样的话呢其实我们是不是就已经完成了我们这样的一个写入的这样的一个操作呢那么到最后呢就是return谁的return true啊就可以了那么这样的话呢我们这个逻辑呢是不是就已经编写完成了对吧哎呦ok好那么接下来呢我们可以来做一个这个写一个单元测试呢去做一个测试啊哎呦ok好那么关于这个就是我们的一个保存我们动态的这样的一个实现呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
2019-09-14 20:46:26.688 INFO 10284 --- [168.31.81.2181] org.apache.ZooKeeper.ClientCnxn: EventThread: 
2019-09-14 20:46:26.902 INFO 10284 --- [pool-1-Thread-1] d.c.e.AwaitingNonAppBe
2019-09-14 20:46:26.914 INFO 10284 --- [pool-1-Thread-1] d.c.e.AwaitingNonAppBe
2019-09-14 20:46:27.573 INFO 10284 --- [Thread-4] org.mongodb.driver.conn
2019-09-14 20:46:27.603 INFO 10284 --- [booShutdownHook] org.apache.ZooKeeper.Cli
2019-09-14 20:46:27.603 INFO 10284 --- [tor-EventThread] org.apache.ZooKeeper.Cli
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

