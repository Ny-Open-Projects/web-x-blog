# 07_自媒体文章自动审核_mapper接口编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\07_自媒体文章自动审核_mapper接口编写【海量资源尽在 666java.com】.mp4
- 时长 8分42秒（音频 522s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好刚才呢咱们是把当前的这种自动审核这一块的流程给说了一下然后下面咱们就来用代码的方式去实现啊这代码可能量会比较大大家一定要跟上思路首先呢咱们还是要去创建咱们的MIPR这个MIPR可能内容也比较多因为刚才说了这里边要去保存的时候呢可能涉及到的表比较多是吧你同时呢你还要去修改当前那个状态还有呢就是有还要去给用户去推送消息
[00:29] 所以说咱们辅助的表其实有很多咱们一块来看一下首先这里边是有一个Channel我去说哪个的时候咱们再去说说业务比如说当前咱们需要在ADChannelMap中去添加一个查询的方法为什么要去有这么一个方法实际上在咱们去真正去保存的时候在保存当前的APArticle的时候它是其实是要有一个什么有一个频道名称
[00:55] 那这时候咱们其实是能拿到当前的频道ID的所以说你需要去查询当前的频道名称去进行保存所以说你这边你需要当前的一个频道根据当前频道ID去查询频道的一个Map好吧那这时候咱们就可以去创建或者说咱们直接拷贝一下开当前的model到当前这个ChinoMap13.20
[01:24] 是在当前admin下面有一个adchina myper在这去加一个新增新增啊然后呢你在这儿去创建一个什么东西去这个myper这个前这个查询给扣过来其实就是edit查询行那这个就做完了啊做完了然后下面再往下看啊下面还有一个ap author myper那这个呢其实有两个方法是吧第一个呢是根据当前名称去查然后第二个呢是要什么要插入一条数据
[01:54] 要插入一条数据啊是这样啊这里边呢如果说你要查查询没有的话呢咱们就会去插入一条数据那为什么会这样呢因为这样啊因为你这个自媒体发布文章的时候呢如果说这个作者啊是没有当前的一个没有作者信息假如说没有作者信息的话咱们应该去应该去插入一条作者信息实际上啊先去查先去查
[02:23] 查完之后如果说没有咱们再去插插入一下就这么个思路咱们在这去拷贝一下咱们之前有吗好像是有的在AEP下面有一个叫什么AEP找一找啊author user author有没有user他他来试一下咱们看看啊AEP author my file是吧AEP author my file就他是吧好在这你拷贝两个方法
[02:56] 好吧然后咱们再去把当前这个mypro给拷贝一下来一个是查询一个是运赠好这个类好像有问题是吧类是叫什么来着这个类好像不在这是吧咱们去搜一下应该跟它跟它是一样的跟它是一样拷贝一下这多了个R是吧其他没有了咱们在这也把它给删了这多了一个R好这个就设置完了做完之后下面还有一个好
[03:30] AP article content那种是吧那种咱们需要去插入一条内容啊所以说你在这啊去这么个东西找到content在这呢去加一个东西然后呢你找到当前的myport去找到一个什么插入啊插入嗯好拷贝这样就可以了啊那拿到之后呢咱们再往下看啊还有啥还有一个config其实config也需要啊config也需要那咱们就
[04:02] 拿过来找到config咱们这个要去保存文章的时候你要去保存文章要config content还有他的一些用户都要去拿或者要保存好吧然后再往下这找到当前的maple好这个做完之后咱们再往下看啊还有这个文章肯定要保存呢是吧所以说你在这去拷贝一下现在文章找到文章文章咱们之前也有直接考他
[04:34] 加完之后在这去加一个语句语句层标直接ctrlc一下好这个其实就是根据当前的字段去做这个跟之前的之前的事不太一样之前的字段保存都是不太一样因为你要去保存当前比如说要保存content的时候在这说你要去保存当前config content的时候它需要拿到当前这个article id也就是当前的文章id
[05:04] 所以说咱们在这去做了一个主见的返回主见的返回你保存完当前AP article2我需要拿到你的ID然后再去保存当前config和content的内容这个能听明白吧好了行这个咱们往下看说完之后咱们再去做一个就是当前修改的这种什么WM news就是自媒体文通的一个方法我考虑一下
[05:33] 找到WM News Mapper在哪啊当前的微密地是吧然后找到他找到他好在这去加一个方法这个呢其实就是修改的方法啊好到Mapper然后是在这去加一个方法好Ctrl VCtrl V好了那这个啊这个Mapper咱们也创建完了下面还有吗
[06:01] 下面还有再往上看下面还有一个就是AP user message那这个呢咱们之前是没有的这时候咱们要去创建当前的Maple接口Maple接口有这里边那为什么要创建它呢你这里边其实刚才咱们说流程的时候就说了你需要给用户发推送消息给用户推送消息所以说咱们在这需要去用到当前的这个这个接口好吧咱们在这去创建一下打开AP user message那也可以看下这个列
[06:31] AEP user message找一找啊AEP user message有没有往后往后有它是吧那里边有一个主件是吧发送人ID还有什么下面是有一个消息的类型关注取消关注取消点赞点赞评论什么一大堆你看下面还有啊这是不是有文章的审核呀有文章审核啊你审核失败和失败和比如说
[07:03] 失败和成功咱们都应该去在这去推送一条信息给给用户这时候你也可以去设置一些内容比如说你的私信内容比如你的你的文章审核成功了或者失败了好吧行咱们在这去创建那个类啊类应该是在哪应该在APP下边啊这写错了啊VP user message当前APP目录下边去创建一个mypro接口在这去加上好好这样就可以了
[07:37] 里边是有一个方法就是新增然后呢然后在这去创建他的什么他的Mapper接口文件拷贝一份去写一下前面删掉啊什么优色麦西子没s a d e没错啊好点OK这时候呢咱们就把里边内容的删了那之后呢在这去改改啊A P U S M I C E D
[08:17] 然后呢这里边还有一个新增的方法咱们也一块考过来啊首先是Redo的Map然后下面是有一个新增好那加进来之后啊那这个内容咱们就算是加完了啊下面呢还有吗下面还暂时没有了啊这个Map咱们暂时就写到这儿后期如果说业务上需要的时候咱们可以再改或者说咱们可以再加好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

