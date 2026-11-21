# 20_自媒体文章管理_文章详情后台接口开发

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\20_自媒体文章管理_文章详情后台接口开发【海量资源尽在 666java.com】.mp4
- 时长 6分18秒（音频 378s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就继续讲啊刚才的接口咱们写完之后呢咱们一会儿再去跟前台一块去连条的时候再测试啊现在咱们要去讲另外一个接口就是文章详情的后台接口啊那这个详情的话呢就是你在这啊在这啊去展示了某一条文章是吧然后我点一下详情就能去跳到详情那一面去查看当前的文章其实呢就是条件啥呢条件条件是不是就只有一个呀哪个
[00:27] 就是根据当前的文章ID去查询对吧所以说这个里边咱们主要用到的主要用到的就是谁就是当前的一个ID条件就是ID返回的看一下返回的就是一个date就是当前的文章的信息好吧那在Map里边咱们需要几个需要一个是吧一个是这样咱们主要是查询就可以了主要是查询行那咱们下面就把这个拷贝一下
[00:58] 根据当前文章ID去查询找到当前谁啊现在MIPER就是他嗯找到了先找到接口啊接口好那这个呢就是根据当前的主件去查询了啊然后在这呢在这个MIPER文件中咱们还要再去定义一下MIPER文件就是他这个非常简单就是根据当前的主件去查询好放到下边这时候呢咱们就可以去写啥了就可以去写当前的Service啊Service还是这个Service啊
[01:37] public response result我们怎么叫find什么wmnewsid好吧行这个参数是wmnewsdq好设置完之后这个就是根据当前的什么根据当前组件查询文章好那下面咱们就来把这个Service写一下
[02:09] 找到这个Service往下走你们叫啥叫findWM news是吧那这个加完之后咱们首先还是第一步首先永远第一步就是干嘛就要去先判断当前的条件GTO等于等银浪或者是啥呢GTO的getid它等于等银浪这不是image是id它等于等银浪这时候有问题我们就可以去解释了
[02:40] 你错了response result.response然后还是参数有问题参数咱们可以设个这参数然后咱们就可以提示一句话你可以不提示说啥呢文章ID不可缺少它这个要是再缺少的话那肯定是有问题然后再往下看然后下面该打起来下面是不是该去查询了是吧没问题那咱们就可以用
[03:14] amreamnewsmypro.select应该是下面这个是吧叫select是吧什么来着这叫select啊prime key是不是他呀根据当前的ID啊dto.id好那这样的话就能去找到当前的一个文章的信息这时候没有完啊没有完怎么办呢你还得去判断啊说它是空的话那这时候肯定是有问题的说它等一等一呢这时候咱们还是要返回啊
[03:45] 当前的这个数据不存在然后这里边是APPHTTP咱们之前是有一个参数的是什么什么BACONAUT一个sense说数据不存在说完了文章不存在好那这样就可以了如果都没事都没事的话就返回呗返回的话咱们就responseresponse resultresponse result
[04:18] 你还记得吗?
[04:47] 介绍更容易了啊打开它public response result什么叫什么什么叫WM news好吧叫他啊这个名字其实无所谓是吧就叫他吧然后呢然后怎么办呢是WM news DTODTO完事这个呢这个是什么意思啊就是根据文章ID是吧根据ID获取文章信息
[05:24] 拿到完之后呢咱们再写他的controllerWM News这里边就这个方法那之后呢咱们就可以在这去写东西了啊写啊加一个host mapping是吧然后这个里边的参数呢就这个值啊URL啊叫news然后在这去加一个什么这个request的body完了啊完了之后呢
[05:55] 这不是request response是request req好这样之后咱们在这直接去用就可以了好吧哪个find wm news是吧然后是byd最终是把dto装进去就完了好吧这个咱们这个一会就算是解完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

