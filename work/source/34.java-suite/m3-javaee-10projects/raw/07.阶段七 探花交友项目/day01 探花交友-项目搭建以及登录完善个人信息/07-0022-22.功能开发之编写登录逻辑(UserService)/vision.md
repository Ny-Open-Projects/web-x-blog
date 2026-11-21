# 画面线理解：22.功能开发之编写登录逻辑（UserService）

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\22.功能开发之编写登录逻辑（UserService）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:58, 03:38, 05:45, 07:04, 08:50, 10:34, 12:48, 14:37, 16:02, 17:06, 18:22, 19:42, 21:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:12:34

1) 这一组画面整体在讲什么（一句话）：
实现一个基于 Spring Boot 的用户登录系统，包含前端请求、SSO 服务验证、Redis 存储验证码、用户注册与密码加密、以及发送短信验证码的完整流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示用户登录流程图，包含客户端、SSO、Redis、数据库、JWT Token 等组件及其交互关系。
画面2：展示 UserController 类的代码，定义了 login 接口，接收手机号和验证码。
画面3：在 UserController 中，通过右键菜单选择创建 Java 类，准备添加新功能。
画面4：展示 UserService 类，定义了 login 方法，接收手机号和验证码。
画面5：在 UserService 中，开始编写 login 方法，准备从 Redis 获取验证码。
画面6：在 UserService 中，使用 StringUtils 判断验证码是否为空。
画面7：在 UserService 中，使用 QueryWrapper 查询用户是否存在。
画面8：在 UserService 中，如果用户不存在则创建新用户并设置密码。
画面9：在 UserService 中，使用 redisTemplate.opsForValue() 方法操作 Redis。
画面10：在 UserService 中，将生成的 token 存储到 Redis。
画面11：在 UserService 中，定义 Logger 日志对象。
画面12：在 UserService 中，开始编写登录逻辑。
画面13：在 UserService 中，使用 SignatureAlgorithm.HS256 算法对 token 进行签名，并发送短信。
画面14：展示 UserController 中的 login 方法，调用 UserService 的 login 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
用户接收收到验证码后，进行输入验证码，点击登录，前端系统将手机号以及验证码提交到SSO进行校验。
```

画面2：
```java
package com.tanhua.sso.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {

}
```

画面4：
```java
@Service
public class UserService {

    private RedisTemplate<String,String> redisTemplate;

    @param mobile
    @param code
    @return
    public String login(String mobile, String code) {
        //校验验证码是否正确
        String redisKey = "CHECK_CODE_" + mobile;
        String value = this.redisTemplate.opsForValue().get(redisKey);
        if(StringUtils.isEmpty(value)) {
            return null;
        }
    }
}
```

画面5：
```java
if(StringUtils.isEmpty(value)) {
    return null;
}
```

画面6：
```java
QueryWrapper<User> queryWrapper = new QueryWrapper<>();
queryWrapper.eq(column, "mobile");
User user = this.userMapper.selectOne(queryWrapper);
if(null == user) {
    // 该手机号未注册
    user = new User();
    user.setMobile(mobile);
    user.setPassword(DigestUtils.md5Hex(data: "123456"));
    this.userMapper.insert(user);
}
```

画面7：
```java
if(null == user) {
    // 该手机号未注册
    user = new User();
    user.setMobile(mobile);
    user.setPassword(DigestUtils.md5Hex(data: "123456"));
    this.userMapper.insert(user);
}
```

画面8：
```java
if(null == user) {
    // 该手机号未注册
    user = new User();
    user.setMobile(mobile);
    user.setPassword(DigestUtils.md5Hex(data: "123456"));
    this.userMapper.insert(user);
}
```

画面9：
```java
this.redisTemplate.opsForValue().set(redisTokenKey, redisTokenValue, 1, TimeUnit.MINUTES);
```

画面10：
```java
this.redisTemplate.opsForValue().set(redisTokenKey, redisTokenValue, 1, TimeUnit.MINUTES);
```

画面11：
```java
private static final Logger logger = LoggerFactory.getLogger(UserService.class);
```

画面12：
```java
private static final Logger logger = LoggerFactory.getLogger(UserService.class);
```

画面13：
```java
try {
    // 将token存储到redis中
    String redisTokenKey = "TOKEN_" + token;
    String redisTokenValue = MAPPER.writeValueAsString(redisToken);
    this.redisTemplate.opsForValue().set(redisTokenKey, redisTokenValue, 1, TimeUnit.MINUTES);
} catch (Exception e) {
    LOGGER.error("存储token出错", e);
    return null;
}
```

画面14：
```java
@RestController
public class UserController {

    @Autowired
    private UserService userService;

    @PostMapping("/login")
    public ResponseEntity<Object> login(@RequestBody Map<String,String> params) {
        String mobile = params.get("phone");
        String code = params.get("verificationCode");
        this.userService.login(mobile, code);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
架构图结构：
- 客户端 → 手机号/验证码 → SSO
- SSO → 控制手机号 → 数据库
- 数据库 → 有效期字段 → JWT Token
- JWT Token → 用户登录成功

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
