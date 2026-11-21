# 19_自媒体文章自动审核_自媒体发布文章_测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\19_自媒体文章自动审核_自媒体发布文章_测试【海量资源尽在 666java.com】.mp4
- 时长 3分52秒（音频 232s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去测试一下啊那测试怎么测试呢测试的话其实就应该启动当前的工程对吧首先呢咱们需要去启动当前的Media打开Media然后在这去打开引导类啊直接去右键debug启动就可以了啊然后呢咱们同时呢再去启动admin好启动完之后呢咱们在这啊稍等一下啊咱们需要去启动前端的工程前端工程其实我已经启动了
[00:33] 我已经启动了咱们在这可以直接去退出咱们测试的实践当我去登录完登录上之后咱们需要去发布一条文章发布文章之后它应该自动的去审核审核通过之后我就干嘛呢我就在当前的这个当前的这个AP article中去添加一条数据是吧没问题那这样咱们为了测试方便一些咱们在这可以去打个断点
[01:04] 看其中的时候没有报错好没有问题这个也没有问题行既然没问题的话咱们下面就来去测试一下咱们可以在接收消息的这一块去打印一个断点好吧在这打断点行咱们下面就来去设置一下然后点一下然后这已经登录了这已经打开了咱们可以输入23然后是123然后点登录
[01:32] 好登录进来之后呢咱们找到当前的发布文章标题比如说我去设立个6666好吧然后这个标题也是666吧无所谓啊当前的是然后这个呢是此刻这个内容呢咱们可以随便设啊好加一个图片可以在下面呢再去加一些内容比如说还是666啊然后可以再加个图片啊行那这个就是咱们内容咱们封面呢是一个单图的咱们可以设置一个
[02:07] 好上车完之后啊下面现在呢我就去提交看看这边能不能接收到消息就可以啊点提交稍等啊他现在新登新登成功了因为他是异物的所以说他应该干嘛呢他应该是在这边去接收的消息你看断点已经到这了说明我干嘛呢已经接收到消息了啊往下走啊这个value里边咱们可以找一找啊当前这个7102是不是有啊RT和RT看到了吧没问题啊好可以咱们往下走走
[02:37] 把这个转换了一下然后转换完之后你可以看MessageMessage里边其实就有咱们的内容第一个是Type第二个是DateDate里边有两个一个TypeType就是当前的Media然后第二个就是Adj7102该有的这都有好 往下走走走走走这时候就去审核了审核这样咱们可以在这先审核好吧用这个我也可以去筛选一下看看到底有没有666
[03:06] 当前的是title看看有没有包含6666的确定应用没有啊没有完之后呢我让他去审核审核完稍等咱们在这去查一下666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
[03:40] 666看是不是已发表了好没问题啊那目前咱们这个生产者和消费者啊都算是结束了整体的审核文章咱们也结束了好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Kafka 消息队列的自动审核文章发布系统，从代码实现、数据流转到前端发布和数据库存储的完整流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IntelliJ IDEA 中，右键点击 `AutoReviewArticleListener.java` 文件，弹出菜单，准备进行操作（如关闭、拆分、重命名等）。
画面 2: 在 IDEA 中浏览项目结构，当前选中 `MediaApplication` 类，位于 `com.heima.media` 包下。
画面 3: 在 IDEA 中打开 `detail.Vue` 文件，显示 Vue 组件代码，用于配置文章详情页的编辑器，包含 `pickerOptions` 和 `lineInfo` 等配置项。
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
        SubmitArticleAuthMessage message = Mapper.readValue(value, SubmitArticleAuthMessage.class);
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
        SubmitArticleAuthMessage message = Mapper.readValue(value, SubmitArticleAuthMessage.class);
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

