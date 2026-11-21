# 09_app搜索_删除搜索历史接口开发完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\09_app搜索_删除搜索历史接口开发完成【海量资源尽在 666java.com】.mp4
- 时长 12分26秒（音频 747s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 来咱们就开始第二个JECKER的开发这个呢是更简单一些说是要删除搜索记录删除搜索记录啊那这个呢你看看一下JECKER定义啊说还是当前这么一个抢求路径然后呢是有一个还是当前这个user search DTO那你认为应该传过来什么参数呢应该传过来是这样啊一般的话咱们要去传过来的话肯定是传过来当前这个什么search
[00:30] 的ID这个ID应该是一个列表信息咱们可以打开当前那个user search DTO这边应该是这个东西就是AP search his list应该就是当前的一个什么这个列表它是一个列表信息好吧行这里边当然还要根据当前设备ID去删除这个肯定是少不了的下面咱们就来去写一下这个myproject最终返回的再去说一下返回的就是删除的条数好吧
[01:03] 咱们一般情况下都是一条一条的删当然你也可以清空这个Maple的更简单就是根据当前GID和HIDID去删除就可以来打开当前的Maple这个Maple在这好那这个Maple拿到之后咱们就来去写当前这个映射这个映射的话咱们也拷过来就是这么一个代码这个其实它并不是真正的删除大家也看到了它是一个UpdateUpdate的意思
[01:37] 这都知道这是叫什么物理不是物理删除这叫逻辑删除都把一个状态给改成零就可以了改成哪些状态呢就是当前有一个黑色ID然后是把它循环之后把所有的传过来的这些值呢都给它改成什么呢都给它改成当前的一个状态为零就可以了好吧行那这个是当前的MIPR文件啊那下面咱们就来去着手去写当前的Service
[02:05] 这Service的话呢咱们也好写啊咱们一块来看一下啊还是打开当前的AP article searchservice然后呢在这去写那这个写的话呢其实就是dl是吧还是返回response啊然后是dluser search参数还是一样啊叫user searchdto然后最终这个咱们写一个注释啊这就是删除搜索好
[02:39] 那咱们就来去实现一下这个方法这个方法的话咱们在这在上面Ctrl按一下方法咱们放到下边吧好吧好那拿回来之后呢那咱们怎么去做呢这步啊也比较简单这步呢主要呢咱们就可以根据当前的什么那这种什么船位的ID和当前的DTO中的什么设备ID去查询对吧所以说这块啊首先呢还是在干嘛呢获取
[03:16] 行为实体ID然后呢是在通过什么通过ID删除通过ID去删除应该是修改状态就可以了不要删除就修改状态好吧那这个首先咱们还要再去做一个判断这边判断的是dto.getheathlist它的如果说它等于等于那或者是dto.getheathlist
[03:56] 点size没有size吗不是set是get点size如果说呢它是小于等于0也不行这时候咱们就直接return就可以了return你说你的参数有问题点error咱们就还是app说你的参数有问题查询参数有问题
[04:28] 然后这块如果说没问题的话咱们就可以干嘛呢就可以获取当前的行为ID行为实体ID啊这时候的这个咱们已经写完了叫getEntryID然后是就是DTO然后返回一个result好然后呢然后干嘛呢然后咱们就可以判断呗判断啊现在如果说当前这个result点什么getcode不等于谁呀
[04:59] 不等于当前的apps,enumer里边的success什么guidecode如果说它不等于成功的话咱们就直接return当前的result,就完事了等到这个说完之后咱们下面就可以来去查询了查询之前咱们还要再做一个事因为最终它里边传的是啥呢你可以看一下,当前这里边是一个对象
[05:28] 对象的话其实咱们不需要去把这个对象整个对象都往后才去传咱们只需要干嘛呢只需要通过传里边的ID就可以了里边咱们再去创建一个集合这个集合的话呢就可以去接收里边只需要ID就可以那这个怎么做呢来打开这儿啊在这儿啊上面呢就可以用一个list里边有个integer我只需要去接收这是个idsids等于啥呢
[06:01] 等于当前的DTO的什么没用流逝变成句写啊get hilist然后叫什么rslam然后呢是.map然后这样写啊然后是r大于什么大于啊是应该是有一个这种这种这种符号r点什么r.get idr.get id没有没有就写啊当然这样写的话可能
[06:36] 可能是有点问题是吧你也可以怎么着呢你可以这样写他的里边装的是怎样装的就是当前的东西是个对象是吧你说你可以在这写这样写啊冒号冒号两个冒号啊然后是get id好那这样就拿到了啊最终的咱就装到哪呢装到目前的一个对象中就是co然后这里边是to list哎这样的话呢
[07:11] 又能不能去当前那个集合把把他他的一个ID值通通都放到了当前那个ids这个集合中这样就完事了啊行那拿到他之后呢啊拿到之后呢咱们就可以干嘛呢就可以去行了哎就是修改状态嗯这边咱们要去注入一个当前一个map啊private然后是啥
[07:39] 然后是当前的ap user这个已经有了是吧有了咱们之前上个方法已经做过了所以说你在这直接去用就可以了叫ap user.myport.dl然后第一个参数就是entry要result.getgate是他的entry id然后第二个就是当前的ids然后最终他返回的就是一个什么就是一个count就是影响的函数中
[08:08] 其中咱们在这就可以干嘛呢可以在这去responseresponse知道它在哪OK当前的count进去就完事了这报错没有事这报错咱们就强转一下强转成int就完事了好吧这个咱们就算是完了做完之后咱们顺便就把这个mine这个Controller也写一下这会咱们要去往下加首先是要写这个接口接口的话咱们还是再去另一个方法叫response
[08:38] public好吧resonance without然后是什么呢叫dl user search然后这里边还是当前什么user search.to最终这个方法是干嘛的就是占卜搜索历史好吧行那这时候咱们需要去写这个controllercontroller的话就是叫dl
[09:07] searchuser user search好冲写一下就可以了冲写完之后咱们直接调用就可以了其实咱们之前这个Service已经出入去了所以说你在这直接去调用R现在DL然后把DTO装进去一关事看这些东西应该补全还补全比如说前头有一个post mapping是吧这里边是写了啥也叫做DL怎么叫我search好吧
[09:40] 这个跟笔记是保持一致的然后在这还要加一个request好那到此咱们的代码就写完了写完之后咱们可以来测一下测试的话比较简单了就是你可以去装一些东西比如说咱们可以拷贝一下上面的东西拷贝一下拷贝完之后这个方法咱们就简单的写DL user search把这个拷贝一下D大写好吧
[10:12] 这里边咱们需要去设置什么参数吗首先这个当前的ID还是有的是吧但这个也要改啊改成他好那这个给咱们就不要了这个小数据我们不要那里边需要啥呢首先咱们需要登录前的IDID的话首先它是一个什么AP user search所以说咱们要去创建一个AP user search对象你就创建一个好吧new一个什么AP user search
[10:44] 比如说咱们apusersearch.setid啊,setid啊,ID的话咱们可以去可以去找一个啊,找一个哪一个呢比如说刚才咱们查出来一个训练是吧叫8103咱们就把这个8103给查一下啊比如把状态给它改成0就可以了啊8103搜一下呃,回一下啊,把,装进去那装进去之后呢,最终啊,咱们要去创建一个集合是吧list,然后是
[11:12] cpu search比如说打个爆然后这啥呢list.unew一个relist然后最终的是把这个list是放入一个对象就是刚才上面串进的对象完了完了之后呢咱们把这个把这个list装到tpo中set paste list好就把list装进去完事了
[11:41] 这样的话咱们就把这个参数给通过去了啊通过去之后呢咱们就来去发送下请求看一下这个效果走好稍等正在运行好绿色啊没有问题说操作成功是一条咱们可以刷下当前的数据啊目前是8103这个变成0就成功了啊来刷新一下呗找到当前那个81038103你看8103这一块是不是0啊
[12:19] 没问题啊行那这个咱们就算是做完了啊当前这个删除搜索历史记录接口咱们就做完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
            .content(Mapper.writeValueAsString(dto));
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
            .content(Mapper.writeValueAsString(dto));
    mvc.perform(builder

