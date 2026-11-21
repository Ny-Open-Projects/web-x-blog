# 15_app搜索_文章搜索接口_代码完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\15_app搜索_文章搜索接口_代码完成【海量资源尽在 666java.com】.mp4
- 时长 17分6秒（音频 1027s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来完成当前文章的搜索啊那咱们还是老套路首先呢还是得去分析一下当前这个代码的思路啊那首先呢咱们要做的第一个事呢就是要去记录记录那个搜索就保存吧保存搜索记录然后第二个呢咱们就去构建查询条件啊构建查询条件那基于谁呢那肯定是咱们在这啊先要去出入一个
[00:31] private test plant这个东西这个东西是不是就可以去连上当前的.4然后去搜寻物种去查询数据所以说咱们这去基于它去固建查询条件但是查询条件的话不换哪些呢不换哪些比如咱们要去设置什么关键字按照关键字查询关键字还有什么分页查询最终咱们就可以干嘛呢获取
[01:06] 结果获取结果行其实就这四大步咱们一步一步去实现首先保存搜索记录其实咱们已经做完了就是上面这个方法咱们只需要去调用上面这个方法就可以了这块其实还设计了个东西咱们要去判断一下判断啥要判断前的什么再特一个什么那这个其实就是页码等于0的时候我再去调用
[01:37] 我再去用当前的保存为什么等于0的时候保存呢因为这会儿写一下只在第一页按旋的时候进行保存同一个关键字它可能搜出来有五六页咱们在第一页的时候只需要做一次保存就可以第二页第三页的时候咱们不需要再进行保存了这个能明白吧行了啊行那这个咱们做了一个判断然后下面呢咱们就去保存那保存的时候
[02:12] 他是不是需要两个参数啊第一个是NGID第二是search words那这search words咱们有那NGID有吗没有没有就拿呗这个咱们之前是不是获取过呀我往下往下拉啊咱们这有一个方法叫getNGID这个传的就是DTO然后返回了当前的一个Ret吧好吧返回这个他然后咱们就去判断啊如果说呢Ret有什么getcode
[02:44] 不等于谁不等于app http enumer.enumer.success而getcode如果说它不成功的话咱们就直接去返回当下的RET就可以了如果说它成功了那说明数据已经拿到了拿到之后咱们就可以保存了保存的方式就是你直接去调用就可以了save user search第一个参数怎么这样了第一个参数就是RET的什么
[03:14] 这个呢就是当前的AndroidD第二个呢就是DTO中的什么Search Words是Get好那这样就完了啊包错的话呢其实他就是要去转换一下啊咱们转换成int类型就可以啊那这样的话咱们就算是做了一个保存的操作好吧现在做完保存之后呢那咱们下面呢就来去构建构建查询对象了啊那构建查询对象之前呢咱们还是要去使用这个
[03:46] 这一次client首先咱们在这儿有一个cute,cute里边咱们需要去设置一个什么设置一个这种action,这个action可以看一下这个action是个接口,这个接口接口咱们最终的可能使用接口,咱们要使用它的一个什么它的一个实现,这个实现咱们用哪个呢实现的有很多是吧咱们用的是一个search,找一找这个search咱们用的是当前这个search
[04:17] 行那咱们就可以构建一个search把它给删了search好search等于什么呢等于new一个search这里边咱们需要去需要去构建一个查询查询的话其实里边就可以去构建一个查询咱们在这儿可以往后去build之前咱们还可以设置一些参数
[04:47] 说你要在哪个输入库中去操作我们可以add index然后呢咱们还可以干嘛呢add type咱们都可以去设置其中再去build管事的好吧这个啊这个这个咱们一会一会再去说首先是构建一个查询条件咱们咱们先构建出来啊这个查询条件呢咱们就叫啥呢search source builderok search source builder等于new一个search source builder
[05:19] 最终咱们就可以把这个search source builder到这出示论一下那index是咱们之前在我们这个common这个工程下边去定义的一些常量咱们这个索引库的名称其实都在这已经定义好了打开common里边有一个constance里边有一个esindexconstance里边是有一个你看首先第一个这个其实就是文章的这种索引名称还有一个默认的类型对吧
[05:50] 所以说咱们在这都可以去设置这个类型的话就是esindexesindexconstancecomment下边的articleindex就它type呢还是这里边esindexconstance
[06:27] 有个Defund DOC其实就是这个技术类型好吧我们就为了方便看咱们直接可以回家车好那这样的话咱们就算是设置完了装在这里边它就需要一个search因为这个search就是当前那个AXIE那个什么实现类是吧这样就算是设置完了这个包错了是吧包错的话它需要去抛下一场我们可以踹一下好了这样就设置完了设置完之后其实这东西咱们还没有构建条件
[06:57] 那构建条件的话这样啊是按照当前的关键字和分页去构建条件在这啊咱们就可以直接去构建条件了啊其实你直接放到上面也行啊那这个里边啊咱们就可以去设置一些参数了比如说啊什么呢有一个qrayqray里边是不是可以装一个qray builder这个builder呢qray builder呢就可以构建一些条件好咱们点一下啊里边呢可以装一个qray
[07:28] 然后咱们可以去match, 咱们可以去模糊匹配模糊匹配啥呢, 叫哪个域容呢首先第一个字段是域, 然后第二个字段是你的参数tto.getSearchWords咱们通常的话都是在哪个域都是在咱们的title中好, 那这个title你不能随便写
[07:53] 这个呢是要跟你的域的名称要对应上的啊你可以打开咱们之前再去设置域的时候啊往下走好的啊这有点快啊这啊你可以参考一下当前这个域的名称比如说有什么啊Channel ID有Content下边有没有title呢可以看一下啊是不是有标题啊咱们是都有标题的啊行那这个咱们设置完之后呢咱们继续往下看啊
[08:23] 然后这个是有一个按照关键字去查询然后下面还有还有啥呢咱们要要去分页分页说这啥说说这哪个呢还是他好而这个是flom好这个呢你又可以去传个参数怎么dto.flom index这个就是70页下面还有啥呢search folder size你可以去传一个dto.at sizeok那这样
[08:55] 我们就算是设置了一页那这个条件呢咱们都已经构建完了然后下面咱们就要去取结果那这个结果该怎么取呢你看啊其实这个呢就这块它是有返回值的来看一下啊返回值呢是一个叫做search result吧好吧这里边呢咱们就可以去拿到某一些类型的值比如说啊search result点它里边有个方法叫什么getSource
[09:26] as object list我们就可以用当前的这个东西好那咱们就回下车啊用的第一个参数呢咱们主要是有一个AP article咱们要转换成当前的一个类型这样就说的完了啊它返回的其实就是一个什么一个叫好吧那返回的就是一个article咱们最终返回的是不是也是它呀
[09:55] 最终这个接口返回的就是一个历史记号里边装的都是一些文章类表信息好了啊那最终那你说他能直接返回吗不能啊为什么不能呢因为防止这个信息不全不知道大家还没有印象咱们之前呢是在这里边啊去做了一个东西做了两个东西呢看看啊在这是不是做了一个查询文章的信息根据ID啊所以说咱们在这啊需要去多做一步怎么做呢来看啊
[10:24] 在这去这个循环AP article.for好吧咱们循环完之后呢拿到里边的ID去查询查询啥呢就是查询当前的文章这时候咱们可以把当前的mypro给注入进来啊private ap article mypro好注入下来之后呢咱们就可以根据ID去查询了在这.slide by id然后这里边是AP
[11:00] article.getid 干净完了啊那是报错了其实它是个lang的型啊咱们可以去转换一下lang.valueof好把后边东西呢装进去就完事了啊那这样就可以了啊最终呢咱们你再给它重新复制再重新复制一下就好了啊那这样的话就可以了那最终呢你说它它要一个列表你是不是要返回一个列表啊所以说咱们在这啊再去专门的去创建一个list集合咱们叫resultlist
[11:33] 等于啥呢等于new一个arraylist好吧它呢是专门来存放这个什么过滤之后啊就是说你填充完数据之后的这种数据咱们也可以做判断if如果说它等于none怎么办呢咱们就让它continue也让它继续啊继续循环如果说都没问题的话呢我们就再去装到目前这个离合好add前的aparticleok那这样
[12:05] 最终你返回的时候呢那也很容易了returnreturn的response result.ok就把当前的result.ok了那这样的话其实就是你最终的一个文章的列表信息好吧当然这最后一个还有一个那这个返回结果咱们往上这个就是返回结果如果说它都不行的话如果说咱走到这的话肯定是有问题的我们就直接返回一个response result.ok
[12:36] 设置一个说你的参数有问题吧好吧APP好吧那这样的话咱们就这个接口啊咱们这个实现类啊就算是也完了啊顺便啊就把这个当前的Controller啊也给写了啊Controller打开当前的Controller这个就是当前的Controller啊那Controller里边呢咱们可以去调用当前的Service首先呢咱们不应该写Controller是吧先写谁呀先写他的一个接口啊就是当前的API在这去定一个方法啊public
[13:07] 然后是叫什么ES article好吧Article search好传输参数呢就是user search好了啊最终这个东西啊这个东西呢就是根据啥呢ES文分页查询好吧那么下面就写具体的Controller
[13:43] article好了啊那写完之后呢那咱们下面呢就去把这个东西给补全啊他叫啥呢这叫啊这叫article search加一个request body中咱们可以去调用我们的Service而search ps啊ps article然后把地图装进去我给他这样出了啊接着完之后呢咱们顺便啊可以再去测试一下测试一下
[14:21] 咱们拷贝一个上面的内容这个方法名咱们就打改一改就关了这是这个方法名方法名改掉然后这是好吧然后再往下看这里边有一个article search把这个也改了我改完之后咱们就可以去设置一些值了设置值咱们可以看一下设置哪些值首先dto.set
[14:54] 咱们设备ID是不是要有有有有用要保存的时候需要有一个这东西还有啥呢这里边咱们还要去设置一个dto点咱们可以看一下有点set number需要预设置吗也就是页面需要设置吧设置个1是dto点set page size要设置吗需要设置个10随便设然后再去设置一个非常关键的就是目前的set search words
[15:25] 那这个search words你可以随便去找一个东西去那个那个可以去先去搜一个什么黑马程序员好吧看看有没有ES库中有没有关于黑马程序员的文章好来稍等啊我们再加载他要是有的话他应该会打印出来啊好这是绿色的应该是没有问题这个文章其实已经查出来了看到了吗只有一条文章啊只有一条应该是只有一条的啊
[16:06] 你看当然你也可以去搜一下其他的只要是你的搜影库中存在的啊你都可以搜啊搜影库中存在的都可以搜比如说咱们再搜一个吧那么多是吧找一个title啊因为咱们最终过滤的是titletitle比如说呃面试好吧咱们搜个面试吧来面试再去搜一下啊看看行不行啊好你要测试的时候一定要注意啊就是title当前的这个预测型啊
[16:41] 这个内容语咱们并没有进行去查询啊好稍等啊看一看啊你看这个是不是面试详细分析是不是当前这个文章信息也查到了呀OK那没问题啊那最终呢咱们这个查询文章的接口咱们就讲到这里啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中使用 Jest 客户端实现文章搜索功能，包括保存记录、构建查询条件、执行搜索并处理结果。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 `ApArticleSearchServiceImpl` 中的 `articleSearch` 方法，用于保存用户搜索记录，调用 `apUserSearchMapper.insert` 插入数据并返回响应结果。
画面2: 展示了 `ApArticleSearchServiceImpl` 中的 `articleSearch` 方法，添加了条件判断，如果 `fromIndex` 为 0 则返回 `getEntryId` 的响应结果。
画面3: 展示了 `ApArticleSearchServiceImpl` 中的 `articleSearch` 方法，添加了 `jestClient.execute` 用于构建和执行搜索条件。
画面4: 展示了 `ApArticleSearchServiceImpl` 中的 `articleSearch` 方法，使用 `SearchSourceBuilder` 构建搜索条件，调用 `jestClient.execute` 执行搜索。
画面5: 展示了 `ApArticleSearchServiceImpl` 中的 `articleSearch` 方法，使用 `SearchSourceBuilder` 构建搜索条件，调用 `jestClient.execute` 执行搜索。
画面6: 展示了 `ApArticleSearchServiceImpl` 中的 `articleSearch` 方法，使用 `SearchSourceBuilder` 构建搜索条件，调用 `jestClient.execute` 执行搜索。
画面7: 展示了 `ApArticleSearchServiceImpl` 中的 `articleSearch` 方法，使用 `SearchSourceBuilder` 构建搜索条件，调用 `jestClient.execute` 执行搜索。
画面8: 展示了 `ApArticleSearchServiceImpl` 中的 `articleSearch` 方法，使用 `SearchSourceBuilder` 构建搜索条件，调用 `jestClient.execute` 执行搜索，并处理返回的 `SearchResult`。
画面9: 展示了 `ApArticleSearchServiceImpl` 中的 `articleSearch` 方法，使用 `SearchSourceBuilder` 构建搜索条件，调用 `jestClient.execute` 执行搜索，并处理返回的 `SearchResult`。
画面10: 展示了 `ArticleSearchController` 中的 `article_search` 方法，用于调用 `aparticleSearchService.articleSearch`。
画面11: 展示了 `ArticleSearchController` 中的 `article_search` 方法，用于调用 `aparticleSearchService.articleSearch`。
画面12: 展示了 `ArticleSearchControllerTest` 中的测试代码，使用 `MockMvc` 模拟请求并验证响应。
画面13: 展示了 Kibana 的 Console 页面，显示了 Elasticsearch 的索引映射配置。
画面14: 展示了 `ArticleSearchControllerTest` 中的测试代码，使用 `MockMvc` 模拟请求并验证响应。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```java
ApUserSearch apUserSearch = new ApUserSearch();
apUserSearch.setEntryId(entryId);
apUserSearch.setKeyword(searchWords);
apUserSearch.settStatus(1);
apUserSearch.setCreatedTime(new Date());
int insert = apUserSearchMapper.insert(apUserSearch);
return ResponseResult.okResult(insert);
```

画面2:
```java
@Override
public ResponseResult cArticleSearch(UserSearchDto dto) {
    if (dto.getFromIndex() == 0) {
        ResponseResult ret = getEntryId(dto);
        if (ret.getCode() == AppHttpCodeEnum.SUCCESS.getCode()) {
            return ret;
        }
    }
    saveUserSearch(int ret.getData(), dto.getSearchWords());
    //构建查询条件  jestClient
    jestClient.execute(
```

画面3:
```java
@Override
public ResponseResult cArticleSearch(UserSearchDto dto) {
    if (dto.getFromIndex() == 0) {
        ResponseResult ret = getEntryId(dto);
        if (ret.getCode() == AppHttpCodeEnum.SUCCESS.getCode()) {
            return ret;
        }
    }
    saveUserSearch(int ret.getData(), dto.getSearchWords());
    //构建查询条件  jestClient
    jestClient.execute(
```

画面4:
```java
@Override
public ResponseResult cArticleSearch(UserSearchDto dto) {
    if (dto.getFromIndex() == 0) {
        ResponseResult ret = getEntryId(dto);
        if (ret.getCode() == AppHttpCodeEnum.SUCCESS.getCode()) {
            return ret;
        }
    }
    saveUserSearch(int ret.getData(), dto.getSearchWords());
    //构建查询条件  jestClient
    Search search = new Search.Builder(
        searchSourceBuilder.toString()).addIndex(ESIndexConstants.ARTICLE_INDEX)
        .addType(ESIndexConstants.DEFAULT_DOC).build();
    jestClient.execute(search);
    return null;
}
```

画面5:
```java
@Override
public ResponseResult cArticleSearch(UserSearchDto dto) {
    if (dto.getFromIndex() == 0) {
        ResponseResult ret = getEntryId(dto);
        if (ret.getCode() == AppHttpCodeEnum.SUCCESS.getCode()) {
            return ret;
        }
    }
    saveUserSearch(int ret.getData(), dto.getSearchWords());
    //构建查询条件  jestClient
    SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
    searchSourceBuilder.query(QueryBuilders.matchQuery("name", dto.getSearchWords()));
    searchSourceBuilder.from(dto.getFromIndex());
    searchSourceBuilder.size(dto.getPageSize());
    Search search = new Search.Builder(searchSourceBuilder.toString())
        .addIndex(ESIndexConstants.ARTICLE_INDEX)
        .addType(ESIndexConstants.DEFAULT_DOC).build();
    jestClient.execute(search);
    return null;
}
```

画面6:
```java
@Override
public ResponseResult cArticleSearch(UserSearchDto dto) {
    if (dto.getFromIndex() == 0) {
        ResponseResult ret = getEntryId(dto);
        if (ret.getCode() == AppHttpCodeEnum.SUCCESS.getCode()) {
            return ret;
        }
    }
    saveUserSearch(int ret.getData(), dto.getSearchWords());
    //构建查询条件  jestClient
    SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
    searchSourceBuilder.query(QueryBuilders.matchQuery("name", dto.getSearchWords()));
    searchSourceBuilder.from(dto.getFromIndex());
    searchSourceBuilder.size(dto.getPageSize());
    Search search = new Search.Builder(searchSourceBuilder.toString())
        .addIndex(ESIndexConstants.ARTICLE_INDEX)
        .addType(ESIndexConstants.DEFAULT_DOC).build();
    try {
        jestClient.execute(search);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return null;
}
```

画面7:
```java
@Override
public ResponseResult cArticleSearch(UserSearchDto dto) {
    if (dto.getFromIndex() == 0) {
        ResponseResult ret = getEntryId(dto);
        if (ret.getCode() == AppHttpCodeEnum.SUCCESS.getCode()) {
            return ret;
        }
    }
    saveUserSearch(int ret.getData(), dto.getSearchWords());
    //构建查询条件  jestClient
    SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
    searchSourceBuilder.query(QueryBuilders.matchQuery("name", dto.getSearchWords()));
    searchSourceBuilder.from(dto.getFromIndex());
    searchSourceBuilder.size(dto.getPageSize());
    Search search = new Search.Builder(searchSourceBuilder.toString())
        .addIndex(ESIndexConstants.ARTICLE_INDEX)
        .addType(ESIndexConstants.DEFAULT_DOC).build();
    try {
        jestClient.execute(search);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return null;
}
```

画面8:
```java
@Override
public ResponseResult cArticleSearch(UserSearchDto dto) {
    if (dto.getFromIndex() == 0) {
        ResponseResult ret = getEntryId(dto);
        if (ret.getCode() == AppHttpCodeEnum.SUCCESS.getCode()) {
            return ret;
        }
    }
    saveUserSearch(int ret.getData(), dto.getSearchWords());
    //构建查询条件  jestClient
    SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
    searchSourceBuilder.query(QueryBuilders.matchQuery("name", dto.getSearchWords()));
    searchSourceBuilder.from(dto.getFromIndex());
    searchSourceBuilder.size(dto.getPageSize());
    Search search = new Search.Builder(searchSourceBuilder.toString())
        .addIndex(ESIndexConstants.ARTICLE_INDEX)
        .addType(ESIndexConstants.DEFAULT_DOC).build();
    try {
        SearchResult searchResult = jestClient.execute(search);
        List<Article> articles = searchResult.getHitsList(Article.class);
        for (Article aparticle : articles) {
            //处理结果
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return null;
}
```

画面9:
```java
@Override
public ResponseResult cArticleSearch(UserSearchDto dto) {
    if (dto.getFromIndex() == 0) {
        ResponseResult ret = getEntryId(dto);
        if (ret.getCode() == AppHttpCodeEnum.SUCCESS.getCode()) {
            return ret;
        }
    }
    saveUserSearch(int ret.getData(), dto.getSearchWords());
    //构建查询条件  jestClient
    SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
    searchSourceBuilder.query(QueryBuilders.matchQuery("name", dto.getSearchWords()));
    searchSourceBuilder.from(dto.getFromIndex());
    searchSourceBuilder.size(dto.getPageSize());
    Search search = new Search.Builder(searchSource

