# 07_热文章计算_定时计算_保存热点文章

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\07_热文章计算_定时计算_保存热点文章【海量资源尽在 666java.com】.mp4
- 时长 3分25秒（音频 205s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就继续往下讲啊那这个还有一个没做完啊说给每一个用户保存一份热点文章信息那首先呢在这里边有两个信息需要去注意啊第一个呢是每一个用户啊第二个呢是保存啊保存啊所以说呢咱们这块啊先得去拿到所有的用户然后呢再去保存是吧保存的并且是热点文章所以说啊咱们在这儿先去注注两个mypro
[00:27] 第一个呢是当前的什么appbehaviorentrymap然后第二个呢就是当前的hotprivate然后是apphotarticlesmap是吧好注进来之后呢这时候呢咱们就可以去先去查询每一个用户啊appbehaviorentry.select all这时候拿到的呢就是一个entrylist然后呢然后咱们就可以去循环谁呢
[01:02] 运行当前的hot article list先去保存热点文章保存热点文章怎么办呢?
[01:15] 这时候就比较容易了AP hot articles.mypro.insert用的是保存hot就可以第二个要去每一个用户
[01:34] 每一个用户保存前的什么热点数据热点数据这个怎么办呢我们在这再去工装一个方法叫fill hot article然后是for什么呢for entry trylist第一个参数就是hot第二个参数就是entry list这个方法没有是吧没有的话咱们就再去创建一下咱们在这就写完了在这好
[02:09] 这个咱们的后期会再做啊咱们就完成前的一个方法这个方法就比较容易了啊每一个用户保存一份热点文章数据啊这个咱们怎么做呀首先呢你要去循环谁呀循环当前的什么entrylist.for然后呢然后的话就是当前的什么out.setEntryID然后你把前那个什么
[02:41] 给它entry吧好吧entry啊entry.getid这样关联起来了啊最终呢你再去保存当前这个文章的数据就可以了啊点没有一个insert然后是保存hot那这样的话咱们这个给每一个用户去保存了一份热点数据好吧那行那到此为止呢这个类啊咱们就写完了啊写完了当然这个刚才说了啊这块内容呢咱们到后期呢还会再去完善再去完善啊
[03:11] 就是去完善当前的图片信息到时候呢咱们会去抽出来一个这种专门用于处理图片的一个微服务啊再去做好吧那这个啊咱们就先说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 IntelliJ IDEA 中编写并完善一个计算热点文章的 Java 服务类，涉及注入多个 Mapper、查询数据、缓存处理以及保存热点文章和用户行为记录。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 代码：在 `ApiHotArticleService` 类中，`computeHotArticle` 方法内，调用 `apArticleMapper.loadLastArticleForHot` 获取文章列表，然后调用 `computeHotArticle` 计算热点文章，并将结果缓存到 Redis。
- 代码：`cacheTagAggRedis(articleList);`
- 代码：`apBehaviorEntryMapper.selectEntry();`
- 代码：`apHotArticlesMapper.insert();`
- 代码：`saveHotArticleForEntryList();`

画面 2：
- 代码：在 `computeHotArticle` 方法中，添加了 `apBehaviorEntryMapper` 的注入。
- 代码：`private ApBehaviorEntryMapper apBehaviorEntryMapper;`

画面 3：
- 代码：在 `computeHotArticle` 方法中，添加了 `apHotArticlesMapper` 的注入。
- 代码：`private ApHotArticlesMapper apHotArticlesMapper;`

画面 4：
- 代码：在 `computeHotArticle` 方法中，添加了 `apBehaviorEntryMapper` 的注入。
- 代码：`private ApBehaviorEntryMapper apBehaviorEntryMapper;`

画面 5：
- 代码：在 `computeHotArticle` 方法中，添加了 `apHotArticlesMapper` 的注入。
- 代码：`private ApHotArticlesMapper apHotArticlesMapper;`

画面 6：
- 代码：在 `computeHotArticle` 方法中，添加了 `apBehaviorEntryMapper` 的注入。
- 代码：`private ApBehaviorEntryMapper apBehaviorEntryMapper;`

画面 7：
- 代码：在 `computeHotArticle` 方法中，添加了 `apBehaviorEntryMapper` 的注入。
- 代码：`private ApBehaviorEntryMapper apBehaviorEntryMapper;`

画面 8：
- 代码：在 `computeHotArticle` 方法中，添加了 `apBehaviorEntryMapper` 的注入。
- 代码：`private ApBehaviorEntryMapper apBehaviorEntryMapper;`

画面 9：
- 代码：在 `computeHotArticle` 方法中，添加了 `apBehaviorEntryMapper` 的注入。
- 代码：`private ApBehaviorEntryMapper apBehaviorEntryMapper;`

画面 10：
- 代码：在 `computeHotArticle` 方法中，添加了 `apBehaviorEntryMapper` 的注入。
- 代码：`private ApBehaviorEntryMapper apBehaviorEntryMapper;`

画面 11：
- 代码：在 `computeHotArticle` 方法中，添加了 `apBehaviorEntryMapper` 的注入。
- 代码：`private ApBehaviorEntryMapper apBehaviorEntryMapper;`

画面 12：
- 代码：在 `computeHotArticle` 方法中，添加了 `apBehaviorEntryMapper` 的注入。
- 代码：`private ApBehaviorEntryMapper apBehaviorEntryMapper;`

画面 13：
- 代码：在 `computeHotArticle` 方法中，添加了 `apBehaviorEntryMapper` 的注入。
- 代码：`private ApBehaviorEntryMapper apBehaviorEntryMapper;`

画面 14：
- 代码：在 `computeHotArticle` 方法中，添加了 `apBehaviorEntryMapper` 的注入。
- 代码：`private ApBehaviorEntryMapper apBehaviorEntryMapper;`

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无

