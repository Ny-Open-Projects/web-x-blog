# 10.WebMagic抓取数据之导入数据到Elasticsearch（批量导入数据）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\10.WebMagic抓取数据之导入数据到Elasticsearch（批量导入数据）【海量资源尽在 ubkz.com】.mp4
- 时长 8分24秒（音频 505s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么接下来呢我们就把我们的数据呢就导入到我们的elixir中啊我们来看一下那么首先呢我们需要把我们之前插入的这条数据呢我们先给它删除掉那我们找下这个数据啊它的ID呢就是这个ID然后呢我们去把它删除掉怎么删除呢是不是我们去做一个delete操作对吧这样的delete操作就可以做一个删除了那么是不是已经删除掉了看刷新一下啊
[00:28] 那么在我们的浏览数据里面会发现其实已经没有数据了那么接下来呢我们去采用我们的批量插入数据的方式呢把这些数据呢插入进去在课前资料中呢为大家提供了我们已经抓好的这个数据啊然后呢我们把这个数据呢导入到我们这个code下面然后呢我就把这个刚刚我们去爬了这个数据呢就删掉了然后呢我们把这个数据拷贝过来然后呢所对应的是图片的数据啊
[00:56] 这个图片数据可能现在我们就不需要了然后我们只是去导入数据而已所以说这个就无所谓了好那么下面我们来编写代码我们去实现一下那么接下来我们来看一下我们就在这个里面就是我们最就是低级的这个API然后里面去写这样的一个操作在这个位置那么我们就以它为例然后我们去把这个代码去改造一下
[01:23] 然后呢我来看一下这个我们改成二吧然后这个呢就来一个叫下完线book然后呢发起的是post请求然后呢我们来看一下那么我们这个book去发起请求呢它呢是是需要去我们去有一行的这个操作一行的数据对吧所以呢我们应该是这么来玩这个我们就不需要了那么我们就需要这么去做就是我们先要去读取到我们这个文件的内容啊那么通过
[01:54] fail utils然后点readless然后呢new一个failnew一个fail那就是我们的f盘下面的code下面的就json.date这样的一个文件来看一下对不对那么叫做date.json这个拼错了就叫date.json然后呢它的一个编码呢就是utf-8
[02:22] 好嘞那么这样的话呢我们就会这个是应该是utf-8写错位置了然后呢我们把它写到后面来写到这个位置来好那么这样的话呢我们就会读取到我们的一行一行的这个数据对吧然后呢我们就需要对它去做一个便利那我们来便利一下那么就是这个lan那么我们上面呢其实需要写一个去需要去写一个什么呢我们streamstreambuilder sb
[02:52] 等于去new一个stream builder然后我们去添加这个lan但是要注意的是那么除了这个lan的添加就是我们append的一个lan然后注意后面要加一个什么呢-n回车这个别忘记然后我们还需要加一个什么呢是否要加一个它的一个操作的一个说明那么操作说明我们来拷贝一下就是我们去定义这样的一个字符串那么我们去定义到上面来把它定义到这在这
[03:21] 然后我们去把它加到上去加一个更n回车好那么这样的话我们是不是就是每一行去添加一个操作说明然后每一行加一条数据然后就可以了然后我们就可以去把它是不是就丢到我们这个json这个里面来对吧toolstrip就可以了这样就好了但是我们可以想一下那么如果我们去这么去玩的话那么每一次一次所提交的
[03:48] 这个量是不是太大了对吧我们可以给它分批一下那么所以我们在这个位置是不是可以来一个计数比如来一个countcount它等于0等于0然后呢我们让它每执行一次呢我们去加加一次加加然后呢我们去是不是可以去做一个判断对吧快判断那么我们就做个判断吧这样如果这个count如果大于等于比如说200那么每200条这个数据我们去
[04:18] 提交一次那么我们是不是就应该这么来玩对吧然后呢我们去把它移到上面吧那先加进去然后呢做一个判断然后呢我们就去做一个count加加这个count加加放到这来然后呢count然后呢如果说大于200的话那就count回0回到0并且呢我这个sb呢做一个重新一个new的strain builder那么我们
[04:47] 再去做一个这样的一个这个new就可以了相当于把这两个呢给它还原一下然后呢还原完成之后呢我们我们是不是就需要在这个位置是不是去做一个提交对吧然后呢我们去set我们的一个json的一个additive然后呢做一个提交就可以了好嘞那么我们去这样去写一下然后下面这个代码就不需要了那么我们把它去做一个做一个post提交就ok
[05:15] 那么如果我们接着来看一下那么其实我们在最后面在最后面实际也是需要再做一个处理就是说如果我们的提交完成之后就是没有进入这个对吧可能还会有一些然后我们就去再次去做一个提交就可以了放到下面来那么我们是不是最好可以做一个判断如果if它的toString如果这个是空的话
[05:45] empty啊easy empty如果是空的话那么我们就不做了如果不为空那么我们就再去再去再去做一次提交这样的话确保我们的数据啊不要有丢失好这样的话是不是基本上就可以去执行了那么可以大致的检查一下这个代码啊应该是没有什么问题那么添加一个他然后呢每一行去做一个添加然后呢去如果判断没问题然后去提交然后再去提交ok没有任何问题好那么下面我们来执行一下然后呢执行他
[06:15] 走 那我们来看一下结果会怎么样我们等待它的一个执行执行的时候呢发现有报错啊是原因我们这个地址呢没有改那么我们去调一下这个可能我没改掉应该是改成1921681.7然后呢这三个呢我们都来把它去调一下然后再转然后呢再转好嘞那么这样的话呢我们就可以再次去做一个执行了
[06:46] 然后走看他会执行结果会怎么样等待一下那么我们看到已经是提交完成了那么我们来看一下这个数据有多少刷新一下那么可以看到数据就已经都提交上来了总共数据是2010条数据那我们来看一下对不对那么我们这个数据条数总共多少我们来看一下打开看一下把这个
[07:10] 折一下然后2010条没有问题所以我们这个数据呢是不是都已经提交到我们的这个elaxus中了ok没有任何问题对吧看一下数据大致的去浏览一下对吧数据应该是ok的应该是ok的好嘞那么现在我们这个数据呢是不是就已经提交完成了对吧当然我们可以去做一个测试就是按照前面我们这个测试去测一下那么在前面这个位置我们把它这个我们改成search然后呢
[07:40] 在上面这个位置我们去调一下比如说搜一个地铁那我们来看一下他搜索这个我们看一下他说是执行操作不是delete应该是post走然后来看一下结果结果总共命中了有419条数据那么看一下是不是都是关于这个地铁相关的一些文档呢应该都是应该都是靠近地铁地铁等等等等OK
[08:08] 好那么基本上是不是就可以说明我们现在数据就已经成功的去导入到我们的ELAC设置中了对吧OK好最后的结果那就是这样的结果好嘞好那么这个数据是不是就导入完成了好那么关于这个数据的一个导入就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Java 代码批量导入数据到 Elasticsearch，并演示了数据查询和集群状态。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Elasticsearch Head 插件界面，显示集群状态为 green，三个节点（node01、node02、node03）及其分配的分片（01 34、0 23 5、12 45）。
画面2：展示 Windows 资源管理器，显示 images 文件夹内包含大量图片文件，以及 code 文件夹下的 data.json 文件。
画面3：展示 IntelliJ IDEA 中 TestRestApi.java 文件，代码片段为测试单条数据插入，设置 title 为“南京西路 一室一厅”，price 为 3500。
画面4：展示 IntelliJ IDEA 中 TestRestApi.java 文件，代码片段为测试根据 id 查询数据，请求地址为 /haoke/house/j5VaHgGpBqIwMr19H-k63。
画面5：展示 IntelliJ IDEA 中 TestRestApi.java 文件，代码片段为测试保存数据，请求地址为 /haoke/house_bulk，使用 FileUtils 读取文件。
画面6：展示 IntelliJ IDEA 中 TestRestApi.java 文件，代码片段为测试保存数据，使用 StringBuilder 构建 JSON 字符串，读取 data.json 文件内容。
画面7：展示 IntelliJ IDEA 中 TestRestApi.java 文件，代码片段为测试保存数据，构建 JSON 字符串，读取 data.json 文件内容。
画面8：展示 IntelliJ IDEA 中 TestRestApi.java 文件，代码片段为测试保存数据，构建 JSON 字符串，读取 data.json 文件内容。
画面9：展示 IntelliJ IDEA 中 TestRestApi.java 文件，代码片段为测试保存数据，构建 JSON 字符串，读取 data.json 文件内容。
画面10：展示 IntelliJ IDEA 中 TestRestApi.java 文件，代码片段为测试保存数据，构建 JSON 字符串，读取 data.json 文件内容。
画面11：展示 IntelliJ IDEA 中 TestRestApi.java 文件，代码片段为测试保存数据，构建 JSON 字符串，读取 data.json 文件内容。
画面12：展示 EditPlus 编辑器，显示 data.json 文件内容，包含多个房屋数据条目，包含 image、title、rent、floor 等字段。
画面13：展示 Postman 工具，发送 DELETE 请求到 Elasticsearch 的索引，请求体为 JSON 格式，包含 index、type、id、_source 等字段。
画面14：展示 Adobe Reader，显示 PDF 文档内容，包含搜索结果，显示 total 为 306，hits 数组中包含一个 hit，包含 index、type、_id、_source 等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面3：
```java
data.put("title", "南京西路 一室一厅");
data.put("price", 3500);
String json = MAPPER.writeValueAsString(data);
request.setJsonEntity(json);
Response response = this.restClient.performRequest(request);
System.out.println("请求完成 -> " + response.getStatusLine());
System.out.println(EntityUtils.toString(response.getEntity()));
```

画面4：
```java
@Test
public void testQueryData() throws IOException {
    Request request = new Request(method: "GET", endpoint: "/haoke/house/j5VaHgGpBqIwMr19H-k63");
    request.addParameter(name: "pretty", value: "true");
    Response response = this.restClient.performRequest(request);
}
```

画面5：
```java
@Test
public void testSave2() throws Exception{
    Request request = new Request(method: "POST", endpoint: "/haoke/house_bulk");
    FileUtils.readLines(new File("F:\\code\\data.json"), encoding: "UTF-8");
    request.setJsonEntity(json);
    Response response = this.restClient.performRequest(request);
    System.out.println("请求完成 -> " + response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

画面6：
```java
@Test
public void testSave2() throws Exception{
    Request request = new Request(method: "POST", endpoint: "/haoke/house_bulk");
    StringBuilder sb = new StringBuilder();
    String createStr = "{\"index\":{\"_index\":\"haoke\",\"_type\":\"house\"}}";
    List<String> lines = FileUtils.readLines(new File(pathname: "F:\\code\\data.json"), encoding: "UTF-8");
    for (String line : lines) {
        sb.append(createStr + "\n");
        sb.append(line + "\n");
    }
    request.setJsonEntity(sb.toString());
    Response response = this.restClient.performRequest(request);
    System.out.println("请求完成 -> " + response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

画面7：
```java
@Test
public void testSave2() throws Exception{
    Request request = new Request(method: "POST", endpoint: "/haoke/house_bulk");
    StringBuilder sb = new StringBuilder();
    String createStr = "{\"index\":{\"_index\":\"haoke\",\"_type\":\"house\"}}";
    List<String> lines = FileUtils.readLines(new File(pathname: "F:\\code\\data.json"), encoding: "UTF-8");
    int count = 0;
    for (String line : lines) {
        sb.append(createStr + "\n");
        sb.append(line + "\n");
        if(count >= 200) {
            request.setJsonEntity(sb.toString());
            this.restClient.performRequest(request);
            count = 0;
            sb = new StringBuilder();
        }
        count++;
    }
}
```

画面8：
```java
@Test
public void testSave2() throws Exception{
    Request request = new Request(method: "POST", endpoint: "/haoke/house_bulk");
    StringBuilder sb = new StringBuilder();
    String createStr = "{\"index\":{\"_index\":\"haoke\",\"_type\":\"house\"}}";
    List<String> lines = FileUtils.readLines(new File(pathname: "F:\\code\\data.json"), encoding: "UTF-8");
    int count = 0;
    for (String line : lines) {
        sb.append(createStr + "\n");
        sb.append(line + "\n");
        if(count >= 200) {
            request.setJsonEntity(sb.toString());
            this.restClient.performRequest(request);
            count = 0;
            sb = new StringBuilder();
        }
        count++;
    }
}
```

画面9：
```java
@Test
public void testSave2() throws Exception{
    Request request = new Request(method: "POST", endpoint: "/haoke/house_bulk");
    StringBuilder sb = new StringBuilder();
    String createStr = "{\"index\":{\"_index\":\"haoke\",\"_type\":\"house\"}}";
    List<String> lines = FileUtils.readLines(new File(pathname: "F:\\code\\data.json"), encoding: "UTF-8");
    int count = 0;
    for (String line : lines) {
        sb.append(createStr + "\n");
        sb.append(line + "\n");
        if(count >= 200) {
            request.setJsonEntity(sb.toString());
            this.restClient.performRequest(request);
            count = 0;
            sb = new StringBuilder();
        }
        count++;
    }
}
```

画面10：
```java
@Test
public void testSave2() throws Exception{
    Request request = new Request(method: "POST", endpoint: "/haoke/house_bulk");
    StringBuilder sb = new StringBuilder();
    String createStr = "{\"index\":{\"_index\":\"haoke\",\"_type\":\"house\"}}";
    List<String> lines = FileUtils.readLines(new File(pathname: "F:\\code\\data.json"), encoding: "UTF-8");
    int count = 0;
    for (String line : lines) {
        sb.append(createStr + "\n");
        sb.append(line + "\n");
        if(count >= 200) {
            request.setJsonEntity(sb.toString());
            this.restClient.performRequest(request);
            count = 0;
            sb = new StringBuilder();
        }
        count++;
    }
}
```

画面11：
```java
// 均匀数据
Map<String, Object> data = new HashMap<>();
data.put("id", 2001);
data.put("title", "南京西路 一室一厅");
data.put("price", 3500);
String json = MAPPER.writeValueAsString(data);
request.setJsonEntity(json);
Response response = this.restClient.performRequest(request);
System.out.println("请求完成 -> " + response.getStatusLine());
System.out.println(EntityUtils.toString(response.getEntity()));

@Test
public void testSave2() throws Exception{
    Request request = new Request(method: "POST", endpoint: "/haoke/house_bulk");
}
```

画面12：
```json
{
  "rent": "3800",
  "floor": "中楼层",
  "image": "SH21059981784336408.jpg",
  "url": "https://sh.lianjia.com/zufang/SH215696415409916480.html",
  "title": "整租",
  "rentMethod": "整租",
  "time": "需提前预约",
  "orientation": "南",
  "houseType": "2室1厅",

