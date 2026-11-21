# 14_app搜索_文章搜索接口_保存搜索记录

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\14_app搜索_文章搜索接口_保存搜索记录【海量资源尽在 666java.com】.mp4
- 时长 10分9秒（音频 609s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就来完成文章搜索接口的单板开发首先咱们来看一下当前的接口定义这个里边咱们来看一下首先是当前的一个URL没啥可出的然后下面主要是咱们要看一下这次咱们需要去传什么参数到这个user search DTO里边来打开当前的这个类这是user search DTO目前的话咱们要去返回一个文章里边信息那我通过什么去传呢
[00:31] 首先是有一个叫什么当前的一个关键字是吧当用户输入关键字之后去查询当然在那里边还会去设两个参数第一个是当前的这种什么PageName和PageNumber和一个PageSize咱们会去设置一个条数然后除了这些之外还有一个tag这个tag其实咱们默认都是article就可以了因为现在目前这个搜封库里边都是文章信息还有一个这个需要用吗
[01:00] 想一想这个咱们也需要用啊因为这里边啊其实它隐藏了一个需求啊隐藏点需求呢咱们可以打开咱们第一个接口啊来看一看那第一个接口是这样啊说查询搜索记录接口那这搜索记录的话咱们咱们之前呢是只查询了但是并没有做保存那你说这个搜索记录在哪里保存是不是就是用户进行搜索完之后
[01:28] 然后再去保存这个东西啊那什么时候搜索完呢其实就在这啊就在这啊当用户去搜索文章的时候咱们应该把它的关键字进行记录这个呢其实就是咱们的一个需要有一个保存的操作啊保存到哪呢保存到咱们的一个叫user search表中打开看一下啊打开当前的这个表user search找一找啊嗯啊这这边啊
[01:59] 就保存到这个表中就可以了然后存的就有一个关键字好吧关键字但是你怎么拿到这个用户ID呢咱们要通过谁啊要通过当前的entry就是当前的设备ID才能拿得到好吧行那这个这个需求咱们说的差不多然后下面呢咱们就来去定义mypro接口好吧这个mypro呢咱们主要是定义两个方法啊第一个是保存的操作第二个是查询的操作那为什么要查询呢
[02:28] 其实呢咱们在保存之前先去查一下看看这个关键词存在不存在如果说已经存在的话咱们就不用再去保存了好吧不存在再去保存好吧行那咱们就来去写当前这个接口啊这个呢其实就是当前的AP user myper里边去设置啊咱们可以搜一下当前这个类好打开之后呢咱们在这去设置两个方法第一个是插入第二个是插群
[03:04] 好那上面咱们还要去定义当前的Maple接口文件Maple接口的什么应声文件也可以从这考过来这是一个插入和一个查询这样的话就结束了插入的话就非常简单就是根据当前的字段去插入就可以了然后第二个就是查询查询的话就是根据当前的设备ID给你的关键字去查询看看有没有有的话我就不进行插入操作了好吧行那这个咱们说完之后下面咱们再去
[03:36] 呃写Service那写Service之前呢这里边还有一个东西咱们要要去做啊就是还是关于mypro这个mypro是哪个mypro呢是一个APRD和mypro这个mypro呢其实咱们在这个课的第一天已经设置过了啊但这个里边呢是少了一个方法就是根据ID根据主件查询的一个这种方法那这个呢咱们为什么要用呢即使呢你要你再去返回当前的文章里边信息的时候呢防止数据不全
[04:04] 所以说咱们再去查一下数据库把数据给补全就可以了行咱们下面就来把这个MAP也给写下拷贝一下到AP audio map好在这去设置一个就是根据主件ID查询的方法然后就是这个src文件放到这下边好那这样的话就结束了他就是根据主件去查询的
[04:39] 等到下面呢咱们就来去写Service那这Service咱们需要写几个呢刚才说了咱们有几个需求啊其实正常的话咱们要去返回文章的列表信息但是还有一个隐藏的需求是不是要保存当前的什么历史记录啊是吧所以说咱们在这啊在当前的Service中article search Service中需要去设置两个方法啊一个呢就是先写啊response
[05:10] 这个就是查询查询搜索文章的这种方法ES article好吧好这个这个参数呢就是user search search detail好吧然后下面还有一个啊就是是抄一下吧ES文章ES文章最好呢咱们是要去做分页啊要去做分页查询好下面还有一个啊就是
[05:51] 直接写response result然后这个是save user search这个条件啥呢条件的话其实咱们就两个第一个是integerinteger的一个entry id第二个是咱们的一个stream的什么search words好了行那这个参数咱们这个方法咱们也可以描述一下这个方法就是保存搜索记录
[06:24] 保存搜索记录行那咱们下面呢就来去完成他的一个什么他的当前的实现啊首先呢咱们先完成第一个啊咱们当然咱们可以先把这个方法都重写一下啊一个呢是save searchsave user search啊第二个呢是ds article search啊
[06:50] 行那咱们先完成第一个保存一会儿再去完成第二个就是查询文章的这种实现好吧那这个里边该怎么去写呢里边该怎么去写呢想一想里边啊首先呢咱们先去干嘛呢首先去检查当前数据是否存在如果说不存在啊不存在就是直接保存保存好吧
[07:26] 那这个这个怎么检查呢咱们是不是ap user search myper里边是刚才去设了一个deck exist这里边是不是要传两个参数啊一个是entry id然后第二个呢是search words这个方法怎么什么时候调呢其实就在当前的查询的时候咱们再去调用啊先去写到这啊现在最终的他是返回的当前的一个count
[07:54] 如果说啊这个bunk大于0的话呢bunk大于0说明是有数据有数据咱们直接返回就可以了啊说咱们直接返回一个response withoutokok吧咱们就是直接返回前的比如说呃回看的也行返回一眼可以好吧就是你返回啥都行因为现在已经成功了已经成功了啊然后如果说他现在是这个大于0那就是没有数据那没有数据的话咱们就要去保存了
[08:27] 首先你要去在这创建一个对象ap user searchok好等于你有一个ap user search主要咱们是这个数据给填充完整就可以了.set什么id id不用管啊保持有一个entry id那就是entry id下面还有啥呢ap user search.set search啊叫keywords啊就keywords啊words的话就是一个search words好吧
[08:57] 好再往下看看还有还有啥测试点什么Status默认给1回来1是有效的好再往下JP user search点什么set create time然后new一个好吧行那这个咱们就算是保存了最终一调一下把这个都拷过来到下面了算是保存好咱们下面就来去
[09:32] 就是还是调用当前的方法而这边有一个 insert把当前的ap user search放进去就完事了啊让它返回一个影响的行数比如说咱们要insert吧最终呢你返回response result等到这了而ok是把当前那个insert放进去就完事了那行最终呢咱们这个保存的操作咱们就算
[10:03] 完成了啊下面呢咱们就来去完成搜索文章的这个方法好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现文章关联搜索功能，包括接口定义、Mapper 实现、Service 逻辑编写及 SQL 映射配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示接口定义文档，包含接口名称、请求 DTO、响应 DTO 以及错误码定义。
画面 2: 展示测试类代码，用于验证文章保存功能，包含 DTO 初始化、数据映射和循环处理逻辑。
画面 3: 展示 Mapper 实现部分，包含插入记录和检查记录是否存在两个方法的 Java 代码及对应的 XML 映射文件。
画面 4: 展示项目结构和 Mapper 实现代码，突出 `checkExist` 方法的定义。
画面 5: 展示 `ApUserSearchMapper.xml` 中的 `insert` 和 `select` SQL 语句。
画面 6: 展示在项目中搜索 `ApUserSearch` 类。
画面 7: 展示 `ApArticleMapper.xml` 中的 SQL 查询语句，用于根据 ID 查询文章。
画面 8: 展示 Service 层代码，包含 `searchassociate` 和 `saveUserSearch` 方法的定义。
画面 9: 展示 `saveUserSearch` 方法的实现，包含对 `ApUserSearch` 对象的初始化和属性设置。
画面 10: 展示 `saveUserSearch` 方法中调用 `apUserSearchMapper.checkExist` 方法的逻辑。
画面 11: 展示 `saveUserSearch` 方法中调用 `apUserSearchMapper.checkExist` 方法并选择返回值。
画面 12: 展示 `saveUserSearch` 方法中创建 `ApUserSearch` 对象并设置属性。
画面 13: 展示 `saveUserSearch` 方法中调用 `apUserSearchMapper.insert` 方法。
画面 14: 展示 `saveUserSearch` 方法中调用 `apUserSearchMapper.insert` 方法并返回结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
接口名称
/api/v1/article/search/article_search
请求DTO
com.heima.model.article.UserSearchDto
响应DTO
ResponseResult< [List<ApArticle> ]>
(2)CODE定义
PARAM_INVALID
PARAM_INVALID(501,"无效参数")
```

画面 2:
```java
@Autowired
private JestClient jestclient;
@Autowired
private ApArticleMapper aparticleMapper;
@Autowired
private ApArticleContentMapper aparticleContentMapper;

@Test
public void testSave() throws TOPException {
    ArticleHomeDto dto = new ArticleHomeDto();
    dto.setsize(50);
    dto.setTag("_all_");
    List<ApArticle> aparticles = aparticleMapper.loadArticleListByLocation(dto, null);
    for (ApArticle aparticle : aparticles) {
        ApArticleContent aparticleContent = aparticleContentMapper.selectByArticleId(aparticle.getId());
        EsIndexEntity esIndexEntity = new EsIndexEntity();
        esIndexEntity.setChannelId(new Long(aparticle.getChannelId()));
        esIndexEntity.setContent(ZipUtils.gunzip(aparticle.getContent()));
        esIndexEntity.setPublishTime(aparticle.getPublishTime());
        esIndexEntity.setStatus(new Long(aparticle.getStatus()));
        esIndexEntity.setTag("article");
        esIndexEntity.setTitle(aparticle.getTitle());
        Index.Builder builder = new Index.Builder(esIndexEntity);
```

画面 3:
```java
/**
 * 插入搜索记录
 * @param record
 * @return
 */
int insert(ApUserSearch record);

/**
 * 查询记录是否存在
 * @param entryId
 * @param keyword
 * @return
 */
int checkExist(@Param("entryId") Integer entryId, @Param("keyword") String keyword);
```

画面 4:
```java
/**
 * 插入搜索记录
 * @param record
 * @return
 */
int insert(ApUserSearch record);

/**
 * 查询记录是否存在
 * @param entryId
 * @param keyword
 * @return
 */
int checkExist(@Param("entryId") Integer entryId, @Param("keyword") String keyword);
```

画面 5:
```xml
<insert id="insert" parameterType="com.heima.model.user.pojos.ApUserSearch">
    insert into ap_user_search (entry_id, keyword, status, created_time)
    values (#entryId, #keyword, #status, #createdTime)
</insert>

<select id="checkExist" resultType="java.lang.Integer">
    select count(1)
    from ap_user_search
    where entry_id = #{entryId} and keyword = #{keyword} and status = 1
</select>
```

画面 6:
```
Search Everywhere
Include non-project items Double click
```

画面 7:
```xml
<select id="loadArticleByIdList" resultMap="resultMap">
    select
    <include refid="Base_Column_List" />
    from sp_article
    where id in
    <trim suffixOverrides=",">
        <foreach collection="list" item="item" separator=",">
            #{item.articleId}
        </foreach>
    </trim>
</select>

<select id="selectById" parameterType="java.lang.Long" resultMap="resultMap">
    select
    <include refid="Base_Column_List" />
    from sp_article
    where id = #{id}
</select>
```

画面 8:
```java
/**
 * 临时查询线程
 * @param dto
 * @return
 */
ResponseResult searchassociate(UserSearchDto dto);

/**
 * 文章分页查询
 * @param dto
 * @return
 */
ResponseResult articleSearch(UserSearchDto dto);
```

画面 9:
```java
@Override
public ResponseResult searchassociate(UserSearchDto dto) {
    if (dto.getPageSize() > 50 || dto.getPageSize() < 1) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    List<ApAssociateWords> apassociateWords = apassociateWordsMapper.selectByAssociateWords(dto);
    return ResponseResult.okResult(apassociateWords);
}

@Override
public ResponseResult saveUserSearch(Integer entryId, String searchWords) {
    return null;
}

@Override
public ResponseResult articleSearch(UserSearchDto dto) {
    return null;
}
```

画面 10:
```java
@Override
public ResponseResult saveUserSearch(Integer entryId, String searchWords) {
    //左检查当前数据是否存在
    if (apUserSearchMapper.checkExist(entryId, searchWords)) {
        return null;
    }
}
```

画面 11:
```java
@Override
public ResponseResult saveUserSearch(Integer entryId, String searchWords) {
    //左检查当前数据是否存在
    if (apUserSearchMapper.checkExist(entryId, searchWords)) {
        return null;
    }
}
```

画面 12:
```java
@Override
public ResponseResult saveUserSearch(Integer entryId, String searchWords) {
    //左检查当前数据是否存在
    if (apUserSearchMapper.checkExist(entryId, searchWords)) {
        return null;
    }
    ApUserSearch apUserSearch = new ApUserSearch();
    apUserSearch.setEntryId(entryId);
    apUserSearch.setKeyword(searchWords);
    apUserSearch.setStatus(1);
    apUserSearch.setCreatedTime(new Date());
    //不存在，保存
    return null;
}
```

画面 13:
```java
@Override
public ResponseResult saveUserSearch(Integer entryId, String searchWords) {
    //左检查当前数据是否存在
    if (apUserSearchMapper.checkExist(entryId, searchWords)) {
        return null;
    }
    ApUserSearch apUserSearch = new ApUserSearch();
    apUserSearch.setEntryId(entryId);
    apUserSearch.setKeyword(searchWords);
    apUserSearch.setStatus(1);
    apUserSearch.setCreatedTime(new Date());
    //不存在，保存
    int code = apUserSearchMapper.insert(apUserSearch);
    return ResponseResult.okResult(code);
}
```

画面 14:
```java
@Override
public ResponseResult saveUserSearch(Integer entryId, String searchWords) {
    //左检查当前数据是否存在
    if (apUserSearchMapper.checkExist(entryId, searchWords)) {
        return null;
    }
    ApUserSearch apUserSearch = new ApUserSearch();
    apUserSearch.setEntryId(entryId);
    apUserSearch.setKeyword(searchWords);
    apUserSearch.setStatus(1);
    apUserSearch.setCreatedTime(new Date());
    //不存在，保存
    int code = apUserSearchMapper.insert(apUserSearch);
    return ResponseResult.okResult(code);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

