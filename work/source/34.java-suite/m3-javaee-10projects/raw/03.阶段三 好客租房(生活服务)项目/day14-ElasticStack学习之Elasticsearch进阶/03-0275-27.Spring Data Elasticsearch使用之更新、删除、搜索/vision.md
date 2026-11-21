# 画面线理解：27.Spring Data Elasticsearch使用之更新、删除、搜索

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\27.Spring Data Elasticsearch使用之更新、删除、搜索【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:19, 00:37, 01:18, 01:30, 01:51, 02:34, 02:54, 03:21, 03:42, 03:59, 05:23, 05:46, 05:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:59:39

1) 这一组画面整体在讲如何使用 Spring Boot 集成 Elasticsearch 实现对 User 实体数据的批量插入、更新、删除和分页搜索功能。

2) 按时间顺序列出每张画面的要点：
画面1：展示 User 实体类代码，包含 @Data、@AllArgsConstructor、@NoArgsConstructor 注解，以及 @Document 注解指定索引名为 "user" 且不自动创建索引，字段包括 id、name、age、hobby。
画面2：展示 TestSpringBootES.java 中的 testBulk 方法，用于批量插入数据，创建 5000 个 User 对象并使用 IndexQueryBuilder 构建批量索引请求，最后打印耗时。
画面3：展示 TestSpringBootES.java 中的 testBulk 方法，代码与画面2相同，但注释显示“用时：7836”。
画面4：展示 ElasticSearch Head 界面，显示索引列表，其中 "user" 索引被选中，下方显示字段列表，包括 id、name、age、hobby。
画面5：展示 PDF 文档中“4.4.6. 搜索”章节内容，显示搜索结果表格，包含 id、name、age、hobby 字段，数据为张三、张二、张三等用户信息。
画面6：展示 TestSpringBootES.java 中的 testUpdate 方法，用于更新索引，创建 IndexRequest 设置字段 "age" 为 "30"，使用 UpdateQueryBuilder 设置 id 为 "1001"，并调用 update 方法。
画面7：展示 TestSpringBootES.java 中的 testUpdate 方法，右键菜单弹出，显示“Refactor”、“Generate”、“Run 'testUpdate'”等选项。
画面8：展示 ElasticSearch Head 界面，显示索引列表，其中 "user" 索引被选中，下方显示字段列表，包括 id、name、age、hobby。
画面9：展示 TestSpringBootES.java 中的 testUpdate 方法，代码与画面6相同，但注释显示“用时：22836”。
画面10：展示 PDF 文档中“4.4.6. 搜索”章节内容，显示搜索方法 testSearch 的代码，使用 NativeSearchQueryBuilder 构建查询，匹配 name 字段为 "张三"，并设置分页参数。
画面11：展示 TestSpringBootES.java 中的 testSearch 方法，代码与画面10相同，但注释显示“用时：10960”。
画面12：展示 PDF 文档中“4.4.6. 搜索”章节内容，显示搜索方法 testSearch 的代码，使用 NativeSearchQueryBuilder 构建查询，匹配 name 字段为 "张三"，并设置分页参数。
画面13：展示 PDF 文档中“4.4.6. 搜索”章节内容，显示搜索方法 testSearch 的代码，使用 NativeSearchQueryBuilder 构建查询，匹配 name 字段为 "张三"，并设置分页参数。
画面14：展示 ElasticSearch Head 界面，显示集群状态，包含 node1、node2、node3 三个节点，每个节点显示分片信息，下方显示搜索结果表格，包含 id、name、age、hobby 字段，数据为张三、张二、张三等用户信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1：
```java
@Data
@AllArgsConstructor
@NoArgsConstructor
@Document(indexName = "itcast", type = "user", createIndex = false)
public class User {
    @Id
    private Long id;
    @Field(store = true)
    private String name;
    @Field(store = true)
    private Integer age;
    @Field(store = true)
    private String hobby;
}
```

画面2：
```java
User user = new User();
user.setId(1001L + i);
user.setAge(i % 50 + 10);
user.setName("张三" + i);
user.setHobby("足球、篮球、听音乐");
IndexQuery indexQuery = new IndexQueryBuilder().withObject(user).build();
list.add(indexQuery);
Long start = System.currentTimeMillis();
this.elasticsearchTemplate.bulkIndex(list);
System.out.println("用时：" + (System.currentTimeMillis() - start)); //用时：7836
```

画面3：
```java
@Test
void testBulk() {
    List list = new ArrayList<>();
    for (int i = 0; i < 5000; i++) {
        User user = new User();
        user.setId(1001L + i);
        user.setAge(i % 50 + 10);
        user.setName("张三" + i);
        user.setHobby("足球、篮球、听音乐");
        IndexQuery indexQuery = new IndexQueryBuilder().withObject(user).build();
        list.add(indexQuery);
    }
    Long start = System.currentTimeMillis();
    this.elasticsearchTemplate.bulkIndex(list);
    System.out.println("用时：" + (System.currentTimeMillis() - start)); //用时：7836
}
```

画面6：
```java
@Test
public void testUpdate() {
    IndexRequest indexRequest = new IndexRequest();
    indexRequest.source("age", "30");
    UpdateQuery updateQuery = new UpdateQueryBuilder()
            .withId("1001")
            .withClass(User.class)
            .withIndexRequest(indexRequest).build();
    this.elasticsearchTemplate.update(updateQuery);
}
```

画面10：
```java
@Test
public void testSearch() {
    PageRequest pageRequest = PageRequest.of(1, 10); //设置分页参数
    SearchQuery searchQuery = new NativeSearchQueryBuilder()
            .withQuery(QueryBuilders.matchQuery("name", "张三")) // match查询
            .withPageable(pageRequest)
            .build();
    AggregatedPage<User> users =
            this.elasticsearchTemplate.queryForPage(searchQuery, User.class);
    System.out.println("总页数：" + users.getTotalPages()); //获取总页数
    for (User user : users.getContent()) { //获取搜索到的数据
        System.out.println(user);
    }
}
```

画面11：
```java
@Test
public void testSearch() {
    PageRequest pageRequest = PageRequest.of(1, 10); //设置分页参数
    SearchQuery searchQuery = new NativeSearchQueryBuilder()
            .withQuery(QueryBuilders.matchQuery("name", "张三")) // match查询
            .withPageable(pageRequest)
            .build();
    AggregatedPage<User> users =
            this.elasticsearchTemplate.queryForPage(searchQuery, User.class);
    System.out.println("总页数：" + users.getTotalPages()); //获取总页数
    for (User user : users.getContent()) { //获取搜索到的数据
        System.out.println(user);
    }
}
```

画面12：
```java
@Test
public void testSearch() {
    PageRequest pageRequest = PageRequest.of(1, 10); //设置分页参数
    SearchQuery searchQuery = new NativeSearchQueryBuilder()
            .withQuery(QueryBuilders.matchQuery("name", "张三")) // match查询
            .withPageable(pageRequest)
            .build();
    AggregatedPage<User> users =
            this.elasticsearchTemplate.queryForPage(searchQuery, User.class);
    System.out.println("总页数：" + users.getTotalPages()); //获取总页数
    for (User user : users.getContent()) { //获取搜索到的数据
        System.out.println(user);
    }
}
```

画面13：
```java
@Test
public void testSearch() {
    PageRequest pageRequest = PageRequest.of(1, 10); //设置分页参数
    SearchQuery searchQuery = new NativeSearchQueryBuilder()
            .withQuery(QueryBuilders.matchQuery("name", "张三")) // match查询
            .withPageable(pageRequest)
            .build();
    AggregatedPage<User> users =
            this.elasticsearchTemplate.queryForPage(searchQuery, User.class);
    System.out.println("总页数：" + users.getTotalPages()); //获取总页数
    for (User user : users.getContent()) { //获取搜索到的数据
        System.out.println(user);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面5：PDF 文档中“4.4.6. 搜索”章节，表格数据包含 id、name、age、hobby 字段，数据为张三、张二、张三等用户信息。
画面10：PDF 文档中“4.4.6. 搜索”章节，表格数据包含 id、name、age、hobby 字段，数据为张三、张二、张三等用户信息。
画面12：PDF 文档中“4.4.6. 搜索”章节，表格数据包含 id、name、age、hobby 字段，数据为张三、张二、张三等用户信息。
画面13：PDF 文档中“4.4.6. 搜索”章节，表格数据包含 id、name、age、hobby 字段，数据为张三、张二、张三等用户信息。
画面14：Elasticsearch Head 界面，显示集群状态，包含 node1、node2
