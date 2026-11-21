# 画面线理解：13_app文章详情_文章关系接口_mapper定义

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\13_app文章详情_文章关系接口_mapper定义【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:16, 01:44, 02:40, 03:59, 05:07, 06:29, 07:11, 08:22, 09:32, 10:36, 11:32, 12:15, 13:20, 14:07
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:14:08

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 MyBatis 实现对文章行为（收藏、点赞、点踩、关注、作者）的数据库操作，包括实体类定义、Mapper 接口与 XML 映射文件的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 ArticleInfoDto 实体类的定义和行为表（ap_behavior_entry）、收藏表（ap_collection）、点赞表（ap_likes_behavior）、点踩表（ap_unlikes_behavior）、关注表（ap_user_follow）、作者表（ap_author）的说明。
画面 2: 展示了 ApBehaviorEntryMapper.xml 文件中，根据 userId 或 equipmentId 查询行为实体的 SQL 语句，包含条件判断。
画面 3: 展示了 ApCollection 类的定义，包含字段如 id、behaviorEntryId、entryId、type、collectionTime、burst，并定义了枚举类型 Type。
画面 4: 展示了 ApCollectionMapper 接口，定义了根据 object_id、entry_id、type、burst 查询收藏数据的方法。
画面 5: 展示了 ApCollectionMapper.xml 文件中，根据 object_id 和 entry_id 查询收藏数据的 SQL 语句。
画面 6: 展示了 ApCollectionMapper.xml 文件中，根据 object_id 和 entry_id 查询收藏数据的 SQL 语句，光标在 select 语句上。
画面 7: 展示了 ApUserFollowMapper.xml 文件中，根据 user_id 和 follow_id 查询关注关系的 SQL 语句。
画面 8: 展示了 MySQL 数据库中 ap_likes_behavior 表的 DDL 创建语句，包含字段定义和注释。
画面 9: 展示了 ApLikesBehaviorMapper.xml 文件中，根据 object_id 和 entry_id 查询点赞数据的 SQL 语句。
画面 10: 展示了 ApLikesBehaviorMapper 接口，定义了查询最后一条点赞记录的方法。
画面 11: 展示了 ApUnlikesBehaviorMapper 的定义和对应的 XML 映射文件，包含根据 entry_id 和 article_id 查询点踩数据的 SQL。
画面 12: 展示了数据库表结构，包括 ap_share_behavior、ap_collection、ap_likes_behavior、ap_behavior_entry 等表的定义，其中 ap_likes_behavior 表的 burst 字段定义为 (id_behavior_id)。
画面 13: 展示了 ApAuthorMapper 接口，定义了根据 id 查询作者信息的方法。
画面 14: 重复画面 1 的内容，强调通过 authorId 和 appUserId 查询作者信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
ArticleInfoDto
// 设备id
@IdEncrypt
Integer equipmentId;
// 文章id
@IdEncrypt
Integer articleId;
// 作者id
@IdEncrypt
Integer authorId;

画面 2:
<select id="selectByIdOrEquipmentId" resultMap="BaseResultMap">
  <!-- 如果userId不为空，查询userId对应的记录 -->
  <if test="userId != null">
    select * from ap_behavior_entry where a.entry_id = #{userId} and type = 1 limit 1
  </if>
  <!-- 如果userId为空，查询equipmentId对应的记录 -->
  <if test="userId == null and equipmentId != null">
    select * from ap_behavior_entry where a.entry_id = #{equipmentId} and type = 0 limit 1
  </if>
</select>

画面 3:
@Data
public class ApCollection {
    @IdEncrypt
    private Long id;
    @IdEncrypt
    private Integer behaviorEntryId;
    @IdEncrypt
    private Integer entryId;
    @IdEncrypt
    private Short type;
    @IdEncrypt
    private Date collectionTime;
    @IdEncrypt
    private Date publishedTime;
    @JsonIgnore
    private String burst;
    // 定义以硬件类型为粒度的burst
    @Alias("ApCollectionEnumType")
    public enum Type {
        ARTICLE((short)0), DYNAMIC((short)1);
        short code;
        Type(short code) {
            this.code = code;
        }
        public short getCode() {
            return this.code;
        }
    }
}

画面 4:
package com.heima.model.mappers.app;
import com.heima.model.article.po.ApCollection;
public interface ApCollectionMapper {
    // 选择一个终端的收藏数据
    @Select("select * from ap_collection where object_id = #{object_id} and entry_id = #{entry_id} and type = #{type} and burst = #{burst}")
    ApCollection selectByObjectAndEntryId(String object_id, Integer entry_id, Short type, Integer burst);
}

画面 5:
<resultMap id="BaseResultMap" type="com.heima.model.article.po.ApCollection">
    <result column="behavior_entry_id" property="behaviorEntryId"/>
    <result column="entry_id" property="entryId"/>
    <result column="type" property="type"/>
    <result column="collection_time" property="collectionTime"/>
    <result column="published_time" property="publishedTime"/>
    <result column="burst" property="burst"/>
</resultMap>
<sql id="Base_Column_list">
    id, behavior_entry_id, entry_id, type, collection_time, published_time, burst
</sql>
<select id="selectForEntryId" resultMap="BaseResultMap">
    <!-- 选择收藏记录 -->
    select * from ap_collection where behavior_entry_id = #{object_id} and entry_id = #{entry_id} and type = #{type} and burst = #{burst}
</select>

画面 6:
<resultMap id="BaseResultMap" type="com.heima.model.article.po.ApCollection">
    <result column="behavior_entry_id" property="behaviorEntryId"/>
    <result column="entry_id" property="entryId"/>
    <result column="type" property="type"/>
    <result column="collection_time" property="collectionTime"/>
    <result column="published_time" property="publishedTime"/>
    <result column="burst" property="burst"/>
</resultMap>
<sql id="Base_Column_list">
    id, behavior_entry_id, entry_id, type, collection_time, published_time, burst
</sql>
<select id="selectForEntryId" resultMap="BaseResultMap">
    <!-- 选择收藏记录 -->
    select * from ap_collection where behavior_entry_id = #{object_id} and entry_id = #{entry_id} and type = #{type} and burst = #{burst}
</select>

画面 7:
<resultMap id="BaseResultMap" type="com.heima.model.user.po.ApUserFollow">
    <result column="id" property="id"/>
    <result column="user_id" property="userId"/>
    <result column="follow_name" property="followName"/>
    <result column="level" property="level"/>
    <result column="is_notice" property="isNotice"/>
    <result column="created_time" property="createdTime"/>
    <result column="burst" property="burst"/>
</resultMap>
<sql id="Base_Column_list">
    follow_id, user_id, level, is_notice, created_time
</sql>
<select id="selectFollowById">
    <!-- 选择关注关系 -->
    select * from ap_user_follow where user_id = #{userId} and follow_id = #{followId} and burst = #{burst}
</select>

画面 8:
CREATE TABLE `ap_likes_behavior` (
  `id` int(11) unsigned NOT NULL,
  `behavior_entry_id` int(11) unsigned DEFAULT NULL COMMENT '实体id',
  `entry_id` int(11) unsigned DEFAULT NULL COMMENT '文章id',
  `type` int(11) unsigned DEFAULT NULL COMMENT '动态',
  `operation` tinyint(4) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '点赞/点踩',
  `created_time` datetime DEFAULT NULL COMMENT '创建时间',
  `burst` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '行为id',
  PRIMARY KEY (`id`),
  KEY `index_behavior_entry_id` (`behavior_entry_id`),
  KEY `index_entry_id` (`entry_id`),
  KEY `index_type` (`type`),
  KEY `index_operation` (`operation`),
  KEY `index_created_time` (`created_time`),
  KEY `index_burst` (`burst`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC COMMENT='点赞行为表';

画面 9:
<resultMap id="BaseResultMap" type="com.heima.model.behavior.po.ApLikesBehavior">
    <result column="id" property="id"/>
    <result column="behavior_entry_id" property="behaviorEntryId"/>
    <result column="entry_id" property="entryId"/>
    <result column="type" property="type"/>
    <result column="operation" property="operation"/>
    <result column="created_time" property="createdTime"/>
    <result column="burst" property="burst"/>
</resultMap>
<sql id="Base_Column_list">
    id, behavior_entry_id, entry_id, type, operation, created_time, burst
</sql>
<select id="selectLastLike" resultMap="BaseResultMap">
    <!-- 选择最后一条点赞记录 -->
    select * from ap_likes_behavior where behavior_entry_id = #{object_id} and entry_id =
