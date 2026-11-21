# 画面线理解：22_app文章列表_mapper文件编写2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\22_app文章列表_mapper文件编写2【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:14, 01:16, 01:54, 03:16, 04:36, 04:59, 05:41, 06:40, 06:56, 07:26, 08:03, 09:21, 09:56, 11:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:39:54

1) 这一组画面整体在讲什么（一句话）：
演示如何在 MyBatis 中通过 XML 映射文件实现分页和条件查询，包括 Java 接口定义、SQL 映射配置和实体类结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示了 IntelliJ IDEA 中的项目结构和 SQL 映射文件 `ApUserArticleListMapper.xml` 的部分内容。
- 代码片段：
  ```xml
  <select id="loadArticleListByIdList">
  <!-- 代码被高亮或部分遮挡 -->
  </select>
  ```
- 画面中高亮显示了 `if test="dto.tag != '_all'"` 和 `limit #{dto.size}` 等条件判断和分页语句。

画面 2：
- 显示了 Java 接口 `ApUserArticleListMapper` 的定义。
- 代码片段：
  ```java
  package com.heima.model.mappers.app;
  import com.heima.model.article.dto.ArticleHomeDto;
  import com.heima.model.user.pojos.ApUser;
  import com.heima.model.user.pojos.ApUserArticleList;
  import org.apache.ibatis.annotations.Param;
  public interface ApUserArticleListMapper {
      List<ApArticleList> loadArticleListByIdList(List<ApUserArticleList> list);
  }
  ```

画面 3：
- 显示了 `ApUserArticleListMapper.xml` 文件中 `select` 标签的编辑状态。
- 代码片段：
  ```xml
  <select id="loadArticleListByIdList">
  <!-- 代码被高亮或部分遮挡 -->
  </select>
  ```
- 画面中高亮显示了 `select` 标签和 `where` 条件。

画面 4：
- 显示了 `ApUserArticleListMapper.xml` 文件中 `select` 标签的完整内容。
- 代码片段：
  ```xml
  <select id="loadArticleListByIdList">
      select * from ap_article
      where id in
      <trim suffixOverrides=",">
          <foreach collection="list" item="item" separator=",">
              #{item.article_id}
          </foreach>
      </trim>
  </select>
  ```

画面 5：
- 显示了 Java 接口 `ApUserArticleListMapper` 的定义。
- 代码片段：
  ```java
  public interface ApUserArticleListMapper {
      List<ApUserArticleList> loadArticleListByUser(@Param("user") ApUser user, @Param("dto") ArticleHomeDto dto);
  }
  ```

画面 6：
- 显示了 MyBatis 的 XML 映射文件内容。
- 代码片段：
  ```xml
  <select id="loadArticleListByUser" parameterType="map" resultMap="BaseResultMap">
      <include refid="Base_Column_List" />
      from ap_user_article_list
      where
      user_id = #{user.id} and is_show = 0 and is_read = 0
      <if test="type != null and type == 1">
          and recommend_time <![CDATA[>]]> #{dto.minHotTime}
      </if>
      <if test="type != null and type == 2">
          and recommend_time <![CDATA[<]]> #{dto.maxHotTime}
      </if>
      <if test="dto.tag != '_all'">
          and channel_id = #{dto.tag}
      </if>
      limit #{dto.size}
  </select>
  ```

画面 7：
- 显示了 `BaseResultMap` 的定义。
- 代码片段：
  ```xml
  <resultMap id="BaseResultMap" type="com.heima.model.user.pojos.ApUserArticleList">
      <result column="id" property="id" />
      <result column="user_id" property="userId" />
      <result column="channel_id" property="channelId" />
      <result column="article_id" property="articleId" />
      <result column="is_show" property="isShow" javaType="java.lang.Boolean" jdbcType="BIT" />
      <result column="recommend_time" property="recommendTime" javaType="java.util.Date" jdbcType="TIMESTAMP" />
      <result column="is_read" property="isRead" javaType="java.lang.Boolean" jdbcType="BIT" />
      <result column="strategy_id" property="strategyId" />
  </resultMap>
  ```

画面 8：
- 显示了 MyBatis 的 XML 映射文件内容。
- 代码片段：
  ```xml
  <resultMap id="Base_Column_List" type="com.heima.model.user.pojos.ApUserArticleList">
      <result column="id" property="id" />
      <result column="user_id" property="userId" />
      <result column="channel_id" property="channelId" />
      <result column="article_id" property="articleId" />
      <result column="is_show" property="isShow" javaType="java.lang.Boolean" jdbcType="BIT" />
      <result column="recommend_time" property="recommendTime" javaType="java.util.Date" jdbcType="TIMESTAMP" />
      <result column="is_read" property="isRead" javaType="java.lang.Boolean" jdbcType="BIT" />
      <result column="strategy_id" property="strategyId" />
  </resultMap>
  ```

画面 9：
- 显示了 `Base_Column_List` 的定义。
- 代码片段：
  ```xml
  <resultMap id="Base_Column_List" type="com.heima.model.user.pojos.ApUserArticleList">
      <result column="id" property="id" />
      <result column="user_id" property="userId" />
      <result column="channel_id" property="channelId" />
      <result column="article_id" property="articleId" />
      <result column="is_show" property="isShow" javaType="java.lang.Boolean" jdbcType="BIT" />
      <result column="recommend_time" property="recommendTime" javaType="java.util.Date" jdbcType="TIMESTAMP" />
      <result column="is_read" property="isRead" javaType="java.lang.Boolean" jdbcType="BIT" />
      <result column="strategy_id" property="strategyId" />
  </resultMap>
  ```

画面 10：
- 显示了 MySQL 数据库的表结构。
- 代码片段：
  ```sql
  CREATE TABLE `ap_user_article_list` (
      `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
      `user_id` int(11) unsigned DEFAULT NULL COMMENT '用户id',
      `channel_id` int(11) unsigned DEFAULT NULL COMMENT '频道id',
      `article_id` int(11) unsigned DEFAULT NULL COMMENT '文章id',
      `is_show` tinyint(1) unsigned DEFAULT NULL COMMENT '是否展示',
      `recommend_time` int(11) unsigned DEFAULT NULL COMMENT '推荐时间',
      `is_read` tinyint(1) unsigned DEFAULT NULL COMMENT '是否已读',
      `strategy_id` int(11) unsigned DEFAULT NULL COMMENT '策略id',
      PRIMARY KEY (`id`) USING BTREE
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC COMMENT='用户文章列表';
  ```

画面 11：
- 显示了 Java 实体类 `ApUser` 的定义。
- 代码片段：
  ```java
  package com.heima.model.user.pojos;
  import lombok.Data;
  public class ApUser {
      private Long id;
      private String salt;
      private String name;
      private String password;
      private String phone;
      private String image;
      private Boolean isCertification;
      private Boolean isIdentityAuthentication;
      private Boolean status;
      private int flag;
  }
  ```

画面 12：
- 显示了 `ApUserArticleListMapper.xml` 文件中 `select` 标签的编辑状态。
- 代码片段：
  ```xml
  <if test="type != null and type == 2">
      and recommend_time <![CDATA[<]]> #{dto.maxHotTime}
  </if>
  <if test="dto.tag != '_all'">
      and channel_id = #{dto.tag}
  </if>
  <where>
      limit #{dto.size}
  </select>
  ```

画面 13：
- 显示了 Java 接口 `ApUserArticleListMapper` 的定义。
- 代码片段：
  ```java
  public interface ApUserArticleListMapper {
      List<ApUserArticleList> loadArticleListByUser(@Param("user") ApUser user, @Param("dto") ArticleHomeDto dto);
  }
  ```

画面 14：
- 显示了 `ApUserArticleListMapper.xml` 文件中 `select` 标签的编辑状态。
- 代码片段：
  ```xml
  <select id="loadArticleListByUser" resultMap="BaseResultMap">
      select * from ap_user_article_list
      where
      user_id = #{user.id} and is_show = 0 and is_read = 0
      <if test="type != null and type == 1">
          and recommend_time <![CDATA[>]]> #{dto.minHotTime}
      </if>
      <if test="type != null and type == 2">
          and recommend_time <![CDATA[<]]> #{dto.maxHot
