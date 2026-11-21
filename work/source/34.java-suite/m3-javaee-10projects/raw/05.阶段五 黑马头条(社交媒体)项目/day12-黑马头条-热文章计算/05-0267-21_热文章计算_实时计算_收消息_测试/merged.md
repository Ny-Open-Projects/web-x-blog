# 21_热文章计算_实时计算_收消息_测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\21_热文章计算_实时计算_收消息_测试【海量资源尽在 666java.com】.mp4
- 时长 9分2秒（音频 543s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面的咱们就来去测试一下那测试起来呢其实比较方便啊那怎么办呢这个呢你只需要去启动当前的Article服务debug启动然后呢你在这发一条消息就可以了咱们这样咱们在这呢分别去打断点然后去跟一下好吧再去把这个流程再去走一遍稍等那当然这个啊这个我要去强调一个问题哪个问题呢就是刚才我改了个东西在这改了个东西
[00:32] 改哪个呢就是这个你要跟笔记上保持一致啊因为这个之前是定义了一个名称啊这个名称按理来说呢这个东西呢你可以随意定义啊其实只要是不重复都可以啊我现在是跟之前的笔记保持一致的啊其实你可以再次去其他定义其他的其实也没有问题啊行那这个这个消息已经来了是吧咱们之前是发过的啊那这样咱们先放行放行啊那放行完之后呢咱们就不管他了啊这也接到了是吧再放行
[01:05] 好那放行之后啊放行之后呢咱们这样咱们重新去发送一条消息好吧在这啊你去走debug走着然后呢咱们可以看一下数据库里边的数据是多少这个like是53看到了吧那这样咱们一会呢让他去改变让他去改变啊来看一看好正在发送啊发送的时候呢咱们可以看一下当前的这个值啊咱们可以跟一下当前这个值到底是啥啊
[01:39] 好还没有到这他应该发完之后他就能够到这了好来了之后你可以一步一步往下走当前当前 value就是update article message里边封装的就是你发送的数据可以看一下当前的我只是发送了当前的type是哪个是like是like add是1好这个设置完了然后接着往下看接着往下看然后他最终的是返回一个key value
[02:11] 里边是封装两个第一个是RT怪地然后第二个就是当前的这么一个参数like 冒号然后是爱的是几那就是几是吧好我先看当然咱们不到这咱们可以直接去到这直接到这好过来好来了到这之后你可以往下走往下走当前你就能看到当前那个Value这个Value是谁你看
[02:39] 可以看一下就是Lex冒号1就是你自己封装那个东西啊好咱们现在给他分割了分割完之后呢这个Lex肯定是有值的所以说他不会走这一步然后接着往下走往下走之后呢咱们又去封割了当前这个东西啊这个东西呢是咱们在上面定义的初始化的一个东西是吧那那那现在呢咱们要去给这些值呢去复制一个默认值默认值就是初始值啊初始值是0所以说咱们在这去做了一个循环
[03:08] 最终的它就是复完值之后都是0好稍等咱们把它走完好吧直接到这过来好这个到这好像是有问题是吧这个代码写的有问题稍等它这个循环应该是在外边在外边这样这个代码可能看起来比较恶我们稍微改一改好吧停了改成简单代码的话其实就怎么说呢
[03:44] 我稍微改造一下在这呢去挨个if其实你最终啊你要知道你最终返回的呢其实就是这一值然后最终呢是给每一个当前的这些东西呢去负值就可以了如果说没有值它又是啥呢没有值就是0那这个就比较容易了因为呢你在这啊你在这其实已经在这设了一个默认值都是0是吧所以说你在这啊直接去判断就可以判断谁呢判断当前这个lax
[04:14] 到底是给谁复职如果说是Lex的话很显然是给当前这个Lex去干嘛呢去加这个1加1啊但这个到底是加几的话根据你切割出来的这个东西是要判断的好吧那这个咱们就在这去写一写吧怎么写呢嗯如果说是Lex引号啊R equal那要是区分大要写啊不区分大要写啊用的是跟谁一样的是valuevalue呃ry
[04:46] 里边是0这个0是不是就是lack没问题不说是lack的话那怎么办这时候你就可以把这个lack去复制是加等于integer value of然后你可以把当前这个value-value是这就不是1了这就不是0了这是1这样的话就算是给它复制了这个这样理解起来还是比较简单的但是这个需要写4个
[05:19] 好那分别是啥呢分别是当前的collection是吧好然后是还有什么comment还有一个是mew好那这样设置完之后啊咱们分别要在这去改一下啊是col啊这个呢这个是当前的com啊这个呢这是mea好那这样的话咱们就设置完了你可以把下边的代码给它删了没有问题啊
[05:50] 那咱们目前这个东西呢其实就没有用了啊这个东西咱们可以不要啊因为暂时这个你要留下啊说这个值如果说这当前这个是弄那这时候呢你直接返回当前这个默认值就可以了好吧那行那这样改造完之后啊那咱们可以再来测一下再来测一下看看最终的结果是啥好吧来咱们再去启动一下当前的项目走咱们还是在这打断点啊好断点打断了啊
[06:21] 你也可以直接去打到这直接打到这也行好吧看看他到底能不能走到这然后呢看看能不能给当前那个like去复制就可以了然后呢他这个如果说这块没有问题啊那这时候呢他就会干嘛呢就会走到这然后是去更新咱们的什么呢更新啊在这吧更新咱们的这种数据库的数据啊好往下走这时候已经来了啊来了之后呢你可以往下走这个是还有之前的消息没有处理完啊所以说他就会直接到这啊
[06:51] 往下走咱们可以直接放行放行到这之后你可以看一下当前这个value是谁还是这个likes冒号1对吧那这时候它这个能匹配上那就是给这个like去加1对吧好往下走不加等于你看这个是不是1你看其他的没有没有的话那就是它就不执行然后最终你返回在字符串里边只有like是有值的其他的是没值好吧好咱们可以直接放行
[07:20] 放行放行完之后呢又来了是吧他这是有两个消息啊好没有问题啊好往下走这时候你可以看一下当前那个Value里边是有什么东西你看这里边东西呢你看当前的这个东西是10120这是阿迪挂地是吧当前的VU像这些是不是都是0呢OK这个Lake是Lake是1因为咱们刚才在这是加了Lake的数据的好吧这时候你也可以去刷新一下当前数据库
[07:48] 目前lag是80对吧那行那咱们下面呢就来去看一下看看能不能加1好走走好执行完了执行完之后呢你可以刷新一下数据库这个好像有点多啊81是吧没问题啊刚才那个啊可能数据数据是不是那一个数据啊是10120是不是就是81啊ok啊没问题那行那这个咱们就算是执行完了啊好那这个我再去强调一下又来了是吧
[08:20] 放行吧咱们把这个关掉也行啊关掉也行啊好简单再说一下这个东西啊那这份在买稍微改了改啊改了改改改完之后的效果呢其实呢你就根据当前的结果去改就可以了因为你最重要想要的字符块不就是拼接这个东西吗所以说呢你不用这一段呢其实也是可以的那这段呢其实写起来呢可能稍微麻烦一些稍微恶心一些啊但这个呢
[08:45] 可能稍微就是漏一些但是呢能够效果会更好啊所以说大家呢一定要能够用不同的方式去写不同的代码好吧那行那这个那这个整体的啊咱们算是讲完了刚才也测了一下啊大家下去的时候呢也可以去测一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
  state.dir = /tmp/Kafka-streams
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
          ArticleVisitStreamMessage message = Mapper.readValue(value, ArticleVisitStreamMessage.class);
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

