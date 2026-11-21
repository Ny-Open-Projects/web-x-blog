# 画面线理解：28_用户行为功能_mapper映射文件编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\28_用户行为功能_mapper映射文件编写【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 01:06, 02:40, 03:08, 04:13, 05:30, 06:43, 07:22, 08:29, 10:02, 10:49, 11:32, 12:20, 13:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:44:52

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 MyBatis 实现用户行为（点赞、浏览）的持久化操作，包括 Service 层逻辑、Mapper 接口定义和 XML 映射文件的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 AppShowBehaviorServiceImpl.java 中的 saveShowBehavior 方法，用于处理用户行为保存逻辑，包含参数校验和调用 Mapper。
画面 2: 展示 ApShowBehaviorMapper.java 接口，定义了 selectListByEntryIdAndArticleIds 和 saveShowBehavior 方法。
画面 3: 展示 ApShowBehaviorMapper.xml 文件中定义的 Base_Column_list 结果映射和 loadArticleListByLocation 查询。
画面 4: 展示 ApShowBehaviorMapper.xml 文件中定义的 Base_Column_list 结果映射和 selectListByEntryIdAndArticleIds 查询。
画面 5: 展示 ApShowBehaviorMapper.xml 文件中定义的 BaseResultMap 结果映射和 Base_Column_list 查询。
画面 6: 展示 ApShowBehavior.java 实体类，包含 id, entryId, articleId, isClick, showTime, createdTime 等字段。
画面 7: 展示 ApShowBehaviorMapper.xml 文件中定义的 selectListByEntryIdAndArticleIds 查询，使用了 foreach 标签。
画面 8: 展示 ApShowBehaviorMapper.xml 文件中定义的 selectListByEntryIdAndArticleIds 查询和 saveShowBehavior 插入语句。
画面 9: 展示 ApShowBehaviorMapper.java 接口，定义了 saveShowBehavior 方法。
画面 10: 展示 PPT 页面，标题为“7.3.4 行为相关开发”，内容包括 ApBehaviorEntryMapper 接口定义。
画面 11: 展示 ApBehaviorEntryMapper.xml 文件中定义的 Base_Column_list 查询。
画面 12: 展示 ApBehaviorEntryMapper.java 接口，定义了 selectByIdUserEquipment 方法。
画面 13: 展示 ApBehaviorEntryMapper.xml 文件中定义的 selectByIdUserEquipmentId 查询，使用了 if 标签进行条件判断。
画面 14: 展示 ApBehaviorEntryMapper.xml 文件中定义的 selectByIdUserEquipmentId 查询，使用了 if 标签进行条件判断。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
private ApBehaviorEntryMapper apBehaviorEntryMapper;
private ApShowBehaviorMapper apShowBehaviorMapper;

@Override
public ResponseResult saveShowBehavior(ShowBehaviorDto dto) {
    //获取用户信息，获取设备id
    ApUser user = ApThreadLocalUtils.getUser();
    //根据当前用户信息设置设备行为表 ap_behavior_entry
    if (user == null || dto.getEquipmentId() == null) {
        return ResponseResult.errorResult(AppTpCodeEnum.PARAM_REQUIRE);
    }
    Long userId = null;
    //...
}
```

画面 2:
```java
package com.heima.model.behavior.mappers.app;

import com.heima.model.behavior.pojos.ApShowBehavior;
import org.apache.ibatis.annotations.Param;
import java.util.List;

public interface ApShowBehaviorMapper {
    List<ApShowBehavior> selectListByEntryIdAndArticleIds(@Param("entryId") Integer id, @Param("articleIds") Integer[] articleIds);
    void saveShowBehavior(@Param("articleIds") Integer[] articleIds, @Param("entryId") Integer entryId);
}
```

画面 3:
```xml
<resultMap id="Base_Column_list" type="com.heima.model.behavior.pojos.ApShowBehavior">
    result column="views" property="views"
    result column="province_id" property="provinceId"
    result column="city_id" property="cityId"
    result column="county_id" property="countyId"
    result column="created_time" property="createdTime"
    result column="publish_time" property="publishTime"
    result column="sync_status" property="syncStatus"
</resultMap>

<sql id="Base_Column_list">
    id, title, author_id, author_name, channel_id, channel_name, layout, flag, images,
    labels, collection, comment, views, province_id, city_id, county_id, created_time,
    publish_time, sync_status
</sql>

<select id="loadArticleListByLocation" resultMap="resultMap">
    select <include refid="Base_Column_list"/>
    from ap_article aa
</select>
```

画面 4:
```xml
<resultMap id="Base_Column_list" type="com.heima.model.behavior.pojos.ApShowBehavior">
    result column="title" property="title"
    result column="author_id" property="authorId"
    result column="channel_id" property="channelId"
    result column="channel_name" property="channelName"
    result column="layout" property="layout"
    result column="flag" property="flag"
    result column="images" property="images"
    result column="labels" property="labels"
    result column="likes" property="likes"
    result column="collection" property="collection"
    result column="comment" property="comment"
    result column="views" property="views"
    result column="province_id" property="provinceId"
    result column="city_id" property="cityId"
    result column="county_id" property="countyId"
    result column="created_time" property="createdTime"
    result column="publish_time" property="publishTime"
    result column="sync_status" property="syncStatus"
</resultMap>

<sql id="Base_Column_list">
    id, title, author_id, author_name, channel_id, channel_name, layout, flag, images,
    labels, collection, comment, views, province_id, city_id, county_id, created_time,
    publish_time, sync_status
</sql>
```

画面 5:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.heima.model.behavior.mappers.app.ApShowBehaviorMapper">
    <resultMap id="BaseResultMap" type="com.heima.model.behavior.pojos.ApShowBehavior">
        <id column="id" property="id"/>
        <result column="entry_id" property="entryId"/>
        <result column="article_id" property="articleId"/>
        <result column="is_click" property="isClick"/>
        <result column="show_time" property="showTime"/>
        <result column="created_time" property="createdTime"/>
    </resultMap>

    <sql id="Base_Column_List">
        id, entry_id, article_id, is_click, show_time, created_time
    </sql>
</mapper>
```

画面 6:
```java
package com.heima.model.behavior.pojos;

import java.util.Date;

@Data
public class ApShowBehavior {
    private Integer id;
    private Integer entryId;
    private Integer articleId;
    private Boolean isClick;
    private Date showTime;
    private Date createdTime;
}
```

画面 7:
```xml
<resultMap id="BaseResultMap" type="com.heima.model.behavior.pojos.ApShowBehavior">
    <id column="id" property="id"/>
    <result column="entry_id" property="entryId"/>
    <result column="article_id" property="articleId"/>
    <result column="is_click" property="isClick"/>
    <result column="show_time" property="showTime"/>
    <result column="created_time" property="createdTime"/>
</resultMap>

<sql id="Base_Column_List">
    id, entry_id, article_id, is_click, show_time, created_time
</sql>

<select id="selectListByEntryIdAndArticleIds" resultMap="BaseResultMap">
    select
    from ap_show_behavior
    where entry_id = #{entryId} and article_id in
    <foreach collection="articleIds" item="item" separator=",">
        #{item}
    </foreach>
</select>
```

画面 8:
```xml
<resultMap id="BaseResultMap" type="com.heima.model.behavior.pojos.ApShowBehavior">
    <id column="id" property="id"/>
    <result column="entry_id" property="entryId"/>
    <result column="article_id" property="articleId"/>
    <result column="is_click" property="isClick"/>
    <result column="show_time" property="showTime"/>
    <result column="created_time" property="createdTime"/>
</resultMap>

<sql id="Base_Column_List">
    id, entry_id, article_id, is_click, show_time, created_time
</sql>

<select id="selectListByEntryIdAndArticleIds" resultMap="BaseResultMap">
    select
    from ap_show_behavior
    where entry_id = #{entryId} and article_id in
    <foreach collection="articleIds" item="item" separator=",">
        #{item}
    </foreach>
</select>

<insert id="saveShowBehavior">
    insert into ap_show_behavior (entry_id, article_id, is_click, show_time, created_time)
    values
    <foreach collection="articleIds" item="item
