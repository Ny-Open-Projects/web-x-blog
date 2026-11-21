# 28_用户行为功能_mapper映射文件编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\28_用户行为功能_mapper映射文件编写【海量资源尽在 666java.com】.mp4
- 时长 13分16秒（音频 796s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们继续往下讲刚才咱们是把这个实现类给写完了这个逻辑这个写完之后你看这里边还有两个这种爆红的是吧咱们之前讲过那这是什么意思这个是不是警告压制警告怎么办就是加一个super warning就可以了那这个警告其实你不压制它也没有问题只是看着不爽对吧所以说咱们是把这个加一个这东西就可以了
[00:29] 那行啊那这个咱们讲完之后呢咱们下面就来去编写具体的这种Mapper接口啊行咱们点击看一看啊这之后呢这呢他也红这爆红的话其实也是警告大家不管其实也没有问题好吧这两个咱们都进来啊这这两个我都已经都已经打开了啊打完之后呢大家来分析一下你看这里边都有两个两个参数你看这里边可能还有这也两个参数是吧那两个参数的话呢
[00:56] 有可能的会出问题那咱们之前是怎么解决的呀你到麦粉无间里边穿餐的时候有可能会有错乱的情况所以说呢咱们在这啊去加一个什么注解这个param注解是吧然后呢这个param就是当前的什么这个ID啊应该是叫userID啊咱们就改个名叫userID好吧这不是userID叫entryID好吧把这个小写OK这个呢也拷贝一下
[01:29] 这个就是articleids是一个数组好再往下那这个就是咱们的写上param然后是articleids这个就是entry那这个是我设完之后这边还有一个咱们把这个注解也加上是userid好吧下面这个是设备id好那补全之后下面咱们就来去创建这个接口所对应的映射文件
[02:13] 那在哪创建呢是不是咱们还得去找到当前的model啊ok 那这个接口啊其实是在这是吧那咱们需要去创建它的映射文件给拷贝一个拷贝一个改个名名字叫啥呢首先咱们写第一个啊叫ap show什么呢show Hive然后是mypure对吧ok 没问题来咱们再来考第二个第二个叫啥呢
[02:46] 这个是叫AP-show了是吧开门然后是下面是N-tree那这样的话咱们就改完了啊改完之后啊咱们就把这个内容啊给删掉啊因为他目前所目前是对应不上的啊好删掉把这个也给删掉啊那顺便让你把这个MAP接口也来改了啊那么2目前的是一个AP-show目前的这个MAP文件这个呢咱们也要也改一改啊
[03:25] 叫什么jp-Hive-intra-mapOK那没问题啊那行那这个咱们做完之后啊咱们先来去编写当前的这个配置我们还是老套路啊从当前的这个里边呢咱们去拷贝拷贝一些东西啊拷贝哪个呢拷贝当前的拷贝当前的redo的map和circle的这种基本的circle的字段啊好那拷贝过来之后好像报错了是吧
[03:54] 没有问题啊这个呢可能是没有找到当前这个类这个类呢咱们不在这个包下边所以说你也要改一改啊是在哪啊在modo下边有个什么Hive什么gogo s里边不能找到了好吧你看这些都没有错了啊那行啊那这个咱们设完之后呢下面呢咱们就来去写一下当前的slack的查询对吧首先咱们写第一个啊第一个是哪个呢
[04:23] 点击看一看是不是他呀好拷贝过来拷贝过来之后呢这里边是有一个返回啊返回的话就是现在Base Result麦克风没问题那这个Circle该怎么去写那咱们还得分析一下当前的这种参数对吧你看啊咱们要查询的肯定是当前的这个表然后参数是第一个是当前的实体ID是吧第二个是这设备ID啊第二个是啥呢
[04:55] 当前的是一个什么article ids所以说咱们直接写就可以了slack 的什么slack 的新flam ap 哪个show 干什么dio 啊然后是然后呢怎么办呢然后咱们就是是不是有一个vr 啊是entry 地 地 啊 位 干 id 啊干 id 啊你可以在这看啊就干 id 吗好等于谁啊
[05:24] 等于当前咱们传过来的这个ID那传过来是哪一个呢你可以打开这个接口去看一眼它啊这接口这里面是不是有一个entry articles id啊不对是吧还是当前的entry id啊那行那下面还有一个啊下面是不是还有一个参数啊是articulds这显然它是一个输组是吧那它应该是叫id啊id然后是怎么着
[06:01] 既然参数是一个数组是不是咱们还得用in okin 的话怎么办咱们是不是还得去for eachok 这个里边就是article ids 拷贝一下吧article ids咱们起一个变量就叫item然后下面是啥呢下面是咱们的一个sublet是分割分是造号好那这样设置完之后咱们就可以直接拿到当前的什么一个item
[06:35] 就能拿到值了啊那的话就能去通过当前的entry ID和article的ids呢去作为条件去查询当前这个表OK那这个没问题啊那这个星呢咱们还要替换一下替换哪个咱们之前讲过最好不要写星是吧写什么呢引入一个啊写具体的字段就是base column哦OK就是上面字段那种啊那行啊那第一个呢咱们就写完了咱们再来写第二个
[07:05] 第二个应该不是一个slack的大家可以看一下这个接口接口应该是一个savesave的话咱们是不是有一个叫insert标签比如说把这ID拷贝过来它的一个prime type咱们可以不设没问题然后下面大概怎么去写呢这里边传参数你会发现首先它是有一个article ids有可能会去存储多条数据所以说这一块内容还要干嘛呢
[07:36] 还要做循环操作所以说怎么写insert into ap show看什么开了然后怎么写啊后是不是他的具体字段呢他字段是不是咱们已经知道了是知道是哪个了i article那这个article应该是错了啊应该是叫article id好吧啊你看这一块啊应该是叫article id
[08:05] 不是article大家一定要注意笔记上写错了大家一定要能够更正过来好那这个做完之后咱们直接去把它拷过来完了好然后下面该怎么办下面是不是有一个values那values下面咱们是要去bin所以说还要加for each咱们当前的这个东西还是谁还是当前的article.ls因为你最终要循环到这然后咱们还去
[08:37] 还去起一个atom就还叫atom然后是分割符的话他们也是用逗号好吧好那里边该怎么写呢其实咱们要去写当前的具体的参数了对吧首先第一个选的就是entry id吗可以说井号谁呀井号entry id你可以看一下咱们传过来的时候是不是传过来一个entry id啊所以说就是他那第二个呢第二个是不是就是article id啊所以说就是谁呀
[09:08] 因为这里边是便利的每一个元素对吧OK啊比如说井号什么那第三个呢第三个是click你是否点击是吧是否点击的话咱们现在可以给一个0好吧给一个0所以说咱们直接写死就可以了然后呢然后下面是两个时间一个是展示时间一个是创建时间那这时候呢咱们可以用mycircle的一个内置函数叫no
[09:39] 那这样的话就是当前的时间相当于你在加入程序里边new了一个data效果是一样的行那这个当前的映射文件咱们就算是写完了然后下面咱们来写第二个映射文件就是当前的设备的映射那设备映射咱们是一样的套路所以说咱们还是要干嘛还是要从当前的映射文件中笔记中
[10:05] 考过来当前的这种 without map和当前的一个搜狗片段啊好考过来之后呢这份内容可能还是出错是吧所以说咱们要去改一改怎么改啊在这写一个什么首先是一个model然后点什么Hive然后点什么do ok那这样找到了啊所以你看这块咱们也可以检查一下这个字段到底对还是不对啊咱们也可以打开当前这个表id type entry id create time
[10:36] boost 是吧所以说这块内容咱们都已经试完了没有问题那这个 circle 该怎么写呢是一个查询的啊比如说咱们打开当前的 entry不是 entry 啊打开的前的 Mapper 文件 Mapper 接口就是当前的这个 id好来放到这啊那放到这之后呢这里边啊它也有一个返回值所以说咱们也有一个 result map就是当前的 result map 好吧
[11:09] 那这个circle该怎么写呢circle的话也比较容易slag的什么slag的新flum谁呀这时候这个表名就变了啊应该是查询的是当前的一个表好查询完之后呢就起个别名吧然后是下面是有vir好vir里边啊咱们需要去根据当前的条件进行查询有哪些条件呢咱们还可以打开这个看看是不是有一个user id和一个什么设备id呀所以说咱们再去写的时候就比较容易了啊
[11:39] 来咱们先去判断一下dif test首先呢是当前的用户ID如果说它等于none的话呢咱们就可以拼接circle了啊OK写错了啊按着什么a.entry你要注意啊这个user ID定的它也是当前的entry因为它呢是有两种例行0是啥呢设备1是用户所以说咱们在这啊
[12:11] 首先要去设置一个什么AzierType等于几啊用户几啊用户是不是1啊比如说用户是1的时候并且我们再去设置当前的什么entryID等于谁啊就等于当前的用户诶错了啊userIDOK那这样我们就写完了啊那写完之后呢咱们下面还有一个啊都是一样的咱们拷贝一份这个呢是叫什么
[12:42] 设备ID是吧所以说这块就是设备ID但是这个就不是1了是谁呀这也是0是吧行啊那这个查询之后啊大家还有一个需要注意这个查询之后返回的呢是一个对象这个对象并不是集合所以说为了能够容错性更高咱们在这加一个limit然后只让它返回一条就可以了当前这两个Mapper文件呢到此呢咱们就写完了
[13:12] 然后下一个呢咱们就来去测试一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
<!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
<Mapper namespace="com.heima.model.behavior.mappers.app.ApShowBehaviorMapper">
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
</Mapper>
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

