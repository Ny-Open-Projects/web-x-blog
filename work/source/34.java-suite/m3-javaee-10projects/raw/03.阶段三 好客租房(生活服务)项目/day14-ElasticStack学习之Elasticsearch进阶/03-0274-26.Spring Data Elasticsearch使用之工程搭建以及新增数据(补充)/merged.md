# 26.Spring Data Elasticsearch使用之工程搭建以及新增数据（补充）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\26.Spring Data Elasticsearch使用之工程搭建以及新增数据（补充）【海量资源尽在 ubkz.com】.mp4
- 时长 2分34秒（音频 155s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么下面我们来看一个问题啊就是刚刚我们在做测试的时候呢呃我们这个是不是能够创建成功啊就是我们这个索引他能够创建成功但是呢会发现有点问题就是那么我们发现创建好的这个索引的这个我们这个分片的数量呢是五个啊五个但是明明我们的这个位置设置六但是他依然设置出现的是五呃然后呢我们可以去去再测试比如说我设置为八啊然后呢我再去设置一个
[00:29] 我在写一些不同的一些index name和这个type我再去做一个测试那么等待它个执行来看一下效果好嘞那么我们又重新做了执行那么刷新来看一下效果那么你会发现呢创建的这个ITcast1那么它的这个分片数呢依然还是五个啊所以说呢这块是这个参数呢是有点问题就是它似乎是没有生效那么这个问题呢目前呢也没找到一个
[00:57] 解决也没有找到一个他这个问题的所在吧然后呢可能暂时把它定性为是一个bug吧就是spin boot的spin boot elixir的这样的一个bug那么其实呢我们如何去避免这个bug呢就是我们可以自己去创建一个这样的一个索引然后呢我们去使用它就可以了比如说啊那么我们在这个地方创建一个新建的索引比如说我们就叫itcast2itcast2然后呢它的分片数呢设置为6然后呢这个副本呢是1
[01:27] 创建那么来看一下这个索引是不是就创建好了你可以看到二是不是说零到五有有这个六个对吧然后呢我们在这个位置去使用的时候啊那么我们这个就不需要了把这两个把这两个保留就可以了然后呢我们给他再加一个第三个有他有一个呃属性叫做create index给他设置为force就不用去创建了那么直接去使用就可以了那么他呢使用的是idcast2那这个type呢依然使用是user那我们再去
[01:57] 我们再去执行一下那么看他是否能够把数据呢保存到我们这个索引中OK那么等待他这个那么现在我们程序呢跑完了我们来看一下进入我们浏览数据啊我们找到一个ITcast2这里面数据他依然可以写进来对吧那么我们这个索引的这个索引的大小呢也没有发生任何变化那么建议大家呢这样去做就是在你保存数据之前呢你可以先去创建这样的一个索引然后呢再去做一个数据的保存那么就没有任何问题了哎呀OK好嘞
[02:27] 好那么这个呢就是我们把刚刚测试的这个发现了一个小的一个bug吧然后呢做一个这个解释OK好嘞

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import org.springframework.data.Elasticsearch.annotations.Field;
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

