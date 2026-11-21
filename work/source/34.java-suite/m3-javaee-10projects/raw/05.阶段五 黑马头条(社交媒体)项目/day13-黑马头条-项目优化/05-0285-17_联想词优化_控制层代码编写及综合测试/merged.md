# 17_联想词优化_控制层代码编写及综合测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\17_联想词优化_控制层代码编写及综合测试【海量资源尽在 666java.com】.mp4
- 时长 7分38秒（音频 458s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就继续往下讲那这Controller还没有写咱们这个是好是一个Controller第二版本v2版本的Controller咱们在这就要去拿给编写一下那这个咱们还是在之前的这个Controller v2中在这去创建一个类这个类就是当前的v2版本在这打去打开右键一个class然后它是跟之前的是一样的
[00:31] 同样的需要去实现当前那个API然后呢是这么个东西考一下那你也可以从之前的代码中去拿过来也行叫article search好吧这边有有那么多方法啊那么多方法那有这些方法该怎么去写呢那其实呢咱们只需要去改一个改一个就改最后一个就可以了啊这一个呢是一个vr版本其他的呢咱们都不变啊其他都不变啊所以说咱们在这还要去诸
[01:02] 注入一个什么呢,叫article search Controller没有search吗,怎么叫AP是吧,我看看啊AP article search Service,那就它然后呢你注入进来注进来之后呢,这时候呢你就可以去调用方法啊,还有一个find,把当前地球转进去啊
[01:33] 然后下面这个东西也是有一样咱们可以这样咱们可以从之前的单本中考一下咱们叫search前面东西基本上都一样咱们都考过来得了都考过来从这考到这考完之后这个路径也不变上面路径得变了这是v2下面这个小路径是不变的只有这变了然后下面这有一个东西咱们需要改就是这个东西就是这这的话咱们需要去加一个v
[02:09] 没有吗啊色尺哎啊是二个门啊那行改这一柱就可以啊是咱们的control也就是咱们的控制层咱们就写到这啊那写完之后啊咱们下面呢还有一个东西需要改啊就是前端的这个地儿啊你要改就是改当前的这种接口的路径就可以了啊你看这我已经标明了啊你打开当前的这个东西这是有一个commoncommon下面有一个config.js里边呢这是有一个叫做他
[02:39] 它之后你又可以改成谁改成2改成22之后这个应该会自动启动一下咱们下面就可以在这打个断点打一个断点然后咱们就在这去怎么着重启一下当前的Article没有启动是吧那要启动一下好稍等然后启动完之后咱们在这一块就可以去进行搜索来看看这个效果好吧好稍等一下
[03:29] 应该是快完了现在这样咱们就可以去登录一下点登录登录完以后这时候他应该去查询这个数据还没有做完是吗稍等数据还没查到稍等咱们可以刷新一下再重新去登录一下稍等好点登录走这个数据还没有拿到是吧这个还是挺慢的是吧启动的时候有没有报错
[04:19] 好像也没有报错是吧报错了啊说你什么呢说有一个东西启动失败了说卡不卡呀Timeout了咱们这个网应该是连的不好这样啊咱们再来去刷一下应该这次就好了因为我这个网刚才网线松了一下那咱们下面再来去测试一下点登录数据还是没有查着不行就重启下载
[05:01] 咱们在这搜索一下啊直接去判断搜索一下啊这个当前这个网好像不太好啊咱们去搜索一下搜索那搜索搜索谁呢搜索的是当前的比如说搜黑马看看好用不好用啊这个的确是不好用啊咱们下面就再去重启一下啊好那这边重启完了啊什么也没动啊就重启完了重启完之后呢在这啊你可以去登录你看这个数据是不是拿到了没问题啊
[05:32] 这时候咱们主要测的是当前搜索雷向磁这一块比如说我把这个都在关掉删掉其实不删也不影响咱们先去搜一个什么搜一个黑马因为这里边有一些东西你看有黑马开头的看到了吗有上海有广州是吧咱们下面就可以去搜比如说我先去搜一个黑马黑马没有搜着并不是没有搜着是因为我在这打断点了比如说我先去给他他是的确走的是VR版本我现在放行
[06:03] 发行完之后你们可以再来测试一下先去测试一下黑码是不是能搜到如果我再去搜黑码程是不是有程序然后再去程序员是不是都有提示这样的话咱们这个字典数它这个效率还是挺高的这个现在感受不出来但是现在你已经知道我们直接查搜索的时候直接查的并不是数据库应该是谁应该是当前的
[06:31] 这么这样咱们可以在哪打断点呢在当前的打断点看看这里边有没有数据那有数据的话肯定就不会走这个数据过差区了是吧好来比如说我还搜黑马我来看一下往下走看这个里边是不是有数据是吧没问题然后你就往下去执行执行执行执行执行这时候他先去往里边去插入数据然后
[07:01] 你再去根据当前的关键词去搜索去当前的输入结构中去搜索那这样的话这个效率就高了好吧那行那这个咱们就算是做完了啊这个效果刚才也出来了当然你也可以再去测试一下比如说我去抽一个传至播客传啊这有断点是吧有断点啊把断点先去掉啊要不然的话他的一个影响啊我搜传播客是不是都有提示啊
[07:33] 这样的话咱们这个功能就算是做完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个文章搜索服务的 V2 版本控制器与服务层代码实现，以及在调试过程中遇到的 Kafka 连接失败问题和最终的修复过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 项目结构：`heima-leadnews-article`，选中 `ApArticleSearchService`。
- 代码：`ApArticleSearchServiceImpl.java` 中的 `searchAssociationV2` 方法，使用 `Trie` 管理关联词，调用 `startWith` 获取搜索词，构建 `ApAssociateWords` 对象列表并返回。

画面 2：
- 项目结构：选中 `ArticleSearchV2Controller`。
- 代码：`ArticleSearchV2Controller.java`，`@RestController` 注解，`@RequestMapping("/api/v2/article/search")`，实现 `ArticleSearchControllerApi` 接口。

画面 3：
- 代码：`ArticleSearchV2Controller.java`，定义了 `findUserSearch`、`delUserSearch`、`clearUserSearch` 方法，均返回 `null`。

画面 4：
- 项目结构：选中 `ArticleSearchV2Controller`。
- 代码：`ArticleSearchV2Controller.java`，`@Autowired private ApArticleSearchService apArticleSearchService;`，定义了 `findUserSearch`、`delUserSearch`、`clearUserSearch` 方法。

画面 5：
- PPT 内容：标题为“v2技术的Controller”，列出 `@PostMapping("load_search_history")`、`@PostMapping("del_search")`、`@PostMapping("clear_search")`、`@PostMapping("associate_search")` 等方法。

画面 6：
- 网页界面：显示一个登录页面和一个二维码，提示使用 Weex playground app 扫描。

画面 7：
- 代码：`ArticleSearchV2Controller.java`，`@PostMapping("/associate_search")` 方法，调用 `apArticleSearchService.searchAssociationV2(dto)`。

画面 8：
- 控制台日志：显示 Kafka 连接失败的错误信息，如 `Connection to node -1 could not be established. Broker may not be available.`。

画面 9：
- 控制台日志：继续显示 Kafka 连接失败的错误信息。

画面 10：
- 控制台日志：显示 Spring 应用启动失败，原因是 Kafka 连接失败。

画面 11：
- 代码：`ArticleSearchV2Controller.java`，`@PostMapping("/associate_search")` 方法，调用 `apArticleSearchService.searchAssociationV2(dto)`。

画面 12：
- 调试器：断点在 `searchAssociationV2` 方法中，显示 `this` 为 `ApArticleSearchServiceImpl`，`dto` 为 `UserSearchDto`，`apAssociateWordsMapper` 为 `null`。

画面 13：
- 调试器：断点在 `searchAssociationV2` 方法中，显示 `apAssociateWordsMapper` 为 `null`，`aw` 为 `null`。

画面 14：
- 代码：`ApArticleSearchServiceImpl.java`，`searchAssociationV2` 方法中，`if (StringUtils.isBlank(assoStr)) { ... } else { ... }`，`aw = apAssociateWordsMapper.selectAll(ApAssociateWords.class)`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
//使用 trie树进行管理词组
Trie t = new Trie();
for (ApAssociateWords a : aw) {
    t.insert(a.getAssociateWords());
}
List<String> ret = t.startWith(dto.getSearchWords());
for (String s : ret) {
    ApAssociateWords apAssociateWords = new ApAssociateWords();
    apAssociateWords.setAssociateWords(s);
    list.add(apAssociateWords);
}
return ResponseResult.okResult(list);
```

画面 2：
```java
package com.heima.article.Controller.v2;
import com.heima.article.apis.ArticleSearchControllerApi;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/api/v2/article/search")
public class ArticleSearchV2Controller implements ArticleSearchControllerApi {
```

画面 3：
```java
@RestController
@RequestMapping("/api/v2/article/search")
public class ArticleSearchV2Controller implements ArticleSearchControllerApi {
    @Override
    public ResponseResult findUserSearch(UserSearchDto dto) {
        return null;
    }
    @Override
    public ResponseResult delUserSearch(UserSearchDto dto) {
        return null;
    }
    @Override
    public ResponseResult clearUserSearch(UserSearchDto dto) {
        return null;
    }
```

画面 4：
```java
@RestController
@RequestMapping("/api/v2/article/search")
public class ArticleSearchV2Controller implements ArticleSearchControllerApi {
    @Autowired
    private ApArticleSearchService apArticleSearchService;
    @Override
    public ResponseResult findUserSearch(UserSearchDto dto) {
        return apArticleSearchService.findUserSearch(dto);
    }
    @Override
    public ResponseResult delUserSearch(UserSearchDto dto) {
        return apArticleSearchService.delUserSearch(dto);
    }
    @Override
    public ResponseResult clearUserSearch(UserSearchDto dto) {
        return apArticleSearchService.clearUserSearch(dto);
    }
    @Override
    public ResponseResult searchAssociate(UserSearchDto dto) {
        return apArticleSearchService.searchAssociationV2(dto);
    }
```

画面 5：
```java
@RestController
@RequestMapping("/api/v2/article/search")
public class ArticleSearchV2Controller implements ArticleSearchControllerApi {
    @Autowired
    private ApArticleSearchService apArticleSearchService;
    @PostMapping("load_search_history")
    public ResponseResult findUserSearch(@RequestBody UserSearchDto userSearchDto) {
        return apArticleSearchService.findUserSearch(userSearchDto);
    }
    @PostMapping("del_search")
    public ResponseResult delUserSearch(@RequestBody UserSearchDto userSearchDto) {
        return apArticleSearchService.delUserSearch(userSearchDto);
    }
    @PostMapping("clear_search")
    public ResponseResult clearUserSearch(@RequestBody UserSearchDto userSearchDto) {
        return apArticleSearchService.clearUserSearch(userSearchDto);
    }
    @PostMapping("associate_search")
    public ResponseResult searchAssociate(@RequestBody UserSearchDto dto) {
        return apArticleSearchService.searchAssociationV2(dto);
    }
```

画面 7：
```java
@PostMapping("/associate_search")
public ResponseResult searchAssociate(@RequestBody UserSearchDto dto) {
    return apArticleSearchService.searchAssociationV2(dto);
}
```

画面 12：
```java
@Override
public ResponseResult searchAssociationV2(UserSearchDto dto) {
    if (dto == null || dto.getPageSize() > 50) {
        return ResponseResult.errorResult(ApIdt.pcodeEnum.PARAM_INVALID);
    }
    String assoStr = redisTemplate.opsForValue().get("associate_list");
    List<ApAssociateWords> aw = null;
    if (StringUtils.isBlank(assoStr)) {
        aw = JSON.parseArray(assoStr, ApAssociateWords.class);
    } else {
        aw = apAssociateWordsMapper.selectAll(ApAssociateWords.class);
    }
    return ResponseResult.okResult(aw);
}
```

画面 14：
```java
@Override
public ResponseResult searchAssociationV2(UserSearchDto dto) {
    if (dto == null || dto.getPageSize() > 50) {
        return ResponseResult.errorResult(ApIdt.pcodeEnum.PARAM_INVALID);
    }
    String assoStr = redisTemplate.opsForValue().get("associate_list");
    List<ApAssociateWords> aw = null;
    if (StringUtils.isBlank(assoStr)) {
        aw = JSON.parseArray(assoStr, ApAssociateWords.class);
    } else {
        aw = apAssociateWordsMapper.selectAll(ApAssociateWords.class);
    }
    return ResponseResult.okResult(aw);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 5：
- PPT 标题：v2技术的Controller
- 内容：
  - 3.1 功能需求
  - 3.2 前端实现
  - 3.3 接口如何
  - 3.3.1 基本定义
  - 3.3.2 COOL定义
  - 3.3.3 Map结构
  - 3.3.4 工具类说明
  - 3.3.5 时间说明
  - 3.3.6 工具类说明
  - 3.3.7 代码实现
  - 4.1 接口需求
  - 4.2 接口实现
  - 4.2.1 COOL定义
  - 4.2.2 Map结构
  - 4.2.3 工具类说明
  - 4.2.4 工具类说明
  - 4.2.5 代码实现

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求完成）

