# 画面线理解：12_自媒体文章管理_发布文章需求分析

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\12_自媒体文章管理_发布文章需求分析【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 01:38, 01:43, 02:10, 02:22, 02:51, 03:42, 04:03, 04:28, 04:51, 05:43, 06:05, 06:32, 07:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:48:41

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
<!DOCTYPE mapper PUBLIC "-//mybatis.org/DTD/mybatis-3.0.dtd" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.heima.model.mappers.wenda.WmNewsMaterialMapper">
    <select id="countByMid" resultType="java.lang.Integer">
        select count(0)
        from wm_news_material
        where material_id = #{mid}
    </select>
</mapper>
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
