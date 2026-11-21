# 22.Elasticsearch的Java低级客户端之搜索数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\22.Elasticsearch的Java低级客户端之搜索数据【海量资源尽在 ubkz.com】.mp4
- 时长 3分48秒（音频 228s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下查询啊查询的有两种啊第一种的是根据ID去查询第二种的是做搜索那么我们就把这个代码拷贝过来吧我们去做一下这个演示啊这个使用的都非常的相似了那么我们把它贴到这里来然后呢我们可以看到这个位置呢去发起的是get请求然后呢它的一个目标地址呢是这样一个地址当然这个ID呢需要我们重新拷贝一下啊比如说我们来去让它去查询一下
[00:29] 新增的这条数据把它呢拷贝过来然后呢往这一贴OK好嘞那么然后呢我们去做一个请求看他能不能够拿到我们这个数据好那我们来看一下现在呢是不是就拿到这条数据了当然了我们是不是这个显示的不是特别好看对吧给他去美化一下这个响应应该是在前面这个位置啊加一个我们的一个这个参数好然后呢我们再去执行一下走
[00:58] 那么等待他的一个执行我们来看一下他的一个响应的一个结果那么其实从刚才的响应结果中可以看到他的响应状态码是200那就是成功拿到数据了对吧OK好那么这个是不是就是我们刚刚所新增的那条数据OK好那么这个就是一个查询数据那么下面我们来看一下搜索数据那我们把这个搜索数据也拷贝过来用法都非常的类似非常类似可以就把它看作是我们
[01:27] 跟我们的浏览器的插件一样对吧去做一个rest client的使用就可以了OK好那么我们来看一下搜索搜索也是去定义一个request对象然后设置一个post因为我们要去添加我们的请求的阶层所以设置post然后它的一个端点就是一个search对吧host下面一个search然后一个搜索这么创就是我们通过一个match去匹配一个title
[01:55] 比如说有个拎包入住啊然后呢设置一个我们的一个请求的一个请求体然后呢设置这样的一个参数啊就是美化了一个参数然后呢做一个请求去打印就可以了所以你可以看到这个用法这个用法是不是非常的一致啊非常的一致所以说为什么把它称之为叫做低级的客户端呢就是非常的偏向于底层啊就是去直接对我们的http做了一些分装
[02:21] 然后去写了这套API出来那么其实在我们前面学习过程中我们学了那么多的一些RESTful API那么我们再通过这样的API去通过这样的API去操作的话我相信大家应该是能够很快上手去使用这样的API去操作的OK好那么这个数据就拿到了总共命中了有4条数据然后是不是可以看到在这个里面没有问题是吧没有任何问题OK好嘞好那么这个就是我们去
[02:50] 给大家所讲的一个低级的一个这样的客户端那么它的使用的方法其实跟我们的使用RESTful API使用方法是几乎是一样的OK那么关于低级客户端我们就讲这么多那么给大家简单的去做一个那么更多的一些这样一些用法还希望大家如果你要是需要在你的项目中需要使用这样的一个API的话那么就需要去参考一下官方的文档去做一些额外的一些学习了
[03:19] 那么其实我们就是如果回到我们项目本身就是回到我们项目本身去说的话那么我们是不太可能会采用这样的一种方式去做我们的一个API的使用的因为这个开发效率是相对比较低的它偏向底层一点OK好那么那么等讲到后面我们再说吧我们再讲我们的一个技术选型了OK好那么关于我们的这个低级的一个客户端的一个讲解那么就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import org.Elasticsearch.client.RestClient;
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

