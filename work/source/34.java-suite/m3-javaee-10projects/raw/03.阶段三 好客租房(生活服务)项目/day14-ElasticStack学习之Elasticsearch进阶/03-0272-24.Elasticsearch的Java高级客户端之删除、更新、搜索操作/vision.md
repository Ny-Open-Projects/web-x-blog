# 画面线理解：24.Elasticsearch的Java高级客户端之删除、更新、搜索操作

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\24.Elasticsearch的Java高级客户端之删除、更新、搜索操作【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:36, 01:37, 02:19, 02:53, 03:58, 04:48, 05:14, 06:15, 06:49, 07:24, 08:03, 09:32, 10:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:57:36

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Java 高级 REST 客户端对 Elasticsearch 中的“house”索引执行索引、查询、存在性判断、删除和更新等操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 PDF 讲义的目录结构，当前位于“3.2. REST高级客户端”章节，同时显示了 IntelliJ IDEA 中的 Java 代码，内容为一个 `ActionListener` 的 `onResponse` 和 `onFailure` 方法，以及一个 `testQuery` 测试方法，其中包含一个 `GetRequest` 对象，用于向 Elasticsearch 发送请求。
画面 2: 展示了 IntelliJ IDEA 中的 Java 代码，内容为 `TestRestHighLevel.java` 文件中的 `testQuery` 方法，该方法使用 `restHighLevelClient.indexAsync` 方法异步执行索引操作，并通过 `ActionListener` 处理响应。
画面 3: 展示了 Elasticsearch Head 插件界面，显示了索引 `haoke` 中的文档列表，其中一条文档的 ID 为 `GpKpdE2gBCKv8opxuOj12`，标题为“等康里 简约风格 * 两户型 拎包入住 看房随时”，价格为 7000。
画面 4: 展示了 IntelliJ IDEA 中的 Java 代码，内容为 `testExists` 测试方法，该方法使用 `GetRequest` 构造一个请求，然后调用 `exists` 方法判断文档是否存在，并打印结果。
画面 5: 展示了 IntelliJ IDEA 中的 Java 代码，内容为 `testExists` 测试方法，该方法使用 `GetRequest` 构造一个请求，然后调用 `exists` 方法判断文档是否存在，并打印结果。
画面 6: 展示了 IntelliJ IDEA 中的 Java 代码，内容为 `testDelete` 测试方法，该方法使用 `DeleteRequest` 构造一个请求，然后调用 `delete` 方法删除文档。
画面 7: 展示了 Elasticsearch Head 插件界面，显示了索引 `haoke` 中的文档列表，其中一条文档的 ID 为 `j5vAHzGgBqIMwr19H-k63`，标题为“南京西路2 一室一厅2”，价格为 4000。
画面 8: 展示了 IntelliJ IDEA 中的 Java 代码，内容为 `testUpdate` 测试方法，该方法使用 `UpdateRequest` 构造一个请求，然后调用 `update` 方法更新文档。
画面 9: 展示了 IntelliJ IDEA 中的 Java 代码，内容为 `testUpdate` 测试方法，该方法使用 `UpdateRequest` 构造一个请求，然后调用 `update` 方法更新文档。
画面 10: 展示了 IntelliJ IDEA 中的 Java 代码，内容为 `testUpdate` 测试方法，该方法使用 `UpdateRequest` 构造一个请求，然后调用 `update` 方法更新文档。
画面 11: 展示了 PDF 讲义的第 3.4 节“Spring Data Elasticsearch”，内容说明 Spring Data 对 Elasticsearch 的支持旨在简化操作。
画面 12: 展示了 IntelliJ IDEA 中的 Java 代码，内容为 `testSearch` 测试方法，该方法使用 `SearchRequest` 和 `SearchSourceBuilder` 构造一个搜索请求。
画面 13: 展示了 IntelliJ IDEA 中的 Java 代码，内容为 `testSearch` 测试方法，该方法使用 `SearchRequest` 和 `SearchSourceBuilder` 构造一个搜索请求，并在终端中显示了搜索结果。
画面 14: 展示了 PDF 讲义的第 3.4 节“Spring Data Elasticsearch”，内容说明 Spring Data 对 Elasticsearch 的支持旨在简化操作。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@Override
public void onResponse(IndexResponse indexResponse) {
    System.out.println("id->" + indexResponse.getId());
    System.out.println("index->" + indexResponse.getIndex());
    System.out.println("type->" + indexResponse.getType());
    System.out.println("version->" + indexResponse.getVersion());
    System.out.println("result->" + indexResponse.getShardInfo());
}

@Override
public void onFailure(Exception e) {
    System.out.println(e);
}

Thread.sleep(20000);
```

画面 2:
```java
this.restHighLevelClient.indexAsync(indexRequest, RequestOptions.DEFAULT, new ActionListener<IndexResponse>() {
    @Override
    public void onResponse(IndexResponse indexResponse) {
        System.out.println("id->" + indexResponse.getId());
        System.out.println("index->" + indexResponse.getIndex());
        System.out.println("type->" + indexResponse.getType());
        System.out.println("version->" + indexResponse.getVersion());
        System.out.println("result->" + indexResponse.getShardInfo());
    }

    @Override
    public void onFailure(Exception e) {
        System.out.println(e);
    }
});
```

画面 4:
```java
@Test
public void testExists() throws Exception {
    GetRequest getRequest = new GetRequest("haoke", "house",
            "Gkpde2gBCKv8opxuOj12");
    getRequest.fetchSourceContext(new FetchSourceContext(false));
    boolean exists = this.client.exists(getRequest, RequestOptions.DEFAULT);
    System.out.println("exists -> " + exists);
}
```

画面 5:
```java
@Test
public void testExists() throws Exception {
    GetRequest getRequest = new GetRequest(index: "haoke", type: "house",
            id: "jpuGgBqIMwr19HZE4A");
    getRequest.fetchSourceContext(new FetchSourceContext(false));
    boolean exists = this.restHighLevelClient.exists(getRequest, RequestOptions.DEFAULT);
    System.out.println("exists -> " + exists);
}
```

画面 6:
```java
@Test
public void testDelete() throws Exception {
    DeleteRequest deleteRequest = new DeleteRequest(index: "haoke", type: "house",
            id: "j5vAHzGgBqIMwr19H-k63");
    boolean deleted = this.restHighLevelClient.delete(deleteRequest, RequestOptions.DEFAULT);
    System.out.println("deleted -> " + deleted);
}
```

画面 8:
```java
@Test
public void testUpdate() throws Exception {
    UpdateRequest updateRequest = new UpdateRequest(index: "haoke", type: "house",
            id: "GpKpdE2gBCKv8opxuOj12");
    Map<String, Object> data = new HashMap<>();
    data.put("title", "张江高科2");
    data.put("price", "5000");
    updateRequest.doc(data);
    UpdateResponse response = this.restHighLevelClient.update(updateRequest,
            RequestOptions.DEFAULT);
    System.out.println("version -> " + response.getVersion());
}
```

画面 9:
```java
@Test
public void testUpdate() throws Exception {
    UpdateRequest updateRequest = new UpdateRequest(index: "haoke", type: "house",
            id: "j5vAHzGgBqIMwr19H-k63");
    Map<String, Object> data = new HashMap<>();
    data.put("title", "南京西路2 一室一厅2");
    data.put("price", "4000");
    updateRequest.doc(data);
    UpdateResponse response = this.restHighLevelClient.update(updateRequest,
            RequestOptions.DEFAULT);
    System.out.println("version -> " + response.getVersion());
}
```

画面 10:
```java
@Test
public void testUpdate() throws Exception {
    UpdateRequest updateRequest = new UpdateRequest(index: "haoke", type: "house",
            id: "j5vAHzGgBqIMwr19H-k63");
    Map<String, Object> data = new HashMap<>();
    data.put("title", "南京西路2 一室一厅2");
    data.put("price", "4000");
    updateRequest.doc(data);
    UpdateResponse response = this.restHighLevelClient.update(updateRequest,
            RequestOptions.DEFAULT);
    System.out.println("version -> " + response.getVersion());
}
```

画面 12:
```java
@Test
public void testSearch() throws Exception {
    SearchRequest searchRequest = new SearchRequest(indices: "haoke");
    searchRequest.types("house");
    SearchSourceBuilder sourceBuilder = new SearchSourceBuilder();
    sourceBuilder.query(QueryBuilders.matchQuery(name: "title", text: "拎包入住"));
    sourceBuilder.from(0);
    sourceBuilder.size(5);
    sourceBuilder.timeout(new TimeValue(duration: 60, TimeUnit.SECONDS));
    searchRequest.source(sourceBuilder);
}
```

画面 13:
```java
@Test
public void testSearch() throws Exception {
    SearchRequest searchRequest = new SearchRequest(indices: "haoke");
    searchRequest.types("house");
    SearchSourceBuilder sourceBuilder = new SearchSourceBuilder();
    sourceBuilder.query(QueryBuilders.matchQuery(name: "title", text: "拎包入住"));
    sourceBuilder.from(0);
    sourceBuilder.size(
