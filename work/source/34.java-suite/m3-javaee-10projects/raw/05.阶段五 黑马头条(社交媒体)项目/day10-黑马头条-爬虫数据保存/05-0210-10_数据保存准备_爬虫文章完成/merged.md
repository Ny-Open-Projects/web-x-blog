# 10_数据保存准备_爬虫文章完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\10_数据保存准备_爬虫文章完成【海量资源尽在 666java.com】.mp4
- 时长 7分8秒（音频 428s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来完成最后一个这种保存准备的一个接口啊就是旁证文章这文章呢咱们只是做一个增删改查而最主要的是做一个这种新增因为呢咱们要从当前这个页面上是吧比如说你要从某一个网站上面去爬去某一条文章某一条文章之后呢咱们要去保存到数据库中那保存到哪呢哎就是目前咱们说这个旁证文章这个呢是对应的表是cell news
[00:28] 你也可以打开当前的他就是clnews这里边咱们也可以简单的去看一下大家那个表说主件什么任务ID这因为他后期咱们可以做一个什么做一个当前的这种调度还有一个是你爬的是哪个URL是吧标题作者名称内容内容这里有还有是布局布局还有图文ID图文频道ID这个频道咱们要去过来连上是吧还有就是当前的label标签
[00:58] 还有是label关联的ID原文时间创建时间提交时间啊这些咱们都要去设置啊当然这个Cedars呢目前的话呢咱们都是在审核啊其实你要爬过来之后呢都是1直接就是1啊然后还有一个发布时间啊咱们有一个不定时是吧OK啊还有一个拒绝理由啊8啊但是你这个拒绝之后呢咱们有一个描述啊就是描述啊还有是article ID那这个article ID啊是审核完之后
[01:26] 审核完之后因为这个文章啊他并不会干嘛呢并不会直接去发到当前的APP库中因为APP库呢是让用户看的这个呢只是爬出来爬出来之后呢他同样需要审核审核的单文啊咱们之前是写过自媒体的这个爬虫子呢咱们后期也会写好吧行那这个咱们就先说到这啊然后下面咱们就来去看一下当前这个MIPR啊这MIPR的话呢其实也比较简单都是做一些增删改查你看啊
[01:56] 比如说删除是吧新增新增这是查询修改修改修改有那么多修改是吧还有就是一个查询这是按条件查询还有根据URL删除根据URL删除还有一个就是怎么样去查询行那这个就直接拷过来就可以了好到当前的modelmodel在下边然后是当前的myproc有一个colors拷贝过来好了那这个就完了
[02:30] 之后呢你这样啊你再去创建一个什么创建一个它的映射文件什么情况这个大纲怎么没了呢好了啊好找到当前的映射啊找到映射mypress colors右键创建文件创建之后呢你可以把它直接拷过来啊
[03:00] 当然这些方法呢咱们也用不完啊咱们只是用一个增长改查刚才说了啊那也是已被后期使用所以说咱们在这儿尽量去完善一些后期咱们关注的麦普尔还是比较少啊行那这个创建完之后啊检查一下啊有没有出问题有没有出问题啊好像是没有事是吧那没有事的话咱们现在啊就来去编写Service那这个Service呢你需要自己去编写然后找到这儿找到这儿啊在这儿去创建是这儿吧看看啊好了没错啊
[03:30] 在这去创建一个CRNNUS怎么叫Color, C-R-A-W-L-E-R, Color News Service它是一个接口这里边咱们说了增商改查先做一个新增Save News参数就是CRNNUS好这是保存然后下面还有什么下面还有一个叫Void,叫Applete
[04:08] news这个呢也是clnews好是更新好下面还有一个删除是吧删除你要注意啊这个删除的话咱们根据主介删除呢还是怎么着呢这样咱们是根据当前的url删除啊所以说这会你要注意一下string的url好删除好下面还有一个查询public然后是
[04:42] 返回的是一个列表CIO news大家包啊当时叫curry list参数呢就是还是当前的CIO news好是查询查询完之后啊下面呢咱们就来去干嘛呢去编写它的总时限类啊MPL然后时限这个还是好写啊Service umservo warning下面要去注入
[05:31] 哪个入入他的mypr是吧private然后是clnewsmypr好好嘞那这时候呢咱们就去直接去保存就可以了而有一个insertinsertselectiveok而insertselective叫clnews好是一个是吧然后呢咱们接着往下看然后是update那就update呗
[06:04] CL News这里面没有业务逻辑基本上啊什么呢有一个叫做update其实一样啊这是一个啊下面还有删除是吧删除的话呢这个啊这个的话咱们来看一看啊有一个delete by ur其实里面有啊CL News看一下deleteur是吧你把这ur传进去就可以了好吧那行那这是一个啊是还有一个叫做CL Newsmyport
[06:34] touristslacklist叫slacklist叫cellnews那这个咱们就算是设置完了这个咱们也不去测试了你们自己去测一下就可以了这个肯定是没有问题的因为代码还是比较简单的没有什么业务没有什么太多业务有业务的话咱们可以测一测行那咱们一会就来去完善咱们的爬虫系统然后让它能够
[07:03] 爬出来之后呢能够直接存储到咱们的数据库中好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过 MyBatis 框架实现对 CNews 实体类的增删改查（CRUD）操作，包括定义接口、编写实现类、配置 Mapper 文件及数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了项目结构和代码文件，当前在 `CrawlerNewsCommentServiceImpl.java` 文件中。
- 代码片段：`public class CrawlerNewsCommentServiceImpl implements CrawlerNewsCommentService {`
- 代码片段：`@Autowired private CNewsCommentMapper cNewsCommentMapper;`
- 代码片段：`public void saveComment(CNewsComment cNewsComment) { cNewsCommentMapper.insertSelective(cNewsComment); }`

画面 2：
- 展示了 MySQL 数据库的 DDL 语句，用于创建 `c_news` 表。
- 代码片段：`CREATE TABLE `c_news` (`
- 代码片段：`id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',`
- 代码片段：`url varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '文章链接',`
- 代码片段：`title varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '文章标题',`
- 代码片段：`content text COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '文章内容',`
- 代码片段：`label_id int(11) DEFAULT NULL COMMENT '标签ID',`
- 代码片段：`channel_id int(11) DEFAULT NULL COMMENT '频道ID',`
- 代码片段：`type varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '文章类型',`
- 代码片段：`created_time datetime DEFAULT NULL COMMENT '创建时间',`
- 代码片段：`publish_time datetime DEFAULT NULL COMMENT '发布时间',`
- 代码片段：`status varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '文章状态',`
- 代码片段：`reason varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '文章理由',`
- 代码片段：`article_id int(11) DEFAULT NULL COMMENT '发布文章ID',`
- 代码片段：`PRIMARY KEY (`id`),`
- 代码片段：`ENGINE=InnoDB AUTO_INCREMENT=3119 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;`

画面 3：
- 展示了 `CrawlerNewsCommentServiceImpl.java` 文件，其中定义了 `saveComment` 方法。
- 代码片段：`@Service @SuppressWarrings("all") public class CrawlerNewsCommentServiceImpl implements CrawlerNewsCommentService {`
- 代码片段：`@Autowired private CNewsCommentMapper cNewsCommentMapper;`
- 代码片段：`public void saveComment(CNewsComment cNewsComment) { cNewsCommentMapper.insertSelective(cNewsComment); }`

画面 4：
- 展示了 `CNewsMapper.xml` 文件，其中定义了 `selectByIdAndStatus` 方法。
- 代码片段：`<Mapper namespace="com.heima.model.mappers.crawlers.CNewsMapper">`
- 代码片段：`<resultMap id="BaseResultMap" type="com.heima.model.crawler.pojos.CNews">`
- 代码片段：`<id column="id" property="id"/>`
- 代码片段：`<result column="title" property="title"/>`
- 代码片段：`<result column="name" property="name"/>`
- 代码片段：`<result column="type" property="type"/>`
- 代码片段：`<result column="channel_id" property="channelId"/>`
- 代码片段：`<result column="labels" property="labels"/>`
- 代码片段：`<result column="original_time" property="originalTime"/>`
- 代码片段：`<result column="created_time" property="createdTime"/>`
- 代码片段：`<result column="submitted_time" property="submittedTime"/>`
- 代码片段：`<result column="status" property="status"/>`
- 代码片段：`<result column="publish_time" property="publishTime"/>`
- 代码片段：`<result column="reason" property="reason"/>`
- 代码片段：`<result column="article_id" property="articleId"/>`

画面 5：
- 展示了 `CNewsMapper.xml` 文件，其中定义了 `selectByIdAndStatus` 方法。
- 代码片段：`<Mapper namespace="com.heima.model.mappers.crawlers.CNewsMapper">`
- 代码片段：`<resultMap id="BaseResultMap" type="com.heima.model.crawler.pojos.CNews">`
- 代码片段：`<id column="id" property="id"/>`
- 代码片段：`<result column="title" property="title"/>`
- 代码片段：`<result column="name" property="name"/>`
- 代码片段：`<result column="type" property="type"/>`
- 代码片段：`<result column="channel_id" property="channelId"/>`
- 代码片段：`<result column="labels" property="labels"/>`
- 代码片段：`<result column="original_time" property="originalTime"/>`
- 代码片段：`<result column="created_time" property="createdTime"/>`
- 代码片段：`<result column="submitted_time" property="submittedTime"/>`
- 代码片段：`<result column="status" property="status"/>`
- 代码片段：`<result column="publish_time" property="publishTime"/>`
- 代码片段：`<result column="reason" property="reason"/>`
- 代码片段：`<result column="article_id" property="articleId"/>`

画面 6：
- 展示了项目结构，其中 `CNewsMapper.xml` 文件位于 `src/main/resources/mappers/crawlers/` 目录下。

画面 7：
- 展示了 `CNewsMapper.xml` 文件，其中定义了 `selectByIdAndStatus` 方法。
- 代码片段：`<resultMap id="BaseResultMap" type="com.heima.model.crawler.pojos.CNews">`
- 代码片段：`<id column="id" property="id"/>`
- 代码片段：`<result column="title" property="title"/>`
- 代码片段：`<result column="name" property="name"/>`
- 代码片段：`<result column="type" property="type"/>`
- 代码片段：`<result column="channel_id" property="channelId"/>`
- 代码片段：`<result column="labels" property="labels"/>`
- 代码片段：`<result column="original_time" property="originalTime"/>`
- 代码片段：`<result column="created_time" property="createdTime"/>`
- 代码片段：`<result column="submitted_time" property="submittedTime"/>`
- 代码片段：`<result column="status" property="status"/>`
- 代码片段：`<result column="publish_time" property="publishTime"/>`
- 代码片段：`<result column="reason" property="reason"/>`
- 代码片段：`<result column="article_id" property="articleId"/>`

画面 8：
- 展示了 `CrawlerNewsService.java` 文件，其中定义了 `saveNews` 方法。
- 代码片段：`public interface CrawlerNewsService {`
- 代码片段：`public void saveNews(CNews cNews);`

画面 9：
- 展示了 `CrawlerNewsService.java` 文件，其中定义了 `deleteById` 方法。
- 代码片段：`public void deleteById(String url);`

画面 10：
- 展示了 `CrawlerNewsService.java` 文件，其中定义了 `updateNews` 方法。
- 代码片段：`public void updateNews(CNews cNews);`

画面 11：
- 展示了 `CrawlerNewsServiceImpl.java` 文件，其中定义了 `saveNews` 方法。
- 代码片段：`@Service @SuppressWarrings("all") public class CrawlerNewsServiceImpl implements CrawlerNewsService {`
- 代码片段：`@Autowired private CNewsMapper cNewsMapper;`
- 代码片段：`public void saveNews(CNews cNews) { cNewsMapper.insertSelective(cNews); }`

画面 12：
- 展示了 `CrawlerNewsServiceImpl.java` 文件，其中定义了 `updateNews` 方法。
- 代码片段：`@Override public void updateNews(CNews cNews) { cNewsMapper.updateByPrimaryKeySelective(cNews); }`

画面 13：
- 展示了 `CrawlerNewsServiceImpl.java` 文件，其中定义了 `deleteById` 方法。
- 代码片段：`@Override public void deleteById(String url) { cNewsMapper.deleteById(url); }`

画面 14：
- 展示了 `CrawlerNewsServiceImpl.java` 文件，其中定义了 `queryList` 方法。
- 代码片段：`@Override public List<CNews> queryList(CNews cNews) { return cNewsMapper.selectList(cNews); }`

3) 画面里出现的**代码、配置、命令、目录

