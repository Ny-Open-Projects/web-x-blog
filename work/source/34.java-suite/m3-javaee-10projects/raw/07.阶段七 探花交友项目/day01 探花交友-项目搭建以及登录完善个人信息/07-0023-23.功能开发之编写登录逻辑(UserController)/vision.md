# 画面线理解：23.功能开发之编写登录逻辑（UserController）

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\23.功能开发之编写登录逻辑（UserController）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:54, 02:05, 03:01, 03:23, 04:11, 04:59, 05:47, 06:13, 06:49, 07:21, 08:05, 09:29, 10:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:13:17

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的用户登录验证系统，包含控制器、服务层、Redis 令牌生成、JWT 令牌生成及前端调用测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示 UserController.java 文件，其中定义了 @PostMapping("/loginVerification") 方法，接收手机号和验证码，调用 userService.login 方法。
- 代码片段：
  ```java
  @RequestMapping("user")
  @RestController
  public class UserController {
      @Autowired
      private UserService userService;
      @PostMapping("loginVerification")
      public ResponseEntity<Object> login(@RequestBody Map<String,String> param) {
          String mobile = param.get("phone");
          String code = param.get("verificationCode");
          String token = this.userService.login(mobile, code);
      }
  ```

画面 2：
- 在 UserController.java 中，添加了对 token 的判断逻辑，如果 token 不为空，则进行字符串分割。
- 代码片段：
  ```java
  if(StringUtils.isNotEmpty(token)) {
      String[] ss = StringUtils.split(token, separatorChar: '|');
  ```

画面 3：
- 在 UserController.java 中，尝试将 token 分割后的字符串数组赋值给 tokenStr，但编译器提示类型不匹配。
- 代码片段：
  ```java
  String tokenStr = ss[1];
  return ResponseEntity.ok();
  ```
- 编译错误提示：
  ```
  Incompatible types.
  Required: org.springframework.http.ResponseEntity
  Found: org.springframework.http.ResponseEntity.BodyBuilder
  ```

画面 4：
- 展示 SmsController.java 文件，其中定义了 @PostMapping("/login") 方法，用于发送验证码。
- 代码片段：
  ```java
  @PostMapping("login")
  public ResponseEntity<Object> sendCheckCode(@RequestBody Map<String,Object> param) {
      String phone = String.valueOf(param.get("erCode"));
      String code = this.smsService.sendCheckCode(phone);
      int code = ((Integer)(sendCheckCode.get("code"))).intValue();
      if (code == 3) {
          return ResponseEntity.ok(null);
      } else if (code != 1) {
          String msg = sendCheckCode.get("msg").toString();
          builder.errCode("000001").errMessage(msg);
      }
      return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(null);
  ```

画面 5：
- 在 UserController.java 中，完善了登录成功后的返回逻辑，将 token 信息封装进 Map 并返回。
- 代码片段：
  ```java
  if(StringUtils.isNotEmpty(token)) {
      String[] ss = StringUtils.split(token, separatorChar: '|');
      Boolean isNew = Boolean.valueOf(ss[0]);
      Map<String, Object> result = new HashMap<>();
      result.put("isNew", isNew);
      result.put("tokenStr", ss[1]);
      return ResponseEntity.ok(result);
  } catch (Exception e) {
      e.printStackTrace();
      ErrorResult.ErrorResultBuilder builder = ErrorResult.builder().errCode("000001").errMessage("登录失败");
      return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(builder.build());
  }
  ```

画面 6：
- 展示 MyApplication.java 文件，其中包含 Spring Boot 的主类，用于启动应用。
- 代码片段：
  ```java
  package com.tanhua.sso;
  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;
  import org.springframework.context.annotation.ComponentScan;
  @ComponentScan("com.tanhua.sso.mapper") // 设置 mapper 接口的扫描包
  @SpringBootApplication
  public class MyApplication {
      public static void main(String[] args) {
          SpringApplication.run(MyApplication.class, args);
      }
  }
  ```

画面 7：
- 展示 UserService.java 文件，其中定义了 login 方法，用于处理登录逻辑。
- 代码片段：
  ```java
  public String login(String mobile, String code) {
      // 仅验证是否登录成功
      String redisKey = "CHECK_CODE" + mobile;
      String value = this.redisTemplate.opsForValue().get(redisKey);
      if (StringUtils.isEmpty(value)) {
          return null;
      }
  ```

画面 8：
- 在 UserController.java 中，调试器断点位于 login 方法的参数获取处。
- 代码片段：
  ```java
  String mobile = param.get("phone");
  String code = param.get("verificationCode");
  String token = this.userService.login(mobile, code);
  ```

画面 9：
- 在 UserService.java 中，调试器断点位于用户信息设置处。
- 代码片段：
  ```java
  user = new User();
  user.setMobile(mobile);
  user.setPassword(DigestUtils.md5Hex(data: "123456"));
  this.userMapper.insert(user);
  ```

画面 10：
- 在 UserService.java 中，调试器断点位于生成 JWT 令牌处。
- 代码片段：
  ```java
  String token = JwtUtils.builder()
      .subject("user")
      .claim("mobile", mobile)
      .claim("isNew", isNew)
      .expiresIn(Duration.ofMinutes(30))
      .build().signWith(SignatureAlgorithm.HS256, secret).compact();
  ```

画面 11：
- 在 UserController.java 中，调试器断点位于 login 方法的参数获取处。
- 代码片段：
  ```java
  String mobile = param.get("phone");
  String code = param.get("verificationCode");
  String token = this.userService.login(mobile, code);
  ```

画面 12：
- 展示 Advanced REST Client 发送 POST 请求到 /user/loginVerification 接口，请求体为 {"phone": "17602189189", "verificationCode": "113421"}。
- 响应状态码为 200，响应体为 {"token": "eyJhbGciOiJIUzI1NiJ9.eyJ..."}。

画面 13：
- 展示 Advanced REST Client 发送 POST 请求到 /user/loginVerification 接口，请求体为 {"phone": "17602189189", "verificationCode": "113421"}。
- 响应状态码为 200，响应体为 {"token": "eyJhbGciOiJIUzI1NiJ9.eyJ..."}。

画面 14：
- 展示 Typora 编辑器中的 day01 项目搭建及登录的个人笔记，其中包含 UserService 类的代码片段。
- 代码片段：
  ```java
  @Service
  public class UserService {
      @Autowired
      private UserMapper userMapper;
      @Autowired
      private RedisTemplate<String, String> redisTemplate;
      private static final ObjectMapper MAPPER = new ObjectMapper();
      @Autowired
      private RocketMQTemplate rocketMQTemplate;
      @Value("${jwt.secret}")
      private String secret;
  }
  ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
见上文第 2 点。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 或架构图/流程图。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
