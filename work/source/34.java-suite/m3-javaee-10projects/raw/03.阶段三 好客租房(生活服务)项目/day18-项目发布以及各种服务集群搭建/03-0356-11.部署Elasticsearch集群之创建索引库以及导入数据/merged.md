# 11.部署Elasticsearch集群之创建索引库以及导入数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\11.部署Elasticsearch集群之创建索引库以及导入数据【海量资源尽在 666java.com】.mp4
- 时长 3分10秒（音频 191s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们基于前面我们所搭建的ES的集群呢我们把我们的这个文档的mapping的创建好以及我们把一些测试数据呢去导入进去那么我们把这个地址来拷贝一下我们去做一下执行那么我们呢去打开我们的一个rest client然后呢向我们这个地址呢去发起pool的请求OK那么在这
[00:26] 好那么下面我们把这个数据呢就是下面这个我们这个结构啊那么这个结构中呢是已经添加了我们这个拼音的啊这样的一个分词和我们的IK的一个分词那么把这个呢就拿过来往这一贴然后我们点击这个send发送那么这样的话呢我们就会去把我们这个文档呢就是我们索引库呢就创建好那么创建好之后呢我们就可以去写入数据啊到我们这个里面了
[00:54] OK好那么到这里呢我们是不是就已经啊创建好了我们来检查一下那么呃我们到这个里面吧来看一下索引那么刷新一下那么目前呢我们是不是已经有一个这个浩克啊这个索引库了那么它呢是有六个我们的一个这个分片啊从零到六啊这样的一个分片然后呢我们来看一下它的索引那么这个是它的数据啊目前呢还没有数据那么一会儿呢我们会导入数据啊进来那么OK那么
[01:23] 接下来我们就来导入数据吧那么这个导入数据逻辑呢其实就是我们之前所写的这个导入逻辑啊那我们可以去打开我们之前所写的这个itcast这个es这个工程然后呢去做一个导入那么我们来看一下再去上面啊他这个位置呢我们需要去把这个地址来改一下那么这个是9200那么我们还需要再写一个就是18他也是92009200然后呢这个呢是19
[01:52] 19也是同样的也是9200OK好那么现在呢我们是不是就已经呢把这个就搞定了对吧好那么下面呢我们就可以去执行这个代码然后呢去把我们这个数据导入进去那么数据呢依然还是在我的这个F凡下面code下面的一个叫data.json这个呢数据还是之前我们所抓取到的那个数据然后呢我们就去让它去做一个写入那么OK那么我们来执行一下它
[02:21] 执行去run一下那么我们就等待它的一个执行那么执行结束之后啊那我们就可以把数据呢就可以写进去了OK那么我们稍微等待一下等待它的一个执行好那么现在呢就已经执行结束了那我们可以看一下这个数据那么你会发现在这个位置呢我们数据呢就已经就导入进去了大概呢我们数据呢基本上跟我们之前的数据呢也都是一样的一些数据啊没有任何问题好嘞
[02:51] 好那么到这里呢我们这个整个ES的集群搭建呢才算个呃才算是结束了那么我们已经把集群搭起来并且我们把这个我们的一个呃索引库呢创建好并且呢我们去把我们的测试数据呢也导入进去了哎OK好那么关于我们这个数据导入呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Java 代码向 Elasticsearch 集群批量导入数据，并展示数据在集群中的分布情况。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Elasticsearch Head 界面，集群名为 es-itcast-cluster，状态为 green，节点包括 node01、node02、node03，其中 node03 被选中。
画面2：展示 Advanced REST Client 的启动界面。
画面3：在 Typora 编辑器中显示 Elasticsearch 的索引设置和分词器配置，包含 "pinyin_analyzer" 和 "my_pinyin" tokenizer 的详细配置。
画面4：在 Advanced REST Client 中，执行了创建索引的请求，状态为 200 OK，响应头包含内容类型和字符集信息。
画面5：在 Elasticsearch Head 界面中，显示了索引 "haoke" 的分片分布情况，node01 分片 1、2、3、5，node02 分片 0、2、4、5，node03 分片 0、1、3、4。
画面6：在 Typora 编辑器中显示 Java 代码，用于导入数据，包含 "Test" 方法和数据读取逻辑。
画面7：在 IntelliJ IDEA 中显示 Java 代码，用于测试 REST API，包含创建请求和处理响应的逻辑。
画面8：在 IntelliJ IDEA 中显示 Java 代码，用于初始化 RestClient 和 ObjectMapper。
画面9：在 IntelliJ IDEA 中显示 Java 代码，用于处理数据导入，包含循环读取数据和分批发送的逻辑。
画面10：在 IntelliJ IDEA 中显示右键菜单，用于复制、粘贴或生成代码。
画面11：在 IntelliJ IDEA 中显示 Java 代码，用于处理数据导入，包含分批发送和计数逻辑。
画面12：在 Elasticsearch Head 界面中，显示了索引 "haoke" 的数据列表，包含多个字段如 image、orientation、houseType 等。
画面13：在 Typora 编辑器中显示文档目录，当前位于 "2.4. 部署RocketMQ集群" 下的 "2.4.1. 规划"。
画面14：在 Typora 编辑器中显示 Elasticsearch 的索引设置和分词器配置，与画面3内容相同。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面3：
```json
"settings": {
  "index": {
    "number_of_shards": 6,
    "number_of_replicas": 1,
    "analysis": {
      "pinyin_analyzer": {
        "tokenizer": "my_pinyin"
      },
      "tokenizer": {
        "my_pinyin": {
          "type": "pinyin",
          "keep_separate_first_letter": false,
          "keep_full_pinyin": true,
          "limit_first_letter_length": 16,
          "lowercase": true,
          "remove_duplicated_term": true
        }
      }
    }
  },
  "mappings": {
    "dynamic": false
  }
}
```

画面6：
```java
@Test
public void testBulk() throws Exception {
  Request request = new Request("POST", "/haoke/house_bulk");
  StringBuilder sb = new StringBuilder();
  String createStr = "{ \"index\": { \"_index\": \"haoke\", \"_type\": \"house\" } }";
  List<String> lines = FileUtils.readLines(new File("F:\\code\\data.json"), encoding: "UTF-8");
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
public void testSave2() throws Exception {
  Request request = new Request(method: "POST", endpoint: "/haoke/house_bulk");
  StringBuilder sb = new StringBuilder();
  String createStr = "{ \"index\": { \"_index\": \"haoke\", \"_type\": \"house\" } }";
  List<String> lines = FileUtils.readLines(new File(pathname: "F:\\code\\data.json"), encoding: "UTF-8");
  int count = 0;
  for (String line : lines) {
    sb.append(createStr + "\n");
    sb.append(line + "\n");
    if (count >= 200) {
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
if (!sb.toString().isEmpty()) {
  request.setJsonEntity(sb.toString());
  this.restClient.performRequest(request);
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面13：PPT 标题为 "2.4. 部署RocketMQ集群"，子标题为 "搭建2master:2slave的集群。"
画面12：表格数据包含字段如 image、orientation、houseType、rootMethod、time，数据行数为 12 行。

5) 无。

