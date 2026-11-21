# 画面线理解：20.Elasticsearch的Java低级客户端之搭建工程以及实现查询集群状态

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\20.Elasticsearch的Java低级客户端之搭建工程以及实现查询集群状态【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 01:02, 01:57, 02:45, 03:27, 04:46, 05:30, 06:24, 07:06, 07:56, 09:03, 09:33, 10:34, 11:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:54:31

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中创建并编写一个测试类，使用 Elasticsearch 的 RestClient 客户端进行 HTTP 请求，并通过 JUnit 进行测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 打开 IntelliJ IDEA，选择项目 "itcast-es"。
画面 2: 显示 pom.xml 文件内容，包含依赖项，如 junit、jackson-databind。
画面 3: 显示 pom.xml 文件中 <build> 部分，包含 <plugin> 配置，用于 Maven 编译。
画面 4: 创建 TestRestApi.java 文件，开始编写测试类。
画面 5: 在 TestRestApi.java 中导入 RestClient 和 RestClientBuilder，并开始编写初始化方法。
画面 6: 在 TestRestApi.java 中，为 RestClientBuilder 设置失败监听器。
画面 7: 在 TestRestApi.java 中，使用 HttpHost 构造函数设置 Elasticsearch 的主机和端口。
画面 8: 在 TestRestApi.java 中，完成 RestClient 的构建并设置失败监听器。
画面 9: 在 TestRestApi.java 中，添加 close() 方法用于关闭客户端。
画面 10: 在 TestRestApi.java 中，添加 testInfo() 方法，用于发起 HTTP 请求。
画面 11: 在 TestRestApi.java 中，使用 Request 类创建请求对象。
画面 12: 在 TestRestApi.java 中，使用 RestClient 发起请求并处理响应。
画面 13: 在 TestRestApi.java 中，为 testInfo() 方法添加参数，用于测试。
画面 14: 在 TestRestApi.java 中，运行 testInfo() 方法，显示测试通过并输出响应内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```xml
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.12</version>
</dependency>

<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.9.4</version>
</dependency>
```

画面 3:
```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.2</version>
        </plugin>
    </plugins>
</build>
```

画面 4:
```java
package cn.itcast.es;

import org.elasticsearch.client.RestClient;

public class TestRestApi {

}
```

画面 5:
```java
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestClientBuilder;
import org.junit.Before;

public class TestRestApi {
    private RestClient restClient;

    @Before
    public void init() {
        RestClientBuilder restClientBuilder = Re
```

画面 6:
```java
restClientBuilder.setFailureListener(new
this.restClient = restClientBuilder.build();
```

画面 7:
```java
new HttpHost(hostname: "172.16.55.185", port: 9200,
new HttpHost(hostname: "172.16.55.185", port: 9201)
```

画面 8:
```java
@Override
public void onFailure(Node node) {
    System.out.println("出错 -> " + node);
}

this.restClient = restClientBuilder.build();
```

画面 9:
```java
@After
public void close() throws Exception {
    // 网络应用的关闭而关闭
    this.restClient.close();
}
```

画面 10:
```java
@Test
public void testInfo() {
    Request request = new Request();
    this.restClient.performRequest();
}
```

画面 11:
```java
Request request = new Request();
```

画面 12:
```java
@Test
public void testInfo() throws IOException {
    Request request = new Request(method: "GET", endpoint: "/cluster/state");
    Response response = this.restClient.performRequest(request);
    System.out.println("请求完成 -> " + response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

画面 13:
```java
@Test
public void testInfo() throws IOException {
    Request request = new Request(method: "GET", endpoint: "/cluster/state");
    request.addParameter(name: "pretty", value: "true");
    Response response = this.restClient.performRequest(request);
    System.out.println("请求完成 -> " + response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

画面 14:
```java
@Test
public void testInfo() throws IOException {
    Request request = new Request(method: "GET", endpoint: "/cluster/state");
    request.addParameter(name: "pretty", value: "true");
    Response response = this.restClient.performRequest(request);
    System.out.println("请求完成 -> " + response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
