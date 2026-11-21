# 画面线理解：13_文章首页接口改造_后端_controller代码编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\13_文章首页接口改造_后端_controller代码编写【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:07, 00:13, 00:24, 00:56, 01:01, 01:25, 01:40, 02:09, 02:15, 02:26, 02:53, 03:03, 03:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:54:20

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中为 ArticleHomeV2Controller 添加注解和方法，实现分页加载文章列表的功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 ArticleHomeV2Controller.java 文件中 loadV2 方法的实现，其中包含对用户行为记录的查询和文章列表的加载逻辑。
画面 2: 展示了 ArticleHomeV2Controller.java 文件中 load 方法的实现，其中包含对文章最大浏览时间和最小浏览时间的设置。
画面 3: 展示了在 IDEA 中右键点击 ArticleHomeV2Controller.java 文件，弹出“New”菜单，准备创建新文件。
画面 4: 展示了在 IDEA 中右键点击 ArticleHomeV2Controller.java 文件，弹出“New”菜单，准备创建新文件。
画面 5: 展示了 ArticleHomeV2Controller.java 文件中 load、loadMore、loadNew 方法的定义，但方法体均为 return null。
画面 6: 展示了在 ArticleHomeV2Controller.java 文件中，光标位于 @RestController 注解上，下方弹出提示“@RestController is a stereotype annotation...”。
画面 7: 展示了 ArticleHomeV2Controller.java 文件中，光标位于 @RestController 注解上，下方弹出提示“@RestController is a stereotype annotation...”。
画面 8: 展示了 ArticleHomeV2Controller.java 文件中，光标位于 @RestController 注解上，下方弹出提示“@RestController is a stereotype annotation...”。
画面 9: 展示了 ArticleHomeV2Controller.java 文件中，光标位于 @RestController 注解上，下方弹出提示“@RestController is a stereotype annotation...”。
画面 10: 展示了 ArticleHomeV2Controller.java 文件中，光标位于 @RestController 注解上，下方弹出提示“@RestController is a stereotype annotation...”。
画面 11: 展示了 ArticleHomeV2Controller.java 文件中，光标位于 @RestController 注解上，下方弹出提示“@RestController is a stereotype annotation...”。
画面 12: 展示了 ArticleHomeV2Controller.java 文件中，光标位于 @RestController 注解上，下方弹出提示“@RestController is a stereotype annotation...”。
画面 13: 展示了 ArticleHomeV2Controller.java 文件中，光标位于 @RestController 注解上，下方弹出提示“@RestController is a stereotype annotation...”。
画面 14: 展示了 ArticleHomeV2Controller.java 文件中，光标位于 @RestController 注解上，下方弹出提示“@RestController is a stereotype annotation...”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
/**
 * @param user
 * @param dto
 * @param type
 * @return
 */
private List<Article> getUserArticleV2(ApUser user, ArticleHomeDto dto, Short type){
    // 用户没有不同同行为
    if(user == null){
        return Lists.newArrayList();
    }
    Long userId = user.getId();
    ApBehaviorEntry apBehaviorEntry = apBehaviorEntryMapper.selectByUserOrEquipmentId(userId, null);
    // 行为实体方法注释：这里注释掉，另外添加注释
    if(apBehaviorEntry == null){
        return Lists.newArrayList();
    }
    Integer entryId = apBehaviorEntry.getEntryId();
    // 如果没有找到，需要抛出异常
    if(entryId == null || entryId == 0){
        return Lists.newArrayList();
    }
    long time = System.currentTimeMillis();
    List<Article> list = apArticleMapper.loadArticleListByEntryId(entryId, dto, type);
    System.out.println("=====================" + (System.currentTimeMillis() - time));
    if(list.isEmpty()){
        List<Integer> articleList = list.stream().map(p -> p.getArticleId()).collect(Collectors.toList());
        List<Article> temp = apArticleMapper.loadArticleByIdListV2(articleList);
        System.out.println("articleList.size() = " + articleList.size());
        return temp;
    }
    return list;
}
```

画面 2:
```java
if(dto.getMaxBehotTime() == null){
    dto.setMinBehotTime(new Date());
}
if(dto.getMinBehotTime() == null){
    dto.setMinBehotTime(new Date());
}
//分页参数校验
Integer size = dto.getPageSize();
if(size == null || size < 0){
    size = 20;
}
size = Math.min(size, MAX_PAGE_SIZE);
dto.setPageSize(size);
//文章标签校验
if(StringUtils.isBlank(dto.getTag())){
    dto.setTag(ArticleConstants.DEFAULT_TAG);
}
```

画面 5:
```java
import com.heima.article.api.ArticleHomeControllerApi;
import com.heima.model.article.dto.ArticleHomeDto;
import com.heima.model.common.dto.ResponseResult;

public class ArticleHomeV2Controller implements ArticleHomeControllerApi {

    @Override
    public ResponseResult load(ArticleHomeDto dto) {
        return null;
    }

    @Override
    public ResponseResult loadMore(ArticleHomeDto dto) {
        return null;
    }

    @Override
    public ResponseResult loadNew(ArticleHomeDto dto) {
        return null;
    }
}
```

画面 6:
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v2/article")
public class ArticleHomeV2Controller implements ArticleHomeControllerApi {

    @Autowired
    private ApArticleService apArticleService;

    @Override
    public ResponseResult load(ArticleHomeDto dto) {
        return null;
    }

    @Override
    public ResponseResult loadMore(ArticleHomeDto dto) {
        return null;
    }

    @Override
    public ResponseResult loadNew(ArticleHomeDto dto) {
        return null;
    }
}
```

画面 7:
```java
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v2/article")
public class ArticleHomeV2Controller implements ArticleHomeControllerApi {

    @Autowired
    private ApArticleService apArticleService;

    @Override
    public ResponseResult load(ArticleHomeDto dto) {
        return null;
    }

    @Override
    public ResponseResult loadMore(ArticleHomeDto dto) {
        return null;
    }

    @Override
    public ResponseResult loadNew(ArticleHomeDto dto) {
        return null;
    }
}
```

画面 8:
```java
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v2/article")
public class ArticleHomeV2Controller implements ArticleHomeControllerApi {

    @Autowired
    private ApArticleService apArticleService;

    @Override
    public ResponseResult load(ArticleHomeDto dto) {
        return null;
    }

    @Override
    public ResponseResult loadMore(ArticleHomeDto dto) {
        return null;
    }

    @Override
    public ResponseResult loadNew(ArticleHomeDto dto) {
        return null;
    }
}
```

画面 9:
```java
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v2/article")
public class ArticleHomeV2Controller implements ArticleHomeControllerApi {

    @Autowired
    private ApArticleService apArticleService;

    @Override
    public ResponseResult load(ArticleHomeDto dto) {
        return null;
    }

    @Override
    public ResponseResult loadMore(ArticleHomeDto dto) {
        return null;
    }

    @Override
    public ResponseResult loadNew(ArticleHomeDto dto) {
        return null;
    }
}
```

画面 10:
```java
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v2/article")
public class ArticleHomeV2Controller implements ArticleHomeControllerApi {

    @Autowired
    private ApArticleService apArticleService;

    @Override
    public ResponseResult load(ArticleHomeDto dto) {
        return null;
    }

    @Override
    public ResponseResult loadMore(ArticleHomeDto dto) {
        return null;
    }

    @Override
    public ResponseResult loadNew(ArticleHomeDto dto) {
        return null;
    }
}
```

画面 11:
```java
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v2/article")
public class ArticleHomeV2Controller implements ArticleHomeControllerApi {

    @Autowired
    private ApArticleService apArticleService;

    @Override
    public ResponseResult load(ArticleHomeDto dto) {
        return null;
    }

    @Override
    public ResponseResult loadMore(ArticleHomeDto dto) {
        return null;
    }

    @Override
    public ResponseResult loadNew(Art
