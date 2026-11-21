# 21.Elasticsearch的Java低级客户端之新增文档数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\21.Elasticsearch的Java低级客户端之新增文档数据【海量资源尽在 ubkz.com】.mp4
- 时长 4分43秒（音频 283s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下新增数据啊那么我们来去写一下这样的一个代码那么我们去还是定一个方法啊word然后呢叫test就叫save然后呢我们来看一下这个里面的加一个注解叫test注解那么这个位置呢我们还是需要去定一个request那么咱们就把上面这个拷贝过来吧request然后呢我们去看一下啊那么需要发起的请求呢肯定是post请求对吧
[00:29] 然后呢我们需要发送的目标地址呢是应该是我们现在是不是已经有一个我们的一个这样的一个索引对吧浩克这个索引那么我们就这样来写浩克下面写一个host这个是不是就是我们的浩克索引你看这个type是不是就host那么我们就往这个下面再去给他提交数据就可以了那么我们来看一下这个数据怎么样去写那么当然了我们也可以把这个刚刚我们
[00:58] 去加的这个参数呢去拷贝过来然后呢我们来设置参数啊怎么样去设置我们的请求体因为我们去新增数据的时候呢需要去提交的是一个json对吧那么怎么样去提交呢我们需要通过一个这个request点然后呢send什么有一个叫json啊看到有个叫json的attitude然后呢我们去用这个方法json
[01:22] 那么我们需要去有一个这样的一个edit那么这个edit怎么来呢我们来看一下那么就是json那么我们需要去构造一下那么我们通过这个先定一个map定一个map然后通过这个map我们再去转一个json定一个object就叫date等于new一个hc map然后我们就需要去通过我们前面是不是导入的这个依赖就是我们的json
[01:51] 我们把这个 Jackson 也导入进来定一个 staticFinal一个 objectMapper定一个 Mapper等于 new一个 objectMapper然后通过这个 Mapper我们去转一个 json那么就定一个 json等于是不是 Mapper.writeValue as string然后设置 date好 那么我们把这个网站一贴
[02:20] 那么这样的话它有异常对吧异常我们就选择抛出我们就直接在这个位置去写exception抛出一个最大的异常好嘞然后我们去设置了参数之后我们就发起请求就可以了rest.clientrest.client点去做一个form request然后去给它设置一个requestOK好那么它的一个响应它的一个响应就是response那么我们把这个response也打印出来
[02:49] 那么是不是就是这两个刚刚我们打印的这两句那么一把他拷贝过来往这一贴好嘞那么接下来我们是不是给他填数据就可以了date.put设置一个什么设置一个我们设置的内容是在后面这个内容这个内容前面这个是他的原数据那么id title还有press id然后比如说我随便写点这叫什么南京西路南京西路
[03:19] 然后呢叫什么呢这个一试一听随便写啊防御的这个信息然后呢有三个内容对吧一个还有是这个是IDID我们应该是看一下他100那这样ID我们应该这样写写这个2001吧那么原来这个是不是叫1001我们把它写成2001然后呢这个叫titletitle是他啊然后呢后面后面还有个press
[03:45] price是价格价格的话呢我们就写一个比如说三千五OK好那么大概呢就是这样的话数据是不是就已经构造完成了这块呢我们就在构造数据啊构造数据好嘞那么接下来我们来发起请求来执行看一下它的结果会怎么样我们来看一下结果呢它给我们响应的是2011就代表着我们这个数据呢已经创建成功了那么这个是它所生成的一个ID然后呢下面呢这个是一个状态然后呢
[04:16] 然后就上了一些相关的信息了total有两个成功的两个OK好那么我们来去到我们这个里面刷新一下走那么可以看到这条数据是不是就是刚刚我们所填的这条数据对吧OK好嘞那么我们这个是不是就已经实现了一个新增这样的一个数据了OK好嘞好那么关于这个新增数据那我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

