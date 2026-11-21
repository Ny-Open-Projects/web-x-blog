# 画面线理解：11.部署Elasticsearch集群之创建索引库以及导入数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\11.部署Elasticsearch集群之创建索引库以及导入数据【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:19, 00:34, 00:52, 01:03, 01:24, 01:30, 01:38, 02:02, 02:21, 02:29, 02:42, 02:52, 03:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:52:56

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
