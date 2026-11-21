# 12_自媒体文章管理_发布文章需求分析

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\12_自媒体文章管理_发布文章需求分析【海量资源尽在 666java.com】.mp4
- 时长 7分23秒（音频 443s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们来去开发文章管理功能啊咱们先来看第一个功能就是文章发布还有什么保存草稿啊这个后台管理快开发那这个啊这个打开页面里边其实咱们可以简单你说一说啊呃在内容管理这一块呢有一个发布文章那发布文章呢你看你可以填一些内容其实就是一些表单是吧比如说标题标签频道定时这定时的话其实就是一个什么呢就是呃就是一个时间是吧还有什么
[00:30] 内容内容啊这内容的话就比较多咱们一会再说啊然后还有封面封面到底是单图三图还是无图的当然你也可以设置为自动然后呢你可以去有两个操作啊第一个是提交审核就是保存然后第二个是存入草稿当前的文章流程啊是先要去保存完之后啊需要去审核审核完之后啊你才能去真正的发布当前的文章
[00:57] 那这个界面能够看简单的看得出来这里边咱们需要哪些参数咱们下面就来去看一下当前的什么当前的这个接口定义这个接口的话咱们还是有两个这种URL第一个是submit第二个就是其实还是submit只是参数不太一样咱们一会儿会再去设置
[01:22] 但是咱们一会也会改一改一会去改一下就可以下面的简易里边URL已经定义好了咱们也可以参考下面的URL下面的简易再去设置自己的URL好吧然后下面还有一个就是请求的DTO这个DTO的话咱们可以打开看一眼把这个关掉好打开它这里边你看就有什么ID就有title你的标题是吧还有你的频道ID
[01:50] 还有你的label级别是吧还有你的发布时间内容类型这类型简单说一说啊这类型的话你可以打开当前这个WM News啊类型的话就分为0是无图1是单图2是多图20多图啊你可以根据不同的类型去设置不同的数字好吧然后呢再往上看啊然后还有就是提交的时间是吧还有一个状态这个状态是这样啊打开打开它在那边
[02:20] 这状态的话呢咱们一开始的话呢就是一一就是提交待审核的状态如果说你要是草稿的话就是零目前的话咱们就涉及到这两个状态啊提交的时候咱们再说好吧目前的话就是零或者一你提你草稿就是零提交的后提交的保存那就是一好吧然后再往下看啊这还有一个race那这啥意思啊来看一看啊就是拒绝的理由
[02:48] 具体的理由目前的话其实咱们并没有这个东西这个东西咱们现在放着就可以了咱们不设置它就没事还有一个是图片这图片大家一定要注意图片一共是包含两部分内容第一部分内容就是当前这有一个隐秘之私这个其实就是一样就是当前的你可以理解为封面的图片比如说当前某一个文章的封面图片这个封面图片其实就在这
[03:18] 在这啊在这就上传的当然还有另外一块就是当前文章内容里边啊其实他也有图片比如说你看你说一段话然后插了一个图然后再说一段话又插入了另外一张图这内容里边他也有图片这个图片咱们一会儿会去重点去说好吧那行啊那这个东西啊咱们就刚才大概去说了一下啊你要理解一下当前的参数是啥意思才行然后咱们再往下看啊
[03:47] 然后最终返回的时候你直接想一个success就完事了非常简单大概里边还有一个就是channel这个channel简单说一说这个channel的话其实就是在这这有一个频道这个频道的话你不应该输入应该是从表中去查这表其实打开哪个表就是打开当前的ad它是在ad中叫admin中去维护的adchannel可以找找adminchannel没有吗
[04:20] 好来看一看啊啊这呢啊adkino这就这东西啊你目前的话呢这个咱们是有那么多数据当然你也可以手动去加好吧有的有有加了有吧有view是吧还有present这些东西呢都是手动加的啊嗯当然这个这个数据呢是让用户去选完之后呢去选完之后呢再往后传再往后才去传好吧行那再接着往下看啊
[04:51] 行那这个咱们需要把这个所有的channel啊都要去返回过来你看这里边是一个细色集合啊把这个数据都通通都装到response.redo.中就完事了然后下面看一下咱们要去当前还是这个重点还是文章的发布啊文章的发布这一块呢是有一个重点的内容应该不叫重点吧应该是说是业务比较复杂大家注意听啊首先啊这个思路咱们在这简单去分析一下咱们携带码的时候还会再说好吧
[05:20] 首先呢咱们会去传递参数啊判断为空啊这个没拿口说的是吧咱们一直是这么做的然后呢是要判断本次修改如果说你要是修改的话咱们先去删除数据库中的数据先去删除数据库中的数据那删谁呢就这样啊咱们删除的呢主要的就是当前的图片跟跟什么呢跟你的图文的一个关系我们看一下啊当前这个图不是当前那个表的关系咱们要简单简单说一遍大家注意听啊
[05:50] 目前的话呢你文章信息是保存到这是吧文章信息保存到这但这个信息呢是一些图文的信息是不是咱们的目前的图片信息都保存到这了对吧没问题啊但是呢你的图片你这个文章里边啊他应该是引用了一些图片引用了一些图片那这个关系保存到哪呢他两个他两个关系他俩关系都在这他俩关系都在这
[06:17] 所以说啊咱们首先要去删除的是当前那个关系要要要去删除关系最终呢咱们可以再重新去保存也就是说啊现在你要去创建文章可以你的文章里边必然会有图片所以说你要在这里边去找到图片并且呢找他的ID跟他的ID最终是保存到当前这个关系表中这个关系大家一定要清楚啊行那这个啊咱们一会儿去讲的时候还会再去重点去说这个东西啊
[06:46] 好那这个啊那这个的话下面的话其实就是重点刚才我说那个内容了啊你保存完文章之后没完拿到文章的ID然后拿到图文的ID最终的是保存图片跟文章的关系图片跟文章的关系两个都要保存因为刚才说了内容中有图片封面也有图片两块都有图片那这个时候你都要去都要去保存他们的关系就是他当前图片跟文章到底啥关系他就是一个关联关系OK啊
[07:15] 最终咱们处理完之后要去返回就可以了那行那这个咱们就算是把这个思路给说了一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个新闻内容管理系统中，如何通过数据库建表、Java实体类和MyBatis Mapper映射，实现文章发布功能的后端开发。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了新闻发布页面，用户可填写标题、标签、内容并上传图片。
画面2: 在IntelliJ IDEA中打开并展示`WmNewsMaterialMapper.xml`文件，其中包含一个用于统计文章数量的SQL查询语句。
画面3: 在IntelliJ IDEA中展示`WmNewsDto.java`文件，定义了新闻文章的Java实体类，包含id、title、channelId、labels、publishTime、content、type、status、reason、images等字段。
画面4: 展示了新闻发布页面，用户可填写标题、标签、内容并上传图片。
画面5: 在Navicat for MySQL中展示`wm_news`表的DDL语句，定义了文章表的结构，包含id、user_id、title、type、labels、content、status、created_time、updated_time、published_time、reason、images等字段。
画面6: 在IntelliJ IDEA中展示`WmNewsDto.java`文件，光标位于`reason`字段上。
画面7: 在IntelliJ IDEA中展示`WmNewsDto.java`文件，光标位于`images`字段的末尾。
画面8: 在Navicat for MySQL中展示`wm_news`表的DDL语句，与画面5内容相同。
画面9: 在Navicat for MySQL中展示`ad_channel`表的DDL语句，定义了频道表的结构，包含id、name、description、status、created_time、updated_time等字段。
画面10: 在Typora中打开文档，内容为“5.1.2 Mapper实现”章节，描述了接口定义和代码实现，包括请求DTO、响应DTO、参数校验和业务逻辑。
画面11: 在Typora中打开文档，内容为“5.1.2 Mapper实现”章节，展示Mapper实现部分，具体为`WmNewsMaterialMapper`中定义的`findMaterialByIdAndImgUrls`方法。
画面12: 在Navicat for MySQL中展示`wm_news`表的DDL语句，与画面5内容相同。
画面13: 在Navicat for MySQL中展示`wm_material`表的DDL语句，定义了素材表的结构，包含id、user_id、type、title、content、status、created_time、updated_time、published_time、reason、images等字段。
画面14: 在Typora中打开文档，内容为“5.1.2 Mapper实现”章节，与画面10内容相同。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面2 XML:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Mapper PUBLIC "-//mybatis.org/DTD/mybatis-3.0.dtd" "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
<Mapper namespace="com.heima.model.mappers.wenda.WmNewsMaterialMapper">
    <select id="countByMid" resultType="java.lang.Integer">
        select count(0)
        from wm_news_material
        where material_id = #{mid}
    </select>
</Mapper>
```

画面3 Java:
```java
package com.heima.model.media.dtos;

import ...
@Data
public class WmNewsDto {
    private Integer id;
    private String title;
    @IdEncrypt
    private Integer channelId;
    private String labels;
    private Date publishTime;
    private String content;
    private Short type;
    private Short status;
    private String reason;
    private List<String> images;
}
```

画面5 SQL:
```sql
CREATE TABLE `wm_news` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `user_id` int(11) unsigned DEFAULT NULL COMMENT '自媒体用户id',
  `title` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '标题',
  `type` tinyint(4) unsigned DEFAULT NULL COMMENT '文章类型',
  `labels` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '标签',
  `content` text COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '内容',
  `status` tinyint(4) unsigned DEFAULT NULL COMMENT '状态',
  `created_time` datetime DEFAULT NULL COMMENT '创建时间',
  `updated_time` datetime DEFAULT NULL COMMENT '更新时间',
  `published_time` datetime DEFAULT NULL COMMENT '发布时间',
  `reason` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '原因',
  `images` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '图片用逗号分隔',
  PRIMARY KEY (`id`),
  KEY `idx_user_id` (`user_id`),
  KEY `idx_status` (`status`),
  KEY `idx_created_time` (`created_time`),
  KEY `idx_updated_time` (`updated_time`),
  KEY `idx_published_time` (`published_time`),
  KEY `idx_reason` (`reason`),
  KEY `idx_images` (`images`),
  KEY `idx_type` (`type`),
  KEY `idx_labels` (`labels`),
  KEY `idx_title` (`title`),
  KEY `idx_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=404 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC COMMENT='自媒体图文内容表';
```

画面9 SQL:
```sql
CREATE TABLE `ad_channel` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '频道主键',
  `name` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '频道名称',
  `description` varchar(128) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '频道描述',
  `status` tinyint(4) unsigned DEFAULT NULL COMMENT '默认状态',
  `created_time` datetime DEFAULT NULL COMMENT '创建时间',
  `updated_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC COMMENT='频道表';
```

画面13 SQL:
```sql
CREATE TABLE `wm_material` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `user_id` int(11) unsigned DEFAULT NULL COMMENT '自媒体用户id',
  `type` tinyint(4) unsigned DEFAULT NULL COMMENT '素材类型',
  `title` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '标题',
  `content` text COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '内容',
  `status` tinyint(4) unsigned DEFAULT NULL COMMENT '状态',
  `created_time` datetime DEFAULT NULL COMMENT '创建时间',
  `updated_time` datetime DEFAULT NULL COMMENT '更新时间',
  `published_time` datetime DEFAULT NULL COMMENT '发布时间',
  `reason` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '原因',
  `images` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '图片用逗号分隔',
  `collection` tinyint(1) DEFAULT NULL COMMENT '是否收藏',
  `tags` text COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '标签',
  PRIMARY KEY (`id`),
  KEY `idx_user_id` (`user_id`),
  KEY `idx_status` (`status`),
  KEY `idx_created_time` (`created_time`),
  KEY `idx_updated_time` (`updated_time`),
  KEY `idx_published_time` (`published_time`),
  KEY `idx_reason` (`reason`),
  KEY `idx_images` (`images`),
  KEY `idx_type` (`type`),
  KEY `idx_title` (`title`),
  KEY `idx_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=404 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC COMMENT='自媒体素材表';
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面10、11、14: PPT标题为“5.1.2 Mapper实现”，内容包括：
- 请求DTO: `{"host": null, "code": 0, "error_message": "操作成功", "data": "SUCCESS"}`
- 响应DTO: `{"host": null, "code": 0, "error_message": "操作成功", "data": "List<AddChannel>"}`
- CODE定义:
  - `PARAM_INVALID` -> `PARAM_INVALID(501, "无效参数")`
  - `PARAM_REQUIRE` -> `PARAM_REQUIRE(500, "缺少参数")`
- 业务逻辑分析:
  - 如果用户传递参数为空或内容为空，返回`PARAM_REQUIRE`错误。
  - 如果用户本次为修改操作，则先删除数据库中的信息。
  - 保存或修改文章的数据。
  - 保存封面图片和当前文章的关系。
  - 流程处理完成返回处理结果。

5) 无。

