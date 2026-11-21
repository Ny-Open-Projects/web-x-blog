# 画面线理解：27.检查登录状态的功能实现

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\27.检查登录状态的功能实现_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:09, 00:14, 00:21, 00:24, 00:39, 00:47, 00:55, 01:03, 01:10, 01:19, 01:34, 01:37, 01:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:16:14

1) 这一组画面整体在讲如何通过 token 查询用户信息，涉及 UserService 和 UserController 的代码实现及测试。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Typora 文档中 UserService 的 queryUserByToken 方法，用于根据 token 查询用户信息，代码中包含 Redis 操作和异常处理。
画面2：展示 UserController 中的 queryUserByToken 方法，使用 @PathVariable 注解接收 token 参数。
画面3：与画面1相同，展示 UserService 代码。
画面4：展示 IntelliJ IDEA 中 UserInfoService.java 文件，包含人脸检测和图片上传逻辑。
画面5：展示 UserController 中的异常处理代码，使用 ErrorResult.builder() 构建错误响应。
画面6：展示 UserController 中的 queryUserByToken 方法，使用 @PathVariable 注解接收 token 参数。
画面7：展示 Advanced REST Client 中上传图片的请求，文件名为 headPhoto。
画面8：展示 Advanced REST Client 中的登录请求 URL。
画面9：展示 Advanced REST Client 中的用户信息请求，包含 Authorization 头和文件上传。
画面10：展示 Advanced REST Client 中的请求响应，状态码为 200。
画面11：展示 Advanced REST Client 中的请求响应，状态码为 200。
画面12：展示 Typora 文档中 UserController 的 queryUserByToken 方法。
画面13：展示 Typora 文档中测试部分的请求 URL。
画面14：展示 Typora 文档中 UserController 的 queryUserByToken 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public User queryUserByToken(String token) {
    try {
        String redisTokenKey = "TOKEN_" + token;
        String cacheData = this.redisTemplate.opsForValue().get(redisTokenKey);
        if (StringUtils.isEmpty(cacheData)) {
            return null;
        }
        // 刷新时间
        this.redisTemplate.expire(redisTokenKey, 1, TimeUnit.HOURS);
        return MAPPER.readValue(cacheData, User.class);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return null;
}
```

画面2：
```java
// 根据token查询用户数据
@GetMapping("({token})")
public User queryUserByToken(@PathVariable("token") String token) {
    return this.userService.queryUserByToken(token);
}
```

画面4：
```java
try {
    // 判断头像是是否为人脸
    boolean isPortrait = this.faceEngineService.checkIsPortrait(file);
    if (!isPortrait) {
        return false;
    }
} catch (Exception e) {
    LOGGER.error("检测人像图片出错！", e);
    return false;
}
// 图片上传到阿里云OSS
PicUploadResult uploadResult = this.picUploadService.upload(file);
UserInfo userInfo = new UserInfo();
userInfo.setLogo(uploadResult.getName());
```

画面5：
```java
ErrorResult.ErrorResultBuilder builder = ErrorResult.builder().errCode(500).errMsg("服务器内部错误");
return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(builder.build());
```

画面6：
```java
// 根据token查询用户数据
@GetMapping("({token})")
public User queryUserByToken(@PathVariable("token") String token) {
    return this.userService.queryUserByToken(token);
}
```

画面7：
```http
POST /user HTTP/1.1
Host: 172.16.55.153:18080
Content-Type: application/x-www-form-urlencoded
Authorization: ey.Jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1NtU8Jy.jh6GdOuU1
