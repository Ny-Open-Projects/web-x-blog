# 画面线理解：21_接口安全_登录验证控制层编写及测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\21_接口安全_登录验证控制层编写及测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:13, 00:45, 01:17, 01:22, 01:33, 01:57, 02:13, 02:19, 02:35, 02:44, 02:55, 03:23, 03:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:59:51

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的登录系统，从控制器层调用服务层，完成用户登录验证、密码校验、MD5 加密和 Token 生成的完整流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示 IntelliJ IDEA 中的项目结构，当前选中 `com.heima.login` 包下的 `MD5Util.java`。
- 代码内容：MD5 加密工具类，将字节数组转换为十六进制字符串。
  ```java
  byte mdBytes = md.digest();
  String hash = "";
  for (int i = 0; i < mdBytes.length; i++) {
      int temp;
      if (mdBytes[i] < 0) {
          temp = 256 + mdBytes[i];
      } else {
          temp = mdBytes[i];
      }
      if (temp < 16) {
          hash += "0";
      }
      hash += Integer.toHexString(temp & 0xf);
  }
  return hash;
  ```

画面 2：
- 与画面 1 几乎相同，只是鼠标光标位置不同，仍聚焦在 MD5Util.java 的代码上。

画面 3：
- 显示 `LoginV2Controller.java` 文件，展示登录接口的定义。
- 代码内容：
  ```java
  @RestController
  @RequestMapping("/api/v2/login")
  public class LoginV2Controller implements LoginController {
      @Autowired
      private ApUserLoginService apUserLoginService;
  }
  ```

画面 4：
- 显示 WebStorm 中的前端项目配置文件，主要为 `config.js`。
- 代码内容：
  ```javascript
  forward_behavior: {url: '/api/v1/behavior/forward_behavior', sv: 'behavior'},
  like_behavior: {url: '/api/v1/behavior/like_behavior', sv: 'behavior'},
  share_behavior: {url: '/api/v1/behavior/share_behavior', sv: 'behavior'},
  unlike_behavior: {url: '/api/v1/behavior/unlike_behavior', sv: 'behavior'},
  collection_behavior: {url: '/api/v1/behavior/collection_behavior', sv: 'behavior'},
  user_follow: {url: '/api/v2/login/user_follow', sv: 'user'},
  user_login: {url: '/api/v2/login/login_auth', sv: 'login'},
  // 解决跨域地址的前缀
  let sv = url;
  if (config.local) {
      return sv;
  } else {
      return config.prefix.server_85 + '/config/services[' + sv + ']';
  }
  ```

画面 5：
- 显示 `LoginV2Controller.java` 中的 `@PostMapping("/login_auth")` 方法。
- 代码内容：
  ```java
  @PostMapping("/login_auth")
  public ResponseResult login(@RequestBody ApUser user) {
      return apUserLoginService.loginAuth(user);
  }
  ```

画面 6：
- 显示一个 Web 页面，内容为“黑马头条”应用的预览界面，包含一个手机界面图和一个二维码。

画面 7：
- 显示 Web 页面，内容为“黑马头条”应用的登录界面，包含用户名和密码输入框。

画面 8：
- 显示 `LoginV2Controller.java` 中的 `login` 方法，鼠标光标在 `apUserLoginService.loginAuth(user)` 调用处。
- 代码内容：
  ```java
  return apUserLoginService.loginAuth(user);
  ```

画面 9：
- 显示 `ApUserLoginServiceImpl.java` 文件，展示 `loginAuth` 方法的实现。
- 代码内容：
  ```java
  public ResponseResult loginAuth(ApUser user) {
      // 验证参数
      if (StringUtils.isEmpty(user.getPhone()) || StringUtils.isEmpty(user.getPassword())) {
          return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
      }
      // 查询用户
      ApUser dbUser = apUserMapper.selectByPhone(user.getPhone());
      if (dbUser == null) {
          return ResponseResult.errorResult(AppHttpCodeEnum.AP_USER_DATA_NOT_EXIST);
      }
  }
  ```

画面 10：
- 显示 `ApUserLoginServiceImpl.java` 文件，展示 `loginAuth` 方法中查询到的用户对象 `dbUser`。
- 代码内容：
  ```java
  // 查询到的用户对象
  dbUser = {
      id = 1,
      name = "zhangsan",
      password = "08986bcd462d1373c4e4e64f3267b74f5",
      phone = "13280915205",
      image = null,
      sex = false,
      isCertification = false,
      isAuthentication = false,
      flag = 1
  }
  ```

画面 11：
- 显示 `ApUserLoginServiceImpl.java` 文件，展示 `loginAuth` 方法中调用 `validateService.validateMD5` 进行密码校验。
- 代码内容：
  ```java
  boolean isValid = validateService.validateMD5(user.getPassword(), dbUser);
  if (!isValid) {
      return ResponseResult.errorResult(AppHttpCodeEnum.LOGIN_PASSWORD_ERROR);
  }
  ```

画面 12：
- 显示 `ApUserLoginServiceImpl.java` 文件，展示 `loginAuth` 方法中调用 `validateService.validateMD5` 进行密码校验。
- 代码内容：
  ```java
  boolean isValid = validateService.validateMD5(user.getPassword(), dbUser);
  if (!isValid) {
      return ResponseResult.errorResult(AppHttpCodeEnum.LOGIN_PASSWORD_ERROR);
  }
  ```

画面 13：
- 显示 `ApUserLoginServiceImpl.java` 文件，展示 `loginAuth` 方法中调用 `validateService.validateMD5` 进行密码校验。
- 代码内容：
  ```java
  boolean isValid = validateService.validateMD5(user.getPassword(), dbUser);
  if (!isValid) {
      return ResponseResult.errorResult(AppHttpCodeEnum.LOGIN_PASSWORD_ERROR);
  }
  ```

画面 14：
- 显示 `ApUserLoginServiceImpl.java` 文件，展示 `loginAuth` 方法中成功校验后生成 Token 并返回。
- 代码内容：
  ```java
  user.setPassword("");
  Map<String, Object> map = new HashMap<>();
  map.put("token", ApJwtUtil.getToken(user));
  map.put("user", user);
  return ResponseResult.okResult(map);
  ```
