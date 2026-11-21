# 05_文章详情_前后台功能接口测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\05_文章详情_前后台功能接口测试【海量资源尽在 666java.com】.mp4
- 时长 13分42秒（音频 823s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好为了能够让大家呢更好的去理解当前这个流程那咱们呢就分别来去测试一下啊通脑测呢是分别从那个功能上去看效果第二个呢是咱们会在后团后端的去打断点来去看一下这个数据的接收好吧行那这个刚才啊咱们把这个东啊其实已经做完了啊效果也演示了就是在当前的比如说你的一个登录的Controller中去打断点然后呢你就能呢去找到
[00:30] 走啊就能去到后台到后台之后呢那这块内容就能去接收到你的用户名和密码是吧然后拿到用户名预览之后呢咱们分别做了验证最终是返回了一个这种令牌TokenOK啊那这个其实咱们已经演示过了咱们就直接放行了啊那放行之后啊你可以看一下啊它呢会直接去跳转到哪呢直接去跳转到当前的一个loadload的请求其实就是咱们的一个主页
[00:58] 那这个在哪呢代码咱们分别从前端到后端去看一下咱们再出去刷一下清掉啊好我点登录好我放行了啊放行之后呢你可以在这往下看啊在这个Nandwork里边去找当前的请求请求里边第一个呢是log author这个呢其实就是登录的请求你所传的就是当前的用户名和密码然后这里有个load这个load的话其实大家都知道啊就是在
[01:32] 之前写过的第一个接口就是加载什么文章的列表信息是吧那这个呢其实其实呢就是他的请求就是他的请求当然咱们当时去做第一天的接口的时候还说了啊你不仅要去加载我所有的这种什么文章信息我还有干嘛呢你还要给我展示或者返回不要展示啊应该是过去发一个这种保存行为的阅读行为的这种行为是吧好你可以往下点啊
[02:02] 点点点点点完之后呢其实就这这发了一个请求但这报一个404大家不要着急那咱们就来调试一下这个404到底是为什么会有404首先来看一下在当前的请求当前请求的话是behaviourapi什么呃ve是吧behaviour应该是后面那个要showbehaviour那个showbehaviour应该是有问题的啊因为咱们后台写的时候好像不是showbehaviour
[02:31] 当然这个前台的请求在哪呢刚才咱们也说了都是在config.js中在这去送装的比如说咱们找到当前的这个show.bhv就它看到了吧是这个路径其实并不是不是这个show不是这个share是show找到的show往下找找一找就这个是吧其实这个其实并不是这个东西咱们后台并不是这么写的那怎么写的呢可以看一下
[03:02] 当时咱们那个写内当前那个Controller是什么样的一个路径啊打开当前的比开门目前的话咱们在这啊只定义了一个类啊打开打开完之后呢你看啊这这都没错是吧然后下面这个save啊其实就这叫save然后其实你改点都行啊只要是前台和后台保持统一就可以目前咱们前台后台都要开发所以说呢你改点都行但是尽量呢是呃去
[03:30] 改这种后台啊用小的你看这个啊是吧这是不喜欢的行为这保存行为是不是不太合适啊应该是什么展示行为啊在这写一个兽这写完之后呢你可以重启一下啊好重启完之后呢那这个应该就没有问题了咱们在这直接打个电啊打个电啊一会儿看他能不能进到这里就可以了好吧行来咱们就来把它清掉啊清掉完之后呢咱们再来去等着看看他到底能不能到这稍等
[04:01] 这个这个启动项目好像稍微有点慢啊他正在加载稍等好应该是结束了啊应该是结束了好那结束之后呢就到这了啊到这之后呢咱们可以去看一下里边的数据是吧DTO点一下因为这个呢其实就是有一个呃当前的设备ID还有一个articleIDarticle的话里边是一个数组啊里边可能有很多的对象啊某一个对象其实就一条数据就只是当前的ID值完事了啊
[04:37] 到这呢其实这个接口也测通了但是这里边我要去解释一下当前这个environment id它是怎么来的它到底是怎么来的呢可以看一下啊我先放行啊放行完之后它就会去保存了啊这也没有报错说明保存是肯定是没有问题的啊主要是咱们来看一下这个数据接收就可以了那这个保存的时候呢不是说这个啊咱们要说当前的这个什么设备id这个设备id啊其实目前的话咱们都都已经写死了比如说你打开当年的home
[05:09] 在Home API里边你可以找到当前这个保存展现行为的这一块这个当前的设备ID是从当前的storage这个storage是谁呢其实就是在当前的一个本地的缓存中去取值在这儿这有个storage这一块目前的话这是写死的就这么一个值就这么一个值那这个值其实转换过来之后就是一个1就是1
[05:38] 因为这个呢咱们知道啊咱们都用了Digson去做序列化是吧你要直接写1的话呢到后台之后它还会反序列化那这时候就不能值了就是它解析不到了就目前的话呢这个值呢是1序列化之后的值所以说呢你把它给放到这儿其实就可以了好吧啊那这个大家一定要理解啊行那这个呢咱们就说明白啊然后继续往下看啊目前的话呢咱们这块你看这块都没问题了啊
[06:08] 呃当前的文章列表展示啊就没问题那咱们再点进去啊点进去哪个呢点进去第一条啊就当前那个游戏制作这个啊我点进去之后呢刚才咱们也讲了应该是从文章列表里边去发送一个事件这个事件的话呢其实用哪个啊打开前端啊当前的打开当前的配置4号目您再去点view
[06:43] 其实就是最后这个事件最后这个事件他通过路由把参数item给传过去了传过去之后我就能在article的页面里边去接收到当前的数据并且他就会去发一个this.loadinfo的请求这个请求其实在这也能看到就是当前的loadarticle不是loadarticleinfo然后他返回的其实就是你的
[07:12] 所有的这种文章的详细信息详细信息拿到这个文章详细信息之后呢咱们又可以干嘛呢就可以去展示当前的文章信息那展示的话其实咱们在那已经看了就不再去看了那还有一个啊还有一些行为那这行为的话咱们再去看一看啊比如说比如啥呢这里边啊是有个东西先看上面吧咱们当时是不是做了一个关注关注和取消关注对吧
[07:44] 那有关注的话呢大家一定要知道就是咱们现在在后台是在哪个Controller中去写的是不是当前的useruser里边是有一个有一个Controller打开其实就是当前那个user了OK啊咱们可以在这打个点啊看看能不能到这好我点了啊点OK那的确是到这了那它传的是啥呢你可以看一下当前的DTO
[08:16] 他传了分别是传了当前的author id也就是当前的文章的作者id然后第二个呢是当前的article idoperation呢是零零是关注一是取消关注ok啊行那到这之后呢咱们可以再往下走进去啊来好嗯往下走啊往下走啊首先是参数的判断没有问题你要拿到一个float id拿到float id啊往下走走
[08:51] 这个Flood ID应该是空的但是空的话没有事咱们需要通过当前的author ID去拿到当前的authorauthor之后咱们再去拿到当前的user ID就可以了走走走走你看这个Flood ID有没有值呢有值是1那为什么是1呢其实这个是手动去设置的你可以先去查看一下当前的author稍等我在这看吧
[09:29] 那这个author id呢是2105你可以去打开当前的作者的表打开啊ap author他你找到当前2105这个数据你看啊2105是2105吧啊2105这个值呢本身是空的你看我在这设置这个11的话呢就是某一个app用户在哪呢你可以去找到当前的ap user表中看看哪个id值
[10:02] 我目前设的就是这条数据也就是说啊当前这个作者对应的APP账号信息就是这一条如果说你这要没有的话你就手动去添上别到时候报错了好吧手动去添上啊行那这时候呢咱们想看啊这时候他有值之后呢就能去通过当前这个东西去保存或者说去保存咱们当前的一个用户关注的一个消息
[10:27] 保存分哪分哪几块呢咱们分两块第一个是要保存当前这个AP user flow第二个呢要保存当前的粉丝是吧咱们可以往下走啊走走走走稍等直接放行吧看报错不报错啊报错了是吧报错了说这有一个by zero啊by zero的话应该是咱们之前呢呃是打了个断点啊这个断点的话咱们在这啊设了一个东西你可以看一下啊
[11:04] 再去这个行为保存的时候啊行为保存的时候这设置了一个这啊这这个白色啊怎么把它给住了啊把它给住了之后呢这个住不住其实都没有事因为它这个义务的其实你要住掉的话呢就是说这个能保存成功如果说不住的话呢它就不能保存成功但是但是我上面这些用户的关系用户关注的关系和当前的粉丝能不能保存成功呢是可以的
[11:34] 是吧是可以的咱们当时说过这个成功或者不成功其实并不影响我的主业务去操作好那这个咱们一路再测那么下面呢就来去看一下这个数据到底有没有分别是找哪两个表哪两个表还知道吧那第一个表呢是当前的AP user flow打开AP user flow刷新一下
[12:00] 其实这个呢其实这条数据啊就是我新保存的数据因为这个时间是对应上的是今天是9月19号没有问题啊咱们呢也可以去看另外一张表另外一张表呢是uap user fund其实这条数据呢就是我刚刚加进来的咱们也可以这样啊也可以这样我现在先取消啊先取消取消完之后呢咱们再来看一下效果啊比如说这是有问题是吗先别取消了好吧我就把这当前的这个注掉了注掉之后呢咱们就来去
[12:31] 重启下项目再来试一试啊好正在启动稍等好这里启动完了啊启动完之后呢咱们可以顺便再去点一下啊点这样啊点之前呢我还是把数据给删了好吧我把数据给删了啊让大家去看看效果把这个数据也删了不要了好那这时候呢就没有数据了啊然后咱们再去点一下啊点一下点那到这了啊我直接放行直接放行啊走好在这里放行走
[13:17] 你看这块它是没有报错的因为刚才我把那个by zero的那个东西给它注掉了啊这时候你可以看一下是不是已经关注了已经关注了啊你看这块它也是给我报了个200这时候咱们可以看一下数据啊看看数据没有保存进来刷新一下你看数据是不是加进来了是吧没问题啊然后你再去看另外一块当前的AP user fund啊刷新一下这个是不是也加了条数据啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个用户关注功能的前后端实现，包括登录校验、前端页面、后端控制器与服务层代码，以及数据库操作和异常处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示登录服务类 `ApplierLoginServiceImpl` 中的 `loginAuth` 方法，用于校验手机号和密码，若为空或不匹配则返回相应错误码。
画面2：继续展示 `loginAuth` 方法，校验逻辑包括手机号和密码是否为空，若为空返回 `PARAM_INVALID`，若用户不存在返回 `AP_USER_DATA_NOT_EXIST`，若密码错误返回 `LOGIN_PASSWORD_ERROR`。
画面3：展示前端配置文件 `config.js`，定义了服务端点、本地服务开关、服务器地址等配置，如 `server_B5: '/server_B5'`。
画面4：展示行为服务控制器 `BehaviorController`，其中包含 `@PostMapping("/show_behavior")` 的 `saveShowBehaviorService` 方法。
画面5：展示 `BehaviorController` 中的 `saveShowBehaviorService` 方法，调试器显示返回值为一个包含19个元素的 `List<ApiArticle>`。
画面6：展示前端存储模块 `storage.js`，定义了 `clearToken`、`_check`、`set`、`get`、`option` 等方法，用于管理存储。
画面7：展示前端页面 `index.Vue`，包含文章列表、作者信息、点赞、收藏、分享等交互按钮。
画面8：展示用户关系控制器 `UserRelationController`，包含 `@PostMapping("/user_follow")` 的 `follow` 方法。
画面9：展示 `AppUserRelationServiceImpl` 中的 `follow` 方法，校验关注者和被关注者ID，若被关注者不存在则返回 `DATA_NOT_EXIST` 错误。
画面10：展示数据库表 `ap_author`，包含 `id`、`name`、`type`、`user_id`、`created_at`、`wm_user_id` 等字段，用于存储作者信息。
画面11：展示 `AppUserRelationServiceImpl` 中的 `follow` 方法，若用户未登录则返回 `UNAUTHORIZED` 错误。
画面12：展示 `AppUserRelationServiceImpl` 中的 `follow` 方法，若用户已关注则返回 `DATA_EXIST` 错误。
画面13：展示 `AppUserRelationServiceImpl` 中的 `follow` 方法，设置关注状态、显示状态、评论状态等，并调用 `appUserFanMapper.insert` 插入数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Override
public ResponseResult loginAuth(Applier user) {
    if (StringUtils.isEmpty(user.getPhone()) || StringUtils.isEmpty(user.getPassword())) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    Applier applier = applierMapper.selectByPhone(user.getPhone());
    if (applier == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.AP_USER_DATA_NOT_EXIST);
    }
    if (user.getPassword().equals(applier.getPassword())) {
        return ResponseResult.errorResult(AppHttpCodeEnum.LOGIN_PASSWORD_ERROR);
    }
}
```

画面2：
```java
@Override
public ResponseResult loginAuth(Applier user) {
    if (StringUtils.isEmpty(user.getPhone()) || StringUtils.isEmpty(user.getPassword())) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    Applier applier = applierMapper.selectByPhone(user.getPhone());
    if (applier == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.AP_USER_DATA_NOT_EXIST);
    }
    if (user.getPassword().equals(applier.getPassword())) {
        return ResponseResult.errorResult(AppHttpCodeEnum.LOGIN_PASSWORD_ERROR);
    }
}
```

画面3：
```javascript
const config = {
    services: {
        article: 'ARTICLE',
        behavior: 'BEHAVIOR',
        user: 'USER',
        login: 'LOGIN'
    },
    local: {
        user: true,
        article: true,
        behavior: true,
        login: true
    },
    prefix: {
        server_B5: '/server_B5'
    },
    load: {
        url: 'api/v1/article/load',
        loadmore: 'api/v1/article/loadmore',
        load_article_info: 'api/v1/article/load_article_info',
        load_search: 'api/v1/article/search/load_search',
        del_search: 'api/v1/article/search/del_search',
        associate_search: 'api/v1/article/search/associate_search',
        article_search: 'api/v1/article/search/article_search',
        show_behavior: 'api/v1/behavior/show_behavior',
        read_behavior: 'api/v1/behavior/read_behavior',
        forward_behavior: 'api/v1/behavior/forward_behavior',
        like_behavior: 'api/v1/behavior/like_behavior'
    }
};
```

画面4：
```java
@Autowired
private AppShowBehaviorService appShowBehaviorService;

@Override
@PostMapping("/show_behavior")
public ResponseResult saveShowBehavior(@RequestBody ShowBehaviorDto dto) {
    return appShowBehaviorService.saveShowBehavior(dto);
}

@Autowired
private AppLikesBehaviorService appLikesBehaviorService;
```

画面5：
```java
// 调试器显示
articles = [ApiArticle ... toString]
0 = (ApiArticle ... toString)
1 = (ApiArticle ... toString)
2 = (ApiArticle ... toString)
...
18 = (ApiArticle ... toString)
```

画面6：
```javascript
clearToken : function(){
    return this._removeToken();
},
_check : function(){
    if(this.storage == null){
        this.storage = weex.requireModule('storage');
        this.setEquipmentId('SD3EBECF883C4E99329AF8A29300A86');
    }
    return this.storage;
},
set : function(key_value){
    let storage = this._check();
    return new Promise((resolve, reject) => {
        storage.set(key_value, function(a){
            if(a.result == 'success'){
                resolve(true);
            }else{
                reject(false);
            }
        });
    });
},
get : function(key){
    let storage = this._check();
    return new Promise((resolve, reject) => {
        storage.get(key, function(a){
            if(a.result == 'success'){
                resolve(a.data);
            }else{
                reject(false);
            }
        });
    });
},
option : function(key){
    let storage = this._check();
    return new Promise((resolve, reject) => {
        storage.get(key, function(a){
            if(a.result == 'success'){
                resolve(a.data);
            }else{
                reject(false);
            }
        });
    });
},
```

画面7：
```html
<template>
    <div class="art-top">
        <text class="title">{{title}}</text>
    </div>
    <div class="head">
        <image src="https://p3.pstatp.com/thumb/1480/178661568" class="head"></image>
        <text class="author">{{author}}</text>
        <text class="time">{{formatDate(date)}}</text>
    </div>
    <div class="empty"></div>
    <div class="content">
        <text class="item" v-if="item.type == 'text'">{{{item.val}}}</text>
        <image :load="imageLoad(item,7)"></image>
    </div>
    <div class="tools">
        <Button text="点赞" @onClick="like" :icon="icon_like" active="relation.isLike" />
        <Button text="收藏" @onClick="collect" :icon="icon_collect" />
        <Button text="分享" @onClick="share" :icon="icon_share" />
        <Button text="评论" @onClick="comment" :icon="icon_comment" />
    </div>
    <div class="art-bottom">
        <Button text="转发" @onClick="forward" :icon="icon_forward" />
        <collection :relation_collection="relation_collection" />
    </div>
</template>
```

画面8：
```java
@RestController
@RequestMapping("/api/v1/user")
public class UserRelationController implements UserRelationControllerApi {

    @Autowired
    private AppUserRelationService appUserRelationService;

    @PostMapping("/user_follow")
    public ResponseResult follow(@RequestBody UserRelationDto dto) {
        return appUserRelationService.follow(dto);
    }
}
```

画面9：
```java
// AppUserRelationServiceImpl
if (followId == null && dto.getAuthorId() == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE, "followId");
} else if (followId == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE, "followId");
}
if (authorId == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE, "authorId");
}
if (followId == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.DATA_NOT_EXIST, "关注者不存在");
}
```

画面10：
```sql
SELECT * FROM `ap_author` LIMIT 0, 1000
```

画面11：
```java
// AppUserRelationServiceImpl
// 判断当前用户是否已经关注
Applier user = AppliedLocalUtils.getUser();
if

