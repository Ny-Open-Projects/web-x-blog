# 21.课程总结

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\21.课程总结_【海量资源尽在 666java.com】.mp4
- 时长 3分55秒（音频 236s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们对今天的课程呢做一个总结那么在今天的课程呢之前呢我们原计划呢我们会讲圈子的一些这个评论相关的功能但是呢今天的这个一些代码量是相对比较大的所以说呢我们就把这个课程呢这一点这个知识点呢我们就放到下一天的课程来做一个讲解那么我们接下来呢对这个课程今天的课程呢做一个总结
[00:27] 那么今天呢我们主要呢就是来完成我们圈子的一些相关的一些功能那我们讲了它的一些这个功能啊以及它的一些技术的一些实现方案啊然后呢我们去讲它的一些技术的解决方案那么其实在我们去学习这个圈子这个功能的时候呢我们最主要的
[00:48] 也就是最核心的我们学习的一些点呢就在于这个它的实现方案那么我们来看一下它的实现方案呢其实就是最核心的有四张表那么第一张表呢是发布表那么第二张表呢是相册表第三张呢是评论第四张呢是时间线那么有了这四张表呢我们就可以去做出一个这个圈子功能就是类似于朋友圈啊这样的一个功能了
[01:15] 那么下面的我们的这个技术方案呢我们主要的采用就是mongodb加redis这样的一个技术来做一个实现那么mongodb呢来负责我们主要的数据的存储那么redis呢主要去负责我们一些缓存数据的一些这种存储啊当然了目前呢我们还没有使用到redis那么在后面我们去实现我们评论的时候呢将会使用到这个redis相关的一些功能那么我们应该把这个给大家来说明一下就是
[01:43] 我们这几个这几个功能我们就放到后面放到后面实现好那么我们把这个给大家来注明一下ok
[01:53] 好那么后面呢我们是有讲了它的一些这个相关的流程发布流程查看流程等等然后呢还有表结构的一些这种设计那么大家呢可以直接去使用这个表结构呢来移植到你的一些项目中去做这样的一些这个使用啊因为它是相对比较通用的这样的一些表结构
[02:14] 然后呢下面呢我们就去具体实现了我们圈子的一些这种功能啊那么我们去实现了什么呢这个发布动态啊以及这个查询这个动态那么当然了我们还做了一个统一的一个这个token这样的一个处理那么在我们后续呢我们使用这个user的时候啊那我们就直接使用这个user local那么就可以拿到我们这个优势对象了而没有必要跟我们之前一样呢都是写一些重复性的一些这个代码逻辑
[02:43] 去获取这个优对象那么这样的话我们就做了一个统一这样的一个处理然后呢后面我们又去实现了什么呢这个查询好友的动态那么查询好友动态呢实际上就是在查询自己的时间线表因为好友在发送动态的时候呢就把动态信息已经写入到了我的这个时间线中了所以我只需要直接查询就OK了然后呢我们又去讲了这个查询推荐动态
[03:11] 那么推荐动态的逻辑其实查询逻辑其实和我们查询好友动态逻辑是一样的那么只是它的数据的来源会有所不同而我们推荐动态我们暂时先去
[03:27] 做查询那么推荐怎么去做一个推荐呢我们后面会做一个实现那么在后面呢我们会将推荐之后的这个结果呢直接写入到我们这个推荐表里面那我们对接到我们现在的逻辑那这个功能是不是就搞定了OK好那么其实以上呢我们主要呢就是去实现这种圈子的一些这样的一些主要的功能啊OK好那么关于我们这个今天的课程的一个总结呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解“圈子”功能的技术实现方案，包括功能说明、实现方案分析、表结构设计、接口定义与实现等。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示“圈子功能”章节的目录结构，当前聚焦于“1.1. 功能说明”，并显示了“圈子”功能的UI截图，说明其基本功能包括发布动态、浏览好友动态、浏览推荐动态、点赞、评论、喜欢等。
画面2：聚焦于“1.2. 实现方案分析”章节，展示“发布动态”功能的UI截图，用户可输入文字并发布。
画面3：继续在“1.2. 实现方案分析”章节，分析数据量大、读多写少、非好友看不到内容等特性，得出需使用MongoDB存储，Redis缓存的结论。
画面4：与画面3内容相同，为“1.2. 实现方案分析”章节的延续，强调核心的4张表：发布表、相册表、评论表、时间线表。
画面5：与画面4内容相同，为“1.2. 实现方案分析”章节的延续，强调核心的4张表：发布表、相册表、评论表、时间线表。
画面6：展示“1.3. 技术方案”章节，明确采用MongoDB+Redis架构，其中MongoDB负责存储，Redis负责缓存数据，并展示“1.3.1. 发布流程”的流程图。
画面7：展示“1.4. 表结构设计”章节，列出“发布表”和“相册表”的结构定义。
画面8：展示“1.4. 表结构设计”章节，展示“发布表”和“相册表”的结构定义，并在下方展示“时间线表”的结构定义。
画面9：展示“1.4. 表结构设计”章节，完整列出“发布表”、“相册表”和“时间线表”的结构定义。
画面10：展示“2.2. 发布动态”章节下的“2.2.1. 定义接口”，展示`QuanZiApi`接口定义，包含`savePublish`方法。
画面11：展示“2.2.2. 编写实现”章节，展示测试类`@SpringBootTest`的导入依赖。
画面12：展示“2.4. 查询好友动态”章节，展示`QuanZiApi`接口定义，包含`queryPublishList`方法。
画面13：展示“2.5. 查询推荐动态”章节，展示`queryPublishList`方法的实现代码，使用MongoTemplate查询。
画面14：回到“1.1. 功能说明”章节，展示“圈子”功能的UI截图，包含多个动态卡片。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面7：
发布表：
#表名：quanzi_publish
{
  "id":1, #主键id
  "userId":1, #用户id
  "text":"今天心情很好！", #文本内容
  "medias":"http://xxxx/x/y/z.jpg", #媒体数据，图片或小视频 url
  "seeType":1, #谁可以看，1-公开，2-私密，3-部分可见，4-不给谁看
  "seeList":[1,2,3], #部分可见的列表
  "notSeeList":[4,5,6], #不给谁看的列表
  "longitude":108.840974298098, #经度
  "latitude":34.2789316522934, #纬度
  "locationName":"上海市浦东区", #位置名称
  "created":1568012791171 #发布时间
}

相册表：
#表名：quanzi_album_userId
{
  "id":1, #主键id
  "publishId":1001, #发布id
  "created":1568012791171 #发布时间
}

画面9：
时间线表：
#表名：quanzi_time_line_userId
{
  "id":1, #主键id
  "userId":1, #用户id
  "publishId":1001, #发布id
  "created":1568012791171 #发布时间
}

画面10：
package com.tanhua.dubbo.server.api;
import com.tanhua.dubbo.server.pojo.Publish;
public interface QuanZiApi {
    /**
     * 发布动态
     */
    @Operation
    boolean savePublish(Publish publish);
}

画面11：
package com.tanhua.dubbo.server.api;
import com.tanhua.dubbo.server.pojo.Users;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringRunner;

画面12：
package com.tanhua.dubbo.server.api;
import com.tanhua.dubbo.server.pojo.Publish;
import com.tanhua.dubbo.server.vo.PageInfo;
public interface QuanZiApi {
    /**
     * 发布动态
     */
    @Operation
    boolean savePublish(Publish publish);
    /**
     * 查询动态
     */
    @Operation
    PageInfo<Publish> queryPublishList(long userId, Integer page, Integer pageSize);
}

画面13：
public PageInfo<Publish> queryPublishList(long userId, Integer page, Integer pageSize) {
    String collectionName = "quanzi_time_line_" + userId;
    Query query = new Query();
    if (userId != null) {
        collectionName = "quanzi_time_line_recommend";
        collectionName = "quanzi_time_line_" + userId;
        query.addCriteria(Criteria.where("userId").is(userId));
    }
    List<ObjectId> publishIds = new ArrayList<>();
    for (Timeline publish : timelineList) {
        publishIds.add(publish.getPublishId());
    }
    return new PageInfo<>(publishIds, publishIds.size(), pageSize);
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面6：
流程图标题：“1.3.1. 发布流程”
结构：
[用户] → [发布动态] → [存储表]
[用户] → [查看好友动态] → [时间线表]
[用户] → [查看推荐动态] → [推荐表]

画面8：
流程图标题：“发布流程”
结构：
[用户] → [发布动态] → [存储表]
[用户] → [查看好友动态] → [时间线表]
[用户] → [查看推荐动态] → [推荐表]

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

