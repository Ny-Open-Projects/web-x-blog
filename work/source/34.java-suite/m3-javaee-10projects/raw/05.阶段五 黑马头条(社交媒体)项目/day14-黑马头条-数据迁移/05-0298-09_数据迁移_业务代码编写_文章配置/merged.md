# 09_数据迁移_业务代码编写_文章配置

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\09_数据迁移_业务代码编写_文章配置【海量资源尽在 666java.com】.mp4
- 时长 7分42秒（音频 462s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去写这个业务代码那什么是业务代码呢就是说咱们在这之前其实讲过这个流程那这个流程呢咱们会去做一些东西比如说怎么要去插入数据要去查询数据那都是关于当前文章的一些数据是吧咱们比如说咱们针对于当前全量数据要针对于文章的比如说文章的一些相关的配置啊作者呀
[00:26] 还有内容啊像这些数据呢咱们统一的都要先去准备还有相关的热点的文章的一些操作咱们也要准备最后呢咱们还有一个啊就是Service里边啊咱们还会再定义一个就是综合的那什么叫综合呢就刚才说了文章配置文章的配置内容啊还有作者像这些信息呢咱们一个一个去操作之后呢咱们再有一个统一的接口去调用这四个然后呢把它统一起来保存到一个
[00:54] 一个当前的实体类中这样的话管理起来就比较方便下面咱们首先要做第一个事就是他会去定义一些实体类这个实体类咱们去拷贝一下我先拷过来咱们再说这你创建一个包当前的爬虫不是爬虫这叫什么欠余的包欠余的位服务下边entity然后是在这去创建第一个这是一个接口是吧然后第二个是啥呢
[01:23] 第二个是一个回调的对象它就实现了当前的接口好放到这然后然后咱们再往下看看没有包错这个需要倒包是吧下面这个也要倒好下面还有一个非常重要的对象要去拷贝看一下就它跑到当前的NTT下面也没有包错然后稍等这个包需要倒一下这个包也要倒一下
[02:05] 然后下面是啥呢咱们可以重新的去看一下重点去看一下这个类这个类里边你可以看一下叫什么Article Quantity是吧然后这里边咱们是有一些东西你看第一个就是文章然后第二个是文章的配置还有文章的内容还有作者是吧还有一个回调函数这个咱们先不用管主要是看上面的几个这个是不是就是综合的实体类
[02:39] 它就包含了咱们文章的所有的信息比如说你要是只查文章的话那肯定不行这个数据不全所以说呢咱们在这又重新封装了一个尸体让它去包含了这四项好吧那咱们以后再去操作的更多的当前的尸体就是它好吧但这里边咱们都会去往里边去填充这四块数据好
[03:03] 行那这个咱们说完之后啊那咱们下面呢就来一个一个的去操作当然这个还有一个啊就是热点文章那个咱们先不去说咱们先去说这个全量的数据好吧那下面呢咱们先去做第一个接口第一个操作呢就是当前的文章的配置那这个比较简单啊就是做就是针对于当前文章文章的配置去做一个查询的操作啊查询查询哪一个你可以看啊
[03:31] 根据当前的ID就是当前的ArticleID去查询当前的列表还有根据当前的文章ID去查询某一个某一个就是两个方法那咱们下面就来去设置一下首先这一块那种这个其实就是根据当前的文章的ID文章它是一个列表去查询这个方法咱们之前是没有的所以说咱们需要在Maple文件中先去定义
[03:59] 根据当前主件去查询这个咱们这个是有的这个咱们就不用管了主要是来把这个定义一下就可以打开它拷贝一下然后是找到谁我可以搜一下叫AParticle叫config myport是吧好在这没有咱们就拷贝一下拷贝完之后你到这然后在这去加一个方法这个方法就是根据
[04:30] 当前的文章的ID列表去查询就是一个in做了一个循环好那这个咱们就设置完了那设置完之后下面还有两个方法咱们需要去定义叫AAP article config Service在哪呢在当前的这个然后是一个Service下边这个方法咱们需要去查询来看一下打开当前的Service右键在这去创建一个接口是吧叫AAP
[05:01] articleconfigconfig Service好 看到创建完了啊然后呢在这里边有两个方法第一个方法呢就是返回一个列表好public返回一个列表列表是里边是装的是aparticleconfig打包吧这个方法名就是他好吧这个是里边装的啥呢里边装的就是当前的
[05:37] 一个集合,integer吧,是integer吧,看看啊,是string是吧,string然后这是ids,这是一个,插群那边啊,然后第二个呢是duble leak,这是返回的一个,jp article config,然后是query咱们最好这个笔记保持一致啊,query article by idquery by article id,说错了啊,根据当前的文章id去插群
[06:09] 好这个是一个什么类型看看integer好吧那行创建完之后咱们在这去创建它的实现类impl当然前面加包名impl.这个实现就特别简单了叫Service然后你在这去输入当前的mypro是吧然后是ap article
[06:46] config mypro然后呢你就可以去实现这个方法叫implement然后是apap article写吧rti clre然后是config Service好这两个方法咱们需要去实现一下直接去调用方法就可以了点有一个slack的ids就把ids装进去就完事了第二个呢
[07:19] 第二个的话就是AP article config myfm然后点一个叫做slack的byid把它的ID装进去这样也行这个是个警告是吧怎么办去加一个super warning好这样的话这个方法咱们就算是是吧咱们先背着先背着以后咱们再去测试好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
package com.heima.migration.Service;
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
画面2：PPT 标题为“7.2.2 Service”，内容包括“对文章配置操作的Service”、“接口位置”、“代码位置”。
画面7：PPT 标题为“7.2.2 Service”，内容包括“对文章配置操作的Service”、“接口位置”、“代码位置”。
画面8：PPT 标题为“7.2.1 Mapper”，内容包括“ApArticleConfigMapper 中新增方法”、“SQL 查询语句”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

