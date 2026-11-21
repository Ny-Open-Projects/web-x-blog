# 画面线理解：21-刷脸登录：测试以及总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\21-刷脸登录：测试以及总结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:17, 00:57, 01:12, 01:32, 01:58, 02:19, 02:46, 03:04, 03:48, 04:20, 04:37, 04:50, 05:00, 05:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:08:13

1) 这一组画面整体在讲什么（一句话）：
演示一个基于人脸识别的登录系统，从后端 Java 代码实现到前端 Vue.js 交互，再到用户实际登录流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 iHRM 系统登录页，弹出一个二维码用于人脸识别登录。
画面2：IDEA 编辑器中显示 `FaceLoginController.java` 代码，包含 `loginByFace` 和 `checkFace` 两个 POST 接口，用于处理人脸识别登录请求。
画面3：IDEA 编辑器中显示 `FaceLoginService.java` 代码，包含 `getQRCode` 方法，用于生成二维码。
画面4：IDEA 编辑器中显示 `FaceLoginService.java` 代码，`getQRCode` 方法中 `System.out.println(content);` 用于打印二维码内容。
画面5：IDEA 控制台输出日志，显示 Spring Boot 启动成功，并打印出生成的二维码 URL：`https://localhost:8080/#/faceLogin?code=1077112622496722944`。
画面6：浏览器开发者工具 Network 标签页，显示了与二维码相关的请求。
画面7：浏览器开发者工具 Network 标签页，显示了请求的响应内容：`{"success":true,"code":10000,"message":"操作成功"}`。
画面8：浏览器开发者工具 Network 标签页，显示了请求的响应内容：`{"success":true,"code":10000,"message":"操作成功"}`。
画面9：浏览器地址栏输入二维码 URL，页面显示“验证成功”。
画面10：登录成功后，进入 iHRM 系统的员工管理首页，显示工作日历和快捷导航。
画面11：点击“首页”按钮，页面跳转到系统首页。
画面12：VS Code 编辑器中显示 `login.vue` 文件，包含 `validateUsername` 和 `validatePassword` 函数，用于前端表单校验。
画面13：VS Code 编辑器中显示 `faceLogin.vue` 文件，包含 `getUserMedia` 方法，用于获取用户摄像头视频流。
画面14：PDF 文档页面，显示“第11章 项目总结”内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
@RequestMapping(value = "/{code}", method = RequestMethod.POST)
public Result loginByFace(@PathVariable(name = "code") String code, @RequestParam(name = "file") MultipartFile attachment) {
    String userId = faceLoginService.loginByFace(code, attachment);
    if (userId != null) {
        return new Result(ResultCode.SUCCESS);
    } else {
        return new Result(ResultCode.FAIL);
    }
}

// 图像检测，判断图片中是否含人脸图像
@RequestMapping(value = "/checkFace", method = RequestMethod.POST)
public Result checkFace(@RequestParam(name = "file") MultipartFile attachment) throws Exception {
    String image = Base64Util.encode(attachment.getBytes());
    Boolean aBoolean = baiduAiUtil.faceCheck(image);
    if (aBoolean) {
        return new Result(ResultCode.SUCCESS);
    } else {
        return new Result(ResultCode.FAIL);
    }
}
```

画面3：
```java
private QRCodeUtil qrCodeUtil;
private BaiduAiUtil baiduAiUtil;
private RedisTemplate redisTemplate;

// 生成二维码
public QRCode getQRCode() throws Exception {
    // 1.生成唯一码
    String code = idWorker.nextId() + "";
    // 2.生成二维码
    String content = url + "code=" + code;
    System.out.println(content);
}
```

画面5：
```
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAYAAADc5171AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAABCSURBVHgA7ZUxDoAgEAXQv9f/268Q8gQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QXQ8QX
