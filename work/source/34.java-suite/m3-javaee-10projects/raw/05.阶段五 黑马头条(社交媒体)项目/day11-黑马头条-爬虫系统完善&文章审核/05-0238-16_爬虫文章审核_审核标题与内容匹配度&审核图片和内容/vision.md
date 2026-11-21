# 画面线理解：16_爬虫文章审核_审核标题与内容匹配度&审核图片和内容

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\16_爬虫文章审核_审核标题与内容匹配度&审核图片和内容【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 02:13, 03:10, 04:20, 05:08, 06:22, 07:21, 08:09, 08:50, 10:40, 11:20, 12:02, 13:20, 14:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:25:23

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
