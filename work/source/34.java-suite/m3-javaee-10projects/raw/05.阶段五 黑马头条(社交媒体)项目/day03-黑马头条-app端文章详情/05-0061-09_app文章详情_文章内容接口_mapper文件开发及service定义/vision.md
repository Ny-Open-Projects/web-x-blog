# 画面线理解：09_app文章详情_文章内容接口_mapper文件开发及service定义

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\09_app文章详情_文章内容接口_mapper文件开发及service定义【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 02:06, 02:57, 03:35, 04:15, 04:49, 05:13, 05:52, 06:17, 06:44, 07:14, 07:35, 08:33, 09:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:11:08

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
<mapper namespace="com.heima.model.mappers.app.ApArticleContentMapper">
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
</mapper>
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
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.heima.model.mappers.app.ApArticleContentMapper">
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
</mapper>
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
package com.heima.article.service.impl;
import com.heima.article.service.AppArticleInfoService;
import com.heima.model.common
