# 08.今日佳人功能实现之实现dubbo服务（查询最大得分推荐用户）

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\08.今日佳人功能实现之实现dubbo服务（查询最大得分推荐用户）_【海量资源尽在 666java.com】.mp4
- 时长 10分20秒（音频 621s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们就来编写我们的一个接口的一个实现那么前面呢我们已经把接口呢就定义好了下面我们就来看具体的实现那么首先呢我们是需要呢在我们的这个Service中去做一个开发啊做这样的一个实现那么我们先把这个配置文件吧那我们先来写好那我们写一个这个application的一个publish的一个配置文件啊这是
[00:27] 标准的spin boot的一个配置文件那我们把这个配置文件内容呢也拷贝过来那么我们就拷贝到这那我们可以大致的来浏览一下这个配置啊然后呢首先指定它的是一个应用的一个名字然后呢我们去指定double的一个扫描包那么就去扫描这个包啊就是com碳花然后double然后呢server这样的一个包然后呢这个application name呢
[00:55] 这个是我们double的一个名字啊就叫它了啊然后呢这个是指定我们的一些double的一些这个使用的协议和这个端口啊以及地址客户端啊等等然后下面这个呢是所定义的是我们的这个使用sprintsprintdata的这个mongodb的模块然后呢去操作我们的一些mongodb它所指定的一个路径呢就这样的一个路径啊然后呢这个端口呢是27017
[01:22] 然后呢再往后面走呢这个呢是我们的一个数据库啊像碳花这样的一个数据库OK好了好那么到这里呢我们这个配置文件是不是就搞定了那么接下来呢我们就来编写我们的一个接口的一个视线类那我们首先呢需要去创建一个包这个包呢我们就写到这个下面来创建一个这个包然后呢我们去写一个这个它的一个视线类那么就
[01:49] 写一个这个impl对吧这样的一个实现那么他呢去实现的一个哎实现那么实现的一个接口呢就是我们之前所定义的这样的一个接口那我们把具体的这个实现类呢实现方法呢也定义出来那么第一个这个方法呢就是我们去查询我们最大的啊这样的一个这个得分的这样的人就是我们那个今日家人了对吧那我们加个注释
[02:18] 这个就是我们的今日家人啊这样的一个调用啊这个大家应该能够理解啊然后呢下面这个呢就是我们的一个什么呢推荐啊用户的一个列表列表的一个查询啊那么做这两个的一个实现OK好那么接下来呢我们先把这个他的一些功能去做一些这个实现吧那么我们在我们先来实现我们这个今日家人中的这个查询啊
[02:48] 在这个位置呢我们做具体的一个实现那我们来看一下怎么去做呢那我们显然呢需要调用上面我们所定义的这个mongo template然后呢有一个叫做fender1啊这样的一个操作那么它呢有两个参数一个呢是query啊这样的一个操作那么一个呢是我们的一个edited class那么就是我们实体类的一个class
[03:10] 那我们来调用这个fund1然后传递两个参数那么第一个参数num呢我们先给它去设置为一个query先设置为num第二个呢我们指定我们的class那么就是这个recommend user.classok好那么接下来我们是只需要去实现这个query是不是就可以了来我们导入它那么这个呢是一个query对象那么它等于什么呢这个query有一个点query这样的一个方法
[03:39] 那么我们需要给他定一个criteria这样的一个对象啊那我们可以看一下这个query方法他是不是需要啊这样的一个对象那么我们来给他定一下然后criteria然后呢他呢就他等于什么呢这个criteria点我们设置一个well的一个条件
[04:02] 是谁呢就是我们来看一下那么这个条件呢显然的是我们需要根据我们之前的这个结构来看一下是不是要根据这个to user id就是我们推荐给张三的这些这个用户那我们来写一个这个to user id那么条件呢就是这个张三然后呢我们设置它为easy等于谁呢等于这个user id哎呀ok
[04:28] 然后呢我们把它呢就传递给他这样的话呢就构造完成了但是呢大家想一下啊那么这个呢仅仅是一个什么呢我们的一个条件对吧哎条件条件然后呢下面的这个呢是我们需要他什么呢需要他按照我们的一个这个得分然后呢做一个倒序的一个什么排序然后呢我们再获取第一条
[04:55] 这个数据是不是我们要做这个操作那么怎么做我们在这个位置有一个叫做什么的VaseVase谁做一个Sort一个排序那么SortBySortBy谁我们再去构造一个Sort.什么Oder.什么DESC在那个Oder根据谁去做一个这个DESC的一个操作是不是要根据我们之前所定义的这样的一个什么Score
[05:25] 此刻是不是要去做一个倒序排序啊并且啊并且什么的limit1是不是我们只拿一条数据啊哎OK那么这样的话我们是不是这个逻辑呢是不是就已经啊写好了那么接下来呢我们是不是需要去编写一个测试用力啊然后呢我们来测试一下哎当然这个这个宽幅没有传给他啊啊传一下哎这样的话呢就OK了好那么接下来呢我们来看一下这个测试用力啊
[05:54] 那么当然了编写测试用力呢我们需要去写我们的一个这个启动类那么也就是下面的在这个位置我们来看一下啊下面呢我们会有一个启动类啊这个启动类呢我们来看一下怎么样去写啊那么我们需要去这个包啊这个包我们得创建一下啊但是我们这个包啊它是已经是有这个包了我们没有办法直接创建啊那我们再来创建一个随便创建一个啊
[06:22] 那么随便随便创建一个之后呢是不是就会有了这个目录了然后呢我们再把这个启动类呢再拷过来哎呦OK那么然后把这个包呢给它删除掉啊就好了哎呦OK好那么这样的话呢我们就有了启动类了那么有了启动类之后呢在下面这个位置啊我们就可以来编写我们的测试用力了那么我们在下面这个位置呢去创建一个哎错了啊我们要创建一个谁呢创建一个我们这个包
[06:51] 然后我们去编写测试用历我们要把它删除掉把它删除掉然后下面我们写一个就叫什么就叫test test recommendrecommend user API我们写这样的一个测试用历然后上面这个位置我需要写一个什么test 叫 run race谁呢是不是我们的一个 spring
[07:22] genit这个class然后呢我们再来写一个叫做什么呢sprintboot test那么接下来呢我们就需要把我们刚刚所写的这个什么recommend user API这个对象呢给我们注入进来然后呢我们去做一个测试那么接下来呢我们就来测试这个方法那么我们把这个前面这个方法呢我们来call一下我们要测试这个方法了
[07:49] 我们来找一下在这那么写一个他那我们就需要写一个testtest这个query那么这个呢就返回word空当然这个参数我们也不需要了好那么我们就给他加一个test注解然后呢我们就调用类似点什么的这个对象对吧然后呢我们去做一个这个查谁然后呢我们去推荐谁呢推荐我们1
[08:18] 给这个1这个用户呢去查询他推荐的一些这个最大值的这个得分的这个用户啊那么为什么是1呢我们来看一下啊在前面我们的数据中这个to, you, id都是唯一的这个数据啊哎OK好那么我们尝试着来拿到这个对象然后呢我们来打印一下这个对象啊好那我们来执行一下走看他是否能够执行成功呢
[08:43] 那么OK来看一下这个结果那么执行是出错了什么错误那么来看一下他说不能创建这个name那么不能创建这个对象那么他说找不到这个对象也就是什么意思那么也就是说在这个位置注入不进来那么为什么注入不进来呢我们来看一下那么其实在我们的这个位置我们没有忘记去加一个Service注解那么要注意了
[09:11] 那么我们当前使用的是Double的服务所以我们要把它注册为什么一个Double的服务我们要使用上面的包而不是一定要看清楚别搞错了好我们来看一下我们就导入这个Service导入它然后我们给它定义一个WarsonWarson版本后我们定义为1.0.0这样的一个版本
[09:39] 然后呢我们再来去做一个执行看他是否能够执行成功呢好那我们来等待他的一个执行好那么我们来看一下这个结果那么是不是已经就拿到这个结果了对吧那么我们可以看到拿到这个得分最高的这个用户呢是用户ID呢是13的这个用户然后得分的是98分然后呢这个给谁推荐呢就是给这个ID为唯一的这个用户呢去做一个推荐OK
[10:06] 好那么到这里呢我们的这个第一个啊这个逻辑是不是就写好了就是我们去查询这个最大的一个得分的这个用户那么这个是不是就搞定了是吧哎OK好那么关于这个呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spring Boot 和 Dubbo 构建一个推荐服务，包括定义接口、实现类、配置 MongoDB 数据源、编写测试用例并进行单元测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 显示了项目结构，当前选中的是 `RecommendUserApi.java` 接口文件。
- 接口定义了两个方法：`queryWithMaxScore(Long userId)` 和 `queryWithPage(Long userId, Long pageNum, Long pageSize)`。
- 方法注释说明了功能：前者查询得分最高的推荐用户，后者按分排序分页查询。

画面 2:
- 显示了右键菜单，选中“Show in Explorer”。
- 选中了 `RecommendUserApi.java` 文件。

画面 3:
- 显示了 `RecommendUserApiImpl.java` 文件，其中 `queryWithMaxScore` 方法被实现，但返回 `null`。
- 方法注释说明了功能：查询得分最高的推荐用户。

画面 4:
- 显示了 `RecommendUserApiImpl.java` 文件，光标在 `Query` 类上。
- `Query` 类是 Spring Data MongoDB 的查询接口。

画面 5:
- 显示了 Typora 编辑器中的 `day02.md` 文件。
- 文件内容包含 Spring Boot 配置信息，如 `spring.application.name`、`dubbo.protocol.name`、`dubbo.registry.address`、`spring.data.mongodb.uri`。
- 也包含 Java 包和导入语句，如 `@Service`、`@Autowired`、`MongoTemplate`、`Query`。

画面 6:
- 显示了 `RecommendUserApiImpl.java` 文件，光标在 `Query` 类上。
- `Query` 类是 Spring Data MongoDB 的查询接口。

画面 7:
- 显示了 Typora 编辑器中的 `day02.md` 文件。
- 文件内容包含表结构设计，如 `user_id`、`score`、`date`。
- 也包含生成测试数据的 Java 代码和 MongoDB 插入语句。

画面 8:
- 显示了 `DubboApplication.java` 文件，Spring Boot 应用启动。
- 项目结构显示了 `DubboApplication` 类。

画面 9:
- 显示了 `pom.xml` 文件，正在删除 `package-info.java` 文件。
- `pom.xml` 文件中包含 `org.mongodb` 和 `io.netty` 的依赖。

画面 10:
- 显示了 `TestRecommendUserApi.java` 文件，这是一个测试类。
- 文件内容包含 `@RunWith(SpringJUnit4ClassRunner.class)` 和 `@SpringBootTest` 注解。

画面 11:
- 显示了 `TestRecommendUserApi.java` 文件，正在添加 `@Autowired` 注解。
- 文件内容包含 `@Autowired private RecommendUserApi recommendUserApi;`。

画面 12:
- 显示了 `TestRecommendUserApi.java` 文件，右键菜单中选中“Run 'testQueryWithMaxScore' with Coverage”。
- 文件内容包含 `@Autowired private RecommendUserApi recommendUserApi;`。

画面 13:
- 显示了 `RecommendUserApiImpl.java` 文件，光标在 `@Override` 注解上。
- 文件内容包含 `@Autowired private MongoTemplate mongoTemplate;` 和 `@Override public RecommendUser queryWithMaxScore(Long userId) { ... }`。

画面 14:
- 显示了 `TestRecommendUserApi.java` 文件，光标在 `@Test` 注解上。
- 文件内容包含 `@Test public void testQueryWithMaxScore() { ... }`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.tanhua.dubbo.server.api;
import com.tanhua.dubbo.server.pojo.RecommendUser;
import com.tanhua.dubbo.server.vo.PageInfo;

/**
 * 查询一位得分最高的推荐用户
 */
@Param userId
@Return
RecommendUser queryWithMaxScore(Long userId);

/**
 * 按照得分倒序
 */
@Param userId
@Param pageNum
@Param pageSize
@Return
```

画面 5:
```properties
# Spring boot application
spring.application.name = itcast-tanhua-dubbo-Service
spring.scan.basePackages = com.tanhua.dubbo.server
dubbo.application.name = dubbo-provider-tanhua
dubbo.protocol.name = dubbo
dubbo.protocol.port = 20880
dubbo.registry.address = ZooKeeper://192.168.31.81:2181
dubbo.registry.client = zkclient
spring.data.mongodb.uri = mongodb://192.168.31.81:27017/tanhua
```

```java
package com.tanhua.dubbo.server.api;
import com.alibaba.dubbo.config.annotation.Service;
import com.tanhua.dubbo.server.pojo.RecommendUser;
import com.tanhua.dubbo.server.vo.PageInfo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;
```

画面 7:
```java
//生成数据代表
@Test
public void testMongoDBData() {
    for (int i = 2; i < 100; i++) {
        int score = RandomUtils.nextInt(10, 99);
        System.out.println("db.recommend_user.insert({\"userId\": " + i + ", \"score\": " + score + ", \"date\": \"2019/1/1\"});");
    }
}

//插入一些测试数据
use tanhua
db.recommend_user.insert({"userId":2,"touserId":1,"score":77,"data":"2019/1/1"});
db.recommend_user.insert({"userId":3,"touserId":1,"score":69,"data":"2019/1/1"});
```

画面 9:
```xml
<dependency>
    <groupId>org.mongodb</groupId>
    <artifactId>mongo-java-driver-sync</artifactId>
    <version>3.9.1</version>
</dependency>
<dependency>
    <groupId>io.netty</groupId>
    <artifactId>netty-all</artifactId>
    <version>4.1.32.Final</version>
</dependency>
```

画面 10:
```java
package com.tanhua.dubbo.server.api;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest
public class TestRecommendUserApi {

}
```

画面 11:
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest
public class TestRecommendUserApi {

    @Autowired
    private RecommendUserApi recommendUserApi;
}
```

画面 13:
```java
package com.tanhua.dubbo.server.api;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

@Service
public class RecommendUserApiImpl implements RecommendUserApi {

    @Autowired
    private MongoTemplate mongoTemplate;

    /**
     * 今日达人
     * @param userId
     * @return
     */
    @Override
    public RecommendUser queryWithMaxScore(Long userId) {
        // 条件
        Criteria criteria = Criteria.where("userId").is(userId);
        // 查询
        Query query = Query.query(criteria).with(Sort.by(Sort.Direction.DESC, "score"));
        return this.mongoTemplate.findOne(query, RecommendUser.class);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 5:
- PPT 标题：`day02.md`。
- 表格数据：
  - `# Spring boot application`
  - `spring.application.name = itcast-tanhua-dubbo-Service`
  - `spring.scan.basePackages = com.tanhua.dubbo.server`
  - `dubbo.application.name = dubbo-provider-tanhua`
  - `dubbo.protocol.name = dubbo`
  - `dubbo.protocol.port = 20880`
  - `dubbo.registry.address = ZooKeeper://192.168.31.81:2181`
  - `dubbo.registry.client = zkclient`
  - `spring.data.mongodb.uri = mongodb://192.168.31.81:27017/tanhua`

画面 7:
- PPT 标题：`2.2、表结构设计`。
- 表格数据：
  - `#表结构`
  - `{ "userId":1001, #推荐的用户id }`
  - `{ "touserId":1002, #用户id }`
  - `{ "score":90, #推荐得分 }`
  - `{ "

