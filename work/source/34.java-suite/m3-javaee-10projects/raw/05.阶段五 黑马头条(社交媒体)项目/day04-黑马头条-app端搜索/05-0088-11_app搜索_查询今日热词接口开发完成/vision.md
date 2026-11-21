# 画面线理解：11_app搜索_查询今日热词接口开发完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\11_app搜索_查询今日热词接口开发完成【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:22, 01:17, 01:35, 02:15, 02:45, 03:42, 04:17, 05:03, 05:47, 06:50, 07:40, 08:04, 08:36, 09:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:34:12

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
<mapper namespace="com.heima.model.mappers.app.ApHotWordsMapper">
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
</mapper>
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
            .content(mapper.writeValueAsString(dto))
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
            .content(mapper.writeValueAsString(dto))
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
