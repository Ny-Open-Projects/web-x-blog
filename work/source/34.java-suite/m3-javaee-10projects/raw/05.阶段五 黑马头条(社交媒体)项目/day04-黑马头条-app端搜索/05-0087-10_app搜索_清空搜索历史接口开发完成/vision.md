# 画面线理解：10_app搜索_清空搜索历史接口开发完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\10_app搜索_清空搜索历史接口开发完成【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:48, 01:07, 01:30, 02:20, 02:49, 03:02, 03:22, 03:39, 04:06, 04:44, 05:02, 05:29, 05:59, 06:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:33:15

1) 这一组画面整体在讲什么（一句话）：
实现一个清理用户搜索历史的接口，包括接口定义、Mapper层SQL、Service层逻辑、Controller层调用及单元测试验证。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示接口文档，定义了清理搜索记录接口的请求路径、请求DTO和响应DTO。
画面2：展示Mapper层SQL，包含根据ID查询和批量删除的SQL语句。
画面3：展示Service接口定义，包含查询和删除方法。
画面4：展示Service实现类中删除方法的开始部分，包含参数校验。
画面5：展示Service实现类中删除方法的参数校验逻辑，使用了ClassCastException等异常处理。
画面6：展示Service实现类中删除方法的返回值处理，使用了ResponseResult。
画面7：展示Service实现类中删除方法的Mapper调用部分。
画面8：展示Service实现类中删除方法的Mapper调用部分，使用了apUserSearchMapper。
画面9：展示Controller接口定义，包含查询和删除方法。
画面10：展示Controller实现类，包含查询和删除方法的注解和调用。
画面11：展示Controller实现类中删除方法的调用部分。
画面12：展示Controller的单元测试代码，模拟请求并验证响应。
画面13：展示数据库中搜索记录表的数据。
画面14：展示数据库中搜索记录表的数据，执行了更新操作。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
4.3 清空搜索记录接口
4.3.1 接口定义
(1)基本定义
参考标准 请参考通用接口规范
接口名称 /api/v1/article/search/clear_search
请求DTO com.heima.model.article.dtos.UserSearchDto
响应DTO ResponseResult（调用的条件）
[2]CODE定义
PARAM_INVALID PARAM_INVALID(501,"参数无效").
```

画面2：
```xml
<sql id="Base_Column_List">
    id, entry_id, keyword, status, created_time
</sql>
<select id="selectById" resultMap="BaseResultMap">
    select
    <include refid="Base_Column_List" />
    from ap_user_search
    where entry_id = #{entryId} and status = 1
    order by created_time desc limit #{limit}
</select>
<update id="delUserSearch">
    update ap_user_search
    set status = 0
    where entry_id = #{entryId} and id in
    <foreach item="item" collection="hisIds" separator=",">
        #{item}
    </foreach>
</update>
```

画面3：
```java
package com.heima.article.service;
import com.heima.model.article.dtos.UserSearchDto;
import com.heima.model.common.dtos.ResponseResult;
public interface ApArticleSearchService {
    /**
     * 查询搜索历史
     * @param dto
     * @return
     */
    ResponseResult findUserSearch(UserSearchDto dto);

    /**
     * 删除搜索历史
     * @param dto
     * @return
     */
    ResponseResult delUserSearch(UserSearchDto dto);
}
```

画面4：
```java
public ResponseResult delUserSearch(UserSearchDto dto) {
    if(dto.getHisIdList() == null || dto.getHisIdList().size() == 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE);
    }
    List<Integer> ids = dto.getHisIdList().stream().map(UserSearch::getId).collect(Collectors.toList());
    apUserSearchMapper.delUser(ids);
    return ResponseResult.okResult();
}
```

画面5：
```java
public ResponseResult delUserSearch(UserSearchDto dto) {
    if(dto.getHisIdList() == null || dto.getHisIdList().size() == 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE);
    }
    List<Integer> ids = dto.getHisIdList().stream().map(UserSearch::getId).collect(Collectors.toList());
    apUserSearchMapper.delUser(ids);
    return ResponseResult.okResult();
}
```

画面6：
```java
public ResponseResult clearUserSearch(UserSearchDto dto) {
    ResponseResult result = getEntityId(dto);
    if(result.getCode() != AppHttpCodeEnum.SUCCESS.getCode()) {
        return result;
    }
    List<Integer> ids = dto.getHisIdList().stream().map(UserSearch::getId).collect(Collectors.toList());
    int count = apUserSearchMapper.delUserSearch(int result.getData(), ids);
    return ResponseResult.okResult(count);
}
```

画面7：
```java
@Override
public ResponseResult clearUserSearch(UserSearchDto dto) {
    ApUserSearchMapper apUserSearchMapper = new ApUserSearchMapper();
    return null;
}
```

画面8：
```java
@Override
public ResponseResult clearUserSearch(UserSearchDto dto) {
    ApUserSearchMapper apUserSearchMapper = new ApUserSearchMapper();
    return null;
}
```

画面9：
```java
package com.heima.article.apis;
import com.heima.model.article.dtos.UserSearchDto;
import com.heima.model.common.dtos.ResponseResult;
public interface ArticleSearchControllerApi {
    /**
     * 查询搜索历史
     * @param dto
     * @return
     */
    ResponseResult findUserSearch(UserSearchDto dto);

    /**
     * 删除搜索历史
     * @param dto
     * @return
     */
    ResponseResult delUserSearch(UserSearchDto dto);
}
```

画面10：
```java
@TargetApi
@RestController
@RequestMapping("/api/v1/article/search")
public class ArticleSearchController implements ArticleSearchControllerApi {
    @Autowired
    private ApArticleSearchService apArticleSearchService;

    @Override
    @GetMapping("/load_search_history")
    public ResponseResult findUserSearch(@RequestBody UserSearchDto dto) {
        return apArticleSearchService.findUserSearch(dto);
    }

    @Override
    @PostMapping("/del_search")
    public ResponseResult delUserSearch(@RequestBody UserSearchDto dto) {
        return apArticleSearchService.delUserSearch(dto);
    }
}
```

画面11：
```java
@Override
public ResponseResult clearUserSearch(UserSearchDto dto) {
    return apArticleSearchService.clearUserSearch(dto);
}
```

画面12：
```java
@Test
void testDelUserSearch() throws Exception {
    UserSearchDto dto = new UserSearchDto();
    dto.setEquipmentId(1);
    ApUserSearch apUserSearch = new ApUserSearch();
    apUserSearch.setId(103);
    List<ApUserSearch> list = new ArrayList<>();
    list.add(apUserSearch);
    dto.setHisList(list);
    MockMvcRequestBuilders.post("/api/v1/article/search/del_search")
            .contentType(MediaType.APPLICATION_JSON_VALUE)
            .content(mapper.writeValueAsString(dto))
            .accept(MediaType.APPLICATION_JSON_VALUE)
            .andExpect(MockMvcResultMatchers.status().isOk())
            .andDo(MockMvcResultHandlers.print());
}
```

画面13：
```sql
SELECT * FROM `ap_user_search` LIMIT 0, 1000
```

画面14：
```sql
UPDATE `ap_user_search` SET `status` = '1' WHERE (`id` = '8100')
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
