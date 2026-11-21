# 06_数据保存准备_爬虫文章图文附加信息_service接口定义

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\06_数据保存准备_爬虫文章图文附加信息_service接口定义【海量资源尽在 666java.com】.mp4
- 时长 8分9秒（音频 489s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就继续啊把那个爬虫文章这个图文的附加信息这块这个咱们写完啊刚才咱们是把myport给定义了现在呢咱们要去把这个Service也给定义一下好吧来打开咱们的idea啊然后是找到咱们自己的系统caller然后是在Service这一块呢咱们去再去定义一个接口是吧它这个接口啊叫什么呢咱们是叫caller
[00:27] C A W L E R News然后是叫 audition auditioni t i o n l然后是Service好简单一下color newsadditional然后是serviceok没问题好吧然后这是一个接口是吧然后咱现在咱们就要去定义里边的什么方法是吧这个方法其实有很多其实你在这已经看到了咱们在这就去定义一下
[01:00] 首先第一个呢咱们要去定义一个叫做保存然后是save是叫audition就可以了add aton al然后是参数呢就是今天的一个参数啊是cl newsaudition现在这个咱们写一下这是保存好嘞然后下面继续还有什么方法呢有一个查询
[01:30] 有一个插信啊,咱们返回呢是一个list集合里边装的就是clnews然后呢,咱们要currylistlist,是by啥呢有一个叫by need需要更新的这个呢后期咱们也会用得着啊里边的参数呢就只是一个date
[02:05] 对当前的时间好这是一个这是针对当前需要更新的时间查询列表然后继续往下看public然后咱们下面再去做一个就是还是要查询querylist这个参数其实跟这个参数是差不多的是cellnews
[02:39] 对,是这个材数有可能会有多个条件是吧返回值是一样的OK,这是查询根据条件查询根据条件查询下面还有什么再定义public然后是有一个bool你们都知道吧我们要检查当前的什么一个sys检查是否存在是吧那个咱们的一个东西
[03:11] 他说是URL是某一个请求的URL检查是否存在这个是一个方法然后接着再往下看这里边咱们还有一个叫做获取跟一个URL去获取这个是一个ZL News然后是BetDDITOL然后by什么URL好这个就是一个
[03:40] 是正的URL然后是根据URL获取什么呢获取图文附加信息OK然后继续往下看下面咱们还有一个叫做是检查当前的URL其实咱们已经有了是吧这样这里边还有一个你可以看跟这个是差不多的跟这个差不多你看一下这个里边怎么写的说
[04:19] 是否已存在URL咱们还要再去检查一下再去检查一下好来这一块是差不多是吧就这个咱们也可以看一下如果说他一样的话咱们就不用再去定义了开我们去找到当前的哪一块是有一个找找根据URL去查找行吧咱们就按笔记上去定义好吧public然后是伙类型伙类型
[05:00] 然后是is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.is.
[05:35] 好,Pathroom就是当前这个对象CLnews.additional.ok这是更新下面还有下面还有一个Dig大家可能不太好理解我们再去看一下public然后这是有一个集合集合你看这个集合是有一个pathitem它转回的是一个pathitem那为什么会有这么一个方法叫toPath
[06:07] item为什么会有这么一个方法呢这个方法是这样啊因为后期啊当前的某一个URL呢咱们需要干嘛呢需要进行再次去下载再次去下载啊也就是说你需要去再次爬取那这时候呢所有爬取的内容呢咱们都要去装到当前的哪当前的这个passitem中所以说呢咱们在这儿需要去转换一下那转换这个里边的参数呢就是当前某一某一些数据serialnews positional你可以在里边啊
[06:37] 比如说叫他哦,didnt know list好吧嗯,这叫转换数据为PathItem行,其实里边最主要转换的是一个UR啊因为咱们最终是要把UR是sizePath还有一个咱们是有一个查询的一个自增长的PathItem那这个呢其实也是根据当前时间去查询listPathItem
[07:08] 这个是一个当前的时间那目前这个东西这个方法就算是完了这个是查询自增的一个什么就是PathEtherm
[07:44] 这个咱们就算是设置完了所有的这个方法都是吧这个方法挺多的是吧那行啊咱们后期咱们去整合咱们的解析保存的时候这些方法咱们基本上都能用得着所以说咱们先要在这先定定义出来这东西其实也很好理解其实即使写咱们的这种实现类其实也比较简单好吧行咱们这个就先说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过 MyBatis 的 Mapper 文件和 Service 接口，实现对 CNewsAdditional 实体的增删改查功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 CNewsAdditionalMapper.xml 文件中的动态 SQL 片段，用于根据条件插入数据，包含多个 if 判断条件。
画面 2: 展示了项目结构，当前选中的是 CrawlerNewsAdditionalService.java 文件，位于 Service 包下。
画面 3: 展示了 CrawlerNewsAdditionalService.java 文件的接口定义，开始编写 saveAdditional 方法。
画面 4: 在 saveAdditional 方法中，添加了对 CNewsAdditional 类型的参数声明，并使用了 IDE 的自动导入功能。
画面 5: 在 saveAdditional 方法中，添加了对 Query 的导入，并开始编写方法体。
画面 6: 展示了 CrawlerNewsAdditionalService.java 文件中，定义了 queryListByNeedUpdate 方法和 checkExist 方法。
画面 7: 展示了 CrawlerNewsAdditionalService.java 文件中，定义了 queryListByNeedUpdate 方法的参数和返回值。
画面 8: 展示了 CNewsAdditionalMapper.xml 文件中的 insert 语句，用于插入数据，包含 trim 和 if 判断。
画面 9: 展示了 CrawlerNewsAdditionalService.java 文件中，定义了 getAdditionalById 方法。
画面 10: 在 getAdditionalById 方法中，使用 IDE 的自动导入功能，导入了 CNewsAdditional 类。
画面 11: 在 getAdditionalById 方法中，使用 IDE 的自动导入功能，导入了 ParseItem 类。
画面 12: 在 getAdditionalById 方法中，使用 IDE 的自动导入功能，导入了 Process 类。
画面 13: 展示了 CrawlerNewsAdditionalService.java 文件中，定义了 updateAdditional 方法和 toParseItem 方法。
画面 14: 展示了 CrawlerNewsAdditionalService.java 文件中，定义了 queryIncrementParseItem 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<if test="id != null">
    #id
</if>
<if test="newsId != null">
    #newsId
</if>
<if test="url != null">
    #url
</if>
<if test="readCount != null">
    #readCount
</if>
<if test="likes != null">
    #likes
</if>
<if test="comment != null">
    #comment
</if>
```

画面 2:
```java
package com.heima.crawler.Service;
```

画面 3:
```java
package com.heima.crawler.Service;
public interface CrawlerNewsAdditionalService {
}
```

画面 4:
```java
import com.heima.model.crawler.po.CNewsAdditional;
public void saveAdditional(CNewsAdditional cNewsAdditional) {
```

画面 5:
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.util.StringUtils;
import java.util.List;
import java.util.Date;
import com.heima.model.crawler.po.CNewsAdditional;
public List<CNewsAdditional> queryListByNeedUpdate(Date currentDate) {
```

画面 6:
```java
public List<CNewsAdditional> queryListByNeedUpdate(Date currentDate);
public boolean checkExist(String url);
```

画面 7:
```java
public List<CNewsAdditional> queryListByNeedUpdate(Date currentDate) {
    return null;
}
public boolean checkExist(String url) {
    return false;
}
```

画面 8:
```xml
<insert id="insertSelective" parameterType="com.heima.model.crawler.po.CNewsAdditional"
        keyProperty="id" useGeneratedKeys="true">
    insert into c_news_additional
    <trim prefix="values (" suffix=")" suffixOverrides=",">
        <if test="id != null">
            id,
        </if>
        <if test="newsId != null">
            news_id,
        </if>
        <if test="url != null">
            url,
        </if>
        <if test="readCount != null">
            read_count,
        </if>
        <if test="likes != null">
            likes,
        </if>
        <if test="comment != null">
            comment,
        </if>
        <if test="forward != null">
            forward,
        </if>
        <if test="unlikes != null">
            unlikes,
        </if>
        <if test="collection != null">
            collection,
        </if>
        <if test="createdTime != null">
            created_time,
        </if>
        <if test="count != null">
            count,
        </if>
        <if test="updatedTime != null">
            updated_time,
        </if>
        <if test="nextUpdateTime != null">
            next_update_time,
        </if>
    </trim>
</insert>
```

画面 9:
```java
public CNewsAdditional getAdditionalById(String url) {
```

画面 10:
```java
import com.heima.model.crawler.po.CNewsAdditional;
public CNewsAdditional getAdditionalById(String url) {
```

画面 11:
```java
import com.heima.model.crawler.po.ParseItem;
public List<ParseItem> toParseItem(List<CNewsAdditional> additionalList) {
```

画面 12:
```java
import com.heima.model.crawler.po.ParseItem;
public List<ParseItem> toParseItem(List<CNewsAdditional> additionalList) {
```

画面 13:
```java
public void updateAdditional(CNewsAdditional cNewsAdditional);
public List<ParseItem> toParseItem(List<CNewsAdditional> additionalList);
public List<ParseItem> queryIncrementParseItem(Date currentDate);
```

画面 14:
```java
import com.heima.model.crawler.po.CNewsAdditional;
import java.util.Date;
import java.util.List;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
public interface CrawlerNewsAdditionalService {
    // 保存
    void saveAdditional(CNewsAdditional cNewsAdditional);
    // 根据当前需要更新的时间查询列表
    List<CNewsAdditional> queryListByNeedUpdate(Date currentDate);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

