# 18_数据保存_频道_mapper定义

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\18_数据保存_频道_mapper定义【海量资源尽在 666java.com】.mp4
- 时长 4分36秒（音频 276s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好咱们就继续往下讲然后下面咱们会有一个mypro接口的定义其实咱们已经分析完这个思路了然后下面咱们就来去说一下或者创建咱们的mypro接口这mypro其实咱们按照之前的套路咱们直接去拷贝一下就可以了这拷到哪你可以看一下拷到当前mypro私下边有一个我的命我的命下边有一个ad label mypro好吧行打开当前的idea
[00:30] 然后再打开 MyPost当然我这已经定位到当前的model中了所以说你在 ad 下面直接去拷贝就可以了拷贝完之后你可以看一下当前是有删除是吧新增还有是也是新增这个新的话可能是会有一些条件还有就是查询根据主件还有是更新的还有根据主件更新的还有什么还有查询的是吧还有查询的行这些方法咱们用到的时候咱们一会可以再去讲
[00:59] 好吧行这是一个这是一个然后下面还有一个下面还有一个就是当前的这种adchannel label mypro咱们也可以去把它拷贝一下这个拷到哪呢这个也是admin因为都是ad开头的大家一定要把这个包给区分开好吧这样的话你管理的时候或者你找的时候还是比较容易的好拷贝拷贝完之后咱们也可以去看一下这里边的方法这个方法是delete是吧insert
[01:30] 还有什么也是新增还有是查询一个是吧根据主件查询还有修改修改两个还有就是下面是根据当前的什么当前的ID去查询一个ADChinaLabel行这个咱们就算是定义完了定义完之后下面其实还有些事咱们需要做是吧哪些事是不是咱们现在需要在这去定义什么东西这一块我多余的删掉
[01:59] 这样应该是没有的是不是应该去定义他的什么他的这种mypro文件所以说咱们在这也直接拷贝就可以了好吧拷贝的方式你直接去拷贝一下当前这个东西然后在这去创建一个文件文件RXX这是一个然后咱们可以再去定义第二个就是PD label mypro
[02:30] 那创建完之后其实这个东西你也不用去写也比较简单咱们之前做的时候也是都是直接拷过来的好拿过来之后咱们可以再简单看一眼好拷贝一下然后首先是拷贝的是当前的adlabel找到label可以拷贝一下你看这一块有没有有没有包错有不错的话你就需要去改一改好吧但是这个为什么会包错因为这个找不着找不着找不着的话肯定是有原因的怎么可以看一下
[03:01] 当前model下边mypros不应该是mypros是吧应该是means下边什么呢PoDOSOK那这样就能找到了请我把这个更新一下笔记更新拷贝一下省得出错好行那这个其实就算是考完了好了你看这些他也能找到对应的方法都没有问题根据主线查询然后是这是
[03:32] 这也是查询是吧这也是查询但是根据条件去查询对这个是根据一个ID查询然后下面还有下面还有什么呢下面还有这种什么curry by什么label by label ids是吧ok然后下面还有一些删除新增还有还有新增再条件的新增还有修改这些大家应该都能看得懂都能看明白行那这些东西我们就不再写了
[04:00] 还有一个这个你也需要考过来这个是adlabelmapper考错了是吧我看看没考错再往下你需要把当前adchannellabelmapper考过来考到哪考到当前的adchannellabel一定要考对了别到时候考也考错了那就好了行这个其实就完了你看这些都能找得着没有问题行这个Mapper咱们就写到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
<!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
<Mapper namespace="com.heima.model.mappers.admin.AdLabelMapper">
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

