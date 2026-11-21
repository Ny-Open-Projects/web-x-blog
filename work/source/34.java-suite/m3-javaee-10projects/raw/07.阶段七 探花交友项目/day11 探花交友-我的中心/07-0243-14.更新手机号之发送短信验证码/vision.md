# 画面线理解：14.更新手机号之发送短信验证码

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\14.更新手机号之发送短信验证码_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:43, 01:25, 02:16, 02:55, 03:34, 04:12, 04:54, 05:30, 06:15, 07:01, 07:55, 09:29, 10:02, 10:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:46:49

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现发送短信验证码功能，包括控制器层、服务层代码编写、配置文件设置以及与 Mock 服务的交互。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Typora 文档中“2.10.1. 发送短信验证码”章节，其中包含 mock 接口的“基本信息”和“请求参数”配置，Mock 地址为 https://mock.boxuegu.com/mock/164/users/sendVerificationCode。
画面2：展示文件资源管理器，定位到 nginx 配置目录，选中 nginx.conf 文件。
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
nginx.conf
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
package com.tanhua.sso.controller;

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
