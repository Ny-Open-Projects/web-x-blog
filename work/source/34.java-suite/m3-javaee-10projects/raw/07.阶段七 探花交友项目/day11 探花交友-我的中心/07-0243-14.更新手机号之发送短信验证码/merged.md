# 14.更新手机号之发送短信验证码

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\14.更新手机号之发送短信验证码_【海量资源尽在 666java.com】.mp4
- 时长 10分41秒（音频 642s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下我们的这个更新手机号的这个功能那么我们更新我们这个手机的这个逻辑呢我们在SSO系统呢完成啊所以说呢我们是需要去配置一下Jex那么为什么要是在SSO系统中完成呢原因是我们的这个短信验证码的发送啊以及我们的一些这个用户的更新啊我们都会放到这个里面来完成的啊所以说也在SSO里面完成
[00:29] 那么对于我们的这个手机号的更新的这个逻辑呢我们大致需要有这样的一个三个步骤啊第一呢我们需要去发送短信的验证码然后呢第二呢我们需要去校验这个验证码第三个呢我们需要去保存我们的一个新的一个手机号那么所以需要有的三个这个接口啊那么接下来呢我们首先来
[00:53] 配置下Nginx让我们的这个urls这个foon这个请求呢就进入到我们的这个sso的这个topcat就18080然后呢我们来找到我们的这个Nginx下面有一个config然后呢找到它然后呢我们来打开一下这个我已经打开了啊然后呢我们就把这个呢大家可以拷贝一下
[01:16] 然后呢就考到我们这个里面来啊那么就是只要映射到这个地址的那么就会进入到它啊然后呢呃别忘记了我们要把我们的ngx呢要做一个reload啊这样的一个操作那我们来写一下叫什么呢ngx-s reload好那么这样的话呢就呃ok了啊呃然后呢我们接下来呢就来一个一个来编写这么几个接口啊首先第一个呢是
[01:46] 发送短信的验证码那么我们先回到我们的这个就是我们的一个默克地址中然后在默克中其实我们可以看到这个接口就是发送我们短信验证码然后它的这个地址是这样的一个地址然后这个是没有任何参数的因为我们需要根据这个token去拿到我们的一个用户的手机号然后再去做一个发送所以说是不需要
[02:13] 其他参数的那么接下来我们就回到哪里这个是有断点那么把这个去掉那么接下来我们回到我们的SSO这个系统那我们进入到SSO里面来然后我们找到SSO里面之前我们已经写过一个叫做Use的Controller那么接下来我们在这个里面去做一个完成
[02:37] 那么首先呢他的这个方法的返回值呢那就是response addt那么这个t呢是谁呢就是word啊没有没有我们的响应的响应内容啊那么这个方法名呢我们就叫他吧那么就发送我们的这个验证码啊然后呢我们去写一个看一下请求是什么呢是post请求那就写一个post mapping然后这个地址我们来拷问一下
[03:03] 那么考过来之后呢把这个us拿掉因为我们上面呢已经有这个us了然后呢呃在我们后面是没有参数的啊但是呢需要注意的是我们是需要拿到我们的token啊所以说呢我们需要把上面这个来我们来拷贝一下那么往后面走来拷贝一下啊把它呢来拷贝一下呃然后呢我们就到这啊到这好嘞好这样的话呢我们就拿到我们这个token了对吧
[03:32] 我们把这个上面的我们都关一下太多了那么我们就把它打开一下好这个呢就是拿到token拿到token之后啊那么接下来呢我们就需要去调用我们的这个叫做usus哎我们是不是没有这个没有这个Service那我们就来创建一个Service那么在这个下面呢去创建一个叫做ususus serviceservice
[04:03] 然后呢去写一个注解叫做Service好嘞好那么接下来呢我们在我们的uscontrol中啊去把它呢注入进来好那么我们去做一个注入那么注入之后啊那么接下来呢我们就去做一个点这个usservice然后呢去发发明就用它吧就是去发送短信的验证码我们把token呢传递过去
[04:33] 然后呢接下来呢我们来看一下它的返回值呢我们就要求它返回一个布尔类型吧然后呢布尔类型那么如果要是发送成功的话那就返回to那我们就return一个response-edit.ok然后呢设置为一个no然后呢我们给它去做一个try catch的一个处理然后呢如果是如果是我们这个
[05:03] 出错的话,我们就给它响应我们的一个500然后呢,state http,state然后点build好,那么这样的话呢,我们这个呢是不是就搞定了那么我们先来写一个这个注释这个就是我们什么呢发送我们的验证码这个逻辑然后呢,我们到这去创建这个方法那我们来看一下这个方法怎么样去创建呢
[05:33] 那么在这个里面呢我们是需要去调用我们的这个就是我们的之前是不是我们写过一个啊叫做我们的一个SMS啊叫做SMS Service写过一个他这个方法啊这个Service然后呢把它注进来然后呢去做一个发送当然了我们首先呢需要查询到我们的一个用户的手机号啊
[05:58] 那么这个手机号怎么查询呢我们就需要通过token来做一个查询了那我们把这个user Service呢去注入进来把这user Service注进来然后呢我们通过race.user Service.query user by token然后呢我们去拿到一个user对象然后呢我们去做一个
[06:28] 我们就不用判断了它肯定是存在的对吧那么当然了如果我们为了这个就是我们的一个程序的一个建状性我们可以判断一下如果空等于U的话那直接什么呢returnreturn false就可以了那么如果不等于空的话那我们就需要拿到它的一个mobile就是我们的手机号拿到手机号之后呢去发送我们的这个验证码
[06:57] 那么我们去这个是我们去拿到他的拿到他的一个返回值就叫mobile然后我们再调用sms的这个servicesend messagesend ms就是发送短信应该是这个不是他应该我们是调用下面的应该是我们是调用他send我们的一个check code
[07:27] 然后呢我们需要去把手机号呢传递给他来看一下啊是这个这个逻辑啊这个方法然后呢我们在这个里面呢去得到一个什么呢我们的一个这个就是map对吧然后呢我们在map中啊那么我们就需要拿到我们的一个响应了那么我们应该叫他result吧result
[07:54] 然后呢通过这个reload呢去拿这个响应啊那么在这个响应体中啊它其实是返回的可以看到它是一个stream object那我们关键是不是拿这个code然后呢等于几的时候是成功呢是不是等于三的时候成功啊所以说我们得这么来玩一下啊呃就是它点get啊get然后呢这个code然后呢我们去给它去转一下啊那么我们就应该是应该是这样
[08:23] 我们去强转成我们的int类型然后呢我们再去哎呀这函底再来一个是吧再来一个括号拿到它的这个intvalue如果等于这个3的话啊等于这个3的话那就代表着我们这个验证码呢是不是就已经发送成功了对吧好那么接下来呢我们就来测试一下我们的这个方法是否OK那么我们把这个sso呢就来重启一下
[08:54] 好那么接下来呢我们就来测试一下还是通过手机呢直接来做一个测试然后呢我们去输入我们的验证码就是0202 6868去先去登录一次啊然后呢去那么获取验证码然后呢123 2456去做一个登录那么等到它这个登录成功之后就会进入到我们的首页然后呢我们会进入到我的这个里面来
[09:25] 然后在这个里面呢有一个通用的设置然后这个里面有一个修改手机号然后呢我们在这个位置点击获取验证码那么在我们这个代码的这个位置啊那么我们去打一个断点吧那我们就打到这个位置来打到这然后呢我们就来试一下点击这个获取验证码那么可以看到请求是不是就来了对吧然后呢我们去进入到我们这个方法然后呢往下面去走
[09:53] 是不是拿到这个U的这个对象了那么拿到那个手机号然后呢我们再去做一个验证码的一个发送啊这个是我们之前啊所写的这样的一个逻辑然后往下面走走去判断我们的Ready时钟是否有手机是否有这个验证码没有然后呢去去发送一个验证码然后呢就123456对吧发送成功了然后呢去写到Ready时钟然后呢去返回OK这样的话呢就
[10:22] 发送成功了发送成功了那么到这里呢我们的这个修改手机号的第一个第一步这个操作是不是就搞定了先去发送这个验证码那之后呢我们就需要去校验这个验证码了OK好那么关于这个第一步的验证码的一个编写的那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现发送短信验证码功能，包括控制器层、服务层代码编写、配置文件设置以及与 Mock 服务的交互。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Typora 文档中“2.10.1. 发送短信验证码”章节，其中包含 mock 接口的“基本信息”和“请求参数”配置，Mock 地址为 https://mock.boxuegu.com/mock/164/users/sendVerificationCode。
画面2：展示文件资源管理器，定位到 Nginx 配置目录，选中 Nginx.conf 文件。
画面3：IDEA 中展示 MovementsController.java 的调试断点，代码为 try-catch 块，用于查询发布列表。
画面4：IDEA 中展示 UsersController.java，高亮显示 @Autowired 注解和 RequestParam 注解的自动补全建议。
画面5：IDEA 中展示 UsersController.java 的 updateNotification 方法，用于更新通知设置。
画面6：IDEA 中展示 UsersController.java，高亮显示上传头像方法的注解和参数。
画面7：IDEA 中展示 UsersController.java 的 sendVerificationCode 方法，用于发送验证码。
画面8：IDEA 中展示 UsersService.java，高亮显示 sendVerificationCode 方法的参数类型。
画面9：IDEA 中展示 UsersService.java，高亮显示 @Autowired 注解和类名补全。
画面10：IDEA 中展示 UsersService.java，高亮显示 Surround With 菜单，用于快速添加 if-else 结构。
画面11：IDEA 中展示 UsersService.java，高亮显示 sendVerificationCode 方法，调用 userService.queryUserByToken(token)。
画面12：展示手机模拟器界面，显示“修改手机号”页面，包含输入框和“下一步”按钮。
画面13：IDEA 中展示 SmsService.java，高亮显示 sendCheckCode 方法，用于发送短信。
画面14：IDEA 中展示 UsersService.java，高亮显示 sendVerificationCode 方法，返回结果的 code 值。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面1：
```
location /users/phone {
    client_max_body_size 300m;
    proxy_connect_timeout 300s;
    proxy_send_timeout 300s;
    proxy_read_timeout 300s;
    proxy_pass http://127.0.0.1:18080;
}
```

画面2：
```
Nginx.conf
```

画面3：
```
public ResponseEntity<PageResult> queryPublishList(@RequestParam(value = "page", defaultValue = "1") Integer page, @RequestParam(value = "pagesize", defaultValue = "10") Integer pageSize) {
    try {
        PageResult pageResult = this.movementsService.queryUserPublishList(page, pageSize);
        return ResponseEntity.ok(pageResult);
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

画面4：
```
@Autowired
private UserInfoController userInfoController;

@RequestMapping(value = "/headPhoto", method = RequestMethod.POST)
public ResponseEntity<Void> amendVerificationCode(@RequestParam("headPhoto") MultipartFile file, @RequestParam("token") String token) {
}
```

画面5：
```
@RequestMapping("/notifications/setting")
public ResponseEntity<Void> updateNotification(@RequestBody Map<String, Object> param) {
    try {
        Boolean likeNotification = param.get("likeNotification");
        Boolean pinglunNotification = param.get("pinglunNotification");
        Boolean gonggaoNotification = param.get("gonggaoNotification");
        this.userService.updateNotification(likeNotification, pinglunNotification, gonggaoNotification);
        return ResponseEntity.ok(null);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面6：
```
package com.tanhua.sso.Controller;

import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RequestMapping("/user")
public class UsersController {
    @PostMapping("/headPhoto")
    public ResponseEntity<Object> saveLogo(@RequestParam("headPhoto") MultipartFile file, @RequestParam("token") String token) {
        return this.userInfoController.saveLogo(file, token);
    }

    @PostMapping("/phone/sendVerificationCode")
    public ResponseEntity<Void> sendVerificationCode(@RequestHeader("Authorization") String token) {
        Boolean bool = this.userService.sendVerificationCode(token);
        if (bool) {
            return ResponseEntity.ok(null);
        }
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    }
}
```

画面7：
```
@PostMapping("/phone/sendVerificationCode")
public ResponseEntity<Void> sendVerificationCode(@RequestHeader("Authorization") String token) {
    Boolean bool = this.userService.sendVerificationCode(token);
    if (bool) {
        return ResponseEntity.ok(null);
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面8：
```
@Service
public class UsersService {
    public Boolean sendVerificationCode(String token) {
    }
}
```

画面9：
```
@Service
public class UsersService {
    @Autowired
    private SmsService smsService;
    @Autowired
    private UserService userService;
    public Boolean sendVerificationCode(String token) {
    }
}
```

画面10：
```
@Service
public class UsersService {
    @Autowired
    private SmsService smsService;
    @Autowired
    private UserService userService;
    public Boolean sendVerificationCode(String token) {
        User user = this.userService.queryUserByToken(token);
        if (null == user) {
            return false;
        }
        String mobile = user.getMobile();
        Map<String, Object> result = this.smsService.sendCheckCode(mobile);
        return (Integer) result.get("code") == 3;
    }
}
```

画面11：
```
@Service
public class UsersService {
    @Autowired
    private SmsService smsService;
    @Autowired
    private UserService userService;
    public Boolean sendVerificationCode(String token) {
        User user = this.userService.queryUserByToken(token);
        if (null == user) {
            return false;
        }
        String mobile = user.getMobile();
        Map<String, Object> result = this.smsService.sendCheckCode(mobile);
        return null;
    }
}
```

画面12：
无代码或配置。

画面13：
```
try {
    String redisKey = "CHECK_CODE_" + mobile;
    String value = this.redisTemplate.opsForValue().get(redisKey);
    if (StringUtils.isNotBlank(value)) {
        result.put("code", 1);
        result.put("msg", "上一次的验证码还未失效");
        return result;
    }
    String code = this.sendSms(mobile);
    if (null == code) {
        result.put("code", 2);
        result.put("msg", "短信发送失败");
        return result;
    }
    // 保存验证码到 Redis
    this.redisTemplate.opsForValue().set(redisKey, code, 5, TimeUnit.MINUTES);
    result.put("code", 3);
    result.put("msg", "验证码发送成功");
    return result;
}
```

画面14：
```
if (null == user) {
    return false;
}
String mobile = user.getMobile();
Map<String, Object> result = this.smsService.sendCheckCode(mobile);
return (Integer) result.get("code") == 3;
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：PPT 标题为“2.10.1. 发送短信验证码”，包含“基本信息”和“请求参数”两个部分。
画面2：无 PPT 标题或架构图。
画面3：无 PPT 标题或架构图。
画面4：无 PPT 标题或架构图。
画面5：无 PPT 标题或架构图。
画面6：无 PPT 标题或架构图。
画面7：无 PPT 标题或架构图。
画面8：无 PPT 标题或架构图。
画面9：无 PPT 标题或架构图。
画面10：无 PPT 标题或架构图。
画面11：无 PPT 标题或架构图。
画面12：无 PPT 标题或架构图。
画面13：无 PPT 标题或架构图。
画面14：无 PPT 标题或架构图。

5) 无。

