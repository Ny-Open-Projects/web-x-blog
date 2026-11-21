# 27.检查登录状态的功能实现

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\27.检查登录状态的功能实现_【海量资源尽在 666java.com】.mp4
- 时长 1分45秒（音频 105s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来实现我们最后一个功能啊就是检查用户的一个登录状态那么就根据这个token呢来做一个查询那么这个Service的方法其实我们刚刚是不是已经就写过了啊那么下面我们只需要去来实现这个Controller就可以了那我们在Controller中就是这个usercontroller中去增加一个方法就ok那么我们就加到下面来吧才知道这个就是把这个user给它导入进来
[00:30] 那么这样的话就搞定了非常简单然后呢我们重新启动一下服务然后呢我们来做个测试好那么现在呢我们就跑起来了那我们来测试一下那么后面我们其实去跟一个我们这个参数就好了那么在前面这个位置测试吧那么我们去Ure把这个拿掉是一个get请求那么我们就把刚刚我们所拿到的这个token那么我们去做一下这个传递
[01:00] 然后呢来看一下啊在这好然后呢把这个改成一个get请求其他就投信息就不需要了然后呢我们走哎好那么其实可以看到结果是不我们已经就拿到我们这个所期望的数据了那么如果我们后面这个随便写个东西啊走会发现什么是不是就是那啊什么都没有啊呃那么呃可以根据我们的这个返回值有没有数据来判断我们的这个用户有没有
[01:31] 状态是不是还是有效的状态好那么这样的话我们是不是就已经实现了这样的一个效果了OK好那么关于检查登录状态的一个接口的实现那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

