# 画面线理解：14_app搜索_文章搜索接口_保存搜索记录

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\14_app搜索_文章搜索接口_保存搜索记录【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 01:13, 02:26, 03:05, 03:34, 04:22, 04:58, 06:29, 06:54, 07:48, 08:30, 08:55, 09:19, 09:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:36:35

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
