# 画面线理解：07_自媒体文章自动审核_mapper接口编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\07_自媒体文章自动审核_mapper接口编写【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:18, 01:04, 01:43, 02:52, 03:19, 03:56, 04:29, 04:49, 05:17, 05:52, 06:25, 07:32, 08:16, 08:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:19:56

1) 这一组画面整体在讲什么（一句话）：
实现文章发布流程中各模块的数据库映射（Mapper）代码，包括频道、作者、文章配置和文章本身等实体的增删改查操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文章发布流程的架构图，包含“文章审核”、“Kafka”、“获取内容”、“文章是否审核”、“状态变更”等节点。
画面2：在文档中说明需修改 AdChannelMapper 和 ApAuthorMapper，添加根据ID或作者名查询的方法。
画面3：在文档中说明需修改 ApAuthorMapper，添加根据名称查询作者的方法。
画面4：在IDEA中打开 AdChannelMapper.xml，展示根据ID查询频道的SQL语句。
画面5：在IDEA中打开 ApAuthorMapper.xml，展示根据作者名查询和插入作者的SQL语句。
画面6：在文档中说明需修改 ApArticleContentMapper 和 ApArticleConfigMapper，添加新增数据的方法。
画面7：在IDEA中打开 ApArticleConfigMapper.xml，展示插入文章配置的SQL语句。
画面8：在IDEA中打开 ApArticleMapper.xml，展示插入文章的SQL语句。
画面9：在IDEA中打开 ApArticleConfigMapper.xml，展示插入文章配置的SQL语句。
画面10：在文档中说明需修改 WmNewsMapper，添加修改的方法。
画面11：在IDEA中打开 WmNewsMapper.xml，展示根据条件更新文章状态的SQL语句。
画面12：在IDEA中右键点击项目，弹出创建新文件的菜单。
画面13：在IDEA中打开 ApMessageMapper.xml，展示其命名空间和包含的Mapper接口。
画面14：在文档中说明需修改 ReviewMediaArticleService 接口，添加自动审核文章的方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
wm_news表状态
1. 草稿（待审核）
2. 等待审核
3. 人工审核
4. 人工审核通过（待发布）
5. 自动审核通过（待发布）
6. 已发布

画面2：
修改com.heima.model.mappers.admin.AdChannelMapper，添加根据ID查询频道方法
AdChannelMapper.xml
<select id="selectByPrimaryKey" resultMap="BaseResultMap"
        parameterType="java.lang.Integer">
    select
    <include refid="Base_Column_List"/>
    from ad_channel
    where id = #{id}
</select>

修改com.heima.model.mappers.app.ApAuthorMapper，添加根据名称查询作者方法
ApAuthorMapper.xml
<select id="selectByAuthorName" parameterType="java.lang.String"
        resultType="com.heima.model.article.po.ApAuthor">
    select * from ap_author where name = #{authorName}
</select>

画面3：
修改com.heima.model.mappers.app.ApAuthorMapper，添加根据名称查询作者方法
ApAuthorMapper.xml
<select id="selectByAuthorName" parameterType="java.lang.String"
        resultType="com.heima.model.article.po.ApAuthor">
    select * from ap_author where name = #{authorName}
</select>

画面4：
<select id="selectByPrimaryKey" resultMap="BaseResultMap"
        parameterType="java.lang.Integer">
    select
    <include refid="Base_Column_List"/>
    from ad_channel
    where id = #{id}
</select>

画面5：
<select id="selectByAuthorName" parameterType="java.lang.String"
        resultType="com.heima.model.article.po.ApAuthor">
    select * from ap_author where name = #{authorName}
</select>

<select id="insert" parameterType="com.heima.model.article.po.ApAuthor"
        resultType="java.lang.Integer" order="AFTER">
    insert into ap_author (name, type, user_id, vm_user_id, created_time)
    values (#{name}, #{type}, #{userId}, #{vmUserId}, #{createdTime})
</insert>

画面6：
修改com.heima.model.mappers.app.ApArticleContentMapper，添加新增数据的方法
ApArticleContentMapper.xml
<insert id="insert" parameterType="com.heima.model.article.po.ApArticleContent">
    insert into ap_article_content (article_id, content) values (#{articleId}, #{content})
</insert>

修改com.heima.model.mappers.app.ApArticleConfigMapper，添加新增数据的方法
ApArticleConfigMapper.xml
<insert id="insert" parameterType="com.heima.model.article.po.ApArticleConfig">
    insert into ap_article_config (article_id, is_comment, is_forward, is_down, is_delete)
    values (#{articleId}, #{isComment}, #{isForward}, #{isDown}, #{isDelete})
</insert>

画面7：
<select id="selectByArticleId" resultType="BaseResultMap" parameterType="int">
    select
    <include refid="Base_Column_List"/>
    from ap_article_config
    where article_id = #{articleId}
</select>

画面8：
<select id="selectById" parameterType="java.lang.Long" resultType="resultMap">
    select
    <include refid="Base_Column_List"/>
    from ap_article
    where id = #{id}
</select>

<insert id="insert" parameterType="com.heima.model.article.ApArticle"
        selectKey="selectKey" resultType="java.lang.Integer" order="AFTER" keyColumn="id" keyProperty="id">
    insert into ap_article
    (title, author_id, author_name, channel_id, layout, flags, images, labels)
    values (#{title}, #{authorId}, #{authorName}, #{channelId}, #{layout}, #{flags}, #{images}, #{labels})
</insert>

画面9：
<select id="selectByArticleId" resultType="BaseResultMap" parameterType="int">
    select
    <include refid="Base_Column_List"/>
    from ap_article_config
    where article_id = #{articleId}
</select>

画面10：
修改com.heima.model.mappers.wemedia.WmNewsMapper，添加修改的方法
WmNewsMapper.xml
<update id="updateByPrimaryKeysSelective"
        parameterType="com.heima.model.wemedia.po.WmNews">
    update wm_news
    <if test="userId != null">
        user_id = #{userId},
    </if>
    <if test="title != null">
        title = #{title},
    </if>
    <if test="type != null">
        type = #{type},
    </if>
    <if test="channelId != null">
        channel_id = #{channelId},
    </if>
    <if test="status != null">
        status = #{status},
    </if>
    <if test="publishTime != null">
        publish_time = #{publishTime},
    </if>
    <if test="reason != null">
        reason = #{reason},
    </if>
    <if test="articleId != null">
        article_id = #{articleId},
    </if>
    <if test="content != null">
        content = #{content},
    </if>
</update>

画面11：
<if test="createdTime != null">
    created_time = #{createdTime},
</if>
<if test="submittedTime != null">
    submitted_time = #{submittedTime},
</if>
<if test="status != null">
    status = #{status},
</if>
<if test="publishTime != null">
    publish_time = #{publishTime},
</if>
<if test="reason != null">
    reason = #{reason},
</if>
<if test="articleId != null">
    article_id = #{articleId},
</if>
<if test="content != null">
    content = #{content},
</if>

画面12：
New
Class
Kotlin File/Class
Interface
Enum
File
Aspect
Scratch File
package-info.java
FXML File
HTML File
JavaScript File
TypeScript File
CSS File
XML File
YAML File
Properties File
JSON File
Groovy File
Kotlin Script
Java File
JavaFX File
Kotlin File
Kotlin Script
Kotlin DSL Settings
Gradle Kotlin DSL Build Script
SQL File
XSD File
XSLT File
DTD File
XML Configuration File
YAML Configuration File
Properties Configuration File
JSON Configuration File
YAML File
YAML Configuration File
Properties Configuration File
JSON Configuration File
YAML File
YAML Configuration File
Properties Configuration File
JSON Configuration File
YAML File
YAML Configuration File
Properties Configuration File
JSON Configuration File
YAML File
YAML Configuration File
Properties Configuration File
JSON Configuration File
YAML File
YAML Configuration File
Properties Configuration File
JSON Configuration File
YAML File
YAML Configuration File
Properties Configuration File
JSON Configuration File
YAML File
YAML Configuration File
Properties Configuration File
JSON Configuration File
YAML File
YAML Configuration File
Properties Configuration File
JSON Configuration File
YAML File
YAML Configuration File
Properties Configuration File
JSON Configuration File
YAML File
YAML Configuration File
Properties Configuration File
JSON Configuration File
YAML File
YAML Configuration File
Properties Configuration File
JSON Configuration File
YAML File
YAML Configuration File
Properties Configuration File
JSON Configuration File
YAML File
YAML Configuration File
Properties Configuration File
JSON Configuration File
YAML File
YAML
