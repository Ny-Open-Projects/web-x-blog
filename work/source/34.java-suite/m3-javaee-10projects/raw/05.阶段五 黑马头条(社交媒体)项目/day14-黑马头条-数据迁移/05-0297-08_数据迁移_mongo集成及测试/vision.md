# 画面线理解：08_数据迁移_mongo集成及测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\08_数据迁移_mongo集成及测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:31, 00:54, 01:40, 02:30, 02:50, 03:14, 03:40, 04:29, 05:07, 05:37, 06:04, 06:27, 07:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:04:25

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中配置并使用 MongoDB，包括配置文件、实体类、测试类编写及数据操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示项目结构，当前选中的是测试类 `MongoTest`，测试已通过。
画面 2: 切换到 `heima-leadnews-common` 模块，展示 `resources/config` 目录下的多个配置文件。
画面 3: 查看 `MongoDBConfigure.java` 代码，配置了 MongoDB 的连接参数和模板工厂。
画面 4: 查看 `StorageData.java` 实体类，定义了目标类名和字段列表。
画面 5: 在 `IntConfig.java` 中使用 `@ComponentScan` 注解扫描多个包。
画面 6: 在 `MongoTest.java` 中导入 Spring Boot 测试和 MongoDB 相关依赖。
画面 7: 在 `MongoTest.java` 中添加 `@Autowired` 注解注入 `MongoTemplate`。
画面 8: 在 `MongoTest.java` 中调用 `mongoTemplate.insert()` 方法插入数据。
画面 9: 在 `MongoTest.java` 中设置 `Article` 实体对象的标题，并调用 `insert` 方法。
画面 10: 在 MongoDB Studio 37 中查看插入的数据，确认数据已存在。
画面 11: 在 `MongoTest.java` 中编写 `testGetOne()` 方法，通过 `findBrid` 查询数据。
画面 12: 在 `MongoTest.java` 中使用 `System.out.println(article)` 打印查询结果。
画面 13: 在 `MongoTest.java` 中执行 `testGetOne()` 方法，终端输出查询到的 `Article` 对象。
画面 14: 在 `MongoTest.java` 中完成 `testGetOne()` 方法的编写，测试通过。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```java
@Configuration
@PropertySource("classpath:mongo.properties")
public class MongoBConfigure {
    @Value("${mongo.host}")
    private String host;
    @Value("${mongo.port}")
    private int port;
    @Value("${mongo.dbName}")
    private String dbName;

    @Bean
    public MongoTemplate getMongoTemplate() { return new MongoTemplate(getSimpleMongoFactory()); }

    public SimpleMongoDbFactory getSimpleMongoFactory() {
        return new SimpleMongoDbFactory(new MongoClient(host, port), dbName);
    }
}
```

画面 4:
```java
public class StorageData {
    /**
     * 目标class 类名
     */
    private String targetClassName;
    /**
     * 存储的字段列表
     */
    private List<StorageEntry> entryList = new ArrayList<StorageEntry>();
}
```

画面 5:
```java
@Configuration
@ComponentScan({"com.heima.common.common.init","com.heima.common.mongo","com.heima.common.mysql"})
@EnableScheduling
public class InitConfig {
}
```

画面 6:
```java
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.test.context.junit4.SpringRunner;
```

画面 7:
```java
@Autowired
private MongoTemplate mongoTemplate;
```

画面 8:
```java
mongoTemplate.insert();
```

画面 9:
```java
public void testSave() {
    ApArticle aparticle = new ApArticle();
    aparticle.setTid(20222);
    aparticle.setTitle("黑马头条说明书");
    mongoTemplate.insert(aparticle);
}
```

画面 11:
```java
public void testGetOne() {
    ApArticle article = mongoTemplate.findBrid(20222, ApArticle.class);
}
```

画面 12:
```java
System.out.println(article);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
