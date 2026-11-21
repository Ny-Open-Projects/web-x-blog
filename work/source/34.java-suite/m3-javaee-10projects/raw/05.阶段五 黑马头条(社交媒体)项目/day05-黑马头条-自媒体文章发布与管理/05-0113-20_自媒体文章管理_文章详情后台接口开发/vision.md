# 画面线理解：20_自媒体文章管理_文章详情后台接口开发

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\20_自媒体文章管理_文章详情后台接口开发【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:14, 00:46, 01:25, 01:59, 02:31, 02:48, 03:14, 03:29, 03:48, 04:14, 04:36, 05:20, 05:53, 06:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:55:48

1) 这一组画面整体在讲什么（一句话）：
实现文章详情后台接口，包括接口定义、Mapper层和Service层的代码编写与逻辑处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档“5.4 文章详情后台接口”中的“5.4.1 接口定义”部分，包含接口规范、请求DTO、响应DTO和错误码定义。
画面2：同画面1，内容无变化。
画面3：展示IDEA中“WmNewsMapper.xml”文件，包含用于查询文章列表和统计的SQL语句，其中包含条件判断和分页参数。
画面4：展示IDEA中“NewsControllerApi.java”文件，包含多个接口方法的声明，如listByUser、findNewsById等。
画面5：展示IDEA中“NewsServiceImp.java”文件，包含listByUser方法的实现，其中包含参数校验、数据库查询和分页处理。
画面6：同画面5，内容无变化。
画面7：展示IDEA中“NewsServiceImp.java”文件，显示“WmNewsMapper”类的自动补全提示，用于调用数据库操作方法。
画面8：展示IDEA中“NewsServiceImp.java”文件，显示findNewsById方法的实现，包含参数校验和数据库查询。
画面9：同画面8，内容无变化。
画面10：展示IDEA中“NewsServiceImp.java”文件，显示findNewsById方法的实现，增加对查询结果为空的判断和错误码返回。
画面11：展示IDEA中“NewsServiceImp.java”文件，显示findNewsById方法的实现，增加对查询结果的封装和设置响应头。
画面12：展示IDEA中“NewsControllerApi.java”文件，显示“saveDraftNews”方法的声明。
画面13：展示IDEA中“NewsControllerApi.java”文件，显示“saveDraft”方法的实现，包含注解和返回值。
画面14：展示IDEA中“NewsControllerApi.java”文件，显示“findNewsById”方法的实现，包含注解和返回值。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3 SQL：
```xml
<select id="CountSelectBySelective" resultType="java.lang.Integer">
    select count(1)
    from wm_news
    where
        status = #{status}
        and title like concat('%', #{dto.keyword}, '%')
        and test.dto.beginPubDate != null
        and publish_time >= #{dto.beginPubDate}
        and test.dto.endPubDate != null
        and publish_time <= #{dto.endPubDate}
</select>
```

画面3 XML：
```xml
<if test="dto.keyword != null">
    and title like concat('%', #{dto.keyword}, '%')
</if>
<if test="dto.beginPubDate != null">
    and publish_time >= #{dto.beginPubDate}
</if>
<if test="dto.endPubDate != null">
    and publish_time <= #{dto.endPubDate}
</if>
```

画面5 Java：
```java
@Override
public ResponseResult listByUser(WmNewsPageReqDto dto) {
    if (dto == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    dto.checkParam();
    Long uid = WmNewsLocalUtils.getUser().getId();
    List<WmNews> datas = wmNewsMapper.selectBySelective(dto, uid);
    int total = wmNewsMapper.countSelectBySelective(dto, uid);
    PageResponseResult responseResult = new PageResponseResult(dto.getPage(), dto.getSize(), total);
    responseResult.setDatas(datas);
    responseResult.setHost(fileServerUrl);
    return responseResult;
}
```

画面6 Java：
```java
@Override
public ResponseResult findNewsById(WmNewsDto dto) {
    if (dto == null || dto.getId() == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRES, errorMessage: "文章ID不可缺少");
    }
    WmNews wmNews = wmNewsMapper.selectNewsDetailByPrimarykey(dto.getId());
    if (wmNews == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.DATA_HOT_EXIST, errorMessage: "文章不存在");
    }
    ResponseResult responseResult = new ResponseResult();
    responseResult.setDatas(wmNews);
    responseResult.setHost(fileServerUrl);
    return responseResult;
}
```

画面13 Java：
```java
@Override
@PostMapping("/save_draft")
public ResponseResult saveDraft(WmNewsDto dto) {
    return newsService.saveNews(dto, WmMediaConstant.FN_NEWS_SUBMIT_STATUS);
}
```

画面14 Java：
```java
@Override
@PostMapping("/news")
public ResponseResult findNewsById(WmNewsDto dto) {
    return newsService.findNewsById(dto);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
