# 27.Spring Data Elasticsearch使用之更新、删除、搜索

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\27.Spring Data Elasticsearch使用之更新、删除、搜索【海量资源尽在 ubkz.com】.mp4
- 时长 6分3秒（音频 363s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下pdm插入数据那么在electrode中呢支持这种buck这种操作对吧然后呢我们来看一下那Spring Boot中如何去使用这种pdm的操作那么我们把这个测试用力的代码我们拷贝到这个位置来那么来看一下那么这个里面呢这个里面我们看一下没错用时这个是在这
[00:25] 那么这个是什么意思呢我们来看一下我们写这个代码那么我们在这个位置做了一个循环复循环循环5000次也就是说我们要去构造5000条数据然后构造这么多数据然后我们去把它添加到一个list中然后调用一个bug index然后把这个list传递进去就可以了也是非常简单的然后去做一个执行走
[00:47] 那么我们等待它的一个执行好那么现在呢我们就已经结束了对吧然后呢我们在这个位置去计算了它的一个用时然后我们计算了一个开始的一个时间然后呢这个是结束的时间减去开始的时间那么用时呢现在我们测试的是一个8802那么就是用时呢用了8秒钟那么这个位置呢是我之前在去整理这个讲义的时候呢去测试这个时间那可能会稍微慢了一点啊
[01:13] 稍微慢了一点好的我们来看一下数据有没有保存到我们的索引中来看一下浏览数据那么点击这个ID cast是不是有这么多的一些这个数据都保存进来了大概有5000个民众对吧5000个民众OK好嘞那么这个就是一个批量的一个操作那么下面我们来看一下更新的操作那么我们依然把这个代码就贴过来我们来去把这个代码做一个讲解就可以了
[01:38] 好那么我们把它拷贝到这个位置来来看一下那么在这个里面呢也是做一个局部的一个更新那么我们来看它API的使用啊那么我们首先呢要用的是template中的update这个API然后呢它呢需要要求我们传递的是一个叫做update的一个query这样的一个对象然后呢我们把它传递进来在这个update的query中呢我们需要去给它设置一个ID那么我要去修改1001的这条数据
[02:06] 然后并且我们去设置它的一个class并且设置class是我们这个user然后并且我们去设置它的一个修改的数据是通过index request去做一个构造我们修改它年龄是30我们来看现在我们这张数据1001它的年龄是1001年龄是10对吧年龄是10那么我们去给它做一个修改那么我们给它修改成30然后走
[02:35] 那么去做一个执行那么等待他的一个执行好那么现在执行结束了我们来看一下那么点击这个后刻然后我们来找一下找我们的一个点击这个itcast刷新一下那么1001我们现在好像是看不到了对吧那么我们就来查询一下吧怎么查询呢我们还是进入到我们这个里面来发起get请求就可以了这个位置有一个叫做itcast然后来一个user对吧然后来一个1001
[03:05] 走发起请求那么可以看到这个数据是不是已经就发生了一个变更年龄已经改成30了OK没有任何问题好那么下面我们来看一下删除数据数据的删除是最为简单的我们指定ID去做删除就可以了那么我们直接把它贴过来然后我们去做一个运行就OK了然后我们运行它走去等待它的一个执行那么在这个位置已经删除成功了那么我们来到我们的客户端里面测试一下
[03:34] 走去查询你会发现什么呢这个放的等于fals了就是我们这个数据呢已经是找不到了已经被删除了哎OK好那么我们接着继续往下面看那么下面呢这个是在做搜索那么我们把这个搜索这个代码也贴过来呃他依然呢是通过使用我们的这个template模板去做一个这样的一个构造啊那么我们把这个代码呢简单的去调一下那么把这个代码呃简单的调整一下到这然后呢
[04:03] 然后呢到下面的这个位置来啊OK好嘞好那么我们来看一下这个代码那么首先它去调用的是我们的模板中的一个query for page那么现在显然是不是需要做一个分页然后呢需要传递两个参数一个呢就是我们的search query一个就是user的class那么这个search query呢我们需要去构造一个search query通过这个build去构造然后呢去指定一个query我们去构造一个查询的一个
[04:29] 查询语句通过一个name去做一个match匹配name等于张三这样的一个做一个匹配然后去设置一个page然后上面我们定义一个page request这样的一个对象设置一个1 10代表着我们是不是要去拿10条数据做一个build得到一个这样的一个search query对象然后传递到这个位置来那么做一个查询得到这样的一个可以得到一个总页数然后把这个数据打印出来
[04:55] OK就是这样的一个测试那么我们去执行一下那么等待他的测试的一个结果那么一会我们来看一下结果那么我们可以看到他的一个执行结果是总页数是500页那么一页是一页我们是10条对吧那就是5000条数据那么所拿到的数据就是这么多那么所有都是和张三相关的当然了这个我们数据本身都是这样的数据他肯定都会拿到这么多些数据OK
[05:22] 好嘞那么这个呢其实我们就是给大家简单的去演示一下这个搜索因为在我们后面去结合到我们项目去使用的时候呢我们再详细的去讲这个搜索的一些这个使用因为我们这个里面也还没有涉及到它的高亮显示对吧那么在我们后期的这个使用的过程中那么这个高亮显示肯定会用到的对吧OK好那么这个呢就是我们所讲的这个Stimulate DataElectros的一些API的一些基本的一些用法让大家先有这样的一个体验
[05:51] 然后后面我们将去使用Splendid Elasticsearch整合到我们的项目中去实现我们项目中的一些功能OK好那么关于我们Splendid Elasticsearch的使用我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

