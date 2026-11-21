# 画面线理解：21_热文章计算_实时计算_收消息_测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\21_热文章计算_实时计算_收消息_测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:28, 01:11, 02:05, 02:57, 03:17, 03:44, 05:17, 05:47, 06:28, 07:08, 07:57, 08:27, 08:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:45:30

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Kafka Streams 应用中，通过自定义 Aggregator 处理文章行为事件（点赞、评论、收藏、浏览），并实现数据聚合与状态更新。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了 `HotArticleStreamHandler.java` 中的 `apply` 方法，用于处理聚合后的数据。
- 代码片段：
  ```java
  public String apply() {
      return "COLLECTION:0,COMMENT:0,LIKES:0,VIEWS:0";
  }
  ```

画面2：
- 展示了 `ArticleApplication` 的项目结构。
- 展示了 `application.properties` 配置文件内容：
  ```
  security.protocol = PLAINTEXT
  send.buffer.bytes = 50381648
  state.cleanup.delay.ms = 600000
  state.dir = /tmp/kafka-streams
  topology.optimization = none
  upgrade.from = null
  windows.ttl.changelog.additional.retention.ms = 36400000
  ```

画面3：
- 展示了 `BehaviorTest.java` 中的测试方法 `testLikesSave`。
- 代码片段：
  ```java
  @Test
  public void testLikesSave() {
      ApiUser user = new ApiUser();
      user.setId(1);
      ArticleReadUtils dto = new ArticleReadDto();
      dto.setArticleId(10120);
  }
  ```

画面4：
- 展示了调试器中的 `UpdateArticleMessage` 对象，其 `type` 字段值为 `"update_article"`。
- 对象内容：
  ```
  type = UpdateArticleType
  articleId = 10120
  upuserId = 1
  behaviorId = 2
  ```

画面5：
- 展示了 `apply` 方法中处理 `UpdateArticle` 类型消息的逻辑。
- 代码片段：
  ```java
  String aggKey = aggValue.split(regex)[0];
  String[] valArry = value.split(regex);
  if ("null".equals(valArry[1])) {
      return aggValue;
  }
  ```

画面6：
- 展示了 `switch` 语句，用于根据 `UpdateArticle.UpdateArticleType` 的值进行不同类型的聚合处理。
- 代码片段：
  ```java
  switch (UpdateArticle.UpdateArticleType.valueOf(valArry[0])) {
      case COLLECTION:
          col += Integer.valueOf(valArry[1]);
      case COMMENT:
          com += Integer.valueOf(valArry[1]);
      case LIKES:
          lik += Integer.valueOf(valArry[1]);
      case VIEWS:
          vie += Integer.valueOf(valArry[1]);
  }
  ```

画面7：
- 展示了 `switch` 语句中 `case LIKES` 的处理逻辑。
- 代码片段：
  ```java
  case LIKES:
      lik += Integer.valueOf(valArry[1]);
  ```

画面8：
- 展示了 `apply` 方法中处理 `UpdateArticle` 类型消息的逻辑。
- 代码片段：
  ```java
  if ("LIKES".equalsIgnoreCase(valArry[0])) {
      lik += Integer.valueOf(valArry[1]);
  }
  ```

画面9：
- 展示了 `apply` 方法中处理 `UpdateArticle` 类型消息的逻辑。
- 代码片段：
  ```java
  if ("COLLECTION".equalsIgnoreCase(valArry[0])) {
      col += Integer.valueOf(valArry[1]);
  }
  ```

画面10：
- 展示了 `apply` 方法中处理 `UpdateArticle` 类型消息的逻辑。
- 代码片段：
  ```java
  if ("VIEWS".equalsIgnoreCase(valArry[0])) {
      vie += Integer.valueOf(valArry[1]);
  }
  ```

画面11：
- 展示了调试器中的变量值，包括 `aggKey`、`value`、`aggValue`、`valArry`。
- 变量值：
  ```
  aggKey = "LIKES"
  value = "LIKES:1"
  aggValue = "COLLECTION:0,COMMENT:0,LIKES:0,VIEWS:0"
  valArry = ["LIKES", "1"]
  ```

画面12：
- 展示了 `ArticleHandleListener.java` 中的 `onMessage` 方法，用于处理 Kafka 消息。
- 代码片段：
  ```java
  public void onMessage(ConsumerRecord<String, String> consumerRecord, String data, Consumer<?, ?> consumer) {
      log.info("接收到的消息为: {}", data);
      String value = data.value();
      try {
          ArticleVisitStreamMessage message = mapper.readValue(value, ArticleVisitStreamMessage.class);
          ArticleVisitStreamDto dto = message.getData();
          appArticleService.updateArticleView(dto);
      } catch (IOException e) {
          e.printStackTrace();
      }
  }
  ```

画面13：
- 展示了 `HotArticleStreamHandler.java` 中的 `getSerivce` 方法。
- 代码片段：
  ```java
  public KStream<?, String> getService(KStream<?, String> stream) {
      return stream.map((key, val) -> {
          UpdateArticleMessage value = format(val);
          System.out.println(value);
          return new KeyValue<>(value.getData().getArticleId().toString(), value.getData().getType().name() + ":" + value.getData().getAddId());
      }).groupByKey().windowedBy(TimeWindows.of(10000)).aggregate(new Initializer<String>() {
  ```

画面14：
- 展示了 `apply` 方法中处理 `UpdateArticle` 类型消息的逻辑。
- 代码片段：
  ```java
  if ("LIKES".equalsIgnoreCase(valArry[0])) {
      lik += Integer.valueOf(valArry[1]);
  }
  ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
见上文各画面要点中列出的代码片段。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
