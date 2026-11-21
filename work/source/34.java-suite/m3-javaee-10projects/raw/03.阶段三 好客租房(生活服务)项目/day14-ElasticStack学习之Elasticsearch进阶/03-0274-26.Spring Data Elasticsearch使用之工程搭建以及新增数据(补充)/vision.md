# 画面线理解：26.Spring Data Elasticsearch使用之工程搭建以及新增数据（补充）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\26.Spring Data Elasticsearch使用之工程搭建以及新增数据（补充）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:18, 00:39, 00:49, 01:13, 01:15, 01:30, 01:44, 01:48, 02:03, 02:09, 02:15, 02:30, 02:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:58:47

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Elasticsearch 的 @Document 注解定义索引，并通过代码控制索引的分片与副本数，以及批量插入数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 IntelliJ IDEA 中 User.java 文件，其中 @Document 注解的 indexName 为 "itcast"，type 为 "user"，shards 为 6，replicas 为 1。
画面 2: 与画面 1 相同，无变化。
画面 3: 显示 Elasticsearch Head 插件界面，展示集群中三个节点（node01, node02, node03）的分片分布情况，索引为 "itcast"。
画面 4: 显示 IntelliJ IDEA 中 User.java 文件，@Document 注解的 indexName 从 "itcast" 修改为 "itcast1"。
画面 5: 显示 Elasticsearch Head 插件界面，索引从 "itcast" 变为 "itcast1"，节点分片分布发生变化。
画面 6: 显示 Elasticsearch Head 插件界面，索引为 "itcast1"，节点分片分布再次变化。
画面 7: 显示 Elasticsearch Head 插件界面，索引从 "itcast1" 变为 "itcast2"，节点分片分布再次变化。
画面 8: 显示 IntelliJ IDEA 中 User.java 文件，@Document 注解的 indexName 为 "itcast1"，并显示了默认配置（如 shards 默认 5，replicas 默认 1）。
画面 9: 显示 IntelliJ IDEA 中 User.java 文件，@Document 注解的 createIndex 属性设置为 false。
画面 10: 显示 IntelliJ IDEA 中 User.java 文件，@Document 注解的 indexName 从 "itcast1" 修改为 "itcast2"，createIndex 仍为 false。
画面 11: 显示 Elasticsearch Head 插件界面，索引列表中包含 "itcast2"，并显示了该索引下的文档数据。
画面 12: 显示 Elasticsearch Head 插件界面，页面为空白。
画面 13: 显示 PDF 文档，章节 4.4.3 “批量插入数据”，代码示例为 testBulk 方法，用于创建批量索引请求。
画面 14: 显示 PDF 文档，章节 4.4.3 “批量插入数据”，代码示例中添加了计算并打印执行时间的语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
import org.springframework.data.elasticsearch.annotations.Field;
@Data
@AllArgsConstructor
@NoArgsConstructor
@Document(indexName = "itcast", type = "user", shards = 6, replicas = 1)
public class User {
    @Id
    private Long id;
    @Field(store = true)
    private String name;
    @Field
    private Integer age;
    @Field(store = true)
    private String hobby;
}
```

画面 4:
```java
@Document(indexName = "itcast1", type = "user1", shards = 6, replicas = 1)
```

画面 8:
```java
@Document(indexName = "itcast1", type = "user1", createIndex = false)
```

画面 9:
```java
@Document(indexName = "itcast1", type = "user1", createIndex = false)
```

画面 10:
```java
@Document(indexName = "itcast2", type = "user", createIndex = false)
```

画面 13:
```java
@Test
public void testBulk() {
    List list = new ArrayList();
    for (int i = 0; i < 5000; i++) {
        User user = new User();
        user.setId(1001 + i);
        user.setAge((i % 50) + 10);
        user.setName("张三" + i);
        user.setHobby("足球、篮球、听音乐");
    }
    IndexQuery indexQuery = new IndexQueryBuilder().withObject(user).build();
    list.add(indexQuery);
}
```

画面 14:
```java
@Test
public void testBulk() {
    List list = new ArrayList();
    for (int i = 0; i < 5000; i++) {
        User user = new User();
        user.setId(1001 + i);
        user.setAge((i % 50) + 10);
        user.setName("张三" + i);
        user.setHobby("足球、篮球、听音乐");
    }
    IndexQuery indexQuery = new IndexQueryBuilder().withObject(user).build();
    list.add(indexQuery);
    Long start = System.currentTimeMillis();
    this.elasticsearchTemplate.bulkIndex(list);
    System.out.println("用时：" + (System.currentTimeMillis() - start));
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 13 和 14: PDF 文档中显示了章节标题“4.4.3、批量插入数据”，并包含代码示例和注释。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
