# 02_图片缓存_需求分析

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\02_图片缓存_需求分析【海量资源尽在 666java.com】.mp4
- 时长 2分34秒（音频 154s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们来去开发咱们咱们这个叫做图片缓存啊那首先呢咱们来看一下这个功能的需求啊说啥呢说是随着热文章的访问越来越频繁文章内的图片频繁的访问的图片服务器对图片服务器造成了很大的压力啊因此决定了把热文章相关的图片缓存到redis咱们之前这个访问图片的时候其实都是去访问当前的什么
[00:30] 目前所缓存的都是什么呢都是这种自媒体发布的文章那这个图片其实是访问的谁啊访问的是咱们的一个叫做FastDFS是吧那这个其实为了减轻当前这个图片负起的压力啊所以说咱们把这个图片啊去保存到哪呢叫缓存到ReadyStorm好那这块其实说做了两块第一个呢咱们要去监听热文章主消息缓存图片功能然后呢咱们要去把这个图片呢去
[00:59] 保存到redis就可以了那首先呢咱们这样啊咱们还是这个思路其实比较清晰了啊咱们之前其实是做过什么呢做过咱们之前的热文章的计算咱们在这啊当时呢是留了留了一个口子可以看一看啊当前的AP hot article Service这里边啊打开好再去计算热文章的数据的时候啊嗯这呢是留了一个东西说缓存文章中的图片信息
[01:30] 那这个图片信息呢现在啊咱们就要做那这时候呢咱们要去发一个消息那为什么要发消息呢因为啊咱们需要在这啊再去创建一个微服务这个微服务呢专门呢是用来做这种或者说咱们要去专门处理咱们的图片的一个微服务好吧那行啊下面呢咱们就来先去发消息那发消息的呢其实呢都是干嘛呢
[01:56] 你就是只需要发什么呢只需要发当前的AP hot articles就是hot当前这个热点文章就可以了因为这里边其实已经包含了什么呢包含了当前的文章的ID你通过文章ID呢就可以去查询文章的内容把内容的图片的换存还有文章的这种封面图片呢咱们也可以进行换存好吧那行那我们下面呢就可以先去做一个这种
[02:23] 微服务的发送啊就是先去发送消息然后呢回过头来之后呢咱们再去真正的去保存或者缓存当前这个图片

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
展示一个名为“heima-leadnews”的项目中，article模块的目录结构，并聚焦于其中的ApplArticleServiceImpl类，讲解其计算热点文章并保存到Redis和数据库的逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在IDEA中打开项目“heima-leadnews”，当前选中模块“heima-leadnews-common”。
画面2：切换到模块“heima-leadnews-article”。
画面3：在“heima-leadnews-article”模块下，展开“src/main/java”目录。
画面4：导航至“com/heima/article”包。
画面5：展开“Service”包，选中“impl”子包。
画面6：在“impl”包下，选中“ApplArticleServiceImpl”类。
画面7：选中“ApplArticleServiceImpl”类，准备查看代码。
画面8：显示“ApplArticleServiceImpl.java”文件内容，代码中包含计算热点文章并保存到Redis和数据库的逻辑。
画面9：代码编辑器中，光标位于“for”循环的结束处。
画面10：代码编辑器中，光标位于“for”循环的结束处，与画面9相同。
画面11：代码编辑器中，光标位于“for”循环的结束处，与画面9、10相同。
画面12：代码编辑器中，光标位于“for”循环的结束处，与画面9、10、11相同。
画面13：在IDEA中，选中“heima-leadnews-article”模块。
画面14：切换到记事本（Notepad++）编辑器，打开“day13_黑马.md”文件，内容为“1 图片缓存开发”章节，其中包含“1.2 article微服务发送消息”小节，提及“maven_test_properties”和“Kafka.properties”配置文件。

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
    Kafka
        Kafka.topic.hot-article=heima.topic.hot.article.single.test
Kafka.properties
    Kafka.topic.hot-article=${Kafka.topic.hot-article}
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
    Kafka
        Kafka.topic.hot-article=heima.topic.hot.article.single.test
Kafka.properties
    Kafka.topic.hot-article=${Kafka.topic.hot-article}

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

