# 24.Elasticsearch的Java高级客户端之删除、更新、搜索操作

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\24.Elasticsearch的Java高级客户端之删除、更新、搜索操作【海量资源尽在 ubkz.com】.mp4
- 时长 10分22秒（音频 622s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们还是给大家来演示一下在我们的这个高级客户端里面的一些基本的一些操作啊那么比如说像一些查询呢一些这个判断存在呢删除啊等等一些这个操作啊那么我们都来去演示一下吧虽然说我们可能在我们后期做项目的时候不会去选择这样的一些客户端去做一些使用但是呢不能排除在你们在去做项目的时候呢可能会用到这样的一些客户端啊然后呢我们去
[00:28] 把这个代码我们拷贝过来吧就不去敲了那我们就直接拷贝过来去大概大致我们去演示一下大家应该就能够明白他是怎么去用的了然后呢我们把这个client拿过来往这一丢那么现在呢我们所演示的是根据我们的一个这个ID去做一个查询并且呢我们可以去指定他返回的一个字段那么你可以看到这个是定义一个get request
[00:56] 然后呢定义的是一个index然后呢还有一个type还有呢就是我们的一个数据的一个id然后呢下面这个呢是定义的include就是去包含啊就是我们这个结果中要包含的是他们俩然后呢排除呢现在是一个空的啊然后做了这样的一个构造然后呢我们就把这个构造之后的这样的一个对象啊给它丢到我们的一个get request中然后呢去做这样的一个执行啊就可以了那么基本上呢就是这样的一个
[01:25] 基本上就是这样的一个代码编写然后我们去挑一个这样的一个ID过来我可以把它拷贝到这个里面我们来看一下它的一个结果那么我们这个结果是要求我们正常情况是不是会返回三个字段一个是ID一个是title一个是价格那么我们现在只要求它返回ID和title那我们来看一下它是否就是只返回了这个ID和title我们走运行
[01:52] 好那么我们可以看到那么这个就是我们运行之后的一个结果那么可以看到我们拿到数据是不是已经就拿到ID和这个title了对吧这个用起来是不是要比json拿到之后再去做一个反序列化操作是不是要方便很多ok好这个就是我们做一个查询然后接下来我们去还可以去做一些比如说我们判断我们这个数据是否存在这个我们在前面讲API是不是也讲过那我们来看一下它是怎么操作的
[02:22] 那么我们把这个类似点这个clientclient的名字有点不太对那么我们就去重新去挑一下就好了然后呢来看一下那么这个位置的还是去查询我们去查询一下他还是去查询某一个我们这个数据然后呢去看他拿到的一个值是否存在然后他这个位置呢这个位置调用的API是exist判断是否存在然后呢我们去做一个执行
[02:50] 走,那么看它的一个结果会怎么样那么等待它的一个执行可以看到这个文档是存在的那么如果随便改一个,把这个改成B这个文档应该是不存在的然后我们再去访问一下OK,那么我们其实要想拿到的结果是你这个文档到底存在还是不存在,对吧但是我们没有必要去返回字段所以说我们这个位置给它设置为False设置为False就是说不去获取这个字段了
[03:21] 那么可以看到结果呢是False那这个文档它显然是不存在的啊OK好就是这个啊判断是否存在在那个API下面呢还有个是删除删除这个API把它也拷贝过来那么我们来看一下那么在删除这个API里面啊那么把这个重写一下它那么我们只需要去构造一个什么呢叫做Delete Request对象
[03:44] 然后呢指定ID和type然后再去指定index和type然后再去指定我们的一个doc的一个ID做一个做一个delet的删除就可以了ok好嘞那么我们这样我们就先把这个拷贝过来那么这个我们知道刚刚在测试的时候会发现这个ID所对应的我们的文档数据是不存在的对吧那么我们尝试让他去删除一个不存在的一个数据那么会怎么样那么等待他的一个测试的一个结果那么可以发现他是一个not found就是说这个
[04:14] 这个文档呢是没有找到的对吧哎OK那么当然了我们是不是也可以是这么来玩对吧我找一个就找他吧我们把它拷贝过来然后呢我们去做一个删除那么其实呃我们去拿到这个状态有什么用啊大家可以想一下啊就是说我们是不是可以在删除完成之后呢再去可以去
[04:32] 判断一下它存在不存在或者有没有删除成功是不是都可以根据这个状态去做一个判断那么你可以看到这个文档我们是存在的文档对吧然后呢我们最后打印出来的一个结果就是OK那就代表着这个文档它是存在并且呢已经被我们删除了那我们来刷新一下这个呢是它的ID呢是2002然后呢做一个刷新那么你会发现2002那个数据是不是就已经不存在了哎呀OK好嘞那么这个呢就是
[05:01] 我们给大家所演示的一个删除的数据然后呢下面还有一个是更新数据啊咱们把这个也拷贝过来做一个演示啊然后呢来看一下这个更新数据那么更新数据呢看他怎么玩呢点这个client啊那么在更新数据中呢他呢也是去先构造这样的一个update request然后呢他他然后以及加一个这个ID对吧
[05:26] 然后这个ID呢我们来找一个吧我们随便找一个就我们刚刚所新增的这条数据吧把它拷贝过来然后呢往这一丢OK好嘞那么这个就是我们这条数据啊然后呢我们去修改你看它现在的一个标题呢是南京西路一试一听那么我们把它拷贝过来那么拷贝过来呢我给它设置的是比如说一试一听2然后呢南京西路2那么价格呢我们给它调成比如说调成
[05:56] 4000块钱OK然后呢然后呢我们将我们这个这个Data然后呢去丢到这个对象的这个Dock中通过这个Dock去做一个传递进去那么是不是在我们嘴快中就携带了我们这个数据然后呢做一个调用去给update一个API去操作就可以了OK好嘞那么我们来尝试一下看它能不能够执行成功呢然后呢我们执行走那么等待它的一个执行那么我们可以看到
[06:26] 那么现在呢我们拿到这个结果的一个Watson等于2那么显然肯定已经被修改了对吧然后呢我们去到我们的这个管理工具里面来查看一下那么我们的这个南京西路是不是这个你看这会变成南京西路2以及一室一厅2对吧然后呢价格呢变成了4000块钱那么在这个点呢需要大家特别注意的一点是那么我们在修改这个数据中啊
[06:50] 我们并没有去传递我们 ID 对吧但 ID 的值是不是依然被保留下来了那么也就意味着什么呢这个操作它是一个什么操作它是一个叫局部更新的这样的一个操作那么前面我们是不是讲 API
[07:04] 也着重也讲过这个点对吧它本身的这个文档就是Lucent底层的文档我们去定义它是不能修改的但怎么去修改呢可以去做一个覆盖这个我们前面也讲过好嘞那么这个呢就是做一个数据的一个更新那么下面呢这个是做一个数据的一个搜索那么我们把这个API呢我们也这个demo我们也拷贝过来我们来去把这个代码给大家讲解一下那么这个呢是做搜索那么还是这个client这个问题我们来把它调一下
[07:34] 点NZCLIENTOK好嘞那么我们看一下把这个代码我们简单做一个回车然后这个type先设置一个它然后下面设置设置它然后到这OK好这样的话应该差不多好来看一下那么我们首先定义一个叫search request加一个对象其实我们会发现如果你去做一些什么delete的操作的时候是不是就是delete request对吧
[08:04] 或者update或者是delete这样的request那么如果要去做搜索的时候就调用的是search request然后指定一个我们这个是索引然后再指定我们的type然后下面去构造我们的一个搜索的这样一个条件对吧那么通过一个search source build去构造一个条件然后通过一个query设置一个构造一个query那么我们通过一个
[08:30] query builds去构建一个match query就是通过一个match这样的一个查询那么在前面我们去讲 API的时候用的是不是也是match查询只是在这个位置我们就通过一个什么json的形式做一个表达而在这个位置通过我们的java是不是用API的方式做了这样的一个表达那么标题就叫拎包入住对吧然后我们并且可以设置它的一个from一个size这两个是不是可以做一个分页那么要返回是不是5条数据
[08:58] OK并且可以设置它的一个超时的时间OK然后呢做一个搜索就可以了那么调用这个search API然后去做一个搜索然后呢我们会得到一个search response在response中呢我们就可以拿到它的一些命中的一些这个数量对吧命中的这个数量然后呢下面做一个复循环把它的所有的这个数据呢命中的数据呢打印出来OK就这样的一个就这样的一个
[09:24] 测试吧那么这样就可以去做一个我们的搜索那么我们来看一下结果对不对那么现在我们可以看到它总共能拿到有4条数据然后是不是有12344条数据ok好嘞那么这数字4条数据中都是包含了拎包入住拎包入住拎包入住没有任何问题ok好嘞那么这个就是我们所给大家演示的高级API的一些高级rest
[09:51] API的一些使用那么还是那句话就是如果我们现在仅仅是带大家去熟悉或者说去演示这么几个API的使用那么在后面就是大家如果在做项目的时候如果选型定位在REST API这个上面的话那么可以采用低级的也可以采用高级的那么其实还是建议使用高级的因为相对会比较方便一点
[10:15] OK好嘞那么关于我们这个rest高级的一个高级客户端的一个讲解那我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

