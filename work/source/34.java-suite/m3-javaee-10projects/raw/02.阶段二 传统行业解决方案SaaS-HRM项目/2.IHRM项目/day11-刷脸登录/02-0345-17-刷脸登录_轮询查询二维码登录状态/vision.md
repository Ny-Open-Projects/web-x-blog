# 画面线理解：17-刷脸登录：轮询查询二维码登录状态

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\17-刷脸登录：轮询查询二维码登录状态_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:22, 01:09, 01:46, 02:11, 02:25, 02:51, 03:20, 03:40, 04:47, 05:13, 05:53, 06:44, 07:11, 07:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:04:48

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot、Shiro 和 Redis 的人脸识别登录系统的核心代码实现与接口测试流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- IDE 中展示 `ShiroConfiguration.java` 文件，其中定义了 Shiro 的过滤器工厂。
- 代码片段：
  ```java
  public ShiroFilterFactoryBean shiroFilter(SecurityManager securityManager) {
      //1.创建过滤器工厂
      ShiroFilterFactoryBean filterFactory = new ShiroFilterFactoryBean();
      //2.设置安全管理器
      filterFactory.setSecurityManager(securityManager);
      //3.设置登录url
      filterFactory.setLoginUrl("/autherror/code-1");//跳转url地址
      filterFactory.setUnauthorizedUrl("/autherror/code-0");//未能授权的url
      Map<String,String> filterMap = new LinkedHashMap<>();
      filterMap.put("/autherror","anon");
      filterMap.put("/sys/login","anon");
      filterMap.put("/auth","authc"); //认证之后访问（登录）
      filterMap.put("/sys","authc"); //认证之后访问（登录）
      filterFactory.setFilterChainDefinitionMap(filterMap);
  }
  ```

画面2：
- IDE 中展示 `FaceLoginService.java` 文件，其中包含生成二维码和校验二维码的逻辑。
- 代码片段：
  ```java
  public QRCode getQRCode() throws Exception {
      //1.创建唯一标识
      String code = IdWorker.nextId() + "";
      //2.生成二维码
      String content = url + "?code=" + code;
      String file = qRCodeUtil.createQRCode(content);
      //3.存入当前二维码
      FaceLoginResult result = new FaceLoginResult(state: "1");
      redisTemplate.boundValueOps(getCacheKey(code)).set(result, 10, TimeUnit.MINUTES);//状态对象，失效时间，单位
      return new QRCode(code,file);
  }
  ```

画面3：
- IDE 中展示 `FaceLoginService.java` 文件，继续展示 `checkQRCode` 方法。
- 代码片段：
  ```java
  public FaceLoginResult checkQRCode(String code) {
      return null;
  }
  ```

画面4：
- IDE 中展示 `SystemApplication.java` 文件，其中包含 Spring Boot 的启动类和相关配置。
- 代码片段：
  ```java
  @SpringBootApplication(scanBasePackages = "com.ihrm")
  @EntityScan(value="com.ihrm.domain.system")
  @EnableEurekaClient
  @EnableDiscoveryClient
  @EnableFeignClients
  public class SystemApplication {
      public static void main(String[] args) { SpringApplication.run(SystemApplication.class, args); }
      @Bean
      public IdWorker idWorker() { return new IdWorker(); }
      @Bean
      public JwtUtils jwtUtils() { return new JwtUtils(); }
      @Bean
      public OpenEntityManagerInViewFilter openEntityManagerInViewFilter() { return new OpenEntityManagerInViewFilter(); }
  }
  ```

画面5：
- IDE 中展示 `SystemApplication.java` 文件，鼠标光标位于 `openEntityManagerInViewFilter` 方法上。
- 代码片段：
  ```java
  public OpenEntityManagerInViewFilter openEntityManagerInViewFilter() { return new OpenEntityManagerInViewFilter(); }
  ```

画面6：
- Postman 界面，准备发送一个 GET 请求到 `localhost:8002`。
- 请求 URL：`GET localhost:8002`

画面7：
- IDE 中展示 `FaceLoginController.java` 文件，其中包含 `@RestController` 注解的类和 `@RequestMapping` 注解的方法。
- 代码片段：
  ```java
  @RestController
  public class FaceLoginController {
      @Autowired
      private FaceLoginService faceLoginService;
      @RequestMapping(value = "/qrcode", method = RequestMethod.GET)
      public Result qrcode() throws Exception {
          QRCode qrCode = faceLoginService.getQRCode();
          return new Result(ResultCode.SUCCESS,qrCode);
      }
  }
  ```

画面8：
- 浏览器界面，显示一个二维码图片。
- 二维码内容：`data:image/png;base64,VRORw0K...`

画面9：
- IDE 中展示 `FaceLoginController.java` 文件，其中包含 `@RequestMapping` 注解的方法。
- 代码片段：
  ```java
  @RequestMapping(value = "/qrcode/{code}", method = RequestMethod.GET)
  public Result qrcodeCheck(@PathVariable("code") String code) throws Exception {
      return null;
  }
  ```

画面10：
- IDE 中展示 `FaceLoginController.java` 文件，鼠标光标位于 `qrcodeCheck` 方法上。
- 代码片段：
  ```java
  public Result qrcodeCheck(@PathVariable("code") String code) throws Exception {
      return null;
  }
  ```

画面11：
- IDE 中展示 `FaceLoginService.java` 文件，其中包含 `checkQRCode` 方法。
- 代码片段：
  ```java
  public FaceLoginResult checkQRCode(String code) {
      return null;
  }
  ```

画面12：
- IDE 中展示 `FaceLoginService.java` 文件，其中包含 `loginByFace` 方法。
- 代码片段：
  ```java
  public String loginByFace(String code, MultipartFile attachment) throws Exception {
      return null;
  }
  ```

画面13：
- IDE 中展示 `FaceLoginController.java` 文件，其中包含 `@RequestMapping` 注解的方法。
- 代码片段：
  ```java
  @RequestMapping(value = "/qrcode", method = RequestMethod.GET)
  public Result qrcode() throws Exception {
      QRCode qrCode = faceLoginService.getQRCode();
      return new Result(ResultCode.SUCCESS,qrCode);
  }
  ```

画面14：
- Postman 界面，准备发送一个 GET 请求到 `localhost:8002/sysFaceLogin/qrcode/1077083504325447880`。
- 请求 URL：`GET localhost:8002/sysFaceLogin/qrcode/1077083504325447880`
