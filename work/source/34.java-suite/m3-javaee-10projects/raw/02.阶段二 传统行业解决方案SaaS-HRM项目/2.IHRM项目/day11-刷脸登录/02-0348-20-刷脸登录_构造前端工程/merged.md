# 20-刷脸登录：构造前端工程

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\20-刷脸登录：构造前端工程_【海量资源尽在 ubkz.com】.mp4
- 时长 7分35秒（音频 455s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了人脸登录呢这个功能我们已经做好了那接下来我们重新启动一下系统为服务做一个简单的测试的一个工作好了这边让服务去重启我打开postman新起一个标签页好了前面这段我就call一下了control c这边call过来control v那我们现在请求的这个接口呢上边代表的是请求路径那我们这边呢还有一个就是你需要把
[00:31] code给我传递过来那我们的code在哪边我也大胆的去抄一下就在这Ctrl C也靠过来Ctrl V注意Ctrl V那么的请求方式各位来看是一个pose请求并且呢把一张图片给我传递过来那pose的请求好了这边添加上图片箱的内容feel代表的是我这个图片的名称也能对应上那接下来我们这个图片用什么呢是刚才我们不是有一个人脸注册是不是注册到一个仓库当中了
[01:01] 那我们注册的是001其实之前我们看过001和002显然都是同一个人001和002显然都是同一个人那003显然就不是同一个人了所以我这边呢就是借助002跟003来进行这么一个登录所以我这边把002传递上来那传递上来之后它内部经过对比是不是会给我返回一个登录成功的这么一个状态没错吧好了那接着我们一起来试一下走
[01:35] 各位这边报了一个错误那咱们一起来看一下我这个代码好了找到代码部分这边告诉我第76行出错了是Service第76行我们一起来看一下Service第76行好了在这儿这边报了一个错误是userdo我们看抱歉这userdo应该是autoware依赖注入起来OK好了这边再去重新启动一下
[02:06] 好了这边让他耐心等待重启成功我们一会儿再来做一个简单的测试这边应该启动的差不多了还是刚才这个逻辑还是刚才这个逻辑唯一标志然后这边是我传递的一个002图片好了接着点击send发起请求好了这边还没启动成功再走OK各位来看现在告诉我操作成功了那操作成功了之后注意操作成功了之后那我别忘了我还有一个接口
[02:39] 那还有一个接口是干嘛的呢我们可以打开这张图形一起来看是不是我们用户登录了之后这边有一个轮旬查询的这么一个工作它不断的在轮旬查询当我刚刚生成的时候你查询的状态你查询的这个状态是不是代表的是负一代表的是一个叫做失败的一个状态代表是刚刚生成还没有扫描的一个状态那我现在这边登录成功了那状态是不是就应该给我改成一并且可以得到用户ID并且可以得到token
[03:10] 那得到token之后页面是不是再去进行一个跳转进首页的这么一个操作那所以我们先来看一下能否得到token能否得到user id那好我们回到这边我们之前get方式进行了一个检索查询的这么一个方法好了接着再send这边body给我来看告诉我操作成功并且有user id有token状态也是1那如果说我这边选择的是003这张图片我们都知道001跟003不是一个人
[03:40] 所以我一点send你会发现操作失败这就相当于我用户拿开手机扫描扫描发现不是一个人没找到这个人就告诉我失败了你重新的再去拍摄一张照片OK那如果失败的话我这边再去轮旬检测的话你会发现这回就不是0这回就不是1也不是-1变成了0了变成0代表的含义是什么不言而喻登录失败所以我这回页面部分不做任何的处理
[04:10] 能理解吧OK那其实呢我们的后端代码部分呢全部都已经完成了那接下来我们关注的就是连接到前端我们把这个整个工程跑起来看一下它的一个效果那首先呢我这边前端工程已经给各位展示到这边了那要想去快速的让这个前端工程可以正常的启动起来在今天资料当中已经把前端工程所要用到的所有的代码资源
[04:43] 给各位准备好了那对于我们而言直接拿到里面的代码一个一个的进行拷贝即可好了那我们开始去构造全端相关的内容好了进入到我们这边准备好的一些资料首先呢就是说我这边的路由呢要做一个简单的配置好了Ctrl C直接call过来替换我们这边总路由的一个配置Src下找到router找到index.js
[05:12] 在最上方有一个白名单无需跳转的OK进行替换那接下来还需要一个路由的配置这个路由的配置Ctrl C也拷过来放到中间部分即可那我解释一下这个路由是在做什么是这样的就是说呢在用户扫描之后它要进行一个页面跳转那这个跳转是前端提供的一个页面所以要进行一个路由的配置并且这个页面不需要经过登录
[05:38] 就这么一个含义OK好了这个路由我们搞定了之后还有这么两块内容一个是一个login.Vue的这么一个界面login.Vue的这个界面那这个界面要放到哪合适呢注意要放到我们model第一个当中这个里面的配置私目录下因为我的页面要login页面要做一个简单的改造我们之前的login页面咱们也看到过OK这边
[06:11] 我配了一个路由现在这个页面没有啊我们一会儿再说吧好了还少一个先把这个login页面呢也给它copy过来右键资源管理器当中显示替换那除了这个login页面之外呢还有一个页面就是说我们就是一个落地页嘛这个落地也给各位准备好了那这个落地页呢我跟这个API这里面这个写到一起了其实这个落地页face logincontrol c也需要给它拿过来
[06:43] 靠到哪呢和我们这个login页面呢给它放到一起即可那这样一来两个页面都准备好了当然还有最后一个就是一个face login.js这是我们前端的一个API那前端的API把它放到哪放到我们这边src下APIbase当中control v那这样一来我前端就已经都构建好了
[07:06] 那其实还是跟之前一样我们这个不注重前端的一个代码开发我们主要是前端连横后端看我们的后端页目的一个写一个编写OK那这些我们都准备好了之后再去刷新一下页面那各位会发现我这边已经具备了刷脸登录的这么一个功能并且呢我这边刷脸登录呢还可以点击弹出这个二维码OK那这样一来我们前端的这个界面其实也已经准备好了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
- 文件夹内包含 `facelogin.Vue` 和 `facelogin.js` 两个文件。

画面 13：
- 显示 Windows 资源管理器中 `api/base` 目录下的 `facelogin.js` 和 `facelogin.Vue` 两个文件。
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

