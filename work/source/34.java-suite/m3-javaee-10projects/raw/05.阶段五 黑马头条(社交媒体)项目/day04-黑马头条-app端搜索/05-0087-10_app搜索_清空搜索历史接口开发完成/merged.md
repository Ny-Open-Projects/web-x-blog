# 10_app搜索_清空搜索历史接口开发完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\10_app搜索_清空搜索历史接口开发完成【海量资源尽在 666java.com】.mp4
- 时长 6分59秒（音频 420s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 来咱们就继续往下讲下面咱们去讲另外一个接口就是清空搜索记录的接口那这个这个接口相对来说应该是最容易的一个接口啊就是你其实只需要去把当前的这种数据给清空就可以了但是清空的话并不是你认为的清空应该是咱们还是要修改当前的状态值对吧那行那咱们一块来看一下啊首先呢这里边内容啊这里边内容咱们还是有一个当前的URL是吧第二个是当前的色识DTO
[00:29] 那这个DQ里边咱们需要去传什么参数呢需要从前台咱们需要拿到什么数据呢其实你只需要拿到一个就可以了拿到当前的设备ID就可以或者是用户就可以是吧他会把当前用户所有的记录都给清空就是虚拐状态好吧行那这个咱们就写一下其实这个比较容易这时候咱们只需要有一个参数就是当前的entry ID这时候咱们可以买一块去写
[00:59] 好找到当前的MAP好拷贝一下这个就是去清空然后咱们MAP文件写一下MAP文件的话其实也是修改也是修改修改啥呢看一看修改的话其实就是当前的什么N2ID状态为1的设置为0就可以了设置为0好咱们下面就继续写下面写Service这个Service的话其实更容易一些就是写写写写好吧
[01:33] 然后呢这里边是首先咱们在这就进一个方法啊一个方法不是当前的叫什么来着先写吧response result咱们叫好吧user searchuser searchuser search cto好实际叫什么是叫做清空搜索记录清空搜索历史行咱们下面去写当前的
[02:17] 这个实时限列啊clearuser search好重写完之后呢咱们就写当前的逻辑啊这逻辑的话呢其实在门之前差不多还是要干嘛呢首先呢这里边参数没啥可判断的因为这里边tto里边只需要有一个设备id所以说咱们在这直接去拿到get entry id就完事了把tto装进去然后最终返回返回一个现在result那拿到result之后呢咱们还是要还是要判断啊如果说result什么get code
[02:50] 不等于谁不等于不是那等于apphhttpcode enumer.success.getcode.getcode如果说它不等于成功的话咱们就说直接去返回就可以了return以前这个result好最终如果说都没事那就很容易了咱们就可以干嘛可以调用现在ap user
[03:20] APU user search mypl.2有一个什么可令哎把当前的什么result.get.get date总管事啊那最终这个是不是要去返回什么东西啊是不是一个强转呢就是int啊行那最终呢咱们要去返回当前的一个count啊其实就是count啊最终咱们把当前的什么responseresponse.result.ok
[03:58] 把当前的conv放进去那这个写完之后咱们就来去写当前的接口这个接口的话也很容易接口的话就是在这好在这定一个方法我们就叫啥叫public response然后是clear user searchsbarch那参数还是这也还是当前的user search
[04:31] 那这是什么呢清风搜索历史记录那咱们API结果算是做完了下面写来写一下当前的这个什么Clear这里边咱们还要直接去调用就可以了非常简单然后是Clear
[05:02] 把DTO装进去 完事啊上面还这部权啊叫什么Post My Ping然后这里边叫啥呢咱们叫什么ClearSearch好吧 当然这里边还要再加一个就是Request Body不要忘了啊那加完之后啊咱们就来可以去测试一下测试的话呢其实还是一样啊咱们直接去拷贝一份往下走然后这个是叫啥呢是叫ClearSearch拷过来
[05:39] 然后是这个要改,往前的可见色值改完之后,参数其实就需要那么多了只需要传一个参数就可以这样这个数据到底有没有,你可以查一下比如说咱们现在可以去打开这个表表上咱们可以筛选筛选啥呢,筛选当前的这个ID等于1因为咱们才能调节就是1
[06:11] 那搜完之后呢你发现啊这都只有一个是1的咱们可以设置两个比如说这是1这是1咱们清完之后应该都是啥呢都变成0都变成0啊那咱们来测一下看看效果啊走执行稍等好正在执行稍等啊完了是吧来看看啊操作成功4条是吧你可以刷新一下当刚才这4个能不能变成0能
[06:55] 能变成零是吧也就是说咱们这接口没有问题啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
package com.heima.article.Service;
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
            .content(Mapper.writeValueAsString(dto))
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

