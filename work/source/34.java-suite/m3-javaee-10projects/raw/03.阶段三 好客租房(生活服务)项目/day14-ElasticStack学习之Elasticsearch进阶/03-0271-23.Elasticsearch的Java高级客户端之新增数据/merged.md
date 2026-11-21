# 23.Elasticsearch的Java高级客户端之新增数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\23.Elasticsearch的Java高级客户端之新增数据【海量资源尽在 ubkz.com】.mp4
- 时长 9分33秒（音频 573s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下rest高级的客户端那么前面我们所讲的是低级的客户端它更加偏向于底层一点那么高级客户端呢就在低级的基础之上呢做了一些分装然后呢让我们使用的更方便一点啊那么我们来看一下首先呢我们需要导入这个依赖啊咱们把这个依赖拷贝过来那么我们来看这个pom啊然后在这个里面那么可以看到
[00:26] 这个是一个high level就是一个高级或者高层次的啊这样的一个client客户端了那么我们来去写一个类吧那么就叫什么呢看一下啊就叫他吧rest这个high level就是一个高级的这样的一个客户端OK当然了大家不要去从这个
[00:51] 从这个文字上面去抠啊就是说低级的我觉得很low了这个高级的我觉得会好一点其实并不是这样的还是要根据实际情况去做选择然后呢我们还是先去写一个那么我们先去定义一个吧就叫一个什么呢rest一个high level这样的一个client那么我们需要先定义这样的一个client下面做一些这个测试
[01:16] 然后呢在这个里面呢我们需要写一个跟我们刚刚讲写一个init方法初始化方法那么这个呢就叫before在执行之前呢去那么在这个位置呢我们给它通过啊this点这个对象它等于去new一个我们这个对象啊然后呢在new的这个方法中呢我们需要传递一个构造参数给它啊就是一个我们的一个这个client对象啊
[01:43] 那么这克兰对象呢跟我们的D级版本中的克兰对象是一样的同一个对象那么我们就把这个对象拿过来然后呢到这拿着它然后呢把这个build传递给它那么它通过这个build就会得到这样的一个客户端了那么非常的类似啊那么下面我们是不是还应该去写一个close方法对吧那么我们就再来一个啊叫public word然后呢close然后呢去写一个叫做after之后
[02:13] 然后调用他点 close都一样的操作然后去抛出一个exceptionok 好那么下面我们是不是就可以写一些相关的一些代码的操作了对吧那么我们首先写一个新增还是一个c5test test c5操作然后我们给它加一个注解叫test然后下面在这个位置我们就要用this.client.index做一个所以
[02:43] 那么其实就是去保存我们的数据了那么这个里面需要传递两个参数第一个是叫做看一下第一个参数叫做indexRequest那么所以在上面这个位置我们定义一下叫做indexRequestindexRequest那么indexRequest等于new一个这样我们一会再说这个先给它设置为一个none然后第一个参数传递过来
[03:11] 然后呢第一个参数含地管的第二个参数呢就需要有一个叫request一个opsense使用这个default啊就可以了那么它呢有异常那么异常呢我们也是为了简单测试呢我们就全部都把这个异常抛出不做个处理然后呢下面呢就可以去拿到它的一些这个响应的一些结果对吧把这个响应结果我们让它去拿到那拿到呢就是一个response
[03:37] 那么在response里面的内容就比较丰富了那么一会我们再来看啊那么下面我们来看一下这个request怎么去我们把这个来构造一下index啊request对象那么去new一个index啊index request然后呢需要传递两个参数啊第一个参数呢就是我们的这个所以那么就叫hook然后第二个呢就是我们的这个type啊那么就是叫什么的host然后呢
[04:05] 我们需要给他去设置一些这个数据对吧然后呢需要给他设置一个通过一个source去设置然后呢可以看到在这个位置你可以接收的是一个map也可以接收object也可以接收这种x contact build这种方式也是比较常用的那我们就采用这个map这种方式吧那么点点source那么这个map呢在前面我们是不是我们是不是已经构造过这个map对吧那么把这个map我们拷贝过来
[04:34] 那就是他那我们简单的去改造一下那么我们把它丢到上面来然后呢这个我们改成2002吧南京东路然后呢改成两室一厅改成4000块钱OK好嘞那么然后呢我们去设置一个这个date好那么这样的话我们是不是就得到一个index request对象然后呢我们在response中就可以拿到各种我们想要拿到的数据了比如说可以拿到get一个
[05:04] 比如说get一个ID那么就是我们新增之后的一个ID对吧那么把它打印出来然后呢来一个ID去加一个它那么还可以去拿到一些其他信息比如说拿到一个你的一个Watson版本也是可以的那么把它靠一下然后呢到这WatsonOK那么还有其他信息我们来看一下get还有的话比如说去拿到它的一些
[05:35] 我们这个内容数据内容数据我们是需要拿到这个result对象result拿到result对象然后它去result那么我们就把这个result直接打印出来result好那么好这样的话我们就可以去做一个执行了但它这个里面还有些其他的一些这个响应的内容那我们就不做一个展示了大家如果需要什么自己去拿就可以了
[06:03] OK那么等待它的一个执行我们来看它的一个运行的一个结果OK那么现在是不是可以看到那么现在是不是ID就是它对吧Watson是1那么Realtor就是Created就是说这个文档已经创建成功了这个是不是要比我们前面所测试的拿到一个阶层字不错那么你更方便更好操作对吧OK那么看一下这个数据它有没有保存到数据库里面看一下那么可以看到在这个里面是不是有个2002
[06:34] 南京东路这条数据是不是也保存到我们的这个elax中了对吧ok好那么这个就是我们给大家所演示的第一个这个高版本的一个这样的一个示例ok好那么这个呢是一个同步的操作它其实还有异步的操作那么咱们把这个代码也抠过来吧然后呢我们一起给大家来演示一下那么同步和异步其实其实呢是差不多其实差不多的那么把这个代码我们贴过来看一下
[07:04] 就直接贴到我们的下面这个位置啊到这OK好那么我们来看这个里面它是不是有一些这个错误啊那么这client我们是这个client啊把它拿过来哎OK好那么我们来看一下这个代码那么我们来看一下啊呃在这个代码中呢我们可以看到上面这个呢还是在构造数据啊构造数据呃然后呢下面的这个呢还是我们刚刚的index request然后呢我们在这个位置啊去调用我们的client
[07:34] 去做一个index之后呢它变成了什么呢变成了异步的方式然后呢除了这两个参数的传递呢我们要去传递一个我们一个action listener然后呢在这个里面去做一个接收那么这个是我们的这个on response就是成功对吧然后这个是如果出错的时候在这个位置啊那么所以你可以看到
[07:55] 这个代码和我们上面几乎差不多只是说一个是做同步的一个这样的一个调用另外一个是做一个异步的这样的一个调用然后呢下面在这个位置呢我们让我们的程序去做一个这个sleep那么原因目的呢就是要等待我们这个程序它这个程序的一个执行如果你这个位置不去sleep的话那么它是不是没有办法去做执行啊OK好了那么我们来测试一下看效果啊走那么等待它的一个执行
[08:23] 那么这个是一个易步的操作那么其实我们它已经创建成功了OK好那么其实我们想说的是看一下这样的一个效果那这样我们先来看这个结果结果是ID没有问题这个index typeWarson都没有任何问题都是OK的包括这个是我们的shad info就是我们分片的信息那么总共有两个分片然后它全部都已经成功了对吧OK好嘞好那么现在
[08:50] 我们在下面打印一句话让大家看一个效果比如说在这我们去打印个OK那么我们再插一条数据比如2004然后南京东路2然后5600块钱好那么我们再去做一个执行看一下这个效果那么他肯定是先打印谁是不是先打印OK然后再打印我们上面的一些内容来看一下这个结果你看是不是先打印OK然后再打印我们
[09:14] 在我们这个on response中打印的这一块内容那么也就是说明这是一个易补的一个操作对不对好那么这个就是在高级这个版本中所讲的一个我们的新增新增文档数据在那个操作OK好那么这个我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Elasticsearch 的 Java High Level REST Client 进行索引创建、数据保存和异步操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 TestRestApi.java 中的 testSearchData() 方法，使用 RestClient 发起 POST 请求搜索数据，打印响应实体。
画面2：展示 TestRestHighLevel.java 文件，导入了 org.Elasticsearch.index.rankeval 包下的多个类。
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

