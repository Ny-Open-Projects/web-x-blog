# 09_app文章详情_文章内容接口_mapper文件开发及service定义

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\09_app文章详情_文章内容接口_mapper文件开发及service定义【海量资源尽在 666java.com】.mp4
- 时长 9分54秒（音频 594s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们下面呢就来去开发第一个接口就是文章内容的接口那内容接口里边呢咱们先来看一下这个基本定义啊基本定义里边呢咱们来打个截图来看一下啊首先呢是有一个接口的名称是吧是需要有一个这样的一个地址去请求然后第二个呢是有一个articleinfo的dto啊这个里边很显然封装的是啥呢封装的是不是咱们的条件呢
[00:27] 那我现在又想问一下目前比如说我想要去查看某一个文章详细信息那这时候它的条件是啥呢是不是就是就应该是当前的一个文章的ID啊对没错啊就是一个文章的ID通过文章ID去查看文章的详细信息但最终返回的时候咱们要返回啥呢返回的是两块内容啊第一个呢是config就是当前文章的配置信息
[00:54] 第二个是content是有一个文章的详细信息好这里边还有一个注意事项说如果文章已经删除content的属性将不返回那这个删除是否删除当点判断呢就是有一个AP article config咱们目前呢咱们现在可以去查看一下当前的这两张表这表呢可以看一下首先第一个是APAP article config来找一找当前就是它
[01:24] 因为这块呢是有一个article id是吧然后是是否可评论是否转发是否下架最后一个叫是否已删除咱们要把这个作为条件去查还有一个就是ap article content那这里边呢是有一个文章id并且是有一个文章的内容啊它是一个大文本的内容啊大文本用这个内容一般会比较多是吧行啊那这个呢就是就是这目前的两张表
[01:53] 行那咱们继续看文档看文档啊那首先呢咱们是从Maple接口开发那咱们目前的话呢需要去针对于这两张表去写两个Maple那这样啊咱们以后在开发过程中呢这个Maple文件呢咱们就不再去手写了直接在当前的这个笔记中或者叫文档中去拷贝因为这个内容呢应该是比较简单的并且呢没有记录含量
[02:21] 讲到一具体业务的时候咱们再去写好吧嗯行那咱们一步步去做啊首先呢这是有一个AP article content就是说咱们一个文章内容的一个这种POGO啊这个类呢其实咱们已经有了啊你可以去找一找点找啊是不是在当在咱们的一个类啊找到咱们类里边啊在你的模块中模块啊model然后找到当前的article
[02:51] Article里有个PoJuS里边有个APArticleContent和Config这两个其实都已经有了刚才看到表所对应的字段是一样的好吧那行这个咱们有了下面咱们就要去创建这个MIPRO那APArticleContentMIPRO这个是不是没有我给你看在当前的MIPRO私下边有个APP里边有一个APArticleContentMIPRO这是一个接口它的条件它的
[03:20] 方法就是根据当前当前的article id去查询当前的内容我看这个还是比较简单的现在咱们直接拷贝一下它在当前的mypros文件mypros文件夹下边mypros app里边你直接去拷贝一下就可以了背完之后这个其实就创建出来了就是一个接口是吧然后当前的就叫ap article content mypros然后是有个方法根据文章id去查询当前一个
[03:51] content内容那好啊那这个MAP文件其实也比较简单咱们可以看一下啊MAP文件的话呢你看咱们可以先分析一下啊首先呢这里边是有一个slack的方法那就是根据当前的article.it去返回就可以了返回两部分第一个是这两个字段是吧一个是it article和一个content那上面这个rebase without map呢其实就是针对于各个字段的进行映射的配置
[04:19] 好吧行那咱们来去一块写一下啊那这个写的过程呢我就不再去写了咱们直接主要主要是拷贝拷贝完之后呢你得去保证他不会出错啊好在这去写拷贝一下这名名称是啥呢名称应该跟上面的名称是一样是吧VP article什么然后是mypro.charmow是吧没问题啊好把里边内容给他删掉咱们就不要了啊这个呢需要去改一改要去改一改啊啥呢叫
[04:55] compent myport然后呢你可以从笔记中跑过来你可以手写啊我就考过来了啊好那考过来之后呢还要再去说一下啊就是前这块是一个映射是吧然后下面是留两个circle的片段是包含了某些字段然后最终呢咱是根据当前的某一个文章ID去查询当前的文章信息完事好吧行那这个啊咱们就算是做完了
[05:25] 然后这个mypro其实还有一个是吧是两个是吧这是刚才说的是content还有一个config其实config是一样的因为它也是通过当前的一个什么article id去查询就可以了当然当然当然这个东西咱们已经有了下面咱们就来去定义这个mypro这个mypro的话其实是一样也是拷贝一下它它也是根据当前的article id去返回当前pp article什么config好还是找到当前的什么哪个
[05:55] 哪个目录啊myporsche是吧myporsche下面有个app然后直接ctrl v一下这时候就考进来了啊回来之后呢你可以稍微改一改啊把它给ctrl c一下然后是ctrl v一下然后这个东西叫什么又不是content了叫什么config啊ok然后这里边内容咱们还要去删啊因为每一个myporsche文件它是都不一样啊所以说这是改了叫config myporsche
[06:25] 这个内容呢你也可以去拷贝过来啊好来看一看这他也是做了一个映射然后是做了一个查询好那这个拷贝过来之后呢那这个是没有问题的啊那这个呢其实mypro呢也算是做完了然后继续往下看啊下面咱们要去定义Service那Service里边呢其实就是要去通过当前的article id是吧去查询就可以了但最终呢咱们接口返回的时候都是一个respawns result但是respawns result里边应该
[06:59] 包含了哪些内容呢咱们是不是在技术定义里边已经说了在这里边是不是要包含哪个来看我来看啊是不是有一个config和一个什么content的内容啊所以说啊咱们来去定义一下当前的Service那这个Service在哪定义呢应该是在哪个模块下边啊是不是在文章的这块内容啊好咱们把这个东西考一下在咱们的当前article为服务里边啊Service
[07:33] 好右键创建创建一个类叫什么叫APArticleInfoService这是一个接口写错了好这是个接口我现在这里边是有一个方法那方法呢主要呢就是要去当前的一个ArticleID去查询就可以了就是来设想getArticleInfoPublic叫responseResult然后是getArticleInfo然后里边是什么他说一个integer呢
[08:10] Article ID是吧好这个呢其实就是加载文章内容啊加载文章详情好那这个完了下面咱们就来去写它的实现类来打开在这就创建一个啊咱们可以考下这东西然后是加一个安排就可以了啊好来放进一个类啊这是一个类啊然后是IMDL好OK然后这时候呢让他去实现谁呀
[08:43] 实现咱们刚才定义的当前的一个Service对吧好然后去实现他所有的方法目前只有一个啊然后加一个Service注解就是说让子润去管理目前的这个类目前的话呢这个东西咱们就先试到这那这个思路是啥呢可以说一下当前实现的一个思路思路呢其实就两步对吧两步啊首先呢咱们要根据什么呢根据文章
[09:14] ID查询查询什么Config信息查询Config的信息然后呢判断当前文章是否删除如果说没有删除怎么办有删除就该怎么办是吧刚才咱们也说了啊这块如果说删除的话那你说content内容还用返回吗
[09:46] 就不需要返回了是吧行那咱们一会呢就把这一步啊把这两步给实现一下好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解文章内容接口的实现，包括POJO类、Mapper映射文件、Service层代码的编写与配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文章内容接口定义，包含接口路径、请求体、响应体等信息，提及使用Map进行分列，以及错误码PARAM_INVALID。
画面2：展示Mapper实现部分，创建ApArticleContent类，使用Lombok注解，以及创建ApArticleContentMapper接口。
画面3：展示ApArticleConfig类的代码，包含id、articleId、isComment、isForward、isDown等字段。
画面4：展示ApArticleContent类的代码，包含id、articleId、content字段。
画面5：展示ApArticleContentMapper.xml文件的SQL语句，包含resultMap、sql、select等标签。
画面6：展示ApArticleContentMapper.xml文件的SQL语句，包含trim、foreach等标签。
画面7：展示ApArticleContentMapper.xml文件的SQL语句，包含resultMap、sql、select等标签。
画面8：展示ApArticleContentMapper.xml文件的SQL语句，包含resultMap、sql、select等标签。
画面9：展示ApArticleConfigMapper.xml文件的SQL语句，包含resultMap、sql、select等标签。
画面10：展示ApArticleConfigMapper.xml文件的SQL语句，包含resultMap、sql、select等标签。
画面11：展示ApArticleConfigMapper.xml文件的SQL语句，包含resultMap、sql、select等标签。
画面12：展示创建ApArticleConfigMapper.xml文件的菜单操作。
画面13：展示AppArticleInfoService接口的代码，包含getArticleInfo方法。
画面14：展示AppArticleInfoServiceImpl类的代码，包含getArticleInfo方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
请求体
com.heima.model.article.dtos.ArticleInfoDto
响应体
使用Map进行分列，其中格式如下：（"config"//ApArticleConfig
"content"//ApArticleContent）注意：如果文章已经存在，content属性将不返回
```
画面2：
```
@Data
public class ApArticleContent {
    private Integer id;
    // 增加注解，jsontype对字段自动加密
    @IdEncrypt
    private Integer articleId;
    private String content;
}
```
画面3：
```
public class ApArticleConfig {
    private Long id;
    // 增加注解，jsontype对字段自动加密
    @IdEncrypt
    private Integer articleId;
    private Boolean isComment;
    private Boolean isForward;
    private Boolean isDown;
}
```
画面4：
```
public class ApArticleContent {
    private Integer id;
    // 增加注解，jsontype对字段自动加密
    @IdEncrypt
    private Integer articleId;
    private String content;
}
```
画面5：
```
<Mapper namespace="com.heima.model.mappers.app.ApArticleContentMapper">
    <resultMap id="BaseResultMap" type="com.heima.model.article.pojos.ApArticleContent">
        <id column="id" property="id"/>
        <result column="content" property="content"/>
    </resultMap>
    <sql id="Base_Column_List">
        id, article_id
    </sql>
    <sql id="Blob_Column_List">
        content
    </sql>
    <select id="selectByArticleId" resultMap="BaseResultMap" parameterType="java.lang.Integer">
        select
        <include refid="Base_Column_List"/>
        <include refid="Blob_Column_List"/>
        from ap_article_content
        where article_id = #{articleId}
    </select>
</Mapper>
```
画面6：
```
<trim suffixOverrides="," prefixOverrides="," prefix="select * from ap_article_content where article_id = #{articleId} and">
    <foreach collection="list" item="item" separator=",">
        <if test="item.id != null">id = #{item.id}</if>
        <if test="item.articleId != null">article_id = #{item.articleId}</if>
        <if test="item.isComment != null">is_comment = #{item.isComment}</if>
        <if test="item.isForward != null">is_forward = #{item.isForward}</if>
        <if test="item.isDown != null">is_down = #{item.isDown}</if>
        <if test="item.isDelete != null">is_delete = #{item.isDelete}</if>
    </foreach>
</trim>
```
画面7：
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0.0//EN" "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
<Mapper namespace="com.heima.model.mappers.app.ApArticleContentMapper">
    <resultMap id="BaseResultMap" type="com.heima.model.article.pojos.ApArticleContent">
        <id column="id" property="id"/>
        <result column="content" property="content"/>
    </resultMap>
    <sql id="Base_Column_List">
        id, article_id
    </sql>
    <sql id="Blob_Column_List">
        content
    </sql>
    <select id="selectByArticleId" resultMap="BaseResultMap" parameterType="java.lang.Integer">
        select
        <include refid="Base_Column_List"/>
        <include refid="Blob_Column_List"/>
        from ap_article_content
        where article_id = #{articleId}
    </select>
</Mapper>
```
画面8：
```
<resultMap id="BaseResultMap" type="com.heima.model.article.pojos.ApArticleContent">
    <id column="id" property="id"/>
    <result column="content" property="content"/>
</resultMap>
<sql id="Base_Column_List">
    id, article_id
</sql>
<sql id="Blob_Column_List">
    content
</sql>
<select id="selectByArticleId" resultMap="BaseResultMap" parameterType="java.lang.Integer">
    select
    <include refid="Base_Column_List"/>
    <include refid="Blob_Column_List"/>
    from ap_article_content
    where article_id = #{articleId}
</select>
```
画面9：
```
<resultMap id="BaseResultMap" type="com.heima.model.article.pojos.ApArticleConfig">
    <id column="id" property="id"/>
    <result column="article_id" property="articleId"/>
    <result column="is_comment" property="isComment"/>
    <result column="is_forward" property="isForward"/>
    <result column="is_down" property="isDown"/>
    <result column="is_delete" property="isDelete"/>
</resultMap>
<sql id="Base_Column_List">
    id, article_id, is_comment, is_forward, is_down, is_delete
</sql>
<select id="selectByArticleId" resultMap="BaseResultMap" parameterType="int">
    select
    <include refid="Base_Column_List"/>
    from ap_article_config
    where article_id = #{articleId}
</select>
```
画面10：
```
<resultMap id="BaseResultMap" type="com.heima.model.article.pojos.ApArticleConfig">
    <id column="id" property="id"/>
    <result column="article_id" property="articleId"/>
    <result column="is_comment" property="isComment"/>
    <result column="is_forward" property="isForward"/>
    <result column="is_down" property="isDown"/>
    <result column="is_delete" property="isDelete"/>
</resultMap>
<sql id="Base_Column_List">
    id, article_id, is_comment, is_forward, is_down, is_delete
</sql>
<select id="selectByArticleId" resultMap="BaseResultMap" parameterType="int">
    select
    <include refid="Base_Column_List"/>
    from ap_article_config
    where article_id = #{articleId}
</select>
```
画面11：
```
<resultMap id="BaseResultMap" type="com.heima.model.article.pojos.ApArticleConfig">
    <id column="id" property="id"/>
    <result column="article_id" property="articleId"/>
    <result column="is_comment" property="isComment"/>
    <result column="is_forward" property="isForward"/>
    <result column="is_down" property="isDown"/>
    <result column="is_delete" property="isDelete"/>
</resultMap>
<sql id="Base_Column_List">
    id, article_id, is_comment, is_forward, is_down, is_delete
</sql>
<select id="selectByArticleId" resultMap="BaseResultMap" parameterType="int">
    select
    <include refid="Base_Column_List"/>
    from ap_article_config
    where article_id = #{articleId}
</select>
```
画面12：
```
创建文件resources/mappers/app/ApArticleConfigMapper.xml
```
画面13：
```
interface AppArticleInfoService {
    ResponseResult getArticleInfo(Integer articleId);
}
```
画面14：
```
package com.heima.article.Service.impl;
import com.heima.article.Service.AppArticleInfoService;
import com.heima.model.common

