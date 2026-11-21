# 11_app搜索_查询今日热词接口开发完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\11_app搜索_查询今日热词接口开发完成【海量资源尽在 666java.com】.mp4
- 时长 9分34秒（音频 575s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就来完成查询今日热词的接口今日热词肯定是以什么为单位肯定是以天是吧也就是说查询当天的一个热词先看一下这个技术定义技术定义的话就是当前这个URL是吧然后下面是有一个还是user search DTO那DTO里边其实咱们可以打开打开当前的user search DTO这里边其实有一个参数叫什么hot
[00:30] 它是一个什么,String类型的一定要看好了行,那它呢就是一个时间的一个字符串咱们就根据当前这个时间去查询就可以了返回的是啥呢返回的就是当前的一个热词的列表这个呢,这个表咱们可以看一下叫AP Hot Words打开AP Hot Words就它
[00:55] 目前在这里边其实我是设置了一些词比如说这些都是比如说你看有什么世界你好那么穿着博客和马成羽选行训练当然这个是当天的这也是当天的当然你也可以指定日期去查询指定日期也是可以查询的那这时候咱们就来写Map这个Map的话就好写这个Map咱们需要去新建Map打开这个Map的话就是根据当前的一个日期的字符串去查询就可以了作为条件
[01:24] 好就是他拷贝一下往哪拷到当前的model下面有一个mypro咱们就快点写拷过来之后这个就是有一个curate by hotdate然后咱们现在去写当前的什么应用车文件是吧打开拷贝一个出来hotwords好点ok然后把里边内容删掉了删掉完之后咱们在这稍微改一改把这个都删了吧好吧
[02:07] 好那这个Maple也是根据当前日期字符串去查询就可以啊就是把它拷过来嗯那这个是映射是吧主要是看这个方法吧好吧这个方法呢就是说我现在呢是要查询这个表啊它是包含了那么多字段并且呢我这有一个条件是Hot Date然后它是一个字符串好吧行啊那目前这个Maple写完了写完之后呢咱们就来去定义咱们的什么
[02:42] Service 来嗯在article里边还是article里边啊其实你还是在那啊还是在咱们之前那个Service里边去定义就可以了好吧来打开当前的Service就是当前的search好嗯这里边咱们再加个方法再加个方法反回的还是response without然后这个呢是叫how wordshow the key吧words
[03:15] 好它里边是一个str的date那这个是叫什么来着今日热词好吧行那咱们下面去写当前的什么实现hot words是吗hot keywords那这个咱们就来去写首先呢你要去住当前的map
[03:54] jp hot words my book ok这个Service其实相对来说可以好写下因为他这个没有太多的参数啊行那咱们就写呗我写呀那这会写的时候呢其实呢你首先呢还得去判断一下当年的条件啊比如说if如果说呢他为空youtube.exe如果他为空的话怎么办呢为空的话咱们就给他一个什么呢给他一个初始值
[04:27] 出世值其实就是今天的一个值就是当前的一个日期啊目前呢是给它转成奏串那这个怎么办呢咱们有个工具列叫it format utils这个是咱们有一个包啊然后叫什么呢r format然后里边两个参数啊第一个是你有一个it第二个参数呢就是你可以去指定一个格式啊当然这个刷引号啊比如说咱们是yyyyy
[05:00] 这个才说你到底该怎么去写呢其实你还得看表表中这一列呢它是比较的这一列你看这个列是不是中间是杠啊假如说没有杠的话呢那你就按照这个表去设置就可以了没有杠的话那你就是在这就不应该有杠OK啊那目前的话咱们这个就算设置完了最终你把这个data给它重新附加值就可以了那附完值之后咱们就可以去查询了查询的话就容易的APHOTWORST.R那么只有一个Qray
[05:30] 然后把这个Data传进去用它会返回回来一个里边里边的咱们最终返回就可以了返回怎么返回在这还是用Response去包一下Response withoutOK然后是把当前那个APHOW的word你去就完事好吧那这个现在Service就装完了下面咱们就来去写它的APIAPI的话咱们还是去到哪还是到刚才那个接口里边去创建就可以了
[06:00] 哪个到Article API里边有一个Article Search Control API然后在这再去加个方法还是response publicresponse result然后这个啥呢叫how然后这个参数呢就是useruser search tto然后给它设一个这个呢就是还是进入热词
[06:33] 天日热词好诶怎么亮了热词热词啊好了啊那这个加完之后啊咱们下面就来去写它的Controller这个hot keywords好那下面咱们就先去补全啊先去补全拨备一下然后这是啥呢咱们叫做loadload啊-hot keywords好啊那这个
[07:12] 关注后呢咱们在这去设置一个request body你还是用当前的Service去查询就可以RHOTWORTH,好吧,BTO,通过什么?
[07:27] RHOTWORTH,通过来,好了下面咱们就来去写下那个测试类去测试一下打开当前的Controller的测试打开然后呢这时候呢咱们还是可以从笔记中拷贝当然
[07:43] 咱们也可以去那个手写下啊收写下很简单这块拷贝一份然后呢这个是下啥呢我们就考考过来吧叫他H大写后当前这个请求路径是不是改一改路径是他啊要加什么东西呢里边咱们只有一个条件是吧有点什么赛特号他比如说咱们设置一个日期比如说看看哪有哪些日期啊比如说就就这个吧好吧
[08:19] 2019 0724好放进去放进去之后呢咱们就可以去发请求了啊来看一下啊看能不能成功走好马上测试完稍等好这是绿色的啊绿色的完之后呢你看能不能查出来东西就可以了那这块是不是查出来了嗯2019 0724是吧像这些0724的数据都查出来了啊那还可以这样还可以这样我现在不传我不传纸不传纸的话他就会去干嘛呢
[08:54] 他就会去找到今天的日期今天的话其实我就说了三个就这三个啊他应该会把这三个数据给我查出来来看一下啊好咱们再走一遍啊好没事啊来看一下你看是不是传着博客然后还有啥呢还有就是黑马成全还有训练应该是啊OK那这三个咱们也查出来了没有问题啊行那这个查询这个什么搜索记录接口啊咱们就算是做完了啊
[09:29] 这不是速度记录这是查询今日热词

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的文章搜索功能的后端实现，包括 DTO 设计、Mapper 映射、Service 业务逻辑、Controller 接口以及对应的单元测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 ArticleSearchControllerApi.java 中的 clearUserSearch 方法，用于清空用户搜索历史记录，方法接收 UserSearchDto 参数并返回 ResponseResult。
画面 2: 展示 UserSearchDto 类的定义，包含 equipmentId、searchWords、tag、hotDate、pageNum、pageSize 等字段，并定义了 getFromIndex 方法用于计算分页起始索引。
画面 3: 展示 UserSearchDto 类的 getFromIndex 方法实现，当 pageNum 为 0 时返回 0，否则返回 pageSize * (pageNum - 1)。
画面 4: 展示 ApHotWordsMapper.java 接口定义，包含 queryByHotDate 方法，用于根据 hotDate 查询热门关键词列表。
画面 5: 展示 ApHotWordsMapper.xml 映射文件，定义了 BaseResultMap 结果映射和 queryByHotDate 查询语句，其中包含 id、hot_words、type、hot_date、created_time 字段。
画面 6: 展示 ApArticleSearchServiceImpl.java 中的 clearUserSearch 方法实现，调用 apUserSearchMapper 的 clearUserSearch 方法。
画面 7: 展示 ApArticleSearchServiceImpl.java 中的 hotKeywords 方法，用于根据日期查询热门关键词，方法接收 String date 参数并返回 ResponseResult。
画面 8: 展示 Navicat for MySQL 中的 hot_words 表数据，包含 id、hot_words、type、hot_date、created_time 字段，显示了多条记录。
画面 9: 展示 ApArticleSearchServiceImpl.java 中的 hotKeywords 方法实现，调用 apHotWordsMapper 的 queryByDate 方法。
画面 10: 展示 ArticleSearchController.java 中的 clearUserSearch 和 hotKeywords 方法，分别用于清空搜索历史和查询热门关键词。
画面 11: 展示 ArticleSearchControllerTest.java 中的 testLoadArticleInfo 方法，用于测试加载文章信息，方法中创建 UserSearchDto 对象并设置参数。
画面 12: 展示 ArticleSearchControllerTest.java 中的 testHotKeywords 方法，用于测试查询热门关键词，方法中创建 UserSearchDto 对象并设置日期参数。
画面 13: 展示 ArticleSearchControllerTest.java 中的 testHotKeywords 方法执行结果，显示请求处理信息和返回的 JSON 数据，包含 hot_words、type、hot_date、created_time 字段。
画面 14: 展示 ArticleSearchControllerTest.java 中的 testHotKeywords 方法执行结果，显示数据库连接关闭日志，表明测试执行完毕。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public ResponseResult clearUserSearch(UserSearchDto dto);
```

画面 2:
```java
@Data
public class UserSearchDto {
    // 设备ID
    @ApiModelProperty(value = "设备ID")
    Integer equipmentId;
    String searchWords;
    // tag: all, article, login, author
    String tag;
    List<ApUserSearch> hisList;
    String hotDate;
    int pageNum;
    int pageSize;
    public int getFromIndex() {
        if(this.pageNum() == 0) return 0;
        if(this.pageSize() == 10) return this.pageSize() * (pageNum - 1);
        return this.pageSize() * (pageNum - 1);
    }
}
```

画面 3:
```java
public int getFromIndex() {
    if(this.pageNum() == 0) return 0;
    if(this.pageSize() == 10) return this.pageSize() * (pageNum - 1);
    return this.pageSize() * (pageNum - 1);
}
```

画面 4:
```java
public interface ApHotWordsMapper {
    // 查询今日热门
    @Param("hotDate")
    @ResultMap("BaseResultMap")
    List<ApHotWords> queryByHotDate(String hotDate);
}
```

画面 5:
```xml
<Mapper namespace="com.heima.model.mappers.app.ApHotWordsMapper">
    <resultMap id="BaseResultMap" type="com.heima.model.article.pojos.ApHotWords">
        <id column="id" property="id"/>
        <result column="hot_words" property="hotWords"/>
        <result column="type" property="type"/>
        <result column="hot_date" property="hotDate"/>
        <result column="created_time" property="createdTime"/>
    </resultMap>

    <sql id="Base_Column_List">
        id, hot_words, type, hot_date, created_time
    </sql>

    <select id="queryByHotDate" resultMap="BaseResultMap" parameterType="java.lang.String">
        select
        <include refid="Base_Column_List"/>
        from ap_hot_words
        where hot_date = #{hotDate,jdbcType=VARCHAR}
    </select>
</Mapper>
```

画面 6:
```java
List<Integer> ids = dto.getHisList().stream().map(ApUserSearch::getId).collect(Collectors.toList());
int count = apUserSearchMapper.clearUserSearch((int) result.getData(), ids);
```

画面 7:
```java
@Override
public ResponseResult hotKeywords(String date) {
    if(StringUtil.isBlank(date)) {
        date = DateUtils.format(new Date(), pattern = "yyyy-MM-dd");
    }
    List<ApHotWords> apHotWords = apHotWordsMapper.queryByDate(date);
    return ResponseResult.okResult(apHotWords);
}
```

画面 8:
无代码，仅展示数据库表数据。

画面 9:
```java
@Override
public ResponseResult hotKeywords(String date) {
    if(StringUtil.isBlank(date)) {
        date = DateUtils.format(new Date(), pattern = "yyyy-MM-dd");
    }
    List<ApHotWords> apHotWords = apHotWordsMapper.queryByDate(date);
    return ResponseResult.okResult(apHotWords);
}
```

画面 10:
```java
// 清空搜索历史记录
@ApiOperation("清空搜索历史记录")
@PostMapping("/clear_search")
public ResponseResult clearUserSearch(@RequestBody UserSearchDto dto) {
    // 清空搜索历史记录
    return ResponseResult.okResult();
}

// 今日热门
@ApiOperation("今日热门")
@GetMapping("/hot_keywords")
public ResponseResult hotKeywords(@RequestParam("date") String date) {
    return ResponseResult.okResult();
}
```

画面 11:
```java
@MockBean
private ApplicationContext applicationContext;

@MockBean
private ApUserSearchMapper apUserSearchMapper;

@MockBean
private ApHotWordsMapper apHotWordsMapper;

@MockBean
private ApArticleSearchService apArticleSearchService;

@MockBean
private ArticleSearchController articleSearchController;

@Test
public void testLoadArticleInfo() throws Exception {
    UserSearchDto dto = new UserSearchDto();
    dto.setEquipmentId(1);
    dto.setPageNum(1);
    dto.setPageSize(10);
    MockMvcRequestBuilder builder = MockMvcRequestBuilders.post("/api/v1/article/search/load_search")
            .contentType(MediaType.APPLICATION_JSON_VALUE)
            .content(Mapper.writeValueAsString(dto))
            .accept(MediaType.APPLICATION_JSON);
    mvc.perform(builder).andExpect(MockMvcResultMatchers.status().isOk()).andDo(MockMvcResultHandlers.print());
}
```

画面 12:
```java
@Test
public void testHotKeywords() throws Exception {
    UserSearchDto dto = new UserSearchDto();
    dto.setEquipmentId(1);
    dto.setPageNum(1);
    dto.setPageSize(10);
    dto.setHotDate("2019-07-24");
    MockMvcRequestBuilder builder = MockMvcRequestBuilders.post("/api/v1/article/search/load_hot_keywords")
            .contentType(MediaType.APPLICATION_JSON_VALUE)
            .content(Mapper.writeValueAsString(dto))
            .accept(MediaType.APPLICATION_JSON);
    mvc.perform(builder).andExpect(MockMvcResultMatchers.status().isOk()).andDo(MockMvcResultHandlers.print());
}
```

画面 13:
```json
{
    "types": [
        {
            "id": "1",
            "hot_date": "2019-09-20",
            "created_time": "1568874291000",
            "type": "1",
            "hot_words": "黑马程序员"
        }
    ]
}
```

画面 14:
无代码，仅展示数据库连接关闭日志。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题、架构图/流程图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

