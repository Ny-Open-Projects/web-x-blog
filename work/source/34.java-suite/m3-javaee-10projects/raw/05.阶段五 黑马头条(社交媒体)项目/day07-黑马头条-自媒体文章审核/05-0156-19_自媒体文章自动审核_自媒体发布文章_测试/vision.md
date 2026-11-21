# 画面线理解：19_自媒体文章自动审核_自媒体发布文章_测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\19_自媒体文章自动审核_自媒体发布文章_测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:17, 00:30, 00:52, 01:07, 01:16, 01:48, 01:56, 02:06, 02:20, 02:48, 03:00, 03:18, 03:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:29:27

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Kafka 消息队列的自动审核文章发布系统，从代码实现、数据流转到前端发布和数据库存储的完整流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IntelliJ IDEA 中，右键点击 `AutoReviewArticleListener.java` 文件，弹出菜单，准备进行操作（如关闭、拆分、重命名等）。
画面 2: 在 IDEA 中浏览项目结构，当前选中 `MediaApplication` 类，位于 `com.heima.media` 包下。
画面 3: 在 IDEA 中打开 `detail.vue` 文件，显示 Vue 组件代码，用于配置文章详情页的编辑器，包含 `pickerOptions` 和 `lineInfo` 等配置项。
画面 4: 在 Navicat for MySQL 中，展示 `heima-news` 数据库的表结构，包括 `ap_article`、`ap_user`、`ap_article_config` 等表，以及 `migration` 相关的触发器和存储过程。
画面 5: 在 IDEA 中，调试控制台输出 Kafka 消费者日志，显示多个分区的消费完成信息，如 `onPartitionsAssigned` 和 `onComplete`。
画面 6: 在 IDEA 中，查看 `AutoReviewArticleListener.java` 代码，其中定义了 `topic` 方法和 `onMessage` 方法，用于处理 Kafka 消息。
画面 7: 在前端页面，显示文章发布表单，用户正在填写文章标题、标签、定时发布时间和内容。
画面 8: 在前端页面，用户上传了一张图片，图片已显示在文章内容区域。
画面 9: 在前端页面，用户从图片库中选择并确认上传了多张图片。
画面 10: 在 IDEA 中，调试器断点处显示 `onMessage` 方法正在处理消息，变量 `value` 被解析。
画面 11: 在 IDEA 中，调试器断点处显示 `message` 对象的详细信息，包括 `name="WMEDIA"`、`ordinal=0` 和 `articleId=7102`。
画面 12: 在 Navicat for MySQL 中，查询 `ap_article` 表，显示文章列表，其中包含 `id=666666` 的文章。
画面 13: 在 Navicat for MySQL 中，执行 SQL 查询 `SELECT * FROM 'ap_article' WHERE 'id' LIKE '666666%' LIMIT 0, 1000`，查询结果为空。
画面 14: 在前端页面，显示文章列表，其中包含 `id=666666` 的文章，状态为“已发布”，并显示“上传”按钮。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```javascript
export default {
  name: 'ContentManage',
  data() {
    return {
      forms: {
        type: '0',
        time: '',
        etime: '',
        list: [],
        all: {},
        graph: {},
        pie: {},
        lineInfo: [
          { name: '发文章', type: 'article' },
          { name: '点赞数', type: 'read_count' },
          { name: '评论数', type: 'comment' },
          { name: '转发数', type: 'collection' },
          { name: '不喜欢', type: 'unlikes' }
        ],
        pickerOptions: {
          disabledDate(time) {
            return time.getTime() > Date.now()
          }
        }
      }
    }
  }
}
```

画面 6:
```java
private KafkaTopicConfig kafkaTopicConfig;
private @Autowired TestKafkaListener testKafkaListener;
private @Autowired ReviewMediaArticleService reviewMediaArticleService;

public String topic() {
    return kafkaTopicConfig.getSubmitArticleAuth();
}

@Override
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    String value = consumerRecord.value();
    log.info("接收到的消息为：{}", value);
    try {
        SubmitArticleAuthMessage message = mapper.readValue(value, SubmitArticleAuthMessage.class);
        if (message != null) {
            SubmitArticleAuto.ArticleType type = message.getData().getType();
            if (type == SubmitArticleAuto.ArticleType.WMEDIA) {
```

画面 10:
```java
public void onMessage(ConsumerRecord<String, String> consumerRecord, Consumer<?, ?> consumer) {
    String value = consumerRecord.value();
    log.info("接收到的消息为：{}", value);
    try {
        SubmitArticleAuthMessage message = mapper.readValue(value, SubmitArticleAuthMessage.class);
        if (message != null) {
            SubmitArticleAuto.ArticleType type = message.getData().getType();
            if (type == SubmitArticleAuto.ArticleType.WMEDIA) {
```

画面 11:
```java
message
  name = "WMEDIA"
  ordinal = 0
  articleId = (integer) 7102
```

画面 12:
```sql
SELECT * FROM 'ap_article' LIMIT 0, 1000
```

画面 13:
```sql
SELECT * FROM 'ap_article' WHERE 'id' LIKE '666666%' LIMIT 0, 1000
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
