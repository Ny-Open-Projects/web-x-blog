# 14_爬虫数据解析保存_思路分析

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\14_爬虫数据解析保存_思路分析【海量资源尽在 666java.com】.mp4
- 时长 3分9秒（音频 189s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们进入下面这个阶段就叫解析的模块啊解析模块那解析啥呢就这个呢是咱们最后的一个小模块啊那这模块呢其实也是爬虫里边最后一个阶段叫people in是吧那这个呢主要是来保存数据啊当然了先去解析再去保存我这边呢是画一张图啊大概去说一说咱们要执行的一个思路啊
[00:25] 首先呢咱们要获取目标页数据那这个目标页呢就是你比如说啊找到某一个用户然后是咱们是爬举了某一条文章咱们是不是这个解析的规则是不是已经做完了是吧咱们已经获取到这个内容了啊但这个内容的器权呢有可能的会不是咱们真正要保存的内容那这份内容呢咱们要去专门的去设置一下好那这是一个啊然后再往下看啊
[00:54] 咱们回去判断啊回去判断到底是正向还是逆向如果说是正向的话啊咱们又再说逆向啊如果是正向的话呢咱们需要去解析刚才说了因为你爬取的文章有可能呢跟你保存的时候这个格式可能不太一样咱们需要去处理一下这个格式就去解析好这是一个一大块啊然后继续往下看然后解析完之后如果说这数据啊咱们都没问题那这时候呢咱们就可以保存了保存的表呢
[01:21] 其实就是当前的CL News然后保存它之后呢咱们要干嘛呢保存它之后啊咱们要去保存咱们的这种附加信息还有咱们的评论信息还有咱们的评论啊评论评论干啥呢你可以找一下啊CL开头的咱们的评论信息对吧假如说这三个都保存了呢咱们最后啊还有一个就是有一个叫做
[01:51] 发送消息审核文章咱们用的是卡不卡然后最终的是发送一条消息让这条文章去进行审核那审核通过之后呢这个呢就能干嘛呢就能真正的去让用户去展示了好吧这就是正向的一个整体的流程啊咱们细节有很多咱们一会儿还会再去讲假如说这块啊嗯是不是正向是反向的那反向的话呢咱们上次也聊过这个反向这个
[02:19] 这个概念啊反向的意思呢其实呢就是要干嘛其实呢就是咱们要去更新已经爬取的文章的一些数据比如说之前的文章啊已经爬下来了咱们现在要更新当前文章的一些数据更新哪些呢主要是更新的是转发量是吧评论量点赞量点赞量啊像等等像这些数据呢咱们要重新去更新一下那更新的表呢或者操作的表呢就是一张表就是这样
[02:47] 就是当前的这个SR News就是当前的附加信息表图文的附加信息表好吧那这个这是一个整体的思路大家一定要把这个思路给捋清这个代码可能会有点多好吧那这个思路咱们就先说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个新闻爬虫系统的解析模块实现，包括HTML样式处理、页面结构分析、数据库表结构设计及数据存储流程。

2) 按时间顺序列出每张画面的要点：
画面1：展示爬虫系统中CrawlerHtmlParsePipeline类的Java代码，用于处理HTML解析管道，包含资源文件读取和依赖注入的配置。
画面2：展示HtmlStyle类的Java代码，用于管理样式映射，包含addStyle和getStyle方法。
画面3：展示CSDN网站的Java技术文章列表页面。
画面4：展示CSDN博客文章页面的空白状态。
画面5：展示CSDN博客文章页面的HTML源代码，包含meta标签和脚本引用。
画面6：展示爬虫系统数据处理流程图，包含“获取已爬取链接”、“是否正则”、“解析数据”、“保存文章”、“保存评论信息”、“保存评论”等步骤。
画面7：展示CSDN博客文章页面的HTML源代码，包含div标签和class属性。
画面8：展示Navicat for MySQL中“d_news_additional”表的数据，包含新闻ID、URL、阅读数、点赞数等字段。
画面9：展示Navicat for MySQL中“d_news”表的DDL创建语句，包含字段定义和主键约束。
画面10：展示Navicat for MySQL中“d_news_comments”表的DDL创建语句，包含字段定义和主键约束。
画面11：展示爬虫系统数据处理流程图，包含“获取已爬取链接”、“是否正则”、“解析数据”、“保存文章”、“保存评论信息”、“保存评论”等步骤。
画面12：展示Navicat for MySQL中“d_news_comments”表的DDL创建语句，包含字段定义和主键约束。
画面13：展示爬虫系统数据处理流程图，包含“获取已爬取链接”、“是否正则”、“解析数据”、“保存文章”、“保存评论信息”、“保存评论”等步骤。
画面14：展示爬虫系统数据处理流程图，包含“获取已爬取链接”、“是否正则”、“解析数据”、“保存文章”、“保存评论信息”、“保存评论”等步骤。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
@Component
public class CrawlerHtmlParsePipeline extends AbstractHtmlParsePipeline<CrawlerParserItem> {
    private static final ResourceBundle resourceBundle =
            ResourceBundle.getBundle("config");
    private static final String cdn_comment_url =
            resourceBundle.getString("cdn.comment.url");

    // 下次更新时间
    private static final String[] next_update_hour_array =
            resourceBundle.getString("crawler.nextupdatehour").split(",");

    @Autowired
    private KafkaSender kafkaSender;
    @Autowired
    private CrawlerNewsService crawlerNewsService;
    @Autowired
    private CrawlerNewsCommentService cNewsCommentService;
```

画面2：
```java
public class HtmlStyle {
    private Map<String, String> styleMap = new HashMap<>();

    public void addStyle(String key, String value) {
        styleMap.put(key, value);
    }

    public void addStyle(Map<String, String> map) {
        styleMap.putAll(map);
    }

    public String getCssStyle() {
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<String, String> entry : styleMap.entrySet()) {
            sb.append(entry.getKey()).append(":").append(entry.getValue()).append(";");
        }
        return StringUtils.remove(sb.toString(), ";");
    }

    public Map<String, String> getStyleMap() {
        return styleMap;
    }
}
```

画面9：
```sql
CREATE TABLE `d_news` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `task_id` int(11) DEFAULT NULL COMMENT '任务ID',
  `news_id` int(11) DEFAULT NULL COMMENT '新闻ID',
  `url` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '新闻链接',
  `title` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '新闻标题',
  `content` text COLLATE utf8mb4_unicode_ci COMMENT '新闻内容',
  `type` int(11) DEFAULT NULL COMMENT '文章类型',
  `created_time` datetime DEFAULT NULL COMMENT '创建时间',
  `updated_time` datetime DEFAULT NULL COMMENT '更新时间',
  `status` tinyint(4) DEFAULT NULL COMMENT '状态',
  `source` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '来源',
  `author` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '作者',
  `tags` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '标签',
  `read_count` int(11) DEFAULT NULL COMMENT '阅读数',
  `like_count` int(11) DEFAULT NULL COMMENT '点赞数',
  `comment_count` int(11) DEFAULT NULL COMMENT '评论数',
  `forward_count` int(11) DEFAULT NULL COMMENT '转发数',
  `unlike_count` int(11) DEFAULT NULL COMMENT '踩数',
  `is_deleted` tinyint(4) DEFAULT NULL COMMENT '是否删除',
  `is_spam` tinyint(4) DEFAULT NULL COMMENT '是否垃圾',
  `is_top` tinyint(4) DEFAULT NULL COMMENT '是否置顶',
  `is_recommend` tinyint(4) DEFAULT NULL COMMENT '是否推荐',
  `is_hot` tinyint(4) DEFAULT NULL COMMENT '是否热门',
  `is_new` tinyint(4) DEFAULT NULL COMMENT '是否新',
  `is_valid` tinyint(4) DEFAULT NULL COMMENT '是否有效',
  `is_locked` tinyint(4) DEFAULT NULL COMMENT '是否锁定',
  `is_hidden` tinyint(4) DEFAULT NULL COMMENT '是否隐藏',
  `is_archived` tinyint(4) DEFAULT NULL COMMENT '是否归档',
  `is_published` tinyint(4) DEFAULT NULL COMMENT '是否发布',
  `is_draft` tinyint(4) DEFAULT NULL COMMENT '是否草稿',
  `is_pending` tinyint(4) DEFAULT NULL COMMENT '是否待审核',
  `is_approved` tinyint(4) DEFAULT NULL COMMENT '是否已审核',
  `is_rejected` tinyint(4) DEFAULT NULL COMMENT '是否已拒绝',
  `is_withdrawn` tinyint(4) DEFAULT NULL COMMENT '是否已撤回',
  `is_deleted_by_admin` tinyint(4) DEFAULT NULL COMMENT '是否被管理员删除',
  `is_deleted_by_user` tinyint(4) DEFAULT NULL COMMENT '是否被用户删除',
  `is_deleted_by_system` tinyint(4) DEFAULT NULL COMMENT '是否被系统删除',
  `is_deleted_by_other` tinyint(4) DEFAULT NULL COMMENT '是否被其他用户删除',
  `is_deleted_by_reason` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除原因',
  `is_deleted_by_time` datetime DEFAULT NULL COMMENT '删除时间',
  `is_deleted_by_user_id` int(11) DEFAULT NULL COMMENT '删除用户ID',
  `is_deleted_by_user_name` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除用户名',
  `is_deleted_by_user_ip` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除用户IP',
  `is_deleted_by_user_agent` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除用户代理',
  `is_deleted_by_user_browser` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除用户浏览器',
  `is_deleted_by_user_os` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除用户操作系统',
  `is_deleted_by_user_language` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除用户语言',
  `is_deleted_by_user_location` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除用户位置',
  `is_deleted_by_user_timezone` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除用户时区',
  `is_deleted_by_user_country` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除用户国家',
  `is_deleted_by_user_region` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除用户地区',
  `is_deleted_by_user_city` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除用户城市',
  `is_deleted_by_user_district` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除用户区县',
  `is_deleted_by_user_street` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除用户街道',
  `is_deleted_by_user_building` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除用户建筑',
  `is_deleted_by_user_room` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL

