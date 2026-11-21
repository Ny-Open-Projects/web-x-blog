# 画面线理解：06_数据保存准备_爬虫文章图文附加信息_service接口定义

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\06_数据保存准备_爬虫文章图文附加信息_service接口定义【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:23, 01:07, 01:39, 02:33, 03:20, 04:02, 04:40, 04:56, 05:42, 06:01, 06:54, 07:47, 08:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:02:52

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过 MyBatis 的 Mapper 文件和 Service 接口，实现对 CNewsAdditional 实体的增删改查功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 CNewsAdditionalMapper.xml 文件中的动态 SQL 片段，用于根据条件插入数据，包含多个 if 判断条件。
画面 2: 展示了项目结构，当前选中的是 CrawlerNewsAdditionalService.java 文件，位于 service 包下。
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
package com.heima.crawler.service;
```

画面 3:
```java
package com.heima.crawler.service;
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
