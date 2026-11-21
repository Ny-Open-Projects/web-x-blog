# 画面线理解：08_app搜索_搜索记录历史接口开发完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\08_app搜索_搜索记录历史接口开发完成【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:03, 02:23, 04:07, 05:16, 07:08, 08:08, 09:47, 10:55, 12:17, 13:31, 14:41, 16:01, 17:06, 18:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:31:26

1) 这一组画面整体在讲：实现一个根据用户ID和设备ID查询用户搜索历史的后端功能，包括数据库表结构、Mapper接口定义、XML映射文件、Service层实现、Controller层接口以及单元测试。

2) 按时间顺序列出每张画面的要点：
画面1：展示数据库表 ap_hot_words 的数据，其中一条记录的 created_time 为 2019-09-20 06:46:18，底部显示 SQL 更新语句 UPDATE ap_hot_words SET created_time='2019-09-20 06:46:18' WHERE (id=7)。
画面2：在 IntelliJ IDEA 中展示 ApUserSearchMapper 接口，定义了 selectById 方法，参数为 @Param("entryId") Integer entryId 和 @Param("limit") int limit。
画面3：在 IntelliJ IDEA 中展示 ApUserSearchMapper.xml 文件，其中包含 resultMap 和 sql 标签，定义了 Base_Column_List 和 selectById 查询语句。
画面4：在 Typora 中展示文档，内容为 4.1.4 代码思路分析和 4.1.5 代码实现，其中提到创建接口 ApArticleSearchService。
画面5：在 Typora 中展示文档，内容为 4.1.5 代码实现，其中提到创建类 ApUserSearch 和接口 ApUserSearchMapper。
画面6：在 IntelliJ IDEA 中展示 ApArticleSearchServiceImpl.java 文件，其中包含 getEntryId 方法和 findUserSearch 方法的实现。
画面7：在 IntelliJ IDEA 中展示 ApArticleSearchServiceImpl.java 文件，其中包含 findUserSearch 方法的实现，调用 apBehaviorEntryMapper.selectByUserDeviceId。
画面8：在 IntelliJ IDEA 中展示 ApArticleSearchServiceImpl.java 文件，其中包含 findUserSearch 方法的实现，调用 apBehaviorEntryMapper.selectByUserDeviceId。
画面9：在 IntelliJ IDEA 中展示 ApArticleSearchServiceImpl.java 文件，其中包含 findUserSearch 方法的实现，调用 apBehaviorEntryMapper.selectByUserDeviceId。
画面10：在 IntelliJ IDEA 中展示 ArticleSearchControllerApi 接口，其中定义了 findUserSearch 方法。
画面11：在 Typora 中展示文档，内容为 4.1.6 单元测试，其中提到使用 MockMvc 进行接口测试。
画面12：在 IntelliJ IDEA 中展示 ArticleSearchController.java 文件，其中定义了 @PostMapping("/load_search_history") 方法。
画面13：在 IntelliJ IDEA 中展示 ArticleSearchControllerTest.java 文件，其中定义了 testLoadArticleInfo 方法，使用 MockMvc 进行测试。
画面14：展示数据库表 ap_user_search 的数据，其中包含多条记录，底部显示 SQL 查询语句 SELECT * FROM ap_user_search LIMIT 0, 1000。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
UPDATE ap_hot_words SET created_time='2019-09-20 06:46:18' WHERE (id=7)

画面2：
public interface ApUserSearchMapper {
    List<ApUserSearch> selectById(@Param("entryId") Integer entryId, @Param("limit") int limit);
}

画面3：
<resultMap id="Base_Column_List" type="com.heima.model.user.pojos.ApUserSearch">
    <id column="id" property="id" />
    <result column="entry_id" property="entryId" />
    <result column="keyword" property="keyword" />
    <result column="status" property="status" />
    <result column="created_time" property="createdTime" />
</resultMap>

<sql id="selectById" resultType="BaseResultMap">
    select
    <include refid="Base_Column_List" />
    from ap_user_search
    where entry_id = #{entryId} and status = 1
    order by created_time desc limit #{limit}
</sql>

画面4：
(1)ApArticleSearchService
创建类：com.heima.article.service.ApArticleSearchService
定义状态的枚举类：

public interface ApArticleSearchService {
    // 新增搜索记录
    @Param userSearchDto
    Return
    /
}

画面5：
创建类 com.heima.model.user.pojos.ApUserSearch
public class ApUserSearch {
    private Integer id;
    private Integer entryId;
    private String keyword;
    private Integer status;
    private Date createdTime;
}

(2)ApUserSearchMapper
创建类 com.heima.model.mappers.app.ApUserSearchMapper
定义根据entryId查询历史记录方法：
public interface ApUserSearchMapper {
    // 根据entryId查询历史记录
    @Param entryId
    Return
    List<ApUserSearch> selectById(@Param("entryId") Integer entryId, @Param("limit") int limit);
}

画面6：
public ResponseResult getEntryId(UserSearchDto dto) {
    ApUser user = AppThreadLocalUtils.getUser();
    // 用户设备不能为空
    if(user == null && dto.getEquipmentId() == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE);
    }
    Long userId = null;
    if(user != null) {
        userId = user.getId();
    }
    ApBehaviorEntry apBehaviorEntry = apBehaviorEntryMapper.selectByUserDeviceId(userId, dto.getEquipmentId());
    if(apBehaviorEntry == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    return ResponseResult.okResult(apBehaviorEntry.getEntryId());
}

@Override
public ResponseResult findUserSearch(UserSearchDto dto) {
    // 分页参数校验
    if(dto.getPageSize() > 50 || dto.getPageSize() < 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    // 获取行为id
    ResponseResult result = getEntryId(dto);
    if(result.getCode() != AppHttpCodeEnum.SUCCESS.getCode()) {
        return result;
    }
    // 查询搜索记录
    return null;
}

画面7：
if(apBehaviorEntry == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
}
return ResponseResult.okResult(apBehaviorEntry.getEntryId());

@Override
public ResponseResult findUserSearch(UserSearchDto dto) {
    if(dto.getPageSize() > 50 || dto.getPageSize() < 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    // 获取行为id
    ResponseResult result = getEntryId(dto);
    if(result.getCode() != AppHttpCodeEnum.SUCCESS.getCode()) {
        return result;
    }
    // 查询搜索记录
    return null;
}

画面8：
// 行为实体以及任务，逻辑上这里必须有值，除非参数错误
if(apBehaviorEntry == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
}
return ResponseResult.okResult(apBehaviorEntry.getEntryId());

@Override
public ResponseResult findUserSearch(UserSearchDto dto) {
    if(dto.getPageSize() > 50 || dto.getPageSize() < 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    // 获取行为id
    ResponseResult result = getEntryId(dto);
    if(result.getCode() != AppHttpCodeEnum.SUCCESS.getCode()) {
        return result;
    }
    // 查询搜索记录
    return null;
}

画面9：
// 行为实体以及任务，逻辑上这里必须有值，除非参数错误
if(apBehaviorEntry == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
}
return ResponseResult.okResult(apBehaviorEntry.getEntryId());

@Override
public ResponseResult findUserSearch(UserSearchDto dto) {
    if(dto.getPageSize() > 50 || dto.getPageSize() < 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    // 获取行为id
    ResponseResult result = getEntryId(dto);
    if(result.getCode() != AppHttpCodeEnum.SUCCESS.getCode()) {
        return result;
    }
    // 查询搜索记录
    return null;
}

画面10：
package com.heima.article.apis;
import com.heima.model.common.dtos.ResponseResult;
public interface ArticleSearchControllerApi {
    public ResponseResult findUserSearch(@RequestBody UserSearchDto userSearchDto);
}

画面11：
@Autowired
private ApArticleSearchService apArticleSearchService;
@PostMapping("/load_search_history")
public ResponseResult findUserSearch(@RequestBody UserSearchDto userSearchDto) {
    return apArticleSearchService.findUserSearch(userSearchDto);
}

画面12：
@Autowired
private ApArticleSearchService apArticleSearchService;
@PostMapping("/load_search_history")
public ResponseResult findUserSearch(@RequestBody UserSearchDto userSearchDto) {
    return apArticleSearchService.findUserSearch(userSearchDto);
}

画面13：
@Autowired
private ApArticleSearchService apArticleSearchService;
@PostMapping("/load_search_history")
public ResponseResult findUserSearch(@RequestBody UserSearchDto userSearchDto) {
    return apArticleSearchService.findUserSearch(userSearchDto);
}

画面14：
SELECT * FROM ap_user_search LIMIT 0, 1000

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面4：PPT标题为“4.1.4 代码思路分析”和“4.1.5 代码实现”，内容包括代码思路分析和代码实现。
画面11：PPT标题为“4.1.6
