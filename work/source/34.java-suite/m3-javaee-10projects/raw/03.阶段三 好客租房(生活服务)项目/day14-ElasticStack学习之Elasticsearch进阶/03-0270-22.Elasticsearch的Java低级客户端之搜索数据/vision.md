# 画面线理解：22.Elasticsearch的Java低级客户端之搜索数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\22.Elasticsearch的Java低级客户端之搜索数据【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:18, 00:33, 00:41, 00:59, 01:12, 01:22, 01:32, 02:16, 02:42, 02:50, 03:04, 03:12, 03:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:55:50

1) 这一组画面整体在讲如何使用 RESTful API 对 Elasticsearch 进行数据查询和搜索操作，包括根据 ID 查询、搜索数据以及使用高级参数（如 pretty）。

2) 按时间顺序列出每张画面的要点：
画面1：展示 IntelliJ IDEA 中 TestRestApi.java 文件，包含根据 ID 查询数据的测试方法 testQueryData()，其中 endpoint 为 "/haoke/house/G0pFE2gBCRV8opxuRz1y"，并调用 restClient.performRequest()。
画面2：展示 testQueryData() 方法中 endpoint 为 "/haoke/house/G0pFE2gBCRV8opxuRz1y"，并调用 restClient.performRequest()。
画面3：展示 testQueryData() 方法中 endpoint 为 "/haoke/house/G0pFE2gBCRV8opxuRz1y"，并调用 restClient.performRequest()。
画面4：展示 testQueryData() 方法中 endpoint 为 "/haoke/house/G0pFE2gBCRV8opxuRz1y"，并调用 restClient.performRequest()。
画面5：展示 testQueryData() 方法中 endpoint 为 "/haoke/house/G0pFE2gBCRV8opxuRz1y"，并调用 restClient.performRequest()。
画面6：展示 testQueryData() 方法中 endpoint 为 "/haoke/house/G0pFE2gBCRV8opxuRz1y"，并调用 restClient.performRequest()。
画面7：展示 testQueryData() 方法中 endpoint 为 "/haoke/house/G0pFE2gBCRV8opxuRz1y"，并调用 restClient.performRequest()。
画面8：展示 testQueryData() 方法中 endpoint 为 "/haoke/house/G0pFE2gBCRV8opxuRz1y"，并调用 restClient.performRequest()。
画面9：展示 testSearchData() 方法，使用 POST 请求到 "/haoke/house/_search"，设置 JSON 查询体和参数。
画面10：展示 testSearchData() 方法执行后的结果，包含 "total": 4, "max_score": 1.1507203, "hits" 数组。
画面11：展示 PDF 文档内容，标题为“3.4、REST高级客户端”，并有代码片段 System.out.println(response.getStatusLine()); System.out.println(EntityUtils.toString(response.getEntity()));。
画面12：展示 testQueryData() 方法中 endpoint 为 "/haoke/house/j5vaGgBqiMwr19H-k63"，并调用 restClient.performRequest()。
画面13：展示 PDF 文档内容，标题为“3.4、REST高级客户端”，并有代码片段 System.out.println(response.getStatusLine()); System.out.println(EntityUtils.toString(response.getEntity()));。
画面14：展示 PDF 文档内容，标题为“3.4.1、引入依赖”，并展示 TestREST 类的代码，包含导入语句和 RestClient.builder() 的配置。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1：
```java
data.put("price", "3500");
request.setJsonEntity(MAPPER.writeValueAsString(data));
Response response = this.restClient.performRequest(request);
System.out.println(response.getStatusLine());
System.out.println(EntityUtils.toString(response.getEntity()));
```

画面2：
```java
@Test
public void testQueryData() throws IOException {
    Request request = new Request("GET", "/haoke/house/G0pFE2gBCRV8opxuRz1y");
    Response response = this.restClient.performRequest(request);
    System.out.println(response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

画面3：
```java
@Test
public void testQueryData() throws IOException {
    Request request = new Request("GET", "/haoke/house/G0pFE2gBCRV8opxuRz1y");
    Response response = this.restClient.performRequest(request);
    System.out.println(response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

画面4：
```java
@Test
public void testQueryData() throws IOException {
    Request request = new Request("GET", "/haoke/house/G0pFE2gBCRV8opxuRz1y");
    Response response = this.restClient.performRequest(request);
    System.out.println(response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

画面5：
```java
@Test
public void testQueryData() throws IOException {
    Request request = new Request("GET", "/haoke/house/G0pFE2gBCRV8opxuRz1y");
    Response response = this.restClient.performRequest(request);
    System.out.println(response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

画面6：
```java
@Test
public void testQueryData() throws IOException {
    Request request = new Request("GET", "/haoke/house/G0pFE2gBCRV8opxuRz1y");
    Response response = this.restClient.performRequest(request);
    System.out.println(response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

画面7：
```java
@Test
public void testQueryData() throws IOException {
    Request request = new Request("GET", "/haoke/house/G0pFE2gBCRV8opxuRz1y");
    Response response = this.restClient.performRequest(request);
    System.out.println(response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

画面8：
```java
@Test
public void testQueryData() throws IOException {
    Request request = new Request("GET", "/haoke/house/G0pFE2gBCRV8opxuRz1y");
    Response response = this.restClient.performRequest(request);
    System.out.println(response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

画面9：
```java
@Test
public void testSearchData() throws IOException {
    Request request = new Request("POST", "/haoke/house/_search");
    String searchJson = "{\"query\": {\"match\": {\"title\": \"拎包入住\"}}}";
    request.setJsonEntity(searchJson);
    request.addParameter(name: "pretty", value: "true");
    Response response = this.restClient.performRequest(request);
    System.out.println(response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

画面10：
```json
{
  "total": 4,
  "max_score": 1.1507203,
  "hits": [
    {
      "_index": "haoke",
      "_type": "house",
      "_id": "j5vaGgBqiMwr19H-k63",
      "_version": 1,
      "found": true,
      "source": {
        "price": 3500,
        "id": 2001,
        "title": "南京西路 一室一厅"
      }
    }
  ]
}
```

画面11：
```java
System.out.println(response.getStatusLine());
System.out.println(EntityUtils.toString(response.getEntity()));
```

画面12：
```java
@Test
public void testQueryData() throws IOException {
    Request request = new Request("GET", "/haoke/house/j5vaGgBqiMwr19H-k63");
    request.addParameter(name: "pretty", value: "true");
    Response response = this.restClient.performRequest(request);
    System.out.println(response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

画面13：
```java
System.out.println(response.getStatusLine());
System.out.println(EntityUtils.toString(response.getEntity()));
```

画面14：
```java
import org.apache.http.util.EntityUtils;
import org.elasticsearch.client.RestClient;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class TestREST {
    private static final ObjectMapper MAPPER = new ObjectMapper();
    private RestClient restClient;

    @Before
    public void init() {
        RestClientBuilder restClientBuilder = RestClient.builder(
            new HttpHost("172.16.55.185", 9200, "http"),
            new HttpHost("172.16.55.185", 9201, "http"),
            new HttpHost("172.16.55.185", 9202, "http")
        );
        restClientBuilder.setFailureListener(new RestClient.FailureListener() {
            @Override
            public void onFailure(RestClient client, Exception e) {
                System.out.println("请求失败：" + e.getMessage());
            }
        });
        restClient = restClientBuilder.build();
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面11：PPT 标题为“3.4、REST高级客户端”，并有文字“从使用中，可以看出，基本和我们使用RESTful api使用几乎是一致的。”
画面13：PPT 标题为“3.4、REST高级客户端”，并有文字“从使用中，可以看出，基本和我们使用RESTful api使用几乎是一致的。”
画面14
