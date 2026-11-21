# 22_app文章列表_mapper文件编写2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\22_app文章列表_mapper文件编写2【海量资源尽在 666java.com】.mp4
- 时长 11分22秒（音频 682s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好来那咱们就继续往下讲刚才咱们是把第一个mypro的这种接口这种已经写完了写完之后这块是说写错了一个东西就是写了一个authorid它不应该是authorid应该是咱们的channelid刚才拷贝错了重新拷贝一下这样就没问题了下面咱们来写第二个这种方法这个方法是干啥的你看这里边是load article list by id list
[00:30] 那list是谁呢咱们可以去打开啊打开咱们的Mapper文件Mapper介绍咱们再来看一眼啊那这里边是有一个listlist里边装的是啥呢装的是一个AP User Article List这个对应的表呢其实呢就是刚才咱们说这个用户推荐的一个列表那这里边是有某一些字段那字段里边它里边咱们需要拿到哪些信息呢咱们主要拿的呀其实应该就是当前的一个什么
[01:01] 一个是article id根据当前的article id去查询出来文章的信息对吧所以说那这个该怎么去写呢有两个问题第一个咱们是要该怎么去传参传参的话咱们就是历史集合是吧那第二个就是那就历史集合我怎么去在这儿去展示我怎么去拿到里边的article id呢大家想一想之前有没有学过便利
[01:31] 咱们还是最基本的首先写一个slack的星flum什么AP article然后是where是吧where id in是吧应该是一个in那in里边咱们就可以去在这里边去便利用哪个标签呢
[02:04] 对吧OK那collection应该是谁collection呢对应的就是咱们的变量OK那咱们这是不是起这个变量叫什么list对吧OK那他就是list然后呢咱们再去起一个变量啊叫这个名字随便起啊一个separate这是干嘛的呢这是分割符是吧我们有一条号分割那最终便利的便利出来的东西呢咱们就可以写一下啊叫item点什么article
[02:37] 是不是这个ID这个ID要给谁对应上啊当前这个表中的这个字段是不是对应上就可以了OK啊那这样的话咱们就算是写完了那写完之后啊这里边还有个问题它有可能呢咱们会多一个逗号出来有可能会多一个逗号出来那这时候呢咱们可以用当前的trim标签呢来给它处理一下怎么办呢这里有一个trim
[03:03] 然后呢咱们设置一个前缀前缀为空好吧然后过滤掉一个前缀前缀是啥呢是个逗号我们要把这个前缀的逗号给过滤掉好那这样的话呢就算说完了啊你把这个 for each 呢搞到这里边好好对那这样的话咱们就算是结束了啊这里边稍微再再改一改当前那个新啊不应该写新写啥哎写当前呢是不是要引入一个东西啊叫什么include咱们有一个 base column list好吧
[03:34] 这样的话咱们这个sql就算是写完了行那这个是关于当前的这个AP article mypro已经写完了但是咱们里边还有是不是还有另外一个mypro接口OK那这个接口咱们也需要去写一下那这个接口咱其实咱们已经准备好了打开这个modelmodel里边是不是有个resource刚才咱们是不是准备了两个是吧有一个article user
[04:04] 那这里边咱们需要去定义咱们定义之前还要再去看一下里边有什么参数那这参数首先是有一个用户还有什么还有一个DTO还有一个什么还有一个type那这个到底该怎么去定义首先咱们一会再去分析这个逻辑咱们首先把这个补全因为这个参数太多有可能你传参的时候区分清楚所以说需要在这
[04:34] 加一个pyram是吧每一个上面都加pyram啊这样的话就能区分区分到底是哪一个参数好好这是一个什么pyram嗯这是type好呃那这样就设置完之后啊下面呢咱们就把这个map文件给写一下啊还是一样的啊咱们可以从当前的这个这个笔记中啊或者讲义中把这些最基本的这种封装的咱们拷贝过来啊
[05:05] 拿过来之后咱们再说一说如果说合适的话咱们就再改一改啊行啊那这边包错了是吧包错的话很显然这个类的找不着那找不着的话怎么办呢哎找不着的话其实呢这个类呢咱们已经不在这个包下了啊所以说你把它给删了到哪啊哦嗯咱们可以在这找一找啊这里边其实在一个user里边user有一个pugus里边的这有一个ap user articlelist就它他们可以拷贝一下它的权利名哎直接拷到这就可以了
[05:39] 考虑之后里边还有一些东西就是当前的ID这里边是不是没有什么Property所以这一块那种看笔记的时候不要说只抄笔记如果说有问题的话就打给改改这是Property这是Channel1这是ArticleID然后下面的话咱们再来看一下Property然后是EaseShow还有就是EaseRead
[06:10] 这不是Ease Read是吧这是Recommend Time这是一个推荐的时间这是Ease Read还有一个是推荐的策略这样的话咱们就全了那补全之后方便你们以后去看笔记我就把这段给它拷贝替换了一下替换完之后咱们就算是做完了下面咱们就来去写咱们具体的这种MIPRO首先咱们还要在这去定一个slack的对吧slack的ID是啥呢
[06:50] 这个 id 的话就是跟当前这个方法名是一样的好放到这后呢是 result my 婆是谁呢就是当前的 base 伪造的卖跑好那这时候拿这个 circle 该怎么去写呢啊首先呢你要知道啊咱们目前所查询的 select是吧新flom谁他觉得是哪个表啊他寻的是当前的 vp 都是 article list好那放到这之后啊首先呢咱们也有 will 是吧
[07:20] 我现在有一个条件那什么条件呢那你要知道啊那这个是怎么传递过来的呢他里边是不是有个useruser是不是必然会有信息啊当然也有可能没有信息所以说这个user啊你必然得作为条件进行查询所以说呢你在这去写的时候啊首先加的第一个条件应该就是user user什么user id是吧user id等于什么呢等于警号是
[07:53] user.id有问题吧来看一眼啊打开当前的这个这个类啊你看它的这种属性是不是就id啊所以说你这要写成user.id这个user刚才说的刚才这个user啊这个user呢要跟你当前的这个user对应上那id的话就是跟当前这个类里边的属性对应上就可以了好吧
[08:21] 那行啊那这个ID做完之后呢咱们还要再去做两个东西按的什么呢其实里边有个是否展示是吧0默认就是0啊那话就是是按的什么意思readread的话也等于0它默认也是可以展示可以读所以说这个呢是必要的条件然后再往下看咱们就可以判断了哪个判断的呢首先第一个呢应该还是type
[08:50] type不等于nonetype等于1的时候咱们是不是还有一个时间的判断呢这个时间的话不是发布时间应该是啥呢应该这里边有一个叫推荐时间所以说咱们推荐时间大于还是小于呢一样的啊里边呢其实跟咱们之前是一样应该是小于
[09:18] 当前的什么最小的时间就可以啊那就跟上面是一样的啊咱们直接从这拷贝过来就可以好吧思路是一样的啊下面是等于这时候呢那正好是大于是吧好那是等于二的时候这个啊这个时间是大于对谁呢大于最大的时间好那这样的话呢我们就算是完了啊但是里边还有一个东西啊就是咱们要去设置一个你看这里边是里面是不是有一个channel id呀
[09:49] 那咱们传参数的时候DTO里边有没有封装这个tag呢很显然是不是有可能会存在呀是吧你可以看这里边是不是有可能会有当前的拆弄ID呀所以说呢我们在这啊也应当去把它作为条件自己判断一下所以说咱们再去拷贝一个if那这个呢就是DTO.tagtag是等于谁呢等于谁呀怎么写的还知道吧刚刚
[10:24] 这边是不是做了个标识这时候这个应该是Tino IDTino ID等于是当前的Tag等号大括号是吧关服DTO打什么Tag这样的话咱们就算是说完了这里边好像有点问题是吧有什么问题吗感觉这里边是不是应该加一个按钮这里边应该都是要加一个按钮
[11:01] 按着之后这里边千万还要再往上另外最后一个是就是Limit应该是设置一个条数因为咱们这个TO里边它有一个Size的标签那目前的话这个咱们就算是写完了所有的Map我念的都写完了下面咱们就来测一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

