# 画面线理解：15.更新手机号之校验验证码

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\15.更新手机号之校验验证码_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 01:05, 01:38, 02:34, 03:25, 04:05, 04:52, 05:43, 06:39, 07:40, 08:34, 09:13, 10:01, 10:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:47:37

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的手机验证码功能的前后端实现，包括接口定义、控制器逻辑、服务层处理、Redis 缓存和短信发送逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Mocky 网站上定义的手机验证码接口，包含请求头 Authorization 和请求体参数 verificationCode，以及返回数据结构（verification: boolean）。
画面 2: 展示了 UsersController.java 中的 sendVerificationCode 方法，用于发送验证码，接收 token 并调用 userService。
画面 3: 展示了 UsersController.java 中的 checkVerificationCode 方法，用于校验验证码，接收 RequestBody 参数。
画面 4: 展示了 checkVerificationCode 方法中获取参数的代码，使用 String param.get("verificationCode")。
画面 5: 展示了 Map<String, Object> 类型的参数处理，调用 result.put("verification", bool)。
画面 6: 展示了 checkVerificationCode 方法的完整逻辑，包括获取参数、调用 userService.checkVerificationCode、构建返回结果。
画面 7: 展示了 SmsService.java 中的 sendCheckCode 方法，用于发送短信验证码，使用 RedisTemplate 检查验证码是否已发送。
画面 8: 展示了 UserService.java 中的 sendVerificationCode 方法，通过 token 查询用户并调用 smsService.sendCheckCode。
画面 9: 展示了 UserService.java 中的 checkVerificationCode 方法，通过 token 查询用户并校验 Redis 中的验证码。
画面 10: 展示了手机端 App 的界面，用于演示验证码功能。
画面 11: 展示了 Advanced REST Client 中发送 POST 请求，请求体为 {"phone": "18621359863", "verificationCode": "123456"}。
画面 12: 展示了 UserService.java 中的 checkVerificationCode 方法，校验成功后删除 Redis 中的验证码。
画面 13: 展示了 UsersController.java 中的 checkVerificationCode 方法，返回包含 verification 字段的响应。
画面 14: 展示了 Typora 编辑器中的 day11 说明文档，内容为 UserService.java 中 checkVerificationCode 方法的注释和代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
@PostMapping("phone/sendVerificationCode")
public ResponseEntity<Void> sendVerificationCode(@RequestHeader("Authorization") String token){
    try {
        Boolean bool = this.usersService.sendVerificationCode(token);
        if(bool){
            return ResponseEntity.ok(null);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 3:
```java
public ResponseEntityMap<String, Object> checkVerificationCode(@RequestBody Map<String, String> param, @RequestHeader("Authorization") String token) {
```

画面 4:
```java
String param.get("verificationCode");
```

画面 5:
```java
result.put("verification", bool);
```

画面 6:
```java
public ResponseEntityMap<String, Object> checkVerificationCode(@RequestBody Map<String, String> param, @RequestHeader("Authorization") String token) {
    try {
        String code = param.get("verificationCode");
        Boolean bool = this.usersService.checkVerificationCode(code, token);
        Map<String, Object> result = new HashMap<>();
        result.put("verification", bool);
        return ResponseEntity.ok(result);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 7:
```java
private RedisTemplate<String, String> redisTemplate;

public Map<String, Object> sendCheckCode(String mobile) {
    Map<String, Object> result = new HashMap<>(initialCapacity: 2);
    try {
        String redisKey = "CHECK_CODE" + mobile;
        String value = this.redisTemplate.opsForValue().get(redisKey);
        if (StringUtils.isNotBlank(value)) {
            result.put("msg", "上一次发送的验证码还未失效");
            return result;
        }
        // 发送短信验证码
        String code = "123456";
        if (null == code) {
            result.put("msg", "发送短信验证码失败");
        }
        result.put("code", 2);
        return result;
    } catch (Exception e) {
        e.printStackTrace();
    }
    return result;
}
```

画面 8:
```java
@Autowired
private SmsService smsService;
@Autowired
private UserService userService;
@Autowired
private RedisTemplate<String, String> redisTemplate;

public Boolean sendVerificationCode(String token) {
    User user = this.userService.queryUserByToken(token);
    if (null == user) {
        return false;
    }
    String mobile = user.getMobile();
    Map<String, Object> result = this.smsService.sendCheckCode(mobile);
    return ((Integer) result.get("code")).intValue() == 3;
}

public Boolean checkVerificationCode(String code, String token) {
```

画面 9:
```java
String redisKey = SmsService.REDIS_KEY_PREFIX + user.getMobile();
String value = this.redisTemplate.opsForValue().get(redisKey);
if (StringUtils.equals(value, code)) {
    // 验证码正确
    this.redisTemplate.delete(redisKey);
    return true;
}
return false;
```

画面 11:
```json
{
  "phone": "18621359863",
  "verificationCode": "123456"
}
```

画面 12:
```java
if (StringUtils.equals(value, code)) {
    // 验证码正确
    this.redisTemplate.delete(redisKey);
    return true;
}
return false;
```

画面 13:
```java
public ResponseEntityMap<String, Object> checkVerificationCode(@RequestBody Map<String, String> param, @RequestHeader("Authorization") String token) {
    try {
        String code = param.get("verificationCode");
        Boolean bool = this.usersService.checkVerificationCode(code, token);
        Map<String, Object> result = new HashMap<>();
        result.put("verification", bool);
        return ResponseEntity.ok(result);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 14:
```java
public Boolean checkVerificationCode(String code, String token) {
    // 查询用户的手机号
    User user = this.userService.queryUserByToken(token);
    if (null == user) {
        return false;
    }
    String redisKey = SmsService.REDIS_KEY_PREFIX + user.getMobile();
    String value = this.redisTemplate.opsForValue().get(redisKey);
    if (StringUtils.equals(value, code)) {
        // 验证码正确
        this.redisTemplate.delete(redisKey);
        return true;
    }
    return false;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
