# 画面线理解：03_热文章计算_定时计算_mapper定义

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\03_热文章计算_定时计算_mapper定义【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 02:16, 02:42, 02:58, 03:21, 03:55, 04:25, 04:42, 04:55, 05:18, 05:43, 06:08, 06:48, 07:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:32:52

1) 这一组画面整体在讲什么（一句话）：
讲解热点文章处理中热数据计算的实现，包括实体类、Mapper接口与XML映射文件、Service层代码的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT，标题为“2 热文章处理-热数据计算”，子标题“2.1 思路分析”和“2.2 实体类”，并显示实体类代码：@Data public class ApHotArticles { private Integer id; private Integer entryId; private Integer tagId; private String tagName; private Integer score; private Integer articleId; private Date releaseDate; private Integer provinceId; private Integer cityId; private Integer countyId; private Integer isRead; }

画面2：展示MySQL Workbench，正在编写创建表语句，表名为ap_hot_articles，包含字段：id, entry_id, tag_id, article_id, province_id, city_id, county_id, release_date, created_time, is_comment, is_forward, is_down, is_delete。语句为：CREATE TABLE `ap_hot_articles` ( `id` int(11) unsigned NOT NULL AUTO_INCREMENT, `entry_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '词条ID', `tag_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '标签ID', `article_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '文章ID', `province_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '省ID', `city_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '市ID', `county_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '县ID', `release_date` datetime DEFAULT NULL COMMENT '发布时间', `created_time` datetime DEFAULT NULL COMMENT '创建时间', `is_comment` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否允许评论', `is_forward` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否允许转发', `is_down` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否允许下载', `is_delete` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否删除', PRIMARY KEY (`id`) USING BTREE ) ENGINE=InnoDB AUTO_INCREMENT=1392 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC COMMENT='热文章表';

画面3：展示IntelliJ IDEA项目结构，当前选中包为com.heima.leadnews.model，目录结构包含main/java/com/heima/leadnews/model及子包article、behavior、common、crawler、mappers、user等。

画面4：在IntelliJ IDEA中，选中了包com.heima.leadnews.model下的admin子包，其中包含多个Mapper接口文件，如ApiArticleConfigMapper、ApiArticleLabelMapper等。

画面5：展示ApiArticlesMapper.java文件，代码中包含方法：List<ApHotArticles> loadArticleByIdList(Integer entryId, ArticleHomeDto short type); List<ApHotArticles> selectList(ApHotArticles apHotArticles); Integer selectTodayMaxScore(String today); int updateReadStatus(Integer entryId, Integer articleId); List<ApHotArticles> loadListByLocation(CursorDto articleHomeDto, short type);

画面6：展示ApiArticlesMapper.java文件，代码中包含方法：int updateReadStatus(Integer entryId, Integer articleId); List<ApHotArticles> loadListByLocation(CursorDto articleHomeDto, short type);

画面7：展示ApiArticlesMapper.xml文件，代码中包含：resultMap id="Base_Column_List" property="is_delete"/>，以及SQL语句：select id="selectByArticleId" resultMap="BaseResultMap" parameterType="int" select <include refid="Base_Column_List"/> from ap_article_config where article_id = #{articleId}，和insert语句：insert into ap_article_config (article_id, is_comment, is_forward, is_down, is_delete) values (#{articleId}, #{isComment}, #{isForward}, #{isDown}, #{isDelete});

画面8：展示PPT，标题为“2.2 实体类”，并显示实体类代码：@Data public class ApHotArticles { private Integer id; private Integer entryId; private Integer tagId; private String tagName; private Integer score; private Integer articleId; private Date releaseDate; private Integer provinceId; private Integer cityId; private Integer countyId; private Integer isRead; }，以及SQL语句：select id="selectTodayMaxScore" resultType="java.lang.Integer"> select max(score) from ap_hot_articles where created_time > #{today} </select>，和update语句：update ap_hot_articles set is_read = 1 where entry_id = #{entryId} and article_id = #{articleId}，以及select语句：select id="loadListByLocation" resultMap="BaseResultMap" select * from ap_hot_articles a where a.entry_id = 0 and a.province_id = #{dto.provinceId} and a.city_id = #{dto.cityId} and a.county_id = #{dto.countyId}。

画面9：展示ApiArticlesMapper.xml文件，代码中包含：xml version="1.0" encoding="UTF-8"，以及resultMap id="BaseResultMap" type="com.heima.model.article.pojos.ApHotArticles"，resultMap中包含多个resultColumn，如result column="id" property="id"，result column="entry_id" property="entryId"，result column="tag_id" property="tagId"，result column="tag_name" property="tagName"，result column="score" property="score"，result column="article_id" property="articleId"，result column="province_id" property="provinceId"，result column="city_id" property="cityId"，result column="county_id" property="countyId"，result column="is_read" property="isRead"，result column="release_date" property="releaseDate"，result column="created_time" property="createdTime"，以及sql id="Base_Column_List"。

画面10：展示PPT，标题为“2.2 实体类”，并显示实体类代码：@Data public class ApHotArticles { private Integer id; private Integer entryId; private Integer tagId; private String tagName; private Integer score; private Integer articleId; private Date releaseDate; private Integer provinceId; private Integer cityId; private Integer countyId; private Integer isRead; }，以及标题“2.3 Mapper实现”，并显示创建接口：public interface ApHotArticlesMapper {

画面11：展示PPT，标题为“2.3 Mapper实现”，并显示创建接口：public interface ApHotArticlesMapper { /* 插入文章数据 */ @Param record @Return int insert(ApHotArticles record); /* 结构传入日期之前的文 */ @Param removeDate @Return int removeHotArticle(String removeDate); }

画面12：展示PPT，标题为“2.3 Mapper实现”，并显示创建接口：public interface ApHotArticlesMapper { /* 插入文章数据 */ @Param record @Return int insert(ApHotArticles record); /* 结构传入日期之前的文 */ @Param removeDate @Return int removeHotArticle(String removeDate); }，以及SQL语句：select id="loadLastArticleForHot" resultMap="resultMap"> select <include refid="Base_Column_List"/> from ap_article where publish_time > #{lastDate} </select>。

画面13：展示PPT，标题为“2.4 service代码实现”，并显示创建接口：public interface ApHotArticleService { /* 获取最近的热文章 */ @Param lastDate @Return List<ApArticle> loadLastArticleForHot(String lastDate); }，以及SQL语句：select id="loadLastArticleForHot" resultMap="resultMap"> select <include refid="Base_Column_List"/> from ap_article where publish_time > #{lastDate} </select>。

画面14：展示PPT，标题为“2.4 service代码实现”，并显示创建接口：public interface ApHotArticleService { /* 获取最近的热文章 */ @Param lastDate @Return List<ApArticle> loadLastArticleForHot(String lastDate); }，以及SQL语句：select id="loadLastArticleForHot" resultMap="resultMap"> select <include refid="Base_Column_List"/> from ap_article where publish_time > #{lastDate} </select>。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：@Data public class ApHotArticles { private Integer id; private Integer entryId; private Integer tagId; private String tagName; private Integer score; private Integer articleId; private Date releaseDate; private Integer provinceId; private Integer cityId; private Integer countyId; private Integer isRead; }

画面2：CREATE TABLE `ap_hot_articles` ( `id` int(11) unsigned NOT NULL AUTO_INCREMENT, `entry_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '词条ID', `tag_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '标签ID', `article_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '文章ID', `province_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '省ID', `
