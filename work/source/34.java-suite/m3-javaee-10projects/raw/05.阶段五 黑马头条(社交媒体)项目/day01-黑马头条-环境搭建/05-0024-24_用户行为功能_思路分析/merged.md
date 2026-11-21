# 24_用户行为功能_思路分析

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\24_用户行为功能_思路分析【海量资源尽在 666java.com】.mp4
- 时长 5分59秒（音频 359s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好各位下面呢咱们来去说一下这个隐藏的需求咱们之前呢在讲那个当前接口定义的时候咱们就说了需求分析的时候咱们就说过这里边是有一个隐藏的行为就是说咱们要去记录当前用户的点击行为点击行为咱们下面就来去重新的去分析一下这个思路主要的是来看这个图OK
[00:28] 首先呢当用户去查看文章的时候呢咱们的会定时在前端啊他定时会往后台去传一些数据那这数据就包括了第一个是设备ID第二个是文章的列表一个设备ID一个是文章的列表大家注意听好下面呢咱们是在有一个业务的判断逻辑然后最终的是要保存当前的用户的行为首先呢咱们先判断啊
[00:58] 先判断当前用户能先去查看或者获取当前的用户信息然后呢是获取设备ID那设备ID看他说了设备ID就是从前台传递过来的问题然后呢然后咱们要根据当前用户ID用户的设备ID和用户信息呢去查询行为实体这里边说了一个字啊叫货因为为什么叫货呢因为啊用户信息有可能没有登录但是呢它必须有啥呢有设备ID
[01:28] 当然如果说以登录的用户呢咱们可以没有设备ID所以说呢这两个必须有一个所以说是叫货这时候呢就去查询了一个叫行为实体那行为实体是啥呢其实也是在咱们系统中去对应了一张表数据那下面呢就有一句描述咱们来看一看啊主要是保存了用户ID和用户的设备ID
[01:57] 那这上个白底大家一定要重新理解一下现在咱们是讲的移动端的项目是吧所以说咱们要去获取一个什么手机的编号信息那这个大家不用担心这个一般都是从前端或者从安卓或是iOS获取到之后传递到后端的OK那这个有一个叫手机的编号唯一编号信息这个一定要知道那行那咱们也可以查看一下这个表这个表的话就是这个表叫
[02:26] AP BEHIND ENTRY是吧那这里边啊字段非常简单有几个字段他们需要知道啊第一个是type用户当前那个保存当前那个实体的时候到底是终端的设备还是你登录的用户还有就是实体的ID那这个实体的ID的话是这样如果说你是终端用户的话肯定是有什么当前的什么实体的ID的对吧如果说你要是用户ID的话那这块就是一个用户的ID
[02:56] 这边有个类型的判断大家一定要注意看下面还有一个创建时间那关于分片的话咱们暂时涉及不到OK咱们主要是看这两个字段就可以了第一个呢就是它到底是终端设备还是一个用户要不然就是它要去保存它自己的一个实体的ID好那这个咱们就说明白了那为什么要去设立一个终端设备呢那不只是设立用户不就行了吗因为有的时候
[03:24] 用户没有登录我也要给他推荐根据他的设备号进行推荐这个能听明白吗?
[03:33] 那这个说完之后啊咱们接着往下看啊这里边还有一个是吧第三步是获取传递过来的文章ID列表那这个文章ID列表是已经存在了啊然后第四步是根据文章ID列表和和什么设备ID查询APP行为
[03:57] 二群一个是叫APP文章展现行为表APP文章展现行为表这个表有吗有就是当前的有一个叫做打开AP show behavior这里边其实也记录了一些东西咱们也可以来分析一下这个字段首先呢ID就没啥可说的是吧然后下面是一个entry ID这个是实体ID那这个实体ID对应的是当前的当前这个的
[04:27] ID值好然后再往下看啊这里边是有一个文章的ID他需要去记录某一条文章的ID信息然后是是否点击咱们要去设置一个0或者是10就是点击1是未点击然后下面还有一个就是呃收这个收的话呢就是收time呢就是文章加载的时间咱们要去记录下当前的时间而登录时间咱们也会去创建那个当前的时间就可以好吧
[04:56] 那这个表咱们也说完了那说完之后咱们再回到讲习上再去看一下判断判断啥呢判断传递过来的传递过来的文章ID如果在表中已经存在则删除那什么意思呢说啊现在咱们首先是要基于当前的文章ID去查如果说这里边能查到的话咱们就在哪啊
[05:27] 就在当前的Article.ids里边就把它给删了那为什么要删了呢大家想一想那你说保存过一次还用再重新保存吗一个文章ID是不是不需要吧所以说呢咱们要过滤掉过滤掉已经存在的ID然后呢剩下的ID咱们再重新保存到当前的文章展现行为表中就可以好那这个呢就是一个整体的逻辑那咱们下面呢
[05:56] 就用代码来实现一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解文章列表功能开发中的行为相关功能，包括用户行为数据表结构设计、DTO类定义及数据库建表语句。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示IDE中ArticleTest测试类代码，用于测试加载文章功能，调用apparticleService.load方法。
画面2：展示“ap_article文章信息表”的字段结构，包括id、title、author_id、author_name、channel_name、layout、flag、images等字段及其类型和说明。
画面3：展示用户行为数据表的流程图，包括“收藏文章”、“点赞文章”、“评论文章”等行为，以及“用户行为”和“文章”之间的关系。
画面4：展示“行为相关功能开发”的思维分析图，包括“保存查看文章行为”、“用户行为”、“文章”等节点。
画面5：展示“行为相关功能开发”的思维分析图，包括“保存查看文章行为”、“用户行为”、“文章”等节点。
画面6：展示“行为相关功能开发”的思维分析图，包括“保存查看文章行为”、“用户行为”、“文章”等节点。
画面7：展示“行为相关功能开发”的思维分析图，包括“保存查看文章行为”、“用户行为”、“文章”等节点。
画面8：展示“行为相关功能开发”的思维分析图，包括“保存查看文章行为”、“用户行为”、“文章”等节点。
画面9：展示Navicat for MySQL中“ap_show_behavior”表的建表语句，包含字段定义和主键约束。
画面10：展示Navicat for MySQL中“ap_behavior_entry”表的建表语句，包含字段定义和主键约束。
画面11：展示Navicat for MySQL中“ap_show_behavior”表的建表语句，包含字段定义和主键约束。
画面12：展示Navicat for MySQL中“ap_show_behavior”表的建表语句，包含字段定义和主键约束。
画面13：展示Navicat for MySQL中“ap_show_behavior”表的建表语句，包含字段定义和主键约束。
画面14：展示“行为相关功能开发”的思维分析图，包括“保存查看文章行为”、“用户行为”、“文章”等节点。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1代码：
```java
public class ArticleTest {
    @Autowired
    private AppArticlesService apparticleService;

    @Test
    void testLoad() {
        ApUser apuser = new ApUser();
        apuser.setId(1);
        AppThreadLocalUtils.setUser(apuser);
        ArticleHomeDto dto = new ArticleHomeDto();
        ResponseResult data = apparticleService.load(ArticleConstants.LOADTYPE_LOAD_MORE,
                dto);
        System.out.println(data.getData());
    }
}
```

画面2表结构：
```text
相关表结构分析
ap_article文章信息表
文章信息，存储已发布的文章
字段名称    类型    说明
id          int(11) 主键
title       varchar(50) 标题
author_id   int(11) 文章作者的ID
author_name varchar(20) 作者昵称
channel_name varchar(10) 频道名称
layout      tinyint(3) 文章布局 0 无图文 1 单图文 2 多图文
flag        tinyint(3) 文章标记 0 普通文章 1 热点文章 2 置顶文章
images      varchar(1000) 文章图片 4 大图多分组
```

画面4-8代码：
```java
import helma.leadnews.behavior.dto.ShowBehaviorDto;

public class ShowBehaviorDto {
    // 设备ID
    @TdEncrypt
    Integer equipmentId;
    List<Article> articleIds;
}
```

画面9 SQL：
```sql
CREATE TABLE `ap_show_behavior` (
  `id` int(11) unsigned NOT NULL COMMENT '实体ID',
  `entry_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
  `article_title` varchar(255) DEFAULT NULL COMMENT '文章标题',
  `show_time` datetime DEFAULT NULL COMMENT '文章显示时间',
  `created_time` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`),
  KEY `idx_entry_id` (`entry_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC COMMENT='文章显示行为';
```

画面10 SQL：
```sql
CREATE TABLE `ap_behavior_entry` (
  `id` int(11) unsigned DEFAULT NULL COMMENT '主键',
  `type` tinyint(3) unsigned DEFAULT NULL COMMENT '实体类型',
  `entry_id` int(11) unsigned DEFAULT NULL COMMENT '实体ID',
  `created_time` datetime DEFAULT NULL COMMENT '创建时间',
  `biz` varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '分片',
  PRIMARY KEY (`id`),
  KEY `idx_entry_id` (`entry_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC COMMENT='行为实体表，一个行为实体可被多个用户行为引用';
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3流程图：
- “收藏文章” → “用户行为”
- “点赞文章” → “用户行为”
- “评论文章” → “用户行为”
- “用户行为” → “文章”

画面4-8思维分析图：
- “保存查看文章行为” → “参数”（包含：Integer equipmentId, List<Article> articleIds）
- “参数” → “行为实体”（描述：主要是保存了用户对文章的浏览行为，不包含用户对文章的点赞、收藏、评论等行为）

画面9-13表格数据：
- 表格标题：“ap_show_behavior”表结构
- 字段：id, entry_id, article_title, show_time, created_time
- 主键：id
- 索引：idx_entry_id (entry_id)

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

