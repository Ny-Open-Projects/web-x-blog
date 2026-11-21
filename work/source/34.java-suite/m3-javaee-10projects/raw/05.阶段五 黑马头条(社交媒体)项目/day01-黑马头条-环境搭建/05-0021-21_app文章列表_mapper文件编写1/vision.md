# 画面线理解：21_app文章列表_mapper文件编写1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\21_app文章列表_mapper文件编写1【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:33, 01:12, 02:13, 02:48, 03:52, 04:52, 05:33, 06:29, 07:18, 07:52, 08:42, 09:54, 11:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:39:01

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过 MyBatis 框架实现文章列表的分页查询功能，包括定义数据访问层接口、编写 SQL 映射文件、配置数据源以及在服务层调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 `AppArticleServiceImpl.java` 中的 `getDefaultArticleList` 方法，该方法通过 `apArticleMapper.loadArticleListByLocation` 查询文章列表。
画面 2: 展示了在 IntelliJ IDEA 中右键点击 `java` 目录，弹出创建新文件的菜单，准备创建新的 Java 类或接口。
画面 3: 展示了 `ApArticleMapper.java` 接口文件，其中定义了 `loadArticleListByLocation` 和 `loadArticleListByIdList` 两个方法。
画面 4: 展示了项目结构，选中了 `ApArticleMapper` 接口文件。
画面 5: 展示了 `ApArticleMapper.xml` 文件，其中包含了 MyBatis 的 XML 配置头和 `<mapper>` 标签。
画面 6: 展示了在 `ApArticleMapper.xml` 文件中，光标位于 `<select id="loadArticleListByLocation">` 标签内，准备编写 SQL。
画面 7: 展示了 MySQL 数据库的 Navicat 界面，显示了 `ap_article` 表的数据，用于验证 SQL 查询结果。
画面 8: 展示了 `ApArticleMapper.xml` 文件中，`<resultMap>` 标签内定义了 `ApArticle` 对象的属性映射。
画面 9: 展示了 `ApArticleMapper.xml` 文件中，`<sql id="Base_Column_List">` 标签定义了公共的列名，以及两个 `<select>` 标签分别对应 `loadArticleListByLocation` 和 `loadArticleListByIdList` 方法。
画面 10: 展示了 `ArticleConsts.java` 文件，其中定义了 `ArticleInfoDto`、`ArticleListDto` 和 `UserArticleListDto` 等数据传输对象。
画面 11: 展示了 `ApArticleMapper.xml` 文件中，`loadArticleListByLocation` 方法的 SQL 查询语句，包含 `where` 条件判断 `dto.provinceId` 是否为空。
画面 12: 展示了 `ApArticleMapper.xml` 文件中，`loadArticleListByLocation` 方法的 SQL 查询语句，增加了对 `dto.cityId` 的条件判断。
画面 13: 展示了 `ApArticleMapper.xml` 文件中，`loadArticleListByLocation` 方法的 SQL 查询语句，增加了对 `dto.countyId` 的条件判断。
画面 14: 展示了 `ApArticleMapper.xml` 文件中，`loadArticleListByLocation` 方法的 SQL 查询语句，增加了对 `type` 参数的条件判断。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
private List<Article> getDefaultArticle(ArticleHomeDto dto, Short type) {
    return apArticleMapper.loadArticleListByLocation(dto, type);
}

@AutoWired
private ApArticleListMapper apUserArticleListMapper;

// 先从用户的缓存中查询文章信息，如果没有再从默认文章信息获取
private List<Article> getUserArticleList(ArticleHomeDto dto, Short type) {
    List<Article> list = apUserArticleListMapper.loadArticleListByUser(dto, user, type);
    if (list.size() == 0) {
        return apArticleMapper.loadArticleListByLocation(list);
    }
    return list;
}
```

画面 3:
```java
package com.heima.model.mappers.app;

import com.heima.model.article.dto.ArticleHomeDto;
import com.heima.model.article.po.Article;
import com.heima.model.user.po.ApUser;
import java.util.List;

public interface ApArticleMapper {
    List<Article> loadArticleListByLocation(ArticleHomeDto dto, Short type);
    List<Article> loadArticleListByIdList(List<ApUserArticleList> list);
}
```

画面 5:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.heima.model.mappers.app.ApArticleMapper">
</mapper>
```

画面 6:
```xml
<select id="loadArticleListByLocation">
</select>
```

画面 8:
```xml
<resultMap id="resultMap" type="com.heima.model.article.po.ApArticle">
    <result column="id" property="id"/>
    <result column="title" property="title"/>
    <result column="author_name" property="authorName"/>
    <result column="channel_id" property="channelId"/>
    <result column="channel_name" property="channelName"/>
    <result column="layout" property="layout"/>
    <result column="flag" property="flag"/>
    <result column="images" property="images"/>
    <result column="labels" property="labels"/>
    <result column="likes" property="likes"/>
    <result column="collection" property="collection"/>
    <result column="comment" property="comment"/>
    <result column="views" property="views"/>
    <result column="province_id" property="provinceId"/>
    <result column="city_id" property="cityId"/>
    <result column="county_id" property="countyId"/>
    <result column="created_time" property="createdTime"/>
    <result column="publish_time" property="publishTime"/>
    <result column="sync_status" property="syncStatus"/>
</resultMap>
```

画面 9:
```xml
<sql id="Base_Column_List">
    id, title, author_name, channel_id, channel_name, layout, flag, images,
    labels, likes, collection, comment, views, province_id, city_id, county_id, created_time,
    publish_time, sync_status
</sql>

<select id="loadArticleListByLocation" resultMap="resultMap">
    <include refid="Base_Column_List"/>
    from ap_article aa
</select>

<select id="loadArticleListByIdList">
</select>
```

画面 11:
```xml
<select id="loadArticleListByLocation" resultMap="resultMap">
    <include refid="Base_Column_List"/>
    from ap_article aa
    where
        <if test="dto.provinceId != null">
            and aa.province_id = #{dto.provinceId}
        </if>
</select>
```

画面 12:
```xml
<select id="loadArticleListByLocation" resultMap="resultMap">
    <include refid="Base_Column_List"/>
    from ap_article aa
    where
        <if test="dto.provinceId != null">
            and aa.province_id = #{dto.provinceId}
        </if>
        <if test="dto.cityId != null">
            and aa.city_id = #{dto.cityId}
        </if>
</select>
```

画面 13:
```xml
<select id="loadArticleListByLocation" resultMap="resultMap">
    <include refid="Base_Column_List"/>
    from ap_article aa
    where
        <if test="dto.provinceId != null">
            and aa.province_id = #{dto.provinceId}
        </if>
        <if test="dto.cityId != null">
            and aa.city_id = #{dto.cityId}
        </if>
        <if test="dto.countyId != null">
            and aa.county_id = #{dto.countyId}
        </if>
</select>
```

画面 14:
```xml
<select id="loadArticleListByLocation" resultMap="resultMap">
    <include refid="Base_Column_List"/>
    from ap_article aa
    where
        <if test="dto.provinceId != null">
            and aa.province_id = #{dto.provinceId}
        </if>
        <if test="dto.cityId != null">
            and aa.city_id = #{dto.cityId}
        </if>
        <if test="dto.countyId != null">
            and aa.county_id = #{dto.countyId}
        </if>
        <if test="type != null and type == 1">
            and aa.publish_time <![CDATA[>]]> #{dto.minBehotTime}
        </if>
        <if test="type != null and type == 2">
            and aa.publish_time <![CDATA[<]]> #{dto.maxBehotTime}
        </if>
</select>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
