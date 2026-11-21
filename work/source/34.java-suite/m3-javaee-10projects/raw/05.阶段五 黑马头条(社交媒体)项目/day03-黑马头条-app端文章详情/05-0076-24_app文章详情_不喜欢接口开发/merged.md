# 24_app文章详情_不喜欢接口开发

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\24_app文章详情_不喜欢接口开发【海量资源尽在 666java.com】.mp4
- 时长 8分11秒（音频 492s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就继续往下讲咱们下面呢就来去完成当前的不喜欢的这个借口其实呢跟点赞借口是类似的都是只是一个保存的操作那这个呢咱们写之前呢在这还要补充一个东西就是刚才咱们做点赞的时候呢这是少写了一个那这个呢咱们需要在这去写一个请求的路径啊Post Mapping然后咱们是叫什么呢加个括号啊Like
[00:30] 然后是笔牌吧这个补充完整之后呢咱们再来回头再去说一下当前这个不喜欢的接口啊那不喜欢接口里边呢首先呢他这个地址是他是吧然后呢是下面呢是有一个当前的DTO咱们可以搜一下这个DTO我们可以把之前的都给关掉啊好搜到当前的DTO这里边呢是有一个东西啊首先呢是当前的设备是吧当前的文章ID
[01:00] 你到底是喜欢还是不喜欢咱们要去做一个保存的操作那行咱们下面就来去完成首先咱们还是从mypro开始这时候不喜欢这个行为咱们其实已经定义完了只需要去加这么一个保存的操作就可以了还是找到当前的model打开modelapp然后找到是unlock然后再这样去加一个是保存保存
[01:33] 但是这里边呢咱们还需要去再去加这么个东西啊就是里边呢咱们需要去设置前的呃买份文件啊好那考过来之后呢那这个事啊就算是完成了啊呃那下面呢咱们就继续往下讲啊这个不喜欢呢是因为呢呃没有id啊是因为他呢是需要让买cat啊自动的去帮你去生成主件就可以了好吧行那咱们就继续往下看然后这个myper文件做完了然后下面咱们就去
[02:06] 定义咱们的Service这个其实咱们之前没有定义过是吧咱们需要去创建一个当前的Service还是当前的行为当前的行为打开这是创建一个Service右键好它是一个接口接口是app index然后behaviour Service这里边是方法是啥呢这个方法的话其实就是当前的一个保存是吧非常简单我们在这写一下
[02:39] public public然后是返回的都是response啊result然后是save unlike啊没有那个s吧好吧然后这里边的参数呢就是当前的什么unlikelike behavior DTOok DTO好吧这个呢其实就是保存什么分除
[03:11] 保存不喜欢数据OK行那这个呢咱们听完之后呢咱们再去定义它的一个实现类打开这去创建一个类IMDL行让它去实现当前的接口嗯奥特加回车然后Ctrl i把这个方法冲写下这去加一个Service然后去顺便去加一个server running好吧顺便让它不报错
[03:43] 那这个里边该怎么去写呢其实写法呢其实跟咱们之前写法是一样的首先呢你应该应该拿到什么呢当前的行为实体对吧所以说呢这个这个代码还是重复的啊所以说咱们还是从之前的代码中考过来就可以啊然后是从这到这都是拿行为实体然后这考过来等他考过来之后呢这边还少个麦粉是吧咱们也把这个麦粉考过来吧是一样的啊
[04:18] 手写一下啊private然后是什么呢jp behavior entrytype然后就注入进来呗然后注入进来之后呢咱们下面下面呢就可以进行保存了啊保存的方式呢其实还是当前的是保存一个叫jp unlike type是吧咱们也叫alb好吧等于一个jp unlike type好这里边咱们可以去设置材数啊
[04:52] sets什么呢这里边其实没有几个值是吧首先第一个是entry id那entry id的话很简单就是apcover.getid是吧然后再往下alb什么set目前的一个career time那就new一个date完了好再往下看alb.set目前的一个什么article id那就ddo中的什么article id就完事了然后下面alb.set
[05:23] 现在有什么type修中有吗有啊这项看的话就算是做完了啊最终呢你就你就保存就可以了那保存的话咱们时候呢还要去注入一个东西是谁啊就是以前的呃mypro是吧然后是jp unlikelikecover mypro好注进来之后呢咱们在这就可以直接去调用当前的什么呢.insert是吧
[05:57] 我现在把这个DTO装进去叫ARB啊ARB装进去完事了好吧最终他是返回一个insert是吧是一个cont啊那最终咱们在这可以直接用listbanswithout.ok好这个insert装进去完了吗好了啊那这个呢咱们就Service就是解完了就只是一个保存的操作
[06:21] 然后下面咱们再去往下看这时候咱们需要去编写咱们的接口了是吧接口的话咱们还是在当前的APIS里边有个BehaviourController API就这里边咱们再去定义一个方法这个方法就是保存怎样保存的是不喜欢的数据是吧保存不喜欢行为数据好吧行那这写法咱们就是还是responseResult然后下面是
[06:55] save unlike lags,becover,havio然后这个参数呢参数就是unlike becover dto,dto,完了啊这时候呢咱们需要再去写它的实现是吧这个实现的话是alt加i重写写完之后呢咱们再去注入啊注入谁呀注入刚才咱们定义的那个东西pp,unlike becover Service是他吧
[07:29] 我带您的Service啊 祝你来呗好那这时候呢你可以交用了啊嗯 给你很简单啊而今天的sig然后把tto装进去就完事了啊那这一块呢你希望不要忘了全东西这是什么呢pulse怎么买一瓶是吧然后这个值是啥呢这个值的话叫likelike然后笔开口好那这里边咱们还是这还少个东西叫request body是吧加上啊这也少一个啊加上啊
[08:04] 好那这个都加上了代码也补全了目前当前那个不喜欢的接口呢咱们就写到这好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现用户点赞/取消点赞功能的完整代码结构，包括控制器、服务层、数据传输对象、数据库映射文件及对应的业务逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示行为控制器（BehaviorController）类，包含保存点赞和取消点赞的接口方法，分别注入了AppShowBehaviorService和AppUnlikesBehaviorService。
画面2：展示点赞/取消点赞的数据传输对象（UnLikesBehaviorDto）类，定义了设备ID、文章ID、操作类型等字段。
画面3：展示项目结构，定位到Mapper包，准备查看数据库映射文件。
画面4：展示点赞/取消点赞的数据库映射文件（ApUnlikesBehaviorMapper.xml），包含查询和插入SQL语句。
画面5：展示服务接口（ApUnlikesBehaviorService）定义，声明了保存点赞/取消点赞的方法。
画面6：展示服务实现类（ApUnlikesBehaviorServiceImpl）的开头，定义了注入的Mapper和Sequences。
画面7：在服务实现类中，通过IDE自动补全选择ApBehaviorEntryMapper。
画面8：在服务实现类中，为ApUnlikesBehavior对象设置属性，如entryId、articleId、type等。
画面9：在服务实现类中，为ApUnlikesBehavior对象设置创建时间并调用Mapper的insert方法。
画面10：在服务实现类中，通过IDE自动补全选择ApBehaviorEntryMapper。
画面11：在服务实现类中，为ApUnlikesBehavior对象设置属性并调用Mapper的insert方法。
画面12：展示行为控制器接口（BehaviorControllerApi）定义，包含保存点赞和取消点赞的方法。
画面13：展示行为控制器（BehaviorController）类，定义了保存点赞和取消点赞的接口方法。
画面14：展示行为控制器（BehaviorController）类，定义了保存点赞和取消点赞的接口方法，其中取消点赞方法的注解为@PostMapping("/unlike_behavior")。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@RequestMapping("/api/v1/behavior")
public class BehaviorController implements BehaviorControllerApi {
    @Autowired
    private AppShowBehaviorService appShowBehaviorService;

    @PostMapping("/save_behavior")
    public ResponseResult saveShowBehavior(@RequestBody ShowBehaviorDto dto) {
        return appShowBehaviorService.saveShowBehavior(dto);
    }

    @Autowired
    private ApplikesBehaviorService applikesBehaviorService;

    @Override
    public ResponseResult saveUnlikesBehavior(LikesBehaviorDto dto) {
        return applikesBehaviorService.saveUnlikesBehavior(dto);
    }
}
```

画面2：
```java
package com.heima.model.behavior.dto;

import ...

@Data
public class UnLikesBehaviorDto {
    // 设备ID
    @IdEncrypt
    Integer equipmentId
    // 文章ID
    @IdEncrypt
    Integer articleId

    // 不喜欢操作方式
    @IdEncrypt
    Short type;
}
```

画面4：
```xml
<resultMap id="BaseResultMap" type="com.heima.model.behavior.pojos.ApUnlikesBehavior">
    <result column="id" property="id"/>
    <result column="article_id" property="articleId"/>
    <result column="type" property="type"/>
    <result column="created_time" property="createdTime"/>
</resultMap>

<sql id="BaseResultMap" type="com.heima.model.behavior.pojos.ApUnlikesBehavior">
    select * from ap_unlikes_behavior where entry_id=#{entryId} and article_id=#{articleId} order by created_time desc
</sql>

<select id="selectLastUnlike" resultType="BaseResultMap">
    select * from ap_unlikes_behavior where entry_id=#{entryId} and article_id=#{articleId} order by created_time desc
</select>

<insert id="insert" parameterType="com.heima.model.behavior.pojos.ApUnlikesBehavior">
    insert into ap_unlikes_behavior (entry_id, article_id, type, created_time) values (#{entryId}, #{articleId}, #{type}, #{createdTime})
</insert>
```

画面5：
```java
interface ApUnlikesBehaviorService {
    ResponseResult saveUnlikesBehavior(UnLikesBehaviorDto dto);
}
```

画面6：
```java
@Service
@RequiredArgsConstructor
public class ApUnlikesBehaviorServiceImpl implements ApUnlikesBehaviorService {
    @Autowired
    private ApBehaviorEntryMapper apBehaviorEntryMapper;

    @Autowired
    private ApUnlikesBehaviorMapper apUnlikesBehaviorMapper;

    @Autowired
    private Sequences sequences;

    @Override
    public ResponseResult saveUnlikesBehavior(LikesBehaviorDto dto) {
        // 获取用户id，获取设备id
        ApUser user = ApUserContext.getCurrentUser();
        if (user == null || user.getEquipmentId() == null) {
            return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRES);
        }
        long userId = null;
        if (user != null) {
            userId = user.getId();
        }
        ApUnlikesBehavior abl = new ApUnlikesBehavior();
        abl.setEquipmentId(user.getEquipmentId());
        abl.setArticleId(Integer articleId);
        abl.setEntryId(Integer entryId);
        abl.setType(Short type);
        abl.setCreatedTime(new Date());
        abl.setUserId(userId);
        return null;
    }
}
```

画面7：
```java
private ApBehaviorEntryMapper apBehaviorEntryMapper;
```

画面8：
```java
if (user == null || user.getEquipmentId() == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRES);
}
long userId = null;
if (user != null) {
    userId = user.getId();
}
ApUnlikesBehavior abl = new ApUnlikesBehavior();
abl.setEquipmentId(user.getEquipmentId());
abl.setArticleId(Integer articleId);
abl.setEntryId(Integer entryId);
abl.setType(Short type);
abl.setCreatedTime(new Date());
abl.setUserId(userId);
```

画面9：
```java
ApUnlikesBehavior abl = new ApUnlikesBehavior();
abl.setEquipmentId(user.getEquipmentId());
abl.setArticleId(Integer articleId);
abl.setEntryId(Integer entryId);
abl.setType(Short type);
abl.setCreatedTime(new Date());
abl.setUserId(userId);
apUnlikesBehaviorMapper.insert(abl);
return null;
```

画面10：
```java
private ApBehaviorEntryMapper apBehaviorEntryMapper;
```

画面11：
```java
ApUnlikesBehavior abl = new ApUnlikesBehavior();
abl.setEquipmentId(user.getEquipmentId());
abl.setArticleId(Integer articleId);
abl.setEntryId(Integer entryId);
abl.setType(Short type);
abl.setCreatedTime(new Date());
abl.setUserId(userId);
apUnlikesBehaviorMapper.insert(abl);
return null;
```

画面12：
```java
package com.heima.behavior.apis;

import ...

public interface BehaviorControllerApi {
    // 保存用户点赞文章的行为
    @PostMapping("/save_behavior")
    ResponseResult saveShowBehavior(ShowBehaviorDto dto);

    // 保存点赞行为
    @PostMapping("/like_behavior")
    ResponseResult saveLikeBehavior(LikesBehaviorDto dto);

    // 保存取消点赞行为
    @PostMapping("/unlike_behavior")
    ResponseResult saveUnlikesBehavior(LikesBehaviorDto dto);
}
```

画面13：
```java
private AppShowBehaviorService appShowBehaviorService;

@Override
@PostMapping("/save_behavior")
public ResponseResult saveShowBehavior(@RequestBody ShowBehaviorDto dto) {
    return appShowBehaviorService.saveShowBehavior(dto);
}

@Autowired
private ApplikesBehaviorService applikesBehaviorService;

@Override
@PostMapping("/like_behavior")
public ResponseResult saveLikeBehavior(@RequestBody LikesBehaviorDto dto) {
    return applikesBehaviorService.saveLikeBehavior(dto);
}

@Override
@PostMapping("/unlike_behavior")
public ResponseResult saveUnlikesBehavior(@RequestBody LikesBehaviorDto dto) {
    return applikesBehaviorService.saveUnlikesBehavior(dto);
}
```

画面14：
```java
@Autowired
private ApplikesBehaviorService applikesBehaviorService;

@Override
@PostMapping("/like_behavior")
public ResponseResult saveLikeBehavior(@RequestBody LikesBehaviorDto dto) {
    return applikesBehaviorService.saveLikeBehavior(dto);
}

@Override
@PostMapping("/unlike_behavior")
public ResponseResult saveUnlikesBehavior(@RequestBody LikesBehaviorDto dto) {
    return applikesBehaviorService.saveUnlikesBehavior(dto);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

