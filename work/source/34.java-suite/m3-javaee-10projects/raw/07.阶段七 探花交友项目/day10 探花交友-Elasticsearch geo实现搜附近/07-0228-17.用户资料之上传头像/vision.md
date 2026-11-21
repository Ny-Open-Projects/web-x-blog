# 画面线理解：17.用户资料之上传头像

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\17.用户资料之上传头像_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 01:10, 02:08, 02:40, 02:58, 03:19, 03:38, 03:53, 04:09, 04:32, 05:05, 05:24, 06:03, 06:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:34:41

1) 这一组画面整体在讲什么（一句话）：
演示用户头像上传功能的前后端实现，包括前端页面、后端控制器代码、服务层逻辑、Nginx配置以及移动端的上传流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示用户资料编辑页面，包含头像、昵称、生日、现居城市等字段，用于演示用户头像上传功能的前端界面。
画面2：展示Nginx配置文件中的location块，用于配置静态资源和代理转发。
画面3：展示Nginx配置文件的目录结构，包含conf、logs、temp等目录，以及nginx.exe文件。
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
nginx.conf
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
