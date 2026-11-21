# 画面线理解：14-刷脸登录：搭建环境-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\14-刷脸登录：搭建环境-下_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:32, 01:06, 01:39, 02:19, 03:32, 04:14, 04:48, 05:08, 05:18, 05:30, 05:43, 05:52, 06:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:02:29

1) 这一组画面整体在讲什么（一句话）：
实现基于人脸识别的登录功能，包括前端二维码生成、后端接口处理、服务层逻辑和配置文件设置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 显示IntelliJ IDEA项目结构，当前选中`ihm_system`模块。
- `application.yml`配置文件内容：
  ```yaml
  driver-class-name: com.mysql.jdbc.Driver
  url: jdbc:mysql://localhost:3306/ihm?useUnicode=true&characterEncoding=utf8
  username: root
  password: 111111
  jpa:
    database: MySQL
    show-sql: true
    open-in-view: true
  redis:
    host: 127.0.0.1
    port: 6379
  jwt:
    config:
      key: ads_ihrm
      ttl: 36000000
      appId: 1191935
      apiKey: cyKHSgas93VtDmt42N0bK8pu
      secretKey: yfGueNvL.Bd0nybFLubhlyod9EDEZW
      imageType: BASE64
      groupId: itcast
      url: https://localhost:8080/#/faceLogin
  ```

画面2：
- 显示`FaceLoginController.java`文件内容，包含三个方法：
  ```java
  @RequestMapping(value = "/qrcode", method = RequestMethod.GET)
  public Result qrcode() throws Exception {
      return null;
  }

  @RequestMapping(value = "/qrcode/{code}", method = RequestMethod.GET)
  public Result qrcodeCack(@PathVariable(name = "code") String code) throws Exception {
      return null;
  }

  @RequestMapping(value = "/checkFace", method = RequestMethod.POST)
  public Result checkFace(@RequestParam(name = "file") MultipartFile attachment) throws Exception {
      return null;
  }
  ```

画面3：
- 显示`FaceLoginController.java`文件内容，方法注释说明了功能。
- `@RequestMapping(value = "/sys/faceLogin")`注解。

画面4：
- 显示`FaceLoginController.java`文件内容，方法注释说明了功能。
- `@RequestMapping(value = "/qrcode", method = RequestMethod.GET)`注解。

画面5：
- 显示`FaceLoginResult.java`类定义，包含状态码、token和用户ID字段。
- `private String userId;`字段被高亮。

画面6：
- 显示`FaceLoginController.java`文件内容，方法注释说明了功能。
- `@RequestMapping(value = "/checkFace", method = RequestMethod.POST)`注解。

画面7：
- 显示PPT页面，标题为“人脸识别登录页面”。
- 页面包含多个窗口截图，显示了二维码、登录页面、代码编辑器等。
- 文本内容：
  ```
  code=1234
  url地址 = http://xxx?code=1234
  登录成功次数：1（存在用户-10001）
  登录失败次数：0
  ```

画面8：
- 显示IntelliJ IDEA项目结构，当前选中`ihm_system`模块。
- `FaceLoginController.java`文件内容，方法注释说明了功能。

画面9：
- 显示IntelliJ IDEA项目结构，当前选中`ihm_system`模块。
- 弹出“Copy”对话框，提示复制文件到`C:\Users\ThinkPad\...\day11\代码\service\FaceLoginService.java`。

画面10：
- 显示`FaceLoginService.java`文件内容，包含`@Service`注解。
- 弹出“Import class”菜单，提示创建类或接口。

画面11：
- 显示IntelliJ IDEA项目结构，当前选中`ihm_system`模块。
- `FaceLoginController.java`文件内容，方法注释说明了功能。

画面12：
- 显示IntelliJ IDEA项目结构，当前选中`ihm_system`模块。
- `FaceLoginController.java`文件内容，方法注释说明了功能。

画面13：
- 显示IntelliJ IDEA项目结构，当前选中`ihm_system`模块。
- `FaceLoginController.java`文件内容，方法注释说明了功能。

画面14：
- 显示`FaceLoginService.java`文件内容，包含`@Service`注解。
- `@Value("${qr.url}")`注解。
- `private String url;`字段。
- `public QRCode getQRCode() throws Exception { return null; }`方法。
- `public String loginByFace(String code, MultipartFile attachment) throws Exception { return null; }`方法。
- `private String getCacheyKey(String code) { return "qrcode_" + code; }`方法。
