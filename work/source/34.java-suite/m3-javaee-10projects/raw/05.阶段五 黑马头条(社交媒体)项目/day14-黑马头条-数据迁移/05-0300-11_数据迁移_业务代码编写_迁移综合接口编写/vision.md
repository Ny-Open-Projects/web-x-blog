# 画面线理解：11_数据迁移_业务代码编写_迁移综合接口编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\11_数据迁移_业务代码编写_迁移综合接口编写【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:23, 00:40, 01:07, 01:27, 01:37, 01:44, 02:21, 02:42, 03:10, 03:38, 04:28, 04:37, 04:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:06:22

1) 这一组画面整体在讲什么（一句话）：
在IDEA中编写和修改ArticleQuantityService接口，定义获取文章数量列表和根据文章ID获取文章数量的方法，并实现将数据同步到HBase的功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构，选中ArticleQuantityService接口文件，准备编写代码。
画面2：展示PPT内容，标题为“7.6 综合迁移接口”，说明接口位置为com.heima.migration.service.ArticleQuantityService。
画面3：展示ArticleQuantity类的字段定义，包括apArticle、apArticleConfig、apArticleContent、apAuthor、apBaseInvok等。
画面4：展示ArticleQuantityService接口中定义的三个方法：getArticleQuantityList()、getArticleQuantityByArticleId(Long id)、dbToHbase()。
画面5：在IDEA中右键“service”目录，弹出菜单，准备创建新文件。
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
接口位置：com.heima.migration.service.ArticleQuantityService
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
package com.heima.migration.service;
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
package com.heima.migration.service;
public interface ArticleQuantityService {
    public List<Article>
```

画面8：
```
package com.heima.migration.service;
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
package com.heima.migration.service;
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
package com.heima.migration.service;
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
package com.heima.migration.service;
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
package com.heima.migration.service;
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
package com.heima.migration.service;
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
package com.heima.migration.service;
import com.heima.migration.entity.ArticleQuantity;
import java.util.List;
public interface ArticleQuantityService {
    // 获取ArticleQuantity列表
    @Return
    /
    public List<ArticleQuantity> getArticleQuantityList();
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：PPT标题为“7.6 综合迁移接口”，内容说明接口位置为com.heima.migration.service.ArticleQuantityService。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
