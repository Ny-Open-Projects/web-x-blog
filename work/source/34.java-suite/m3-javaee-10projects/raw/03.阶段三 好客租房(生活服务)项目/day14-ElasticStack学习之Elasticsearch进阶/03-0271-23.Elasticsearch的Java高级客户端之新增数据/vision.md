# 画面线理解：23.Elasticsearch的Java高级客户端之新增数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\23.Elasticsearch的Java高级客户端之新增数据【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:20, 01:07, 01:47, 02:15, 02:51, 03:17, 04:26, 05:05, 05:54, 06:52, 07:17, 07:54, 08:49, 09:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:56:43

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Elasticsearch 的 Java High Level REST Client 进行索引创建、数据保存和异步操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 TestRestApi.java 中的 testSearchData() 方法，使用 RestClient 发起 POST 请求搜索数据，打印响应实体。
画面2：展示 TestRestHighLevel.java 文件，导入了 org.elasticsearch.index.rankeval 包下的多个类。
画面3：展示 TestRestHighLevel.java 中的 init() 方法，使用 RestClient.builder() 创建连接到 172.16.55.185:9200、9201、9202 的客户端，并设置失败监听器。
画面4：展示 TestRestHighLevel.java 中的 search() 方法，提示用户选择方法。
画面5：展示 TestRestHighLevel.java 中的 testSave() 方法，调用 index() 方法。
画面6：展示 TestRestHighLevel.java 中的 testSave() 方法，提示用户选择方法。
画面7：展示 TestRestHighLevel.java 中的 testSave() 方法，创建 IndexRequest 对象，设置索引和类型。
画面8：展示 TestRestHighLevel.java 中的 testSave() 方法，调用 response.get() 获取响应。
画面9：展示 TestRestHighLevel.java 中的 testSave() 方法，构建数据 Map，创建 IndexRequest，调用 index() 方法并打印响应信息。
画面10：展示 PDF 文档内容，包含 Java 代码片段，演示如何使用 indexAsync 方法并处理 onResponse 和 onFailure 回调。
画面11：展示 TestRestHighLevel.java 中的 testCreateAsync() 方法，创建 IndexRequest 并调用 indexAsync 方法。
画面12：展示 TestRestHighLevel.java 中的 testCreateAsync() 方法，定义 onResponse 和 onFailure 回调方法。
画面13：展示 TestRestHighLevel.java 中的 testCreateAsync() 方法，调用 indexAsync 方法。
画面14：展示 PDF 文档内容，包含 testCreateAsync() 方法的代码，与画面11、13 中的代码一致。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
System.out.println(EntityUtils.toString(response.getEntity()));
// 控搜数据
@Test
public void testSearchData() throws IOException {
    Request request = new Request(method: "POST", endpoint: "/haoke/house_search");
    String searchJson = "{ \"query\": { \"match\": { \"title\": \"\\铃铛入住\\\" } }";
    request.setJsonEntity(searchJson);
    request.addParameter(name: "pretty", value: "true");
    Response response = this.restClient.performRequest(request);
    System.out.println(response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

画面2：
```java
package cn.itcast.es;
public class TestRestHighLevel {
    private Re
```

画面3：
```java
private RestClient restClient;
private static final ObjectMapper MAPPER = new ObjectMapper();
@Before
public void init() {
    RestClientBuilder restClientBuilder = RestClient.builder(
        new HttpHost(hostname: "172.16.55.185", port: 9200),
        new HttpHost(hostname: "172.16.55.185", port: 9201),
        new HttpHost(hostname: "172.16.55.185", port: 9202)
    );
    restClientBuilder.setFailureListener(new RestClient.FailureListener {
        @Override
        public void onFailure(Node node) {
            System.out.println("出错 -> " + node);
        }
    });
}
```

画面4：
```java
search(SearchRequest searchRequest, RequestOptions options)
search(UpdateRequest updateRequest, Header... headers)
update(UpdateRequest updateRequest, RequestOptions options)
delete(DeleteRequest deleteRequest, Header... headers)
get(GetRequest getRequest, Header... headers)
bulk(BulkRequest bulkRequest, RequestOptions options)
bulkAsync(BulkRequest bulkRequest, RequestOptions options, ActionListener<BulkResponse> actionListener)
```

画面5：
```java
@Test
public void testSave() {
    this.restHighLevelClient.index(indexRequest, Re);
}
```

画面6：
```java
@Test
public void testSave() throws Exception {
    IndexRequest indexRequest = null;
    this.restHighLevelClient.index(indexRequest, Re);
}
```

画面7：
```java
@Test
public void testSave() throws Exception {
    IndexRequest indexRequest = new IndexRequest(index: "haoke", type: "house");
}
```

画面8：
```java
response.get
```

画面9：
```java
@Test
public void testSave() throws Exception {
    Map<String, Object> data = new HashMap<>();
    data.put("id", 2002);
    data.put("title", "南京东路 二室一厅");
    data.put("price", 4000);
    IndexRequest indexRequest = new IndexRequest(index: "haoke", type: "house").source(data);
    IndexResponse response = this.restHighLevelClient.index(indexRequest, RequestOptions.DEFAULT);
    System.out.println("id -> " + response.getId());
    System.out.println("version -> " + response.getVersion());
    System.out.println("result -> " + response.getResult());
}
```

画面10：
```java
data.put("price", "$500");
IndexRequest indexRequest = new IndexRequest("haoke", "house").source(data);
this.client.indexAsync(indexRequest, RequestOptions.DEFAULT, new ActionListener<IndexResponse>() {
    @Override
    public void onResponse(IndexResponse indexResponse) {
        System.out.println("id->" + indexResponse.getId());
        System.out.println("index->" + indexResponse.getIndex());
        System.out.println("type->" + indexResponse.getType());
        System.out.println("version->" + indexResponse.getVersion());
        System.out.println("result->" + indexResponse.getResult());
        System.out.println("shardInfo->" + indexResponse.getShardInfo());
    }
    @Override
    public void onFailure(Exception e) {
        System.out.println(e);
    }
});
Thread.sleep(20000);
```

画面11：
```java
@Test
public void testCreateAsync() throws Exception {
    Map<String, Object> data = new HashMap<>();
    data.put("id", "2003");
    data.put("title", "南京东路 最新房源 二室一厅");
    data.put("price", "$500");
    IndexRequest indexRequest = new IndexRequest(index: "haoke", type: "house").source(data);
    this.restHighLevelClient.indexAsync(indexRequest, RequestOptions.DEFAULT, new ActionListener<IndexResponse>() {
        @Override
        public void onResponse(IndexResponse indexResponse) {
            System.out.println("id->" + indexResponse.getId());
            System.out.println("index->" + indexResponse.getIndex());
            System.out.println("type->" + indexResponse.getType());
            System.out.println("version->" + indexResponse.getVersion());
            System.out.println("result->" + indexResponse.getResult());
            System.out.println("shardInfo->" + indexResponse.getShardInfo());
        }
        @Override
        public void onFailure(Exception e) {
            System.out.println(e);
        }
    });
}
```

画面12：
```java
public void onResponse(IndexResponse indexResponse) {
    System.out.println("id->" + indexResponse.getId());
    System.out.println("index->" + indexResponse.getIndex());
    System.out.println("type->" + indexResponse.getType());
    System.out.println("version->" + indexResponse.getVersion());
    System.out.println("result->" + indexResponse.getResult());
    System.out.println("shardInfo->" + indexResponse.getShardInfo());
}
@Override
public void onFailure(Exception e) {
    System.out.println(e);
}
```

画面13：
```java
@Test
public void lestCreateAsync() throws Exception {
    Map<String, Object> data = new HashMap<>();
    data.put("id", "2003");
    data.put("title", "南京东路 最新房源 二室一厅");
    data.put("price", "$500");
    IndexRequest indexRequest = new IndexRequest(index: "haoke", type: "house").source(data);
    this.restHighLevelClient.indexAsync(indexRequest, RequestOptions.DEFAULT, new ActionListener<IndexResponse>() {
        @Override
        public void onResponse(IndexResponse indexResponse) {
            System.out.println("id->" + indexResponse.getId());
            System.out.println("index->" + indexResponse.getIndex());
            System.out.println("type->" + indexResponse.getType());
            System.out.println("version->" + indexResponse.getVersion());
            System.out.println("result->" + indexResponse.getResult());
            System.out.println("shardInfo->" + indexResponse.getShardInfo());
        }
        @Override
        public void onFailure(Exception e) {
            System.out.println(e);
        }
    });
}
```

画面14：
```java
@Test
public void testCreateAsync() throws Exception {
    Map<String, Object> data = new HashMap<>();
    data.put("id", "2003");
    data.put("title", "南京东路 最新房源 二室一厅");
    data.put("price", "$500");
    IndexRequest indexRequest = new IndexRequest("h
