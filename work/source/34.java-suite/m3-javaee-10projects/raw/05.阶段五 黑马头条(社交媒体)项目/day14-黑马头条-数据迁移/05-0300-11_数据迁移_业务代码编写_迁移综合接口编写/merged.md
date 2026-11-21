# 11_数据迁移_业务代码编写_迁移综合接口编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\11_数据迁移_业务代码编写_迁移综合接口编写【海量资源尽在 666java.com】.mp4
- 时长 5分24秒（音频 324s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们来定义当前的这个叫综合的迁移接口那这个接口啊其实非常重要里边的方法呢也特别多那它主要是干啥事呢主要的是封装了文章相关的数据其实呢就是咱们刚才定义的这四个都是为当前的这个接口服务的咱们可以看一下里边的方法啊首先呢是获取的当前的一个什么quantityquantity是吧article quantity
[00:29] 这个对象大家还有印象吗可以看一下这个对象其实就是它综合了当前的文章文章的配置文章的内容还有作者里边还有一个回调的函数是吧这里边其实就它就包含了刚才咱们说的那些4个机口里边的内容好吧这是第一个是获取然后第二个是获取一个这个是根据当前的文章it去获取一个
[00:56] 因为文章ID跟其他4个都有关系好吧还有一个就是咱们需要去从哪从当前的HBase中去查询一个那种过来你说有查询当然咱们也会去插入咱们会去从数据库同步到哪同步到HBase还有一个就是咱们会从当前的一个根据当前的文章ID然后是同步到当前的HBase好吧就这么些方法咱们下面就来去定义当前的Service
[01:25] 好背下然后在这去创建一个接口这是一个接口Article Quantity Service然后咱们就去定义方法Public然后第一个是叫做返回一个list集合里边是叫ArticleTiCleQuantity打个包然后第一个是叫做getArticleQuantityTiTiTi然后是list好吧这是没有参数的这是获取
[02:02] 获取这个综合吧Article综合啊Article然后是Quantity那边好吧下面咱们再获取一个啊获取一个Public然后是叫ArticleQuantity就它然后是这啥呢GetArticleArticle然后是Quantity就有antity然后是BuyArticleID好
[02:39] 这个装的就是一个lang类型的lang类型的ID这是根据主件应该是根据文章ID根据文章ID然后是查询好这是第二个是吧咱们再来看第三个第三个咱们要去定义当前的什么从当前的HBase中去查查询的也是
[03:12] ArticleQuantity,然后是getArticleQuantity好然后是byArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticleArticle
[03:49] 从哪儿啊HBase中查询谁啊查询他好那咱们下面继续啊还有两个方法咱们消息定义这个呢就是Public然后是Void然后是DBHBase第一个呢是没有参数的啊下面还有一个有参数的那这个呢就是数据库同步到哪儿啊H
[04:23] 还有一个再参数的是public void db to h base这里边是有参数叫lang类型的IDlang类型还是integer类型看啊是个integer的ID是吧也行好吧什么意思是根据文章ID然后是将数据库将
[05:04] 数据库的数据同步到HList中好吧行那这个方法咱们就算是定义完了那咱们下面就来去定义它的实现我这个视频先断一下咱们一会儿再去写实现实现的这个代码还是比较多的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在IDEA中编写和修改ArticleQuantityService接口，定义获取文章数量列表和根据文章ID获取文章数量的方法，并实现将数据同步到HBase的功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构，选中ArticleQuantityService接口文件，准备编写代码。
画面2：展示PPT内容，标题为“7.6 综合迁移接口”，说明接口位置为com.heima.migration.Service.ArticleQuantityService。
画面3：展示ArticleQuantity类的字段定义，包括apArticle、apArticleConfig、apArticleContent、apAuthor、apBaseInvok等。
画面4：展示ArticleQuantityService接口中定义的三个方法：getArticleQuantityList()、getArticleQuantityByArticleId(Long id)、dbToHbase()。
画面5：在IDEA中右键“Service”目录，弹出菜单，准备创建新文件。
画面6：在ArticleQuantityService接口中，光标位于“public”关键字前，准备修改访问修饰符。
画面7：在ArticleQuantityService接口中，光标位于“public List<Article>”前，准备修改返回类型。
画面8：在ArticleQuantityService接口中，光标位于“public List<ArticleQuantity>”前，准备修改返回类型。
画面9：在ArticleQuantityService接口中，光标位于“public List<ArticleQuantity> getArticleQuantityList()”前，准备修改方法签名。
画面10：在ArticleQuantityService接口中，光标位于“public ArticleQuantity getArticleQuantityByArticleId(Long id)”前，准备修改方法签名。
画面11：在ArticleQuantityService接口中，光标位于“public ArticleQuantity getArticleQuantityByArticleIdForHbase(Long id)”前，准备修改方法签名。
画面12：在ArticleQuantityService接口中，光标位于“public void dbToHbase()”前，准备修改方法签名。
画面13：在ArticleQuantityService接口中，光标位于“public void dbToHbase(Long id)”前，准备修改方法签名。
画面14：在ArticleQuantityService接口中，光标位于“public void dbToHbase(Long id)”后，方法已定义完成。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```
7.6 综合迁移接口
ArticleQuantityService
操作ArticleQuantity对象的Service ArticleQuantity对象对文章相关的数据
接口位置：com.heima.migration.Service.ArticleQuantityService
```

画面3：
```
private ApArticle apArticle.
// 文章配置实体
private ApArticleConfig apArticleConfig.
// 文章内容实体
private ApArticleContent apArticleContent.
// 文章作者实体
private ApAuthor apAuthor.
// 调接口
private HBaseInvok apBaseInvok;
```

画面4：
```
// 获取ArticleQuantity列表
@Return
/
public List<ArticleQuantity> getArticleQuantityList();

// 根据ArticleId获取ArticleQuantity
@Param id
@Return
/
public ArticleQuantity getArticleQuantityByArticleId(Long id);

// 根据ArticleId从HBase中获取ArticleQuantity
@Param id
@Return
/
public ArticleQuantity getArticleQuantityByArticleIdForHbase(Long id);

// 数据同步到HBase
@Return
/
public void dbToHbase();

// 根据articleId 消费数据同步到HBase
@Param articleId
@Return
/
public void dbToHbase(Integer articleId);
```

画面6：
```
package com.heima.migration.Service;
public interface ArticleQuantityService {
    protected
    public
    Package (java.lang)
    Process (java.lang)
    ProcessBuilder (java.lang)
    pause
    main() method declaration
    pruf
    private static final
    prfi
    public static final int
    prefs
    public static final String
    Co- and Ce- will move soon down and up in the editor
```

画面7：
```
package com.heima.migration.Service;
public interface ArticleQuantityService {
    public List<Article>
```

画面8：
```
package com.heima.migration.Service;
import com.heima.migration.entity.ArticleQuantity;
import java.util.List;
public interface ArticleQuantityService {
    // 获取ArticleQuantity列表
    @Return
    /
    public List<ArticleQuantity> getArticleQuantityList();
```

画面9：
```
package com.heima.migration.Service;
import com.heima.migration.entity.ArticleQuantity;
import java.util.List;
public interface ArticleQuantityService {
    // 获取ArticleQuantity列表
    @Return
    /
    public List<ArticleQuantity> getArticleQuantityList();
```

画面10：
```
package com.heima.migration.Service;
import com.heima.migration.entity.ArticleQuantity;
import java.util.List;
public interface ArticleQuantityService {
    // 获取ArticleQuantity列表
    @Return
    /
    public List<ArticleQuantity> getArticleQuantityList();
```

画面11：
```
package com.heima.migration.Service;
import com.heima.migration.entity.ArticleQuantity;
import java.util.List;
public interface ArticleQuantityService {
    // 获取ArticleQuantity列表
    @Return
    /
    public List<ArticleQuantity> getArticleQuantityList();
```

画面12：
```
package com.heima.migration.Service;
import com.heima.migration.entity.ArticleQuantity;
import java.util.List;
public interface ArticleQuantityService {
    // 获取ArticleQuantity列表
    @Return
    /
    public List<ArticleQuantity> getArticleQuantityList();
```

画面13：
```
package com.heima.migration.Service;
import com.heima.migration.entity.ArticleQuantity;
import java.util.List;
public interface ArticleQuantityService {
    // 获取ArticleQuantity列表
    @Return
    /
    public List<ArticleQuantity> getArticleQuantityList();
```

画面14：
```
package com.heima.migration.Service;
import com.heima.migration.entity.ArticleQuantity;
import java.util.List;
public interface ArticleQuantityService {
    // 获取ArticleQuantity列表
    @Return
    /
    public List<ArticleQuantity> getArticleQuantityList();
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：PPT标题为“7.6 综合迁移接口”，内容说明接口位置为com.heima.migration.Service.ArticleQuantityService。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

