# 画面线理解：09_数据迁移_业务代码编写_文章配置

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\09_数据迁移_业务代码编写_文章配置【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:23, 01:41, 01:58, 02:27, 02:59, 04:05, 04:27, 05:19, 05:44, 06:13, 06:47, 07:15, 07:33
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:05:05

1) 这一组画面整体在讲什么（一句话）：
讲解如何在业务层代码中，通过 HBase 操作工具类和 Service 层，实现对文章配置数据的查询与转换。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示一个业务流程图，包含“支付业务”、“安全校验”、“HBase操作”、“MongoDB操作”等模块，用于说明系统架构。
画面2：展示 PPT 页面，介绍 ArticleCallBack 接口和 ArticleHBaseInvok 类，用于 HBase 数据操作。
画面3：在 IDEA 中展示 ArticleHBaseInvok 类的代码，包含 Getter 和 Setter 方法，以及私有字段 apArticle 和 articleCallBack。
画面4：展示 ArticleQuantity.java 文件中的 HBaseStorage 对象转换方法，包含 StorageData 的添加操作。
画面5：展示 ArticleQuantity.java 文件中的私有字段 apArticleConfig。
画面6：展示 ArticleQuantity.java 文件中的私有字段 apArticleContent。
画面7：展示 PPT 页面，介绍 ApArticleConfigService 接口和其实现类 ApArticleConfigServiceImpl。
画面8：展示 PPT 页面，介绍 ApArticleConfigMapper.xml 中的 SQL 查询语句。
画面9：在 IDEA 中展示 ApArticleConfigService.java 文件，定义了接口。
画面10：在 IDEA 中展示 ApArticleConfigService.java 文件，添加了 import 语句。
画面11：在 IDEA 中展示 ApArticleConfigService.java 文件，添加了方法签名。
画面12：在 IDEA 中展示 ApArticleConfigServiceImpl.java 文件，添加了 @Service 注解和字段注入。
画面13：在 IDEA 中展示 ApArticleConfigServiceImpl.java 文件，实现 queryByArticleIds 方法。
画面14：在 IDEA 中展示 ApArticleConfigServiceImpl.java 文件，实现 getArticleId 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
public interface ArticleCallBack {
    public void articleCallback(ApArticle aparticle);
}
```
```java
// 回调对象
@Setter
@Getter
public class ArticleHBaseInvok implements HBaseInvok {
    // 回调需要传递的对象
    private ApArticle aparticle;
    // 回调需要对应的回调接口
    private ArticleCallBack articleCallBack;
}
```
画面3：
```java
import com.heima.common.hbase.entity.HBaseInvok;
import com.heima.model.article.pojos.ApArticle;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
```
画面4：
```java
if (null != aparticle) {
    return aparticle.getArticleId();
}
return null;
```
```java
public HBaseStorage getHbaseStorage() {
    HBaseStorage hbaseStorage = new HBaseStorage();
    hbaseStorage.setTable(String.valueOf(aparticle.getArticleId()));
    hbaseStorage.setHBaseInvok(hBaseInvok);
    StorageData aparticleData = StorageData.getStorageData(aparticle);
    if (null != aparticleData) {
        hbaseStorage.addStorageData(aparticleData);
    }
    StorageData aparticleConfigData = StorageData.getStorageData(aparticle);
    return hbaseStorage;
}
```
画面5：
```java
private ApArticleConfig apArticleConfig;
```
画面6：
```java
private ApArticleContent apArticleContent;
```
画面7：
```java
public interface ApArticleConfigService {
    List<ApArticleConfig> queryByArticleIds(List<String> ids);
    ApArticleConfig getArticleId(Integer id);
}
```
画面8：
```xml
<select id="selectByArticleIds" resultMap="baseResultMap">
    select
    <include refid="base.Column.List"/>
    from ap_article_config
    where article_id in
    <foreach item="item" index="index" collection="list" open="(" separator="," close=")">
        #{item}
    </foreach>
</select>
```
画面9：
```java
package com.heima.migration.service;
public interface ApArticleConfigService {
}
```
画面10：
```java
import com.heima.model.article.pojos.ApArticleConfig;
import java.util.List;
```
画面11：
```java
public List<ApArticleConfig> queryByArticleIds(List<String> ids);
public ApArticleConfig getArticleId(Integer id);
```
画面12：
```java
@Service
public class ApArticleConfigServiceImpl {
    private ApArticleConfig apArticleConfig;
    private ApArticleContent apArticleContent;
    private ApArticleConfigMapper apArticleConfigMapper;
    private ApArticleConfigService apArticleConfigService;
}
```
画面13：
```java
import com.heima.mappers.app.ApArticleConfigMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
@Service
public class ApArticleConfigService {
    @Autowired
    private ApArticleConfigMapper apArticleConfigMapper;
    @Override
    public List<ApArticleConfig> queryByArticleIds(List<String> ids) {
        return apArticleConfigMapper.selectByArticleIds(ids);
    }
    @Override
    public ApArticleConfig getArticleId(Integer id) {
        return null;
    }
}
```
画面14：
```java
import java.util.List;
@Service
public class ApArticleConfigServiceImpl implements ApArticleConfigService {
    @Autowired
    private ApArticleConfigMapper apArticleConfigMapper;
    @Override
    public List<ApArticleConfig> queryByArticleIds(List<String> ids) {
        return apArticleConfigMapper.selectByArticleIds(ids);
    }
    @Override
    public ApArticleConfig getArticleId(Integer id) {
        return apArticleConfigMapper.selectByArticleId(id);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：架构图，包含“支付业务”、“安全校验”、“HBase操作”、“MongoDB操作”等模块，其中“支付业务”指向“安全校验”，“安全校验”指向“HBase操作”，“HBase操作”指向“MongoDB操作”。
画面2：PPT 标题为“7.2.2 service”，内容包括“对文章配置操作的service”、“接口位置”、“代码位置”。
画面7：PPT 标题为“7.2.2 service”，内容包括“对文章配置操作的service”、“接口位置”、“代码位置”。
画面8：PPT 标题为“7.2.1 mapper”，内容包括“ApArticleConfigMapper 中新增方法”、“SQL 查询语句”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
