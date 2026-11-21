# 14_app文章详情_文章关系接口_service代码编写(1)

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\14_app文章详情_文章关系接口_service代码编写(1)【海量资源尽在 666java.com】.mp4
- 时长 11分17秒（音频 678s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就继续往下讲刚才是把所有的Map文件都已经说完了这篇内容主要是还是根据当前的思路咱们去写当前的Service那这Service写的时候咱们先把它给关了先把所有都关掉然后到哪个模块去写是不是当前的article是吧到这然后打开这之后咱们就在这去先去创建一个Service
[00:29] 新传言Service这个Service在这这个Service叫啥呢叫article info Service这有了是吗之前咱们是设置过一个是吧那在那咱们在这再去加一个再加一个的话其实方法呢就比较简单了就是跟之前是差不多的这个呢主要呢是加载加载文章详情初始化配置信息
[01:02] 这个配置进行呢其实主要包括了刚才没说的比如什么呢关注啊是吧收藏啊喜欢应该是点赞啊点赞不喜欢是吗没了是吧这四个啊目前的话咱就有四个ok行那这个再往下去看啊那这个方法该怎么定义呢统一都反馈什么呢然后respawns result然后怎么叫load article
[01:30] load article behavior好吧我们看这个是怎么写的啊当前啊就他是吧ok 考过来参数呢参数是一样的是吧参数的话就是当前的article info dto啊article info dtook dto 完了那这样的话咱们这个Service啊就算是定好了定好之后呢下面咱们继续往下写这个Service啊
[02:00] 那这个Service呢其实咱们已经写了一部分了是吧咱们继续往下啊让它control i一下啊直接去方法重写方法现在放到放到放到下边好吧放到下边啊好那这方法有了那这里边该怎么去写呢有什么逻辑呢逻辑是不是就是这个逻辑啊是吧好拷贝一下啊拷贝一下我就稍微简化一下稍微简化一下啊这个干掉啊123啊行也可以啊我一个个去加吧好吧哎
[02:44] 二三四这个也加上啊然后我看啊行那这个加完之后呢咱们下面去来说一下首先第一步呢咱们要去通过这个设备ID或者是用户ID去查看去查找行为实体对吧那行为实体该怎么去找呢其实这个代码咱们之前是学过的首先咱们是应该先获取谁呀先获取用户ID
[03:15] 那用户ID怎么获取咱们是学过叫app-local-youtube.com.us然后咱们就可以拿到当前的一个用户信息然后咱们就去判断判断啥呢判断当前的用户如果说等于等于那按的什么ETO打什么这个设备ID等于等于那的话这时候呢
[03:46] 因为它两个不能同时都为难只能说最少有一个是吧最少有一个所以咱们直接去返回一个response result.irror result说你的参数啊说你的参数有问题PPP下面这个参数他说的参数是有问题的我看是哪个是缺少参数是缺少参数这是一步这是一步
[04:14] 刚才说了Jab为啥要这么写用于用户与设备不能同时为空再往下看这时候如果说Jab过了这时候咱们就可以查了查的话其实很简单你首先要去注入一个当前的行为实体的Map这个咱们之前是写过的行为实体写的APBehaviour
[04:44] entrymifer就是他啊好他有了之后呢咱们就可以去查了查询的方式呢就是有一个slagged by user id那一个设备id就是他两个是可以通过某一个运动id或者是设备id去查询的啊所以说user.idget id啊好第二个呢是tto.什么而且那个increment
[05:28] 好第二参数呢就是当前的设备ID对吧OK啊这时候他返回的就是一个行为实体的名称行啊行为实体对象啊这个拿到之后呢这个内容啊咱们还要自己改一改啊拿了之后咱们又再说这个user ID啊咱们之前说过那这么写的话有可能他会为浪是吧你直接去点get ID可能就直接为空了所以说呢咱们在这单独去处理一步好吧怎么处理啊是首先呢咱们在这去定义一个lang类型的user
[05:58] 这个之前大板写过的啊等于none然后呢if如果说user不等于none怎么办呢user.id等于谁啊user.getid好吧这样就可以了啊这样的话是即使他那个他为空是吧他为空的话呢也没有事啊咱们传个none进去也是可以的啊但你要直接说user.getid的话有可能会爆空的真是吧所以说咱们现在是
[06:29] 把当前的user id放到这可以了啊行那这个啊这只是咱们完成了第一步只是完成第一步那第二步要干嘛呢第二步第二步是不是要去通过当前的entry id和什么article id去查看咱们的收藏啊是吧没问题吧ok那这个收藏的话其实这样啊咱们先不去查咱们首先呢先去定义定义啥呢就是定义一个东西出来
[06:55] 这个东西呢其实跟他们的接口有关系咱们可以打开他们接口的定义啊接入定义里边呢咱们已经说说完了这啊你需要去返回这四个东西啊是is trueis likeis unlike还是什么is collection这时候它反复的这个是什么呢是true或者是first就是反而不而类型那这时候咱们先去把这个东西给定义出来好吧好比如说咱们先去定义一个啊
[07:23] 统一就是为了能够更方便的复制和返回啊而不而上 is unlikelike like 没有like啊好是 first然后第二个参数呢就是 is 什么like 是吧等于相一个默认值都是 first 啊它是 is collectionc o i r e c t o i r 啊好等于 first然后再往再最后一个什么 is flow好等于啥呢它也等于 first
[07:55] 好吧那这样设置完之后呢咱们先去设置了这几个局部变量一个是is unlike第二个呢是is like还有is collection这是收藏这是关注是否关注然后下面咱们再去做另外一个东西我们去抽出来一个post为什么要抽出来一个post呢可以啊这样
[08:17] 咱们呢这里边因为涉及到了四张表去查询那应该是五张表是吧咱们已经是查询了一张表了啊说了咱们一共是查询六张表是吧一共查询六张表啊那目前的话咱们第一张表其实已经做完了然后下面呢咱们主要是说第二啊下面的五张那下面这五张的话首先呢他查询的时候呢有一些他需要一个boss的对条件进行查询当然不喜欢这个他不需要比如说咱们就这个收藏表跟点赞表
[08:46] 收入插表跟点单表那这个它的分表字段是啥呢分表段的话首先呢你还得去看谁啊你还得去看咱们当之前啊在这设置了路由的定义咱们可以分别去看一下嗯不喜欢他没有没有分啊没有分表所以说咱们这个不用去看啊那往下走走你看这个啊AP Connection好往下你看这个他的分表的字段嗯然后拉一拉啊拉不过来是吗选中好
[09:21] 你看他的分表字段是什么entry id啊entry id下面这个lags他的分表字段什么呢也是entry id是一样的啊是一样的啊他两个分表字段都是entry id所以说这时候呢咱们就可以抽出来啊抽出来一个啊呃怎么抽呢就是四针Burst等于啥呢等于咱们之前呢应该是封装一个工具类叫Burstqtus.corbo1那为什么写一个corbo1呢
[09:53] 因为当前的ID啊你可能不太知道比如说你你你可能不知道当前的什么刚才这两表的ID啊你不知道当前的什么收藏的ID和不知道当前的什么这个喜欢的ID喜欢这个表的ID那这时候呢你怎么办呢咱们可以去拿寻拿到第一组就是group这不是一吗group是组吗哪组呢是一组那一组的话呢咱们就拼装的时候就是拼装的是
[10:23] 前面第一个啥呢第一个拼完的就是零啊你都是零后边是前的一个组这叫分表的ID啊分表的ID啊这个大家一定要留意点啊因为前面这个数啊其实你要是小于五亿的话呢其实多少多少都无所谓他都是在第一个组当中是吧第一组当中啊行那这个设置的时候那这个里边写啥呢里边写的话其实就是当前的什么当前发的什么
[10:53] ID吧RET ID好那让你结束了啊这时候咱们再去查询再去查询这个收藏和喜欢表的时候咱们都可以去把这个BOSS给传过去就可以了啊行咱们再往下看啊那这时候咱们都应该该做完的工作都做完了下面咱们就写具体的一些这种东西

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过文章ID查询文章详情并加载用户行为（收藏、点赞、不喜欢、关注）数据，涉及服务层代码实现与数据库表结构设计。

2) 按时间顺序列出每张画面的要点：
画面1: 展示ArticleInfoDto类定义及行为表映射说明，右侧列出通过equipmentId或userId查询行为实体（entryId）的逻辑。
画面2: 展示IDE中项目结构，定位到heima-leadnews-article模块下的Service包。
画面3: 展示AppArticleInfoServiceImpl类中根据文章ID查询文章内容和配置的代码。
画面4: 展示AppArticleInfoServiceImpl类中loadArticleBehavior方法的开始部分，注释说明通过equipmentId或userId查询行为实体。
画面5: 展示loadArticleBehavior方法中对user和equipmentId的非空校验逻辑。
画面6: 展示loadArticleBehavior方法中对user和equipmentId的非空校验逻辑，使用AppThreadLocal工具类获取用户信息。
画面7: 展示loadArticleBehavior方法中声明并初始化ApBehaviorEntryMapper。
画面8: 展示loadArticleBehavior方法中通过ApBehaviorEntryMapper查询行为实体。
画面9: 展示loadArticleBehavior方法中对user非空的判断逻辑。
画面10: 展示loadArticleBehavior方法中对user非空的判断逻辑，以及查询行为实体的SQL语句。
画面11: 重复画面1的内容，展示ArticleInfoDto类定义及行为表映射说明。
画面12: 展示Typora中文章行为表的表结构设计，包含ap_follow_behavior、ap_share_behavior、ap_collection、ap_likes_behavior等表。
画面13: 展示Typora中文章行为表的表结构设计，继续展示ap_likes_behavior表的详细配置。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面3:
```java
//根据文章id查询content信息
ArticleConfig aparticleConfig = aparticleConfigMapper.selectByArticleId(articleId);
if(aparticleConfig==null){
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
}else if(!aparticleConfig.getIsData()){
    aparticleContent = aparticleContentMapper.selectByArticleId(articleId);
    String content = StringUtils.join(aparticleContent.getContent(), "");
    aparticleContent.setContent(content);
    data.put("content",aparticleContent);
    data.put("config",aparticleConfig);
}
return ResponseResult.okResult(data);
```

画面4:
```java
@Override
public ResponseResult loadArticleBehavior(ArticleInfoDto dto) {
    //1. 通过equipmentId或userId查看行为实体 -->entryId
    //2. 通过entryId和articleId去查看收藏表，看是否有数据，有数据就说明已经收藏，否则就是没有收藏
    //3. 通过entryId和articleId去查看点赞表，看是否有数据，有数据就说明已经点赞，否则就是没有点赞
    //4. 通过entryId和articleId去查看不喜欢表，看是否有数据，有数据就说明不喜欢，否则就是喜欢
    //5. 通过authorId去app的id  user_id( app账号信息id)
    //查看关注表，根据当前登录人的userId与作者的app账号id去查询，如果有数据，就说明已经关注，没有则说明没有关注
    return null;
}
```

画面5:
```java
if(user==null && dto.getEquipmentId()==null){
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE);
}
```

画面6:
```java
if(user==null && dto.getEquipmentId()==null){
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE);
}
```

画面7:
```java
@Autowired
private ApBehaviorEntryMapper apBehaviorEntryMapper;
```

画面8:
```java
@Override
public ResponseResult loadArticleBehavior(ArticleInfoDto dto) {
    ApUser user = AppThreadLocalUtils.getUser();
    if(user==null && dto.getEquipmentId()==null){
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE);
    }
    //1. 通过equipmentId或userId查看行为实体 -->entryId
    ApBehaviorEntry apBehaviorEntry = apBehaviorEntryMapper.selectByUserIdEquipmentId(user.getId(), dto.getEquipmentId());
```

画面9:
```java
if(user==null){
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE);
}
```

画面10:
```java
if(user==null){
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE);
}
```

画面12:
```markdown
| 表名 | 是否分库 | 分库类型 | 分库数量 | 分库策略 | 主键 |
|------|----------|----------|----------|----------|------|
| ap_follow_behavior | 是 | mycat | 2,000,000 | 1 | DN[1] | entry_id |
| ap_share_behavior | 是 | mycat | 1,000,000 | 1 | DN[2] | entry_id |
| ap_collection | 否 | zk_sequence | 1,000,000 | 50 | DN[0~49] | burst-(id_entry_id) |
| ap_likes_behavior | 否 | zk_sequence | 5,000,000 | 50 | DN[0~49] | burst-(id_behavior_entry_id) |
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面12、13: 展示Typora中文章行为表的表结构设计，包含ap_follow_behavior、ap_share_behavior、ap_collection、ap_likes_behavior等表，以及它们的分库、分库类型、分库数量、分库策略和主键等信息。

5) 无。

