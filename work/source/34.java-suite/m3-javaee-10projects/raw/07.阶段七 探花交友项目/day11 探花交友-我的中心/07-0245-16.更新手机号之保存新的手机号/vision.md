# 画面线理解：16.更新手机号之保存新的手机号

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\16.更新手机号之保存新的手机号_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:53, 01:40, 02:32, 03:20, 04:18, 05:40, 06:48, 07:30, 08:13, 08:46, 09:40, 10:23, 11:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:48:37

1) 这一组画面整体在讲什么（一句话）：
演示一个 Spring Boot 项目中，通过 REST API 验证用户手机验证码并更新手机号的完整流程，涉及前端请求、后端 Controller、Service 层逻辑及数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：使用 Advanced REST Client 发送 POST 请求，请求体为 JSON 格式，包含 phone 和 verificationCode 字段，请求成功返回状态码 200，响应体为 {"errorCode": "00000", "errorMessage": "验证成功"}。
画面 2：在 IntelliJ IDEA 中，展示 UsersController.java 文件中 checkVerificationCode 方法的代码，该方法接收 @RequestBody 和 @RequestHeader 参数。
画面 3：在 UsersController.java 文件中，展示 checkVerificationCode 方法的 try-catch 块，其中调用 userService.checkVerificationCode 方法。
画面 4：在 UsersController.java 文件中，展示 checkVerificationCode 方法的完整代码，包括 try 块和 catch 块，以及 @PostMapping 注解。
画面 5：在 UsersService.java 文件中，展示 queryUserByToken 方法的代码，其中包含对 User 对象的 equals 方法的调用。
画面 6：在 UsersService.java 文件中，展示 updateNewMobile 方法的代码，其中包含对 redisTemplate 的操作。
画面 7：在 UsersService.java 文件中，展示 queryUserByToken 方法的代码，其中包含对 redisTemplate.opsForValue().get 方法的调用。
画面 8：在 UsersService.java 文件中，展示 queryUserByToken 方法的代码，其中包含对 QueryWrapper 的使用。
画面 9：在 UsersService.java 文件中，展示 updateNewMobile 方法的代码，其中包含对 QueryWrapper 的使用。
画面 10：展示手机应用界面，用于演示用户操作。
画面 11：在 UsersController.java 文件中，展示 checkVerificationCode 方法的代码，其中包含对 userService.checkVerificationCode 方法的调用。
画面 12：在 Navicat Premium 中，展示 tb_user 表的数据，用于演示数据库操作。
画面 13：展示手机应用界面，用于演示用户操作。
画面 14：在 Typora 中，展示 day11 识文.md 文件的内容，其中包含 UsersController 和 UsersService 的代码片段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```json
{
  "phone": "18620320863",
  "verificationCode": "123456"
}
```

画面 2：
```java
@PutMapping("/checkVerificationCode")
public ResponseEntity<Map<String, Object>> checkVerificationCode(@RequestBody Map<String, String> param, @RequestHeader("Authorization") String token) {
```

画面 3：
```java
try {
    String code = param.get("verificationCode");
    this.userService.checkVerificationCode(code, token);
    Map<String, Object> result = new HashMap<>();
    result.put("verification", bool);
    return ResponseEntity.ok(result);
} catch (Exception e) {
    e.printStackTrace();
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 4：
```java
@PutMapping("/checkVerificationCode")
public ResponseEntity<Map<String, Object>> checkVerificationCode(@RequestBody Map<String, String> param, @RequestHeader("Authorization") String token) {
    try {
        String code = param.get("verificationCode");
        Boolean bool = this.userService.checkVerificationCode(code, token);
        Map<String, Object> result = new HashMap<>();
        result.put("verification", bool);
        return ResponseEntity.ok(result);
    } catch (Exception e) {
        e.printStackTrace();
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    }
}
```

画面 5：
```java
User user = this.userService.queryUserByToken(token);
if (null == user) {
    return false;
}
```

画面 6：
```java
String redisKey = SmsService.REDIS_KEY_PREFIX + user.getMobile();
String value = this.redisTemplate.opsForValue().get(redisKey);
if (StringUtils.equals(value, code)) {
    this.redisTemplate.delete(redisKey);
    return true;
}
return false;
```

画面 7：
```java
String redisTokenKey = "TOKEN" + token;
String cacheData = this.redisTemplate.opsForValue().get(redisTokenKey);
if (StringUtils.isEmpty(cacheData)) {
    return null;
}
```

画面 8：
```java
Query<User> query = this.userMapper.selectOne();
User user = new User();
user.setId(id);
user.setMobile(newPhone);
return this.userMapper.updateById(user) > 0;
```

画面 9：
```java
public Boolean updateNewMobile(Long id, String newPhone) {
    QueryWrapper<User> queryWrapper = new QueryWrapper<>();
    queryWrapper.eq("column", "mobile", newPhone);
    User oldUser = this.userMapper.selectOne(queryWrapper);
    if (null != oldUser) {
        return false;
    }
    User user = new User();
    user.setId(id);
    user.setMobile(newPhone);
    return this.userMapper.updateById(user) > 0;
}
```

画面 11：
```java
@PutMapping("/checkVerificationCode")
public ResponseEntity<Map<String, Object>> checkVerificationCode(@RequestBody Map<String, String> param, @RequestHeader("Authorization") String token) {
    try {
        String code = param.get("verificationCode");
        Boolean bool = this.userService.checkVerificationCode(code, token);
        Map<String, Object> result = new HashMap<>();
        result.put("verification", bool);
        return ResponseEntity.ok(result);
    } catch (Exception e) {
        e.printStackTrace();
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    }
}
```

画面 14：
```markdown
2.8.1 UsersController
2.8.2 UsersService
2.8.3 UsersController
2.8.4 UsersService
2.8.5 UsersController
2.8.6 UsersService
2.8.7 UsersController
2.8.8 UsersService
2.8.9 UsersController
2.8.10 UsersService
2.8.11 UsersController
2.8.12 UsersService
2.8.13 UsersController
2.8.14 UsersService
2.8.15 UsersController
2.8.16 UsersService
2.8.17 UsersController
2.8.18 UsersService
2.8.19 UsersController
2.8.20 UsersService
2.8.21 UsersController
2.8.22 UsersService
2.8.23 UsersController
2.8.24 UsersService
2.8.25 UsersController
2.8.26 UsersService
2.8.27 UsersController
2.8.28 UsersService
2.8.29 UsersController
2.8.30 UsersService
2.8.31 UsersController
2.8.32 UsersService
2.8.33 UsersController
2.8.34 UsersService
2.8.35 UsersController
2.8.36 UsersService
2.8.37 UsersController
2.8.38 UsersService
2.8.39 UsersController
2.8.40 UsersService
2.8.41 UsersController
2.8.42 UsersService
2.8.43 UsersController
2.8.44 UsersService
2.8.45 UsersController
2.8.46 UsersService
2.8.47 UsersController
2.8.48 UsersService
2.8.49 UsersController
2.8.50 UsersService
2.8.51 UsersController
2.8.52 UsersService
2.8.53 UsersController
2.8.54 UsersService
2.8.55 UsersController
2.8.56 UsersService
2.8.57 UsersController
2.8.58 UsersService
2.8.59 UsersController
2.8.60 UsersService
2.8.61 UsersController
2.8.62 UsersService
2.8.63 UsersController
2.8.64 UsersService
2.8.65 UsersController
2.8.66 UsersService
2.8.67 UsersController
2.8.68 UsersService
2.8.69 UsersController
2.8.70 UsersService
2.8.71 UsersController
2.8.72 UsersService
2.8.73 UsersController
2.8.74 UsersService
2.8.75 UsersController
2.8.76 UsersService
2.8.77 UsersController
2.8.78 UsersService
2.8.79 UsersController
2.8.80 UsersService
2.8.81 UsersController
2.8.82 UsersService
2.8.83 UsersController
2.8.84 UsersService
2.8.85 UsersController
2.8.86 UsersService
2.8.87 UsersController
2.8.88 UsersService
2.
