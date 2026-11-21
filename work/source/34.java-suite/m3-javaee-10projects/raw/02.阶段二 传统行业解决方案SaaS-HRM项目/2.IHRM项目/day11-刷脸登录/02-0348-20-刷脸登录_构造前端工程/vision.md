# 画面线理解：20-刷脸登录：构造前端工程

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\20-刷脸登录：构造前端工程_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:23, 00:48, 01:17, 01:41, 01:58, 03:21, 04:21, 05:02, 05:28, 06:01, 06:25, 06:53, 07:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:07:22

1) 这一组画面整体在讲什么（一句话）：
演示一个基于人脸识别的登录系统，包括后端 Java 控制器与服务层代码、前端 Vue 路由配置、以及通过 Postman 发起的 HTTP 请求和最终的登录界面。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示 IntelliJ IDEA 中 `FaceLoginController.java` 文件的代码，其中包含 `@RequestMapping(value = "/{code}", method = RequestMethod.POST)` 的 `loginByFace` 方法，用于处理人脸登录请求。
- 代码中调用 `faceLoginService.loginByFace(code, attachment)`。
- 控制台日志显示 Eureka 服务发现成功。

画面 2：
- 显示 `FaceLoginController.java` 文件的代码，包含 `qrcode()` 和 `qrcodeCheck()` 两个 GET 请求方法，用于生成和校验二维码。
- 代码中调用 `faceLoginService.getQRCode()` 和 `faceLoginService.checkQRCode(code)`。

画面 3：
- 显示 Postman 中一个 POST 请求的设置界面，目标地址为 `localhost:9002/sysfaceLogin/1077083504325447880`，请求类型为 `form-data`。
- 该请求用于上传人脸图片进行登录。

画面 4：
- 显示一个图片查看器，正在查看一张名为 `001.jpg` 的人脸图片（刘德华）。
- 该图片是用于人脸识别登录的测试素材。

画面 5：
- 显示 IntelliJ IDEA 中 `FaceLoginController.java` 文件的代码，与画面 1 类似，但此处的 `loginByFace` 方法在执行时抛出了 `NullPointerException`。
- 控制台日志显示异常堆栈，指出 `faceLoginService.loginByFace` 方法在第 76 行抛出 `NullPointerException`。

画面 6：
- 显示 IntelliJ IDEA 中 `FaceLoginService.java` 文件的代码，其中 `loginByFace` 方法调用 `faceLoginService.loginByFace`。
- 代码中使用 `Base64Util.encode` 对上传的图片进行编码。
- 代码中调用 `userDao.findById` 查询用户信息。
- 控制台日志显示 `NullPointerException` 异常，堆栈信息指向 `faceLoginService.loginByFace` 方法。

画面 7：
- 显示 Postman 中一个 GET 请求的设置界面，目标地址为 `localhost:9002/sysfaceLogin/qrcode/1077083504325447880`。
- 该请求用于获取二维码。

画面 8：
- 显示 IntelliJ IDEA 中 `FaceLoginService.java` 文件的代码，其中 `loginByFace` 方法中设置了用户登录状态。
- 代码中使用 `SecurityUtils.getSubject()` 获取当前用户。
- 代码中调用 `subject.login(new UsernamePasswordToken(...))` 进行登录。
- 代码中调用 `subject.getSession().getId()` 获取会话 ID。
- 代码中调用 `result.setToken(...)` 设置登录令牌。

画面 9：
- 显示 Notepad++ 中一个名为 `index.js` 的文件，内容为 Vue 路由配置。
- 代码中定义了 `const Whitelist = ['/login', '/reg', '/authdirect', '/facelogin']`。
- 代码中定义了 `router` 的 `constantRouterMap`，其中包含 `path: '/facelogin'` 的路由配置。

画面 10：
- 显示 Visual Studio Code 中 `index.js` 文件的代码，内容为 Vue 路由配置。
- 代码中定义了 `export const constantRouterMap`，其中包含 `path: '/facelogin'` 的路由配置。
- 代码中定义了 `path: '/reg'` 和 `path: '/authdirect'` 的路由配置。

画面 11：
- 显示 Visual Studio Code 中 `index.js` 文件的代码，内容为 Vue 路由配置。
- 代码中定义了 `export const constantRouterMap`，其中包含 `path: '/facelogin'` 的路由配置。
- 代码中定义了 `path: '/reg'` 和 `path: '/authdirect'` 的路由配置。
- 代码中定义了 `path: '/401'` 和 `path: '/404'` 的路由配置。

画面 12：
- 显示 Windows 资源管理器中 `module-dashboard` 目录下的 `pages` 文件夹。
- 文件夹内包含 `facelogin.vue` 和 `facelogin.js` 两个文件。

画面 13：
- 显示 Windows 资源管理器中 `api/base` 目录下的 `facelogin.js` 和 `facelogin.vue` 两个文件。
- 该目录是前端 Vue 项目中用于人脸识别登录的页面和逻辑文件。

画面 14：
- 显示浏览器中 iHRM 后台登录系统的登录页面。
- 页面包含一个二维码登录按钮和一个“刷脸登录”按钮。
- 页面显示了“还没有账号？立即注册”的提示。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
@RequestMapping(value = "/{code}", method = RequestMethod.POST)
public Result loginByFace(@PathVariable(name = "code") String code, @RequestParam(name = "file") MultipartFile attachment) throws Exception {
    String userId = faceLoginService.loginByFace(code, attachment);
    if(userId != null) {
        return new Result(ResultCode.SUCCESS);
    }else {
        return new Result(ResultCode.FAIL);
    }
}
```

画面 2：
```java
@RequestMapping(value = "/qrcode", method = RequestMethod.GET)
public Result qrcode() throws Exception {
    QRCode qrcode = faceLoginService.getQRCode();
    return new Result(ResultCode.SUCCESS);
}

@RequestMapping(value = "/{code}", method = RequestMethod.GET)
public Result qrcodeCheck(String code) throws Exception {
    FaceLoginResult checkQRCode = faceLoginService.checkQRCode(code);
    return new Result(ResultCode.SUCCESS, checkQRCode);
}
```

画面 3：
- 无代码，仅显示 Postman 请求设置。

画面 4：
- 无代码，仅显示图片查看器。

画面 5：
- 无代码，仅显示控制台日志。

画面 6：
```java
private UserDao userDao;

//扫描二维码后，使用白名单进行登录
//如果用户不存在，生成指定的用户id
//如果用户存在，返回用户id
public String loginByFace(String code, MultipartFile attachment) throws Exception {
    //1.使用百度云人脸搜索的用户
    String userId = Base64Util.faceSearch(Base64Util.encode(attachment.getBytes()));
    //2.获取用户信息
    FaceLoginResult result = new FaceLoginResult();
    if(userId == null) {
        //3.生成用户id
        User user = userDao.findById(userId).get();
        if(user == null) {
            //4.创建用户
            user = new User();
            user.setId(userId);
            user.setUserName("face" + userId);
            user.setNickName("face" + userId);
            user.setAvatar("face" + userId);
            user.setSex(1);
            user.setCreateTime(new Date());
            user.setUpdateTime(new Date());
            user.setIsDel(0);
            user.setIsAdmin(0);
            user.setIsLocked(0);
            user.setIsEnabled(1);
            user.setIsDeleted(0);
            user.setIsSystem(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0);
            user.setIsDefault(0
