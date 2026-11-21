# 20_爬虫文章审核_创建索引

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\20_爬虫文章审核_创建索引【海量资源尽在 666java.com】.mp4
- 时长 9分28秒（音频 569s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就来去把这个索引给创建一下咱们这个保存这块基本上都完事了这个索引该怎么去创建呢这个你可以完全可以参考咱们之前去审核自媒体文章的时候是那个代码是差不多咱们就再去写一下咱们就快点写一下首先咱们在这再去封装一个方法叫createcreate什么呢c-i-e-a-t然后是ex index好吧
[00:28] 然后咱们需要去传两个参数啊一个是AP article第二个是CL News好那这两个方法啊方法都没有没有咱们就创建出来好这是创建所有对象啊下面呢咱们要创建所有的时候他需要有一个异常需要抛出所以说咱们在这直接去加一个trag catch啊好这个这句话呢放到上面咱们在这catch一下这是exception然后下面呢咱们要去打印一下
[01:05] 然后那个关之后呢下面咱们主要的是来构建当前的对象那这个对象咱们要创建所以怎么创建呢其实这时候呢你需要去在当前的内亚去接一个什么rest client加上他之后啊这种呢咱们就可以去用他去构建咱们的所有对象里边呢他需要一个action对象
[01:34] 这个action它是个接口,我帮您看一下这个接口,这时候咱们可以用它的什么用它的实现类去做可以找到它的实现类我找翻翻翻翻谁呢,咱们是找一个叫做index的一个对象index找一找没有吗好,就它,你看是在这个包下边io.searchbox.curve是吧,是这个index所以说咱们在这直接用index去创建就可以了好吧
[02:06] 那首先呢是indexindexindexindex等于谁呢其实这时候呢咱们需要去来固件一个对象啊哪个对象呢你看啊这边有一个index.build用build里边呢这时候啊来看一下它这里边咱们需要去传一个对象这个对象啊说一下这个对象呢其实就是你要锁引的文档对象
[02:34] 给索引的文档对象啊所以说这时候啊咱们还要再去封装一个对象那这个对象呢主要是来去保存文档的这个对象咱们之前呢其实也教授过啊那个呢叫esindexentity是他吧所以说呢你在这啊扭一个扭一个啊然后他咱们再封装一个好吧save什么呢save esindexentity好吧
[03:03] 传输的参数呢第一个是EP article第二个呢就是CL news这个对象没有我们就来复建一下这个对象呢就是怎么着构建索引索引索引索引对象那这个咱们一会再写咱们先把这段给完成这时候呢你如果说拿到了一个ES S index entity的话这时候呢你就可以往里边去装一下它可以接受任何参数
[03:38] 下面怎么办呢?
[03:40] 就可以用dodr.dr再去设置两个东西一个是id你可以再去给这个文档设置一个id,这个id是谁?
[03:48] 就是咱们取的是aprtq中的id然后你to string一下,因为它是一个string型的然后再往下咱们还有什么呢?
[03:58] dodr.dr咱们有一个refresh你直接设置一个tool就可以了,然后刷新一下好吧那这样的话咱们就算是设置完了
[04:08] 说完之后下面这个东西你需要去构建一下用todo. 咱们有一个什么indexindex其实咱们之前写过一个常量这个常量的话叫什么exindexconstance.咱们有一个articleindex就是上面这个东西这就是咱们缩影库的名称是吧然后下面还有什么typetype的话其实也是用一个常量是吧它有一个叫做define doc
[04:38] 最后是有一个这样的话咱们就把这个bs给构建了构建完之后你就可以直接放到这它会返回一个返回这个这个有错误咱们先抛出来好吧这个返回啥呢咱们返回一个gestest result返回一个它就可以了那这个返回它之后咱们可以去判断一下
[05:11] result不等于none并且咱们主要说下面这个result.is就是是否成功是吧如果说它不成功的话这时候咱们就去po一个一堂po一堂th through new runtime这里边咱们就可以去设置一个说啥呢叫result.get error message
[05:40] 咱们可以在后边再去补充一下说啥呢说插入更新索引不索引吧索引失败好再加一个东西可以了那行这样的话咱们就这个索引这个流程咱们就算是做完了下面还有一个东西是吧是不是这个这个还没做呀所以说咱们在这还要去这个对象给封装咱们首先还是得先去创建这么一个对象ES
[06:11] 等于new一个什么esIndexEntity然后下面咱们只要去封装里边的参数就可以啊esIndex.setID那这个ID就是aparticled.getID这个它需要构建一下用这个这个是一个integer那它需要的啥呢需要的是一个lang那这时候咱们就构建一个langnew一个lang好把后面东西装进去就可以了
[06:43] 然后下面接着我们要看然后下面还有啥呢s.s.s.content这content是一个内容是吧比如说你从哪去从当前的article中还是clnews中那这里边显然是没有内容的这里边有吗有好那咱们就从clnews里边去拿s.s.content是content呢还是上面这个呢显然是上面这个解压之后的是吧这是解压之后的
[07:14] 你说你要你取的时候呢那要是拿到解压之后的那种文本内容啊好拿到之后呢咱们接着往下看ES index.set里边还有一个叫做titletitle的话咱们也可以从cellnews中去拿title好get title这个好像也不行是吧我看看
[07:46] 这不是status这是title写错了行那咱们先写这个状态也行这状态的话咱们默认给一个什么给一个1就可以了好然后下面再往下看点settitle好吧这个把这个title给设置一下clnews.settitle好再往下看es.set这里边还有一个叫做他他他他就状态给一个好吧new有什么
[08:17] 又一个好然后再往下啊ex index.setpublish time这个是完了是吧.set这些咱们都有了啊就是一个channel id这个user id咱们就不给了啊咱们给一个channel id这个channel id那怎么给那你说从这边去呢还是从这边去呢这都行无所谓啊但是呢你要去判断一下这个channel id有可能是为空所以说咱们在这啊
[08:48] AP article.getChinaID不等于None的时候这时候咱们再去给它装入当前这个ChinaID就可以了AP article.getChinaID这个也要构建一下把这个进去最终你把它返回就可以了return当前的esIndexEntity我们就这个开始创建完了
[09:21] 整个索引呢咱们也算是做完了啊行那下面还有一个更新状态所以咱们一会再说

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Java 项目中使用 Jest（Elasticsearch 客户端）为文章实体创建并更新索引。

2) 按时间顺序列出每张画面的要点：
画面 1:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  //保存标签
  saveArticleLabel(aparticle);
  //保存文章
  saveArticle(aparticle);
  //保存文章内容
  saveArticleContent(content_aparticle);
  //更改状态为 9
  ```

画面 2:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  private
  ```
  代码补全弹窗显示了 `private` 关键字的可用选项，包括 `Private`、`PrivateKey`、`PrivateClassLoader` 等。

画面 3:
- 代码位置：搜索结果页面（非代码文件）
- 代码内容：
  ```
  import
  Choose Implementation of Action (8) found:
  Refresh (io.searchbox.indices.refresh)
  Reindex (io.searchbox.indices.reindex)
  Revert (io.searchbox.indices.revert)
  RestoreSnapshot (io.searchbox.indices.snapshot)
  ScavengeStatus (io.searchbox.indices.scavenge)
  Search (io.searchbox.indices.search)
  SearchScroll (io.searchbox.indices.searchscroll)
  SearchShards (io.searchbox.indices.searchshards)
  SingleResultAbstractDocumentTargetedAction (io.searchbox.action)
  State (io.searchbox.indices.state)
  TaskInformation (io.searchbox.indices.task)
  TemplateAction (io.searchbox.indices.template)
  ```

画面 4:
- 代码位置：Elasticsearch 实体类文件
- 代码内容：
  ```java
  package com.heima.common.common.pojo;

  public class EsIndexEntity {
      private Long id;
      private String content;
      private Long channelId;
      // private Date pub_time;
      private Date publishTime;
      private Long status;
      private String title;
      private Long userId;
      private String tag;
  }
  ```

画面 5:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  private void createEsIndex(ApArticle aparticle, CNews cNews) {
      EsIndexEntity esIndexEntity = saveEsIndexEntity(aparticle, cNews);
      Index.Builder builder = new Index.Builder(esIndexEntity);
      builder.id(aparticle.getId().toString());
      // ...
  }
  ```
  代码补全弹窗显示了 `Index.Builder` 的方法，如 `id`、`type`、`index`、`refresh` 等。

画面 6:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  Index index = builder.index(ESIndexConstants.ARTICLE_INDEX).type(ESIndexConstants.DOC).build();
  jestClient.execute(index);
  ```
  代码补全弹窗显示了 `ESIndexConstants` 类中的常量，如 `ARTICLE_INDEX`、`AUTHOR_INDEX`、`USER_INDEX`、`DEFAULT_DOC`。

画面 7:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  Index index = builder.index(ESIndexConstants.ARTICLE_INDEX).type(ESIndexConstants.DOC).build();
  JestResult result = jestClient.execute(index);
  if (result != null && result.isSucceeded()) {
  ```
  代码补全弹窗显示了 `JestResult` 类的常用方法，如 `isSucceeded()`、`getErrorMessage()`。

画面 8:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  if (result != null && result.isSucceeded()) {
      throw new RuntimeException(result.getErrorMessage()) + "插入更新索引失败!";
  }
  ```
  代码补全弹窗显示了 `RuntimeException` 类的构造方法。

画面 9:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  private EsIndexEntity saveEsIndexEntity(ApArticle aparticle, CNews cNews) {
      EsIndexEntity esIndexEntity = new EsIndexEntity();
      esIndexEntity.setId(new Long(aparticle.getId()));
      // ...
  }
  ```

画面 10:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  esIndexEntity.setContent(cNews.getCompressContent());
  ```

画面 11:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  esIndexEntity.setTitle(cNews.getTitle());
  ```

画面 12:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  esIndexEntity.setStatus(cNews.getStatus());
  ```

画面 13:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  if (aparticle.getChannelId() != null) {
      esIndexEntity.setChannelId(aparticle.getChannelId());
  }
  ```

画面 14:
- 代码位置：ReviewCrawlerArticleServiceImpl.java
- 代码内容：
  ```java
  @Autowired
  private JestClient jestClient;

  private void createEsIndex(ApArticle aparticle, CNews cNews) throws TOException {
      EsIndexEntity esIndexEntity = saveEsIndexEntity(aparticle, cNews);
      Index.Builder builder = new Index.Builder(esIndexEntity);
      builder.id(aparticle.getId().toString());
      builder.refresh(true);
      Index index = builder.index(ESIndexConstants.ARTICLE_INDEX).type(ESIndexConstants.DEFAULT_DOC).build();
      JestResult result = jestClient.execute(index);
      if (result != null && result.isSucceeded()) {
          throw new RuntimeException(result.getErrorMessage()) + "插入更新索引失败!";
      }
  }
  ```

