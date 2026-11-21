# 画面线理解：21.Elasticsearch的Java低级客户端之新增文档数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\21.Elasticsearch的Java低级客户端之新增文档数据【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:22, 00:44, 01:02, 01:28, 01:38, 01:53, 02:09, 02:31, 02:43, 03:01, 03:37, 04:01, 04:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:55:00

1) 这一组画面整体在讲如何使用 Java 代码通过 REST 客户端向 Elasticsearch 集群发送 POST 请求以保存数据。

2) 按时间顺序列出每张画面的要点：
画面1：展示 TestRestApi.java 文件中 testInfo() 方法，用于获取集群状态，代码中包含 request.addParameter 和 response.getHttpStatusLine 等操作。
画面2：在 testInfo() 方法后，开始编写 testSave() 方法的骨架。
画面3：切换到浏览器，显示 Elasticsearch Head 插件界面，展示索引为 "haoke" 的数据，包含 id、title、price 字段。
画面4：在 testSave() 方法中，初始化一个 POST 请求，endpoint 为 "/haoke/house"，并添加参数 "pretty" 为 "true"。
画面5：在 testSave() 方法中，调用 request.setJsonEntity() 方法准备设置 JSON 实体。
画面6：在 testSave() 方法中，光标位于 request.setJsonEntity() 后，准备输入数据。
画面7：展示 TestRestApi.java 文件中 Init() 方法，初始化 RestClientBuilder，配置两个 HttpHost，分别指向 172.16.55.185 的 9200 和 9201 端口。
画面8：在 testSave() 方法中，光标位于 request.setJsonEntity() 后，准备输入数据。
画面9：在 testSave() 方法中，光标位于 request.setJsonEntity() 后，准备输入数据。
画面10：在 testSave() 方法中，完成 request.setJsonEntity() 调用，并添加了 this.restClient.performRequest(request)。
画面11：在 testSave() 方法中，光标位于 request.setJsonEntity() 后，准备输入数据。
画面12：在 testSave() 方法中，向 Map<String, Object> data 中添加了 "id" 和 "title" 字段。
画面13：在 testSave() 方法中，光标位于 request.setJsonEntity() 后，准备输入数据。
画面14：切换到 PDF 文档，展示 testCreateData() 方法，用于创建数据，其中 data.put("id", "2001"); data.put("title", "张江高科"); data.put("price", "3500");。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1：
```java
@Test
public void testInfo() throws IOException {
    Request request = new Request(method: "GET", endpoint: "/_cluster/state");
    request.addParameter(name: "pretty", value: "true");
    Response response = this.restClient.performRequest(request);
    System.out.println("请求完成 -> " + response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

画面4：
```java
@Test
public void testSave() {
    Request request = new Request(method: "POST", endpoint: "/haoke/house");
    request.addParameter(name: "pretty", value: "true");
}
```

画面5：
```java
request.setJsonEntity();
```

画面7：
```java
@Before
public void Init() {
    RestClientBuilder restClientBuilder = RestClient.builder(
        new HttpHost(hostname: "172.16.55.185", port: 9200),
        new HttpHost(hostname: "172.16.55.185", port: 9201)
    );
    restClientBuilder.setFailureListener(new RestClient.FailureListener(
```

画面10：
```java
this.restClient.performRequest(request);
```

画面12：
```java
data.put("id", "2001");
data.put("title", "南京西路 一室一厅");
```

画面14：
```java
@Test
public void testCreateData() throws IOException {
    Request request = new Request(method: "POST", endpoint: "/haoke/house");
    Map<String, Object> data = new HashMap<>();
    data.put("id", "2001");
    data.put("title", "张江高科");
    data.put("price", "3500");
    request.setJsonEntity(MAPPER.writeValueAsString(data));
    Response response = this.restClient.performRequest(request);
    System.out.println(response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
