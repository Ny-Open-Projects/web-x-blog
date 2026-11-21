# 13_文章首页接口改造_后端_controller代码编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\13_文章首页接口改造_后端_controller代码编写【海量资源尽在 666java.com】.mp4
- 时长 3分32秒（音频 212s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好继续往下讲刚才这个Service咱们已经写完了下面咱们就写Controller这时候你需要在这去创建一个Controller是v2版本的所以说咱们在这再去创建一个包这包叫做Controller下边的v2然后你就可以在这里边去创建咱们的这个类叫做什么咱们叫做什么叫article t s l e或是article home
[00:32] 号码v2方式叫Controller好让他同时也去实现之前的叫什么叫article然后是叫home奇怪了home然后是Controller API它是有三个方法咱们需要去重写下分别是loadload more和load new这个首先要去加上这东西叫什么叫restcontroller再加一个叫什么request mapping
[01:03] 在这个地址是不一样的记得要注意一下他们是叫什么来着API然后是V2然后是ARTICLE这是ARTICLE最终咱们就可以去一个一个去设置了首先你要去输入前的Service还是前Service叫APPARTICLEservice好吧加上之后的时候你在这去可以去加你的在下边加
[01:34] 都一样啊再一个叫post mapping别错了啊post mapping好第一个呢是叫做loadload啊load第二个呢咱们可以去拷贝一下那是叫做load more不是小写啊然后下面是一个load new加完之后呢那这个这个调用的方法肯定是不太一样的啊这时候咱们可以去照用load v2
[02:11] 首先第一个值咱们还是当前的ArticleConstants点有一个叫做load默认都是load最终咱们可以把DTO装进去然后你说第三个猜数是force还是true第一个猜数是true只有load如果load的话它会打开首页的时候第一次会加载的是load所以说它肯定是首页
[02:43] 但是你打开之后你可以上拉或者下拉去加的更多或者加的更新的时候这个就不是处理所以说咱们可以把它拷过来拷过来之后拷过来这个就是first这个也是first好当然这个也不是load mode这是什么这是load new改一改好有问题是吧稍微改一改这样就可以了
[03:18] 这样的话咱们这个前的这种control啊也算是改造完了然后下面呢咱们就可以去把前端也给写了然后呢咱们可以把这个地址改完之后呢一块来去测试一下好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

