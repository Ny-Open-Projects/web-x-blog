# 画面线理解：10.WebMagic抓取数据之导入数据到Elasticsearch（批量导入数据）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\10.WebMagic抓取数据之导入数据到Elasticsearch（批量导入数据）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:57, 01:23, 02:00, 03:00, 03:52, 04:24, 05:07, 05:33, 06:01, 06:44, 07:09, 07:35, 08:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:06:18

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
