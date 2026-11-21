# 15-刷脸登录：功能介绍和人脸注册

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\15-刷脸登录：功能介绍和人脸注册_【海量资源尽在 ubkz.com】.mp4
- 时长 11分45秒（音频 705s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那我们搭建好了环境之后接下来就开始着手去写代码去完成刷脸登录的这个功能那我们在写代码之前呢先简单的来分析一下对于我们来说对于刷脸登录需要我们共同去解决这么五个事情首先第一个事情就是人脸注册那人脸注册其实就是像百度的这个人脸库当中添加我们面部照片的这么一个功能
[00:29] 那这一步我们应该如何去实现其实这个不比较简单在我们之前呢专门讲过用户头像的这么一个功能我们是不是当把用户头像上传成功之后可以顺带着把这个用户的头像给他注册到百度这个仓库当中啊所以对于第一块功能呢不是我们先添加的我们是做一个简单的修改就可以了那做简单修改的时候其实这个代码也比较简单
[00:57] 我们直接可以调用我们刚才封装的一个工具类直接调用其实就可以了好了这个我们一会再说好了那人脸注册我们搞定了之后当然了又一个人脸更新那这个其实就是一个逻辑判断的这么一个情况好了那接着第二件事就是二维码生成二维码生成这个也比较简单我们刚才也自己玩过还有一个二维码检测那二维码检测其实就是在登录页面获取到二维码之后它开启一个定时的一个任务获取一个定时器
[01:24] 通过定时器不断的去在后台去查找看一下当前是否登录了是否有人扫描二维码当然了还有人脸检测还有人脸登录的这些功能OK那我们先来完成第一个功能人脸注册和人脸更新OK那在真正的去实现代码之前我们先来看一下就是这块功能我们应该添加到什么地方更加合适那在这边呢我打开我的浏览器去访问一下我们当前的工程Localhost 8080没问题
[01:56] 进来之后呢先登录那注意这边有一个员工的模块我们可以针对某一个员工进行一个查看比如说我想查看一下ZBZOK查看那过来之后呢各位会发现这边有员工照片的这么一个这么一个接口那对于我们来说呢之前通过青牛云的形式是不是可以把一张照片传递过去啊那接着我想跟各位说的是真正的我们的业务流程是这样的
[02:20] 员工补充自己投箱照片的时候既要把这张照片保存到青牛云同时也应该把这张照片是不是注册到百度云AI它的人脸库当中那当然了注册好了之后比如说你过了两年面部可能发生了一些变化我再去传一张照片是不是对这个照片做一个更新的处理没错吧所以我们应该把这个功能人脸注册或者人脸更新的功能给它放置到上传员工照片的地方
[02:50] 好了我们这个分析过了之后找到我们的代码部分我们之前把这块代码呢写到系统微服务的user Controller当中了user Controller那好了这个user Controller里面Controller层的代码我就不想改它了我要改只改Service当中的内容因为Service才是我们的业务逻辑好了那接下来在Service业务逻辑当中我们要做自己的处理那我们要做什么我就写到上面了
[03:19] 那上传青牛云之后我们还需要将这张图片给他注册到我们的百度云AI人脸库中人脸库中那这个我们应该如何去做呢因为我们传的一个照片它究竟是要对人脸的一个注册还是要对人脸的一个更新这个其实就有点麻烦了没错吧所以在这边我们要做的事情有如下这么几件事
[03:51] 首先第一件事我们需要调用百度云接口那调用这个接口去判断一下当前用户是否已经注册了他这个面部信息那接下来就是做一个分支了如果已注册我们就更新如果未注册我们现在就是注册了这个都能理解没错吧所以接下来我们要完成的就是这个点
[04:23] 那我们要做如何进行处理呢其实也不难我们全部都借助的是百度云的这个工具类所以呢我在这边把百度云那个工具类给它依赖注入进来atoutwareprivate百度云AIutilok百度云AIutil那注册进来之后在百度云AI当中我们需要补充一个方法我就写到上边了这个方法呢就是判断用户是否已经
[04:55] 注册了面部信息好了这个如何去做呢其实比较简单我就来一个布林类型的一个返回值了来一个叫做 faceexist ok做一个判断用户头像是否存在的那这边呢我们要借助的是百度云ai的他的一个方法那client打点注意这个方法呢叫做 get userget userget user需要传递三个参数第一个用户 id 第二个
[05:31] 组ID第三个是你的一些配置当然我们这个设置呢用空就用None即可第三个参数用None好了接下来呢我们需要两个参数第一个User ID第二个代表的是我们Group ID那User ID你需要给我传递过来所以我补充一个请求的这么一个参数User ID传过来那Group ID想都不要想我们之前呢已经把它抽取到上边了OK那这样一来呢我们就能得到相应的一个返回值IS
[06:03] 那这个返回值呢我需要跟各位做一个声明如果返回它的返回值的error code它其实有一个叫做error code这么一个编码这个error code呢如果是0代表存在如果不是0代表不存在如果非0它其实代表的就是不存在了所以对于我们来说很简单直接从返回值当中得到error code接着做判断跟这个逻辑基本上是一样的如果
[06:44] 反回值的0说明已经有了如果反回值不等于0说明没有这个都能理解吧好了那接下来呢我们就第一个方法已经写好了第一个方法写好了之后调用注册或者调用更新嘛如果触注册如果触如果触是不是应该要更新啊触是不是应该有啊OK那好了接着我们回到思维的部分那在这边呢在返回之前我就写到上边了把这代码呢做一个简单的修改好了我们要做的事情可以借助百度云
[07:14] util进行判断已经注册面部信息OK百步云util打点来一个exist判断那user id传递过去直接就id了user id传递过去OK那开始判断if如果存在我们调用更新的方法else那不存在我们采用注册的方法所以这个里面我们应该是更新底下这个我们应该是注册
[07:51] 能理解吧那接下来呢就是说注册或者更新全部介入百度云i utils打点解里面的方法就可以了上面呢应该是更新所以是updateID拿过来好了底下呢打点registerID拿过来那接下来我想跟各位来聊的不管是注册或者是我们的更新操作第二个参数是不是都应该是这张图片的经过base64编码处理的这么一个值啊所以对于我们
[08:23] 第二个参数而言我们可以构造一个四进base64等于那如何处理呢我们之前写这个代码呢其实自己也写过就是base64接着对你传递的流信息进行一个编码处理即可所以这边直接拿到第二个参数拿到第二个参数就可以了OK那这样一来我这个逻辑咱们也已经写好了写好了之后呢注意我去重新启动一下
[08:54] 我这个系统为服务OK这个系统为服务让它去重新启动我们回到我们的浏览器那接着这边呢我需要打开百度云添爱它的一个人脸库我们一起来看一下cloud.baidu.com好了这边呢我需要登录了一下我的管理控制台OK我已经登录成功了这边呢找到我们的人工智能找到人脸识别
[09:34] 我的应用呢一共有两个我们一起来看一下那注意啊我刚才跟各位演示的这个案例呢是以底下这个人脸库举例的IHM那各位可以看到就是目前来说呢这边呢抱歉要看他的人脸库啊这个网络有点慢啊各位可以看一下他的人脸库这人脸库呢把所有的人脸全部放到ITcast这个组下了目前来说一个都没有那一个都没有我去
[10:04] 来张图片传上去是不是代表的应该是注册没错吧所以接下来呢我去重新的搞一张图片我就拿我们今天的这个资料第11天资源照片好了我就用01来举例各位来看01我换了一张新的图片过来那换了一张图片过来之后注意我刷新一下先来看一下是否已经存到新牛云刷新各位来看
[10:34] 确确实实从七星云获取到的图片信息那接着我们来看一下这个百度云好了百度云当中的人脸库看一下有没有各位来看现在呢已经换了这么一张图片了就是我们刚才传到的这张已经注册过来了那接下来呢我们来看一下人脸的一个更新那重新换一张图片好了我就用003吧好了003呢这边呢已经替换好了替换好了之后我再去刷新一下各位来看
[11:06] 这个网络有点慢啊各位现在的图片已经上传到青春云了没错吧所以它能够显示出来嘛那接下来来看一下百度云管理中心它有没有进行替换再去刷新各位来看还是一张人脸我们进来观察一下它的图片你会发现是不是这张图片也发生了一个变化呀那这样一来我们整个的头像注册和头像更新的这个操作其实我们就已经写好了其实这边呢就多了一个处理判断了一下
[11:39] 是否它具有面部信息就多了这么一个我们的方法而已OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 iHRM 系统中实现人脸登录功能的前后端代码逻辑，包括用户注册、二维码生成、人脸检测与登录等环节。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 页面“4.5 功能实现”，内容包括人脸注册、二维码生成、二维码检测、人脸检测、人脸登录五个步骤。
画面 2: 展示 iHRM 后台登录页面，包含用户名、密码输入框和登录按钮。
画面 3: 在 IntelliJ IDEA 中展示 UserServic.java 文件，代码片段为上传图片到七牛云的逻辑。
画面 4: 在 IntelliJ IDEA 中展示 UserServic.java 文件，代码片段为上传图片到七牛云的逻辑，注释部分显示“上传到七牛云存储”、“注册到百度云AI人脸库”、“判断当前用户是否已经注册”、“已注册，更新”、“未注册，注册”。
画面 5: 在 IntelliJ IDEA 中展示 BaiduAIIUtil.java 文件，代码片段为人脸注册方法，使用百度AI接口。
画面 6: 在 IntelliJ IDEA 中展示 BaiduAIIUtil.java 文件，代码片段为初始化百度AI客户端和人脸注册方法。
画面 7: 在 IntelliJ IDEA 中展示 UserServic.java 文件，代码片段为上传图片并调用百度AI接口进行人脸注册。
画面 8: 在 IntelliJ IDEA 中展示 UserServic.java 文件，代码片段为上传图片并调用百度AI接口进行人脸注册，注释部分显示“判断是否已经注册”、“更新”、“注册”、“返回”。
画面 9: 展示浏览器地址栏输入“Swagger UI”，页面显示 Google 搜索结果。
画面 10: 展示百度AI人脸识别控制台，页面显示“产品概览”、“应用”、“用量”等信息。
画面 11: 展示 iHRM 系统员工详情页面，包含员工照片和基础信息表单。
画面 12: 展示百度AI人脸识别控制台，页面显示“/itcast”路径和“+ 新增用户”按钮。
画面 13: 展示 iHRM 系统登录用户设置页面，包含用户名、密码输入框和“更新”、“取消”按钮。
画面 14: 在 IntelliJ IDEA 中展示 UserServic.java 文件，代码片段为上传图片并调用百度AI接口进行人脸注册，注释部分显示“判断是否已经注册”、“更新”、“注册”、“返回”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3 代码：
```java
public String uploadImage(String id, MultipartFile file) throws IOException {
    User user = userDao.findById(id).get();
    String imgUrl = new QiniuUploadUtil().upload(user.getId(), file.getBytes());
    user.setStaffPhoto(imgUrl);
    userDao.save(user);
    return imgUrl;
}
```

画面 4 代码：
```java
public String uploadImage(String id, MultipartFile file) throws IOException {
    User user = userDao.findById(id).get();
    String imgUrl = new QiniuUploadUtil().upload(user.getId(), file.getBytes());
    user.setStaffPhoto(imgUrl);
    userDao.save(user);
    return imgUrl;
}
```

画面 5 代码：
```java
public Boolean faceRegister(String userId, String image) {
    // 人脸注册
    JSONObject res = client.addUser(image, IMAGE_TYPE, groupId, userId, options);
    Integer errorCode = res.getInt(key: "error_code");
    return errorCode == 0 ? true : false;
}
```

画面 6 代码：
```java
private AiFace client;
private HashMap<String, String> options = new HashMap<>();
public BaiDuAIIUtil() {
    options.put("quality_control", "NORMAL");
    options.put("liveness_control", "LOW");
}
@PostConstruct
public void init() { client = new AiFace(APP_ID, API_KEY, SECRET_KEY); }
// 判断用户是否已经注册了人脸信息
public Boolean faceExist(String userId) {
    // 返回错误码
    JSONObject res = client.getUser(userId, groupId, options);
    return res.getInt(key: "error_code") == 0 ? true : false;
}
```

画面 7 代码：
```java
public String up
    // 1. 上传图片
    // 2. 判断是否已经注册
    // 3. 已注册，更新
    // 4. 未注册，注册
    // 5. 返回
    // 上传图片，图片的byte数组
    // 判断是否已经注册
    // 更新
    // 注册
    // 返回
```

画面 8 代码：
```java
public String uploadImage(String id, MultipartFile file) throws IOException {
    User user = userDao.findById(id).get();
    String imgUrl = new QiniuUploadUtil().upload(user.getId(), file.getBytes());
    user.setStaffPhoto(imgUrl);
    userDao.save(user);
    return imgUrl;
}
// 判断是否已经注册
Boolean aBoolean = baiduAiiUtil.faceExist(id);
if (aBoolean) {
    // 更新
    baiduAiiUtil.faceUpdate(id, imgBase64);
} else {
    // 注册
    baiduAiiUtil.faceRegister(id, imgBase64);
}
// 返回
return imgUrl;
```

画面 14 代码：
```java
public String uploadImage(String id, MultipartFile file) throws IOException {
    User user = userDao.findById(id).get();
    String imgUrl = new QiniuUploadUtil().upload(user.getId(), file.getBytes());
    user.setStaffPhoto(imgUrl);
    userDao.save(user);
    return imgUrl;
}
// 判断是否已经注册
Boolean aBoolean = baiduAiiUtil.faceExist(id);
if (aBoolean) {
    // 更新
    baiduAiiUtil.faceUpdate(id, imgBase64);
} else {
    // 注册
    baiduAiiUtil.faceRegister(id, imgBase64);
}
// 返回
return imgUrl;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1 PPT 标题：“4.5 功能实现”，内容包括：
- 人脸注册/人脸更新
- 二维码生成
- 二维码检测
- 人脸检测
- 人脸登录

画面 10 百度AI人脸识别控制台页面标题：“产品概览 / 人脸识别 - 概览”，包含“应用”、“用量”等信息。

画面 12 百度AI人脸识别控制台页面标题：“/itcast”，包含“+ 新增用户”按钮。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

