# 画面线理解：02_图片缓存_需求分析

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\02_图片缓存_需求分析【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:07, 01:09, 01:10, 01:12, 01:13, 01:14, 01:18, 01:19, 01:21, 01:22, 01:24, 01:37, 01:38, 02:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:46:37

1) 这一组画面整体在讲什么（一句话）：
展示一个名为“heima-leadnews”的项目中，article模块的目录结构，并聚焦于其中的ApplArticleServiceImpl类，讲解其计算热点文章并保存到Redis和数据库的逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在IDEA中打开项目“heima-leadnews”，当前选中模块“heima-leadnews-common”。
画面2：切换到模块“heima-leadnews-article”。
画面3：在“heima-leadnews-article”模块下，展开“src/main/java”目录。
画面4：导航至“com/heima/article”包。
画面5：展开“service”包，选中“impl”子包。
画面6：在“impl”包下，选中“ApplArticleServiceImpl”类。
画面7：选中“ApplArticleServiceImpl”类，准备查看代码。
画面8：显示“ApplArticleServiceImpl.java”文件内容，代码中包含计算热点文章并保存到Redis和数据库的逻辑。
画面9：代码编辑器中，光标位于“for”循环的结束处。
画面10：代码编辑器中，光标位于“for”循环的结束处，与画面9相同。
画面11：代码编辑器中，光标位于“for”循环的结束处，与画面9、10相同。
画面12：代码编辑器中，光标位于“for”循环的结束处，与画面9、10、11相同。
画面13：在IDEA中，选中“heima-leadnews-article”模块。
画面14：切换到记事本（Notepad++）编辑器，打开“day13_黑马.md”文件，内容为“1 图片缓存开发”章节，其中包含“1.2 article微服务发送消息”小节，提及“maven_test_properties”和“kafka.properties”配置文件。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面8-12中显示的Java代码：
```java
//查询前一天新发布的文章列表
String lastDay = DateTime.now().minusDays(1).toString("yyyy-MM-dd 00:00:00");
List<Article> articleList = apArticleMapper.loadLastArticleForHot(lastDay);
//计算文章热度（阅读量、评论、点赞、收藏）
List<ApHotArticles> hotArticlesList = computeHotArticle(articleList);
//缓存频道首页到redis
cacheTagRedis(articleList);
//给每一个用户保存一份热点文章
List<ApBehaviorEntry> entryList = apBehaviorEntryMapper.selectAllEntry();
for (ApHotArticles hot : hotArticlesList) {
    //保存热点文章
    apHotArticlesMapper.insert(hot);
    //给每一个用户保存热点数据
    saveHotArticleForEntryList(hot, entryList);
}
//缓存文章中的图片（暂时不做）
```

画面14中显示的Markdown文档内容：
```
1 图片缓存开发
1.1 功能需求
    随着热文章的访问越来越频繁，文章内的图片访问图片服务器，对图片服务器造成了很大的压力，因此决定
    把热文章主流信息缓存图片功能
    不要开发功能包括：
        - 热文章主流信息缓存图片
1.2 article微服务发送消息
1.2.1 定义消息名称 common模块
maven_test_properties
    kafka
        kafka.topic.hot-article=heima.topic.hot.article.single.test
kafka.properties
    kafka.topic.hot-article=${kafka.topic.hot-article}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14中显示的PPT标题和内容：
标题：1 图片缓存开发
子标题：1.1 功能需求
内容：
- 随着热文章的访问越来越频繁，文章内的图片访问图片服务器，对图片服务器造成了很大的压力，因此决定
- 把热文章主流信息缓存图片功能
- 不要开发功能包括：
    - 热文章主流信息缓存图片
子标题：1.2 article微服务发送消息
子子标题：1.2.1 定义消息名称 common模块
内容：
maven_test_properties
    kafka
        kafka.topic.hot-article=heima.topic.hot.article.single.test
kafka.properties
    kafka.topic.hot-article=${kafka.topic.hot-article}

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
