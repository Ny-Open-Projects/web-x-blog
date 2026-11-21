# 画面线理解：12_app搜索_查询联想词接口开发完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\12_app搜索_查询联想词接口开发完成【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:26, 01:42, 02:37, 03:13, 04:25, 05:20, 05:57, 06:18, 06:44, 07:46, 08:37, 09:08, 09:45, 10:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:34:56

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现文章搜索功能，包括控制器测试、实体类、MyBatis Mapper 映射文件、服务层逻辑和单元测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 画面显示 IntelliJ IDEA 中的测试类 ArticleSearchControllerTest。
- 代码：`public void testHotKeywords() throws Exception { UserSearchDto dto = new UserSearchDto(); dto.setHotDate("2019-06-24"); MockMultipartRequestBuilder builder = MockMvcRequestBuilders.post("/api/v1/article/search/load_hot_keywords").contentType(MediaType.APPLICATION_JSON_VALUE).content(mapper.writeValueAsBytes(dto)).andExpect(MockMvcResultMatchers.status().isOk()).andDo(MockMvcResultHandlers.print()); }`
- 测试结果：Tests passed: 1 of 1 in 148ms。

画面 2:
- 画面显示 UserSearchDto 类的定义，包含字段如 equipmentId, searchWords, tag, hotDate, pageNo, pageSize。

画面 3:
- 画面显示 ApAssociateWordsMapper.xml 文件内容，包含 resultMap 和 sql 标签。
- 代码：`<resultMap id="BaseResultMap" type="com.heima.model.article.pojos.ApArticleConfig"> <result column="id" property="id"/> <result column="is_comment" property="isComment"/> <result column="is_forward" property="isForward"/> <result column="is_down" property="isDown"/> <result column="is_delete" property="isDelete"/> </resultMap> <sql id="Base_Column_List"> id, article_id, is_comment, is_forward, is_down, is_delete </sql> <select id="selectById" resultType="com.heima.model.article.pojos.ApArticleConfig" parameterType="int"> select <include refid="Base_Column_List"/> from ap_article_config where article_id = #{id} </select>`

画面 4:
- 画面显示 ApAssociateWordsMapper.xml 文件内容，包含 resultMap 和 sql 标签。
- 代码：`<resultMap id="BaseResultMap" type="com.heima.model.article.pojos.ApArticleConfig"> <result column="id" property="id"/> <result column="is_comment" property="isComment"/> <result column="is_forward" property="isForward"/> <result column="is_down" property="isDown"/> <result column="is_delete" property="isDelete"/> </resultMap> <sql id="Base_Column_List"> id, article_id, is_comment, is_forward, is_down, is_delete </sql> <select id="selectById" resultType="com.heima.model.article.pojos.ApArticleConfig" parameterType="int"> select <include refid="Base_Column_List"/> from ap_article_config where article_id = #{id} </select>`

画面 5:
- 画面显示 ApArticleSearchServiceImpl.java 文件内容，包含 hotKeywords 和 searchAssociate 方法的定义。

画面 6:
- 画面显示 ApArticleSearchServiceImpl.java 文件内容，正在编辑 searchAssociate 方法。
- 代码：`public ResponseResult searchAssociate(UserSearchDto dto) { if (dto.getPageSize() > 50 || dto.getPageSize() < 0) return null; }`

画面 7:
- 画面显示 ApArticleSearchServiceImpl.java 文件内容，正在编辑 searchAssociate 方法。
- 代码：`public ResponseResult searchAssociate(UserSearchDto dto) { if (dto.getPageSize() > 50 || dto.getPageSize() < 0) return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID); return null; }`

画面 8:
- 画面显示 ApArticleSearchServiceImpl.java 文件内容，正在编辑 searchAssociate 方法。
- 代码：`public ResponseResult searchAssociate(UserSearchDto dto) { if (dto.getPageSize() > 50 || dto.getPageSize() < 0) return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID); apAssociateWordsMapper.selectByAssociateWords(dto.getSearchWords(), dto.getPageSize()); return null; }`

画面 9:
- 画面显示 ArticleSearchControllerApi.java 文件内容，包含 clearUserSearch 和 loadHotKeywords 方法的定义。

画面 10:
- 画面显示 ArticleSearchControllerApi.java 文件内容，包含 clearUserSearch 和 loadHotKeywords 方法的定义。
- 代码：`@PostMapping("/clear_search") public ResponseResult clearUserSearch(UserSearchDto dto) { return aparticleSearchService.clearUserSearch(dto); } @PostMapping("/load_hot_keywords") public ResponseResult hotKeywords(@RequestBody UserSearchDto dto) { return aparticleSearchService.hotKeywords(dto.getHotDate()); }`

画面 11:
- 画面显示 ArticleSearchControllerTest.java 文件内容，测试代码与画面 1 相同。

画面 12:
- 画面显示 ArticleSearchControllerTest.java 文件内容，正在编辑测试代码。
- 代码：`MockMvcRequestBuilders.post("/api/v1/article/search/associate_search").contentType(MediaType.APPLICATION_JSON_VALUE).content(mapper.writeValueAsBytes(dto)).andExpect(MockMvcResultMatchers.status().isOk()).andDo(MockMvcResultHandlers.print());`

画面 13:
- 画面显示测试结果，测试通过。
- 代码：`ArticleSearchControllerTest > testSearchAssociate()`

画面 14:
- 画面显示 ApAssociateWordsMapper.xml 文件内容，包含 resultMap 和 sql 标签。
- 代码：`<resultMap id="BaseResultMap" type="com.heima.model.article.pojos.ApAssociateWords"> <id column="id" property="id"/> <result column="associate_words" property="associateWords"/> <result column="created_time" property="createdTime"/> </resultMap> <sql id="Base_Column_List"> id, associate_words, created_time </sql> <select id="selectByAssociateWords" resultMap="BaseResultMap"> select <include refid="Base_Column_List"/> from ap_associate_words where associate_words like #{searchWords} limit #{limit} </select>`

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
（已在上文第 2 点中完整列出）

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 或架构图/流程图。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）
