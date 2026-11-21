# 画面线理解：10_数据保存准备_爬虫文章完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\10_数据保存准备_爬虫文章完成【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:14, 01:46, 02:14, 02:35, 02:57, 03:10, 03:26, 03:54, 04:32, 05:07, 05:44, 06:09, 06:32, 06:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:06:10

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
- 代码片段：`<mapper namespace="com.heima.model.mappers.crawlers.CNewsMapper">`
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
- 代码片段：`<mapper namespace="com.heima.model.mappers.crawlers.CNewsMapper">`
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
