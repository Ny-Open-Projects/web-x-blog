# 17.用户资料之上传头像

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\17.用户资料之上传头像_【海量资源尽在 666java.com】.mp4
- 时长 6分32秒（音频 392s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么最后一个内容呢我们来看一下头像的这个上传那么这个头像上传呢其实我们可以看到在这个位置啊我们也可以重新再选择我们这个头像的去做一个上传啊当然了我们其实这个头像的上传呢在我们之前的SSO系统中呢已经就完成了这个上传的逻辑啊只是说我们的这个路径啊就是我们现在比如说来看啊保存头像这个路径呢
[00:27] 跟我们之前的SSO中的这个路径是不一样的但他请求的参数什么都是一样的这个时候怎么办呢我们会有两种选择那么就第一种选择呢就是我们在我们的server工程中呢我们再来写一套这个上传逻辑这个好像有点重复了不是太好对吧那么另外一种方式就是我们可以直接让他去使用SSO里面的那个逻辑
[00:52] 但是呢现在他的这个请求路径呢又是不一样的那么我们应该怎么办呢那我们其实只需要去修改一下NJX的配置啊就可以了那么我们来看一下这个NJX的配置怎么样去做一些这个调整那我们来看一下那么主要呢其实就是在下面的这个位置啊需要去做调整那就是在哪呢在这那么我们希望他去按照这个去做一个映射的时候呢
[01:19] 我们也去映射到我们这个18080的这个这个端口就可以了然后呢上面这个URA你看URA走的是这个18080没有问题那么如果URA这个HAND的话也是到这里但是如果是走到ES的话那么就会走到这一档18082里面来那么如果是我们走的是其他的话那么就进入我的18081所以说呢我们会根据这个我们会根据我们的不同的这个映射呢
[01:49] 就直接进入到我们的这个SSL工程就可以了但是呢现在我们只需要去修改我们的一个这个就是我们的一个ngx的一个配置是不是已经修改好了大家别忘记进行做一个reload就是我给大家来演示一下那么就是在我们这个位置然后呢我们去做一个做一个ngx我们应该是应该是把它退出一下
[02:18] 应该是我们要去通过一个这个ngx exe-s reload然后呢把我们这个修改的一个配置文件的去让它生效那么这是我第一个做的事情啊那么现在呢我们是不是请求这个地址就能够进入到我们的SSO的这个系统了但是呢在我们的SSO里面它并没有去接收我们这个请求的一个处理那么这个时候怎么办呢我们来找到我们的SSO啊那么在SSO里面啊在SSO里面呢我们去找到我们
[02:47] 的这个Controller那么之前的我们图片的上传呢我们是写到这个里面来就是在下面的是不是就在这个位置啊对吧在这个位置那么我们应该怎么样去使用它呢我们就应该这么来玩那我们再来写一个叫做usr的一个controllercontroller然后呢把它定义为也是一个restcontroller然后呢再写一个request mapping然后呢我们去写一个usr
[03:15] 然后呢我们下面再来写一个这个方法就是一个上传头像这个方法把这个呢拷贝过来但是呢我们不需要啊这个完全拷贝它这个逻辑啊那么上传头像我们来看一下这个路径啊我们把这个路径要保持对的啊那么这个是hand这个是直接我们去写一个us下面的一个hand就可以了然后呢下面的请求参数呢那就是这个参数那么参数呢是
[03:43] 参数是没有问题的对吧好嘞那么接下来来看一下怎么操作呢那么我们来做一个这个C5一个logo那么这个我们就全部都去掉了我们只需要把我们之前的这个Controller注入进来是不是就可以附用我们这个逻辑了那么我们就注一个叫做UinfoController把Controller注入进来然后呢下面呢我们就可以return一个this.这个Controller.
[04:12] C5 logo这个方法那么把这个fail和token传递过去好那么这样的话我们这个就实现了对吧好那么接下来呢我们就来把我们的这个SSO呢我们重启一下那我们来看一下它的这个效果OK好那么现在呢就服务启动好了那么接下来呢我们就再来测试一下那么我们还是我们
[04:39] 重新把这个应用退出那么我们重新再进入一次那我们再来去做一个这个测试啊然后我们稍微等一下它的一个启动然后呢我们在这个位置啊去输入我们的手机号嗯然后呢去获取验证码然后123嗯123456好登录那么现在它就登录成功了
[05:08] 那么接下来呢我们就进入这个我的这个模块中啊然后呢我们去查询用户的这个资料的数据然后呢在头像这个位置然后呢我们去选择我们没有图片吗看一下有没有图片有图片啊那我们就随便来一个吧那么这个肯定是不行的对吧那我们得来这个因为我们对头像的是有个教验的对吧好那我们就用它吧这个头像啊小孩这个头像
[05:34] 那我们去上传啊上传现在是不是就成功了好那我们哎这块是不是还没有成功那么再去加载一下但是这块好像没换掉啊那么我们再来点一下其他地方啊点过来看他会不会换掉啊这个时候呢他这个头像是不是就换掉了
[05:52] 我们再来去点击加载头像就是我们刚刚所选择这个头像那就说明我们刚刚的配置是不是就没问题搞定了所以说对于头像的上传我们变得就非常简单我们只需要附用我们之前的SSO逻辑就可以了但是我们要注意的是对于Nex的配置我们需要再添加一条这样的一个配置
[06:15] 那么到这里呢最终呢我们就已经实现了我们的这个头像的一个上传那么到这里呢我们关于用户资料的一个维护的功能呢我们就做完了对吧好那么关于我们的用户资料的一个维护呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示用户头像上传功能的前后端实现，包括前端页面、后端控制器代码、服务层逻辑、Nginx配置以及移动端的上传流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示用户资料编辑页面，包含头像、昵称、生日、现居城市等字段，用于演示用户头像上传功能的前端界面。
画面2：展示Nginx配置文件中的location块，用于配置静态资源和代理转发。
画面3：展示Nginx配置文件的目录结构，包含conf、logs、temp等目录，以及Nginx.exe文件。
画面4：展示Java后端代码，实现用户点赞功能，包含likeUser和dislikeUser方法。
画面5：展示UserInfoController中saveLogo方法的代码，用于处理用户头像上传。
画面6：展示UserInfoController中saveLogo方法的代码，用于处理用户头像上传。
画面7：展示UserInfoController中saveLogo方法的代码，用于处理用户头像上传。
画面8：展示UserInfoController中saveLogo方法的代码，用于处理用户头像上传，增加图片非人像的错误提示。
画面9：展示UsersController中saveLogo方法的代码，用于处理用户头像上传。
画面10：展示UsersController中saveLogo方法的代码，用于处理用户头像上传，通过UserInfoController调用服务。
画面11：展示移动端Genymotion模拟器界面，显示“999 请联系程序猿”错误提示。
画面12：展示移动端Genymotion模拟器界面，显示相册中多张图片，用于选择头像。
画面13：展示移动端Genymotion模拟器界面，显示用户个人主页，包含昵称和现居城市。
画面14：展示Typora编辑器中的用户个人主页界面，包含“我的动态”、“谁看过我”、“通用设置”、“客服在线”等选项。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```
# error_page  404  /404.html;
# redirect server error pages to the static page /50x.html
error_page  500 502 503 504 /50x.html;
location = /50x.html {
    root   html;
}

location /user/ {
    client_max_body_size 300m;
    proxy_connect_timeout 30s;
    proxy_send_timeout 30s;
    proxy_read_timeout 30s;
    proxy_pass http://127.0.0.1:8080;
}

location /users/header {
    client_max_body_size 100m;
    proxy_connect_timeout 30s;
    proxy_send_timeout 30s;
    proxy_read_timeout 30s;
    proxy_pass http://127.0.0.1:8080;
}

location / {
    client_max_body_size 300m;
    proxy_connect_timeout 30s;
    proxy_send_timeout 30s;
    proxy_read_timeout 30s;
    proxy_pass http://127.0.0.1:8080;
}
```

画面3：
```
fastcgi.conf
fastcgi_params
Nginx.conf
```

画面4：
```
public Boolean likeUser(Long likeUserId) {
    User user = UserThreadLocal.get();
    String id = this.userLikeApi.saveUserLike(user.getId(), likeUserId);
    if (StringUtils.isEmpty(id)) {
        return false;
    }
    if (this.userLikeApi.isMutualLike(user.getId(), likeUserId)) {
        // 相互喜欢成为好友
        this.imService.contactUser(likeUserId);
    }
    return true;
}

public Boolean dislikeUser(Long likeUserId) {
    User user = UserThreadLocal.get();
    String id = this.userLikeApi.deleteUserLike(user.getId(), likeUserId);
    return this.userLikeApi.deleteUserLike(user.getId(), likeUserId);
}
```

画面5：
```
@RequestMapping("loginReginfo/head")
@PostMapping
public ResponseEntity<Object> saveLogo(@RequestParam("headPhoto") MultipartFile file, @RequestHeader("token") String token) {
    try {
        Boolean bool = this.userInfoService.saveLogo(file, token);
        if (bool) {
            return ResponseEntity.ok(null);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    ErrorResult errorResult = ErrorResult.builder().errorCode("000000").build();
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(errorResult);
}
```

画面6：
```
@RequestMapping("loginReginfo/head")
@PostMapping
public ResponseEntity<Object> saveLogo(@RequestParam("headPhoto") MultipartFile file, @RequestHeader("token") String token) {
    try {
        Boolean bool = this.userInfoService.saveLogo(file, token);
        if (bool) {
            return ResponseEntity.ok(null);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    ErrorResult errorResult = ErrorResult.builder().errorCode("000000").build();
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(errorResult);
}
```

画面7：
```
@RequestMapping("loginReginfo/head")
@PostMapping
public ResponseEntity<Object> saveLogo(@RequestParam("headPhoto") MultipartFile file, @RequestHeader("token") String token) {
    try {
        Boolean bool = this.userInfoService.saveLogo(file, token);
        if (bool) {
            return ResponseEntity.ok(null);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    ErrorResult errorResult = ErrorResult.builder().errorCode("000000").build();
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(errorResult);
}
```

画面8：
```
@RequestMapping("loginReginfo/head")
@PostMapping
public ResponseEntity<Object> saveLogo(@RequestParam("headPhoto") MultipartFile file, @RequestHeader("token") String token) {
    try {
        Boolean bool = this.userInfoService.saveLogo(file, token);
        if (bool) {
            return ResponseEntity.ok(null);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    ErrorResult errorResult = ErrorResult.builder().errorCode("000000").errMessage("图片非人像，请重新上传").build();
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(errorResult);
}
```

画面9：
```
public class UsersController {

    @RequestMapping("users")
    @PostMapping
    public ResponseEntity<Object> saveLogo(@RequestParam("headPhoto") MultipartFile file, @RequestHeader("token") String token) {
        return this.userInfoController.saveLogo(file, token);
    }
}
```

画面10：
```
@AutoWired
private UserInfoController userInfoController;

@RequestMapping("users")
@PostMapping
public ResponseEntity<Object> saveLogo(@RequestParam("headPhoto") MultipartFile file, @RequestHeader("token") String token) {
    return this.userInfoController.saveLogo(file, token);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

