# 21_接口安全_登录验证控制层编写及测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\21_接口安全_登录验证控制层编写及测试【海量资源尽在 666java.com】.mp4
- 时长 3分43秒（音频 223s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们还有最后一块内容咱们要去说一说就是当前login的Controller咱们要去编写一下这个就是在当前的v1的基础上咱们再去添加一个v2是吧在这去new一个包叫Controller加v这个类其实跟这个类是类似的咱们直接考一下考到这之后咱们可以把它改个名叫v2本的这种Controller然后这里边路径你可能来改是v2
[00:30] 好吧前头还是实现他还是这个Service没错然后呢这个是方法不一样这是v那这改完之后呢完了他们可以启动一下这项目啊测一下打个年啊然后呢这个前台的项目啊你要去改当前的config.js中的什么登录验证这个呢这个不是v1了是谁啊v2那这时候呢改完之后啊完之后呢你现在就去冲击一下吧冲击一下啊
[01:01] 充其完之后这时候后台也充其了看一看看看有没有重启成功这个的关了因为我这前面是有一个的刷新稍等吧等到启动完之后这个就能去加载了后台启动也启动完了没有报错这时候咱们可以在这打断点已经打了我们也可以在后台在Service中也打断点我们一步一步去走一遍就能看出来当前加密的过程好这个前台已经登录完了
[01:38] 我输入的是一个手机号跟一个密码这个手机号和密码是谁呢跟我的数据库是对应上的我用的是这一条数据去测的首先我这个密码是用MD5进行加密之后放到这的它是一个test它是一个test然后这个是一个手机号这个手机号就跟我前面的手机号是一样的好吧我这边输的输的就是一个test咱们可以看一下点登录你就能看到当前的手机号是它
[02:07] 密码是他好吧好我点确定啊这时候断点就来了看到了吧他进的是v2啊好那咱们呢直接直接放行放行完之后呢先验证参数这这些肯定都没事啊咱们这次呢就就去从数据库中去查查谁呢查当前用户看看能不能查出来查查出来了是吧看看这个用户看这个用户啊用户的信息张三啊这是啊这个不用看啊这是张三
[02:35] 手机上是他密码是这个OK咱们主要看密码因为咱们验证的就是密码是吧好用户查出来了那肯定是这一步肯定没事啊往下走那这时候呢需要去验证用户这时候你看啊user里边传过来的是一个test但是你这里边是啥呢是一个这种加密户的密文那你进到这里边啊他就会干嘛呢不会当前这个什么前这个什么数据过程查出来的密文去比对谁呀
[03:04] 去比对当前你传过来这个但是你比对没法比对这时候你就要先去加密加密之后比对这时候他一样的话就返回处怎么可以在这打这点好执行过来然后往下走呗你看他这时候就有一天出了看到了吧我看在这咱们可以在这打点让他过来好过来了这时候就是出那如果出的话他就会走下面一个逻辑然后把用户给返回了看到了吧
[03:32] OK那这样的话逻辑就算是做完了那行那咱们当前的这种接口安全登录验证这块那关于密码的验证咱们就说完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

