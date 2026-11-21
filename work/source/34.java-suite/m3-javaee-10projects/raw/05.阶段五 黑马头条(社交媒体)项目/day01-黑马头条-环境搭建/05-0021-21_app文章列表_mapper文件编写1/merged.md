# 21_app文章列表_mapper文件编写1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\21_app文章列表_mapper文件编写1【海量资源尽在 666java.com】.mp4
- 时长 11分29秒（音频 689s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们继续啊把这个MAP文件咱们也去写一下首先呢咱们要去创建两个MAP文件那这个MAP文件在哪去创建呢首先呢咱们要去先创建什么呢先创建咱们的一个这种MAP接口在当前的什么Java model里边有个什么model里边有一个MAPs在APP里边咱们创建两个接口啊第一个接口是谁呢就是ApparticleMap它是一个接口好OK一个
[00:28] 然后还有第二个就是他还在这创建啊还是一个接口好背一下好那这创建完之后啊这里边还有些方法需要创建啊你看他创建完之后他已经引入进来了首先咱们还可以按out加回车直接把这方法给创建出来就可以啊好回车好这是一个然后下面还有啊下面还有两个啊那有一个这个也要创建出来这是另外一个还有一个
[00:58] AP article里边还有另外一个方法根据当前list user的查询出来的这种list去查询当前的article列表信息也按回车奥特加回车啊好 也创建出来这个所有的方法都算是已经创建完了这一块呢应该是不会再报错了啊那但这个这个标红呢它是其实呢它是报警告如果说你要想去加持警告的话也很容易啊咱们在这呢去加一个super warningsuper warning然后是给个参数调那这时候
[01:30] 你看它所有的这种红或者爆黄的就没了当然那加上这个之后呢它如果说真错误的话呢它还是会报错的比如说咱们可以试一下还是会报错的啊它刚才那个红呢它只是警告所以说它只是压制了警告而已啊那行那这个说完之后啊咱们下面就来去编写具体的Maple文件好吧那Maple文件怎么去写呢咱们呢
[01:57] 之前再说了啊mypro接口是定义到这个mypro的这个文件这个算是路径下边啊那咱们mypro文件的统一呢都是在这个mypro的最后source下面这个mypro文件夹下边所以说咱们在这去创建两个这种mypro文件第一个是AP article mypro好吧这去创建一个文件啊咱们叫插门是吧然后第二个第二个啊也是他是他点
[02:29] 这样的话咱们就创建完了关于这投信息咱们就直接从笔记上拷过来就可以首先第一个是他我打开当前的mypro拷贝一下需要补全当年你检查一下当前这个类到底能不能选中是吧还挺强大的他能去看一下到底你写对还是没写对咱们把第二个也去补全一下咱们也直接拷贝一下但这个类肯定是不对的是吧你去写上来了
[03:04] 叫AP, use article list Mapper,是吧把这个好这样的话呢这个两个类啊就两个文件呢算是准备完了啊那准备完之后呢咱们就下下面呢就来去写刚前的这种码那这个Mapper文件里面代码到底该怎么去写呢咱们先定义这个AP article Mapper这个文件啊首先呢咱们在这儿去定一个slack的方法是吧那这个ID是谁呢
[03:32] IT的话就应该给你当前这个MIPR接口的方法名是不是对应上啊好拷贝过来然后呢我们就先结束一下啊那行那这是一个啊这是一个然后第二个那第二个是啥呢看一下啊第二个是这个方法我们也定义一下叫select好这样的话呢应该是不会报错了啊它还在报错是吧可能还有一些参数咱们没有设置啊
[04:02] 这里边咱们说到这咱们再多说一个这里边如果说你要传输多个参数的话这里边可能会有一个问题它有可能不能区分到底是DTO还是Type所以说建议咱们在这去设置一个这种参数的区别比如说我这个参数就叫做DTO那这个也可以加一个Pyram叫啥呢叫Type这样的话就算是显示一下
[04:30] 那咱们继续编写当前这个接口那这里边的这个circle该怎么去写呢这个circle其实非常简单只是咱们急于当前的某一些条件进行查询就可以了因为这里边都是单表查询好slack的是吧新flum谁呀flum当前的叫jp article好点一下叫jp article
[04:59] 那这个表写完之后呢咱们有一些条件呢那这条件就是返回值是啥条件是啥返回值是啥首先呢咱们这里边啊之前讲mybodies的时候应该说过啊这里边咱们可以去封装一个什么伪造的map那比如说map里边它不是可以封装咱们的一些类型这个呢我就从笔记上直接拷贝一下啊咱们拿过来去讲一讲因为这里边都是一些什么呢都是一些自动的映射信息好来看一下啊
[05:30] 首先返回的是当前的article当前这个类型是吧这里边所有的都是跟主件不是主件应该是字段跟当前的属性一一一对应上这个是做了一颗映射所以说咱们直接返回的时候应该是返回的是rezo的map就可以了所以说这边呢我直接设置为rezo的map可以好吧那这里边还有一个这里边还拷贝了一个这种最基本的字段的列表是吧所以说咱们这儿不要设置为新
[05:59] 应该设置啥呢设置为他那他怎么办呢咱们可以引入进来是吧一个include是吧就是column好那这样的话呢就算是那的话咱们就算是设置完了啊那这里边啊是有一些参数的啊那有哪些参数呢你们都知道BTO里边是不是有很多参数那里边是不是还有一个什么是不是还有一个type的参数对吧所以说咱们在这啊就都要去把这些参数进行去进行判断
[06:30] 所以说那参数判断怎么判断呢首先呢咱们在这习惯性的加一个无约条件是吧然后呢咱们就可以进行判断了是哪个标签呢是地府是吧好test首先咱们做的第一个判断呢是当前的这什么呢一个什么打开当前这个类啊我们可以看一下里边有什么参数我们再去看一下嗯这个类在哪呢啊对这个类在这是吧啊没有在这是吧在model下边啊model下边有一个
[07:00] Article里面有个DTOS里面有个ArticleHomeDTO首先你看如果说是有这些参数的话咱们都应该进行判断所以说里面第一个是省市的所以说咱们需要这个给加上省市如果说它不等于空是吧不等于浪怎么办呢不等于浪咱们就可以拼接咱们参数了叫按的什么咱们可以起个别名叫BA好吧
[07:34] A 讲什么?
[07:35] 当前的这种等份Provis 。
[07:38] OK,你要注意啊,就是ID,因为你的导中就是这么写的啊,咱们可以看一下,是不是这么写的呀?
[07:48] OK啊,没问题,所以说它等于啥呢?
[07:52] 它就等于一个站位符,站位符是谁呢?
[07:56] 站位符就是GTO下边的,当前的Provis,是吧?
[08:01] 嗯,行,那这是第一个啊,就是当前的,
[08:05] 整市下面还有咱们的城市咱们的市区都可以去拷贝过来啊那这个拷贝的时候呢咱们就来去直接拷贝一下啊那拷贝的话我在这拷贝啊CTID是吧这个是CTID好下面还有个什么呢ContentContentID是吧就是咱们的区限ID好这个你写一下啊就是A是
[08:36] 把它给删了下划线这是小写的ID好吧那这时候省市区的条件算是加完了那还有啊还有个参数啊这个参数是不是type呀这个type的这个字段呢咱们也要去进行判断一下啊它呢就可以去决定到底是加载更多或者是加载比新是吧所以说咱们在这判断一下如果说它呢不等于none并且呢它是type等于等于1的时候不是加载更多
[09:05] 那这里更多的话咱们呢主要的是有一个字段进行跟时间的进行判断哪个是哪个字段呢这里边有一个publish name就是方前文章的发布时间AA.R那到底是谁去对比呢根据方前的什么一个什么ATO里边的一个是最小时间去对比啊那到底是大鱼呢还是小鱼呢应该是小鱼是吧小鱼号吧那小鱼号是不是报错了
[09:36] 包错没有问题啊咱们呢可以让他去包裹一下好过来啊这样的话呢咱们就可以去写信写这个小鱼号了啊行那这个一之外是不是还有等于二啊他是不是还有可以去加载最新的加载最新的方式呢你就可以在这他等于然后呢然后这是大鱼大鱼谁呢应该是大鱼不是命是谁呀是max好这样的话咱们就把这个
[10:08] 设置完了但这里边还有最后一个参数就是当前的一个什么种频道频道也要去打一下好拷贝拷贝完之后呢这里边是一个频道频道的话怎么写就是to点什么承诺应该是不等于不说不等于那因为咱们之前做了个标识还没明显标识是不是叫什么杠杠当他等于他的时候呢
[10:42] 我们就应该去有值是吧这个Tag里面有值有值的话咱们就要去复制这个Tag是谁呢我们可以看下表啊Tag呢就是当前的哪一个呢啊对这里边不是Tag啊这个Tag头应该是一个频道是吧所以说它对应的是当前的频道的ID好拷贝过来那都是等于谁呀等于当前的BTO.好那这样的话咱们就说这完了啊
[11:12] 好最后一步千万不要忘了这块需要去设置一个分页分页怎么写VMT方式咱们直接可以把这个DTO的什么size放进来可以了目前的话这个circle的或者这个方法的咱们就写完了啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过 MyBatis 框架实现文章列表的分页查询功能，包括定义数据访问层接口、编写 SQL 映射文件、配置数据源以及在服务层调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 `AppArticleServiceImpl.java` 中的 `getDefaultArticleList` 方法，该方法通过 `apArticleMapper.loadArticleListByLocation` 查询文章列表。
画面 2: 展示了在 IntelliJ IDEA 中右键点击 `java` 目录，弹出创建新文件的菜单，准备创建新的 Java 类或接口。
画面 3: 展示了 `ApArticleMapper.java` 接口文件，其中定义了 `loadArticleListByLocation` 和 `loadArticleListByIdList` 两个方法。
画面 4: 展示了项目结构，选中了 `ApArticleMapper` 接口文件。
画面 5: 展示了 `ApArticleMapper.xml` 文件，其中包含了 MyBatis 的 XML 配置头和 `<Mapper>` 标签。
画面 6: 展示了在 `ApArticleMapper.xml` 文件中，光标位于 `<select id="loadArticleListByLocation">` 标签内，准备编写 SQL。
画面 7: 展示了 MySQL 数据库的 Navicat 界面，显示了 `ap_article` 表的数据，用于验证 SQL 查询结果。
画面 8: 展示了 `ApArticleMapper.xml` 文件中，`<resultMap>` 标签内定义了 `ApArticle` 对象的属性映射。
画面 9: 展示了 `ApArticleMapper.xml` 文件中，`<sql id="Base_Column_List">` 标签定义了公共的列名，以及两个 `<select>` 标签分别对应 `loadArticleListByLocation` 和 `loadArticleListByIdList` 方法。
画面 10: 展示了 `ArticleConsts.java` 文件，其中定义了 `ArticleInfoDto`、`ArticleListDto` 和 `UserArticleListDto` 等数据传输对象。
画面 11: 展示了 `ApArticleMapper.xml` 文件中，`loadArticleListByLocation` 方法的 SQL 查询语句，包含 `where` 条件判断 `dto.provinceId` 是否为空。
画面 12: 展示了 `ApArticleMapper.xml` 文件中，`loadArticleListByLocation` 方法的 SQL 查询语句，增加了对 `dto.cityId` 的条件判断。
画面 13: 展示了 `ApArticleMapper.xml` 文件中，`loadArticleListByLocation` 方法的 SQL 查询语句，增加了对 `dto.countyId` 的条件判断。
画面 14: 展示了 `ApArticleMapper.xml` 文件中，`loadArticleListByLocation` 方法的 SQL 查询语句，增加了对 `type` 参数的条件判断。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
private List<Article> getDefaultArticle(ArticleHomeDto dto, Short type) {
    return apArticleMapper.loadArticleListByLocation(dto, type);
}

@AutoWired
private ApArticleListMapper apUserArticleListMapper;

// 先从用户的缓存中查询文章信息，如果没有再从默认文章信息获取
private List<Article> getUserArticleList(ArticleHomeDto dto, Short type) {
    List<Article> list = apUserArticleListMapper.loadArticleListByUser(dto, user, type);
    if (list.size() == 0) {
        return apArticleMapper.loadArticleListByLocation(list);
    }
    return list;
}
```

画面 3:
```java
package com.heima.model.mappers.app;

import com.heima.model.article.dto.ArticleHomeDto;
import com.heima.model.article.po.Article;
import com.heima.model.user.po.ApUser;
import java.util.List;

public interface ApArticleMapper {
    List<Article> loadArticleListByLocation(ArticleHomeDto dto, Short type);
    List<Article> loadArticleListByIdList(List<ApUserArticleList> list);
}
```

画面 5:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
<Mapper namespace="com.heima.model.mappers.app.ApArticleMapper">
</Mapper>
```

画面 6:
```xml
<select id="loadArticleListByLocation">
</select>
```

画面 8:
```xml
<resultMap id="resultMap" type="com.heima.model.article.po.ApArticle">
    <result column="id" property="id"/>
    <result column="title" property="title"/>
    <result column="author_name" property="authorName"/>
    <result column="channel_id" property="channelId"/>
    <result column="channel_name" property="channelName"/>
    <result column="layout" property="layout"/>
    <result column="flag" property="flag"/>
    <result column="images" property="images"/>
    <result column="labels" property="labels"/>
    <result column="likes" property="likes"/>
    <result column="collection" property="collection"/>
    <result column="comment" property="comment"/>
    <result column="views" property="views"/>
    <result column="province_id" property="provinceId"/>
    <result column="city_id" property="cityId"/>
    <result column="county_id" property="countyId"/>
    <result column="created_time" property="createdTime"/>
    <result column="publish_time" property="publishTime"/>
    <result column="sync_status" property="syncStatus"/>
</resultMap>
```

画面 9:
```xml
<sql id="Base_Column_List">
    id, title, author_name, channel_id, channel_name, layout, flag, images,
    labels, likes, collection, comment, views, province_id, city_id, county_id, created_time,
    publish_time, sync_status
</sql>

<select id="loadArticleListByLocation" resultMap="resultMap">
    <include refid="Base_Column_List"/>
    from ap_article aa
</select>

<select id="loadArticleListByIdList">
</select>
```

画面 11:
```xml
<select id="loadArticleListByLocation" resultMap="resultMap">
    <include refid="Base_Column_List"/>
    from ap_article aa
    where
        <if test="dto.provinceId != null">
            and aa.province_id = #{dto.provinceId}
        </if>
</select>
```

画面 12:
```xml
<select id="loadArticleListByLocation" resultMap="resultMap">
    <include refid="Base_Column_List"/>
    from ap_article aa
    where
        <if test="dto.provinceId != null">
            and aa.province_id = #{dto.provinceId}
        </if>
        <if test="dto.cityId != null">
            and aa.city_id = #{dto.cityId}
        </if>
</select>
```

画面 13:
```xml
<select id="loadArticleListByLocation" resultMap="resultMap">
    <include refid="Base_Column_List"/>
    from ap_article aa
    where
        <if test="dto.provinceId != null">
            and aa.province_id = #{dto.provinceId}
        </if>
        <if test="dto.cityId != null">
            and aa.city_id = #{dto.cityId}
        </if>
        <if test="dto.countyId != null">
            and aa.county_id = #{dto.countyId}
        </if>
</select>
```

画面 14:
```xml
<select id="loadArticleListByLocation" resultMap="resultMap">
    <include refid="Base_Column_List"/>
    from ap_article aa
    where
        <if test="dto.provinceId != null">
            and aa.province_id = #{dto.provinceId}
        </if>
        <if test="dto.cityId != null">
            and aa.city_id = #{dto.cityId}
        </if>
        <if test="dto.countyId != null">
            and aa.county_id = #{dto.countyId}
        </if>
        <if test="type != null and type == 1">
            and aa.publish_time <![CDATA[>]]> #{dto.minBehotTime}
        </if>
        <if test="type != null and type == 2">
            and aa.publish_time <![CDATA[<]]> #{dto.maxBehotTime}
        </if>
</select>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

