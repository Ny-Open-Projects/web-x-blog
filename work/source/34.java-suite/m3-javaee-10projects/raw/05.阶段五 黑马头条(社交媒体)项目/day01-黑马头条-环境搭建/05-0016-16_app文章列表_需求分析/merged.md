# 16_app文章列表_需求分析

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\16_app文章列表_需求分析【海量资源尽在 666java.com】.mp4
- 时长 4分48秒（音频 288s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好各位下面呢咱们来进入APP端文章列表后端的开发然后首先呢咱们第一个模块呢是文章列表的展示啊咱们目前呢咱们这个本项目呢是一个啊这种移动端的项目所以说呢咱们需要在手机上去展示文章的列表信息那这文章列表啊咱们只需要在后台去提供接口就可以啊只要把文章信息展返给前台就行目前咱们需要做这个工作
[00:28] 那这里边咱们需要去分析一下需求啊那展示的话其实分几种情况那咱们呢主要是来看下面这个图来简单说一说啊首先呢当某一个用户啊用户登进来之后啊当然或者是有不登的情况啊咱们可以先说登录他登录进来之后呢咱们首先要加载的是当前用户推荐的文章推荐OK那里边有推荐啊这样的话呢推荐文章之后呢咱们就可以去展示用户推荐的一些文章列表
[00:58] 好那如果说用户未登录的话呢咱们会去加载默认的文章那边咱们会有一些规则是吧默认的文章那边那行啊这是登录或不登录的情况下当然还有呢用户还有一些行为比如说有一个下拉刷新和上拉刷新那下拉刷新呢就是加载当前时间之后当前时间之后发布的文章OK那其实呢就是最新的文章对吧这还有一个上拉刷新
[01:28] 上两刷新的话就是加载当前时间什么之前的发布的文章也就是说咱们需要去加载更多的文章那好啊那这就是当前的一个需求那这里边特别注意一个事就是这里边啊有一个隐藏的需求这个需求呢就是需要去记录当前用户的行为
[01:51] 因为呢咱们要去记录这个行为之后呢就可以到后期能够更方便的给用户去推荐一些热点的文章那好那这个呢就是咱们的一些需求然后下面还有一些表啊这目前的话呢涉及到了四张表咱们可以简单看一眼啊首先呢是有一个叫AP article那这个表啊是咱们从始至终都会
[02:16] 用到的一张表这个表应该是咱们目前来说应该是最重要的一张表就是文章信息表那这个表的字段也比较多那分别咱们来看一眼啊首先的是主见主见的是一个十一位的字增是吧还有标题文章的标题还有文章的作者是吧作者的昵称OK那这都很好理解啊还有是文章所属哪个频道那这个频道的话实际上啊这两个话都是啊频道的话比如说当前文章属于
[02:45] 加入类或者说属于PHP类属于大数据等等这个就是频道的名称下面还有些布局布局的话就是无图是零一是单图二是多图下面还有些文章标记标记普通文章热点文章置顶文章还有什么大V文章还有精品文章是吧入书这样才能用户当前这个文章转发点点击
[03:09] 量比较高的时候呢咱们有可能会把它设置为精品文章也有可能设置为大V文章好下面还有一些啊就是文章的图片图片的话咱们需要去用逗号分割还有就是文章的标签呢咱们最多是可以设置三个也是逗号分割的啊下面还有一些数量啊就是点赞收藏评论阅读的数量咱们也会去更新
[03:33] 下面还有一个省市区那省市区的话呢咱们主要是为了能够进行在设备上去这种查询的时候方便根据条件查询的时候设置的这省市区还有三个还有这几个创建时间发布时间还有状态还有来源行那关于这个来源的话咱们后期还会再去说这里边主要是两个一个是吗一个是当前的自媒体人是吧另外一个是爬虫
[03:59] 好下面还有一个文章下面是APP用户文章那边这个是给用户推荐的时候用的这里边主要是关注两个字段第一个是当前用户的ID第二个是article ID也就是说当前用户跟这个文章是有关联的咱们也可以用户登录之后可以根据当前用户去查询他所推荐的文章OK
[04:26] 然后下面还有一些行为啊那这个呢主要就是记录比如说用户去点击了某一些文章咱们可以用这两个表去记录当前用户的行为那好那这四段呢大家可以看一眼咱们去讲到具体需求的时候咱们可以再具体去说好吧行那这个需求跟表分析呢咱们就说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解一个文章列表功能的数据库表结构设计，包括文章信息表、用户文章列表表、文章行为表等，并分析其字段含义和类型。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文章首页的用户行为流程图，包括用户登录状态、加载文章列表、用户行为追踪等逻辑。
画面2：展示文章首页的用户行为流程图，包括用户登录状态、加载文章列表、用户行为追踪等逻辑。
画面3：展示文章首页的用户行为流程图，包括用户登录状态、加载文章列表、用户行为追踪等逻辑。
画面4：展示“ap_article文章信息表”的字段结构，包括id、title、author_id、channel_id、layout、flag、images、labels、likes、collection、comment、views、province_id、city_id、county_id、created_time、publish_time、sync_status、origin等字段及其类型和说明。
画面5：展示“ap_article文章信息表”的字段结构，包括id、title、author_id、channel_id、layout、flag、images、labels、likes、collection、comment、views、province_id、city_id、county_id、created_time、publish_time、sync_status、origin等字段及其类型和说明。
画面6：展示“ap_user_article_list APP用户文章列表”的字段结构，包括id、user_id、channel_id、article_id、is_show、recommend_time、is_read、strategy_id等字段及其类型和说明。
画面7：展示“ap_article文章信息表”的字段结构，包括id、title、author_id、channel_id、layout、flag、images、labels、likes、collection、comment、views、province_id、city_id、county_id、created_time、publish_time、sync_status、origin等字段及其类型和说明。
画面8：展示“ap_article文章信息表”的字段结构，包括id、title、author_id、channel_id、layout、flag、images、labels、likes、collection、comment、views、province_id、city_id、county_id、created_time、publish_time、sync_status、origin等字段及其类型和说明。
画面9：展示“ap_article文章信息表”的字段结构，包括id、title、author_id、channel_id、layout、flag、images、labels、likes、collection、comment、views、province_id、city_id、county_id、created_time、publish_time、sync_status、origin等字段及其类型和说明。
画面10：展示“ap_user_article_list APP用户文章列表”的字段结构，包括id、user_id、channel_id、article_id、is_show、recommend_time、is_read、strategy_id等字段及其类型和说明。
画面11：展示“ap_show_behaviorAPP文章展现行为表”的字段结构，包括id、entry_id、article_id、is_click、show_time、created_time等字段及其类型和说明。
画面12：展示“ap_behavior_entry app行为实体表”的字段结构，包括id、type、entry_id、created_time、burst等字段及其类型和说明。
画面13：展示“ap_behavior_entry app行为实体表”的字段结构，包括id、type、entry_id、created_time、burst等字段及其类型和说明。
画面14：展示“7.2 文章列表相关接口定义”的标题，以及“ap_behavior_entry app行为实体表”的字段结构，包括id、type、entry_id、created_time、burst等字段及其类型和说明。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
架构图/流程图：
- 用户 → 加载默认的频道数据 → 未登录，加载默认的文章列表 → 登录后，加载推荐的文章列表 → 用户设置的频道进行加载 → 用户行为追踪 → 推荐请求，记录用户行为
表格数据：
- “ap_article文章信息表”：
  | 字段名称 | 类型 | 说明 |
  | --- | --- | --- |
  | id | int(11) | 主键 |
  | title | varchar(50) | 标题 |
  | author_id | int(11) | 文章作者的ID |
  | author_name | varchar(20) | 作者昵称 |
  | channel_id | int(10) | 文章所属频道ID |
  | channel_name | varchar(10) | 频道名称 |
  | layout | tinyint(1) | 文章布局 0 无图文章 1 单图文章 2 多图文章 3 |
  | flag | tinyint(3) | 文章标记 0 普通文章 1 热点文章 2 首页文章 3 大V文章 |
  | images | varchar(1000) | 文章图片 多张逗号分隔 |
  | labels | varchar(500) | 文章标签最多3个 逗号分隔 |
  | likes | int(5) | 点赞数量 |
  | collection | int(5) | 收藏数量 |
  | comment | int(5) | 评论数量 |
  | views | int(5) | 阅读数量 |
  | province_id | int(11) | 省市 |
  | city_id | int(11) | 市区 |
  | county_id | int(11) | 区县 |
  | created_time | datetime | 创建时间 |
  | publish_time | datetime | 发布时间 |
  | sync_status | tinyint(1) | 同步状态 |
  | origin | tinyint(1) | 来源 |
- “ap_user_article_list APP用户文章列表”：
  | 字段名称 | 类型 | 说明 |
  | --- | --- | --- |
  | id | int(11) | 主键 |
  | user_id | int(11) | 用户ID |
  | channel_id | int(11) | 频道ID |
  | article_id | int(11) | 文章ID |
  | is_show | tinyint(1) | 是否展示 |
  | recommend_time | datetime | 推荐时间 |
  | is_read | tinyint(1) | 是否阅读 |
  | strategy_id | int(5) | 推荐算法 |
- “ap_show_behaviorAPP文章展现行为表”：
  | 字段 | 类型 | 描述 |
  | --- | --- | --- |
  | id | int(11) | 主键 |
  | entry_id | int(11) | 实体ID |
  | article_id | int(11) | 文章ID |
  | is_click | tinyint(1) | 是否点击 |
  | show_time | datetime | 文章加载时间 |
  | created_time | datetime | 登录时间 |
- “ap_behavior_entry app行为实体表”：
  | 字段 | 类型 | 描述 |
  | --- | --- | --- |
  | id | int(11) | 主键 |
  | type | tinyint(1) | 实体类型 0终端设备 1用户 |
  | entry_id | int(11) | 实体ID |
  | created_time | datetime | 创建时间 |
  | burst | varchar(40) | 分片 |

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

