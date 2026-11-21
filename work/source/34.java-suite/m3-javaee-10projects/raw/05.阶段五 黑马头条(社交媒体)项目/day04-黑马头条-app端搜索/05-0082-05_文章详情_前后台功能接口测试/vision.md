# 画面线理解：05_文章详情_前后台功能接口测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\05_文章详情_前后台功能接口测试【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:22, 01:14, 02:37, 03:43, 04:37, 06:02, 06:54, 08:00, 09:06, 10:05, 11:00, 11:43, 12:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:29:27

1) 这一组画面整体在讲什么（一句话）：
演示一个用户关注功能的前后端实现，包括登录校验、前端页面、后端控制器与服务层代码，以及数据库操作和异常处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示登录服务类 `ApplierLoginServiceImpl` 中的 `loginAuth` 方法，用于校验手机号和密码，若为空或不匹配则返回相应错误码。
画面2：继续展示 `loginAuth` 方法，校验逻辑包括手机号和密码是否为空，若为空返回 `PARAM_INVALID`，若用户不存在返回 `AP_USER_DATA_NOT_EXIST`，若密码错误返回 `LOGIN_PASSWORD_ERROR`。
画面3：展示前端配置文件 `config.js`，定义了服务端点、本地服务开关、服务器地址等配置，如 `server_B5: '/server_B5'`。
画面4：展示行为服务控制器 `BehaviorController`，其中包含 `@PostMapping("/show_behavior")` 的 `saveShowBehaviorService` 方法。
画面5：展示 `BehaviorController` 中的 `saveShowBehaviorService` 方法，调试器显示返回值为一个包含19个元素的 `List<ApiArticle>`。
画面6：展示前端存储模块 `storage.js`，定义了 `clearToken`、`_check`、`set`、`get`、`option` 等方法，用于管理存储。
画面7：展示前端页面 `index.vue`，包含文章列表、作者信息、点赞、收藏、分享等交互按钮。
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
