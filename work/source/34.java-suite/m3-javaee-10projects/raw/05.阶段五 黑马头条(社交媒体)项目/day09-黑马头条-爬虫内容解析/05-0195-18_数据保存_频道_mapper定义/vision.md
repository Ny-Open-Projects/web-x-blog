# 画面线理解：18_数据保存_频道_mapper定义

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\18_数据保存_频道_mapper定义【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:19, 00:48, 01:12, 01:41, 02:02, 02:26, 02:39, 02:50, 03:26, 03:48, 04:00, 04:15, 04:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:55:11

1) 这一组画面整体在讲什么（一句话）：
演示如何为广告标签（AdLabel）和广告频道标签（AdChannelLabel）实体类定义 MyBatis Mapper 接口及对应的 XML 映射文件，包括 CRUD 操作和条件查询。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 AdLabel 和 AdChannelLabel 实体类的 Java 代码，位于 `com.heima.model.admin.pojos` 包下，包含 id、name、type、createdTime、channelId、ord 等字段。
画面 2: 展示了 AdLabelMapper 和 AdChannelLabelMapper 接口的定义，包含 deleteByPrimaryKey、insert、insertSelective、selectByPrimaryKey、updateByPrimaryKeySelective、updateByPrimaryKey 等方法。
画面 3: 在 IntelliJ IDEA 中展示了项目结构，重点是 `mappers/admin` 目录下的 Mapper 接口文件。
画面 4: 展示了 AdLabelMapper.xml 的 XML 配置文件开头部分，定义了命名空间和基础 resultMap。
画面 5: 展示了 AdChannelLabelMapper.java 文件中的 selectById 方法，注释为“根据 labelId 查询”。
画面 6: 在 IntelliJ IDEA 中展示了 AdChannelLabelMapper.java 文件，光标位于 selectById 方法的参数 id 上。
画面 7: 在 IntelliJ IDEA 中展示了项目结构，选中了 AdChannelLabelMapper.xml 文件。
画面 8: 展示了 AdLabelMapper.xml 文件中的 selectById、deleteByPrimaryKey、insert、insertSelective、updateByPrimaryKey 等 SQL 映射语句。
画面 9: 展示了 AdLabelMapper.xml 文件中的 updateByPrimaryKeySelective 和 updateByPrimaryKey 语句。
画面 10: 展示了 AdLabelMapper.xml 文件中的 resultMap 和 selectById、queryAdLabelByLabels、queryAdLabelByLabelIds 等 SQL 映射语句。
画面 11: 展示了 AdLabelMapper.xml 文件中的 queryAdLabelByLabelIds 语句，包含 foreach 循环。
画面 12: 在 IntelliJ IDEA 中展示了项目结构，选中了 AdChannelLabelMapper.xml 文件。
画面 13: 展示了 AdChannelLabelMapper.xml 文件中的 insertSelective 语句，包含 trim 和 if 条件判断。
画面 14: 展示了 AdChannelLabelMapper.xml 文件中的 selectById 和 selectByLabelId 语句，包含 resultMap 和 select 语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public class AdLabel {
    private Integer id;
    private String name;
    private Boolean type;
    private Date createdTime;
}

public class AdChannelLabel {
    private Integer id;
    private Integer channelId;
    private Integer labelId;
    private Integer ord;
}
```

画面 2:
```java
public interface AdLabelMapper {
    int deleteByPrimaryKey(Integer id);
    int insert(AdLabel record);
    int insertSelective(AdLabel record);
    AdLabel selectByPrimaryKey(Integer id);
    int updateByPrimaryKeySelective(AdLabel record);
    int updateByPrimaryKey(AdLabel record);
}

public interface AdChannelLabelMapper {
    int deleteByPrimaryKey(Integer id);
    int insert(AdChannelLabel record);
    int insertSelective(AdChannelLabel record);
    AdChannelLabel selectByPrimaryKey(Integer id);
    int updateByPrimaryKeySelective(AdChannelLabel record);
    int updateByPrimaryKey(AdChannelLabel record);
}
```

画面 4:
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.heima.model.mappers.admin.AdLabelMapper">
```

画面 8:
```xml
<select id="queryAdLabelByLabelIds" resultMap="BaseResultMap" parameterType="list">
    select
    <include refid="Base_Column_List"/>
    from ad_label
    where id IN
    <foreach item="item" index="index" collection="list" open="(" separator="," close=")">
        #{item}
    </foreach>
</select>

<delete id="deleteByPrimaryKey" parameterType="java.lang.Integer">
    delete from ad_label
    where id = #{id}
</delete>

<insert id="insert" parameterType="com.heima.model.admin.pojos.AdLabel">
    insert into ad_label (id, name, type, created_time)
    values (#{id}, #{name}, #{type}, #{createdTime})
</insert>

<insert id="insertSelective" parameterType="com.heima.model.admin.pojos.AdLabel">
    insert into ad_label
    <trim prefix="values (" suffix=")" suffixOverrides=",">
        <if test="id != null">
            #{id},
        </if>
        <if test="name != null">
            #{name},
        </if>
        <if test="type != null">
            #{type},
        </if>
        <if test="createdTime != null">
            #{createdTime},
        </if>
    </trim>
    <if test="id != null">
        id,
    </if>
    <if test="name != null">
        name,
    </if>
    <if test="type != null">
        type,
    </if>
    <if test="createdTime != null">
        created_time,
    </if>
</insert>

<update id="updateByPrimaryKeySelective" parameterType="com.heima.model.admin.pojos.AdLabel">
    update ad_label
    <set>
        <if test="name != null">
            name = #{name},
        </if>
        <if test="type != null">
            type = #{type},
        </if>
        <if test="createdTime != null">
            created_time = #{createdTime},
        </if>
    </set>
    where id = #{id}
</update>

<update id="updateByPrimaryKey" parameterType="com.heima.model.admin.pojos.AdLabel">
    update ad_label
    set
        name = #{name},
        type = #{type},
        created_time = #{createdTime}
    where id = #{id}
</update>
```

画面 9:
```xml
<update id="updateByPrimaryKeySelective" parameterType="com.heima.model.admin.pojos.AdLabel">
    update ad_label
    <set>
        <if test="name != null">
            name = #{name},
        </if>
        <if test="type != null">
            type = #{type},
        </if>
        <if test="createdTime != null">
            created_time = #{createdTime},
        </if>
    </set>
    where id = #{id}
</update>

<update id="updateByPrimaryKey" parameterType="com.heima.model.admin.pojos.AdLabel">
    update ad_label
    set
        name = #{name},
        type = #{type},
        created_time = #{createdTime}
    where id = #{id}
</update>
```

画面 10:
```xml
<resultMap id="BaseResultMap" type="com.heima.model.admin.pojos.AdLabel">
    <id column="id" property="id"/>
    <result column="name" property="name"/>
    <result column="type" property="type"/>
    <result column="created_time" property="createdTime"/>
</resultMap>

<sql id="Base_Column_List">
    id, name, type, created_time
</sql>

<select id="selectByPrimaryKey" resultMap="BaseResultMap" parameterType="java.lang.Integer">
    select
    <include refid="Base_Column_List"/>
    from ad_label
    where id = #{id}
</select>

<select id="queryAdLabelByLabels" resultMap="BaseResultMap" parameterType="list">
    select
    <include refid="Base_Column_List"/>
    from ad_label
    where name IN
    <foreach item="item" index="index" collection="list" open="(" separator="," close=")">
        #{item}
    </foreach>
</select>

<select id="queryAdLabelByLabelIds" resultMap="BaseResultMap" parameterType="list">
    select
    <include refid="Base_Column_List"/>
    from ad_label
    where id IN
    <foreach item="item" index="index" collection="list" open="(" separator="," close=")">
        #{item}
    </foreach>
</select>
```

画面 13:
```xml
<insert id="insertSelective" parameterType="com.heima.model.admin.pojos.AdChannelLabel">
    insert into ad_channel_label
    <trim prefix="values (" suffix=")" suffixOverrides=",">
        <if test="id != null">
            #{id},
        </if>
        <if test="channelId != null">
            #{channelId},
        </if>
        <if test="labelId != null">
            #{labelId},
        </if>
        <if test="ord != null">
            #{ord},
        </if>
    </trim>
    <if test="id != null">
        id,
    </if>
    <if test="channelId != null">
        channel_id,
    </if>
    <if test="labelId != null">
        label_id,
    </if>
    <if test="ord != null">
        ord,
    </if>
</insert>

<
