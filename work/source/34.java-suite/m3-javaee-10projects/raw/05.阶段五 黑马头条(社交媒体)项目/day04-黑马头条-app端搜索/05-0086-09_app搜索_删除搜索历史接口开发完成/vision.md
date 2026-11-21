# 画面线理解：09_app搜索_删除搜索历史接口开发完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\09_app搜索_删除搜索历史接口开发完成【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:36, 01:27, 02:43, 03:46, 04:28, 05:04, 06:07, 06:55, 07:52, 08:39, 09:29, 10:53, 11:34, 12:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:32:26

1) 这一组画面整体在讲什么（一句话）：
演示一个用户搜索历史加载与删除功能的完整实现，包括测试、服务层、数据访问层和数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示测试类 ArticleSearchControllerTest 中的 testLoadUserSearch 方法，使用 MockMvc 模拟 POST 请求到 "/api/v1/article/search/load_search_history" 接口，设置请求体为 UserSearchDto 对象并期望返回 200 状态码。
画面2：展示 PPT 页面，标题为“4.2.3 Mapper实现”，内容包括定义搜索记录方法的 Java 代码和对应的 MyBatis XML 映射文件（ApUserSearchMapper.xml）中的 SQL 语句。
画面3：展示服务层代码，定义了 findUserSearch 方法，用于根据用户ID和分页参数查询搜索记录。
画面4：展示服务层代码，继续编写 findUserSearch 方法，创建 ResponseResult 对象并设置状态码。
画面5：展示服务层代码，继续编写 findUserSearch 方法，调用 apUserSearchMapper.selectByEntryId 查询数据并返回。
画面6：展示服务层代码，编写 delUserSearch 方法，用于删除用户搜索历史，首先检查参数有效性。
画面7：展示服务层代码，继续编写 delUserSearch 方法，获取用户ID并调用 apUserSearchMapper.delUserSearch 删除记录。
画面8：展示服务层代码，继续编写 delUserSearch 方法，使用 Stream API 对 dto.getHisList() 进行处理。
画面9：展示服务层代码，继续编写 delUserSearch 方法，调用 apUserSearchMapper.delUserSearch 并返回结果。
画面10：展示 API 层代码，定义 ArticleSearchControllerApi 接口，包含多个注解和方法签名。
画面11：展示控制器层代码，ArticleSearchController 继承 ArticleSearchControllerApi，使用 @Autowired 注入服务并实现接口方法。
画面12：展示数据库 Navicat 界面，显示 ap_user_search 表的数据，包含 entry_id、keyword、status、created 等字段。
画面13：展示测试类 ArticleSearchControllerTest 中的 testDelUserSearch 方法，使用 MockMvc 模拟 POST 请求到 "/api/v1/article/search/del_search" 接口。
画面14：展示数据库 Navicat 界面，SQL 编辑器中显示 SELECT * FROM ap_user_search LIMIT 0, 1000 的语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Test
public void testLoadUserSearch() throws Exception {
    UserSearchDto dto = new UserSearchDto();
    dto.setEquipmentId(1);
    dto.setPageSize(20);
    MockMvcRequestBuilders.post(urlTemplate, "/api/v1/article/search/load_search_history")
            .contentType(MediaType.APPLICATION_JSON_VALUE)
            .content(mapper.writeValueAsString(dto));
    mvc.perform(builder).andExpect(MockMvcResultMatchers.status().isOk()).andDo(MockMvcResultHandlers.print());
}
```

画面2：
```java
// 删除搜索记录
@param entryId
@return hisIds
```
```xml
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
long userId = null;
if (user != null) {
    userId = user.getId();
}
ApBehaviorEntry apBehaviorEntry = apBehaviorEntryMapper.selectByUserAndEquipmentId(userId, dto.getEquipmentId());
// 不为实体以默认注册，这里上处理是肯定有异常，异常参数错误
if (apBehaviorEntry == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
}
return ResponseResult.okResult(apBehaviorEntry.getId());
```

画面4：
```java
@Override
public ResponseResult findUserSearch(UserSearchDto dto) {
    if (dto.getPageSize() > 50 || dto.getPageSize() < 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    //先获取行为实体id
    ResponseResult result = getEntryId(dto);
    if (result.getLoca() != null) {
        return result;
    }
    //查询搜索记录
    List<ApUserSearch> list = apUserSearchMapper.selectByEntryId((int) result.getData(), dto.getPageSize());
    return ResponseResult.okResult(list);
}
```

画面5：
```java
@Override
public ResponseResult delUserSearch(UserSearchDto dto) {
    if (dto.getHisList() == null || dto.getHisList().size() <= 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE);
    }
    //获取行为实体id
    ResponseResult result = getEntryId(dto);
    if (result.getCode() != AppHttpCodeEnum.SUCCESS.getCode()) {
        return result;
    }
    //删除搜索记录
    List<ApUserSearch> list = apUserSearchMapper.selectByEntryId((int) result.getData(), dto.getPageSize());
    return ResponseResult.okResult(list);
}
```

画面6：
```java
@Override
public ResponseResult delUserSearch(UserSearchDto dto) {
    if (dto.getHisList() == null || dto.getHisList().size() <= 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE);
    }
    //获取行为实体id
    ResponseResult result = getEntryId(dto);
    if (result.getCode() != AppHttpCodeEnum.SUCCESS.getCode()) {
        return result;
    }
    //删除搜索记录
    List<ApUserSearch> list = apUserSearchMapper.selectByEntryId((int) result.getData(), dto.getPageSize());
    return ResponseResult.okResult(list);
}
```

画面7：
```java
@Override
public ResponseResult delUserSearch(UserSearchDto dto) {
    if (dto.getHisList() == null || dto.getHisList().size() <= 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE);
    }
    //获取行为实体id
    ResponseResult result = getEntryId(dto);
    if (result.getCode() != AppHttpCodeEnum.SUCCESS.getCode()) {
        return result;
    }
    //删除搜索记录
    List<Integer> ids = dto.getHisList().stream().map(ApUserSearch::getId).collect(Collectors.toList());
    return null;
}
```

画面8：
```java
@Override
public ResponseResult delUserSearch(UserSearchDto dto) {
    if (dto.getHisList() == null || dto.getHisList().size() <= 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE);
    }
    //获取行为实体id
    ResponseResult result = getEntryId(dto);
    if (result.getCode() != AppHttpCodeEnum.SUCCESS.getCode()) {
        return result;
    }
    //删除搜索记录
    List<Integer> ids = dto.getHisList().stream().map(ApUserSearch::getId).collect(Collectors.toList());
    return null;
}
```

画面9：
```java
@Override
public ResponseResult delUserSearch(UserSearchDto dto) {
    if (dto.getHisList() == null || dto.getHisList().size() <= 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE);
    }
    //获取行为实体id
    ResponseResult result = getEntryId(dto);
    if (result.getCode() != AppHttpCodeEnum.SUCCESS.getCode()) {
        return result;
    }
    //删除搜索记录
    List<Integer> ids = dto.getHisList().stream().map(ApUserSearch::getId).collect(Collectors.toList());
    return null;
}
```

画面10：
```java
package com.heima.article.api;

import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartResolver;
import org.springframework.web.multipart.commons.CommonsMultipartResolver;
import org.springframework.web.multipart.support.StandardServletMultipartResolver;
import org.springframework.web.servlet.mvc.method.annotation.*;

import java.util.List;
import java.util.Map;

public interface ArticleSearchControllerApi {
    @PostMapping("/api/v1/article/search")
    public ResponseResult delUserSearch(@RequestBody UserSearchDto dto);
}
```

画面11：
```java
@RestController
@CrossOrigin
@RequestMapping("/api/v1/article/search")
public class ArticleSearchController implements ArticleSearchControllerApi {

    @Autowired
    private ArticleSearchService aparticleSearchService;

    @PostMapping("/api/v1/article/search")
    public ResponseResult delUserSearch(@RequestBody UserSearchDto dto) {
        return aparticleSearchService.delUserSearch(dto);
    }
}
```

画面12：
```sql
SELECT * FROM ap_user_search LIMIT 0, 1000
```

画面13：
```java
@Test
public void testDelUserSearch() throws Exception {
    UserSearchDto dto = new UserSearchDto();
    dto.setEquipmentId(1);
    dto.setPageSize(20);
    ApUserSearch apUserSearch = new ApUserSearch();
    dto.setHisList(Arrays.asList(apUserSearch));
    MockMvcRequestBuilders.post(urlTemplate, "/api/v1/article/search/del_search")
            .contentType(MediaType.APPLICATION_JSON_VALUE)
            .content(mapper.writeValueAsString(dto));
    mvc.perform(builder
