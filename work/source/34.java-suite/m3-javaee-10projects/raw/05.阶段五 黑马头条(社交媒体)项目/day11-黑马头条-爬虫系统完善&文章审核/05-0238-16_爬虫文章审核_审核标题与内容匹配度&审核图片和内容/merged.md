# 16_爬虫文章审核_审核标题与内容匹配度&审核图片和内容

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\16_爬虫文章审核_审核标题与内容匹配度&审核图片和内容【海量资源尽在 666java.com】.mp4
- 时长 14分5秒（音频 846s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 来下面咱们就来完成当前比较重要的方法这个方法咱们还是得看流程其实咱们状态为一其实已经判断到了是吧下面主要是这些内容第一个是标题与内容的匹配然后是审核文本审核图片最终是保存数据和创建索引好了咱们下面就来去一一去完成这些内容然后首先咱们在这还是得去先去干嘛呢
[00:30] 先去写下思路是吧这个要干嘛这个要去审核文本和内容内容和标题的匹配匹配度是吧然后第二个呢要去审核审核不是删核审核图片和文本第三个呢这时候啊两个如果说都过的话那这时候就说明咱们的文章已经干嘛
[00:58] 审核通过了审核通过要去保存数据保存哪个数据呢一个是文章文章信息文章还有什么文章的配置文章的内容还有什么还有作者信息作者还有什么还有一个是标签还有标签最后呢我们就可以干嘛呢可以去创建索引好再来一个最后就是更改状态为9好吧
[01:29] 那这个咱们就算是思路算是设置完了然后下面咱们就来去写代码首先咱们在这还是按照之前的套路去写比如说咱们要先去拿到一个时间获取它的执行时间点它然后是拿到这个时间然后咱们就在这去设置一个说你干嘛呢开始自动审核开始自动审核流程然后下面咱们就可以去真正的去做业务了
[02:00] 最好是在这再去做一个判断说None不等于当前的CL News不等于它之后咱们可以审核了把它给放在里边好一个咱们先要获取它的什么标题跟内容标题内容怎么拿就是当前的clnews.get一个叫做为什么说是这个方法其实你可以看一下
[02:31] 其实呢咱们在去保存当前文章内容的时候呢其实是已经压缩的那这会儿呢咱们要去审核的话肯定是要去先去解压先去解压所以说呢这个是解压缩之后的内容这个内容是可见的要不然的话你可能看不明白你可以看一下数据库里边我们打开当前随便一个找到CL News你看它存的内容是不是它呀
[02:58] 这个内容你是看不明白的所以说你要先去解压之后才能够看明白真正的一些文字内容好这是一个内容然后下面还有啥呢clnews.gettitleok那这个就是好拿到title之后咱们就在这可以做一个判断判断啥里边说是要content等于等于num或者是前的title等于等于num这时候这两个是不成为空的
[03:28] 咱们就可以直接return就可以了但return的话你得去告诉他吧所以说咱们在这直接告诉他你审核不通过就可以了在这去一个方法叫update cellnews好两个参数第一个参数就是当前的cellnews第二个参数就告诉他你为什么不停为什么审核没成功就是文内容内容标题我也空了
[03:59] 所以说你审核不通过啊这个方法没有咱们可以先创建出来啊那这个呢就是修改文章修改文章信息咱们一会再写好吧这个好像是有问题是吧咱们在这去写一个message好吧行那咱们继续往下去写啊这是一个但是呢在现在啊咱只是去做了一个真正的去设置或者要去审核的话或者要去那个
[04:33] 审核当前的内容和标题的匹配度的话咱们还要去调用一个工具类对吧这工具类叫什么叫computer.这个当前这个方法然后第一个呢是当前的content这个值说错了啊第一个就是content第二个呢才是title好最终呢它就能返回一个double的类型double值是吧那这个值呢咱们可以判断如果说呢它小于等于0的话说明
[05:04] 说明你这份审核没通过因为就是不匹配这个咱们就是可以在这去写和文章和标题不匹配好这也是审核通过也需要去复习行那这个就设置完了设置完之后咱们接着往下看下面咱还可以在这去设置个下面该干嘛了
[05:33] 去审核文本的内容啊所以说要是开始文本内容的审核好接着往下看那这个文本内容该怎么去审核呢这块内容呢咱们还是先去拿到一个什么拿到一个图片并且呢是要去解析当前的图片还有什么还有一个内容还有一个内容啊那这个怎么办呢其实咱们在这儿还是要去
[06:03] new list里边存的是一个str,叫img list等于一个new array然后咱们在这再去创一个str builder咱们之前其实差不多,sb等于new str builder然后咱们再去解析当前的功能现在patch
[06:32] Post的数据图片都是存到了当前的content中所以说这个图片跟文本你都需要干嘛都需要从content中去解析所以说咱们在这json.err有一个叫做pass object把当前的content装进去就可以了这个其实就是一个json array这不应该是一个object应该是一个arrayjson.err
[07:03] BusArray就是当前的content是一个JSONArray那为什么要去为什么是一个Array呢这个你还得去翻过头来你可以看一下当前的APArticle当前打开稍等我去找一下出去大家看一下就知道了APArticleOK就它这个没有是吧你得去找当前的content稍等
[07:39] 有点慢那么慢吗好拿到了拿到之后这个好像也不行是吧那这样你可以找到当前哪个笔记当前的第四天还是第三天应该是第三天第三天找到讲仪然后是有一个详情可以看一下还是咱们昨天打的笔记然后往下找找找然后是有一个叫做前台的东西稍等
[08:12] 找一找啊那就是第四天找一找讲一他然后找到这个view style你往上翻一翻往上翻一翻啊好就这个内容啊你看其实咱们最终要解析的内容呢其实这个东西看到了吗他呢外边是一个书组里边呢是一个一个的对象看到了吧一个一个对象咱们这时候要去筛出来texttext就是文本内容然后下面是image就啥的
[08:43] Image就是图片那种所以说咱们要去筛出来好那这时候咱们要去在这去写一个方法什么Handler有一个叫做textAndimagesM-A-D-S咱们需要去传几个参数第一个是当前的image然后第二个是sb三个就是别前的json而已好吧这个方法没有没有的话咱们也去放线出来这个就是解析
[09:20] 写习文本和图片这个啊其实这样啊这个咱们在之前是写过的咱们也可以之前拿过来拷过来之后呢咱们再用一下啊那这样啊经过这一步之后呢经过这一步之后啊咱们就能在这里边去获取到他的图片和他的内容图片和内容这时候呢你就已经获取到了啊那获取到文本和内容之后呢那这个是获取到所有的图片所以说呢那这个图片呢并不合适
[09:50] 因为咱们这个你不能说所有的图片都要去审核是吧这时候咱们可以做一个代表性的咱们可以去干嘛呢去截五张图片去审核这样也行当然你要是都审核的话其实也是可以都审核也是可以的那这样吧咱们就都审核好吧就都审核然后接着往下看都审核的话其实这个行可以吧都审核吧没事无非就是多花点钱对吧OK
[10:20] 然后下面的咱们就可以去进行去审核了审核要怎么审核呢拿下比如说文明审核文明审核那文明审核是不是得去调用谁的接口啊是不是对用阿里的接口啊所以说啊现在这啊就要去入接口读当前的类哪个类啊你可以这样你可以打开当前的哪啊澳门下边找到阿里云啊是不是这两个呀一个是阿里云tags阿里
[10:53] xscan request是这个东西啊这是审核文本用的啊好还有什么下面啊还有一个叫做阿里云的什么image scan request这是审核图片用的啊拿到之后呢这时候啊就比较简单了啊你可以直接用它审核图片咱们有一个叫做第一个啊xscan request
[11:28] 你可以把当前的s.toString放进去就可以了一种它就能返回一个response好拿到了response之后咱们就可以去判断了怎么判断其实这里边咱们还是按照之前的方式去进行判断如果说当前的response点它什么呢
[12:01] response不等于response并且response-equals是pass这样的话咱们就算是审核成功了这块咱们就可以去这样是非这个咱们也是改成或改成或这时候它就是等于没等于或者是啥或者是不等于pass的时候这时候就是审核成功
[12:34] 那审核不成功的话咱们就可以干嘛呢就可以直接return并且呢要去告诉他你为什么审核不成功咱们就可以update然后呢第一个是sell news第二个呢就是告诉你为啥不成功呢说你的文本内容不合规文本内容文本内容审核失败吧文本内容审核失败OK那这样就可以了这是审核文本
[13:05] 那下面还有审核图片是吧嗯审核图片就是差不多是吧怎么办呢阿里云然后是image scan.request点里面有一个他然后最终的是把image scan进去就可以了最终他也是返回一个response叫scan嗯叫image吧imad response好吧然后呢就可以判断了啊其实跟上面这个是一样的一样的啊
[13:38] 直接去跑过来当然这个呢这个值你要改改啊或者是他等于pass的时候呢你就是叫什么图片内容审核失败那这个啊这块内容呢咱们就算是做完了啊当前这个文本还有什么图片还有什么标题咱们就写到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个文章审核流程的实现，包括流程图、Java 代码逻辑、数据库表结构和相关依赖配置。

2) 按时间顺序列出每张画面的要点：
画面1: 展示一个文章审核流程图，包含“状态为1”、“审核中”、“审核通过”、“审核不通过”等节点，以及“存入数据库”的操作。流程图下方列出数据库表名：`article_config`, `article`, `article_label`。
画面2: IDE中显示 `ReviewCrawlerArticleServiceImpl.java` 文件，代码中定义了审核流程的入口方法 `autoReviewArticleByCrawler`，并注释“审核内容标题的匹配度”。
画面3: IDE中显示 `ReviewCrawlerArticleServiceImpl.java` 文件，代码中获取文章内容和标题：`String content = cNews.getUnCompressContent(); String title = cNews.getTitle();`。
画面4: IDE中显示 `ReviewCrawlerArticleServiceImpl.java` 文件，代码中对内容和标题为空的情况进行判断并更新状态：`if(content==null || title == null) { updateNews(cNews, message: "文章内容或标题为空"); return; }`。
画面5: IDE中显示 `ReviewCrawlerArticleServiceImpl.java` 文件，代码中计算内容和标题的相似度：`double degree = Compute.SimilarDegree(content, title);`。
画面6: IDE中显示 `ReviewCrawlerArticleServiceImpl.java` 文件，代码中对相似度为0的情况进行处理：`if(degree < 0) { ... }`。
画面7: MySQL数据库管理工具中显示 `c_news` 表的数据和结构，包含字段如 `id`, `task_id`, `url`, `title`, `name`, `content`, `type`, `channel_id`, `labels`。
画面8: PPT页面标题为“文章详情前后端成形记”，内容包括“熟悉Zookeeper的对接集成”、“熟悉分布式自增主键的封装”、“掌握文章详情页面的需求和实现流程”、“掌握mockMvc测试的使用场景和方法”。子章节“1.1 依赖导入”中包含 Maven 依赖配置：
```xml
<properties>
    <curator.version>4.2.0</curator.version>
</properties>
<dependency>
    <groupId>org.apache.curator</groupId>
    <artifactId>curator-recipes</artifactId>
    <version>${curator.version}</version>
</dependency>
```
画面9: IDE中显示 `ReviewCrawlerArticleServiceImpl.java` 文件，代码中定义了 `handlerTextAndImages` 方法，用于处理文本和图片。
画面10: IDE中显示 `ReviewCrawlerArticleServiceImpl.java` 文件，代码中定义了 `autoReviewArticleByCrawler` 方法的入口和 `private` 修饰的 `ReviewCrawlerArticleService` 实例。
画面11: IDE中显示 `ReviewCrawlerArticleServiceImpl.java` 文件，代码中定义了 `Compute.SimilarDegree` 方法的调用和 `Log.info` 日志输出。
画面12: IDE中显示 `ReviewCrawlerArticleServiceImpl.java` 文件，代码中对 `null` 值进行判断：`if(null == response) { ... }`。
画面13: IDE中显示 `ReviewCrawlerArticleServiceImpl.java` 文件，代码中调用 `aliyunImageScanRequest.imageScanRequest` 方法进行图片审核。
画面14: IDE中显示 `ReviewCrawlerArticleServiceImpl.java` 文件，代码中对图片审核结果进行判断：`if(null == imageResponse || !imageResponse.equals("pass")) { ... }`。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1: 无代码或配置。
画面2: 无代码或配置。
画面3: 无代码或配置。
画面4: 无代码或配置。
画面5: 无代码或配置。
画面6: 无代码或配置。
画面7: SQL 语句：
```sql
CREATE TABLE `c_news` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `task_id` int(11) DEFAULT NULL COMMENT '任务ID',
  `url` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '文章链接',
  `title` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '文章标题',
  `name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '文章作者',
  `content` text COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '文章内容',
  `type` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '文章类型',
  `channel_id` int(11) DEFAULT NULL COMMENT '频道ID',
  `labels` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '标签',
  `original_time` datetime DEFAULT NULL COMMENT '发布时间',
  `submit_time` datetime DEFAULT NULL COMMENT '提交时间',
  `status` int(11) DEFAULT NULL COMMENT '状态',
  `reason` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '拒绝理由',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```
画面8: XML 配置：
```xml
<properties>
    <curator.version>4.2.0</curator.version>
</properties>
<dependency>
    <groupId>org.apache.curator</groupId>
    <artifactId>curator-recipes</artifactId>
    <version>${curator.version}</version>
</dependency>
```
画面9: 无代码或配置。
画面10: 无代码或配置。
画面11: 无代码或配置。
画面12: 无代码或配置。
画面13: 无代码或配置。
画面14: 无代码或配置。

4) PPT 标题、架构图/流程图的结构、表格数据：
画面8: PPT 标题为“文章详情前后端成形记”，内容包括“熟悉Zookeeper的对接集成”、“熟悉分布式自增主键的封装”、“掌握文章详情页面的需求和实现流程”、“掌握mockMvc测试的使用场景和方法”。子章节“1.1 依赖导入”中包含 Maven 依赖配置。
画面1: 流程图结构：从“状态为1”开始，判断“是否审核中”，如果是则继续判断“审核是否通过”，如果通过则“存入数据库”，如果不通过则“审核不通过”。
画面7: 数据库表结构：`c_news` 表包含字段 `id`, `task_id`, `url`, `title`, `name`, `content`, `type`, `channel_id`, `labels`, `original_time`, `submit_time`, `status`, `reason`。

5) 无。

