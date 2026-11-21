# 13_app文章详情_文章关系接口_mapper定义

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\13_app文章详情_文章关系接口_mapper定义【海量资源尽在 666java.com】.mp4
- 时长 14分13秒（音频 853s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就继续往下讲刚才咱们是把这个思路给说了一下其实这个思路呢还是一个大体的思路咱们后期再去写MIPR文件的时候咱们马上写MIPR文件啊写MIPR文件的时候呢咱们还会再去加一些小小的逻辑因为它每个表查询的方式是有所不同的那好啊那咱们接下来就去编写当前的MIPR接口刚才说了一共是几个表吧六个表咱们需要去写六个MIPR接口
[00:28] 那其中有一个啊就是第一个就是根据当前的什么设备ID和用户ID查看行为实体那这个在第一天咱们已经做完了所以说咱们还有五个需要完成好吧那行那咱们就来看笔记来一块去写啊首先第一个啊就是行为实体这边查询那你通过当前的用户ID或者是当前的设备去查询的时候咱们已经有了啊就是根据当前这个东西那这个呢是跟之前的第一天不太一样
[00:59] 因为这个咱们需要去通过当前的一个Boss去查询所以说Map文件里边需要去稍微的改动一下就把这个东西直接拷过来就可以了因为它这个无非就是说你需要去看UserID如果说它不会空就按运输查如果说运输ID并且运输ID等于空并且它设备ID不等于空的时候咱们要去按照设备去查就是两个条件所以说你把它可以拷贝一下
[01:29] 往哪呢找到当前的麦克麦克在哪知道吧嗨麦克是在当前的麦克斯有一个他然后是找到当前的嗯他叫ap behavior然后是entry然后你找一下你看我这块已经改过来了已经改过来了一个是按照用户场一个是按照设备场好这第一个麦克咱们就做完了行咱们继续往下看咱们写第二个第二个就是收藏收藏的话刚才说了大体的思路是啥呢
[01:59] 大体的思路是需要去通过当前的entry ID和什么article ID去查询就可以了所以说咱们再去写mypl文件的时候来看一看这是它的一个实体列实体列里边其实咱们目前所需要知道的其实就两个字段第一个是当前的entry ID然后第二个是这个entry ID其实不是咱们可以看一下表这个entry ID应该是当前的一个什么东西看看
[02:28] 应该是文章ID这个定义的是有问题但是你要知道它是一个文章ID比如说通过这两个字段需要去查询当前的这种收藏表好那咱们定义的时候咱们可以看一下往下去看Maple好那这个其实就是当前的一个东西一个东西首先这里边还有一个需要去说明一下就是这有一个Boss因为咱们现在查询
[02:53] 到底是去哪个分片上去查询所以说呢这块内容呢咱们需要去加一个Burst那这个怎么传咱们后期咱们一会儿就调用Service Service调用的时候咱们再去讲好吧这里面还有一个type啊那type是啥呢type的话其实咱们可以看这个表这里边说了啊你type的话就是说明你是文章文章的收藏还是动态的收藏
[03:18] 有动态信息还有文章信息其实咱们绝大部分都是文章信息那好啊那这个你知道一下所以说咱们在这写的时候应该是传了四个字段传四个字段那这时候咱们需要去把当前的这个mypros接口给创建一下还是在当前的mypros里边有一个APP然后直接去拷贝一下就可以了
[03:41] 拷贝完之后呢那这块内容报错没有事啊因为咱们现在还缺少mypro文件但这块呢大家知道啊目前的话是有四个参数那四个参数有可能mypro文件是区分不了的那怎么办呢在这是不是在加注解叫什么注解一个是吧然后呢咱们就去写一下去分一下防止报错好往后往后我看看啊还有一个然后分别咱们去拷贝一下这是
[04:16] 这是entry id然后下面是type好那这样就说说这完了啊下面呢咱们再去拷贝一个mypro文件好吧然后这个文件就叫做啥呢就叫做ap collection好那这样的话mypro文件定义完了定义完之后呢咱们把这个东西给删了啊这个叫啥呢好ap collection好关于这个mypro文件咱们也拷贝过来啊
[04:50] 里边是有一个伪造的麦普和一个查询咱们搞怪之后咱们再讲一讲好你看首先咱们这是当前的一个映射是吧这段的映射然后这是一个搜索的片段然后咱们去查询查询的条件其实有三个是吧当前的NHID和一个这个NHID是一个什么是一个刚才说了是一个ArticleID然后还有根据当前的类型好了这里边还有东西
[05:20] 这里边还有一个就是当前的一个burst因为它需要去按照某一个分片去查询看当前这条数据到底是在哪一个分片上面这样查询效率会比较快一些如果说您不加它的话呢它就会查询所有的库然后是把这条数据给查出来那这样的话性能可能会比较慢所以说这个咱们要加上啊这个咱们在昨天已经讲完了好吧行啊那这个咱们这个当前这个收藏这个mypr文件咱们就说这完了啊
[05:49] 然后继续往下看啊继续往下看然后下面咱们要去设置另外一个就是当前的关注表那这关注刚才其实咱们也分析了啊关注的话呢咱们主要是根据当前的用户ID和作者的账号ID去查询对吧所以说呢咱们来看一下这个Maple啊那这个Maple呢其实它是有几个呀有两个一个是User ID一个是Fraud ID这个Fraud ID其实就是说的当前的作者的APP账号ID
[06:20] OK啊那这个是个Boss也是为了方便去能够区分哪个分片上去查询所以说咱们再把这个接口给定义一下好直接考到这就可以了啊考过来之后呢咱们再去创建一个Map好拷贝一份这识叫什么看一下啊叫userflow好然后呢咱们点OK然后把这个东西给删了这去写什么呢jp userflow map好把这后边删了啊
[06:55] 然后咱们就把当前的这种硬设文件也拷过来好拷过来之后咱们也可以简单看一下前面这也是硬设是吧我就不再一说了这是它的字段然后下面这个就是根据当前的一个user id和当前的float id这个float id刚才说了就是指的当前什么当前的什么
[07:22] 看这啊这有一个登录人啊作者的APP账号ID去查询对吧所以啊所以说呢这两个大家一定要区分清楚Boss啊还是过滤当前某一个分片OK啊那这当前的当前的这个什么呃算是关注表啊咱们也说完了啊然后下面还有一个啊咱们再去网上社就是不就是喜欢就是点赞啊那点赞的话呢其实也是差不多啊点赞也差不多啊
[07:51] 点赞的话呢,打开当前的这个这块它是不是也是通过什么通过一个entry ID和什么article ID去查询的OK啊所以说这块呢内容呢咱们去设置的时候也是一样啊也是一个什么object IDentry ID啊还有什么呢还有一个type,那type是啥呢这个type你可以看一下啊这个type的话其实打开当前的lagslags啊嗯是lags吗我看看啊啊是lags啊
[08:22] 那这块内容呢你看有一个什么呢有一个点赞和一个取消点赞当然你最主要的条件应该是一个实体一个是文章ID一个实体ID一个文章ID然后呢再去根据当前的是到底是点赞呢还是取消点赞去做了一个标识0就是点赞1就是取消点赞所以说咱们也要根据当前这个去查询这有三个条件啊实体ID文章ID和点赞是否点赞好那这个咱们也考过来啊
[08:50] 就是当前的这东西好直接拷贝这就可以了然后把它拷到这拷到这之后咱们还要再去创建一个Map文件LexCover好然后点OK然后咱们就把它给删了删了之后改一改一定要改不改的话它就报错了AP LexCover Map好然后剩下的Map文件咱们也拷过来Map文件咱们再讲一讲
[09:32] 因为这个东西啊就是没有什么技术含量啊所以说你写的时候其实也是大量重复浪费时间是吧所以说这一块啊统一都考过来大家呢是一定要注意听啊你跟跟跟住当前的那个思路啊行那这个还是应之后就不再去说了啊就是根据当前的某一个表的字段是吧然后下面还有就是当前你要去查询Lex啊需要有三个材数第一个当前的实体ID第二个是当前的
[09:58] 文章外底第三个是它的一个type到底是点赞还是取消点赞而你查询的时候应该是要去根据分片去查询好吧行当前的likes咱们也做完了然后再往下看这还有一个不喜欢不喜欢的话其实也是一样咱们可以看下这思路不喜欢是不是也是这不喜欢是不是也通过这两个字段去查询好咱们来看一看往下走
[10:29] 其实他也是根据这两个字段去查询所以说咱们去拷贝一下好多了之后咱们再去拷贝一个当前的mybar然后是这是好这个不太合适是吧拷这个likes这样稍改少一点好这是unlike前面去加一个可以了好点ok检查院好没有问题点ok上面东西咱们还要去删掉删掉
[11:05] 然后这是加一个安就可以了加上之后呢你看哎找着吗我再去设置一下啊好没问题啊那可能还是写错了啊等到这个加上加上之后呢我可以看这个这个这个能找着能找着啊好这样之后咱们再去拷贝一下啊把这个东西再考考过来然后是麦普他麦普不要啊只要主要在麦普里麦普里边就可以了
[11:44] 好考过来之后呢咱们可以看一下它就有两个条件一个是当前的intra id和一个article id没了啊就两个条件然后最终是查询这个数据就可以了啊那这个为什么没有呢啥呢这个为什么没有当前的burst呢其实呢你还可以去查看当前咱们一开始啊一开始去说当前的一个什么东西的时候接口接口定义然后是一个路由定义啊打开路由定义好往下走往下找一找啊
[12:17] 你看他这个呢其实并没有干嘛的其实并没有去分表因为这个不喜欢还是比较少的相对啊相对比较少所以说呢这个东西呢咱们只设了一个节点只设了一个节点啊所以说你查询的时候不需要去再去根据当前的Burst去查询了好吧行啊那这个咱们设完之后啊咱们还有一个啊还有最后一个咱们再来看一下啊就是Service上面有一个咱们有一个author
[12:44] 一个author需要去通过author去查询这个author id其实都是在哪在哪在哪在哪是不是都是从前台传递过来的一个作者id咱们需要去通过作者id去查询他的user id其实咱们去查询他的一个信息就可以了因为里边包含了用户id
[13:06] 所以说咱们再去设置一个麦芙这个麦芙的话其实就是只需要根据某一个ID去查询当前的author信息就可以了好这是一个麦芙再考过来考过来之后咱们再去改一个随便改一个吧然后这是AP author是吧然后点OK这改一改AP au好
[13:41] 然后把里边内容删了啊这个大家改的时候一定要细心啊不要弄乱了啊然后再往下看啊这是一个resultmap好把它给拷过来好这是映射是吧然后下面这是要去通过当前的一个ID去查询前的一条信息啊一条信息啊行那这个呢吧map呢咱们就算是写完了啊map写完了下面呢咱们就来去写当前的Service那这个逻辑啊主要是根据这个逻辑去
[14:10] 世界单位检查服务

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

