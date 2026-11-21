# 画面线理解：08.今日佳人功能实现之实现dubbo服务（查询最大得分推荐用户）

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\08.今日佳人功能实现之实现dubbo服务（查询最大得分推荐用户）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:13, 01:48, 02:43, 03:31, 04:05, 05:08, 06:01, 06:28, 06:58, 07:35, 08:08, 08:40, 09:27, 10:07
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:22:40

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
spring.application.name = itcast-tanhua-dubbo-service
spring.scan.basePackages = com.tanhua.dubbo.server
dubbo.application.name = dubbo-provider-tanhua
dubbo.protocol.name = dubbo
dubbo.protocol.port = 20880
dubbo.registry.address = zookeeper://192.168.31.81:2181
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
  - `spring.application.name = itcast-tanhua-dubbo-service`
  - `spring.scan.basePackages = com.tanhua.dubbo.server`
  - `dubbo.application.name = dubbo-provider-tanhua`
  - `dubbo.protocol.name = dubbo`
  - `dubbo.protocol.port = 20880`
  - `dubbo.registry.address = zookeeper://192.168.31.81:2181`
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
